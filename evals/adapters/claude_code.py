#!/usr/bin/env python3
"""Run one pilot response through an isolated Claude Code/Bedrock process."""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
import signal
import shutil
import subprocess
import sys
import tempfile


MODEL = os.environ.get("PILOT_CLAUDE_MODEL", "").strip()
ADAPTER_TIMEOUT = int(os.environ.get("PILOT_ADAPTER_TIMEOUT", "285"))
MODEL_ALIASES = {"haiku", "sonnet", "opus", "fable"}
UMBRELLA_SKILLS = frozenset(
    {
        "ping-app-integration",
        "ping-foundation",
        "ping-identity-for-ai",
        "ping-orchestration",
        "ping-quickstart",
        "ping-universal-services",
    }
)
PASSTHROUGH_ENV = frozenset(
    {
        "ANTHROPIC_API_KEY",
        "ANTHROPIC_AUTH_TOKEN",
        "ANTHROPIC_BASE_URL",
        "AWS_ACCESS_KEY_ID",
        "AWS_BEARER_TOKEN_BEDROCK",
        "AWS_CA_BUNDLE",
        "AWS_CONFIG_FILE",
        "AWS_DEFAULT_REGION",
        "AWS_PROFILE",
        "AWS_REGION",
        "AWS_SDK_LOAD_CONFIG",
        "AWS_SECRET_ACCESS_KEY",
        "AWS_SESSION_TOKEN",
        "AWS_SHARED_CREDENTIALS_FILE",
        "CLAUDE_CODE_USE_BEDROCK",
        "CLAUDE_CODE_USE_FOUNDRY",
        "CLAUDE_CODE_USE_VERTEX",
        "GOOGLE_APPLICATION_CREDENTIALS",
        "HTTPS_PROXY",
        "HTTP_PROXY",
        "LANG",
        "LC_ALL",
        "LC_CTYPE",
        "NO_PROXY",
        "NODE_EXTRA_CA_CERTS",
        "PATH",
        "SHELL",
        "SSL_CERT_FILE",
        "TERM",
    }
)
SANDBOX_DENY_READ = ("~/", "/tmp", "/private/tmp", "/var/folders", "/private/var/folders")
PING_DOC_DOMAINS = ("docs.pingidentity.com", "developer.pingidentity.com")


def fail(message: str, code: int = 2) -> int:
    print(f"pilot Claude adapter: {message}", file=sys.stderr)
    return code


def discover_skills(root: Path) -> list[tuple[str, Path]]:
    skills: list[tuple[str, Path]] = []
    seen_paths: set[Path] = set()
    seen_names: set[str] = set()
    for current, dirs, files in os.walk(root, followlinks=True):
        dirs.sort()
        if "SKILL.md" not in files:
            continue
        skill_file = Path(current) / "SKILL.md"
        resolved = skill_file.resolve()
        if resolved in seen_paths:
            dirs[:] = []
            continue
        content = skill_file.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"(?m)^name:\s*[\"']?([^\"'\n]+)", content)
        name = (match.group(1).strip() if match else Path(current).name).replace("/", "-")
        if name in seen_names:
            raise RuntimeError(f"duplicate skill name {name!r}")
        seen_names.add(name)
        seen_paths.add(resolved)
        skills.append((name, Path(current).absolute()))
        dirs[:] = []
    return sorted(skills)


def sum_model_usage(model_usage: dict[str, object], key: str) -> int:
    total = 0
    for value in model_usage.values():
        if isinstance(value, dict) and isinstance(value.get(key), int):
            total += int(value[key])
    return total


def redacted(value: str, environment: dict[str, str]) -> str:
    """Remove credential-like environment values before persisting provider output."""
    result = value
    for name, secret in environment.items():
        if (
            len(secret) >= 8
            and any(marker in name for marker in ("KEY", "TOKEN", "SECRET", "AUTH"))
        ):
            result = result.replace(secret, f"[REDACTED:{name}]")
    return result


def terminate_process_group(process: subprocess.Popen[str]) -> None:
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except (ProcessLookupError, PermissionError):
        process.kill()


def expected_skill_names(condition_id: str) -> set[str]:
    if condition_id not in {"A", "B"}:
        raise ValueError(f"unsupported condition {condition_id!r}")
    result = set(UMBRELLA_SKILLS)
    if condition_id == "B":
        result.add("ping-docs")
    return result


def filtered_environment(environment: dict[str, str]) -> dict[str, str]:
    return {
        name: environment[name]
        for name in PASSTHROUGH_ENV
        if name in environment
    }


def build_claude_settings(
    host_home: Path | None, sandbox_deny_read: tuple[str, ...]
) -> dict[str, object]:
    return {
        "permissions": {
            "allow": [
                "Skill",
                "Read",
                "Bash",
                "WebSearch",
                *[f"WebFetch(domain:{domain})" for domain in PING_DOC_DOMAINS],
            ],
            "deny": [
                "Edit",
                "Write",
                "NotebookEdit",
                *(
                    [f"Read(/{host_home.as_posix()}/**)"]
                    if host_home is not None
                    else []
                ),
            ],
        },
        "sandbox": {
            "enabled": True,
            "failIfUnavailable": True,
            "autoAllowBashIfSandboxed": True,
            "allowUnsandboxedCommands": False,
            "excludedCommands": [],
            "filesystem": {
                "denyRead": list(sandbox_deny_read),
                "allowRead": ["."],
            },
            "network": {"allowedDomains": list(PING_DOC_DOMAINS)},
        },
    }


def main() -> int:
    required = [
        "PILOT_WORKSPACE",
        "PILOT_SKILLS_DIR",
        "PILOT_METADATA_FILE",
        "PILOT_CONDITION_ID",
    ]
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        return fail("missing environment variables: " + ", ".join(missing))
    if not MODEL:
        return fail("PILOT_CLAUDE_MODEL must name an explicit, pinned model")
    if MODEL.casefold() in MODEL_ALIASES:
        return fail(f"PILOT_CLAUDE_MODEL must be pinned; mutable alias {MODEL!r} is not allowed")

    workspace = Path(os.environ["PILOT_WORKSPACE"]).absolute()
    skills_root = Path(os.environ["PILOT_SKILLS_DIR"]).absolute()
    metadata_file = Path(os.environ["PILOT_METADATA_FILE"]).absolute()
    condition_id = os.environ["PILOT_CONDITION_ID"]
    prompt = sys.stdin.read()
    if not prompt.strip():
        return fail("received an empty prompt")

    try:
        skills = discover_skills(skills_root)
    except (OSError, RuntimeError) as exc:
        return fail(str(exc))
    try:
        expected_skills = expected_skill_names(condition_id)
    except ValueError as exc:
        return fail(str(exc))
    actual_skills = {name for name, _ in skills}
    if actual_skills != expected_skills:
        return fail(
            f"condition {condition_id} skill inventory mismatch; "
            f"missing={sorted(expected_skills - actual_skills)}, "
            f"unexpected={sorted(actual_skills - expected_skills)}"
        )

    runtime_root = Path(tempfile.mkdtemp(prefix="ping-pilot-claude-"))
    agent_workspace = runtime_root / "workspace"
    isolated_home = runtime_root / "home"
    config_dir = runtime_root / "config"
    temp_dir = runtime_root / "tmp"
    agent_workspace.mkdir(parents=True)
    isolated_home.mkdir()
    config_dir.mkdir()
    temp_dir.mkdir()
    host_home = Path(os.environ["HOME"]).resolve() if os.environ.get("HOME") else None
    sandbox_deny_read = tuple(
        dict.fromkeys(
            [
                *SANDBOX_DENY_READ,
                *([str(host_home)] if host_home is not None else []),
            ]
        )
    )

    project_skills = agent_workspace / ".claude" / "skills"
    project_skills.mkdir(parents=True)
    resolved_sources: dict[str, Path] = {}
    try:
        for name, source in skills:
            resolved_sources[name] = source.resolve()
            shutil.copytree(source, project_skills / name, symlinks=False)
    except OSError as exc:
        shutil.rmtree(runtime_root, ignore_errors=True)
        return fail(f"could not copy assigned skills into the isolated workspace: {exc}")

    if "ping-docs" in resolved_sources:
        standalone = resolved_sources["ping-docs"] / "references" / "docsets"
        candidate = (
            standalone
            if standalone.is_dir()
            else resolved_sources["ping-docs"].parents[1] / "skills"
        )
        if not candidate.is_dir():
            shutil.rmtree(runtime_root, ignore_errors=True)
            return fail(f"could not locate deep-doc data root from {resolved_sources['ping-docs']}")
        isolated_data_root = agent_workspace / ".ping-docs-data"
        try:
            shutil.copytree(candidate, isolated_data_root, symlinks=False)
        except OSError as exc:
            shutil.rmtree(runtime_root, ignore_errors=True)
            return fail(f"could not copy deep-doc data into the isolated workspace: {exc}")
    else:
        isolated_data_root = None

    claude_settings = build_claude_settings(host_home, sandbox_deny_read)
    settings_file = agent_workspace / ".claude" / "settings.json"
    settings_file.write_text(json.dumps(claude_settings, indent=2) + "\n", encoding="utf-8")

    inventory = {
        "condition_id": condition_id,
        "skills_root": str(skills_root),
        "skills": [
            {"name": name, "source": str(resolved_sources[name])} for name, _ in skills
        ],
        "model": MODEL,
        "agent_workspace_isolated": True,
        "user_home_isolated": True,
        "filesystem_sandbox": True,
        "sandbox_fail_if_unavailable": True,
        "sandbox_allow_unsandboxed_commands": False,
        "sandbox_denied_read_roots": list(sandbox_deny_read),
        "direct_file_tools": ["Read"],
        "provider_bundled_skills_disabled": True,
        "subprocess_credentials_scrubbed": True,
        "mcp_servers": [],
        "setting_sources": ["explicit", "project"],
    }
    command = [
        shutil.which("claude") or "claude",
        "--print",
        "--verbose",
        "--output-format",
        "stream-json",
        "--no-session-persistence",
        "--setting-sources",
        "project",
        "--settings",
        str(settings_file),
        "--strict-mcp-config",
        "--mcp-config",
        '{"mcpServers":{}}',
        "--no-chrome",
        "--allowedTools=Skill,Read,Bash,WebFetch,WebSearch",
        "--tools=Skill,Read,Bash,WebFetch,WebSearch",
        "--model",
        MODEL,
    ]
    child_env = filtered_environment(dict(os.environ))
    child_env["HOME"] = str(isolated_home)
    child_env["CLAUDE_CONFIG_DIR"] = str(config_dir)
    child_env["TMPDIR"] = str(temp_dir)
    child_env["XDG_CONFIG_HOME"] = str(config_dir)
    child_env["CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS"] = "1"
    child_env["CLAUDE_CODE_DISABLE_AUTO_MEMORY"] = "1"
    child_env["CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"] = "1"
    child_env["CLAUDE_CODE_DISABLE_BUNDLED_SKILLS"] = "1"
    child_env["CLAUDE_CODE_DISABLE_CLAUDE_MDS"] = "1"
    child_env["CLAUDE_CODE_SKIP_PROMPT_HISTORY"] = "1"
    child_env["CLAUDE_CODE_SUBPROCESS_ENV_SCRUB"] = "1"
    if isolated_data_root is not None:
        child_env["PING_DOCS_DATA_ROOT"] = str(isolated_data_root)
    (config_dir / ".claude.json").write_text(
        json.dumps(
            {
                "projects": {
                    str(agent_workspace.resolve()): {"hasTrustDialogAccepted": True}
                }
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    inventory["child_environment_keys"] = sorted(child_env)
    (workspace / "adapter-inventory.json").write_text(
        json.dumps(inventory, indent=2) + "\n", encoding="utf-8"
    )

    try:
        process = subprocess.Popen(
            command,
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=child_env,
            cwd=agent_workspace,
            start_new_session=True,
        )
        try:
            stdout, stderr = process.communicate(prompt, timeout=ADAPTER_TIMEOUT)
        except subprocess.TimeoutExpired:
            terminate_process_group(process)
            stdout, stderr = process.communicate()
            (workspace / "adapter-claude-events.jsonl").write_text(
                redacted(stdout, child_env), encoding="utf-8"
            )
            (workspace / "adapter-claude-stderr.txt").write_text(
                redacted(stderr, child_env), encoding="utf-8"
            )
            return fail(f"Claude exceeded the adapter timeout of {ADAPTER_TIMEOUT} seconds", 124)
        except (KeyboardInterrupt, SystemExit):
            terminate_process_group(process)
            process.communicate()
            raise
        returncode = process.returncode
    finally:
        shutil.rmtree(runtime_root, ignore_errors=True)

    (workspace / "adapter-claude-events.jsonl").write_text(
        redacted(stdout, child_env), encoding="utf-8"
    )
    (workspace / "adapter-claude-stderr.txt").write_text(
        redacted(stderr, child_env), encoding="utf-8"
    )
    if stderr:
        print(redacted(stderr, child_env), file=sys.stderr, end="")

    final_event: dict[str, object] | None = None
    tool_names: list[str] = []
    invoked_skills: list[str] = []
    runtime_skills: list[str] = []
    parse_errors: list[str] = []
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            parse_errors.append(line[:200])
            continue
        if event.get("type") == "result":
            final_event = event
        if event.get("type") == "system" and event.get("subtype") == "init":
            announced = event.get("skills")
            if isinstance(announced, list):
                runtime_skills = [str(value) for value in announced]
        message = event.get("message")
        if event.get("type") == "assistant" and isinstance(message, dict):
            content = message.get("content")
            if isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "tool_use":
                        tool_name = str(block.get("name", "unknown"))
                        tool_names.append(tool_name)
                        tool_input = block.get("input")
                        if tool_name == "Skill" and isinstance(tool_input, dict):
                            skill_name = tool_input.get("skill")
                            if isinstance(skill_name, str):
                                invoked_skills.append(skill_name)

    if returncode != 0 or final_event is None or final_event.get("is_error"):
        if parse_errors:
            print(
                redacted("unparsed Claude output: " + " | ".join(parse_errors), child_env),
                file=sys.stderr,
            )
        if stdout:
            print(redacted(stdout, child_env), file=sys.stderr, end="")
        return returncode or 1
    if not actual_skills.issubset(runtime_skills):
        return fail(
            "Claude runtime did not announce every assigned skill; "
            f"missing={sorted(actual_skills - set(runtime_skills))}",
            1,
        )

    result = final_event.get("result")
    if not isinstance(result, str) or not result.strip():
        return fail("Claude returned no final answer", 1)

    model_usage = final_event.get("modelUsage")
    if not isinstance(model_usage, dict):
        model_usage = {}
    input_tokens = sum_model_usage(model_usage, "inputTokens")
    cache_read_tokens = sum_model_usage(model_usage, "cacheReadInputTokens")
    cache_creation_tokens = sum_model_usage(model_usage, "cacheCreationInputTokens")
    output_tokens = sum_model_usage(model_usage, "outputTokens")
    permission_denials = final_event.get("permission_denials")
    if not isinstance(permission_denials, list):
        permission_denials = []

    metadata = {
        "condition_id": condition_id,
        "loaded_skill_roots": [str(skills_root)],
        "loaded_skills": sorted(actual_skills & set(runtime_skills)),
        "filesystem_sandbox": True,
        "sandbox_fail_if_unavailable": True,
        "sandbox_allow_unsandboxed_commands": False,
        "direct_file_tools": ["Read"],
        "provider_bundled_skills_disabled": True,
        "subprocess_credentials_scrubbed": True,
        "mcp_servers": [],
        "child_environment_keys": sorted(child_env),
        "model": MODEL,
        "resolved_models": sorted(model_usage),
        "tool_calls": len(tool_names),
        "tool_names": tool_names,
        "invoked_skills": invoked_skills,
        "runtime_builtin_skills": sorted(
            set(runtime_skills) - {name for name, _ in skills}
        ),
        "runtime_announced_skills": sorted(runtime_skills),
        "input_tokens": input_tokens + cache_read_tokens + cache_creation_tokens,
        "uncached_input_tokens": input_tokens,
        "cached_input_tokens": cache_read_tokens,
        "cache_creation_input_tokens": cache_creation_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + cache_read_tokens + cache_creation_tokens + output_tokens,
        "cost_usd": final_event.get("total_cost_usd"),
        "permission_denials": permission_denials,
    }
    metadata_file.parent.mkdir(parents=True, exist_ok=True)
    metadata_file.write_text(
        redacted(json.dumps(metadata, indent=2) + "\n", child_env),
        encoding="utf-8",
    )
    print(redacted(result, child_env))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

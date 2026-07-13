#!/usr/bin/env python3
"""Run the Ping Agent Skills A/B pilot with a provider-supplied agent command."""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import random
import re
import shlex
import shutil
import subprocess
import sys
import time
from typing import Any, Iterable


EVALS_DIR = Path(__file__).resolve().parent
DEFAULT_MANIFEST = EVALS_DIR / "pilot.json"
DEFAULT_CASES = EVALS_DIR / "cases.json"
DEFAULT_RESULTS = EVALS_DIR / "results"
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
SKILL_NAME = re.compile(r"(?m)^name:\s*[\"']?([^\"'\n]+)")


class PilotError(RuntimeError):
    """Raised for a pilot configuration or protocol error."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PilotError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise PilotError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise PilotError(f"Expected a JSON object in {path}")
    return value


def canonical_json_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def default_run_id() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def ensure_safe_id(value: str, label: str) -> None:
    if not SAFE_ID.fullmatch(value):
        raise PilotError(f"Unsafe {label} {value!r}; use letters, digits, dot, underscore, or hyphen")


def validate_inputs(manifest: dict[str, Any], cases_doc: dict[str, Any]) -> None:
    if manifest.get("schema_version") != 1:
        raise PilotError("pilot manifest schema_version must be 1")
    if cases_doc.get("schema_version") != 1:
        raise PilotError("case suite schema_version must be 1")
    for flag in ("require_isolation_metadata", "require_filesystem_sandbox_metadata"):
        if flag in manifest and not isinstance(manifest[flag], bool):
            raise PilotError(f"pilot manifest {flag} must be a boolean")
    if manifest.get("require_filesystem_sandbox_metadata") and not manifest.get(
        "require_isolation_metadata"
    ):
        raise PilotError(
            "require_filesystem_sandbox_metadata requires require_isolation_metadata"
        )

    conditions = manifest.get("conditions")
    cases = cases_doc.get("cases")
    if not isinstance(conditions, list) or len(conditions) != 2:
        raise PilotError("pilot manifest must define exactly two conditions")
    if not isinstance(cases, list) or not cases:
        raise PilotError("case suite must define a non-empty cases list")

    condition_ids: set[str] = set()
    for condition in conditions:
        if not isinstance(condition, dict) or not isinstance(condition.get("id"), str):
            raise PilotError("each condition must be an object with a string id")
        condition_id = condition["id"]
        ensure_safe_id(condition_id, "condition id")
        if condition_id in condition_ids:
            raise PilotError(f"duplicate condition id: {condition_id}")
        condition_ids.add(condition_id)
        if not isinstance(condition.get("assets"), list):
            raise PilotError(f"condition {condition_id} must define assets")
        for asset in condition["assets"]:
            if not isinstance(asset, dict) or not asset.get("mount"):
                raise PilotError(f"condition {condition_id} has an invalid asset")
            mount = Path(str(asset["mount"]))
            if mount.is_absolute() or ".." in mount.parts:
                raise PilotError(f"condition {condition_id} asset mount escapes workspace: {mount}")

    case_ids: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            raise PilotError("each case must be a JSON object")
        case_id = case.get("id")
        if not isinstance(case_id, str):
            raise PilotError("each case must have a string id")
        ensure_safe_id(case_id, "case id")
        if case_id in case_ids:
            raise PilotError(f"duplicate case id: {case_id}")
        case_ids.add(case_id)
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            raise PilotError(f"case {case_id} has no prompt")
        answer_key = case.get("answer_key")
        if not isinstance(answer_key, dict):
            raise PilotError(f"case {case_id} has no answer_key")
        if answer_key.get("expected_behavior") not in {"answer", "clarify", "decline"}:
            raise PilotError(f"case {case_id} has invalid expected_behavior")


def selected_items(items: list[dict[str, Any]], requested: list[str], label: str) -> list[dict[str, Any]]:
    by_id = {item["id"]: item for item in items}
    if not requested or requested == ["all"]:
        return list(items)
    missing = [item_id for item_id in requested if item_id not in by_id]
    if missing:
        raise PilotError(f"Unknown {label}: {', '.join(missing)}")
    return [by_id[item_id] for item_id in requested]


def resolve_asset_source(asset: dict[str, Any], manifest_dir: Path) -> Path:
    if asset.get("source_env"):
        name = str(asset["source_env"])
        value = os.environ.get(name)
        if not value:
            raise PilotError(f"Required environment variable {name} is not set")
        source = Path(os.path.expandvars(os.path.expanduser(value)))
    elif asset.get("source"):
        raw = os.path.expandvars(os.path.expanduser(str(asset["source"])))
        source = Path(raw)
        if not source.is_absolute():
            source = manifest_dir / source
    else:
        raise PilotError(f"Asset {asset.get('id', '<unnamed>')} has neither source nor source_env")
    source = source.absolute()
    if not source.exists():
        raise PilotError(f"Asset source does not exist: {source}")
    for entry in asset.get("required_entries", []):
        if not (source / str(entry)).exists():
            raise PilotError(f"Asset {asset.get('id')} is missing required entry {entry}: {source}")
    if asset.get("forbid_additional_skills"):
        expected = {str(entry) for entry in asset.get("required_entries", [])}
        found = {
            child.name
            for child in source.iterdir()
            if child.is_dir() and (child / "SKILL.md").is_file()
        }
        unexpected = sorted(found - expected)
        if unexpected:
            raise PilotError(
                f"Asset {asset.get('id')} contains additional skills not allowed in this condition: "
                + ", ".join(unexpected)
            )
    return source


def asset_inventory(condition: dict[str, Any], manifest_dir: Path) -> list[dict[str, Any]]:
    inventory: list[dict[str, Any]] = []
    for asset in condition["assets"]:
        source = resolve_asset_source(asset, manifest_dir)
        inventory.append(
            {
                "id": asset.get("id"),
                "source": str(source),
                "mount": str(asset["mount"]),
                "mode": asset.get("mode", "symlink"),
            }
        )
    return inventory


def mount_assets(workspace: Path, inventory: list[dict[str, Any]]) -> None:
    for asset in inventory:
        target = workspace / asset["mount"]
        target.parent.mkdir(parents=True, exist_ok=True)
        source = Path(asset["source"])
        mode = asset["mode"]
        if target.exists() or target.is_symlink():
            if target.is_dir() and not target.is_symlink():
                shutil.rmtree(target)
            else:
                target.unlink()
        if mode == "symlink":
            target.symlink_to(source, target_is_directory=source.is_dir())
        elif mode == "copy":
            if source.is_dir():
                shutil.copytree(source, target)
            else:
                shutil.copy2(source, target)
        else:
            raise PilotError(f"Unsupported asset mode {mode!r}; use symlink or copy")


def discover_staged_skills(skills_dir: Path) -> list[str]:
    """Return the declared names of every skill staged below the isolated root."""
    names: set[str] = set()
    seen_files: set[Path] = set()
    for current, dirs, files in os.walk(skills_dir, followlinks=True):
        dirs.sort()
        if "SKILL.md" not in files:
            continue
        skill_file = Path(current) / "SKILL.md"
        resolved = skill_file.resolve()
        if resolved in seen_files:
            dirs[:] = []
            continue
        content = skill_file.read_text(encoding="utf-8", errors="replace")
        match = SKILL_NAME.search(content)
        name = (match.group(1).strip() if match else Path(current).name).replace("/", "-")
        if not name:
            raise PilotError(f"Staged skill has an empty name: {skill_file}")
        if name in names:
            raise PilotError(f"Duplicate staged skill name {name!r} below {skills_dir}")
        names.add(name)
        seen_files.add(resolved)
        dirs[:] = []
    if not names:
        raise PilotError(f"No skill directories were staged below {skills_dir}")
    return sorted(names)


def expand_command(command: str, values: dict[str, str]) -> list[str]:
    expanded = command
    for key, value in values.items():
        expanded = expanded.replace("{" + key + "}", value)
    try:
        argv = shlex.split(expanded)
    except ValueError as exc:
        raise PilotError(f"Cannot parse agent command: {exc}") from exc
    if not argv:
        raise PilotError("Agent command is empty")
    return argv


def read_agent_metadata(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    if not path.exists():
        return None, "agent did not write PILOT_METADATA_FILE"
    try:
        metadata = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, f"invalid agent metadata: {exc}"
    if not isinstance(metadata, dict):
        return None, "agent metadata must be a JSON object"
    return metadata, None


def verify_protocol(
    metadata: dict[str, Any] | None,
    condition_id: str,
    skills_dir: Path,
    staged_skills: list[str],
    isolation_required: bool,
    filesystem_sandbox_required: bool,
) -> tuple[bool, list[str]]:
    if not isolation_required and not filesystem_sandbox_required:
        return True, []
    issues: list[str] = []
    if metadata is None:
        return False, ["isolation metadata is required but missing"]
    if isolation_required:
        if metadata.get("condition_id") != condition_id:
            issues.append("metadata condition_id does not match the assigned condition")
        roots = metadata.get("loaded_skill_roots")
        if not isinstance(roots, list) or not roots:
            issues.append("metadata loaded_skill_roots must be a non-empty list")
        else:
            expected = os.path.normcase(os.path.abspath(skills_dir))
            actual = {os.path.normcase(os.path.abspath(str(root))) for root in roots}
            if actual != {expected}:
                issues.append(f"loaded_skill_roots must contain only the isolated root {skills_dir}")

        loaded = metadata.get("loaded_skills")
        if not isinstance(loaded, list) or not loaded or not all(
            isinstance(name, str) for name in loaded
        ):
            issues.append("metadata loaded_skills must be a non-empty list of skill names")
        else:
            loaded_names = set(loaded)
            expected_names = set(staged_skills)
            if len(loaded_names) != len(loaded):
                issues.append("metadata loaded_skills must not contain duplicate names")
            if loaded_names != expected_names:
                issues.append(
                    "loaded_skills must exactly match the staged skill inventory; "
                    f"missing={sorted(expected_names - loaded_names)}, "
                    f"unexpected={sorted(loaded_names - expected_names)}"
                )
    if filesystem_sandbox_required and metadata.get("filesystem_sandbox") is not True:
        issues.append("metadata filesystem_sandbox must be true")
    return not issues, issues


def run_one(
    *,
    run_dir: Path,
    manifest: dict[str, Any],
    manifest_dir: Path,
    condition: dict[str, Any],
    case: dict[str, Any],
    attempt: int,
    agent_command: str,
    timeout_seconds: int,
    keep_workspaces: bool,
    resume: bool,
) -> dict[str, Any]:
    condition_id = condition["id"]
    case_id = case["id"]
    record_dir = run_dir / "records" / condition_id / case_id / f"attempt-{attempt:02d}"
    result_path = record_dir / "result.json"
    if resume and result_path.exists():
        return load_json(result_path)

    workspace = run_dir / "workspaces" / condition_id / case_id / f"attempt-{attempt:02d}"
    if workspace.exists():
        shutil.rmtree(workspace)
    workspace.mkdir(parents=True)
    record_dir.mkdir(parents=True, exist_ok=True)

    inventory = asset_inventory(condition, manifest_dir)
    mount_assets(workspace, inventory)
    skills_dir = workspace / "skills"
    skills_dir.mkdir(exist_ok=True)
    staged_skills = discover_staged_skills(skills_dir)

    rendered_prompt = case["prompt"].rstrip() + str(manifest.get("prompt_suffix", "")) + "\n"
    prompt_file = workspace / "prompt.txt"
    prompt_file.write_text(rendered_prompt, encoding="utf-8")
    public_case = {key: value for key, value in case.items() if key != "answer_key"}
    case_file = workspace / "case.json"
    case_file.write_text(json.dumps(public_case, indent=2) + "\n", encoding="utf-8")
    condition_public = {
        "id": condition_id,
        "label": condition.get("label"),
        "description": condition.get("description"),
        "capabilities": condition.get("capabilities", []),
        "skill_root": str(skills_dir),
        "staged_skills": staged_skills,
        "assets": [{"id": a["id"], "mount": a["mount"], "mode": a["mode"]} for a in inventory],
    }
    condition_file = workspace / "condition.json"
    condition_file.write_text(json.dumps(condition_public, indent=2) + "\n", encoding="utf-8")
    metadata_file = workspace / "agent-metadata.json"

    values = {
        "workspace": str(workspace),
        "prompt_file": str(prompt_file),
        "case_file": str(case_file),
        "condition_file": str(condition_file),
        "skills_dir": str(skills_dir),
        "metadata_file": str(metadata_file),
        "condition_id": condition_id,
        "case_id": case_id,
        "attempt": str(attempt),
    }
    argv = expand_command(agent_command, values)
    env = os.environ.copy()
    env.update(
        {
            "PILOT_RUN_DIR": str(run_dir),
            "PILOT_WORKSPACE": str(workspace),
            "PILOT_PROMPT_FILE": str(prompt_file),
            "PILOT_CASE_FILE": str(case_file),
            "PILOT_CONDITION_FILE": str(condition_file),
            "PILOT_SKILLS_DIR": str(skills_dir),
            "PILOT_METADATA_FILE": str(metadata_file),
            "PILOT_CONDITION_ID": condition_id,
            "PILOT_CASE_ID": case_id,
            "PILOT_ATTEMPT": str(attempt),
        }
    )

    started_at = utc_now()
    start = time.perf_counter()
    timed_out = False
    try:
        completed = subprocess.run(
            argv,
            input=rendered_prompt,
            text=True,
            cwd=workspace,
            env=env,
            capture_output=True,
            timeout=timeout_seconds,
            check=False,
        )
        stdout = completed.stdout
        stderr = completed.stderr
        exit_code: int | None = completed.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        stdout = exc.stdout if isinstance(exc.stdout, str) else ""
        stderr = exc.stderr if isinstance(exc.stderr, str) else ""
        stderr += f"\nPilot runner timed out after {timeout_seconds} seconds.\n"
        exit_code = None
    elapsed = time.perf_counter() - start
    finished_at = utc_now()

    (record_dir / "stdout.txt").write_text(stdout, encoding="utf-8")
    (record_dir / "stderr.txt").write_text(stderr, encoding="utf-8")
    metadata, metadata_error = read_agent_metadata(metadata_file)
    protocol_ok, protocol_issues = verify_protocol(
        metadata,
        condition_id,
        skills_dir,
        staged_skills,
        bool(manifest.get("require_isolation_metadata", False)),
        bool(manifest.get("require_filesystem_sandbox_metadata", False)),
    )
    if metadata_error:
        protocol_issues.append(metadata_error)

    result = {
        "schema_version": 1,
        "run_id": run_dir.name,
        "pilot_id": manifest.get("pilot_id"),
        "condition": {
            "id": condition_id,
            "label": condition.get("label"),
            "capabilities": condition.get("capabilities", []),
            "assets": inventory,
        },
        "case": {
            "id": case_id,
            "title": case.get("title"),
            "case_type": case.get("case_type"),
            "product": case.get("product"),
        },
        "attempt": attempt,
        "started_at": started_at,
        "finished_at": finished_at,
        "elapsed_seconds": round(elapsed, 6),
        "exit_code": exit_code,
        "timed_out": timed_out,
        "stdout": stdout,
        "stderr": stderr,
        "agent_metadata": metadata,
        "protocol": {
            "isolation_required": bool(manifest.get("require_isolation_metadata", False)),
            "filesystem_sandbox_metadata_required": bool(
                manifest.get("require_filesystem_sandbox_metadata", False)
            ),
            "expected_loaded_skills": staged_skills,
            "isolation_verified": protocol_ok,
            "issues": protocol_issues,
        },
        "command": {"argv": argv},
        "artifacts": {
            "record_dir": str(record_dir),
            "workspace": str(workspace) if keep_workspaces else None,
        },
    }
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not keep_workspaces:
        shutil.rmtree(workspace, ignore_errors=True)
    return result


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--cases-file", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--output", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--agent-command", help="Command invoked for each case; prompt is also passed on stdin")
    parser.add_argument("--condition", action="append", default=[], help="Condition id; repeat or use all")
    parser.add_argument("--case", action="append", default=[], help="Case id; repeat or use all")
    parser.add_argument("--repetitions", type=int, default=None)
    parser.add_argument("--timeout", type=int, default=None)
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--discard-workspaces", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        manifest_path = args.manifest.absolute()
        cases_path = args.cases_file.absolute()
        manifest = load_json(manifest_path)
        cases_doc = load_json(cases_path)
        validate_inputs(manifest, cases_doc)

        conditions = selected_items(manifest["conditions"], args.condition or ["all"], "condition ids")
        cases = selected_items(cases_doc["cases"], args.case or ["all"], "case ids")
        repetitions = args.repetitions if args.repetitions is not None else int(manifest.get("repetitions", 1))
        timeout_seconds = args.timeout if args.timeout is not None else int(manifest.get("timeout_seconds", 300))
        if repetitions < 1 or args.jobs < 1 or timeout_seconds < 1:
            raise PilotError("repetitions, jobs, and timeout must be positive integers")

        inventories = {condition["id"]: asset_inventory(condition, manifest_path.parent) for condition in conditions}
        jobs = [
            (condition, case, attempt)
            for attempt in range(1, repetitions + 1)
            for case in cases
            for condition in conditions
        ]
        random.Random(int(manifest.get("random_seed", 0))).shuffle(jobs)

        if args.dry_run:
            print(
                json.dumps(
                    {
                        "valid": True,
                        "pilot_id": manifest.get("pilot_id"),
                        "conditions": [condition["id"] for condition in conditions],
                        "cases": [case["id"] for case in cases],
                        "repetitions": repetitions,
                        "job_count": len(jobs),
                        "assets": inventories,
                    },
                    indent=2,
                )
            )
            return 0

        if not args.agent_command:
            raise PilotError("--agent-command is required unless --dry-run is used")
        run_id = args.run_id or default_run_id()
        ensure_safe_id(run_id, "run id")
        run_dir = args.output.absolute() / run_id
        run_dir.mkdir(parents=True, exist_ok=args.resume)

        run_manifest = {
            "schema_version": 1,
            "run_id": run_id,
            "created_at": utc_now(),
            "pilot_manifest": str(manifest_path),
            "case_suite": str(cases_path),
            "pilot_manifest_sha256": canonical_json_hash(manifest),
            "case_suite_sha256": canonical_json_hash(cases_doc),
            "condition_ids": [condition["id"] for condition in conditions],
            "case_ids": [case["id"] for case in cases],
            "repetitions": repetitions,
            "random_seed": manifest.get("random_seed", 0),
            "timeout_seconds": timeout_seconds,
            "jobs": args.jobs,
            "require_isolation_metadata": bool(manifest.get("require_isolation_metadata", False)),
            "require_filesystem_sandbox_metadata": bool(
                manifest.get("require_filesystem_sandbox_metadata", False)
            ),
            "agent_command": args.agent_command,
        }
        (run_dir / "run-manifest.json").write_text(
            json.dumps(run_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )

        def invoke(job: tuple[dict[str, Any], dict[str, Any], int]) -> dict[str, Any]:
            condition, case, attempt = job
            return run_one(
                run_dir=run_dir,
                manifest=manifest,
                manifest_dir=manifest_path.parent,
                condition=condition,
                case=case,
                attempt=attempt,
                agent_command=args.agent_command,
                timeout_seconds=timeout_seconds,
                keep_workspaces=not args.discard_workspaces,
                resume=args.resume,
            )

        results: list[dict[str, Any]] = []
        if args.jobs == 1:
            for index, job in enumerate(jobs, 1):
                condition, case, attempt = job
                print(f"[{index}/{len(jobs)}] {condition['id']} {case['id']} attempt {attempt}", flush=True)
                results.append(invoke(job))
        else:
            with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
                future_map = {executor.submit(invoke, job): job for job in jobs}
                for index, future in enumerate(concurrent.futures.as_completed(future_map), 1):
                    condition, case, attempt = future_map[future]
                    results.append(future.result())
                    print(f"[{index}/{len(jobs)}] {condition['id']} {case['id']} attempt {attempt}", flush=True)

        results.sort(key=lambda item: (item["case"]["id"], item["attempt"], item["condition"]["id"]))
        with (run_dir / "results.jsonl").open("w", encoding="utf-8") as handle:
            for result in results:
                handle.write(json.dumps(result, sort_keys=True) + "\n")
        protocol_failures = sum(not item["protocol"]["isolation_verified"] for item in results)
        execution_failures = sum(item["exit_code"] != 0 or item["timed_out"] for item in results)
        print(
            json.dumps(
                {
                    "run_dir": str(run_dir),
                    "records": len(results),
                    "execution_failures": execution_failures,
                    "isolation_protocol_failures": protocol_failures,
                },
                indent=2,
            )
        )
        return 0 if execution_failures == 0 and protocol_failures == 0 else 1
    except PilotError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

# Ping Agent Skills deep-documentation A/B pilot

This directory contains a provider-neutral pilot comparing only two conditions:

- **A:** the six official Ping umbrella Agent Skills.
- **B:** the same six skills plus one consolidated deep-documentation layer.

There is no MCP condition. The runner does not call a model API itself; it invokes a command supplied by the evaluator, so both conditions use the same model, account, system prompt, and agent harness.

## What is measured

The suite contains 15 natural TC prompts spanning detailed configuration, API workflows, troubleshooting, operations, an underspecified request, and a non-Ping `agent` request. The prompt text does not name a skill or documentation guide. Machine-readable answer keys contain gold source groups, lightweight fact checks, and expected clarification behavior; answer keys are never copied into an agent workspace.

Default execution is three repetitions per case and condition: 90 responses total. Job order is deterministically shuffled to reduce time/order bias. Run at concurrency 1 when the provider applies shared rate limits or when latency is a primary outcome.

Deterministic reporting includes:

- execution and timeout success;
- isolation-protocol compliance;
- recall of gold documentation source groups;
- a diagnostic gold-citation precision measure;
- citation-policy behavior for the non-Ping case;
- explicitly labelled regex heuristics for key facts and clarification behavior;
- median and p95 elapsed time; and
- tool-call, token, and cost metadata together with per-field coverage rates; and
- whether the provider's runtime built-in skill inventory is fully reported, stable, and identical across A/B.

Technical correctness, completeness, evidence quality, safety, and actionability require blinded SME scoring with [SME_RUBRIC.md](SME_RUBRIC.md).

## Prepare the two skill inputs

Create a staging directory that contains exactly the six official skill directories and no other directory containing `SKILL.md`:

```text
/path/to/umbrella-only/
  ping-quickstart/
  ping-foundation/
  ping-app-integration/
  ping-orchestration/
  ping-universal-services/
  ping-identity-for-ai/
```

The consolidated layer is a single skill directory containing its own `SKILL.md`. Point the pilot at both inputs:

```bash
export PING_UMBRELLA_SKILLS_DIR=/path/to/umbrella-only
export PING_DEEP_DOC_LAYER_DIR=/path/to/consolidated-ping-deep-docs
```

The runner rejects extra staged umbrella skills. This prevents condition A from silently seeing unrelated product doc skills.

## Agent command contract

The `--agent-command` is executed once per response in a new isolated working directory. The rendered prompt is sent on standard input and is also available in `PILOT_PROMPT_FILE`.

The command or thin provider adapter must load assigned skills **only** from `PILOT_SKILLS_DIR`. It must disable globally installed, auto-discovered, or marketplace skills for the evaluated process. Provider-bundled skills that cannot be disabled must be identical in both conditions and recorded by the adapter. Network access is allowed for live-page fallback, but both conditions must receive identical network/tool access.

The runner sets these environment variables:

| Variable | Meaning |
|---|---|
| `PILOT_WORKSPACE` | Unique workspace for this response |
| `PILOT_PROMPT_FILE` | Prompt file; identical content is sent on stdin |
| `PILOT_CASE_FILE` | Public case metadata without the answer key |
| `PILOT_CONDITION_FILE` | Public condition metadata |
| `PILOT_SKILLS_DIR` | The only skill root the adapter may load |
| `PILOT_METADATA_FILE` | JSON file the adapter must write |
| `PILOT_CONDITION_ID` | `A` or `B` |
| `PILOT_CASE_ID` | Stable case identifier |
| `PILOT_ATTEMPT` | One-based repetition number |

The command string can use `{workspace}`, `{prompt_file}`, `{case_file}`, `{condition_file}`, `{skills_dir}`, `{metadata_file}`, `{condition_id}`, `{case_id}`, and `{attempt}` placeholders. It is parsed as an argument vector without a shell; put pipelines or provider-specific setup in an adapter script.

For an auditable run, the adapter must write at least:

```json
{
  "condition_id": "B",
  "loaded_skill_roots": ["/absolute/path/from/PILOT_SKILLS_DIR"],
  "loaded_skills": [
    "ping-app-integration",
    "ping-docs",
    "ping-foundation",
    "ping-identity-for-ai",
    "ping-orchestration",
    "ping-quickstart",
    "ping-universal-services"
  ],
  "filesystem_sandbox": true,
  "runtime_builtin_skills": ["provider-bundled-skill"],
  "model": "provider-model-version",
  "tool_calls": 4,
  "input_tokens": 8200,
  "output_tokens": 950,
  "total_tokens": 9150
}
```

`condition_id` must match the assignment, `loaded_skill_roots` must contain only the exact `PILOT_SKILLS_DIR` path, and `loaded_skills` must exactly match the names declared by the `SKILL.md` files actually staged below that root. The default manifest also requires `filesystem_sandbox: true`; this is a protocol declaration, not a substitute for inspecting the adapter's sandbox configuration. `runtime_builtin_skills` must list provider-bundled skills that could not be disabled, including an empty list when there are none. Tool, token, and cost values are optional, but the report shows their coverage so a partial sample cannot masquerade as a complete efficiency comparison. Missing or mismatched required metadata makes the response unsuccessful and prevents a publishable comparison.

## Bundled Claude Code adapter

`adapters/claude_code.py` runs each response through Claude Code with a fresh home and configuration directory, an isolated temporary working directory, project-local copies of only the assigned skills and deep-doc data, no MCP servers, and an explicit tool allowlist. Claude's OS-level Bash sandbox is mandatory and fails closed; the host home is denied, unsandboxed commands are disabled, and cloud credentials are scrubbed from tool subprocesses. Provider-bundled skills, memory, CLAUDE files, background tasks, and built-in agents are disabled where the CLI supports it. The adapter verifies that Claude's runtime-announced inventory contains every assigned skill and records unavoidable built-ins (currently `doctor`) for the A/B consistency check. It also records native skill invocations, tools, resolved models, tokens, cost, and permission denials. It requires an already authenticated Claude Code installation; credentials are not copied into a result workspace.

The adapter requires an explicit model identifier and rejects mutable aliases such as `sonnet`. Pin it for every run:

```bash
export PILOT_CLAUDE_MODEL=global.anthropic.claude-sonnet-4-6
export PILOT_ADAPTER_TIMEOUT=285
```

Keep the pilot output outside this source checkout. That prevents a shell-capable condition-A agent from discovering the deep-doc repository simply by walking up from its working directory.

## Validate and run

Dry-run validation resolves both asset inputs, checks the case suite, and prints the planned inventory without invoking an agent:

```bash
python3 evals/run.py --dry-run
```

Before a publishable run, verify that the version-pinned gold sources still resolve:

```bash
python3 evals/validate_sources.py
```

Run the full randomized pilot with a provider adapter:

```bash
python3 evals/run.py \
  --agent-command "$PWD/evals/adapters/claude_code.py" \
  --output /absolute/path/outside/repo/ping-pilot-results \
  --run-id pilot-001 \
  --jobs 1
```

For an iterative smoke test, select cases, one repetition, and both conditions:

```bash
python3 evals/run.py \
  --agent-command "$PWD/evals/adapters/claude_code.py" \
  --output /absolute/path/outside/repo/ping-pilot-results \
  --run-id smoke-001 \
  --case paz-conditional-redaction \
  --case ambiguous-token-rollover \
  --repetitions 1
```

Use `--resume` to skip records whose `result.json` already exists. Use `--discard-workspaces` to retain only prompts, stdout, stderr, metadata, and result records. By default the full isolated workspaces remain for audit.

## Score and review

Generate deterministic results and a blinded SME review packet:

```bash
python3 evals/score.py /absolute/path/outside/repo/ping-pilot-results/pilot-001
```

Outputs are written under `<output>/pilot-001/report/`:

- `report.md` and `summary.json` — aggregate comparison;
- `case-scores.csv` — deterministic per-response metrics;
- `sme-reviews.csv` — blinded prompts/responses and blank rubric columns; and
- `sme-review-key.csv` — condition key, held by the pilot owner until scoring is locked.

After SMEs complete the blinded CSV, incorporate scores without changing the responses:

```bash
python3 evals/score.py evals/results/pilot-001 \
  --sme-reviews /path/to/completed-sme-reviews.csv
```

Do not publish aggregate gains if either condition has less than 100% isolation verification. Do not attribute differences to the deep-doc layer unless runtime built-in skill inventories have 100% metadata coverage, are internally stable, and are identical across A/B. Treat tool, token, or cost comparisons as incomplete whenever the relevant numeric metadata coverage is below 100%. Report paired product-level regressions and critical correctness/safety failures, not only the overall mean.

## Harness self-test

The self-test uses a fake provider command and temporary skill inputs; it does not contact a model or the network:

```bash
python3 -m unittest discover -s evals/tests -v
```

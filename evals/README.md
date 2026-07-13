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
- tool-call and token metadata when the adapter supplies it.

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

The command or thin provider adapter must load skills **only** from `PILOT_SKILLS_DIR`. It must disable globally installed, auto-discovered, or marketplace skills for the evaluated process. Network access is allowed because the current deep-doc design is live-doc-first, but both conditions must receive identical network/tool access.

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
  "model": "provider-model-version",
  "tool_calls": 4,
  "input_tokens": 8200,
  "output_tokens": 950,
  "total_tokens": 9150
}
```

`condition_id` must match the assignment, and `loaded_skill_roots` must contain only the exact `PILOT_SKILLS_DIR` path. Tool and token fields are optional. A missing or mismatched isolation declaration makes the response unsuccessful and prevents a publishable comparison.

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
  --agent-command '/absolute/path/to/my-agent-adapter' \
  --run-id pilot-001 \
  --jobs 1
```

For an iterative smoke test, select cases, one repetition, and both conditions:

```bash
python3 evals/run.py \
  --agent-command '/absolute/path/to/my-agent-adapter' \
  --run-id smoke-001 \
  --case paz-conditional-redaction \
  --case ambiguous-token-rollover \
  --repetitions 1
```

Use `--resume` to skip records whose `result.json` already exists. Use `--discard-workspaces` to retain only prompts, stdout, stderr, metadata, and result records. By default the full isolated workspaces remain for audit.

## Score and review

Generate deterministic results and a blinded SME review packet:

```bash
python3 evals/score.py evals/results/pilot-001
```

Outputs are written under `evals/results/pilot-001/report/`:

- `report.md` and `summary.json` — aggregate comparison;
- `case-scores.csv` — deterministic per-response metrics;
- `sme-reviews.csv` — blinded prompts/responses and blank rubric columns; and
- `sme-review-key.csv` — condition key, held by the pilot owner until scoring is locked.

After SMEs complete the blinded CSV, incorporate scores without changing the responses:

```bash
python3 evals/score.py evals/results/pilot-001 \
  --sme-reviews /path/to/completed-sme-reviews.csv
```

Do not publish aggregate gains if either condition has less than 100% isolation verification. Report paired product-level regressions and critical correctness/safety failures, not only the overall mean.

## Harness self-test

The self-test uses a fake provider command and temporary skill inputs; it does not contact a model or the network:

```bash
python3 -m unittest discover -s evals/tests -v
```

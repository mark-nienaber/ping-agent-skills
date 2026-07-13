---
name: ping-docs
description: Find exact, detailed, version-specific Ping Identity documentation pages and offline snapshots. Use after Ping product or intent routing when implementation, configuration, API, policy, troubleshooting, release, or citation detail is needed across Ping products; also use when live documentation access is unavailable. Do not use for unrelated requests or initial product selection.
---

# Ping documentation retrieval

Search the cached documentation indexes with the bundled script. The indexes are routing metadata,
not the answer source. Use answer-context mode so the script returns exact live page URLs and keeps
verified, bounded snapshot excerpts available only as an offline fallback.

```bash
python3 scripts/search_docs.py --json --answer-context "<specific user task>"
```

Add `--product <slug-or-name>` when the product is known, for example:

```bash
python3 scripts/search_docs.py --json --answer-context --product pingam "configure account lockout"
```

## Bounded workflow

1. Run exactly one answer-context search with the concrete task, preserving the product, version,
   error text, endpoint, and feature names. Use `--product` whenever the product is known. Execute
   the script directly; do not read its source.
2. Select at most two results that directly match the product and intent. Treat `no_results` as
   abstention: clarify instead of guessing. One narrower retry is allowed when the first result
   set is irrelevant; do not run additional searches.
3. Fetch each selected result's `live_markdown_url` directly before using any snapshot content.
   Fetch at most two selected live pages. If a selected URL has moved, check the current live
   product index or make one bounded retry; do not broaden into general web search otherwise.
4. Only when the live page cannot be reached may you use its returned `snapshot_excerpt`. Never
   open, grep, search, or read a `local_snapshot`, `llms.txt`, the script source, or a per-docset
   `SKILL.md`. A null excerpt means the exact page is not captured; do not search neighboring
   snapshot content for it.
5. Stop when the evidence establishes the relevant feature or configuration surface, the inputs
   needed, and the main validation or safety constraint. If exact syntax is not documented in the
   selected excerpts, identify that gap and give a clearly labelled recommendation instead of
   searching for optional corroboration.
6. Cite each selected `live_markdown_url`. When a dated local snapshot supplied the content,
   explicitly say that live access failed and disclose `snapshot_version` and `snapshot_sync_date`
   for potentially changeable behavior.

Hard retrieval budget per request: at most two answer-context searches, two direct live-page
fetches, and zero follow-up local file reads. Do not chase alternate terminology after the
selected evidence supports the answer.

The script performs no network requests. It discovers docsets from the repository layout,
`references/docsets/` in a copied standalone skill, or `PING_DOCS_DATA_ROOT` when explicitly set.

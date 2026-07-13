---
name: ping-docs
description: Find exact, detailed, version-specific Ping Identity documentation pages and offline snapshots. Use after Ping product or intent routing when implementation, configuration, API, policy, troubleshooting, release, or citation detail is needed across Ping products; also use when live documentation access is unavailable. Do not use for unrelated requests or initial product selection.
---

# Ping documentation retrieval

Search the cached documentation indexes with the bundled script. Do not read an entire
`llms.txt` into context.

```bash
python3 scripts/search_docs.py --json --top-k 5 "<specific user task>"
```

Add `--product <slug-or-name>` when the product is known, for example:

```bash
python3 scripts/search_docs.py --json --product pingam "configure account lockout"
```

## Workflow

1. Search with the user's concrete task, preserving product names, error text, endpoint names,
   and version terms.
2. Select the highest-scoring result that matches the user's product and intent. Treat a
   `no_results` response as abstention: clarify the product or task instead of guessing.
3. Read the returned live Markdown URL when live access is available.
4. Otherwise, read only the returned `local_snapshot` and use `snapshot_sync_date` to disclose
   its freshness. The snapshot can contain multiple pages, so search within it for the returned
   title or URL before loading a small relevant section.
5. Cite the live Markdown URL in the answer even when the local snapshot supplied the content.

The script performs no network requests. It discovers docsets from the repository layout,
`references/docsets/` in a copied standalone skill, or `PING_DOCS_DATA_ROOT` when explicitly set.

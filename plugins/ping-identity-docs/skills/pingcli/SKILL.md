---
name: pingcli
description: "Use when the user explicitly names Ping CLI or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Ping CLI

A CLI tool for managing the configuration of Ping Identity products.

## Live source of truth

- Product docs: https://developer.pingidentity.com/pingcli/
- llms.txt index: https://developer.pingidentity.com/pingcli/llms.txt
- Snapshot version: 1.11
- Snapshot manifest: references/MANIFEST.md

## Retrieval strategy

1. Use the routing table to narrow the task to a guide when possible.
2. Search `references/llms.txt` for task terms and inspect at most 20 matching lines. Never load the whole index. Prefer `rg -i -n --max-count 20 '<term1>|<term2>' references/llms.txt` when shell access is available.
3. Fetch only the best matching live `.md` page from Ping documentation.
4. If that URL moved, fetch the live llms.txt index above and repeat the targeted search.
5. If live access is unavailable, read only the closest snapshot, check `references/MANIFEST.md`, and disclose its version, sync date, and partial-capture status.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Command Reference: administrative, pingfederate, advanced | command_reference | https://developer.pingidentity.com/pingcli/1.11/command_reference/*.md | references/snapshots/command-reference.md |
| Using Pingcli: managing, output, services | using_pingcli | https://developer.pingidentity.com/pingcli/1.11/using_pingcli/*.md | references/snapshots/using-pingcli.md |
| Install: install, update, container | install | https://developer.pingidentity.com/pingcli/1.11/install/*.md | references/snapshots/install.md |
| Root: cli, compatibility, getting | root | https://developer.pingidentity.com/pingcli/1.11/*.md | references/snapshots/root.md |
| Output Schema Reference: json, output, reference | output_schema_reference | https://developer.pingidentity.com/pingcli/1.11/output_schema_reference/*.md | references/snapshots/output-schema-reference.md |
| Pingone: cli, getting, pingone | pingone | https://developer.pingidentity.com/pingcli/1.11/pingone/*.md | references/snapshots/pingone.md |
| Release Notes: release, notes, cli | release_notes | https://developer.pingidentity.com/pingcli/1.11/release_notes/*.md | references/snapshots/release-notes.md |
| Settings Reference: configuration, cli, command | settings_reference | https://developer.pingidentity.com/pingcli/1.11/settings_reference/*.md | references/snapshots/settings-reference.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

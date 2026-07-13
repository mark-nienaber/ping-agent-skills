---
name: openicf
description: "Use when the user explicitly names OpenICF or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# OpenICF

Overview of the Identity Connector Framework (ICF) for connecting external resources to Ping Identity products, with available connectors listed.

## Live source of truth

- Product docs: https://docs.pingidentity.com/openicf/
- llms.txt index: https://docs.pingidentity.com/openicf/llms.txt
- Snapshot version: current
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
| Connector Reference: connector, pingidm, configure | connector-reference | https://docs.pingidentity.com/openicf/connector-reference/*.md | references/snapshots/connector-reference.md |
| Connector Dev Guide: connector, icf, connectors | connector-dev-guide | https://docs.pingidentity.com/openicf/connector-dev-guide/*.md | references/snapshots/connector-dev-guide.md |
| Connector Release Notes: release, notes, connector | connector-release-notes | https://docs.pingidentity.com/openicf/connector-release-notes/*.md | references/snapshots/connector-release-notes.md |
| Index.Md: identity, available, connecting | index.md | https://docs.pingidentity.com/openicf/index.md | references/snapshots/index-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

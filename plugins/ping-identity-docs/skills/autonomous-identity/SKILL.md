---
name: autonomous-identity
description: "Use when the user explicitly names Autonomous Identity or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Autonomous Identity

Autonomous Identity documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/autonomous-identity/
- llms.txt index: https://docs.pingidentity.com/autonomous-identity/llms.txt
- Snapshot version: 2022.11.12
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
| Admin Guide: appendix, data, file | admin-guide | https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/*.md | references/snapshots/admin-guide.md |
| Api Guide: application, autonomous, config | api-guide | https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/*.md | references/snapshots/api-guide.md |
| Install Guide: deployment, install, node | install-guide | https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/*.md | references/snapshots/install-guide.md |
| Release Notes: release, advisories, before | release-notes | https://docs.pingidentity.com/autonomous-identity/2022.11.12/release-notes/*.md | references/snapshots/release-notes.md |
| Users Guide: tasks, autonomous, identity | users-guide | https://docs.pingidentity.com/autonomous-identity/2022.11.12/users-guide/*.md | references/snapshots/users-guide.md |
| Deployment Planning: deployment, planning, architecture | deployment-planning | https://docs.pingidentity.com/autonomous-identity/2022.11.12/deployment-planning/*.md | references/snapshots/deployment-planning.md |
| Root: architecture, brief, features | root | https://docs.pingidentity.com/autonomous-identity/2022.11.12/*.md | references/snapshots/root.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

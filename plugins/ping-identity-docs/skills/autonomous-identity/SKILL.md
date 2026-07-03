---
name: autonomous-identity
description: "Use when administering Ping Autonomous Identity, including installation, deployment planning, analytics, governance users, APIs, upgrades, troubleshooting, or release notes. Routes to live docs; snapshots fallback."
license: MIT
---

# Autonomous Identity

Autonomous Identity documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/autonomous-identity/
- llms.txt index: https://docs.pingidentity.com/autonomous-identity/llms.txt
- Snapshot version: 2022.11.12
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

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

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

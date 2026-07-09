---
name: identity-governance
description: "Use when working with Identity Governance: users guide, release notes, admin guide, api guide, root. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# Identity Governance

Identity Governance documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/identity-governance/
- llms.txt index: https://docs.pingidentity.com/identity-governance/llms.txt
- Snapshot version: 7.1.2
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Users Guide: access, requests, review | users-guide | https://docs.pingidentity.com/identity-governance/7.1.2/users-guide/*.md | references/snapshots/users-guide.md |
| Release Notes: release, before, changelog | release-notes | https://docs.pingidentity.com/identity-governance/7.1.2/release-notes/*.md | references/snapshots/release-notes.md |
| Admin Guide: access, administration, common | admin-guide | https://docs.pingidentity.com/identity-governance/7.1.2/admin-guide/*.md | references/snapshots/admin-guide.md |
| Api Guide: access, about, governance | api-guide | https://docs.pingidentity.com/identity-governance/7.1.2/api-guide/*.md | references/snapshots/api-guide.md |
| Root: glossary | root | https://docs.pingidentity.com/identity-governance/7.1.2/*.md | references/snapshots/root.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

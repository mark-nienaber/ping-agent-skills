---
name: identity-governance
description: "Use when the user explicitly names Identity Governance or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Identity Governance

Identity Governance documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/identity-governance/
- llms.txt index: https://docs.pingidentity.com/identity-governance/llms.txt
- Snapshot version: 7.1.2
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
| Users Guide: access, requests, review | users-guide | https://docs.pingidentity.com/identity-governance/7.1.2/users-guide/*.md | references/snapshots/users-guide.md |
| Release Notes: release, before, changelog | release-notes | https://docs.pingidentity.com/identity-governance/7.1.2/release-notes/*.md | references/snapshots/release-notes.md |
| Admin Guide: access, administration, common | admin-guide | https://docs.pingidentity.com/identity-governance/7.1.2/admin-guide/*.md | references/snapshots/admin-guide.md |
| Api Guide: access, about, governance | api-guide | https://docs.pingidentity.com/identity-governance/7.1.2/api-guide/*.md | references/snapshots/api-guide.md |
| Root: glossary | root | https://docs.pingidentity.com/identity-governance/7.1.2/*.md | references/snapshots/root.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

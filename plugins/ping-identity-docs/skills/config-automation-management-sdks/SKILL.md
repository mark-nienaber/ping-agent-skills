---
name: config-automation-management-sdks
description: "Use when the user explicitly names Config Automation Management SDKs or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Config Automation Management SDKs

Find the available Ping Identity Management and User client SDK libraries for PingOne Advanced Identity Cloud, PingFederate, and PingDirectory.

## Live source of truth

- Product docs: https://developer.pingidentity.com/config-automation-management-sdks/
- llms.txt index: https://developer.pingidentity.com/config-automation-management-sdks/llms.txt
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
| Products: client, connect, pingdirectory | products | https://developer.pingidentity.com/config-automation-management-sdks/products/*.md | references/snapshots/products.md |
| Develop With Management Sdks: identity, client, projects | develop_with_management_sdks | https://developer.pingidentity.com/config-automation-management-sdks/develop_with_management_sdks/*.md | references/snapshots/develop-with-management-sdks.md |
| Develop With Management Sdks.Md: management, sdks, user | develop_with_management_sdks.md | https://developer.pingidentity.com/config-automation-management-sdks/develop_with_management_sdks.md | references/snapshots/develop-with-management-sdks-md.md |
| Management Sdks Landing Page.Md: identity, management, user | management_sdks_landing_page.md | https://developer.pingidentity.com/config-automation-management-sdks/management_sdks_landing_page.md | references/snapshots/management-sdks-landing-page-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

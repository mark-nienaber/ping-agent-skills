---
name: config-automation-management-sdks
description: "Use when working with Config Automation Management SDKs: products, develop with management sdks, develop with management sdks.md, management sdks landing page.md. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# Config Automation Management SDKs

Config Automation Management SDKs documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/config-automation-management-sdks/
- llms.txt index: https://developer.pingidentity.com/config-automation-management-sdks/llms.txt
- Snapshot version: current
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Products: client, configuration, introduction | products | https://developer.pingidentity.com/config-automation-management-sdks/products/*.md | references/snapshots/products.md |
| Develop With Management Sdks: getting, interface, stability | develop_with_management_sdks | https://developer.pingidentity.com/config-automation-management-sdks/develop_with_management_sdks/*.md | references/snapshots/develop-with-management-sdks.md |
| Develop With Management Sdks.Md: configuration, develop, management | develop_with_management_sdks.md | https://developer.pingidentity.com/config-automation-management-sdks/develop_with_management_sdks.md | references/snapshots/develop-with-management-sdks-md.md |
| Management Sdks Landing Page.Md: configuration, management, overview | management_sdks_landing_page.md | https://developer.pingidentity.com/config-automation-management-sdks/management_sdks_landing_page.md | references/snapshots/management-sdks-landing-page-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

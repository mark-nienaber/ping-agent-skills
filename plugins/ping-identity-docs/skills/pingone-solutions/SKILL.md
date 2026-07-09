---
name: pingone-solutions
description: "Use when working with PingOne Solutions: healthcare, pingone customers plus, financial services, pingone customers passwordless, gift card auth, index.md. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# PingOne Solutions

Learn about the purpose and configuration of the Financial Services.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingone-solutions/
- llms.txt index: https://docs.pingidentity.com/pingone-solutions/llms.txt
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
| Healthcare: healthcare, subflow, flow | healthcare | https://docs.pingidentity.com/pingone-solutions/healthcare/*.md | references/snapshots/healthcare.md |
| Pingone Customers Plus: plus, ciam, protect | pingone-customers-plus | https://docs.pingidentity.com/pingone-solutions/pingone-customers-plus/*.md | references/snapshots/pingone-customers-plus.md |
| Financial Services: financial, services, ootb | financial-services | https://docs.pingidentity.com/pingone-solutions/financial-services/*.md | references/snapshots/financial-services.md |
| Pingone Customers Passwordless: passwordless, ciam, protect | pingone-customers-passwordless | https://docs.pingidentity.com/pingone-solutions/pingone-customers-passwordless/*.md | references/snapshots/pingone-customers-passwordless.md |
| Gift Card Auth: card, gift, redemption | gift-card-auth | https://docs.pingidentity.com/pingone-solutions/gift-card-auth/*.md | references/snapshots/gift-card-auth.md |
| Index.Md: packs, pingone, solution | index.md | https://docs.pingidentity.com/pingone-solutions/index.md | references/snapshots/index-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

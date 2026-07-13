---
name: pingone-solutions
description: "Use when the user explicitly names PingOne Solutions or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingOne Solutions

Learn about the purpose and configuration of the Financial Services.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingone-solutions/
- llms.txt index: https://docs.pingidentity.com/pingone-solutions/llms.txt
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
| Healthcare: healthcare, subflow, flow | healthcare | https://docs.pingidentity.com/pingone-solutions/healthcare/*.md | references/snapshots/healthcare.md |
| Pingone Customers Plus: plus, ciam, protect | pingone-customers-plus | https://docs.pingidentity.com/pingone-solutions/pingone-customers-plus/*.md | references/snapshots/pingone-customers-plus.md |
| Financial Services: financial, services, ootb | financial-services | https://docs.pingidentity.com/pingone-solutions/financial-services/*.md | references/snapshots/financial-services.md |
| Pingone Customers Passwordless: passwordless, ciam, protect | pingone-customers-passwordless | https://docs.pingidentity.com/pingone-solutions/pingone-customers-passwordless/*.md | references/snapshots/pingone-customers-passwordless.md |
| Gift Card Auth: card, gift, redemption | gift-card-auth | https://docs.pingidentity.com/pingone-solutions/gift-card-auth/*.md | references/snapshots/gift-card-auth.md |
| Index.Md: packs, pingone, solution | index.md | https://docs.pingidentity.com/pingone-solutions/index.md | references/snapshots/index-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

---
name: pingone-api-ea
description: "Use when the user explicitly names PingOne API (Early Access) or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingOne API (Early Access)

Early access endpoints to create, read, update, test, and delete PingOne Authorize trust framework attributes, plus their data model and event types.

## Live source of truth

- Product docs: https://developer.pingidentity.com/pingone-api-ea/
- llms.txt index: https://developer.pingidentity.com/pingone-api-ea/llms.txt
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
| Authorize: authorization, create, access | authorize | https://developer.pingidentity.com/pingone-api-ea/authorize/*.md | references/snapshots/authorize.md |
| Platform: pingone, promotion, environment | platform | https://developer.pingidentity.com/pingone-api-ea/platform/*.md | references/snapshots/platform.md |
| Verify: verification, pingone, verify | verify | https://developer.pingidentity.com/pingone-api-ea/verify/*.md | references/snapshots/verify.md |
| Auth: access, early, auth | auth | https://developer.pingidentity.com/pingone-api-ea/auth/*.md | references/snapshots/auth.md |
| Index.Md: access, early, pingone | index.md | https://developer.pingidentity.com/pingone-api-ea/index.md | references/snapshots/index-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

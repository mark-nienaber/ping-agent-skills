---
name: pingoneaic-api
description: "Use when the user explicitly names PingOne AIC API or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingOne AIC API

Learn about new PingOne Advanced Identity Cloud API updates.

## Live source of truth

- Product docs: https://developer.pingidentity.com/pingoneaic-api/
- llms.txt index: https://developer.pingidentity.com/pingoneaic-api/llms.txt
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
| Idm Rest Api: managed, rest, objects | idm-rest-api | https://developer.pingidentity.com/pingoneaic-api/idm-rest-api/*.md | references/snapshots/idm-rest-api.md |
| Am Oauth2: oauth2, oauth, token | am-oauth2 | https://developer.pingidentity.com/pingoneaic-api/am-oauth2/*.md | references/snapshots/am-oauth2.md |
| Am Authentication: callbacks, over, rest | am-authentication | https://developer.pingidentity.com/pingoneaic-api/am-authentication/*.md | references/snapshots/am-authentication.md |
| Am Oidc1: oauth2, connect, jwk | am-oidc1 | https://developer.pingidentity.com/pingoneaic-api/am-oidc1/*.md | references/snapshots/am-oidc1.md |
| Crest: action, advanced, cloud | crest | https://developer.pingidentity.com/pingoneaic-api/crest/*.md | references/snapshots/crest.md |
| Am Scripting: script, scripts, create | am-scripting | https://developer.pingidentity.com/pingoneaic-api/am-scripting/*.md | references/snapshots/am-scripting.md |
| Am Authorization: over, rest, policy | am-authorization | https://developer.pingidentity.com/pingoneaic-api/am-authorization/*.md | references/snapshots/am-authorization.md |
| Am Rest: realms, rest, specify | am-rest | https://developer.pingidentity.com/pingoneaic-api/am-rest/*.md | references/snapshots/am-rest.md |
| Identity Governance: governance, identity, access | identity-governance | https://developer.pingidentity.com/pingoneaic-api/identity-governance/*.md | references/snapshots/identity-governance.md |
| Am Sessions: manage, over, rest | am-sessions | https://developer.pingidentity.com/pingoneaic-api/am-sessions/*.md | references/snapshots/am-sessions.md |
| Api Custom Headers.Md: advanced, cloud, custom | api-custom-headers.md | https://developer.pingidentity.com/pingoneaic-api/api-custom-headers.md | references/snapshots/api-custom-headers-md.md |
| Api Reference.Md: advanced, cloud, identity | api-reference.md | https://developer.pingidentity.com/pingoneaic-api/api-reference.md | references/snapshots/api-reference-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

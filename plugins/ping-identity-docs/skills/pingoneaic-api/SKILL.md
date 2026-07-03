---
name: pingoneaic-api
description: "Use when developing with PingOne AIC APIs, including IDM REST, AM OAuth2/OIDC, authentication, authorization, sessions, scripting, CREST, and API auth. Routes to live docs; snapshots fallback."
license: MIT
---

# PingOne AIC API

Learn about new PingOne Advanced Identity Cloud API updates.

## Live source of truth

- Product docs: https://developer.pingidentity.com/pingoneaic-api/
- llms.txt index: https://developer.pingidentity.com/pingoneaic-api/llms.txt
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
| Api Custom Headers.Md: advanced, cloud, custom | api-custom-headers.md | https://developer.pingidentity.com/pingoneaic-api/api-custom-headers.md/*.md | references/snapshots/api-custom-headers-md.md |
| Api Reference.Md: advanced, cloud, identity | api-reference.md | https://developer.pingidentity.com/pingoneaic-api/api-reference.md/*.md | references/snapshots/api-reference-md.md |
| Authenticate To Rest Api Overview.Md: advanced, authenticate, cloud | authenticate-to-rest-api-overview.md | https://developer.pingidentity.com/pingoneaic-api/authenticate-to-rest-api-overview.md/*.md | references/snapshots/authenticate-to-rest-api-overview-md.md |
| Authenticate To Rest Api With Access Token.Md: access, advanced, authenticate | authenticate-to-rest-api-with-access-token.md | https://developer.pingidentity.com/pingoneaic-api/authenticate-to-rest-api-with-access-token.md/*.md | references/snapshots/authenticate-to-rest-api-with-access-token-md.md |
| Authenticate To Rest Api With Api Key And Secret.Md: advanced, authenticate, cloud | authenticate-to-rest-api-with-api-key-and-secret.md | https://developer.pingidentity.com/pingoneaic-api/authenticate-to-rest-api-with-api-key-and-secret.md/*.md | references/snapshots/authenticate-to-rest-api-with-api-key-and-secret-md.md |
| Changelog.Md: about, advanced, changelog | changelog.md | https://developer.pingidentity.com/pingoneaic-api/changelog.md/*.md | references/snapshots/changelog-md.md |
| Index.Md: about, advanced, aic | index.md | https://developer.pingidentity.com/pingoneaic-api/index.md/*.md | references/snapshots/index-md.md |
| Postman Collection.Md: advanced, cloud, collection | postman-collection.md | https://developer.pingidentity.com/pingoneaic-api/postman-collection.md/*.md | references/snapshots/postman-collection-md.md |
| Scripting Auth.Md: auth, scripting | scripting-auth.md | https://developer.pingidentity.com/pingoneaic-api/scripting-auth.md/*.md | references/snapshots/scripting-auth-md.md |
| Scripting Custom Endpoints.Md: custom, endpoints | scripting-custom-endpoints.md | https://developer.pingidentity.com/pingoneaic-api/scripting-custom-endpoints.md/*.md | references/snapshots/scripting-custom-endpoints-md.md |
| Scripting Event Hooks.Md: event, hooks | scripting-event-hooks.md | https://developer.pingidentity.com/pingoneaic-api/scripting-event-hooks.md/*.md | references/snapshots/scripting-event-hooks-md.md |
| Scripting.Md: scripting | scripting.md | https://developer.pingidentity.com/pingoneaic-api/scripting.md/*.md | references/snapshots/scripting-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

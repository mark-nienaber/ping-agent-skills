---
name: developer-resources
description: "Use when working with Developer Resources: oauth 20 developer guide, application integration guide, scim 11 developer guide, federated sso primer, openid connect developer guide, dev jwt jose overview.md. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# Developer Resources

Developer Resources documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/developer-resources/
- llms.txt index: https://docs.pingidentity.com/developer-resources/llms.txt
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
| Oauth 20 Developer Guide: get, tokens, developer | oauth_20_developer_guide | https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/*.md | references/snapshots/oauth-20-developer-guide.md |
| Application Integration Guide: integration, web, integrating | application_integration_guide | https://docs.pingidentity.com/developer-resources/application_integration_guide/*.md | references/snapshots/application-integration-guide.md |
| Scim 11 Developer Guide: scim, action, resource | scim_11_developer_guide | https://docs.pingidentity.com/developer-resources/scim_11_developer_guide/*.md | references/snapshots/scim-11-developer-guide.md |
| Federated Sso Primer: sign, single, sso | federated_sso_primer | https://docs.pingidentity.com/developer-resources/federated_sso_primer/*.md | references/snapshots/federated-sso-primer.md |
| Openid Connect Developer Guide: client, connect, openid | openid_connect_developer_guide | https://docs.pingidentity.com/developer-resources/openid_connect_developer_guide/*.md | references/snapshots/openid-connect-developer-guide.md |
| Dev Jwt Jose Overview.Md: introduction, json, jwt | dev_jwt_jose_overview.md | https://docs.pingidentity.com/developer-resources/dev_jwt_jose_overview.md | references/snapshots/dev-jwt-jose-overview-md.md |
| Index.Md: developer, resources | index.md | https://docs.pingidentity.com/developer-resources/index.md | references/snapshots/index-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

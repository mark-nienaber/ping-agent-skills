---
name: developer-resources
description: "Use when the user explicitly names Developer Resources or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Developer Resources

Developer Resources documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/developer-resources/
- llms.txt index: https://docs.pingidentity.com/developer-resources/llms.txt
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
| Oauth 20 Developer Guide: get, tokens, developer | oauth_20_developer_guide | https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/*.md | references/snapshots/oauth-20-developer-guide.md |
| Application Integration Guide: integration, web, integrating | application_integration_guide | https://docs.pingidentity.com/developer-resources/application_integration_guide/*.md | references/snapshots/application-integration-guide.md |
| Scim 11 Developer Guide: scim, action, resource | scim_11_developer_guide | https://docs.pingidentity.com/developer-resources/scim_11_developer_guide/*.md | references/snapshots/scim-11-developer-guide.md |
| Federated Sso Primer: sign, single, sso | federated_sso_primer | https://docs.pingidentity.com/developer-resources/federated_sso_primer/*.md | references/snapshots/federated-sso-primer.md |
| Openid Connect Developer Guide: client, connect, openid | openid_connect_developer_guide | https://docs.pingidentity.com/developer-resources/openid_connect_developer_guide/*.md | references/snapshots/openid-connect-developer-guide.md |
| Dev Jwt Jose Overview.Md: introduction, json, jwt | dev_jwt_jose_overview.md | https://docs.pingidentity.com/developer-resources/dev_jwt_jose_overview.md | references/snapshots/dev-jwt-jose-overview-md.md |
| Index.Md: developer, resources | index.md | https://docs.pingidentity.com/developer-resources/index.md | references/snapshots/index-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

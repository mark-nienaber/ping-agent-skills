---
name: pingam
description: "Use when the user explicitly names PingAM or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingAM

Secure your resources and manage user access across your network with PingAM, a centralized access management server providing authentication, authorization, web security, and federation services.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingam/
- llms.txt index: https://docs.pingidentity.com/pingam/llms.txt
- Snapshot version: 8.1
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
| Entity Reference: accepttermsandconditions, accepttermsandconditionscollection, accountactivecheck | entity-reference | https://docs.pingidentity.com/pingam/8.1/entity-reference/*.md | references/snapshots/entity-reference.md |
| Am Oauth2: oauth, authorization, token | am-oauth2 | https://docs.pingidentity.com/pingam/8.1/am-oauth2/*.md | references/snapshots/am-oauth2.md |
| Am Authentication: authentication, pingam, authenticate | am-authentication | https://docs.pingidentity.com/pingam/8.1/am-authentication/*.md | references/snapshots/am-authentication.md |
| Release Notes: changes, fixes, deprecated | release-notes | https://docs.pingidentity.com/pingam/release-notes/*.md | references/snapshots/release-notes.md |
| Security: pingam, session, configure | security | https://docs.pingidentity.com/pingam/8.1/security/*.md | references/snapshots/security.md |
| Am Scripting: scripts, scripting, bindings | am-scripting | https://docs.pingidentity.com/pingam/8.1/am-scripting/*.md | references/snapshots/am-scripting.md |
| Installation: pingam, configuration, install | installation | https://docs.pingidentity.com/pingam/8.1/installation/*.md | references/snapshots/installation.md |
| Am Saml2: saml, service, pingam | am-saml2 | https://docs.pingidentity.com/pingam/8.1/am-saml2/*.md | references/snapshots/am-saml2.md |
| Setup: configure, pingam, directory | setup | https://docs.pingidentity.com/pingam/8.1/setup/*.md | references/snapshots/setup.md |
| Am Oidc1: connect, openid, pingam | am-oidc1 | https://docs.pingidentity.com/pingam/8.1/am-oidc1/*.md | references/snapshots/am-oidc1.md |
| Auth Nodes: authentication, nodes, node | auth-nodes | https://docs.pingidentity.com/pingam/8.1/auth-nodes/*.md | references/snapshots/auth-nodes.md |
| Uma: uma, user, access | uma | https://docs.pingidentity.com/pingam/8.1/uma/*.md | references/snapshots/uma.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

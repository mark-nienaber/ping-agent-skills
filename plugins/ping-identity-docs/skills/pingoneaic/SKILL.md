---
name: pingoneaic
description: "Use when working with PingOne Advanced Identity Cloud: identity governance, release notes, am oauth2, tenants, app management, am authentication. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# PingOne Advanced Identity Cloud

Home page for PingOne Advanced Identity Cloud documentation, linking to release notes, getting started guides, tenant management, and troubleshooting resources.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingoneaic/
- llms.txt index: https://docs.pingidentity.com/pingoneaic/llms.txt
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
| Identity Governance: access, create, certification | identity-governance | https://docs.pingidentity.com/pingoneaic/identity-governance/*.md | references/snapshots/identity-governance.md |
| Release Notes: channel, changelog, identity | release-notes | https://docs.pingidentity.com/pingoneaic/release-notes/*.md | references/snapshots/release-notes.md |
| Am Oauth2: authorization, oauth, oauth2 | am-oauth2 | https://docs.pingidentity.com/pingoneaic/am-oauth2/*.md | references/snapshots/am-oauth2.md |
| Tenants: email, configure, configuration | tenants | https://docs.pingidentity.com/pingoneaic/tenants/*.md | references/snapshots/tenants.md |
| App Management: identity, advanced, cloud | app-management | https://docs.pingidentity.com/pingoneaic/app-management/*.md | references/snapshots/app-management.md |
| Am Authentication: authentication, configure, rest | am-authentication | https://docs.pingidentity.com/pingoneaic/am-authentication/*.md | references/snapshots/am-authentication.md |
| Idm Objects: objects, managed, rest | idm-objects | https://docs.pingidentity.com/pingoneaic/idm-objects/*.md | references/snapshots/idm-objects.md |
| Am Scripting: scripts, scripting, bindings | am-scripting | https://docs.pingidentity.com/pingoneaic/am-scripting/*.md | references/snapshots/am-scripting.md |
| Idm Synchronization: synchronization, data, objects | idm-synchronization | https://docs.pingidentity.com/pingoneaic/idm-synchronization/*.md | references/snapshots/idm-synchronization.md |
| Use Cases: identity, advanced, cloud | use-cases | https://docs.pingidentity.com/pingoneaic/use-cases/*.md | references/snapshots/use-cases.md |
| Am Oidc1: connect, openid, oauth2 | am-oidc1 | https://docs.pingidentity.com/pingoneaic/am-oidc1/*.md | references/snapshots/am-oidc1.md |
| Identities: identity, advanced, configure | identities | https://docs.pingidentity.com/pingoneaic/identities/*.md | references/snapshots/identities.md |
| Am Saml2: saml, federation, identities | am-saml2 | https://docs.pingidentity.com/pingoneaic/am-saml2/*.md | references/snapshots/am-saml2.md |
| Idm Rest Api: rest, operations, managed | idm-rest-api | https://docs.pingidentity.com/pingoneaic/idm-rest-api/*.md | references/snapshots/idm-rest-api.md |
| Idm Scripting: scripts, script, configuration | idm-scripting | https://docs.pingidentity.com/pingoneaic/idm-scripting/*.md | references/snapshots/idm-scripting.md |
| Developer Docs: identity, advanced, cloud | developer-docs | https://docs.pingidentity.com/pingoneaic/developer-docs/*.md | references/snapshots/developer-docs.md |
| Realms: identity, advanced, cloud | realms | https://docs.pingidentity.com/pingoneaic/realms/*.md | references/snapshots/realms.md |
| Am Authorization: policy, policies, authorization | am-authorization | https://docs.pingidentity.com/pingoneaic/am-authorization/*.md | references/snapshots/am-authorization.md |
| Getting Started: identity, task, advanced | getting-started | https://docs.pingidentity.com/pingoneaic/getting-started/*.md | references/snapshots/getting-started.md |
| Product Information: identity, cloud, advanced | product-information | https://docs.pingidentity.com/pingoneaic/product-information/*.md | references/snapshots/product-information.md |
| End User: identity, advanced, cloud | end-user | https://docs.pingidentity.com/pingoneaic/end-user/*.md | references/snapshots/end-user.md |
| Idm Schedules: schedules, tasks, configure | idm-schedules | https://docs.pingidentity.com/pingoneaic/idm-schedules/*.md | references/snapshots/idm-schedules.md |
| Planning: identity, cloud, advanced | planning | https://docs.pingidentity.com/pingoneaic/planning/*.md | references/snapshots/planning.md |
| Reports: custom, reports, create | reports | https://docs.pingidentity.com/pingoneaic/reports/*.md | references/snapshots/reports.md |
| Am Sessions: sessions, session, side | am-sessions | https://docs.pingidentity.com/pingoneaic/am-sessions/*.md | references/snapshots/am-sessions.md |
| Journeys: journey, nodes, authentication | journeys | https://docs.pingidentity.com/pingoneaic/journeys/*.md | references/snapshots/journeys.md |
| Self Service: identity, advanced, cloud | self-service | https://docs.pingidentity.com/pingoneaic/self-service/*.md | references/snapshots/self-service.md |
| Integrations: pingone, credentials, identity | integrations | https://docs.pingidentity.com/pingoneaic/integrations/*.md | references/snapshots/integrations.md |
| Idm Auth: authentication, access, authorization | idm-auth | https://docs.pingidentity.com/pingoneaic/idm-auth/*.md | references/snapshots/idm-auth.md |
| Am Reference: secret, access, across | am-reference | https://docs.pingidentity.com/pingoneaic/am-reference/*.md | references/snapshots/am-reference.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

---
name: pingam
description: "Use when configuring PingAM access management, authentication journeys, OAuth2/OIDC, SAML2 federation, sessions, security, Amster, REST APIs, or upgrade and install work. Routes to live docs; snapshots fallback."
license: MIT
---

# PingAM

Secure your resources and manage user access across your network with PingAM, a centralized access management server providing authentication, authorization, web security, and federation services.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingam/
- llms.txt index: https://docs.pingidentity.com/pingam/llms.txt
- Snapshot version: 8.1
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Entity Reference: accepttermsandconditions, accepttermsandconditionscollection, accountactivecheck | entity-reference | https://docs.pingidentity.com/pingam/8.1/entity-reference/*.md | references/snapshots/entity-reference.md |
| Am Oauth2: oauth, authorization, token | am-oauth2 | https://docs.pingidentity.com/pingam/8.1/am-oauth2/*.md | references/snapshots/am-oauth2.md |
| Am Authentication: authentication, pingam, authenticate | am-authentication | https://docs.pingidentity.com/pingam/8.1/am-authentication/*.md | references/snapshots/am-authentication.md |
| Security: pingam, session, configure | security | https://docs.pingidentity.com/pingam/8.1/security/*.md | references/snapshots/security.md |
| Am Scripting: scripts, scripting, bindings | am-scripting | https://docs.pingidentity.com/pingam/8.1/am-scripting/*.md | references/snapshots/am-scripting.md |
| Installation: pingam, configuration, install | installation | https://docs.pingidentity.com/pingam/8.1/installation/*.md | references/snapshots/installation.md |
| Am Saml2: saml, service, pingam | am-saml2 | https://docs.pingidentity.com/pingam/8.1/am-saml2/*.md | references/snapshots/am-saml2.md |
| Setup: configure, pingam, directory | setup | https://docs.pingidentity.com/pingam/8.1/setup/*.md | references/snapshots/setup.md |
| Am Oidc1: connect, openid, pingam | am-oidc1 | https://docs.pingidentity.com/pingam/8.1/am-oidc1/*.md | references/snapshots/am-oidc1.md |
| Auth Nodes: authentication, nodes, node | auth-nodes | https://docs.pingidentity.com/pingam/8.1/auth-nodes/*.md | references/snapshots/auth-nodes.md |
| Uma: uma, user, access | uma | https://docs.pingidentity.com/pingam/8.1/uma/*.md | references/snapshots/uma.md |
| Am Authorization: policies, policy, pingam | am-authorization | https://docs.pingidentity.com/pingam/8.1/am-authorization/*.md | references/snapshots/am-authorization.md |
| Am Sessions: sessions, side, session | am-sessions | https://docs.pingidentity.com/pingam/8.1/am-sessions/*.md | references/snapshots/am-sessions.md |
| Monitoring: monitoring, pingam, logging | monitoring | https://docs.pingidentity.com/pingam/8.1/monitoring/*.md | references/snapshots/monitoring.md |
| Deployment Planning: deployment, pingam, requirements | deployment-planning | https://docs.pingidentity.com/pingam/8.1/deployment-planning/*.md | references/snapshots/deployment-planning.md |
| User Self Service: configure, user, self | user-self-service | https://docs.pingidentity.com/pingam/8.1/user-self-service/*.md | references/snapshots/user-self-service.md |
| Amster: configuration, amster, pingam | amster | https://docs.pingidentity.com/pingam/8.1/amster/*.md | references/snapshots/amster.md |
| Maintenance: pingam, recording, tuning | maintenance | https://docs.pingidentity.com/pingam/8.1/maintenance/*.md | references/snapshots/maintenance.md |
| Sts: token, service, security | sts | https://docs.pingidentity.com/pingam/8.1/sts/*.md | references/snapshots/sts.md |
| Cts: cts, token, tokens | cts | https://docs.pingidentity.com/pingam/8.1/cts/*.md | references/snapshots/cts.md |
| Upgrade: upgrade, pingam, your | upgrade | https://docs.pingidentity.com/pingam/8.1/upgrade/*.md | references/snapshots/upgrade.md |
| Evaluation: pingam, user, store | evaluation | https://docs.pingidentity.com/pingam/8.1/evaluation/*.md | references/snapshots/evaluation.md |
| Am Rest: rest, pingam, endpoints | am-rest | https://docs.pingidentity.com/pingam/8.1/am-rest/*.md | references/snapshots/am-rest.md |
| Ui Customization: user, customize, pingam | ui-customization | https://docs.pingidentity.com/pingam/8.1/ui-customization/*.md | references/snapshots/ui-customization.md |
| Am Reference: endpoints, pingam, reference | am-reference | https://docs.pingidentity.com/pingam/8.1/am-reference/*.md | references/snapshots/am-reference.md |
| Root: access, pingam, your | root | https://docs.pingidentity.com/pingam/8.1/*.md | references/snapshots/root.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

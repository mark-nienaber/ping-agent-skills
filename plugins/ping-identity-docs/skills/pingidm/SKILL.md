---
name: pingidm
description: "Use when administering PingIDM, including managed objects, synchronization, connectors, REST APIs, scripts, schedules, audit, samples, installation, and security. Routes to live docs; snapshots fallback."
license: MIT
---

# PingIDM

Overview of PingIDM: Reconciling user accounts across distributed data stores and resources.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingidm/
- llms.txt index: https://docs.pingidentity.com/pingidm/llms.txt
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
| Objects Guide: objects, pingidm, managed | objects-guide | https://docs.pingidentity.com/pingidm/8.1/objects-guide/*.md | references/snapshots/objects-guide.md |
| Synchronization Guide: pingidm, mapping, synchronization | synchronization-guide | https://docs.pingidentity.com/pingidm/8.1/synchronization-guide/*.md | references/snapshots/synchronization-guide.md |
| Install Guide: pingidm, cluster, configuration | install-guide | https://docs.pingidentity.com/pingidm/8.1/install-guide/*.md | references/snapshots/install-guide.md |
| Audit Guide: audit, event, pingidm | audit-guide | https://docs.pingidentity.com/pingidm/8.1/audit-guide/*.md | references/snapshots/audit-guide.md |
| Samples Guide: pingidm, users, ldap | samples-guide | https://docs.pingidentity.com/pingidm/8.1/samples-guide/*.md | references/snapshots/samples-guide.md |
| Rest Api Reference: rest, pingidm, endpoints | rest-api-reference | https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/*.md | references/snapshots/rest-api-reference.md |
| Scripting Guide: pingidm, configuration, script | scripting-guide | https://docs.pingidentity.com/pingidm/8.1/scripting-guide/*.md | references/snapshots/scripting-guide.md |
| Security Guide: pingidm, secret, encryption | security-guide | https://docs.pingidentity.com/pingidm/8.1/security-guide/*.md | references/snapshots/security-guide.md |
| Setup Guide: pingidm, admin, configuration | setup-guide | https://docs.pingidentity.com/pingidm/8.1/setup-guide/*.md | references/snapshots/setup-guide.md |
| Auth Guide: authentication, pingidm, user | auth-guide | https://docs.pingidentity.com/pingidm/8.1/auth-guide/*.md | references/snapshots/auth-guide.md |
| Schedules Guide: pingidm, tasks, scanning | schedules-guide | https://docs.pingidentity.com/pingidm/8.1/schedules-guide/*.md | references/snapshots/schedules-guide.md |
| Pwd Plugin Guide: password, synchronization, active | pwd-plugin-guide | https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/*.md | references/snapshots/pwd-plugin-guide.md |
| Release Notes: pingidm, release, features | release-notes | https://docs.pingidentity.com/pingidm/8.1/release-notes/*.md | references/snapshots/release-notes.md |
| Crest: rest, common, http | crest | https://docs.pingidentity.com/pingidm/8.1/crest/*.md | references/snapshots/crest.md |
| Monitoring Guide: pingidm, metrics, prometheus | monitoring-guide | https://docs.pingidentity.com/pingidm/8.1/monitoring-guide/*.md | references/snapshots/monitoring-guide.md |
| Workflow Guide: workflow, pingidm, workflows | workflow-guide | https://docs.pingidentity.com/pingidm/8.1/workflow-guide/*.md | references/snapshots/workflow-guide.md |
| Upgrade Guide: pingidm, upgrade, repository | upgrade-guide | https://docs.pingidentity.com/pingidm/8.1/upgrade-guide/*.md | references/snapshots/upgrade-guide.md |
| External Services Guide: email, rest, external | external-services-guide | https://docs.pingidentity.com/pingidm/8.1/external-services-guide/*.md | references/snapshots/external-services-guide.md |
| Getting Started: pingidm, management, software | getting-started | https://docs.pingidentity.com/pingidm/8.1/getting-started/*.md | references/snapshots/getting-started.md |
| Root: glossary, idm, jwt | root | https://docs.pingidentity.com/pingidm/8.1/*.md | references/snapshots/root.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

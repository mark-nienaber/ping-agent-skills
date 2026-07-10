---
name: pingds
description: "Use when working with PingDS: schemaref, configref, config guide, tools reference, security guide, release notes. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# PingDS

Introduction to LDAP directory concepts including data model, communication, controls, indexes, schema, access control, replication, and HTTP access.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingds/
- llms.txt index: https://docs.pingidentity.com/pingds/llms.txt
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
| Schemaref: attribute, about, account | schemaref | https://docs.pingidentity.com/pingds/8.1/schemaref/*.md | references/snapshots/schemaref.md |
| Configref: password, handler, scheme | configref | https://docs.pingidentity.com/pingds/8.1/configref/*.md | references/snapshots/configref.md |
| Config Guide: pingds, replication, configure | config-guide | https://docs.pingidentity.com/pingds/8.1/config-guide/*.md | references/snapshots/config-guide.md |
| Tools Reference: ldif, about, addrate | tools-reference | https://docs.pingidentity.com/pingds/8.1/tools-reference/*.md | references/snapshots/tools-reference.md |
| Security Guide: pingds, password, policies | security-guide | https://docs.pingidentity.com/pingds/8.1/security-guide/*.md | references/snapshots/security-guide.md |
| Release Notes: pingds, fixes, releases | release-notes | https://docs.pingidentity.com/pingds/release-notes/*.md | live-only |
| Install Guide: install, pingds, setup | install-guide | https://docs.pingidentity.com/pingds/8.1/install-guide/*.md | references/snapshots/install-guide.md |
| Upgrade Guide: upgrade, new, pingds | upgrade-guide | https://docs.pingidentity.com/pingds/8.1/upgrade-guide/*.md | references/snapshots/upgrade-guide.md |
| Getting Started: learn, pingds, access | getting-started | https://docs.pingidentity.com/pingds/8.1/getting-started/*.md | references/snapshots/getting-started.md |
| Ldap Guide: ldap, pingds, tools | ldap-guide | https://docs.pingidentity.com/pingds/8.1/ldap-guide/*.md | references/snapshots/ldap-guide.md |
| Monitoring Guide: pingds, metrics, monitor | monitoring-guide | https://docs.pingidentity.com/pingds/8.1/monitoring-guide/*.md | references/snapshots/monitoring-guide.md |
| Rest Guide: hdap, pingds, http | rest-guide | https://docs.pingidentity.com/pingds/8.1/rest-guide/*.md | references/snapshots/rest-guide.md |
| Use Cases: pingds, password, backup | use-cases | https://docs.pingidentity.com/pingds/8.1/use-cases/*.md | references/snapshots/use-cases.md |
| Deployment Guide: deployment, pingds, project | deployment-guide | https://docs.pingidentity.com/pingds/8.1/deployment-guide/*.md | references/snapshots/deployment-guide.md |
| Maintenance Guide: pingds, server, account | maintenance-guide | https://docs.pingidentity.com/pingds/8.1/maintenance-guide/*.md | references/snapshots/maintenance-guide.md |
| Ldap Reference: ldap, supported, reference | ldap-reference | https://docs.pingidentity.com/pingds/8.1/ldap-reference/*.md | references/snapshots/ldap-reference.md |
| Logging Guide: log, access, logging | logging-guide | https://docs.pingidentity.com/pingds/8.1/logging-guide/*.md | references/snapshots/logging-guide.md |
| Log Reference: log, message, reference | log-reference | https://docs.pingidentity.com/pingds/8.1/log-reference/*.md | references/snapshots/log-reference.md |
| Release Notes: notes, release, all | release-notes | https://docs.pingidentity.com/pingds/8.1/release-notes/*.md | live-only |
| Root: pingds | root | https://docs.pingidentity.com/pingds/8.1/*.md | references/snapshots/root.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

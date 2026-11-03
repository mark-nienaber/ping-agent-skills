---
name: pingds
description: "Use when the user explicitly names PingDS or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingDS

Introduction to LDAP directory concepts including data model, communication, controls, indexes, schema, access control, replication, and HTTP access.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingds/
- llms.txt index: https://docs.pingidentity.com/pingds/llms.txt
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
| Schemaref: attribute, about, account | schemaref | https://docs.pingidentity.com/pingds/8.1/schemaref/*.md | references/snapshots/schemaref.md |
| Configref: password, handler, scheme | configref | https://docs.pingidentity.com/pingds/8.1/configref/*.md | references/snapshots/configref.md |
| Config Guide: pingds, replication, configure | config-guide | https://docs.pingidentity.com/pingds/8.1/config-guide/*.md | references/snapshots/config-guide.md |
| Tools Reference: ldif, about, addrate | tools-reference | https://docs.pingidentity.com/pingds/8.1/tools-reference/*.md | references/snapshots/tools-reference.md |
| Security Guide: pingds, password, policies | security-guide | https://docs.pingidentity.com/pingds/8.1/security-guide/*.md | references/snapshots/security-guide.md |
| Release Notes: pingds, fixes, releases | release-notes | https://docs.pingidentity.com/pingds/release-notes/*.md | references/snapshots/release-notes.md |
| Install Guide: install, pingds, setup | install-guide | https://docs.pingidentity.com/pingds/8.1/install-guide/*.md | references/snapshots/install-guide.md |
| Upgrade Guide: upgrade, new, pingds | upgrade-guide | https://docs.pingidentity.com/pingds/8.1/upgrade-guide/*.md | references/snapshots/upgrade-guide.md |
| Getting Started: learn, pingds, access | getting-started | https://docs.pingidentity.com/pingds/8.1/getting-started/*.md | references/snapshots/getting-started.md |
| Ldap Guide: ldap, pingds, tools | ldap-guide | https://docs.pingidentity.com/pingds/8.1/ldap-guide/*.md | references/snapshots/ldap-guide.md |
| Monitoring Guide: pingds, metrics, monitor | monitoring-guide | https://docs.pingidentity.com/pingds/8.1/monitoring-guide/*.md | references/snapshots/monitoring-guide.md |
| Rest Guide: hdap, pingds, http | rest-guide | https://docs.pingidentity.com/pingds/8.1/rest-guide/*.md | references/snapshots/rest-guide.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

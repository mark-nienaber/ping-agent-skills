---
name: pingidm
description: "Use when the user explicitly names PingIDM or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingIDM

Overview of PingIDM: Reconciling user accounts across distributed data stores and resources.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingidm/
- llms.txt index: https://docs.pingidentity.com/pingidm/llms.txt
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

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

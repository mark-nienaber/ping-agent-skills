---
name: pingaccess
description: "Use when the user explicitly names PingAccess or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingAccess

Learn how you can use authentication challenge policies and authentication requirements in PingAccess to manage how users authenticate.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingaccess/
- llms.txt index: https://docs.pingidentity.com/pingaccess/llms.txt
- Snapshot version: 9.1
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
| Pingaccess User Interface Reference Guide: adding, rules, request | pingaccess_user_interface_reference_guide | https://docs.pingidentity.com/pingaccess/9.1/pingaccess_user_interface_reference_guide/*.md | references/snapshots/pingaccess-user-interface-reference-guide.md |
| Agents And Integrations: sdk, com, agent | agents_and_integrations | https://docs.pingidentity.com/pingaccess/9.1/agents_and_integrations/*.md | references/snapshots/agents-and-integrations.md |
| Reference Guides: deployment, architecture, configuring | reference_guides | https://docs.pingidentity.com/pingaccess/9.1/reference_guides/*.md | references/snapshots/reference-guides.md |
| Configuring And Customizing Pingaccess: logging, enabling, configuring | configuring_and_customizing_pingaccess | https://docs.pingidentity.com/pingaccess/9.1/configuring_and_customizing_pingaccess/*.md | references/snapshots/configuring-and-customizing-pingaccess.md |
| Pingaccess Use Cases: configuring, host, rule | pingaccess_use_cases | https://docs.pingidentity.com/pingaccess/9.1/pingaccess_use_cases/*.md | references/snapshots/pingaccess-use-cases.md |
| Token Providers: configuring, pingaccess, creating | token_providers | https://docs.pingidentity.com/pingaccess/9.1/token_providers/*.md | references/snapshots/token-providers.md |
| Installing And Uninstalling Pingaccess: pingaccess, service, windows | installing_and_uninstalling_pingaccess | https://docs.pingidentity.com/pingaccess/9.1/installing_and_uninstalling_pingaccess/*.md | references/snapshots/installing-and-uninstalling-pingaccess.md |
| Pingaccess Zero Downtime Upgrade: key, rolling, disabling | pingaccess_zero_downtime_upgrade | https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/*.md | references/snapshots/pingaccess-zero-downtime-upgrade.md |
| Upgrading Pingaccess: pingaccess, upgrade, upgrading | upgrading_pingaccess | https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/*.md | references/snapshots/upgrading-pingaccess.md |
| Pingaccess Monitoring Guide: connecting, heartbeat, log | pingaccess_monitoring_guide | https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/*.md | references/snapshots/pingaccess-monitoring-guide.md |
| Troubleshooting: sso, administrative, disable | troubleshooting | https://docs.pingidentity.com/pingaccess/9.1/troubleshooting/*.md | references/snapshots/troubleshooting.md |
| Backing Up And Restoring Pingaccess: pingaccess, code, backing | backing_up_and_restoring_pingaccess | https://docs.pingidentity.com/pingaccess/9.1/backing_up_and_restoring_pingaccess/*.md | references/snapshots/backing-up-and-restoring-pingaccess.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

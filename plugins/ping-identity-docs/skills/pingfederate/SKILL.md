---
name: pingfederate
description: "Use when the user explicitly names PingFederate or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingFederate

All the pre-runtime architectural and setup tasks necessary to prepare the PingFederate server and its dependencies before it handles live traffic.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingfederate/
- llms.txt index: https://docs.pingidentity.com/pingfederate/llms.txt
- Snapshot version: 13.1
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
| Administrators Reference Guide: adding, administrative, adapter | administrators_reference_guide | https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/*.md | references/snapshots/administrators-reference-guide.md |
| Introduction To Pingfederate: multiple, bridging, about | introduction_to_pingfederate | https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/*.md | references/snapshots/introduction-to-pingfederate.md |
| Release Notes: pingfederate, february, december | release_notes | https://docs.pingidentity.com/pingfederate/13.1/release_notes/*.md | references/snapshots/release-notes.md |
| Developers Reference Guide: authentication, authorization, enabling | developers_reference_guide | https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/*.md | references/snapshots/developers-reference-guide.md |
| Server Clustering Guide: service, active, administrative | server_clustering_guide | https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/*.md | references/snapshots/server-clustering-guide.md |
| Sdk Developers Guide: developing, adapters, authentication | sdk_developers_guide | https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/*.md | references/snapshots/sdk-developers-guide.md |
| Upgrading Pingfederate: upgrade, pingfederate, considerations | upgrading_pingfederate | https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/*.md | references/snapshots/upgrading-pingfederate.md |
| Getting Started With Pingfederate: pingfederate, console, integrating | getting_started_with_pingfederate | https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/*.md | references/snapshots/getting-started-with-pingfederate.md |
| Performance Tuning Guide: tuning, jvm, memoryoptions | performance_tuning_guide | https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/*.md | references/snapshots/performance-tuning-guide.md |
| Installing And Uninstalling Pingfederate: pingfederate, installing, windows | installing_and_uninstalling_pingfederate | https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/*.md | references/snapshots/installing-and-uninstalling-pingfederate.md |
| Pingfederate Monitoring Guide: connecting, monitoring, jmx | pingfederate_monitoring_guide | https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/*.md | references/snapshots/pingfederate-monitoring-guide.md |
| Root: pingfederate | root | https://docs.pingidentity.com/pingfederate/13.1/*.md | references/snapshots/root.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

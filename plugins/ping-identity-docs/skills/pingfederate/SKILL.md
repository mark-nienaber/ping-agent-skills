---
name: pingfederate
description: "Use when configuring PingFederate SSO, federation, OAuth2/OIDC, SAML, adapters, grants, clustering, SDK development, administration, and release notes. Routes to live docs; snapshots fallback."
license: MIT
---

# PingFederate

All the pre-runtime architectural and setup tasks necessary to prepare the PingFederate server and its dependencies before it handles live traffic.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingfederate/
- llms.txt index: https://docs.pingidentity.com/pingfederate/llms.txt
- Snapshot version: 13.1
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

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

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

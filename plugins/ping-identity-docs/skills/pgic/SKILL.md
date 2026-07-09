---
name: pgic
description: "Use when working with PGIC: service requests, products and self service tasks, environments, identity federation, index.md, introduction. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# PGIC

PGIC documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pgic/
- llms.txt index: https://docs.pingidentity.com/pgic/llms.txt
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
| Service Requests: certificates, connection, dns | service_requests | https://docs.pingidentity.com/pgic/service_requests/*.md | references/snapshots/service-requests.md |
| Products And Self Service Tasks: pingfederate, self, service | products_and_self-service_tasks | https://docs.pingidentity.com/pgic/products_and_self-service_tasks/*.md | references/snapshots/products-and-self-service-tasks.md |
| Environments: environments | environments | https://docs.pingidentity.com/pgic/environments/*.md | references/snapshots/environments.md |
| Identity Federation: identity, federation, provisioning | identity_federation | https://docs.pingidentity.com/pgic/identity_federation/*.md | references/snapshots/identity-federation.md |
| Index.Md: cloud, government, identity | index.md | https://docs.pingidentity.com/pgic/index.md | references/snapshots/index-md.md |
| Introduction: cloud, government, identity | introduction | https://docs.pingidentity.com/pgic/introduction/*.md | references/snapshots/introduction.md |
| Maintenance: maintenance, network, ongoing | maintenance | https://docs.pingidentity.com/pgic/maintenance/*.md | references/snapshots/maintenance.md |
| Network: connectivity, guide, network | network | https://docs.pingidentity.com/pgic/network/*.md | references/snapshots/network.md |
| Penentration Load Testing: load, penetration, testing | penentration_load_testing | https://docs.pingidentity.com/pgic/penentration_load_testing/*.md | references/snapshots/penentration-load-testing.md |
| Pgic Data Loading.Md: access, data, loading | pgic_data_loading.md | https://docs.pingidentity.com/pgic/pgic_data_loading.md | references/snapshots/pgic-data-loading-md.md |
| Pgic Infrastructure.Md: infrastructure, regions, supported | pgic_infrastructure.md | https://docs.pingidentity.com/pgic/pgic_infrastructure.md | references/snapshots/pgic-infrastructure-md.md |
| Pgic Observability.Md: logging, observability | pgic_observability.md | https://docs.pingidentity.com/pgic/pgic_observability.md | references/snapshots/pgic-observability-md.md |
| Pgic Task Summary Table: summary, table, task | pgic_task_summary_table | https://docs.pingidentity.com/pgic/pgic_task_summary_table/*.md | references/snapshots/pgic-task-summary-table.md |
| Pgic Web Servers.Md: ingress, servers, web | pgic_web_servers.md | https://docs.pingidentity.com/pgic/pgic_web_servers.md | references/snapshots/pgic-web-servers-md.md |
| Secure Containers.Md: containers, secure | secure-containers.md | https://docs.pingidentity.com/pgic/secure-containers.md | references/snapshots/secure-containers-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

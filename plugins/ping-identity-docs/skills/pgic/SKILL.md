---
name: pgic
description: "Use when the user explicitly names PGIC or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PGIC

PGIC documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pgic/
- llms.txt index: https://docs.pingidentity.com/pgic/llms.txt
- Snapshot version: current
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

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

---
name: pingoneadvancedservices
description: "Use when the user explicitly names PingOne Advanced Services or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingOne Advanced Services

The home page for the PingOne Advanced Services guide.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingoneadvancedservices/
- llms.txt index: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
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
| Task Summary Table: request, instructions, completing | task_summary_table | https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/*.md | references/snapshots/task-summary-table.md |
| Release Notes: platform, version, march | release_notes | https://docs.pingidentity.com/pingoneadvancedservices/release_notes/*.md | references/snapshots/release-notes.md |
| Introduction To Pingone Advanced Services: additional, advanced, benefits | introduction_to_pingone_advanced_services | https://docs.pingidentity.com/pingoneadvancedservices/introduction_to_pingone_advanced_services/*.md | live-only |
| Environments: considerations, data, environments | environments | https://docs.pingidentity.com/pingoneadvancedservices/environments/*.md | live-only |
| Comparison Pingone Advanced Services And Pingone Cloud Platform: pingone, advanced, cloud | comparison_pingone_advanced_services_and_pingone_cloud_platform | https://docs.pingidentity.com/pingoneadvancedservices/comparison_pingone_advanced_services_and_pingone_cloud_platform/*.md | live-only |
| Limitations Guide: guide, limitations | limitations_guide | https://docs.pingidentity.com/pingoneadvancedservices/limitations_guide/*.md | references/snapshots/limitations-guide.md |
| Monitoring And Logging: logging, monitoring | monitoring_and_logging | https://docs.pingidentity.com/pingoneadvancedservices/monitoring_and_logging/*.md | references/snapshots/monitoring-and-logging.md |
| Network Guide: guide, network | network_guide | https://docs.pingidentity.com/pingoneadvancedservices/network_guide/*.md | references/snapshots/network-guide.md |
| P1As Home.Md: advanced, pingone, services | p1as_home.md | https://docs.pingidentity.com/pingoneadvancedservices/p1as_home.md | references/snapshots/p1as-home-md.md |
| P1As How Works.Md: advanced, pingone, services | p1as_how_works.md | https://docs.pingidentity.com/pingoneadvancedservices/p1as_how_works.md | references/snapshots/p1as-how-works-md.md |
| P1As Load Testing.Md: load, penetration, testing | p1as_load_testing.md | https://docs.pingidentity.com/pingoneadvancedservices/p1as_load_testing.md | references/snapshots/p1as-load-testing-md.md |
| P1As Support Policy.Md: policy, support, about | p1as_support_policy.md | https://docs.pingidentity.com/pingoneadvancedservices/p1as_support_policy.md | references/snapshots/p1as-support-policy-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

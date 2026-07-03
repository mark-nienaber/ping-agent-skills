---
name: config-automation-promotion
description: "Use when designing Ping configuration promotion pipelines, promoting configuration between environments, using promotion concepts, or reviewing pipeline examples. Routes to live docs; snapshots fallback."
license: MIT
---

# Config Automation Promotion

Config Automation Promotion documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/config-automation-promotion/
- llms.txt index: https://developer.pingidentity.com/config-automation-promotion/llms.txt
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
| Concepts: configuration, automation, auditing | concepts | https://developer.pingidentity.com/config-automation-promotion/concepts/*.md | references/snapshots/concepts.md |
| Configuration Promotion Landing Page.Md: configuration, identity, promotion | configuration_promotion_landing_page.md | https://developer.pingidentity.com/config-automation-promotion/configuration_promotion_landing_page.md/*.md | references/snapshots/configuration-promotion-landing-page-md.md |
| Configuration Promotion Pipeline Examples.Md: examples, gitops, pipeline | configuration_promotion_pipeline_examples.md | https://developer.pingidentity.com/config-automation-promotion/configuration_promotion_pipeline_examples.md/*.md | references/snapshots/configuration-promotion-pipeline-examples-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

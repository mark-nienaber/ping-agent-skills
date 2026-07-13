---
name: config-automation-promotion
description: "Use when the user explicitly names Config Automation Promotion or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Config Automation Promotion

Config Automation Promotion documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/config-automation-promotion/
- llms.txt index: https://developer.pingidentity.com/config-automation-promotion/llms.txt
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
| Concepts: configuration, automation, auditing | concepts | https://developer.pingidentity.com/config-automation-promotion/concepts/*.md | references/snapshots/concepts.md |
| Configuration Promotion Landing Page.Md: configuration, identity, promotion | configuration_promotion_landing_page.md | https://developer.pingidentity.com/config-automation-promotion/configuration_promotion_landing_page.md | references/snapshots/configuration-promotion-landing-page-md.md |
| Configuration Promotion Pipeline Examples.Md: examples, gitops, pipeline | configuration_promotion_pipeline_examples.md | https://developer.pingidentity.com/config-automation-promotion/configuration_promotion_pipeline_examples.md | references/snapshots/configuration-promotion-pipeline-examples-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

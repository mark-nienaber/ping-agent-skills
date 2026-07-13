---
name: licensing-guide
description: "Use when the user explicitly names Licensing Guide or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Licensing Guide

Licensing information for Ping Identity advanced identity software products, including features, packaging, and managed (stored) identity unit of measure.

## Live source of truth

- Product docs: https://docs.pingidentity.com/licensing-guide/
- llms.txt index: https://docs.pingidentity.com/licensing-guide/llms.txt
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
| Advanced Identity Software.Md: identity, advanced, software | advanced-identity-software.md | https://docs.pingidentity.com/licensing-guide/advanced-identity-software.md | references/snapshots/advanced-identity-software-md.md |
| Archive: archive, archived, components | archive | https://docs.pingidentity.com/licensing-guide/archive/*.md | references/snapshots/archive.md |
| Index.Md: licensing, guide, identity | index.md | https://docs.pingidentity.com/licensing-guide/index.md | references/snapshots/index-md.md |
| Licensing Basics.Md: licensing, production, basics | licensing-basics.md | https://docs.pingidentity.com/licensing-guide/licensing-basics.md | references/snapshots/licensing-basics-md.md |
| Multitenant Saas.Md: multi, pingone, saas | multitenant-saas.md | https://docs.pingidentity.com/licensing-guide/multitenant-saas.md | references/snapshots/multitenant-saas-md.md |
| Ping Government Identity Cloud.Md: identity, cloud, government | ping-government-identity-cloud.md | https://docs.pingidentity.com/licensing-guide/ping-government-identity-cloud.md | references/snapshots/ping-government-identity-cloud-md.md |
| Pingone Advanced Identity Cloud.Md: advanced, cloud, identity | pingone-advanced-identity-cloud.md | https://docs.pingidentity.com/licensing-guide/pingone-advanced-identity-cloud.md | references/snapshots/pingone-advanced-identity-cloud-md.md |
| Pingone Advanced Services.Md: advanced, pingone, services | pingone-advanced-services.md | https://docs.pingidentity.com/licensing-guide/pingone-advanced-services.md | references/snapshots/pingone-advanced-services-md.md |
| Release Notes: licensing, guide, identity | release_notes | https://docs.pingidentity.com/licensing-guide/release_notes/*.md | references/snapshots/release-notes.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

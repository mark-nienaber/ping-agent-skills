---
name: licensing-guide
description: "Use when working with Licensing Guide: advanced identity software.md, archive, index.md, licensing basics.md, multitenant saas.md, ping government identity cloud.md. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# Licensing Guide

Licensing information for Ping Identity advanced identity software products, including features, packaging, and managed (stored) identity unit of measure.

## Live source of truth

- Product docs: https://docs.pingidentity.com/licensing-guide/
- llms.txt index: https://docs.pingidentity.com/licensing-guide/llms.txt
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

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

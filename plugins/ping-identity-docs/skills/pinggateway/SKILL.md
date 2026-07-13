---
name: pinggateway
description: "Use when the user explicitly names PingGateway or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingGateway

Landing page for PingGateway documentation: get started, installation, upgrade, integration guides, troubleshooting, and community resources.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pinggateway/
- llms.txt index: https://docs.pingidentity.com/pinggateway/llms.txt
- Snapshot version: 2026
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
| Reference: pinggateway, configure, reference | reference | https://docs.pingidentity.com/pinggateway/2026/reference/*.md | live-only |
| Gateway Guide: pingam, pinggateway, configure | gateway-guide | https://docs.pingidentity.com/pinggateway/2026/gateway-guide/*.md | live-only |
| Release Notes: pinggateway, release, version | release-notes | https://docs.pingidentity.com/pinggateway/release-notes/*.md | live-only |
| Aic: identity, advanced, cloud | aic | https://docs.pingidentity.com/pinggateway/2026/aic/*.md | live-only |
| Studio Guide: studio, routes, pinggateway | studio-guide | https://docs.pingidentity.com/pinggateway/2026/studio-guide/*.md | live-only |
| Fapi: fapi, pinggateway, identity | fapi | https://docs.pingidentity.com/pinggateway/2026/fapi/*.md | live-only |
| Installation Guide: pinggateway, configure, jwt | installation-guide | https://docs.pingidentity.com/pinggateway/2026/installation-guide/*.md | live-only |
| Maintenance Guide: pinggateway, configure, deployment | maintenance-guide | https://docs.pingidentity.com/pinggateway/2026/maintenance-guide/*.md | live-only |
| About: pinggateway, proxy, descriptors | about | https://docs.pingidentity.com/pinggateway/2026/about/*.md | live-only |
| Configure: pinggateway, routes, configure | configure | https://docs.pingidentity.com/pinggateway/2026/configure/*.md | live-only |
| Getting Started: pinggateway, configure, application | getting-started | https://docs.pingidentity.com/pinggateway/2026/getting-started/*.md | live-only |
| Security Guide: pinggateway, access, security | security-guide | https://docs.pingidentity.com/pinggateway/2026/security-guide/*.md | live-only |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

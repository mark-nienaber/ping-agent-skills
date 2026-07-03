---
name: pinggateway
description: "Use when configuring PingGateway, including routes, filters, handlers, Studio, AIC integration, installation, security, maintenance, and troubleshooting. Routes to live docs; snapshots fallback."
license: MIT
---

# PingGateway

Landing page for PingGateway documentation: get started, installation, upgrade, integration guides, troubleshooting, and community resources.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pinggateway/
- llms.txt index: https://docs.pingidentity.com/pinggateway/llms.txt
- Snapshot version: 2026
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Reference: pinggateway, configure, reference | reference | https://docs.pingidentity.com/pinggateway/2026/reference/*.md | references/snapshots/reference.md |
| Gateway Guide: pingam, pinggateway, configure | gateway-guide | https://docs.pingidentity.com/pinggateway/2026/gateway-guide/*.md | references/snapshots/gateway-guide.md |
| Aic: identity, advanced, cloud | aic | https://docs.pingidentity.com/pinggateway/2026/aic/*.md | references/snapshots/aic.md |
| Studio Guide: studio, routes, pinggateway | studio-guide | https://docs.pingidentity.com/pinggateway/2026/studio-guide/*.md | references/snapshots/studio-guide.md |
| Installation Guide: pinggateway, configure, jwt | installation-guide | https://docs.pingidentity.com/pinggateway/2026/installation-guide/*.md | references/snapshots/installation-guide.md |
| Maintenance Guide: pinggateway, configure, deployment | maintenance-guide | https://docs.pingidentity.com/pinggateway/2026/maintenance-guide/*.md | references/snapshots/maintenance-guide.md |
| Fapi: fapi, pinggateway, identity | fapi | https://docs.pingidentity.com/pinggateway/2026/fapi/*.md | references/snapshots/fapi.md |
| About: pinggateway, proxy, descriptors | about | https://docs.pingidentity.com/pinggateway/2026/about/*.md | references/snapshots/about.md |
| Configure: pinggateway, routes, configure | configure | https://docs.pingidentity.com/pinggateway/2026/configure/*.md | references/snapshots/configure.md |
| Getting Started: pinggateway, configure, application | getting-started | https://docs.pingidentity.com/pinggateway/2026/getting-started/*.md | references/snapshots/getting-started.md |
| Security Guide: pinggateway, access, security | security-guide | https://docs.pingidentity.com/pinggateway/2026/security-guide/*.md | references/snapshots/security-guide.md |
| Pingone: pinggateway, pingone, configure | pingone | https://docs.pingidentity.com/pinggateway/2026/pingone/*.md | references/snapshots/pingone.md |
| Upgrade: pinggateway, upgrade, mode | upgrade | https://docs.pingidentity.com/pinggateway/2026/upgrade/*.md | references/snapshots/upgrade.md |
| Devops Guide: docker, pinggateway, configuration | devops-guide | https://docs.pingidentity.com/pinggateway/2026/devops-guide/*.md | references/snapshots/devops-guide.md |
| Mcp: mcp, gateway, security | mcp | https://docs.pingidentity.com/pinggateway/2026/mcp/*.md | references/snapshots/mcp.md |
| Release Notes: notes, pinggateway, release | release-notes | https://docs.pingidentity.com/pinggateway/2026/release-notes/*.md | references/snapshots/release-notes.md |
| Root: pinggateway, community, documentation | root | https://docs.pingidentity.com/pinggateway/2026/*.md | references/snapshots/root.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

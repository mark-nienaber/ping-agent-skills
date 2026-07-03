---
name: web-agents
description: "Use when installing, configuring, upgrading, securing, or troubleshooting PingAM Web Agents, including properties, policies, identity cloud integration, and maintenance. Routes to live docs; snapshots fallback."
license: MIT
---

# Web Agents

Overview of PingAM Web Agent: components, configuration locations, request processing flow, realms, and session management.

## Live source of truth

- Product docs: https://docs.pingidentity.com/web-agents/
- llms.txt index: https://docs.pingidentity.com/web-agents/llms.txt
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
| Properties Reference: agent, url, profile | properties-reference | https://docs.pingidentity.com/web-agents/2026/properties-reference/*.md | references/snapshots/properties-reference.md |
| Release Notes: agent, web, changes | release-notes | https://docs.pingidentity.com/web-agents/release-notes/*.md | references/snapshots/release-notes.md |
| User Guide: pingam, agent, web | user-guide | https://docs.pingidentity.com/web-agents/2026/user-guide/*.md | references/snapshots/user-guide.md |
| Installation Guide: agent, web, pingam | installation-guide | https://docs.pingidentity.com/web-agents/2026/installation-guide/*.md | references/snapshots/installation-guide.md |
| Maintenance Guide: pingam, agent, web | maintenance-guide | https://docs.pingidentity.com/web-agents/2026/maintenance-guide/*.md | references/snapshots/maintenance-guide.md |
| Security Guide: agent, pingam, web | security-guide | https://docs.pingidentity.com/web-agents/2026/security-guide/*.md | references/snapshots/security-guide.md |
| Identity Cloud Guide: advanced, cloud, identity | identity-cloud-guide | https://docs.pingidentity.com/web-agents/2026/identity-cloud-guide/*.md | references/snapshots/identity-cloud-guide.md |
| Upgrade: upgrade, agent, pingam | upgrade | https://docs.pingidentity.com/web-agents/2026/upgrade/*.md | references/snapshots/upgrade.md |
| Root: agent, web | root | https://docs.pingidentity.com/web-agents/2026/*.md | references/snapshots/root.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

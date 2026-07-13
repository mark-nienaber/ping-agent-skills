---
name: web-agents
description: "Use when the user explicitly names Web Agents or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Web Agents

Overview of PingAM Web Agent: components, configuration locations, request processing flow, realms, and session management.

## Live source of truth

- Product docs: https://docs.pingidentity.com/web-agents/
- llms.txt index: https://docs.pingidentity.com/web-agents/llms.txt
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
| Properties Reference: agent, url, profile | properties-reference | https://docs.pingidentity.com/web-agents/2026/properties-reference/*.md | references/snapshots/properties-reference.md |
| Release Notes: agent, web, changes | release-notes | https://docs.pingidentity.com/web-agents/release-notes/*.md | references/snapshots/release-notes.md |
| User Guide: pingam, agent, web | user-guide | https://docs.pingidentity.com/web-agents/2026/user-guide/*.md | references/snapshots/user-guide.md |
| Installation Guide: agent, web, pingam | installation-guide | https://docs.pingidentity.com/web-agents/2026/installation-guide/*.md | live-only |
| Maintenance Guide: pingam, agent, web | maintenance-guide | https://docs.pingidentity.com/web-agents/2026/maintenance-guide/*.md | references/snapshots/maintenance-guide.md |
| Security Guide: agent, pingam, web | security-guide | https://docs.pingidentity.com/web-agents/2026/security-guide/*.md | references/snapshots/security-guide.md |
| Identity Cloud Guide: advanced, cloud, identity | identity-cloud-guide | https://docs.pingidentity.com/web-agents/2026/identity-cloud-guide/*.md | references/snapshots/identity-cloud-guide.md |
| Upgrade: upgrade, agent, pingam | upgrade | https://docs.pingidentity.com/web-agents/2026/upgrade/*.md | references/snapshots/upgrade.md |
| Root: agent, web | root | https://docs.pingidentity.com/web-agents/2026/*.md | references/snapshots/root.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

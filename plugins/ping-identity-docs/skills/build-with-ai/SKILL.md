---
name: build-with-ai
description: "Use when the user explicitly names Build with AI or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Build with AI

Agent skills that extend AI coding assistants with Ping Identity domain expertise for building, integrating, and operating identity solutions.

## Live source of truth

- Product docs: https://developer.pingidentity.com/build-with-ai/
- llms.txt index: https://developer.pingidentity.com/build-with-ai/llms.txt
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
| Davinci Mcp Server: davinci, mcp, server | davinci-mcp-server | https://developer.pingidentity.com/build-with-ai/davinci-mcp-server/*.md | references/snapshots/davinci-mcp-server.md |
| Aic Mcp Server: server, aic, mcp | aic-mcp-server | https://developer.pingidentity.com/build-with-ai/aic-mcp-server/*.md | references/snapshots/aic-mcp-server.md |
| Agent Skills: agent, identity, skills | agent-skills | https://developer.pingidentity.com/build-with-ai/agent-skills/*.md | references/snapshots/agent-skills.md |
| Disclaimers.Md: disclaimers, limitations, agent | disclaimers.md | https://developer.pingidentity.com/build-with-ai/disclaimers.md | references/snapshots/disclaimers-md.md |
| Docs For Agents.Md: agents, alternates, can | docs-for-agents.md | https://developer.pingidentity.com/build-with-ai/docs-for-agents.md | references/snapshots/docs-for-agents-md.md |
| Index.Md: here, start | index.md | https://developer.pingidentity.com/build-with-ai/index.md | references/snapshots/index-md.md |
| Release Notes: announcements, build, new | release_notes | https://developer.pingidentity.com/build-with-ai/release_notes/*.md | references/snapshots/release-notes.md |
| Tying It All Together.Md: all, together, tying | tying-it-all-together.md | https://developer.pingidentity.com/build-with-ai/tying-it-all-together.md | references/snapshots/tying-it-all-together-md.md |
| Use Cases: app, build, ios | use-cases | https://developer.pingidentity.com/build-with-ai/use-cases/*.md | references/snapshots/use-cases.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

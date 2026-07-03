---
name: build-with-ai
description: "Use when building with Ping AI resources, including Docs for Agents, Agent Skills, AIC MCP Server, DaVinci MCP Server, AI tooling security, examples, or release notes. Routes to live docs; snapshots fallback."
license: MIT
---

# Build with AI

Agent skills that extend AI coding assistants with Ping Identity domain expertise for building, integrating, and operating identity solutions.

## Live source of truth

- Product docs: https://developer.pingidentity.com/build-with-ai/
- llms.txt index: https://developer.pingidentity.com/build-with-ai/llms.txt
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
| Davinci Mcp Server: davinci, mcp, server | davinci-mcp-server | https://developer.pingidentity.com/build-with-ai/davinci-mcp-server/*.md | references/snapshots/davinci-mcp-server.md |
| Aic Mcp Server: server, aic, mcp | aic-mcp-server | https://developer.pingidentity.com/build-with-ai/aic-mcp-server/*.md | references/snapshots/aic-mcp-server.md |
| Agent Skills: agent, identity, skills | agent-skills | https://developer.pingidentity.com/build-with-ai/agent-skills/*.md | references/snapshots/agent-skills.md |
| Disclaimers.Md: disclaimers, limitations, agent | disclaimers.md | https://developer.pingidentity.com/build-with-ai/disclaimers.md/*.md | references/snapshots/disclaimers-md.md |
| Docs For Agents.Md: agents, alternates, can | docs-for-agents.md | https://developer.pingidentity.com/build-with-ai/docs-for-agents.md/*.md | references/snapshots/docs-for-agents-md.md |
| Index.Md: here, start | index.md | https://developer.pingidentity.com/build-with-ai/index.md/*.md | references/snapshots/index-md.md |
| Release Notes: announcements, build, new | release_notes | https://developer.pingidentity.com/build-with-ai/release_notes/*.md | references/snapshots/release-notes.md |
| Tying It All Together.Md: all, together, tying | tying-it-all-together.md | https://developer.pingidentity.com/build-with-ai/tying-it-all-together.md/*.md | references/snapshots/tying-it-all-together-md.md |
| Use Cases: app, build, ios | use-cases | https://developer.pingidentity.com/build-with-ai/use-cases/*.md | references/snapshots/use-cases.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

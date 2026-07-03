---
name: identity-for-ai
description: "Use when designing identity for AI agents, including agent identity, delegated access, OAuth2 patterns, use cases, getting started guidance, glossary terms, or release notes. Routes to live docs; snapshots fallback."
license: MIT
---

# Identity for AI

Ping Identity's comprehensive Identity for AI solution secures, manages, and governs AI systems and data.

## Live source of truth

- Product docs: https://developer.pingidentity.com/identity-for-ai/
- llms.txt index: https://developer.pingidentity.com/identity-for-ai/llms.txt
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
| Agents: mcp, secure, agents | agents | https://developer.pingidentity.com/identity-for-ai/agents/*.md | references/snapshots/agents.md |
| Use Cases: agents, least, privilege | use-cases | https://developer.pingidentity.com/identity-for-ai/use-cases/*.md | references/snapshots/use-cases.md |
| Identity: agent, exchange, token | identity | https://developer.pingidentity.com/identity-for-ai/identity/*.md | references/snapshots/identity.md |
| Getting Started: identity, about, comprehensive | getting-started | https://developer.pingidentity.com/identity-for-ai/getting-started/*.md | references/snapshots/getting-started.md |
| Glossary: identity, key, about | glossary | https://developer.pingidentity.com/identity-for-ai/glossary/*.md | references/snapshots/glossary.md |
| Index.Md: identity, comprehensive, data | index.md | https://developer.pingidentity.com/identity-for-ai/index.md/*.md | references/snapshots/index-md.md |
| Release Notes: identity, new, about | release-notes | https://developer.pingidentity.com/identity-for-ai/release-notes/*.md | references/snapshots/release-notes.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

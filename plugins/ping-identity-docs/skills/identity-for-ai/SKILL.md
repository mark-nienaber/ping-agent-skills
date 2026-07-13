---
name: identity-for-ai
description: "Use when the user explicitly names Identity for AI or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Identity for AI

Ping Identity's comprehensive Identity for AI solution secures, manages, and governs AI systems and data.

## Live source of truth

- Product docs: https://developer.pingidentity.com/identity-for-ai/
- llms.txt index: https://developer.pingidentity.com/identity-for-ai/llms.txt
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
| Agents: mcp, secure, agents | agents | https://developer.pingidentity.com/identity-for-ai/agents/*.md | references/snapshots/agents.md |
| Use Cases: agents, least, privilege | use-cases | https://developer.pingidentity.com/identity-for-ai/use-cases/*.md | references/snapshots/use-cases.md |
| Identity: agent, exchange, token | identity | https://developer.pingidentity.com/identity-for-ai/identity/*.md | references/snapshots/identity.md |
| Getting Started: identity, about, comprehensive | getting-started | https://developer.pingidentity.com/identity-for-ai/getting-started/*.md | references/snapshots/getting-started.md |
| Glossary: identity, key, about | glossary | https://developer.pingidentity.com/identity-for-ai/glossary/*.md | references/snapshots/glossary.md |
| Index.Md: identity, comprehensive, data | index.md | https://developer.pingidentity.com/identity-for-ai/index.md | references/snapshots/index-md.md |
| Release Notes: identity, new, about | release-notes | https://developer.pingidentity.com/identity-for-ai/release-notes/*.md | references/snapshots/release-notes.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

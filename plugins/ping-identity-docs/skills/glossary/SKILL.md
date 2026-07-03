---
name: glossary
description: "Use when clarifying Ping Identity terminology, acronyms, product names, IAM concepts, standards, or documentation vocabulary. Routes to live docs; snapshots fallback."
license: MIT
---

# Glossary

Glossary for the Ping Identity documentation.

## Live source of truth

- Product docs: https://docs.pingidentity.com/glossary/
- llms.txt index: https://docs.pingidentity.com/glossary/llms.txt
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
| Index.Md: glossary, identity, documentation | index.md | https://docs.pingidentity.com/glossary/index.md/*.md | references/snapshots/index-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

---
name: pingauthorize-dev
description: "Use when working with PingAuthorize (Developer): pingauthorize. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# PingAuthorize (Developer)

PingAuthorize (Developer) documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/pingauthorize/
- llms.txt index: https://developer.pingidentity.com/pingauthorize/llms.txt
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
| Pingauthorize: create, authorize, client | pingauthorize | https://developer.pingidentity.com/pingauthorize/pingauthorize/*.md | references/snapshots/pingauthorize.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

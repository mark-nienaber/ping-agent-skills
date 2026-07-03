---
name: sdks
description: "Use when integrating Ping SDKs, including native SDKs, JavaScript SDKs, mobile flows, authentication, orchestration, sample apps, and release guidance. Routes to live docs; snapshots fallback."
license: MIT
---

# Ping SDKs

Ping SDKs documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/sdks/
- llms.txt index: https://docs.pingidentity.com/sdks/llms.txt
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
| Latest: authentication, journey, tutorial | latest | https://docs.pingidentity.com/sdks/latest/*.md | references/snapshots/latest.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

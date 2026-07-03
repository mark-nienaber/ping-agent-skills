---
name: pingone-api-ea
description: "Use when developing against PingOne Early Access APIs, including EA platform, auth, authorize, preview endpoints, and migration considerations. Routes to live docs; snapshots fallback."
license: MIT
---

# PingOne API (Early Access)

PingOne API (Early Access) documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/pingone-api-ea/
- llms.txt index: https://developer.pingidentity.com/pingone-api-ea/llms.txt
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
| Authorize: authorization, create, delete | authorize | https://developer.pingidentity.com/pingone-api-ea/authorize/*.md | references/snapshots/authorize.md |
| Platform: create, promotion, delete | platform | https://developer.pingidentity.com/pingone-api-ea/platform/*.md | references/snapshots/platform.md |
| Auth: access, early, auth | auth | https://developer.pingidentity.com/pingone-api-ea/auth/*.md | references/snapshots/auth.md |
| Introduction.Md: untitled | introduction.md | https://developer.pingidentity.com/pingone-api-ea/introduction.md/*.md | references/snapshots/introduction-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

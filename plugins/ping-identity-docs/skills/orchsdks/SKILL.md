---
name: orchsdks
description: "Use when working with Orchestration SDKs: journey, davinci, oidc, release notes, security, concepts. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# Orchestration SDKs

Use the FIDO module to register and authenticate FIDO authenticators in JavaScript apps built with the DaVinci client.

## Live source of truth

- Product docs: https://developer.pingidentity.com/orchsdks/
- llms.txt index: https://developer.pingidentity.com/orchsdks/llms.txt
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
| Journey: configure, identity, device | journey | https://developer.pingidentity.com/orchsdks/journey/*.md | references/snapshots/journey.md |
| Davinci: davinci, configure, pingone | davinci | https://developer.pingidentity.com/orchsdks/davinci/*.md | references/snapshots/davinci.md |
| Oidc: oidc, before, sign | oidc | https://developer.pingidentity.com/orchsdks/oidc/*.md | references/snapshots/oidc.md |
| Release Notes: orchestration, sdk, release | release-notes | https://developer.pingidentity.com/orchsdks/release-notes/*.md | references/snapshots/release-notes.md |
| Security: security, orchestration, sdks | security | https://developer.pingidentity.com/orchsdks/security/*.md | references/snapshots/security.md |
| Concepts: concepts, multiple, system | concepts | https://developer.pingidentity.com/orchsdks/concepts/*.md | references/snapshots/concepts.md |
| Index.Md: orchestration, sdks, advanced | index.md | https://developer.pingidentity.com/orchsdks/index.md | references/snapshots/index-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

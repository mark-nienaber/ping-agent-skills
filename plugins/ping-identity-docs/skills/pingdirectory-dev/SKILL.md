---
name: pingdirectory-dev
description: "Use when developing against PingDirectory APIs, including Directory REST, Directory Proxy SCIM, consent APIs, developer examples, and application integration. Routes to live docs; snapshots fallback."
license: MIT
---

# PingDirectory (Developer)

PingDirectory (Developer) documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/pingdirectory/
- llms.txt index: https://developer.pingidentity.com/pingdirectory/llms.txt
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
| Directory: entry, change, control | directory | https://developer.pingidentity.com/pingdirectory/directory/*.md | references/snapshots/directory.md |
| Directory Proxy Scim: read, scim, group | directory-proxy-scim | https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/*.md | references/snapshots/directory-proxy-scim.md |
| Consent: consent, read, activity | consent | https://developer.pingidentity.com/pingdirectory/consent/*.md | references/snapshots/consent.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

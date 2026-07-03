---
name: platform
description: "Use when deploying or operating the Ping Platform, including sample setup, platform guide, Kubernetes deployment, product integration, and release notes. Routes to live docs; snapshots fallback."
license: MIT
---

# Ping Platform

Ping Platform documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/platform/
- llms.txt index: https://docs.pingidentity.com/platform/llms.txt
- Snapshot version: 8
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Sample Setup: set, customization, deployment | sample-setup | https://docs.pingidentity.com/platform/8/sample-setup/*.md | references/snapshots/sample-setup.md |
| Platform Guide: edge, hsm, overview | platform-guide | https://docs.pingidentity.com/platform/8/platform-guide/*.md | references/snapshots/platform-guide.md |
| Release Notes: notes, release | release-notes | https://docs.pingidentity.com/platform/8/release-notes/*.md | references/snapshots/release-notes.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

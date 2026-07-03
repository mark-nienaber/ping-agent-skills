---
name: recognize
description: "Use when integrating PingOne Recognize, including mobile SDK, web SDK, identity verification bridge, on-prem deployment, user guide, troubleshooting, and release notes. Routes to live docs; snapshots fallback."
license: MIT
---

# Recognize

This page explains the options customers have when using PingOne Recognize to support account recovery.

## Live source of truth

- Product docs: https://docs.pingidentity.com/recognize/
- llms.txt index: https://docs.pingidentity.com/recognize/llms.txt
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
| Mobile Sdk: pingone, recognize, sdk | mobile-sdk | https://docs.pingidentity.com/recognize/mobile-sdk/*.md | references/snapshots/mobile-sdk.md |
| Web Sdk: pingone, recognize, web | web-sdk | https://docs.pingidentity.com/recognize/web-sdk/*.md | references/snapshots/web-sdk.md |
| Idv Bridge: bridge, idv, pingone | idv-bridge | https://docs.pingidentity.com/recognize/idv-bridge/*.md | references/snapshots/idv-bridge.md |
| On Premise: premise, pingone, recognize | on-premise | https://docs.pingidentity.com/recognize/on-premise/*.md | references/snapshots/on-premise.md |
| User Guide: account, your, app | user-guide | https://docs.pingidentity.com/recognize/user-guide/*.md | references/snapshots/user-guide.md |
| Introduction: page, pingone, recognize | introduction | https://docs.pingidentity.com/recognize/introduction/*.md | references/snapshots/introduction.md |
| Folder Example: folder, page | folder-example | https://docs.pingidentity.com/recognize/folder-example/*.md | references/snapshots/folder-example.md |
| Pingone Recognize.Md: pingone, recognize | pingone-recognize.md | https://docs.pingidentity.com/recognize/pingone-recognize.md/*.md | references/snapshots/pingone-recognize-md.md |
| Release Notes: previous, releases | release-notes | https://docs.pingidentity.com/recognize/release-notes/*.md | references/snapshots/release-notes.md |
| Troubleshooting: guide, troubleshooting | troubleshooting | https://docs.pingidentity.com/recognize/troubleshooting/*.md | references/snapshots/troubleshooting.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

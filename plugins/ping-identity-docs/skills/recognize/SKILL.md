---
name: recognize
description: "Use when the user explicitly names Recognize or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Recognize

This page explains the options customers have when using PingOne Recognize to support account recovery.

## Live source of truth

- Product docs: https://docs.pingidentity.com/recognize/
- llms.txt index: https://docs.pingidentity.com/recognize/llms.txt
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
| Mobile Sdk: pingone, recognize, sdk | mobile-sdk | https://docs.pingidentity.com/recognize/mobile-sdk/*.md | references/snapshots/mobile-sdk.md |
| Web Sdk: pingone, recognize, web | web-sdk | https://docs.pingidentity.com/recognize/web-sdk/*.md | references/snapshots/web-sdk.md |
| Idv Bridge: bridge, idv, pingone | idv-bridge | https://docs.pingidentity.com/recognize/idv-bridge/*.md | references/snapshots/idv-bridge.md |
| On Premise: premise, pingone, recognize | on-premise | https://docs.pingidentity.com/recognize/on-premise/*.md | references/snapshots/on-premise.md |
| User Guide: account, your, app | user-guide | https://docs.pingidentity.com/recognize/user-guide/*.md | references/snapshots/user-guide.md |
| Introduction: page, pingone, recognize | introduction | https://docs.pingidentity.com/recognize/introduction/*.md | references/snapshots/introduction.md |
| Folder Example: folder, page | folder-example | https://docs.pingidentity.com/recognize/folder-example/*.md | references/snapshots/folder-example.md |
| Pingone Recognize.Md: pingone, recognize | pingone-recognize.md | https://docs.pingidentity.com/recognize/pingone-recognize.md | references/snapshots/pingone-recognize-md.md |
| Release Notes: previous, releases | release-notes | https://docs.pingidentity.com/recognize/release-notes/*.md | references/snapshots/release-notes.md |
| Troubleshooting: guide, troubleshooting | troubleshooting | https://docs.pingidentity.com/recognize/troubleshooting/*.md | references/snapshots/troubleshooting.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

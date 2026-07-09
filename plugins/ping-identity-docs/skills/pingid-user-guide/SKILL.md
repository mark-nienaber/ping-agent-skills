---
name: pingid-user-guide
description: "Use when working with PingID User Guide: index.md, ma lost or stolen mobile.md, ma where find qr code.md. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# PingID User Guide

PingID FAQ for end users. Covers pairing PingID mobile app, finding a QR code, a lost or stolen device, and when to contact their company's help desk.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingid-user-guide/
- llms.txt index: https://docs.pingidentity.com/pingid-user-guide/llms.txt
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
| Index.Md: pingid, help, app | index.md | https://docs.pingidentity.com/pingid-user-guide/index.md | references/snapshots/index-md.md |
| Ma Lost Or Stolen Mobile.Md: help, lost, phone | ma_lost_or_stolen_mobile.md | https://docs.pingidentity.com/pingid-user-guide/ma_lost_or_stolen_mobile.md | references/snapshots/ma-lost-or-stolen-mobile-md.md |
| Ma Where Find Qr Code.Md: your, app, code | ma_where_find_qr_code.md | https://docs.pingidentity.com/pingid-user-guide/ma_where_find_qr_code.md | references/snapshots/ma-where-find-qr-code-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

---
name: pingid-user-guide
description: "Use when the user explicitly names PingID User Guide or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingID User Guide

PingID FAQ for end users. Covers pairing PingID mobile app, finding a QR code, a lost or stolen device, and when to contact their company's help desk.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingid-user-guide/
- llms.txt index: https://docs.pingidentity.com/pingid-user-guide/llms.txt
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
| Index.Md: pingid, help, app | index.md | https://docs.pingidentity.com/pingid-user-guide/index.md | references/snapshots/index-md.md |
| Ma Lost Or Stolen Mobile.Md: help, lost, phone | ma_lost_or_stolen_mobile.md | https://docs.pingidentity.com/pingid-user-guide/ma_lost_or_stolen_mobile.md | references/snapshots/ma-lost-or-stolen-mobile-md.md |
| Ma Where Find Qr Code.Md: your, app, code | ma_where_find_qr_code.md | https://docs.pingidentity.com/pingid-user-guide/ma_where_find_qr_code.md | references/snapshots/ma-where-find-qr-code-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

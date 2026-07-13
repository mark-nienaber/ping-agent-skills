---
name: pingone-api
description: "Use when the user explicitly names PingOne API or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingOne API

PingOne API documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/pingone-api/
- llms.txt index: https://developer.pingidentity.com/pingone-api/llms.txt
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
| Platform: application, resources, agreement | platform | https://developer.pingidentity.com/pingone-api/platform/*.md | references/snapshots/platform.md |
| Workflow Library: client, flow, secret | workflow-library | https://developer.pingidentity.com/pingone-api/workflow-library/*.md | references/snapshots/workflow-library.md |
| Auth: authorize, authorization, accept | auth | https://developer.pingidentity.com/pingone-api/auth/*.md | references/snapshots/auth.md |
| Mfa: device, fido, mfa | mfa | https://developer.pingidentity.com/pingone-api/mfa/*.md | references/snapshots/mfa.md |
| Credentials: credential, create, signing | credentials | https://developer.pingidentity.com/pingone-api/credentials/*.md | references/snapshots/credentials.md |
| Authorize: application, create, permissions | authorize | https://developer.pingidentity.com/pingone-api/authorize/*.md | references/snapshots/authorize.md |
| Verify: delete, verify, deprecated | verify | https://developer.pingidentity.com/pingone-api/verify/*.md | references/snapshots/verify.md |
| Foundations: authorization, authentication, type | foundations | https://developer.pingidentity.com/pingone-api/foundations/*.md | references/snapshots/foundations.md |
| Davinci: davinci, admin, flow | davinci | https://developer.pingidentity.com/pingone-api/davinci/*.md | references/snapshots/davinci.md |
| Protect: risk, create, predictor | protect | https://developer.pingidentity.com/pingone-api/protect/*.md | references/snapshots/protect.md |
| Getting Started: step, create, get | getting-started | https://developer.pingidentity.com/pingone-api/getting-started/*.md | references/snapshots/getting-started.md |
| Native Sdks: pingone, sdk, native | native-sdks | https://developer.pingidentity.com/pingone-api/native-sdks/*.md | references/snapshots/native-sdks.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

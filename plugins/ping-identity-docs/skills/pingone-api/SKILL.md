---
name: pingone-api
description: "Use when developing with PingOne Platform APIs, including auth flows, users, groups, applications, MFA, credentials, authorize, verify, protect, DaVinci, and SDKs. Routes to live docs; snapshots fallback."
license: MIT
---

# PingOne API

PingOne API documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/pingone-api/
- llms.txt index: https://developer.pingidentity.com/pingone-api/llms.txt
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
| Before You Begin: pingone, postman, before | before-you-begin | https://developer.pingidentity.com/pingone-api/before-you-begin/*.md | references/snapshots/before-you-begin.md |
| Changelog.Md: changelog | changelog.md | https://developer.pingidentity.com/pingone-api/changelog.md/*.md | references/snapshots/changelog-md.md |
| Introduction.Md: pingone, platform | introduction.md | https://developer.pingidentity.com/pingone-api/introduction.md/*.md | references/snapshots/introduction-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

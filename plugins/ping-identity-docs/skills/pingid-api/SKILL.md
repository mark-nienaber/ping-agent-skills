---
name: pingid-api
description: "Use when integrating with PingID APIs, including authentication, user management, policy API, error codes, FIDO examples, passwordless, and registration flows. Routes to live docs; snapshots fallback."
license: MIT
---

# PingID API

PingID API documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/pingid-api/
- llms.txt index: https://developer.pingidentity.com/pingid-api/llms.txt
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
| Pid C Pingidapiauthentication.Md: authentication, pingid | pid_c_PingIDapiAuthentication.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiAuthentication.md/*.md | references/snapshots/pid-c-pingidapiauthentication-md.md |
| Pid C Pingidapierrorcodes.Md: codes, error, pingid | pid_c_PingIDapiErrorCodes.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiErrorCodes.md/*.md | references/snapshots/pid-c-pingidapierrorcodes-md.md |
| Pid C Pingidapiexamplefidobiometrics.Md: biometrics, example, fido | pid_c_PingIDapiExampleFIDObiometrics.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiExampleFIDObiometrics.md/*.md | references/snapshots/pid-c-pingidapiexamplefidobiometrics-md.md |
| Pid C Pingidapiexamplefidosecuritykey.Md: example, fido, key | pid_c_PingIDapiExampleFIDOsecurityKey.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiExampleFIDOsecurityKey.md/*.md | references/snapshots/pid-c-pingidapiexamplefidosecuritykey-md.md |
| Pid C Pingidapiexamplepasswordless.Md: authentication, example, fido | pid_c_PingIDapiExamplePasswordless.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiExamplePasswordless.md/*.md | references/snapshots/pid-c-pingidapiexamplepasswordless-md.md |
| Pid C Pingidapiexampleuserregistration.Md: example, pingid, registration | pid_c_PingIDapiExampleUserRegistration.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiExampleUserRegistration.md/*.md | references/snapshots/pid-c-pingidapiexampleuserregistration-md.md |
| Pid C Pingidapioverview.Md: overview, pingid | pid_c_PingIDapiOverview.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiOverview.md/*.md | references/snapshots/pid-c-pingidapioverview-md.md |
| Pid C Pingidapipfapplicationpolicy.Md: application, management, pingfederate | pid_c_PingIDapiPFapplicationPolicy.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiPFapplicationPolicy.md/*.md | references/snapshots/pid-c-pingidapipfapplicationpolicy-md.md |
| Pid C Pingidapippmrequest.Md: authentication, browser, ppm | pid_c_PingIDapiPpmrequest.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiPpmrequest.md/*.md | references/snapshots/pid-c-pingidapippmrequest-md.md |
| Pid C Pingidapirelatedresources.Md: related, resources | pid_c_PingIDapiRelatedResources.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiRelatedResources.md/*.md | references/snapshots/pid-c-pingidapirelatedresources-md.md |
| Pid C Pingidapiusermanagement.Md: management, pingid, user | pid_c_PingIDapiUserManagement.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiUserManagement.md/*.md | references/snapshots/pid-c-pingidapiusermanagement-md.md |
| Pingid Policy Api.Md: authentication, policy, web | pingid_policy_api.md | https://developer.pingidentity.com/pingid-api/pingid_policy_api.md/*.md | references/snapshots/pingid-policy-api-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

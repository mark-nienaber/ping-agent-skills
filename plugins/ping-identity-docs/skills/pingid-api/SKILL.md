---
name: pingid-api
description: "Use when the user explicitly names PingID API or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingID API

PingID API documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/pingid-api/
- llms.txt index: https://developer.pingidentity.com/pingid-api/llms.txt
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
| Pid C Pingidapiauthentication.Md: authentication, pingid | pid_c_PingIDapiAuthentication.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiAuthentication.md | references/snapshots/pid-c-pingidapiauthentication-md.md |
| Pid C Pingidapierrorcodes.Md: codes, error, pingid | pid_c_PingIDapiErrorCodes.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiErrorCodes.md | references/snapshots/pid-c-pingidapierrorcodes-md.md |
| Pid C Pingidapiexamplefidobiometrics.Md: biometrics, example, fido | pid_c_PingIDapiExampleFIDObiometrics.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiExampleFIDObiometrics.md | references/snapshots/pid-c-pingidapiexamplefidobiometrics-md.md |
| Pid C Pingidapiexamplefidosecuritykey.Md: example, fido, key | pid_c_PingIDapiExampleFIDOsecurityKey.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiExampleFIDOsecurityKey.md | references/snapshots/pid-c-pingidapiexamplefidosecuritykey-md.md |
| Pid C Pingidapiexamplepasswordless.Md: authentication, example, fido | pid_c_PingIDapiExamplePasswordless.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiExamplePasswordless.md | references/snapshots/pid-c-pingidapiexamplepasswordless-md.md |
| Pid C Pingidapiexampleuserregistration.Md: example, pingid, registration | pid_c_PingIDapiExampleUserRegistration.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiExampleUserRegistration.md | references/snapshots/pid-c-pingidapiexampleuserregistration-md.md |
| Pid C Pingidapioverview.Md: overview, pingid | pid_c_PingIDapiOverview.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiOverview.md | references/snapshots/pid-c-pingidapioverview-md.md |
| Pid C Pingidapipfapplicationpolicy.Md: application, management, pingfederate | pid_c_PingIDapiPFapplicationPolicy.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiPFapplicationPolicy.md | references/snapshots/pid-c-pingidapipfapplicationpolicy-md.md |
| Pid C Pingidapippmrequest.Md: authentication, browser, ppm | pid_c_PingIDapiPpmrequest.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiPpmrequest.md | references/snapshots/pid-c-pingidapippmrequest-md.md |
| Pid C Pingidapirelatedresources.Md: related, resources | pid_c_PingIDapiRelatedResources.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiRelatedResources.md | references/snapshots/pid-c-pingidapirelatedresources-md.md |
| Pid C Pingidapiusermanagement.Md: management, pingid, user | pid_c_PingIDapiUserManagement.md | https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiUserManagement.md | references/snapshots/pid-c-pingidapiusermanagement-md.md |
| Pingid Policy Api.Md: authentication, policy, web | pingid_policy_api.md | https://developer.pingidentity.com/pingid-api/pingid_policy_api.md | references/snapshots/pingid-policy-api-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

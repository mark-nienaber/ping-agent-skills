---
name: p14e-directory-api
description: "Use when the user explicitly names P14e Directory API or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# P14e Directory API

P14e Directory API documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/p14e-directory-api/
- llms.txt index: https://developer.pingidentity.com/p14e-directory-api/llms.txt
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
| Create Requests.Md: creating, requests | create-requests.md | https://developer.pingidentity.com/p14e-directory-api/create-requests.md | references/snapshots/create-requests-md.md |
| Create Resource.Md: creating, resource | create-resource.md | https://developer.pingidentity.com/p14e-directory-api/create-resource.md | references/snapshots/create-resource-md.md |
| Delete Resource.Md: deleting, resource | delete-resource.md | https://developer.pingidentity.com/p14e-directory-api/delete-resource.md | references/snapshots/delete-resource-md.md |
| Directory Actions.Md: actions, directory | directory-actions.md | https://developer.pingidentity.com/p14e-directory-api/directory-actions.md | references/snapshots/directory-actions-md.md |
| Functional Overview.Md: functional, overview | functional-overview.md | https://developer.pingidentity.com/p14e-directory-api/functional-overview.md | references/snapshots/functional-overview-md.md |
| Group Actions.Md: actions, group | group-actions.md | https://developer.pingidentity.com/p14e-directory-api/group-actions.md | references/snapshots/group-actions-md.md |
| Group Membership Count.Md: count, group, membership | group-membership-count.md | https://developer.pingidentity.com/p14e-directory-api/group-membership-count.md | references/snapshots/group-membership-count-md.md |
| Group Resources.Md: group, resources | group-resources.md | https://developer.pingidentity.com/p14e-directory-api/group-resources.md | references/snapshots/group-resources-md.md |
| Handle Errors.Md: errors, handling | handle-errors.md | https://developer.pingidentity.com/p14e-directory-api/handle-errors.md | references/snapshots/handle-errors-md.md |
| Handle Responses.Md: handling, responses | handle-responses.md | https://developer.pingidentity.com/p14e-directory-api/handle-responses.md | references/snapshots/handle-responses-md.md |
| Index.Md: directory, enterprise, pingone | index.md | https://developer.pingidentity.com/p14e-directory-api/index.md | references/snapshots/index-md.md |
| Read Resource.Md: reading, resource | read-resource.md | https://developer.pingidentity.com/p14e-directory-api/read-resource.md | references/snapshots/read-resource-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

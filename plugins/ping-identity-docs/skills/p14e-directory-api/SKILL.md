---
name: p14e-directory-api
description: "Use when working with P14e Directory API: create requests.md, create resource.md, delete resource.md, directory actions.md, functional overview.md, group actions.md. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# P14e Directory API

P14e Directory API documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://developer.pingidentity.com/p14e-directory-api/
- llms.txt index: https://developer.pingidentity.com/p14e-directory-api/llms.txt
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
| Release Notes: previous, releases | release_notes | https://developer.pingidentity.com/p14e-directory-api/release_notes/*.md | references/snapshots/release-notes.md |
| Reset Password By Email.Md: email, password, resetting | reset-password-by-email.md | https://developer.pingidentity.com/p14e-directory-api/reset-password-by-email.md | references/snapshots/reset-password-by-email-md.md |
| Reset Password.Md: password, resetting | reset-password.md | https://developer.pingidentity.com/p14e-directory-api/reset-password.md | references/snapshots/reset-password-md.md |
| Update Resource.Md: resource, updating | update-resource.md | https://developer.pingidentity.com/p14e-directory-api/update-resource.md | references/snapshots/update-resource-md.md |
| User Actions.Md: actions, user | user-actions.md | https://developer.pingidentity.com/p14e-directory-api/user-actions.md | references/snapshots/user-actions-md.md |
| User Authentication.Md: authentication, user | user-authentication.md | https://developer.pingidentity.com/p14e-directory-api/user-authentication.md | references/snapshots/user-authentication-md.md |
| User Invitation.Md: invitation, user | user-invitation.md | https://developer.pingidentity.com/p14e-directory-api/user-invitation.md | references/snapshots/user-invitation-md.md |
| User Registration Notifications.Md: notifications, registration, user | user-registration-notifications.md | https://developer.pingidentity.com/p14e-directory-api/user-registration-notifications.md | references/snapshots/user-registration-notifications-md.md |
| User Resources.Md: resources, user | user-resources.md | https://developer.pingidentity.com/p14e-directory-api/user-resources.md | references/snapshots/user-resources-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

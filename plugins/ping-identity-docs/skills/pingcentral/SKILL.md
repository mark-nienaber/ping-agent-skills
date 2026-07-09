---
name: pingcentral
description: "Use when working with PingCentral: release notes, pingcentral for iam administrators, pingcentral for application owners, root. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# PingCentral

Instructions for accessing PingCentral.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingcentral/
- llms.txt index: https://docs.pingidentity.com/pingcentral/llms.txt
- Snapshot version: 3.1.1
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Release Notes: pingcentral, notes, release | release_notes | https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/*.md | references/snapshots/release-notes.md |
| Pingcentral For Iam Administrators: pingcentral, configuring, instructions | pingcentral_for_iam_administrators | https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/*.md | references/snapshots/pingcentral-for-iam-administrators.md |
| Pingcentral For Application Owners: applications, instructions, pingcentral | pingcentral_for_application_owners | https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/*.md | references/snapshots/pingcentral-for-application-owners.md |
| Root: pingcentral | root | https://docs.pingidentity.com/pingcentral/3.1.1/*.md | references/snapshots/root.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

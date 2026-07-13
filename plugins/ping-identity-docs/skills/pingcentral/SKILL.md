---
name: pingcentral
description: "Use when the user explicitly names PingCentral or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingCentral

Instructions for accessing PingCentral.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingcentral/
- llms.txt index: https://docs.pingidentity.com/pingcentral/llms.txt
- Snapshot version: 3.1.1
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
| Release Notes: pingcentral, notes, release | release_notes | https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/*.md | references/snapshots/release-notes.md |
| Pingcentral For Iam Administrators: pingcentral, configuring, instructions | pingcentral_for_iam_administrators | https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/*.md | references/snapshots/pingcentral-for-iam-administrators.md |
| Pingcentral For Application Owners: applications, instructions, pingcentral | pingcentral_for_application_owners | https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/*.md | references/snapshots/pingcentral-for-application-owners.md |
| Root: pingcentral | root | https://docs.pingidentity.com/pingcentral/3.1.1/*.md | references/snapshots/root.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

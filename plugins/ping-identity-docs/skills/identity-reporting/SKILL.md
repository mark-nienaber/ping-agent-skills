---
name: identity-reporting
description: "Use when working with Identity Reporting: identity reporting, release notes. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# Identity Reporting

Identity Reporting documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/identity-reporting/
- llms.txt index: https://docs.pingidentity.com/identity-reporting/llms.txt
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
| Identity Reporting: report, reporting, compliance | identity-reporting | https://docs.pingidentity.com/identity-reporting/identity-reporting/*.md | references/snapshots/identity-reporting.md |
| Release Notes: advisories, before, changelog | release-notes | https://docs.pingidentity.com/identity-reporting/release-notes/*.md | references/snapshots/release-notes.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

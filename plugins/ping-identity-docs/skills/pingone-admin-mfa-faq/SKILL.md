---
name: pingone-admin-mfa-faq
description: "Use when working with PingOne Admin MFA FAQ: p1 mfa required for admins faq.md. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# PingOne Admin MFA FAQ

PingOne Admin MFA FAQ documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingone-admin-mfa-faq/
- llms.txt index: https://docs.pingidentity.com/pingone-admin-mfa-faq/llms.txt
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
| P1 Mfa Required For Admins Faq.Md: administrators, faq, mfa | p1_mfa_required_for_admins_faq.md | https://docs.pingidentity.com/pingone-admin-mfa-faq/p1_mfa_required_for_admins_faq.md | references/snapshots/p1-mfa-required-for-admins-faq-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

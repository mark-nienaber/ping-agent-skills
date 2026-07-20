---
name: pingone
description: "Use when the user explicitly names PingOne or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingOne

How to enable and configure WhatsApp authentication in PingOne to let users receive a one-time passcode via WhatsApp.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingone/
- llms.txt index: https://docs.pingidentity.com/pingone/llms.txt
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
| Integrations: identity, provider, pingone | integrations | https://docs.pingidentity.com/pingone/integrations/*.md | references/snapshots/integrations.md |
| Authorization Using Pingone Authorize: pingone, authorize, adding | authorization_using_pingone_authorize | https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/*.md | references/snapshots/authorization-using-pingone-authorize.md |
| Applications: application, pingone, applications | applications | https://docs.pingidentity.com/pingone/applications/*.md | references/snapshots/applications.md |
| Strong Authentication Mfa: pingid, app, authentication | strong_authentication_mfa | https://docs.pingidentity.com/pingone/strong_authentication_mfa/*.md | references/snapshots/strong-authentication-mfa.md |
| Settings: pingone, configuring, adding | settings | https://docs.pingidentity.com/pingone/settings/*.md | references/snapshots/settings.md |
| User Experience: pingone, adding, configuring | user_experience | https://docs.pingidentity.com/pingone/user_experience/*.md | references/snapshots/user-experience.md |
| Directory: pingone, user, users | directory | https://docs.pingidentity.com/pingone/directory/*.md | references/snapshots/directory.md |
| Threat Protection Using Pingone Protect: protect, pingone, risk | threat_protection_using_pingone_protect | https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/*.md | references/snapshots/threat-protection-using-pingone-protect.md |
| Getting Started With Pingone: pingone, your, administrator | getting_started_with_pingone | https://docs.pingidentity.com/pingone/getting_started_with_pingone/*.md | references/snapshots/getting-started-with-pingone.md |
| Pingone Tutorials: creating, pingone, application | pingone_tutorials | https://docs.pingidentity.com/pingone/pingone_tutorials/*.md | references/snapshots/pingone-tutorials.md |
| Authentication: authentication, pingone, adding | authentication | https://docs.pingidentity.com/pingone/authentication/*.md | references/snapshots/authentication.md |
| Identity Verification Using Pingone Verify: verify, pingone, identity | identity_verification_using_pingone_verify | https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/*.md | references/snapshots/identity-verification-using-pingone-verify.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

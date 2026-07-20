---
name: pingoneaic
description: "Use when the user explicitly names PingOne Advanced Identity Cloud or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingOne Advanced Identity Cloud

Home page for PingOne Advanced Identity Cloud documentation, linking to release notes, getting started guides, tenant management, and troubleshooting resources.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingoneaic/
- llms.txt index: https://docs.pingidentity.com/pingoneaic/llms.txt
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
| Identity Governance: access, create, certification | identity-governance | https://docs.pingidentity.com/pingoneaic/identity-governance/*.md | references/snapshots/identity-governance.md |
| Release Notes: channel, changelog, identity | release-notes | https://docs.pingidentity.com/pingoneaic/release-notes/*.md | references/snapshots/release-notes.md |
| Am Oauth2: authorization, oauth, oauth2 | am-oauth2 | https://docs.pingidentity.com/pingoneaic/am-oauth2/*.md | references/snapshots/am-oauth2.md |
| Tenants: email, configure, configuration | tenants | https://docs.pingidentity.com/pingoneaic/tenants/*.md | references/snapshots/tenants.md |
| App Management: identity, advanced, cloud | app-management | https://docs.pingidentity.com/pingoneaic/app-management/*.md | references/snapshots/app-management.md |
| Idm Objects: objects, managed, rest | idm-objects | https://docs.pingidentity.com/pingoneaic/idm-objects/*.md | references/snapshots/idm-objects.md |
| Am Authentication: authentication, configure, rest | am-authentication | https://docs.pingidentity.com/pingoneaic/am-authentication/*.md | references/snapshots/am-authentication.md |
| Am Scripting: scripts, scripting, bindings | am-scripting | https://docs.pingidentity.com/pingoneaic/am-scripting/*.md | references/snapshots/am-scripting.md |
| Use Cases: identity, advanced, cloud | use-cases | https://docs.pingidentity.com/pingoneaic/use-cases/*.md | references/snapshots/use-cases.md |
| Idm Synchronization: synchronization, data, objects | idm-synchronization | https://docs.pingidentity.com/pingoneaic/idm-synchronization/*.md | references/snapshots/idm-synchronization.md |
| Am Oidc1: connect, openid, oauth2 | am-oidc1 | https://docs.pingidentity.com/pingoneaic/am-oidc1/*.md | references/snapshots/am-oidc1.md |
| Identities: identity, advanced, configure | identities | https://docs.pingidentity.com/pingoneaic/identities/*.md | references/snapshots/identities.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

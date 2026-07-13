---
name: pingoneforenterprise
description: "Use when the user explicitly names PingOne for Enterprise or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# PingOne for Enterprise

PingOne for Enterprise documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingoneforenterprise/
- llms.txt index: https://docs.pingidentity.com/pingoneforenterprise/llms.txt
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
| Pingone For Enterprise App Catalog: adding, dock, enterprise | pingone_for_enterprise_app_catalog | https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/*.md | references/snapshots/pingone-for-enterprise-app-catalog.md |
| Pingone For Enterprise: add, application, adding | pingone_for_enterprise | https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/*.md | references/snapshots/pingone-for-enterprise.md |
| Pingone Sso For Saas Apps: application, connection, account | pingone_sso_for_saas_apps | https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/*.md | references/snapshots/pingone-sso-for-saas-apps.md |
| Pingone For Enterprise Release Notes: pingone, previous, releases | pingone_for_enterprise_release_notes | https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_release_notes/*.md | references/snapshots/pingone-for-enterprise-release-notes.md |
| Invited Pingone For Enterprise Sso: enterprise, invited, pingone | invited_pingone_for_enterprise_sso | https://docs.pingidentity.com/pingoneforenterprise/invited_pingone_for_enterprise_sso/*.md | references/snapshots/invited-pingone-for-enterprise-sso.md |
| Migrating From P14E: pingone, enterprise, migrating | migrating_from_p14e | https://docs.pingidentity.com/pingoneforenterprise/migrating_from_p14e/*.md | references/snapshots/migrating-from-p14e.md |
| P14E Landing.Md: enterprise, pingone | p14e_landing.md | https://docs.pingidentity.com/pingoneforenterprise/p14e_landing.md | references/snapshots/p14e-landing-md.md |
| P14E Monitoring Usage.Md: enterprise, monitoring, pingone | p14e_monitoring_usage.md | https://docs.pingidentity.com/pingoneforenterprise/p14e_monitoring_usage.md | references/snapshots/p14e-monitoring-usage-md.md |
| P14E Requirements Browsers.Md: browser, enterprise, pingone | p14e_requirements_browsers.md | https://docs.pingidentity.com/pingoneforenterprise/p14e_requirements_browsers.md | references/snapshots/p14e-requirements-browsers-md.md |
| P14E Which P14E Am I Using.Md: pingone, which | p14e_which_p14e_am_i_using.md | https://docs.pingidentity.com/pingoneforenterprise/p14e_which_p14e_am_i_using.md | references/snapshots/p14e-which-p14e-am-i-using-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

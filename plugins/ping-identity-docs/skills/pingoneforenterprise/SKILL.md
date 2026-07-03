---
name: pingoneforenterprise
description: "Use when administering PingOne for Enterprise, including SSO app catalog, SaaS apps, invited SSO, migration from P14E, monitoring, and release notes. Routes to live docs; snapshots fallback."
license: MIT
---

# PingOne for Enterprise

PingOne for Enterprise documentation is indexed in the bundled llms.txt and live Ping Markdown pages.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingoneforenterprise/
- llms.txt index: https://docs.pingidentity.com/pingoneforenterprise/llms.txt
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
| Pingone For Enterprise App Catalog: adding, dock, enterprise | pingone_for_enterprise_app_catalog | https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_app_catalog/*.md | references/snapshots/pingone-for-enterprise-app-catalog.md |
| Pingone For Enterprise: add, application, adding | pingone_for_enterprise | https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/*.md | references/snapshots/pingone-for-enterprise.md |
| Pingone Sso For Saas Apps: application, connection, account | pingone_sso_for_saas_apps | https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/*.md | references/snapshots/pingone-sso-for-saas-apps.md |
| Pingone For Enterprise Release Notes: pingone, previous, releases | pingone_for_enterprise_release_notes | https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_release_notes/*.md | references/snapshots/pingone-for-enterprise-release-notes.md |
| Invited Pingone For Enterprise Sso: enterprise, invited, pingone | invited_pingone_for_enterprise_sso | https://docs.pingidentity.com/pingoneforenterprise/invited_pingone_for_enterprise_sso/*.md | references/snapshots/invited-pingone-for-enterprise-sso.md |
| Migrating From P14E: pingone, enterprise, migrating | migrating_from_p14e | https://docs.pingidentity.com/pingoneforenterprise/migrating_from_p14e/*.md | references/snapshots/migrating-from-p14e.md |
| P14E Landing.Md: enterprise, pingone | p14e_landing.md | https://docs.pingidentity.com/pingoneforenterprise/p14e_landing.md/*.md | references/snapshots/p14e-landing-md.md |
| P14E Monitoring Usage.Md: enterprise, monitoring, pingone | p14e_monitoring_usage.md | https://docs.pingidentity.com/pingoneforenterprise/p14e_monitoring_usage.md/*.md | references/snapshots/p14e-monitoring-usage-md.md |
| P14E Requirements Browsers.Md: browser, enterprise, pingone | p14e_requirements_browsers.md | https://docs.pingidentity.com/pingoneforenterprise/p14e_requirements_browsers.md/*.md | references/snapshots/p14e-requirements-browsers-md.md |
| P14E Which P14E Am I Using.Md: pingone, which | p14e_which_p14e_am_i_using.md | https://docs.pingidentity.com/pingoneforenterprise/p14e_which_p14e_am_i_using.md/*.md | references/snapshots/p14e-which-p14e-am-i-using-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

---
name: davinci
description: "Use when working with DaVinci: flows, davinci best practices, connectors, applications, integrating flows into applications, variables. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# DaVinci

Use the flow search option to find specific nodes.

## Live source of truth

- Product docs: https://docs.pingidentity.com/davinci/
- llms.txt index: https://docs.pingidentity.com/davinci/llms.txt
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
| Flows: flow, editing, adding | flows | https://docs.pingidentity.com/davinci/flows/*.md | references/snapshots/flows.md |
| Davinci Best Practices: best, practices, subflows | davinci_best_practices | https://docs.pingidentity.com/davinci/davinci_best_practices/*.md | references/snapshots/davinci-best-practices.md |
| Connectors: connector, connectors, adding | connectors | https://docs.pingidentity.com/davinci/connectors/*.md | references/snapshots/connectors.md |
| Applications: flow, configuring, policy | applications | https://docs.pingidentity.com/davinci/applications/*.md | references/snapshots/applications.md |
| Integrating Flows Into Applications: flow, launching, pingone | integrating_flows_into_applications | https://docs.pingidentity.com/davinci/integrating_flows_into_applications/*.md | references/snapshots/integrating-flows-into-applications.md |
| Variables: variable, variables, adding | variables | https://docs.pingidentity.com/davinci/variables/*.md | references/snapshots/variables.md |
| Use Cases: pingone, adding, authentication | use_cases | https://docs.pingidentity.com/davinci/use_cases/*.md | references/snapshots/use-cases.md |
| Users: user, deleting, editing | users | https://docs.pingidentity.com/davinci/users/*.md | references/snapshots/users.md |
| Usage Terms: browser, davinci, support | usage_terms | https://docs.pingidentity.com/davinci/usage_terms/*.md | references/snapshots/usage-terms.md |
| Company Settings: company, settings | company_settings | https://docs.pingidentity.com/davinci/company_settings/*.md | references/snapshots/company-settings.md |
| Configuring Siem Streaming: configuring, siem, streaming | configuring_siem_streaming | https://docs.pingidentity.com/davinci/configuring_siem_streaming/*.md | references/snapshots/configuring-siem-streaming.md |
| Davinci Adding P1 Admin Users.Md: adding, admin, davinci | davinci_adding_p1_admin_users.md | https://docs.pingidentity.com/davinci/davinci_adding_p1_admin_users.md | references/snapshots/davinci-adding-p1-admin-users-md.md |
| Davinci Audit Trail.Md: audit, trail | davinci_audit_trail.md | https://docs.pingidentity.com/davinci/davinci_audit_trail.md | references/snapshots/davinci-audit-trail-md.md |
| Davinci Dashboard.Md: dashboard | davinci_dashboard.md | https://docs.pingidentity.com/davinci/davinci_dashboard.md | references/snapshots/davinci-dashboard-md.md |
| Davinci Early Access.Md: access, davinci, early | davinci_early_access.md | https://docs.pingidentity.com/davinci/davinci_early_access.md | references/snapshots/davinci-early-access-md.md |
| Davinci Forms.Md: forms | davinci_forms.md | https://docs.pingidentity.com/davinci/davinci_forms.md | references/snapshots/davinci-forms-md.md |
| Davinci Introduction.Md: davinci, introduction, pingone | davinci_introduction.md | https://docs.pingidentity.com/davinci/davinci_introduction.md | references/snapshots/davinci-introduction-md.md |
| Davinci Landing Page.Md: davinci, pingone | davinci_landing_page.md | https://docs.pingidentity.com/davinci/davinci_landing_page.md | references/snapshots/davinci-landing-page-md.md |
| Release Notes: notes, release | release_notes | https://docs.pingidentity.com/davinci/release_notes/*.md | references/snapshots/release-notes.md |
| Ui Studio: studio | ui_studio | https://docs.pingidentity.com/davinci/ui_studio/*.md | references/snapshots/ui-studio.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

---
name: davinci
description: "Use when the user explicitly names DaVinci or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# DaVinci

Reference for PingOne DaVinci actions, predefined node sets for registration, authentication, and account recovery available in the PingOne Marketplace.

## Live source of truth

- Product docs: https://docs.pingidentity.com/davinci/
- llms.txt index: https://docs.pingidentity.com/davinci/llms.txt
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
| Flows: flow, pingone, davinci | flows | https://docs.pingidentity.com/davinci/flows/*.md | references/snapshots/flows.md |
| Davinci Best Practices: best, practices, davinci | davinci_best_practices | https://docs.pingidentity.com/davinci/davinci_best_practices/*.md | references/snapshots/davinci-best-practices.md |
| Connectors: connector, pingone, davinci | connectors | https://docs.pingidentity.com/davinci/connectors/*.md | references/snapshots/connectors.md |
| Applications: flow, davinci, pingone | applications | https://docs.pingidentity.com/davinci/applications/*.md | references/snapshots/applications.md |
| Integrating Flows Into Applications: pingone, flow, davinci | integrating_flows_into_applications | https://docs.pingidentity.com/davinci/integrating_flows_into_applications/*.md | references/snapshots/integrating-flows-into-applications.md |
| Variables: variable, davinci, pingone | variables | https://docs.pingidentity.com/davinci/variables/*.md | references/snapshots/variables.md |
| Use Cases: pingone, davinci, flows | use_cases | https://docs.pingidentity.com/davinci/use_cases/*.md | references/snapshots/use-cases.md |
| Users: user, davinci, pingone | users | https://docs.pingidentity.com/davinci/users/*.md | references/snapshots/users.md |
| Usage Terms: davinci, browser, pingone | usage_terms | https://docs.pingidentity.com/davinci/usage_terms/*.md | references/snapshots/usage-terms.md |
| Company Settings: company, settings, behavior | company_settings | https://docs.pingidentity.com/davinci/company_settings/*.md | references/snapshots/company-settings.md |
| Configuring Siem Streaming: davinci, pingone, siem | configuring_siem_streaming | https://docs.pingidentity.com/davinci/configuring_siem_streaming/*.md | references/snapshots/configuring-siem-streaming.md |
| Davinci Adding P1 Admin Users.Md: admin, davinci, pingone | davinci_adding_p1_admin_users.md | https://docs.pingidentity.com/davinci/davinci_adding_p1_admin_users.md | references/snapshots/davinci-adding-p1-admin-users-md.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

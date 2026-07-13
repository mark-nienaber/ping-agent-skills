---
name: davinci
description: "Use when the user explicitly names DaVinci or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# DaVinci

Use the flow search option to find specific nodes.

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

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

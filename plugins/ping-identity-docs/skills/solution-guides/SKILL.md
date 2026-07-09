---
name: solution-guides
description: "Use when working with Solution Guides: single sign on use cases, data and application security use cases, workforce use cases, customer use cases, best practice guides, multi factor authentication use cases. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# Solution Guides

Identity for AI secures AI agents with agent registration, authentication, authorization, risk detection, agent gateway, and integrations.

## Live source of truth

- Product docs: https://docs.pingidentity.com/solution-guides/
- llms.txt index: https://docs.pingidentity.com/solution-guides/llms.txt
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
| Single Sign On Use Cases: configuring, pingfederate, enterprise | single_sign-on_use_cases | https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/*.md | references/snapshots/single-sign-on-use-cases.md |
| Data And Application Security Use Cases: pingaccess, pingfederate, application | data_and_application_security_use_cases | https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/*.md | references/snapshots/data-and-application-security-use-cases.md |
| Workforce Use Cases: pingfederate, setting, authentication | workforce_use_cases | https://docs.pingidentity.com/solution-guides/workforce_use_cases/*.md | references/snapshots/workforce-use-cases.md |
| Customer Use Cases: setting, password, pingone | customer_use_cases | https://docs.pingidentity.com/solution-guides/customer_use_cases/*.md | references/snapshots/customer-use-cases.md |
| Best Practice Guides: best, practices, passwordless | best_practice_guides | https://docs.pingidentity.com/solution-guides/best_practice_guides/*.md | references/snapshots/best-practice-guides.md |
| Multi Factor Authentication Use Cases: mfa, pingid, authentication | multi-factor_authentication_use_cases | https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/*.md | references/snapshots/multi-factor-authentication-use-cases.md |
| Standards And Protocols Use Cases: client, commands, federation | standards_and_protocols_use_cases | https://docs.pingidentity.com/solution-guides/standards_and_protocols_use_cases/*.md | references/snapshots/standards-and-protocols-use-cases.md |
| Developer Api Use Cases: pingid, administrative, cases | developer_api_use_cases | https://docs.pingidentity.com/solution-guides/developer_api_use_cases/*.md | references/snapshots/developer-api-use-cases.md |
| Verified Trust: trust, desk, help | verified-trust | https://docs.pingidentity.com/solution-guides/verified-trust/*.md | references/snapshots/verified-trust.md |
| Directory Use Cases: attributes, cases, configuring | directory_use_cases | https://docs.pingidentity.com/solution-guides/directory_use_cases/*.md | references/snapshots/directory-use-cases.md |
| Htg Overview.Md: cases, overview, use | htg_overview.md | https://docs.pingidentity.com/solution-guides/htg_overview.md | references/snapshots/htg-overview-md.md |
| Identity For Ai: agent, identity, agents | identity-for-ai | https://docs.pingidentity.com/solution-guides/identity-for-ai/*.md | references/snapshots/identity-for-ai.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

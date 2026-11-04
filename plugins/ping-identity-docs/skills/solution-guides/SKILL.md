---
name: solution-guides
description: "Use when the user explicitly names Solution Guides or its exact docset and needs official, version-specific product documentation. Do not use for generic IAM or product-selection questions. Routes to live Ping docs; dated snapshots are the offline fallback."
license: MIT
---

# Solution Guides

Add MFA to web apps by synchronizing sessions between PingFederate and PingAccess through PingID.

## Live source of truth

- Product docs: https://docs.pingidentity.com/solution-guides/
- llms.txt index: https://docs.pingidentity.com/solution-guides/llms.txt
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
| Single Sign On Use Cases: pingfederate, sso, enterprise | single_sign-on_use_cases | https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/*.md | references/snapshots/single-sign-on-use-cases.md |
| Data And Application Security Use Cases: pingaccess, pingfederate, oidc | data_and_application_security_use_cases | https://docs.pingidentity.com/solution-guides/data_and_application_security_use_cases/*.md | references/snapshots/data-and-application-security-use-cases.md |
| Workforce Use Cases: pingfederate, authentication, pingone | workforce_use_cases | https://docs.pingidentity.com/solution-guides/workforce_use_cases/*.md | references/snapshots/workforce-use-cases.md |
| Customer Use Cases: password, pingfederate, pingone | customer_use_cases | https://docs.pingidentity.com/solution-guides/customer_use_cases/*.md | references/snapshots/customer-use-cases.md |
| Best Practice Guides: passwordless, authentication, best | best_practice_guides | https://docs.pingidentity.com/solution-guides/best_practice_guides/*.md | references/snapshots/best-practice-guides.md |
| Multi Factor Authentication Use Cases: mfa, pingid, pingfederate | multi-factor_authentication_use_cases | https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/*.md | references/snapshots/multi-factor-authentication-use-cases.md |
| Standards And Protocols Use Cases: federation, pingfederate, kerberos | standards_and_protocols_use_cases | https://docs.pingidentity.com/solution-guides/standards_and_protocols_use_cases/*.md | references/snapshots/standards-and-protocols-use-cases.md |
| Developer Api Use Cases: pingid, pingfederate, powershell | developer_api_use_cases | https://docs.pingidentity.com/solution-guides/developer_api_use_cases/*.md | references/snapshots/developer-api-use-cases.md |
| Verified Trust: verified, account, agent | verified-trust | https://docs.pingidentity.com/solution-guides/verified-trust/*.md | references/snapshots/verified-trust.md |
| Htg Overview.Md: cases, identity, overview | htg_overview.md | https://docs.pingidentity.com/solution-guides/htg_overview.md | references/snapshots/htg-overview-md.md |
| Identity For Ai: agent, identity, agents | identity-for-ai | https://docs.pingidentity.com/solution-guides/identity-for-ai/*.md | references/snapshots/identity-for-ai.md |

## Composition

- Use after pingidentity/agent-plugins has established the product when the task needs deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

Treat snapshots as a dated offline fallback, not the source of truth. See references/MANIFEST.md for sync date, source URLs, capture counts, and checksums.

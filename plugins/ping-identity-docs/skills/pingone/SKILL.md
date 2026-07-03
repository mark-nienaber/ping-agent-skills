---
name: pingone
description: "Use when administering PingOne, including applications, MFA, authentication policies, directory, integrations, Protect, Verify, Authorize, Credentials, DaVinci, and settings. Routes to live docs; snapshots fallback."
license: MIT
---

# PingOne

Groups and populations are both used to organize users in PingOne, but they differ in several ways.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingone/
- llms.txt index: https://docs.pingidentity.com/pingone/llms.txt
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
| Integrations: identity, provider, adding | integrations | https://docs.pingidentity.com/pingone/integrations/*.md | references/snapshots/integrations.md |
| Authorization Using Pingone Authorize: pingone, authorize, adding | authorization_using_pingone_authorize | https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/*.md | references/snapshots/authorization-using-pingone-authorize.md |
| Applications: application, pingone, applications | applications | https://docs.pingidentity.com/pingone/applications/*.md | references/snapshots/applications.md |
| Strong Authentication Mfa: configuring, authentication, pingid | strong_authentication_mfa | https://docs.pingidentity.com/pingone/strong_authentication_mfa/*.md | references/snapshots/strong-authentication-mfa.md |
| Settings: pingone, configuring, adding | settings | https://docs.pingidentity.com/pingone/settings/*.md | references/snapshots/settings.md |
| User Experience: pingone, adding, configuring | user_experience | https://docs.pingidentity.com/pingone/user_experience/*.md | references/snapshots/user-experience.md |
| Directory: pingone, user, users | directory | https://docs.pingidentity.com/pingone/directory/*.md | references/snapshots/directory.md |
| Threat Protection Using Pingone Protect: protect, pingone, risk | threat_protection_using_pingone_protect | https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/*.md | references/snapshots/threat-protection-using-pingone-protect.md |
| Getting Started With Pingone: pingone, administrators, your | getting_started_with_pingone | https://docs.pingidentity.com/pingone/getting_started_with_pingone/*.md | references/snapshots/getting-started-with-pingone.md |
| Pingone Tutorials: creating, pingone, application | pingone_tutorials | https://docs.pingidentity.com/pingone/pingone_tutorials/*.md | references/snapshots/pingone-tutorials.md |
| Authentication: authentication, pingone, adding | authentication | https://docs.pingidentity.com/pingone/authentication/*.md | references/snapshots/authentication.md |
| Identity Verification Using Pingone Verify: verify, pingone, verification | identity_verification_using_pingone_verify | https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/*.md | references/snapshots/identity-verification-using-pingone-verify.md |
| Early Access Features: access, early, promotion | early-access-features | https://docs.pingidentity.com/pingone/early-access-features/*.md | references/snapshots/early-access-features.md |
| Use Cases: pingone, entra, microsoft | use_cases | https://docs.pingidentity.com/pingone/use_cases/*.md | references/snapshots/use-cases.md |
| Monitoring: pingone, alerts, audit | monitoring | https://docs.pingidentity.com/pingone/monitoring/*.md | references/snapshots/monitoring.md |
| Digital Credentials Using Pingone Credentials: credential, pingone, credentials | digital_credentials_using_pingone_credentials | https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/*.md | references/snapshots/digital-credentials-using-pingone-credentials.md |
| Pingone Expression Language: expression, pingone, language | pingone_expression_language | https://docs.pingidentity.com/pingone/pingone_expression_language/*.md | references/snapshots/pingone-expression-language.md |
| Managing Your Pingone User Profile: your, managing, pingone | managing_your_pingone_user_profile | https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/*.md | references/snapshots/managing-your-pingone-user-profile.md |
| Orchestration: experience, center, design | orchestration | https://docs.pingidentity.com/pingone/orchestration/*.md | references/snapshots/orchestration.md |
| Developer Tools: pingone, tools, identity | developer_tools | https://docs.pingidentity.com/pingone/developer_tools/*.md | references/snapshots/developer-tools.md |
| Ai Agents: agents, pingone, agent | ai_agents | https://docs.pingidentity.com/pingone/ai_agents/*.md | references/snapshots/ai-agents.md |
| Introduction To Pingone: identity, pingone, access | introduction_to_pingone | https://docs.pingidentity.com/pingone/introduction_to_pingone/*.md | references/snapshots/introduction-to-pingone.md |
| Migration Tools: cloud, acceleration, migration | migration-tools | https://docs.pingidentity.com/pingone/migration-tools/*.md | references/snapshots/migration-tools.md |
| Operational Status: operational, status, alert | operational_status | https://docs.pingidentity.com/pingone/operational_status/*.md | references/snapshots/operational-status.md |
| P1 Cloud Platform Main Landing Page.Md: pingone | p1_cloud__platform_main_landing_page.md | https://docs.pingidentity.com/pingone/p1_cloud__platform_main_landing_page.md/*.md | references/snapshots/p1-cloud-platform-main-landing-page-md.md |
| P1 Open Davinci Console.Md: davinci | p1_open_davinci_console.md | https://docs.pingidentity.com/pingone/p1_open_davinci_console.md/*.md | references/snapshots/p1-open-davinci-console-md.md |
| P1 Overview P1.Md: overview, page | p1_overview_p1.md | https://docs.pingidentity.com/pingone/p1_overview_p1.md/*.md | references/snapshots/p1-overview-p1-md.md |
| Release Notes: notes, pingone, release | release_notes | https://docs.pingidentity.com/pingone/release_notes/*.md | references/snapshots/release-notes.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

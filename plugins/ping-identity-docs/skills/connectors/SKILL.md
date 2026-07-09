---
name: connectors
description: "Use when working with Connectors: relnotes, type, accertify connector.md, adobe experience manager connector.md, apple login connector.md, authentication connector.md. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# Connectors

The Apple Login connector authenticates users with Sign in with Apple and retrieves Apple ID attributes for use in DaVinci flows.

## Live source of truth

- Product docs: https://docs.pingidentity.com/connectors/
- llms.txt index: https://docs.pingidentity.com/connectors/llms.txt
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
| Relnotes: april, february, january | relnotes | https://docs.pingidentity.com/connectors/relnotes/*.md | references/snapshots/relnotes.md |
| Type: connectors, case, core | type | https://docs.pingidentity.com/connectors/type/*.md | references/snapshots/type.md |
| Accertify Connector.Md: accertify, connector | accertify_connector.md | https://docs.pingidentity.com/connectors/accertify_connector.md | references/snapshots/accertify-connector-md.md |
| Adobe Experience Manager Connector.Md: adobe, connector, experience | adobe_experience_manager_connector.md | https://docs.pingidentity.com/connectors/adobe_experience_manager_connector.md | references/snapshots/adobe-experience-manager-connector-md.md |
| Apple Login Connector.Md: apple, connector, login | apple_login_connector.md | https://docs.pingidentity.com/connectors/apple_login_connector.md | references/snapshots/apple-login-connector-md.md |
| Authentication Connector.Md: authentication, connector, cases | authentication_connector.md | https://docs.pingidentity.com/connectors/authentication_connector.md | references/snapshots/authentication-connector-md.md |
| Authenticid Connector.Md: authenticid, connector | authenticid_connector.md | https://docs.pingidentity.com/connectors/authenticid_connector.md | references/snapshots/authenticid-connector-md.md |
| Azure Ad User Management Connector.Md: azure, connector, management | azure_ad_user_management_connector.md | https://docs.pingidentity.com/connectors/azure_ad_user_management_connector.md | references/snapshots/azure-ad-user-management-connector-md.md |
| Babelstreet Connector.Md: babel, connector, street | babelstreet_connector.md | https://docs.pingidentity.com/connectors/babelstreet_connector.md | references/snapshots/babelstreet-connector-md.md |
| Castle Connector.Md: castle, connector | castle_connector.md | https://docs.pingidentity.com/connectors/castle_connector.md | references/snapshots/castle-connector-md.md |
| Challenge Connector.Md: challenge, connector | challenge_connector.md | https://docs.pingidentity.com/connectors/challenge_connector.md | references/snapshots/challenge-connector-md.md |
| Clear Connector.Md: clear, connector | clear_connector.md | https://docs.pingidentity.com/connectors/clear_connector.md | references/snapshots/clear-connector-md.md |
| Cloudflare Connector.Md: cloudflare, connector | cloudflare_connector.md | https://docs.pingidentity.com/connectors/cloudflare_connector.md | references/snapshots/cloudflare-connector-md.md |
| Code Snippet Connector.Md: code, connector, snippet | code_snippet_connector.md | https://docs.pingidentity.com/connectors/code_snippet_connector.md | references/snapshots/code-snippet-connector-md.md |
| Constella Connector.Md: connector, constella | constella_connector.md | https://docs.pingidentity.com/connectors/constella_connector.md | references/snapshots/constella-connector-md.md |
| Cookie Connector.Md: connector, cookie | cookie_connector.md | https://docs.pingidentity.com/connectors/cookie_connector.md | references/snapshots/cookie-connector-md.md |
| Crowdstrike Connector.Md: connector, crowdstrike | crowdstrike_connector.md | https://docs.pingidentity.com/connectors/crowdstrike_connector.md | references/snapshots/crowdstrike-connector-md.md |
| Daon Connector.Md: connector, daon | daon_connector.md | https://docs.pingidentity.com/connectors/daon_connector.md | references/snapshots/daon-connector-md.md |
| Device Policy Connector.Md: connector, device, policy | device_policy_connector.md | https://docs.pingidentity.com/connectors/device_policy_connector.md | references/snapshots/device-policy-connector-md.md |
| Duo Connector.Md: connector, duo | duo_connector.md | https://docs.pingidentity.com/connectors/duo_connector.md | references/snapshots/duo-connector-md.md |
| Entrust Connector.Md: connector, entrust | entrust_connector.md | https://docs.pingidentity.com/connectors/entrust_connector.md | references/snapshots/entrust-connector-md.md |
| Error Message Connector.Md: connector, error, message | error_message_connector.md | https://docs.pingidentity.com/connectors/error_message_connector.md | references/snapshots/error-message-connector-md.md |
| Facebook Login Connector.Md: facebook, connector, login | facebook_login_connector.md | https://docs.pingidentity.com/connectors/facebook_login_connector.md | references/snapshots/facebook-login-connector-md.md |
| Fingerprintjs Connector.Md: connector, fingerprintjs | fingerprintjs_connector.md | https://docs.pingidentity.com/connectors/fingerprintjs_connector.md | references/snapshots/fingerprintjs-connector-md.md |
| Flow Analytics Connector.Md: analytics, connector, flow | flow_analytics_connector.md | https://docs.pingidentity.com/connectors/flow_analytics_connector.md | references/snapshots/flow-analytics-connector-md.md |
| Flow Conductor Connector.Md: conductor, connector, flow | flow_conductor_connector.md | https://docs.pingidentity.com/connectors/flow_conductor_connector.md | references/snapshots/flow-conductor-connector-md.md |
| Form Connector.Md: connector, form | form_connector.md | https://docs.pingidentity.com/connectors/form_connector.md | references/snapshots/form-connector-md.md |
| Functions Connector.Md: connector, functions | functions_connector.md | https://docs.pingidentity.com/connectors/functions_connector.md | references/snapshots/functions-connector-md.md |
| Google Login Connector.Md: google, connector, login | google_login_connector.md | https://docs.pingidentity.com/connectors/google_login_connector.md | references/snapshots/google-login-connector-md.md |
| Google Workspace Admin Connector.Md: admin, connector, google | google_workspace_admin_connector.md | https://docs.pingidentity.com/connectors/google_workspace_admin_connector.md | references/snapshots/google-workspace-admin-connector-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.

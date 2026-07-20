---
title: Add-on capabilities
description: Optional add-on capabilities for Advanced Identity Cloud, including access management, governance, reporting, and network security features
component: pingoneaic
page_id: pingoneaic:product-information:add-on-capabilities
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/add-on-capabilities.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Deployment", "Planning", "Governance", "Autonomous Access", "Tenants"]
section_ids:
  access-management-add-ons: Access management
  environment-management-add-ons: Environment management
  governance-and-reporting-add-ons: Governance and reporting
  network-security-add-ons: Network security
---

# Add-on capabilities

Add-on capabilities are features or integrated products that enhance PingOne Advanced Identity Cloud, but are not part of the standard offering. They can each be added to your tenant environments for an additional subscription; contact your Ping Identity representative to arrange this.

The following wording identifies add-on capabilities in the Advanced Identity Cloud documentation:

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud add-on capabilityContact your Ping Identity representative if you want to add this feature to your Advanced Identity Cloud subscription. |

## Access management

| Capability             | Summary                                                                                                                                                                                                                                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WS-Federation/WS-Trust | Lets you integrate Advanced Identity Cloud with Microsoft 365 and other service providers (SPs) to provide SSO using the WS-Federation identity protocol. Microsoft 365 also supports using the WS-Trust protocol.Learn more in [Register an SSO application](../app-management/register-a-custom-application.html#register-SSO-application). |

## Environment management

| Capability                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Multi-region high availability | Lets you deploy your Advanced Identity Cloud tenant environments across multiple geographic regions to enhance availability and disaster recovery capabilities.Learn more in [Architecture, availability, and disaster recovery](../tenants/environments-architecture-availability-disaster-recovery.html).	This capability is dependent on Outbound static IP addresses.                                               |
| Sandbox tenant environment     | Standalone environment that lets you experiment with new configuration or test new use cases without affecting other environments.Learn more in [Sandbox tenant environment](../tenants/environments-sandbox.html).                                                                                                                                                                                                     |
| UAT tenant environment         | Additional environment that you can add to your standard promotion group of [development, staging, and production tenant environments](../tenants/environments-development-staging-production.html). It has the same capabilities as your staging environment, allowing you to test your development changes in a production-like environment.Learn more in [UAT tenant environment](../tenants/environments-uat.html). |

## Governance and reporting

| Capability                  | Summary                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Advanced Reporting          | Lets you create custom reports on activity in your Advanced Identity Cloud tenant environment. You can query a number of metrics to create useful reports for your company.Learn more in [Advanced Reporting](../reports/administration/advanced-reports.html).                                                                                         |
| Agent Governance            | Lets you discover, onboard, and govern agents you've created in external AI agent platforms, such as AWS Bedrock and Azure AI Foundry. You can view and manage agent profiles, certify entitlements, and request access to tools on behalf of agents.Learn more in [Agent Governance](../identity-governance/administration/iga-agent-governance.html). |
| PingOne Identity Governance | Lets you centrally administer and manage user access to applications and data across your organization to support regulatory compliance.Learn more in [What is PingOne Identity Governance?](../identity-governance/administration/getting-started-what-is-iga.html).                                                                                   |

## Network security

| Capability     | Summary                                                                                                                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Secure Connect | Lets you connect to Advanced Identity Cloud directly from your private network without using the public internet.Learn more in [Create private network connections with Secure Connect](../tenants/secure-connect.html). |

---

---
title: Advanced Identity Cloud penetration testing and load testing policy
description: Policy for penetration and load testing of Advanced Identity Cloud, covering permitted activities, restrictions, and test plan requirements
component: pingoneaic
page_id: pingoneaic:product-information:penetration-and-load-testing-policy
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/penetration-and-load-testing-policy.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Getting started", "Policy", "Testing", "Penetration Testing", "Load Testing"]
section_ids:
  policy: Policy
  policy-rules: Policy rules
  policy-summary: Policy summary
  create-a-test-plan: Create a test plan
  test-plan-information: Test plan information
---

# Advanced Identity Cloud penetration testing and load testing policy

Ping Identity has a strict policy on the penetration testing and load testing of your PingOne Advanced Identity Cloud infrastructure and applications.

The policy exists for the following reasons:

* Preserves platform stability

  The policy preserves platform stability for all Ping Identity customers.

  Unscheduled testing can cause severe problems, as it can initially be indistinguishable from a real problem or a DoS attack. It can set off alarms, cause service shutdowns, add services to denylists, and prevent the support team from taking remedial actions. It can also disproportionally occupy our support team, delaying our response to other Ping Identity customers with pressing support problems.

* Regulates testing

  The policy regulates how testing is approached so that it is realistic and manageable.

  For example, a load testing plan would not be approved if it created and deleted large numbers of identities and entitlements for each test, as this is a hugely expensive operation, but not a realistic pattern of behavior.

* Avoids unnecessary testing

  The policy helps you avoid unnecessary testing.

  Ping Identity already directly tests Advanced Identity Cloud infrastructure and applications on your behalf, using code scans, penetration tests, and automated load tests. This ensures that testing is consistent and that results can be compared over time.

  The penetration testing is done by a third party, in line with industry best practice. The results of the penetration testing are shared with you, with the time-consuming analysis and elimination of false positives already done by our engineers.

## Policy

### Policy rules

* You are not permitted to directly test Advanced Identity Cloud infrastructure and applications. In particular, this applies to DoS or DDoS attacks. Ping Identity already does this on your behalf.

* You are permitted to indirectly test Advanced Identity Cloud infrastructure and applications as part of a wider test of your own infrastructure and applications.

* You are permitted to perform penetration testing and load testing only against your staging and UAT\[[1](#_footnotedef_1 "View footnote.")] environments.

  |   |                                                                                                                                                                                                                                                                                                                        |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Staging, UAT, and production environments are configured with equivalent resource allocations and monitored to ensure alignment; load testing performed in staging and UAT environments accurately reflects production behavior. However, staging and UAT environments must never be used to serve production traffic. |

* You are permitted to perform penetration testing and load testing only up to a maximum of 2 weeks per test plan.

* You are permitted to perform load testing only up to the license volume limits listed in the [Test plan information](#test-plan-information) section.

* You are not permitted to use the [built-in SMTP server](../tenants/email-provider.html) as the email provider. If you have any email-dependent journeys, you must configure your own [external email service](../tenants/email-provider.html) as the email provider.

* You are not permitted to perform penetration testing or load testing without Ping Identity's prior written consent.

* You are not permitted to authorize a third party to perform penetration testing or load testing without Ping Identity's prior written consent.

* To obtain Ping Identity's prior written consent you must [create a test plan](#create-a-test-plan) and have it reviewed and approved by Ping Identity.

* You must provide at least 2 weeks' notice of the testing start date.

### Policy summary

| Development environment                           | Staging and UAT\[[1](#_footnotedef_1 "View footnote.")] environments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Production environment                            |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| 	No penetration testing or load testing permitted | * Indirect penetration testing and load testing permitted as part of a wider test of your own infrastructure and applications

* DoS or DDoS attacks not permitted

* Load testing permitted only up to your license volume limits

* Penetration testing and load testing permitted only up to a maximum of two weeks per test plan

* Use of [built-in SMTP server](../tenants/email-provider.html) not permitted for testing

* Penetration testing and load testing only permitted with Ping Identity's prior written consent, an approved [test plan](#create-a-test-plan), and at least two weeks' notice | 	No penetration testing or load testing permitted |

## Create a test plan

1. Go to <https://support.pingidentity.com>.

2. Click Create a case.

3. Follow the steps in the case submission wizard by selecting your account and contract and answering questions about your tenant environments.

4. On the Please answer the following questions to help us understand the issue you're facing page, enter the following details, and then click Next:

   | Field                                                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | What product family is experiencing the issue?       | Select PingOne Advanced Identity Cloud                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | What specific product is experiencing the issue?     | * For penetration testing requests, select Penetration Test Request.

   * For load testing requests for Advanced Identity Cloud, select Performance/Load Test Request - AIC Only.

   * For load testing requests for a particular PingOne integration, select one of the following:

     * Performance/Load Test Request - Credentials Integration

     * Performance/Load Test Request - Protect Integration

     * Performance/Load Test Request - Verify Integration |
   | What version of the product are you using?           | Select NA                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | What Hostname(s) or Tenant ID(s) does this apply to? | Enter the FQDN of your staging tenant environment.                                                                                                                                                                                                                                                                                                                                                                                                            |

5. On the Tell us about the issue page, enter the following details, and then click Next:

   | Field                                      | Value                                                                                                                                                                                                                          |
   | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | Provide a descriptive title for your issue | Enter one of the following:- `Submit a load testing request`

   - `Submit a penetration testing request`                                                                                                                         |
   | Describe the issue below                   | Enter the following details:- [Test plan information](#test-plan-information)

   - Within a maximum permitted duration of 2 weeks, the dates and times that you intend to do the testing, including the start date and end date. |

6. Click Submit.

### Test plan information

| Information             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Testing strategy        | Describe the strategy you intend to follow when testing your own infrastructure and applications. For load testing plans, indicate the number of identities you intend to create, and the throughput levels you intend to simulate. These should be in line with the number of identities and throughput agreed with Ping Identity when your Advanced Identity Cloud service was provisioned, and not go above the following thresholds:- Agreed number of identities +25%

- Agreed throughput +50%Your load testing plan should also avoid unrealistic patterns such as the setup and teardown of large numbers of identities for each load test. |
| Origin of testing       | Confirm if the testing will originate from an external source over the internet or from an internal source within your Advanced Identity Cloud tenant environments. If originating from an external source, you must also supply IP addresses.                                                                                                                                                                                                                                                                                                                                                                                                      |
| Named contact           | Provide a named point of contact in your testing team in case Ping Identity requires the testing to be stopped due of unforeseen impacts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Vulnerability discovery | Confirm that in the unlikely event that a vulnerability is discovered in Advanced Identity Cloud infrastructure or applications:- That the vulnerability will be tested no further than the point of discovery

- That a description of the vulnerability will be promptly and responsibly disclosed to Ping Identity                                                                                                                                                                                                                                                                                                                               |

***

[1](#_footnoteref_1). A [user acceptance testing (UAT) environment](../tenants/environments-uat.html) is an [add-on capability](add-on-capabilities.html).

---

---
title: Application management migration FAQ
description: FAQ on the improved application management UI in Advanced Identity Cloud, available for tenants created on or after January 12, 2023
component: pingoneaic
page_id: pingoneaic:product-information:migration-dependent-features/application-management-migration-faq
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/migration-dependent-features/application-management-migration-faq.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Tenants", "Application Management", "Migration"]
section_ids:
  how_is_application_management_changing: How is application management changing?
  how_is_the_improved_application_management_ui_being_introduced: How is the improved application management UI being introduced?
  what_documentation_should_i_use: What documentation should I use?
  how_can_i_upgrade_my_tenants: How can I upgrade my tenants?
---

# Application management migration FAQ

Application management allows you to manage the security and access of common and custom relying-party applications and SAML 2.0 applications directly from PingOne Advanced Identity Cloud. This functionality is most commonly used to manage data and system access for employees within an organization, commonly referred to as *workforce identity and access management*.

## How is application management changing?

Ping Identity has improved application management by introducing a single UI interface to the Advanced Identity Cloud admin console that manages all aspects of an application relevant to Advanced Identity Cloud. This replaces the previous arrangement, which required a combination of actions across the Advanced Identity Cloud admin console, AM native admin console, and IDM admin console. In addition, Ping Identity has introduced an application catalog to speed up application configuration for common use cases.

## How is the improved application management UI being introduced?

The improved application management UI is only available in tenants created on or after January 12, 2023.

## What documentation should I use?

* For tenants created on or after January 12, 2023, learn more in [Application management](../../app-management/applications.html).

* For tenants created before January 12, 2023, learn more in [Application management (legacy)](../../realms/applications.html).

## How can I upgrade my tenants?

There are no instructions yet on how to upgrade your tenants.

---

---
title: Data regions
description: Global data regions where Advanced Identity Cloud is available, with a breakdown of product availability by region
component: pingoneaic
page_id: pingoneaic:product-information:global-identity-cloud-locations
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/global-identity-cloud-locations.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Tenants", "Region"]
page_aliases: ["pingoneaic::plan-deploy:global-identity-cloud-locations.adoc"]
section_ids:
  product-availability-by-region: Product availability by region
---

# Data regions

Ping Identity provides PingOne Advanced Identity Cloud capabilities at worldwide geographic locations, or *regions*. Learn more about data regions in [Data residency](../tenants/environments-data-residency.html).

![Map of global data regions](_images/global-data-regions.png)

## Product availability by region

| Region Group      | Location (Region)                  | Advanced Identity Cloud  | Identity Governance and Administration & Autonomous Identity |
| ----------------- | ---------------------------------- | ------------------------ | ------------------------------------------------------------ |
| **Canada**        | Montreal (northamerica-northeast1) | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
| **United States** | Oregon (usa-west1)                 | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
|                   | Los Angeles (usa-west2)            | [icon: check, set=fa]Yes | [icon: times, set=fa]No                                      |
|                   | Iowa (usa-central1)                | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
|                   | South Carolina (usa-east1)         | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
|                   | North Virginia (usa-east4)         | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
| **Brazil**        | São Paolo (southamerica-east1)     | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
| **Europe**        | Finland (europe-north1)            | [icon: check, set=fa]Yes | [icon: times, set=fa]No                                      |
|                   | Belgium (europe-west1)             | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
|                   | London (europe-west2)              | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
|                   | Frankfurt (europe-west3)           | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
|                   | Netherlands (europe-west4)         | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
|                   | Zurich (europe-west6)              | [icon: check, set=fa]Yes | [icon: times, set=fa]No                                      |
|                   | Paris (europe-west9)               | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
| **Middle East**   | Doha (me-central1)                 | [icon: check, set=fa]Yes | [icon: times, set=fa]No                                      |
|                   | Dammam (me-central2)               | [icon: check, set=fa]Yes | [icon: times, set=fa]No                                      |
| **Asia**          | Singapore (asia-southeast1)        | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
|                   | Jakarta (asia-southeast2)          | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |
|                   | Hong Kong (asia-east2)             | [icon: check, set=fa]Yes | [icon: times, set=fa]No                                      |
| **Australia**     | Sydney (australia-southeast1)      | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                                     |

---

---
title: Deferred release migration FAQ
description: FAQ on the deferred release feature becoming standard in Advanced Identity Cloud, covering how new and existing production tenants are affected
component: pingoneaic
page_id: pingoneaic:product-information:migration-dependent-features/deferred-release-migration-faq
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/migration-dependent-features/deferred-release-migration-faq.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  what-has-changed: What has changed?
  why-has-this-changed: Why has this changed?
  how-are-new-tenants-affected: How are new tenants affected?
  how-are-existing-tenants-affected: How are existing tenants affected?
  how-can-i-prepare-for-the-change: How can I prepare for the change?
  what-if-i-dont-want-to-use-the-deferred-release-feature: What if I don't want to use the deferred release feature?
---

# Deferred release migration FAQ

## What has changed?

When the [deferred release](../../release-notes/release-deferral.html) feature was introduced, it was an opt-in feature. This meant that Advanced Identity Cloud customers could choose whether to enable the feature for their tenants. From October 21, 2025, the deferred release feature has changed so it's a standard feature.

## Why has this changed?

By making deferred release a standard feature, Ping Identity is enhancing the release experience for all customers and delivering a consistent and controlled approach to managing change in production:

* You can defer production upgrades for up to 7 days. This lets you validate new features and updates in your lower environments before they reach production.

* You can trigger the production upgrade at any time during the 7-day deferral period. You can also select a preferred upgrade time in UTC for the automatic production upgrade at the end of the 7-day deferral period. This lets you align production upgrades with your organization's change management processes and minimize disruption to your end users.

## How are new tenants affected?

Production tenants created on or after October 21, 2025 have the deferred release feature as standard.

## How are existing tenants affected?

Existing production tenants that already have the deferred release feature enabled aren't affected by this change.

Existing production tenants that don't yet have the deferred release feature enabled will be migrated in phases, with each phase preceded by a 4-week notice period to let you prepare.

## How can I prepare for the change?

If you have an existing production tenant that doesn't yet have the deferred release feature enabled, your Ping Identity representative will contact you to discuss the migration process and help you prepare for the change. You'll have 4 weeks' notice before your tenant is migrated. When your migration date arrives, Ping Identity will make the necessary changes to enable the deferred release feature for your production tenant.

## What if I don't want to use the deferred release feature?

If you don't want to use the deferred release feature, you can choose to trigger a release upgrade to your production environment immediately by running a promotion.

---

---
title: Deprecation notices
description: Deprecation notices and end-of-life dates for Advanced Identity Cloud features, API endpoints, and services
component: pingoneaic
page_id: pingoneaic:product-information:deprecation-notices
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/deprecation-notices.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Getting started", "Deployment", "Planning", "Administration", "Scripts", "Email"]
page_aliases: ["pingoneaic::changelog-deprecation-notices.adoc"]
section_ids:
  saml2-inactive-cots: SAML 2.0 authentication with an inactive circle of trust
  node-rest-api-endpoints: Authentication node REST API endpoints
  rsa-securid-node: RSA SecurID Marketplace node
  deprecation-non-persisted-schedules: Non-persisted schedules
  pingone-marketplace-nodes: PingOne Verify service and PingOne Marketplace nodes
  idc-cli-oauth-client: IDC.CLI OAuth 2.0 client
  esv-rest-api-using-resource-version-1: Access to ESV REST API endpoints using resource version 1.0
  esv-rest-api-using-idm-scope: Access to ESV REST API endpoints using fr:idm:* scope
  auto-access-deprecation: Autonomous Access
  duo-node-deprecation: Duo authentication node
  introspect-endpoint: Introspect endpoint GET requests and URL query string parameters
  health-check-endpoints: Health check endpoints
  skip-option-2-step-verification: Skip option for 2-step verification registration for Advanced Identity Cloud tenant administrators
  forgerock_identity_cloud_email_server_service: ForgeRock Identity Cloud Email Server Service
  groovy_oidc_custom_claims_script: Groovy OIDC Custom Claims Script
---

# Deprecation notices

For information about the PingOne Advanced Identity Cloud product lifecycle and deprecation, learn more in [Deprecation and end of life](release-lifecycle.html#deprecation-and-end-of-life).

## SAML 2.0 authentication with an inactive circle of trust

* Notification date

  July 14, 2026

  Previously, Advanced Identity Cloud allowed authentication to continue even when a circle of trust (CoT) was marked as inactive. This behavior is now deprecated.

  After the end-of-life date, Advanced Identity Cloud will always enforce the CoT status. Review your SAML 2.0 configurations and make sure that any CoTs used for authentication are marked as active.

* End-of-life date

  July 14, 2027

## Authentication node REST API endpoints

* Notification date

  July 1, 2026

  Resource versions 1.0 and 2.0 are deprecated for the `realm-config/authentication/authenticationtrees` endpoint. Use resource version 3.0 instead.

  Versionless node endpoints are also deprecated. Make sure you always specify the node version in the request URL.

* End-of-life date

  July 1, 2027

## RSA SecurID Marketplace node

* Notification date

  March 31, 2026

  The Marketplace [RSA SecurID](https://docs.pingidentity.com/auth-node-ref/latest/cloud/rsa-securid.html) node is deprecated. It has been superseded by the [RSA SecurID](https://docs.pingidentity.com/auth-node-ref/latest/rsa-securid.html) node, which has the same functionality and is available to all Advanced Identity Cloud customers as part of their standard subscription. You must update your journeys to use the new node before the end-of-life date.

* End-of-life date

  March 31, 2027

## Non-persisted schedules

* Notification date

  March 17, 2026

  Non-persisted (in memory) schedules are deprecated. Update your tenants to use [persisted schedules](../idm-schedules/persistent-schedules.html). You can continue to use non-persisted schedules in the short term, but they will be removed on the end-of-life date.

* End-of-life date

  March 31, 2027

## PingOne Verify service and PingOne Marketplace nodes

* Notification date

  November 20, 2025

  The PingOne Verify service is deprecated. Use [PingOne product connections](../integrations/pingone-set-up-product-connections.html) instead.

  The following Marketplace nodes are deprecated:

  * [PingOne node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone.html)

  * [PingOne Verify Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-authn.html)

  * [PingOne Verify Proofing node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-proof.html)

  Depending on your use case, use the following nodes instead:

  * [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html)

  * [PingOne Verify Completion Decision node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-completion-decision.html)

  * [PingOne Identity Match node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-identity-match.html)

  * [PingOne Create User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-create-user.html)

  * [PingOne Delete User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-delete-user.html)

  * [PingOne DaVinci node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-davinci.html)

* End-of-life date

  November 30, 2026

## IDC.CLI OAuth 2.0 client

* Notification date

  June 24, 2025

  Ping Identity is no longer provisioning the `IDC.CLI` OAuth 2.0 client in new tenants and has deprecated it in existing tenants.

  If you have any automation or scripts that rely on using the `IDC.CLI` OAuth 2.0 client in existing tenants, you must update them to use a service account before the end-of-life date when the client will be removed.

* End-of-life date

  June 26, 2026

## Access to ESV REST API endpoints using resource version `1.0`

* Notification date

  June 24, 2025

  Ping Identity has deprecated the use of resource version `1.0` to access ESV REST API endpoints in Advanced Identity Cloud.

  In the short term, you can continue to use the `1.0` resource version to access to ESV REST API endpoints, but this won't be possible after the end-of-life date.

  If you have any automation or scripts that rely on using the `1.0` resource version for ESV REST API endpoints, you must update them to use resource version `2.0` before the end-of-life date.

* End-of-life date

  June 26, 2026

## Access to ESV REST API endpoints using `fr:idm:*` scope

* Notification date

  June 24, 2025

  Ping Identity has deprecated use of the `fr:idm:*` scope to access ESV REST API endpoints in Advanced Identity Cloud.

  In the short term, you can continue to use the scope to access ESV REST API endpoints, but this won't be possible after the end-of-life date.

  If you have any automation or scripts that rely on using the scope for ESV REST API endpoints, you must update them to use the `fr:idc:esv:*` scope or an appropriate child scope (`fr:idc:esv:read`, `fr:idc:esv:update`, or `fr:idc:esv:restart`) before the end-of-life date.

* End-of-life date

  June 26, 2026

## Autonomous Access

* Notification date

  November 18, 2024

  Ping Identity has deprecated Autonomous Access. The product will reach end of life on October 31, 2025. During the deprecation period, Ping Identity will not provide new patches, updates, or new features for Autonomous Access.

  To support our Autonomous Access customers, we're providing migration assistance to PingOne Protect. This advanced threat detection solution leverages machine learning to analyze authentication signals and detect abnormal online behavior. PingOne Protect is a well-established product trusted by hundreds of customers worldwide.

  The Autonomous Access documentation has moved to the documentation archive at <https://docs.pingidentity.com/archive/>.

* End-of-life date

  October 31, 2025

## Duo authentication node

* Notification date

  March 5, 2024

  ForgeRock has deprecated the Duo authentication node because [Duo has deprecated Traditional Duo Prompt](https://help.duo.com/s/article/8193?language=en_US#traditionalprompt) that is used by the Duo node.

  ForgeRock created [Duo Universal Prompt node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/duo-univ-prompt.html) in anticipation of this depreciation. You should use [Duo Universal Prompt node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/duo-univ-prompt.html) instead of [Duo node (Deprecated)](https://docs.pingidentity.com/auth-node-ref/latest/cloud/duo.html).

* End-of-life date

  September 30, 2024

## Introspect endpoint GET requests and URL query string parameters

* Notification date

  July 19, 2023

  ForgeRock has deprecated the following behaviors of the OAuth 2.0 `introspect` endpoint in Advanced Identity Cloud:

  * Accept GET requests

  * Accept data in POST requests from URL query string parameters

  You can continue to use these behaviors, but they will be removed on July 19, 2024. Instead, when using the OAuth 2.0 `introspect` endpoint, you should use POST requests and pass data in the POST request body.

* End-of-life date

  July 19, 2024

## Health check endpoints

* Notification date

  June 13, 2023

  ForgeRock has deprecated the following Advanced Identity Cloud health check endpoints:

  * `/am/isAlive.jsp`

  * `/am/json/health/live`

  * `/am/json/health/ready`

  * `/openidm/info/ping`

  You can continue to use the endpoints, but they will be removed on June 13, 2024. You should update any external monitoring to use the Advanced Identity Cloud `/monitoring/health` endpoint instead. Learn more in [Monitor using health check endpoint](../tenants/monitoring.html#monitor-using-health-check-endpoint).

* End-of-life date

  June 13, 2024

## Skip option for 2-step verification registration for Advanced Identity Cloud tenant administrators

* Notification date

  February 3, 2023

  ForgeRock has deprecated the option to let Advanced Identity Cloud tenant administrators skip 2-step verification. You can continue to use the skip option in your tenants, but this functionality will be removed from Advanced Identity Cloud on April 2, 2024. Learn more in [Tenant administrator mandatory 2-step verification FAQ](migration-dependent-features/tenant-administrator-mandatory-2-step-verification-faq.html).

* End-of-life date

  April 2, 2024

## ForgeRock Identity Cloud Email Server Service

* Notification date

  April 12, 2021

  Built-in Email Server Service

  ForgeRock no longer supports the default email provider settings for use in production. The default email provider settings will only be available for testing purposes. Current customers can continue to use the default email provider settings for production purposes, but this functionality will reach end of life on April 12, 2022. Customers should move to using their own email provider.

* End-of-life date

  April 12, 2022

## Groovy OIDC Custom Claims Script

* Notification date

  April 20, 2021

  ForgeRock will continue to support the Groovy version of the OIDC custom claims script until it is end of lifed on April 20th 2022. Current customers can continue to use the Groovy version of the OIDC custom claims script for production purposes, but this functionality will reach end of life on April 20, 2022.

* End-of-life date

  April 20, 2022

---

---
title: Event hooks migration FAQ
description: FAQ on event hooks in Advanced Identity Cloud, which trigger scripts during identity object lifecycle stages in tenants created from January 12, 2023
component: pingoneaic
page_id: pingoneaic:product-information:migration-dependent-features/event-hooks-migration-faq
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/migration-dependent-features/event-hooks-migration-faq.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Migration", "Extensibility", "Scripts", "Identities"]
section_ids:
  what_has_changed: What has changed?
  how_are_event_hooks_being_introduced: How are event hooks being introduced?
  does_this_affect_any_other_features: Does this affect any other features?
  how_can_i_upgrade_my_tenants: How can I upgrade my tenants?
---

# Event hooks migration FAQ

## What has changed?

Ping Identity has introduced [event hooks](../../developer-docs/scripting-event-hooks.html) to PingOne Advanced Identity Cloud to let you trigger scripts during various stages of an identity object lifecycle.

## How are event hooks being introduced?

Event hooks are only available in tenants created on or after January 12, 2023.

## Does this affect any other features?

Yes. If you have not upgraded your tenant to enable groups, event hooks are not available for group identities. Learn more in [Group identity migration FAQ](group-identity-migration-faq.html).

## How can I upgrade my tenants?

There are no instructions yet on how to upgrade your tenants.

---

---
title: Group identity migration FAQ
description: FAQ on group identity in Advanced Identity Cloud, which simplifies managing permissions for user collections, and how to enable it in older tenants
component: pingoneaic
page_id: pingoneaic:product-information:migration-dependent-features/group-identity-migration-faq
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/migration-dependent-features/group-identity-migration-faq.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Groups", "Identities", "Migration"]
section_ids:
  what_has_changed: What has changed?
  how_is_the_group_identity_being_introduced: How is the group identity being introduced?
  does_this_affect_any_other_features: Does this affect any other features?
  what_documentation_should_i_use: What documentation should I use?
---

# Group identity migration FAQ

## What has changed?

Ping Identity has introduced a group identity to PingOne Advanced Identity Cloud to simplify the management of permissions and authorizations for collections of users.

## How is the group identity being introduced?

Tenants created on or after November 29, 2022 have the group identity enabled by default. Tenants created before that date can follow an upgrade path to enable it; learn more in [Enable groups](../../idm-objects/groups.html).

## Does this affect any other features?

Yes. If you have not upgraded your tenant, [event hooks](../../developer-docs/scripting-event-hooks.html) are not available for group identities.

## What documentation should I use?

Learn more in [Group management](../../idm-objects/groups.html).

---

---
title: Identity Cloud product lifecycle and releases
description: "Advanced Identity Cloud release lifecycle stages: early access, beta, limited availability, general availability, deprecation, and end of life"
component: pingoneaic
page_id: pingoneaic:product-information:release-lifecycle
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/release-lifecycle.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Getting started", "Deployment", "Planning"]
page_aliases: ["pingoneaic::changelog-release-lifecycle.adoc"]
section_ids:
  early-access: Early access
  beta: Beta
  upcoming-features: Upcoming features
  limited-availability: Limited availability
  general-availability: General availability
  migration-dependent-features: Migration dependent features
  bug-fixes-and-low-impact-changes: Bug fixes and low impact changes
  deprecation-and-end-of-life: Deprecation and end of life
  deprecated-features: Deprecated functionality
  deprecation-notification: Deprecation notification
  during-deprecation: During deprecation
  end-of-life: End of life
---

# Identity Cloud product lifecycle and releases

PingOne Advanced Identity Cloud releases new features, updates functionality and fixes bugs on a continual cadence. Ping Identity aims to deliver features and functionality that will be the most useful, complete and intuitive for customers. In order to deliver on this goal we have several stages to our release lifecycle.

* [Early access](#early-access)

* [Beta](#beta)

* [Upcoming features](#upcoming-features)

* [Limited availability](#limited-availability)

* [General availability](#general-availability)

* [Migration dependent features](#migration-dependent-features)

* [Bug fixes and low impact changes](#bug-fixes-and-low-impact-changes)

* [Deprecation and end of life](#deprecation-and-end-of-life)

## Early access

Participating in Early Access programs allow customers to provide feedback and collaborate with Ping Identity in designing future capabilities in the product.

Select customers are invited to provide feedback on new features. Customers are encouraged to give feedback and have an active say in product direction; product management and customer success will work with you to gather feedback. Features may be unstable, changed in backward-incompatible ways, and are not guaranteed to be released. We will use all reasonable efforts to communicate breaking changes to customers participating in the program.

## Beta

Beta features give customers advanced insights into up-and-coming product capabilities with extra time to prepare to adopt the feature and provide design feedback to the product team. Generally speaking, functionality is stable and meets security and quality expectations but please note that a beta feature is not officially supported for production use.

## Upcoming features

Customers receive notifications of new and upcoming features at least a week in advance of a release. The notifications provide customers with high-level information on changes or new functionality.

## Limited availability

Features are available for production use and are fully functional and supported; however, they are available only to a select set of customers.

## General availability

Features are available for production use and are fully functional and supported. They are available to all customers.

## Migration dependent features

Features are not backward compatible and require a tenant migration before they can be used. Learn more in [Migration dependent features](migration-dependent-features.html).

## Bug fixes and low impact changes

On an ongoing basis, Ping Identity makes bug fixes and low impact changes as necessary to Advanced Identity Cloud. These types of fixes are deployed as necessary. You can monitor these in the [Regular channel changelog](../release-notes/regular-channel-changelog.html) and [Rapid channel changelog](../release-notes/rapid-channel-changelog.html). You can also subscribe to the RSS feeds mentioned at the start of the two changelog pages.

## Deprecation and end of life

To maintain both security and quality in Advanced Identity Cloud, we periodically have to modify or remove functionality.

Learn more in [Deprecation Notices](deprecation-notices.html).

### Deprecated functionality

Deprecated functionality can include features, behaviors, API endpoints, or node versions. Functionality flagged as deprecated means it's no longer actively enhanced and is minimally maintained. Tenants using the functionality at the time of deprecation will continue to have access to the deprecated functionality until it reaches end of life, at which point customers will no longer have access to the functionality. We know deprecation disruptions are inconvenient, and as such, we attempt to limit the frequency of deprecations and to pair them with alternative options and migration recommendations where available.

### Deprecation notification

Deprecation information is posted to the Advanced Identity Cloud documentation. [Deprecation notices](deprecation-notices.html) typically include a date the deprecated functionality reaches end of life. Our policy is to flag functionality for deprecation with at least 12 months advance notice prior to end of life whenever possible to allow a 12 month migration window.

Periodically, and in case of emergency (critical vulnerabilities or changes required by applicable law or third-party certification standards), we may accelerate this time frame. In such cases, we will provide as much prior notice as is reasonable under the circumstances.

### During deprecation

Customers should engage in a migration to move away from the deprecated functionality.

### End of life

Features that reach the end of life stage are removed from the platform. Continued use of these features will likely result in errors.

---

---
title: Migration dependent features
description: Features in Advanced Identity Cloud that require tenant migration before they can be used, with effective dates and migration summaries
component: pingoneaic
page_id: pingoneaic:product-information:migration-dependent-features
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/migration-dependent-features.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Getting started", "Deployment", "Planning", "Migration", "Tenants", "Application Management", "Groups", "Promotion"]
section_ids:
  summary-of-migration-dependent-features: Summary of migration dependent features
---

# Migration dependent features

Certain PingOne Advanced Identity Cloud features require changes to your tenant environments before they can be introduced. In such cases, Ping Identity defines a migration strategy for the feature. Some examples of feature migration strategies are:

* Updating the format of your static configuration

* Updating the way your automated applications are configured

* Restricting the new feature only to tenants built after the feature is introduced

## Summary of migration dependent features

| Feature                                            | Effective date | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deferred release feature as standard               | 2025-10-21     | Ping Identity has changed the deferred release feature so it's no longer an opt-in feature. Tenants created on or after October 21, 2025 now have the deferred release feature as standard. Existing tenants that don't yet have the deferred release feature enabled will be migrated in phases, with each phase preceded by a 4-week notice period to let you prepare. Learn more in [Deferred release migration FAQ](migration-dependent-features/deferred-release-migration-faq.html).                                                                                   |
| Secure RCS access                                  | 2025-06-10     | Ping Identity has introduced the ability to secure the `openicf` WebSocket endpoint used for communication between RCS client mode and Advanced Identity Cloud connector servers. This feature is enabled by default in tenants created on or after June 10, 2025. Learn how to enable the feature in tenants created before that date in [RCS configuration migration FAQ](migration-dependent-features/rcs-configuration-migration-faq.html).                                                                                                                              |
| Two-factor authentication (2FA) profile attributes | 2025-01-09     | Ping Identity has introduced five multivalue (array) string attributes that can be used to store references to a user's associated two-factor authentication (2FA) devices.- `deviceProfiles`

- `devicePrintProfiles`

- `webauthnDeviceProfiles`

- `oathDeviceProfiles`

- `pushDeviceProfiles`These five attributes are enabled by default in tenants created on or after January 09, 2025. Learn how to enable them in tenants created before that date in [2FA profile attributes](../idm-rest-api/endpoints/rest-feature.html#feature-enable-2fa-profile-attributes). |
| Additional indexed string attributes               | 2024-11-12     | Ping Identity has introduced 15 additional indexed string attributes that can be used as general purpose extension attributes. These 15 attributes are enabled by default in tenants created on or after November 12, 2024. Learn how to enable them in tenants created before that date in [Additional indexed string attributes](../idm-rest-api/endpoints/rest-feature.html#feature-enable-indexed-string-attributes).                                                                                                                                                    |
| Password timestamp attributes                      | 2024-02-06     | Ping Identity has introduced two indexed string attributes that can be used to query when a user password was last changed and when it is set to expire:- `passwordLastChangedTime`

- `passwordExpirationTime`These two attributes are enabled by default in tenants created on or after February 06, 2024. Learn how to enable them in tenants created before that date in [Password timestamp attributes](../idm-rest-api/endpoints/rest-feature.html#feature-enable-pass-timestamp-attributes).                                                                          |
| Outbound static IP addresses                       | 2023-04-18     | ForgeRock has introduced outbound static IP addresses to each of your tenant environments. Outbound static IP addresses are enabled by default in tenants created on or after April 18, 2023. To enable in tenants created before that date, you can raise a support ticket.Learn more in [Outbound static IP addresses](../tenants/environments-outbound-static-ip-addresses.html).	This feature is a dependency for Proxy Connect and Multi-region high availability.                                                                                                      |
| Tenant administrator mandatory 2-step verification | 2023-02-03     | ForgeRock has deprecated the option to let Advanced Identity Cloud tenant administrators skip 2-step verification. Customers can continue to use the skip option in their tenants, but this functionality will be removed from Advanced Identity Cloud on April 2, 2024.Learn more in [Tenant administrator mandatory 2-step verification FAQ](migration-dependent-features/tenant-administrator-mandatory-2-step-verification-faq.html).                                                                                                                                    |
| Application management                             | 2023-01-12     | ForgeRock has introduced an improved application management UI to Advanced Identity Cloud. The UI is only available in tenants created on or after January 12, 2023.Learn more in [Application management migration FAQ](migration-dependent-features/application-management-migration-faq.html).                                                                                                                                                                                                                                                                            |
| Event hooks                                        | 2023-01-12     | ForgeRock has introduced event hooks to Advanced Identity Cloud. This feature is only available in tenants created on or after January 12, 2023.Learn more in [Event hooks migration FAQ](migration-dependent-features/event-hooks-migration-faq.html).                                                                                                                                                                                                                                                                                                                      |
| Group identity                                     | 2022-11-29     | ForgeRock has introduced a group identity to simplify the management of permissions and authorizations for collections of users. The group identity is enabled by default in tenants created on or after November 29, 2022. Tenants created before that date can follow an upgrade path to enable it.Learn more in [Group identity migration FAQ](migration-dependent-features/group-identity-migration-faq.html).                                                                                                                                                           |

---

---
title: RCS configuration migration FAQ
description: FAQ on configuring secure access rules for Remote Connector Server connections in Advanced Identity Cloud, with upgrade steps for existing tenants
component: pingoneaic
page_id: pingoneaic:product-information:migration-dependent-features/rcs-configuration-migration-faq
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/migration-dependent-features/rcs-configuration-migration-faq.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  what-has-changed: What has changed?
  why-do-i-need-to-add-this-feature-to-my-configuration: Why do I need to add this feature to my configuration?
  when-is-the-feature-being-introduced: When is the feature being introduced?
  is-the-feature-enabled-by-default-for-existing-tenants: Is the feature enabled by default for existing tenants?
  is-the-feature-enabled-by-default-for-new-tenants: Is the feature enabled by default for new tenants?
  how-can-i-upgrade-my-tenants: How can I upgrade my tenants?
  connector-servers-using-the-default-rcs-client-oauth2-client: Connector servers using the default RCSClient OAuth 2.0 client
  authentication-configuration-rcsclient: Authentication configuration
  access-configuration-rcsclient: Access configuration
  connector-servers-using-specific-oauth2-clients: Connector servers using specific OAuth 2.0 clients
  authentication-configuration-specific-clients: Authentication configuration
  access-configuration-specific-clients: Access configuration
  verify_the_configuration: Verify the configuration
  what-documentation-should-i-use: What documentation should I use?
---

# RCS configuration migration FAQ

## What has changed?

Ping Identity has introduced the ability to configure access rules for the `openicf` WebSocket endpoint used by Advanced Identity Cloud connector servers.

## Why do I need to add this feature to my configuration?

The feature lets you lock down Advanced Identity Cloud connector servers so that each connector server can be accessed only by an RCS connector using that connector server's designated OAuth 2.0 client. This prevents an RCS connector associated with a particular connector server from gaining unauthorized access to the resources of other connector servers.

As each Advanced Identity Cloud customer has a different arrangement of connector servers, Ping Identity can't configure this feature automatically. You must update the configuration in each of your tenant environments to suit your own connector server arrangement.

## When is the feature being introduced?

The feature was introduced on the following dates:

* June 10, 2025 for UAT\[[1](#_footnotedef_1 "View footnote.")], staging, and production tenant environments.

* May 23, 2025 for development and sandbox\[[2](#_footnotedef_2 "View footnote.")] tenant environments.

## Is the feature enabled by default for existing tenants?

No, the feature isn't enabled by default for existing tenant environments. To enable it, you must add access and authentication configuration for each of your existing connector servers. This process is explained in [How can I upgrade my tenants?](#how-can-i-upgrade-my-tenants)

|   |                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In each tenant environment, the feature is enabled as soon as you configure an access rule for any connector server. You must configure all existing connector servers at the same time per environment to prevent access issues. |

## Is the feature enabled by default for new tenants?

Yes, the feature is enabled by default for new tenant environments. However, it's only configured for connector servers created using the default `RCSClient` OAuth 2.0 client. If you create a connector server using a specific OAuth 2.0 client, you must add access and authentication configuration. This process is explained in step 2 in [How can I upgrade my tenants?](#how-can-i-upgrade-my-tenants)

## How can I upgrade my tenants?

This depends on whether the connector servers in your existing tenants are configured to use the default `RCSClient` OAuth 2.0 client, specific OAuth 2.0 clients, or a combination of both.

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The process of setting up an OAuth 2.0 client with a connector server is explained in [Register a remote server](../../identities/sync-identities.html#task-1-register-a-remote-server). |

### Connector servers using the default RCSClient OAuth 2.0 client

If any of your existing connector servers use the default `RCSClient` OAuth 2.0 client, you need to check or modify the configuration as follows.

|   |                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To ensure that only trusted connectors access a connector server, Ping Identity recommends that you migrate each of these connector servers to use specific OAuth 2.0 clients. |

#### Authentication configuration

For these connector servers, there's no need to update the authentication configuration, as Advanced Identity Cloud already has the following internal configuration:

Authentication configuration (internal)

```json
{
    "_id": "authentication",
    "rsFilter": {
        ...
        "staticUserMapping": [
            {
                "subject" : "RCSClient",
                "roles" : [
                    "rcsclient-authorized"
                ],
            }
        ...
        ],
    ...
    }
}
```

#### Access configuration

* If your tenant was created before June 10, 2025, you'll need to add the following access configuration. Use the instructions in [Change the access configuration over REST](../../idm-auth/authorization-and-roles.html#access-control-rest) to make the update.

  Access configuration (endpoint `/openidm/config/access`)

  ```json
  {
      "_id": "access",
      "configs": [
          ...
          {
              "methods": "read",
              "pattern": "*",
              "roles": "~rcsclient-authorized",
              "servlet": "openicf"
          },
          ...
      ]
  }
  ```

* If your tenant was created on or after June 10, 2025, you don't need to update the access configuration. The configuration in the previous bullet point is already present.

### Connector servers using specific OAuth 2.0 clients

If any of your existing connector servers use a specific OAuth 2.0 client, you need to check or modify the configuration as follows.

#### Authentication configuration

For each of these connector servers, add authentication configuration based on the following example. Use the instructions in [Change the authentication configuration over REST](../../idm-auth/authentication-and-roles.html#authentication-control-rest) to make the update.

Authentication configuration (endpoint `/openidm/config/authentication`)

```json
{
    "_id": "authentication",
    "rsFilter": {
        ...
        "staticUserMapping": [
            {
                "subject": "<oauth-client-id>", (1)
                "roles": [
                    "<role-name>" (2)
                ]
            }
        ...
        ],
    ...
    }
}
```

|       |                                                                                                                                                                                                      |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | Replace \<oauth-client-id> with the OAuth 2.0 client ID for the connector server. For example, `myrcs1-client`. This value is set in `connectorserver.clientId` in your RCS connector configuration. |
| **2** | Replace \<role-name> with the name of a custom role. For example, `myrcs1-client-authorized`. Ping Identity recommends that you create a separate role for each connector server.                    |

#### Access configuration

For each of these connector servers, add an access rule based on the following example. Use the instructions in [Change the access configuration over REST](../../idm-auth/authorization-and-roles.html#access-control-rest) to make the update.

Access configuration (endpoint `/openidm/config/access`)

```json
{
    "_id": "access",
    "configs": [
        ...
        {
            "servlet": "openicf",
            "pattern": "<connector-server-name>", (1)
            "roles": "<role-name>", (2)
            "methods": "read"
        },
        ...
    ]
}
```

|       |                                                                                                                                                                                                |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | Replace \<connector-server-name> with the name of the connector server. For example, `myrcs1`. This value is set in `connectorserver.connectorServerName` in your RCS connector configuration. |
| **2** | Replace \<role-name> with the name of the custom role specified in the corresponding `staticUserMapping` authentication configuration. For example, `myrcs1-client-authorized`.                |

### Verify the configuration

Restart all your RCS connectors:

* Connectors that have correctly configured connector servers show the following message:

  ```none
  RCS 1.5.20.29 started.
  Press q to shutdown.
  ```

* Connectors that have incorrectly configured connector servers show the following message and require troubleshooting:

  ```none
  RCS 1.5.20.29 started.
  Press q to shutdown.
  Jun 19, 2025 12:33:36 pm INFO  o.f.o.f.client.ConnectionManager: [myrcs1] Connector Server: Access Forbidden - closing connection
  Jun 19, 2025 12:33:36 pm INFO  o.f.o.f.c.ClientRemoteConnectorInfoManager: [myrcs1] Connection to server failed: 403 - Access Forbidden
  Jun 19, 2025 12:33:36 pm WARN  o.f.o.f.c.ClientRemoteConnectorInfoManager: [myrcs1] StaggeredConnectionCreator: Exception while connecting WebSocket: java.util.concurrent.ExecutionException: org.identityconnectors.framework.common.exceptions.InvalidCredentialException: 403 - Access Forbidden
  ```

## What documentation should I use?

Learn more in [Secure RCS access to Advanced Identity Cloud connector servers](../../idm-auth/authorization-and-roles.html#secure-openicf-access).

***

[1](#_footnoteref_1). A [user acceptance testing (UAT) environment](../../tenants/environments-uat.html) is an [add-on capability](../add-on-capabilities.html).[2](#_footnoteref_2). A [sandbox environment](../../tenants/environments-sandbox.html) is an [add-on capability](../add-on-capabilities.html).

---

---
title: Security and compliance
description: Security architecture and compliance certifications for Advanced Identity Cloud, including SOC 2 Type 2, ISO 27001, HIPAA, HITECH, and TISAX
component: pingoneaic
page_id: pingoneaic:product-information:security-compliance
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/security-compliance.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Getting started", "Compliance", "GDPR", "HIPAA"]
section_ids:
  certifications_and_compliance: Certifications and compliance
  soc_2_type_2: SOC 2 Type 2
  iso_27001_27017_and_27018: ISO 27001, 27017, and 27018
  iso_22301: ISO 22301
  csa_star_level_2: CSA STAR (Level 2)
  hipaa_and_hitech: HIPAA and HITECH
  trusted_information_security_assessments_exchange: Trusted Information Security Assessments Exchange
  security_white_paper: Security white paper
---

# Security and compliance

PingOne Advanced Identity Cloud provides full tenant isolation in a multi-tenant cloud service by using individual trust zones. Each customer's environment is a dedicated trust zone that shares no code, data, or identities with other customers' environments. This prevents any accidental or malicious commingling. All data is encrypted, at rest and in transmission, to prevent unauthorized access and data breaches.

## Certifications and compliance

### SOC 2 Type 2

![soc2 logo](_images/soc2-logo.jpeg)

Ping Identity is SOC 2 Type 2-certified. This confirms that Ping Identity's information security practices, policies, procedures, and operations meet the SOC 2 standards for security, availability, and confidentiality. Our adherence to these standards is externally validated by an independent third party annually.

Our SOC 2 report is available to customers with a signed NDA on the [Security Documentation](https://support.pingidentity.com/s/secure-docs) page of the Ping Identity Support Portal. You must be signed on to access the report.

### ISO 27001, 27017, and 27018

![iso logo](_images/iso-logo.png)

Ping Identity's information security management system (ISMS) has been independently assessed and [certified](https://www.schellman.com/certificate-directory) to the ISO 27001:2022 standard.

Ping Identity has included ISO 27017 and ISO 27018 into its certified ISMS and has also achieved independent certifications validating that the controls and implementation guidance relevant to those standards are in place and operational.

The scope of Ping Identity's ISMS covers all major offices used in the development of Ping Identity products, all of our product offerings, both standalone on-premises products and our cloud services (PingOne, PingOne Advanced Services, and PingOne Advanced Identity Cloud), as well as all supporting infrastructure, systems, and internal processes.

Our ISO 27001 certificate is available in the [Schellman Certificate Directory](https://www.schellman.com/certificate-directory) by searching for Ping Identity.

### ISO 22301

![iso 22301 logo](_images/iso-22301-logo.png)

Ping Identity's business continuity management system (BCMS) has been independently assessed and certified to the ISO 22301:2019 standard. This certification covers the BCMS supporting the reliability and resilience of the Ping Identity platform, including PingOne Advanced Identity Cloud and its accompanying autonomous products, PingOne, and PingOne Advanced Services.

The current ISO 22301 certificate, including scope and validity dates, is available to customers under NDA from the [Security Documentation](https://support.pingidentity.com/s/secure-docs) page of the Ping Identity Support Portal. You must be signed on to access the certificate.

Our ISO 22301 certificate is also available in the [Schellman Certificate Directory](https://www.schellman.com/certificate-directory) by searching for Ping Identity.

### CSA STAR (Level 2)

![csa logo](_images/csa-logo.png)

Ping Identity's cloud offerings are certified as meeting the criteria of the Cloud Security Alliance Cloud Controls Matrix (Version 4). Our CSA STAR (Level 2) Attestation demonstrates Ping Identity's commitment to high standards and industry-accepted cloud security controls and transparency of our security posture.

Our attestation and the CSA Consensus Assessments Initiative Questionnaire are available on the [CSA STAR (Level 2) Registry Page](https://cloudsecurityalliance.org/star/registry/ping-identity/services/pingone-pingone-advanced-services).

### HIPAA and HITECH

![hipaa logo](_images/hipaa-logo.png)

The Health Insurance Portability and Accountability Act (HIPAA) is the US national standard for health information security and privacy that governs the use and disclosure of sensitive protected health information (PHI).

Advanced Identity Cloud complies with HIPAA security standards, as well as the breach notification requirements of the Health Information Technology for Economic and Clinical Health (HITECH) Act. Learn more about [how Ping Identity supports HIPAA compliance](https://hub.pingidentity.com/datasheets/3836-hipaa-compliance).

### Trusted Information Security Assessments Exchange

![tisax logo](_images/tisax-logo.jpeg)

The Trusted Information Security Assessment Exchange (TISAX) is an assessment and exchange mechanism for the information security of enterprises governed by ENX on behalf of the German VDA. The exchange allows recognition of assessment results among the participants. TISAX can be accessed by active participants through <https://enx.com/tisax>. TISAX and TISAX results are not intended for general public use.

ForgeRock Inc. and ForgeRock Ltd. (Ping Identity) are active TISAX participants with assessment results available through the [ENX portal - Tisax assessment results](https://portal.enx.com/en-US/TISAX/tisaxassessmentresults/), under scope ID: SZZMC3 and assessment ID: AZ5YYL-1.

## Security white paper

Learn more about our security practices in our [security white paper](https://hub.pingidentity.com/white-papers/3806-pingone-advanced-identity-cloud-security-compliance).

---

---
title: Supported browsers
description: Browsers supported by Advanced Identity Cloud for administrative and end-user access, including Chrome, Firefox, Safari, and Microsoft Edge
component: pingoneaic
page_id: pingoneaic:product-information:supported-browsers
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/supported-browsers.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Getting started", "Browser"]
---

# Supported browsers

The following browsers are supported in PingOne Advanced Identity Cloud:

| Browser        | Version                                       |
| -------------- | --------------------------------------------- |
| Google Chrome  | Latest stable version of full-desktop browser |
| Firefox        | Latest stable version of full-desktop browser |
| Safari         | Latest stable version of full-desktop browser |
| Microsoft Edge | Latest stable version of full-desktop browser |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ping Identity does not provide support for these browsers:- Internet Explorer 11

- Microsoft Edge in Internet Explorer compatibility mode

- Embedded browsers within any application (for example, within Citrix environments or Office 365)Ping Identity optimizes its platform for modern browsers to ensure the best user experience, security, and performance. If you encounter issues while using the Ping Identity platform, ensure you use a supported, up-to-date browser for the optimal experience. |

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | While Advanced Identity Cloud works with all supported browsers, administrative activity works best using Google Chrome. |

---

---
title: Tenant administrator mandatory 2-step verification FAQ
description: FAQ on mandatory 2-step verification for Advanced Identity Cloud tenant administrators, covering how to prepare automation and request enforcement
component: pingoneaic
page_id: pingoneaic:product-information:migration-dependent-features/tenant-administrator-mandatory-2-step-verification-faq
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/migration-dependent-features/tenant-administrator-mandatory-2-step-verification-faq.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Tenants", "Authentication", "Troubleshooting", "Migration", "Administration"]
page_aliases: ["product-information:tenant-upgrade-dependent-features/tenant-administrator-mandatory-2-step-verification-faq.adoc"]
section_ids:
  how_is_2_step_verification_changing: How is 2-step verification changing?
  will_the_change_to_mandatory_2_step_verification_affect_me: Will the change to mandatory 2-step verification affect me?
  how_do_i_prepare_my_tenants_to_support_2_step_verification: How do I prepare my tenants to support 2-step verification?
  how_do_i_enable_mandatory_2_step_verification_for_my_tenants: How do I enable mandatory 2-step verification for my tenants?
---

# Tenant administrator mandatory 2-step verification FAQ

## How is 2-step verification changing?

Ping Identity is making 2-step verification mandatory for all PingOne Advanced Identity Cloud tenant administrators.

The option to skip registration for 2-step verification [is deprecated](../deprecation-notices.html#skip-option-2-step-verification) and will be removed a year after the deprecation notification date (**Friday, February 3, 2023**), following the Advanced Identity Cloud [deprecation and end of life policy](../release-lifecycle.html#deprecation-and-end-of-life).

![idcloudui tenant administrator set up 2 step verification skip deprecated](../_images/idcloudui-tenant-administrator-set-up-2-step-verification-skip-deprecated.png)

After the option to skip registration is removed, any tenant administrator that has not already set up 2-step verification will be forced to do so the next time they sign in. Advanced Identity Cloud guides the tenant administrator through the device registration process, with no assistance needed from Ping Identity support.

## Will the change to mandatory 2-step verification affect me?

Yes, this change affects all customers. You have until the deprecation end-of-life date (**Tuesday, April 2, 2024**) to update your tenants to make 2-step verification mandatory for all tenant administrators.

## How do I prepare my tenants to support 2-step verification?

If you have any automation that relies on the skip option to authenticate to Advanced Identity Cloud APIs, it must be updated to use a [service account](../../tenants/service-accounts.html) to get an access token.

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | After 2-step verification is enforced, any automation that depends on the skip option will fail authentication. |

## How do I enable mandatory 2-step verification for my tenants?

1. Make sure you have updated any automation that authenticates to Advanced Identity Cloud APIs to use a [service account](../../tenants/service-accounts.html). Learn more in [How do I prepare my tenants to support 2-step verification?](#how_do_i_prepare_my_tenants_to_support_2_step_verification).

2. Open a support case with Ping Identity support:

   1. Go to <https://support.pingidentity.com>.

   2. Click Create a case.

   3. Follow the steps in the case submission wizard by selecting your account and contract and answering questions about your tenant environments.

   4. On the Please answer the following questions to help us understand the issue you're facing page, enter the following details, and then click Next:

      | Field                                                | Value                                                                       |
      | ---------------------------------------------------- | --------------------------------------------------------------------------- |
      | What product family is experiencing the issue?       | Select PingOne Advanced Identity Cloud                                      |
      | What specific product is experiencing the issue?     | Select Configuration                                                        |
      | What version of the product are you using?           | Select NA                                                                   |
      | What Hostname(s) or Tenant ID(s) does this apply to? | Enter a comma-separated list of FQDNs for the relevant tenant environments. |

   5. On the Tell us about the issue page, enter the following details, and then click Next:

      | Field                                      | Value                                                         |
      | ------------------------------------------ | ------------------------------------------------------------- |
      | Provide a descriptive title for your issue | Enter `Enforce 2-step verification for tenant administrators` |
      | Describe the issue below                   | Enter `Enforce 2-step verification for tenant administrators` |

   6. Click Submit.

3. Ping Identity support turns on the enforcement of 2-step verification for your tenant administrators and then asks you to verify that everything is working as expected.
---
title: PingOne Multi-tenant SaaS
description: Licensing for the PingOne Multi-Tenant SaaS platform, including environment management, identity-based usage measures, and license limits.
component: licensing-guide
page_id: licensing-guide::multitenant-saas
canonical_url: https://docs.pingidentity.com/licensing-guide/multitenant-saas.html
llms_txt: https://docs.pingidentity.com/licensing-guide/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  identity-based-licensing: Identity-based licensing
  packaging: Packaging
  pingone-authorize: PingOne Authorize
  pingone-credentials: PingOne Credentials
  pingone-davinci: PingOne DaVinci
  pingone-directory: PingOne Directory
  pingone-mfa-pingid: PingOne MFA and PingID
  pingone-privilege: PingOne Privilege
  pingone-protect: PingOne Protect
  pingone-recognize: PingOne Recognize
  pingone-sso: PingOne SSO
  pingone-verify: PingOne Verify
  pingone-platform-agent-iam-core: PingOne Platform Agent IAM Core
  solutions-bundles: Solutions bundles
---

# PingOne Multi-tenant SaaS

PingOne is Ping Identity's **multi-tenant cloud platform**, where your environments run in a secure, shared infrastructure managed by Ping Identity. Information related to [solution bundles](#solutions-bundles) appears later on this page.

* By default, you receive one or more **environments**, such as sandbox and production, in a Ping Identity-hosted cloud.

* There is a platform **cap of 500 environments** per organization.

* Licenses and usage, such as identities, flows, and risk evaluations, are surfaced in the **PingOne admin console**.

![A diagram illustrating Ping Identity's product offerings from human to agentic with PingOne on the human end of the scale and highlighted](_images/p1multitenantsaas.png)

PingOne licenses are records managed in the **Licenses** page of the admin console. You can use the **Licenses** page to view the details of your PingOne license and usage. PingOne license details include:

* **Organization**

* **Admin License**

* **Active Licenses**

* **Future Licenses**

* **Expired Licenses**

You can find more information in [Viewing your licenses](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_view_licenses.html) and the [License FAQ](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_license_faq.html) in the PingOne documentation.

## Identity-based licensing

* All PingOne multi-tenant licensed identities, transactions, and resources in all environments count fully against your contracted limits.

* The following products use an **Annual Active User (AAU)** or **Monthly Active User (MAU)** identity-based unit of measure: PingOne Authorize, PingOne Credentials, PingOne DaVinci, PingOne Directory, PingOne MFA and PingID, PingOne Protect, PingOne Recognize, and PingOne SSO.

* An **Annual Active User (AAU)** is a **unique identity** that is **active at least once** during a **365-day period** starting at the license start date.

* Active means at least one qualifying identity operation during the year, such as:

  * Sign-on or authentication.

  * Token issuance, validation, or refresh.

  * Password set or password change.

  * Other identity operations explicitly covered in the Product Terms.

* Each identity is counted **once per contract year**, regardless of how many times it authenticates.

* A **Monthly Active User (MAU)** is a unique identity that is **active at least once** in a given **calendar month**.

* Active means the identity is processed at least once by the product during that month, such as sign-on, token issuance, token validation, or password change.

* Admins can typically see licensed quantities and current usage, environment associations for each license, and high-level usage trends over time.

* Each PingOne license includes a **soft limit** and a **hard limit** for the maximum number of stored identities.

* The **soft limit** is usually 12× the licensed MAU or AAU of the subscription.

* The **hard limit** is 10% above the soft limit, capped at 100M identities, whichever is lower.

* When usage approaches or reaches the soft limit:

  * At **90% of the soft limit**, the admin console displays a **90% of allowed users** warning.

  * At **100% of the soft limit**, another warning indicates the soft limit has been reached, but you can still add users.

  * When the hard limit is reached, PingOne blocks the creation of new users until the license is updated.

## Packaging

### PingOne Authorize

Central decision service for fine-grained, contextual authorization decisions on APIs and data, using identity and resource attributes.

* PingOne Authorize is licensed by identities, and a fair-use transaction allowance is defined for each identity tier. The fair-use transaction allowance corresponds to the total number of licensed identities specified in your PingOne subscription.

* For some authorization use cases (for example, when permissions are checked for every page access or operation), the volume of authorization events can be significantly higher than the volume of authentication events. The fair-use transaction allowance provides you and Ping Identity with a shared expectation about the volume of authorization traffic. If this limit isn't sufficient, contact Ping Identity Sales about increasing the monthly allowance.

| Feature                                                                                                                              | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| [Dynamic authorization policies](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_overview.html)     | Centralized, fine-grained authorization policies that leverage user, resource, and contextual attributes to allow, deny, or filter access. |
| [API and data protection](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_api_services.html)        | Protect APIs and data by externalizing authorization decisions from applications to a central decision service.                            |
| [Decision APIs](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_decision_endpoints.html)            | REST-based decision endpoints that applications and gateways can call at runtime for authorization decisions.                              |
| [Policy modeling and testing](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_policy_testing.html) | Tools to model, test, and troubleshoot authorization policies before rolling them into production.                                         |

### PingOne Credentials

Verifiable credentials platform to issue, manage, and verify digital identity credentials for users.

| Feature                                                                                                                                                               | Description                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [Credential templates](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_customizing_notification_templates.html)    | Design credential types, attributes, and display format used when issuing digital credentials. |
| [Issuance flows](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_getting_started.html)                             | Issue verifiable credentials to users using journeys, APIs, or administrator-driven actions.   |
| [Presentation and verification](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_scenario_present_verify_cred.html) | Verify credentials when users present them during access or onboarding flows.                  |
| [Revocation and lifecycle](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_revoking_a_credential.html)             | Revoke credentials when they are no longer valid and notify users where appropriate.           |

### PingOne DaVinci

No-code orchestration platform to design and run identity journeys (sign-up, sign-on, step-up, recovery, migrations) using a drag-and-drop flow canvas and connectors.

DaVinci can be sold in many ways: **identity-based** (AAU and MAU referenced above) and **transaction-based through flows**. Refer to the [Product Specific Terms and Conditions](https://www.pingidentity.com/en/legal/product-terms.html) for fair-use policies.

A **flow** is an **executed DaVinci flow run** triggered at the **start of a journey** that can internally call multiple APIs and services.

* Examples include:

  * Registration journey.

  * Passwordless login journey.

  * Password recovery journey.

  * Device registration journey.

  * Adaptive authentication journey.

* A flow invocation occurs each time a flow is initiated in DaVinci. If a flow launches one or more subflows, the subflows do not count as additional invocations. Only the initial invocation is counted.

* The flow-based license comes with a fair-use transaction limit of 80 connector executions per flow. If the limit is not sufficient, contact [Ping Identity Sales](https://www.pingidentity.com/en/company/contact-sales.html) about increasing volume limits as your usage increases. Learn more in [DaVinci Usage Terms](https://docs.pingidentity.com/davinci/usage_terms/davinci_best_practices_usage_terms.html).

| Feature                                                                                                                                     | Description                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Low or no-code flow orchestration](https://docs.pingidentity.com/davinci/davinci_introduction.html)                                        | Drag-and-drop flow canvas for building identity and access management (IAM) journeys (registration, authentication, recovery, step-up, migrations) using nodes and logical operators.                                         |
| [Connector library](https://docs.pingidentity.com/davinci/connectors/davinci_connections.html)                                              | Hundreds of pre-built connectors (Ping Identity services and third-party apps) used as nodes in flows for multi-factor authentication (MFA), fraud, identity verification (IDV), software as a service (SaaS) apps, and more. |
| [Flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)                                     | Ready-made DaVinci flow templates for common use cases (passwordless, social login, account recovery, and so on) that can be cloned and customized.                                                                           |
| [UI Studio and forms](https://docs.pingidentity.com/davinci/ui_studio/davinci_ui_studio.html)                                               | UI Studio and SK-components for building branded HTML forms and pages (sign-on, registration, MFA, agreements) directly into flows.                                                                                           |
| [Flow policies and A/B tests](https://docs.pingidentity.com/davinci/applications/davinci_flow_policies.html)                                | Flow policies to control which flows run for which apps or users and support A/B-style routing for testing and optimizing journeys.                                                                                           |
| [Analytics and debugging](https://docs.pingidentity.com/davinci/flows/davinci_viewing_flow_analytics.html)                                  | Built-in flow analytics, validation, and best-practices tooling to monitor performance, errors, and outcomes for journeys.                                                                                                    |
| [Embedding and integration](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_how_to_implement_a_flow.html) | Multiple ways to launch flows: redirect, widget, API calls, and Ping Identity SDKs for embedding journeys into web and mobile apps.                                                                                           |

### PingOne Directory

Cloud directory and user store for PingOne, managing users, groups, attributes, and basic sync and provisioning to external directories and apps.

| Feature                                                                                                                | Description                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [Cloud directory and user store](https://docs.pingidentity.com/pingone/directory/p1_directories_menu.html)             | Cloud-hosted directory to store and manage users, groups, and identity data for PingOne solutions.                             |
| [Users, groups, and populations](https://docs.pingidentity.com/pingone/directory/p1_aboutusers.html)                   | Manage users, groups, and populations to control access, policy targeting, and delegated administration.                       |
| [Custom attributes and schema](https://docs.pingidentity.com/pingone/directory/p1_user_attributes.html)                | Add and manage custom user attributes and control how attributes are exposed to applications.                                  |
| [Attribute access control](https://docs.pingidentity.com/pingone/directory/p1_attribute_access_control_user_atts.html) | Use attribute access control rules to restrict which attributes admins and apps can read or write.                             |
| [LDAP gateways and external directories](https://docs.pingidentity.com/pingone/integrations/p1_ldap_gateways.html)     | Use LDAP gateways to authenticate against or provision to external directories such as Active Directory (AD) or PingDirectory. |

### PingOne MFA and PingID

Strong, adaptive MFA and passwordless experiences across web and mobile, using methods like push, one-time passcode (OTP), and FIDO2 passkeys.

| Feature                                                                                                                                 | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| [Multi-factor methods](https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_configuring_strong_authentication_start.html) | Support for multiple MFA methods such as mobile app push, OTP, SMS and voice, email, and FIDO2 passkeys.  |
| [MFA policies](https://docs.pingidentity.com/pingone/authentication/p1_mfa_policies.html)                                               | Policies that define when and how MFA is required based on application, user, group, or other conditions. |
| [Passwordless experiences](https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_strong_authentication_integrations.html)  | Build passwordless sign-on journeys combining PingOne MFA, PingOne SSO, and DaVinci flows.                |
| [MFA dashboards and reporting](https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_using_mfa_dashboard.html)             | Dashboards that show MFA enrollments, authentications, and method usage across your environment.          |
| [PingID compatibility and migration](https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_integrate_pingid_with_p1.html)  | Integrate or migrate existing PingID tenants into PingOne while preserving MFA capabilities.              |

### PingOne Privilege

Just-in-time privileged access management for cloud resources (servers, databases, VMs, Kubernetes), with real-time monitoring and control.

PingOne Privilege uses **resources** as its unit of measure.

A **resource** is a **managed infrastructure target** such as:

* **Server**

* **Database**

* **Virtual machine (VM)**

* **Kubernetes cluster**

To count as a resource for licensing purposes, the component must be **registered** with the product and be assigned a **unique identifier** in the product.

| Feature                                                                                                                                            | Description                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| [Just-in-time privileged access](https://docs.pingidentity.com/privilege/getting-started/key-concepts.html)                                        | Grant time-bound elevated access to servers, databases, VMs, and Kubernetes clusters based on policy and approvals. |
| [Cloud infrastructure onboarding](https://docs.pingidentity.com/privilege/configuration/cloud-accounts.html)                                       | Onboard cloud infrastructure to enable privileged access management for resources.                                  |
| [Policy-based access management](https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/access-management/policies.html) | Define who can access which resources, with what roles, and under what conditions, using centralized policies.      |
| [Session visibility](https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/activity/activity-logs.html)                 | Monitor and audit privileged sessions to understand who accessed what and when.                                     |

### PingOne Protect

Risk evaluation and threat protection that scores sign-on and other events using signals and predictors, driving adaptive policies.

PingOne Protect can be sold in many ways: **identity-based** (AAU and MAU referenced above) and **transaction-based through risk evaluations**.

A **risk evaluation** is a **risk assessment event** triggered by a business operation.

* Common examples include:

  * User sign-on.

  * Registration or account creation.

  * Password recovery or high-risk account change.

  * Any other call to the risk engine for a risk score.

* Each qualifying call to the risk service typically counts as **one risk evaluation**.

* PingOne Protect is licensed with a **fair-use allowance of risk evaluations per identity per year**. The allowance depends on the identity type and usage tier. Reference [Product terms and conditions](https://www.pingidentity.com/en/legal/product-terms.html) for information about these fair-use limits.

| Feature                                                                                                                                | Description                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [Risk policies](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html)           | Define policies that evaluate risk at key events, such as sign-on or registration, and return risk levels and actions. |
| [Predictors](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_predictors.html)            | Signals such as device, IP reputation, behavior, and velocity that feed into risk models.                              |
| [Risk evaluations](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_evaluations.html)     | Per-event risk assessments used to drive adaptive responses such as allow, deny, or step-up authentication.            |
| [Threat Protection Dashboard](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_dashboard.html) | Dashboard visualizing risk events, high-risk users, risky IPs, and model effectiveness over time.                      |

### PingOne Recognize

Zero-knowledge biometric authentication that uses privacy-preserving facial recognition with liveness and anti-injection detection.

| Feature                                                                                                                                                                                | Description                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| [Zero-knowledge biometric authentication](https://docs.pingidentity.com/recognize/pingone-recognize.html)                                                                              | Privacy-preserving facial biometric authentication that verifies the user in less than a second without storing reconstructable biometric data. |
| [Liveness and anti-injection detection](https://docs.pingidentity.com/recognize/introduction/authentication.html)                                                                      | Detects presentation and injection attacks (for example, deepfakes, replays) using certified liveness and anti-injection checks.                |
| [Device and face binding](https://docs.pingidentity.com/recognize/idv-bridge/idv-bridge-introduction.html)                                                                             | Binds the user's face to their account and device so each authentication checks both the enrolled face and context.                             |
| [Web](https://docs.pingidentity.com/recognize/web-sdk/web-sdk-getting-started.html) and [mobile SDKs](https://docs.pingidentity.com/recognize/mobile-sdk/mobile-sdk-introduction.html) | SDKs for iOS, Android, and web to embed PingOne Recognize into existing applications and journeys.                                              |

### PingOne SSO

Standards-based single sign-on (OIDC, OAuth 2.0, and SAML) and app portal for secure, one-click access to SaaS and custom applications.

| Feature                                                                                                                            | Description                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [Single sign-on for apps](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_p1sso_start.html)                  | Standards-based SSO (SAML, OIDC, OAuth 2.0) for SaaS and custom apps using PingOne as the identity provider. |
| [Application catalog and templates](https://docs.pingidentity.com/pingone/applications/p1_application_types.html)                  | Pre-built application templates and catalog integrations to speed onboarding of common SaaS applications.    |
| [Authentication policies](https://docs.pingidentity.com/pingone/authentication/p1_authenticationpolicies.html)                     | Configurable sign-on policies that define how users authenticate to different applications and resources.    |
| [Application portal](https://docs.pingidentity.com/pingone/applications/p1_application_portal_showing_applications.html)           | User-facing portal that lists assigned applications and optional resource links for quick access.            |
| [API access control](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1_az_api_access_management.html) | Use OAuth 2.0 resources and scopes to protect APIs and issue access tokens for API clients.                  |

### PingOne Verify

Identity verification service for document plus selfie checks, liveness, and verification workflows during onboarding or high-risk events.

**Identity-based** (AAU and MAU referenced above) and **transaction-based unit of measure through Verifications**. **Verifications** count **identity verification checks**, such as:

* Document plus selfie verification.

* Liveness checks.

* ID document lookups (for example, driver license, passport).

* Utility bill or credit report checks (where applicable).

Each verification transaction (or bundled verification process, depending on configuration) counts toward the verification allowance.

| Feature                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Universal Capture](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_types_of_verification.html)                                | Allows for one verification data capture with quality assurance, one email possession verification, one mobile phone possession verification, and one basic biographic matching.                                                                                                                      |
| [Automated ID Inspection](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_documentation_authentication.html)                   | Automated inspection of one sample image file set (image signal) captured from a supported government-issued ID with authenticity checks. Automated ID Inspection does not include live selfie-to-photo matching, issuer or commercial authoritative system-of-record check, or manual ID inspection. |
| [Face Verification](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_face_verification.html)                                    | Match one live selfie against a reference photo for the purposes of identity verification.                                                                                                                                                                                                            |
| [Manual ID Inspection](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_manually_approve_id.html)                               | Manual inspection of one sample image file set (image signal) captured from a supported government-issued ID. Does not require Automated Inspection to occur in advance.                                                                                                                              |
| [Manual ID Inspection Step Up](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_documentation_authentication.html)              | Manual inspection of one sample image file set (image signal) captured from a supported government-issued ID after Automated ID Inspection if required. Service requires purchase of Automated Document Inspection.                                                                                   |
| [Government ID System of Record Check](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_aamva_dldv.html)                        | Compare data extracted from one supported government ID against the issuer's, or an authoritative commercial, system of record upon completion of an automated document inspection. Service requires purchase of Automated Document Inspection. Not eligible for any uptime availability commitment.  |
| [Data-Based Identity Verification (Group I - V)](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_data_based_verification.html) | Connects to over 300 government, credit, consumer, and utility data sources worldwide to verify identity attributes.                                                                                                                                                                                  |

### PingOne Platform Agent IAM Core

PingOne Platform Agent IAM Core treats autonomous artificial intelligence (AI) agents as first-class, governed identities in PingOne, so they authenticate, get scoped tokens, and access APIs, data, and tools under the same least-privilege policies and audit controls as human users and applications.

It's licensed based on the number of human identities (customer, workforce, or partner) that your AI agents act on behalf of, rather than by agent or transaction volume.

| Feature                                                                                                                               | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| [Identity for AI foundation](https://developer.pingidentity.com/identity-for-ai/getting-started/idai-what-is-identity-for-ai.html)    | Integrates AI agents into your IAM so they authenticate, authorize, and audit like users and apps.                 |
| [AI agent architecture](https://developer.pingidentity.com/identity-for-ai/agents/idai-what-are-agents.html)                          | Defines agents as autonomous systems that use LLMs, tools, memory, and workflows to complete tasks.                |
| [Agent types and trust model](https://developer.pingidentity.com/identity-for-ai/identity/idai-agent-types.html)                      | Classifies agents (personal, assistants, digital workers) and distinguishes managed vs unmanaged based on control. |
| [Tools and external actions](https://developer.pingidentity.com/identity-for-ai/agents/idai-tools-intro.html)                         | Treats tools as external APIs/functions agents call to access data or perform actions under IAM control.           |
| [MCP and A2A collaboration](https://developer.pingidentity.com/identity-for-ai/agents/idai-tools-intro.html#idai-mcp-and-a2a)         | Uses MCP for secure agent-tool calls and A2A for agent-agent coordination in multi-agent workflows.                |
| [IAM best practices for agents](https://developer.pingidentity.com/identity-for-ai/getting-started/idai-what-is-identity-for-ai.html) | Applies IAM principles like delegation (not impersonation), least privilege, and monitoring to agents.             |
| [PingOne AI Agents integration](https://docs.pingidentity.com/pingone/ai_agents/p1_ai_agents.html)                                    | Implements these Identity for AI patterns in PingOne so AI agents get scoped tokens and policy-governed access.    |

## Solutions bundles

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find more information about the solutions bundles in [Ping Identity Platform Pricing](https://www.pingidentity.com/en/platform/pricing.html). |

![A diagram illustrating Ping Identity's product suite](_images/p1productbundles.png)

**Customer**

| Bundle             | Includes                                                                                              |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| **P14C Essential** | PingOne SSO; PingOne Directory; DaVinci (with flow limits); PingDataSync                              |
| **P14C Plus**      | PingOne SSO; PingOne Directory; **DaVinci**; **PingOne MFA**; PingDataSync; **API Access Management** |

**Workforce**

| Bundle             | Includes                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------ |
| **P14W Essential** | PingOne SSO; PingOne Directory; DaVinci (with flow limits); basic PingID MFA; PingDataSync |
| **P14W Plus**      | PingOne SSO; PingOne Directory; **DaVinci**; **full PingID MFA**; PingDataSync             |

**B2B**

| Bundle               | Includes                                                                                              |
| -------------------- | ----------------------------------------------------------------------------------------------------- |
| **P14B2B Essential** | PingOne SSO; PingOne Directory; DaVinci (with flow limits); PingDataSync                              |
| **P14B2B Plus**      | PingOne SSO; PingOne Directory; **DaVinci**; **PingOne MFA**; PingDataSync; **API Access Management** |

|   |                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Refer to the fair-use policy in [Product terms and conditions](https://www.pingidentity.com/en/legal/product-terms.html) for Plus bundles. |

**PingOne for Customers Passwordless**

| Bundle           | Includes                                                              |
| ---------------- | --------------------------------------------------------------------- |
| **Passwordless** | PingOne Protect; PingOne SSO; PingOne Directory; PingOne MFA; DaVinci |

PingOne for Customers Passwordless is a solution bundle licensed by transactions based on flow invocations. Learn more in the [PingOne DaVinci](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_licenses_and_identities.html#section_ank_jbn_5bc) section.

It includes PingOne Protect, PingOne SSO including Directory, and PingOne MFA in PingOne DaVinci. This solution bundle requires use of each product only through DaVinci flows.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can review your current licenses and entitlements in the Ping Identity Support Portal. After signing on, go to the **Licensing** section. From this page, you can also access your support keys and open a support case if anything about your entitlements appears incorrect.You can find more information in Ping Identity's legal [Product terms and conditions](https://www.pingidentity.com/en/legal/product-terms.html). |
---
title: PingOne Advanced Identity Cloud
description: Licensing information for PingOne Advanced Identity Cloud, a dedicated-tenant SaaS platform, covering CIAM packaging options, annual active user measures, and add-ons.
component: licensing-guide
page_id: licensing-guide::pingone-advanced-identity-cloud
canonical_url: https://docs.pingidentity.com/licensing-guide/pingone-advanced-identity-cloud.html
llms_txt: https://docs.pingidentity.com/licensing-guide/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  packaging: Packaging
  ciam: CIAM
  pingone-advanced-identity-cloud-core: PingOne Advanced Identity Cloud Core
  access-plus: Access Plus
  edge: Edge
  personalization: Personalization
  organizations: Organizations
  sync: Sync
  advanced-reporting: Advanced Reporting
  agentiam: Agent IAM Core
  workforce-and-b2b: Workforce and B2B
  workforce-core: Workforce Core
  advanced-reporting-for-access-and-governance: Advanced Reporting (for Access and Governance)
  access-management: Access Management
  edge-2: Edge
  enterprise-connect: Enterprise Connect
  enterprise-connect-passwordless: Enterprise Connect Passwordless
  lifecycle-automation: Lifecycle Automation
  identity-workflow: Identity Workflow
  access-request: Access Request
  access-review: Access Review (Access Certifications)
  segregation-of-duties: Segregation of Duties (SoD)
  role-modeling: Role Modeling
  agentiam2: Agent IAM Core
  pingone-advanced-identity-cloud-infrastructure-add-ons: PingOne Advanced Identity Cloud Infrastructure Add-Ons
---

# PingOne Advanced Identity Cloud

PingOne Advanced Identity Cloud and PingOne Advanced Services are **single-tenant software as a service (SaaS)** offerings.

* By default, you receive a dedicated tenant with three environments (Dev, Staging, and Prod) operated by Ping Identity.

* Usage is surfaced in **PingOne Advanced Identity Cloud-specific dashboards and documentation**.

* All single-tenant SaaS licensed identities and transactions in production count fully against your contracted limits.

* There are no hard limits in the system that automatically shut off PingOne Advanced Identity Cloud capabilities.

* In development and sandbox environments, infrastructure limits usage to 10,000 objects.

![A diagram illustrating Ping Identity's product offerings from human to agentic with PingOne Advanced Identity Cloud in the middle of the scale and highlighted](_images/p1advancedidentitycloud.png)

## Packaging

### CIAM

PingOne Advanced Identity Cloud is a comprehensive, hosted identity platform that provides identity, access, directory, governance, and edge security capabilities as a managed SaaS service. It is packaged into a Core subscription with optional add-on feature packages to match different customer identity and access management (CIAM) requirements (Access Plus, Personalization, Organizations, Edge, Sync).

The following PingOne Advanced Identity Cloud CIAM offerings are licensed with an **Annual Active User (AAU)** unit of measure.

An **Annual Active User (AAU)** is a **unique identity** that is **active at least once** during a **365-day period** starting at the license start date.

* Active means at least one qualifying identity operation during the year, such as:

  * Sign-on or authentication

  * Token issuance, validation, and refresh

  * Password set or password change

  * Other identity operations explicitly covered in the Product Terms

* Each identity is counted **once per contract year**, regardless of how many times it authenticates.

#### PingOne Advanced Identity Cloud Core

Foundational identity, access, single sign-on (SSO), multi-factor authentication (MFA), and directory capabilities for CIAM use cases.

| Feature                                                                                                                  | Description                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Authentication journeys and nodes](https://docs.pingidentity.com/pingoneaic/journeys/journeys.html)                     | Visual, node-based authentication journeys that let you combine many authentication, risk, and UX building blocks into a single flow with multiple decision points and paths.                                     |
| [Session and SSO capabilities](https://docs.pingidentity.com/pingoneaic/am-authentication/about-sso.html)                | Central session management and single sign-on across apps using journeys and standards-based protocols, including browser and API, OpenID Connect (OIDC), and OAuth use cases.                                    |
| [Multi-factor and strong authentication](https://docs.pingidentity.com/pingoneaic/am-authentication/authn-mfa.html)      | MFA and passwordless options (one-time passcode (OTP), push, device binding, WebAuthn and FIDO2, biometrics) used in journeys for step-up or primary authentication.                                              |
| [Federation (SAML, OIDC, OAuth 2.0)](https://docs.pingidentity.com/pingoneaic/app-management/applications.html)          | Identity provider and service provider capabilities for SAML 2.0 SSO and single logout (SLO), OpenID Connect 1.0, and OAuth 2.0 authorization server to federate with SaaS apps and enterprise IdPs.              |
| [Web and Java agents for SSO](https://docs.pingidentity.com/pingoneaic/realms/gateways-agents.html)                      | Policy agents for web and Java apps that intercept requests, enforce policies, and redirect to Advanced Identity Cloud for authentication and SSO.                                                                |
| [User login analytics](https://docs.pingidentity.com/pingoneaic/tenants/analytics-dashboard.html)                        | Counters, timers, and dashboard views to monitor journey usage, success/failure, and performance, including top journeys by outcome and usage.                                                                    |
| [Identity lifecycle management](https://docs.pingidentity.com/pingoneaic/identities/roles-assignments.html)              | Managed objects, roles, entitlements, and assignments used to model identities and provision access based on role and assignment structures.                                                                      |
| [Identity self-service](https://docs.pingidentity.com/pingoneaic/self-service/overview.html)                             | End-user journeys for self-registration, password reset, username recovery, progressive profiling, and terms and conditions acceptance.                                                                           |
| [Social identity integration](https://docs.pingidentity.com/pingoneaic/self-service/social-registration.html)            | Social login and registration with account linking so users can sign on or register using social identity providers and have accounts linked in PingOne Advanced Identity Cloud.                                  |
| [Directory services (LDAP, REST, DSML)](https://docs.pingidentity.com/platform/8/platform-guide/directory-services.html) | LDAPv3 directory with REST and DSML access, multi-master replication, user-object store, and password and data security controls for high-availability identity storage and use as a backing store for the cloud. |
| [Basic reporting](https://docs.pingidentity.com/pingoneaic/reports/administration/about-reports.html)                    | Built-in analytics and reporting included with the service at no additional charge. Includes out-of-the-box standard reports with data refreshed every 1 - 2 hours and 30 days of report data retention.          |

#### Access Plus

Adds fine-grained and transactional authorization, continuous access policies, and dynamic scopes.

| Feature                                                                                                                   | Description                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Fine-grained authorization](https://docs.pingidentity.com/pingoneaic/am-authorization/what-is-authz-decision.html)       | Centralized, web-based authorization policies that use identity attributes and contextual signals (device, request, risk, and so on) to make fine-grained allow/deny/filter decisions without changing app code. |
| [Transactional authorization](https://docs.pingidentity.com/pingoneaic/am-authorization/transactional-authorization.html) | One-time, per-transaction authorization that requires the user to complete a designated journey (such as MFA/step-up) before a sensitive action or API call is allowed.                                          |
| Continuous authorization                                                                                                  | Continuous, context-aware authorization that evaluates behavior and environment signals over time (risk, device, network, transaction context) to adjust access and enforce real-time policies.                  |
| [Application MFA](https://docs.pingidentity.com/pingoneaic/am-sessions/session-upgrade.html)                              | Application-level step-up/upgrade of an existing session with MFA when users attempt higher-risk actions, typically implemented using journeys that upgrade the session with additional factors.                 |
| [WebAuthn Passwordless](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)                    | Passwordless FIDO2/WebAuthn authentication using platform authenticators or security keys (often passkeys) as a strong factor in journeys, supporting usernameless and MFA use cases.                            |

#### Edge

Adds gateway and edge security to extend PingOne Advanced Identity Cloud to legacy apps and APIs in on-premise and cloud environments.

| Feature                                                                                                                | Description                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Identity gateway](https://docs.pingidentity.com/platform/8/platform-guide/edge-security.html#identity-gateway-module) | Identity-aware reverse proxy based on PingGateway that secures web apps, APIs, Internet of Things (IoT), and microservices with centralized authentication and authorization, token transformation, and policy enforcement. |
| [Microservices](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/microgateway-protect-service.html)     | PingGateway deployed as a microgateway to front individual services, applying OAuth 2.0 security, throttling, and policy enforcement close to each microservice.                                                            |

#### Personalization

Adds consent, preference, profile and relationship management, and privacy and self-service controls.

| Feature                                  | Description                                                                                                                                      |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Profile and Privacy Management Dashboard | Central end-user view where customers can see, review, and manage the personal data held about them (profile details, history, and so on).       |
| Consent and preference management        | Capture, store, and enforce customer consent and communication preferences across apps and journeys in a consistent, auditable way.              |
| Custom relationships                     | Model and manage rich relationships (for example, households, accounts, dependents) between identities to drive tailored access and experiences. |

#### Organizations

Adds hierarchical organization modeling and delegated administration for complex business-to-business (B2B) and business-to-business-to-consumer (B2B2C) structures.

| Feature                  | Description                                                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| Organizations            | Model customer organizations and hierarchies (tenants, partners, business units) so users, apps, and policies can be scoped by org. |
| Multi-brand capabilities | Support multiple brands or lines of business in a single deployment (different domains, logos, journeys, and policies per brand).   |
| Customer Delegated Admin | Let customer org admins manage their own users, groups, and access within their org—without giving them full tenant admin rights.   |

#### Sync

Adds synchronization and provisioning capabilities across Advanced Identity Cloud and external systems.

| Feature                                                                                                                         | Description                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Synchronization module](https://docs.pingidentity.com/pingoneaic/idm-synchronization/sync-overview.html)                       | Core synchronization engine that keeps identity data aligned across Advanced Identity Cloud and external systems, supporting unidirectional and bidirectional sync and provisioning flows. |
| [Password synchronization plugin](https://docs.pingidentity.com/pingidm/8/pwd-plugin-guide/)                                    | Near real-time password synchronization so password changes in a source directory are propagated to other connected systems without users needing to reset manually.                       |
| [PingDS and Active Directory (AD) Plugins](https://docs.pingidentity.com/pingidm/8/pwd-plugin-guide/chap-sync-dj.html)          | Native password sync plugins for DS and Microsoft Active Directory that capture password changes and feed them into the sync engine securely.                                              |
| [Reconciliation](https://docs.pingidentity.com/pingoneaic/idm-synchronization/sync-overview.html)                               | Alignment between accounts across datastores by comparing source and target, detecting differences, and applying configured actions to resolve conflicts.                                  |
| [Outbound provisioning](https://docs.pingidentity.com/pingoneaic/identities/sync-identities.html)                               | Creation, update, and deletion of accounts and entitlements in external applications when identities change in Advanced Identity Cloud (and vice versa, where configured).                 |
| [Connectors](https://docs.pingidentity.com/pingoneaic/identities/sync-identities.html#about-advanced-identity-cloud-connectors) | Library of built-in and remote connectors (LDAP, AD, database, SaaS apps, and so on) that read and write identity data between Advanced Identity Cloud and external systems.               |
| [Pass-through authentication and JIT migration](https://docs.pingidentity.com/pingoneaic/identities/sync-identities.html)       | Pass-through authentication against external directories or datastores so users can authenticate with existing credentials while being migrated just-in-time into Advanced Identity Cloud. |

#### Advanced Reporting

Paid reporting tier that includes all out-of-the-box reports.

| Feature                                                                                | Description                                                                                                                                           |
| -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Paid Tier](https://docs.pingidentity.com/pingoneaic/tenants/analytics-dashboard.html) | Includes all out-of-the-box reports plus the ability to create custom reports, with near real-time data latency and 90 days of report data retention. |

#### Agent IAM Core

Treats autonomous artificial intelligence (AI) agents as first-class, governed identities in PingOne, so they authenticate, get scoped tokens, and access APIs, data, and tools under the same least-privilege policies and audit controls as human users and applications.

| Feature                                                                                                                                                             | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| [Governed AI agent identities](https://developer.pingidentity.com/identity-for-ai/getting-started/idai-what-is-identity-for-ai.html)                                | Treats AI agents as governed identities that authenticate, authorize, and audit like users and apps.                                       |
| [Agent models and trust boundaries](https://developer.pingidentity.com/identity-for-ai/identity/idai-agent-types.html)                                              | Defines agent types (personal, assistants, digital workers) and managed vs unmanaged based on control and trust.                           |
| [Delegated, least-privilege access](https://developer.pingidentity.com/identity-for-ai/getting-started/idai-what-is-identity-for-ai.html)                           | Applies delegation (not impersonation), scoped access, least privilege, and monitoring to AI agents.                                       |
| [Agent architecture and lifecycle](https://developer.pingidentity.com/identity-for-ai/agents/idai-what-are-agents.html)                                             | Models agents as large language model (LLM)-driven systems that use tools, memory, and workflows in an iterative loop to do tasks.         |
| [Secure tool and API access](https://developer.pingidentity.com/identity-for-ai/agents/idai-tools-intro.html)                                                       | Treats tools and APIs as governed resources that agents call using structured commands under identity and access management (IAM) control. |
| [MCP and Agent2Agent (A2A) integration](https://developer.pingidentity.com/identity-for-ai/agents/idai-tools-intro.html#idai-mcp-and-a2a)                           | Uses MCP for secure agent-to-tool calls and A2A for agent-to-agent collaboration in multi-agent flows.                                     |
| [Central IAM benefits for PingOne Advanced Identity Cloud AI](https://developer.pingidentity.com/identity-for-ai/getting-started/idai-what-is-identity-for-ai.html) | Brings IAM benefits—secure access, governance, auditability, and risk controls—into AI agent use cases.                                    |

### Workforce and B2B

The following PingOne Advanced Identity Cloud Workforce + B2B offerings use a Managed (Stored) Identity unit of measure.

|   |                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------- |
|   | A Managed (Stored) Identity means a unique identifier for a device or user that is managed by the products, regardless of activity. |

#### Workforce Core

Foundational IAM platform for Workforce and B2B.

| Feature                                                                                                                                                      | Description                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SSO, SAML, OAuth, OIDC, and OTP](https://docs.pingidentity.com/pingoneaic/am-saml2/saml2-sso-slo.html)                                                      | Standards-based SSO and federation using SAML 2.0, OAuth 2.0, and OIDC, plus OTP-based authentication within Advanced Identity Cloud journeys.                                                           |
| Trust Network                                                                                                                                                | Use external IdPs and social providers as authentication sources, brokering trust between multiple identity providers and service providers.                                                             |
| [SSO agents](https://docs.pingidentity.com/pingoneaic/am-authentication/about-sso.html)                                                                      | Web and Java policy agents that sit in front of applications to enforce authentication, SSO, and policy decisions from the central access management service.                                            |
| [Token exchange](https://docs.pingidentity.com/pingoneaic/am-oauth2/token-exchange.html)                                                                     | OAuth 2.0 token exchange and delegation patterns that let services trade one token for another or impersonate users securely.                                                                            |
| [Directory services (user stores)](https://docs.pingidentity.com/pingoneaic/app-management/applications/directory-services.html)                             | Directory and identity store for workforce and B2B users, backing authentication, authorization, and profile management in Advanced Identity Cloud.                                                      |
| [Users and roles](https://docs.pingidentity.com/pingoneaic/identities/roles-assignments.html)                                                                | Core user and role model to represent employees, contractors, and B2B users and assign access using roles and entitlements.                                                                              |
| [Inbound reconciliation](https://docs.pingidentity.com/pingoneaic/identities/sync-identities.html)                                                           | Reconciles and normalizes identity data coming from upstream sources (HR, AD, other systems) into PingOne Advanced Identity Cloud's identity model.                                                      |
| [User self-service (registration, password reset, and account recovery)](https://docs.pingidentity.com/pingoneaic/use-cases/preface-pages/self-service.html) | Self-service journeys that let users register, reset passwords, and recover accounts without help desk intervention.                                                                                     |
| [Password authentication](https://docs.pingidentity.com/pingoneaic/realms/password-policy.html)                                                              | Username and password-based authentication integrated into Intelligent Access journeys for workforce and B2B users.                                                                                      |
| [Knowledge-based authentication (KBA)](https://docs.pingidentity.com/pingoneaic/self-service/progressive-profile.html)                                       | Knowledge-based challenge and response (security questions) used as an additional or fallback authentication factor where required.                                                                      |
| [Federation](https://docs.pingidentity.com/pingoneaic/am-saml2/saml2-sso-slo.html)                                                                           | Standards-based federation (SAML, OAuth 2.0, OIDC) for SSO between PingOne Advanced Identity Cloud and SaaS and enterprise applications.                                                                 |
| [Delegated Admin](https://docs.pingidentity.com/pingoneaic/idm-auth/delegated-admin.html)                                                                    | Delegated administration model so local admins (for example, line-of-business or B2B org admins) can manage their own users and access within defined scopes.                                            |
| Business org model                                                                                                                                           | Business organization structures (units, departments, partners) used to scope administration, policies, and reporting for workforce and B2B use cases.                                                   |
| [Social ID (registration)](https://docs.pingidentity.com/pingoneaic/self-service/social-registration.html)                                                   | Social identity registration and login so workforce and B2B users can sign on using external IdPs (for example, social or partner IdPs) where appropriate.                                               |
| [Basic reporting](https://docs.pingidentity.com/pingoneaic/reports/administration/about-reports.html)                                                        | Built-in analytics and reporting included with the service at no additional charge. Includes out-of-the-box standard reports with data refreshed every 1 - 2 hours and 30 days of report data retention. |

#### Advanced Reporting (for Access and Governance)

Paid reporting and analytics tier that adds near real-time latency and custom report creation on top of standard out-of-the-box reports and identity governance and administration (IGA) reports (access request, review, segregation of duties (SoD), and role modeling), with longer data retention (up to 90 days) for access and governance insights.

| Feature                                                                                            | Description                                                                                                                                           |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Paid Tier](https://docs.pingidentity.com/pingoneaic/reports/administration/advanced-reports.html) | Includes all out-of-the-box reports plus the ability to create custom reports, with near real-time data latency and 90 days of report data retention. |

#### Access Management

Central authentication and authorization module providing WS-Fed and WS-Trust, all MFA including passwordless and FIDO, context nodes (risk and context except Protect), and both coarse-grained and fine-grained authorization for workforce access.

| Feature                                                                                                                            | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [WS-Fed and WS-Trust](https://docs.pingidentity.com/pingoneaic/app-management/register-a-custom-application.html#sso-custom-wsfed) | Support for WS-Federation and WS-Trust protocols so PingOne Advanced Identity Cloud and PingAM can federate with legacy Microsoft and other WS-\*-based applications and services. |
| [All MFA including passwordless and FIDO](https://docs.pingidentity.com/pingoneaic/am-authentication/authn-mfa.html)               | Full MFA capabilities for workforce (OTP, push, device, WebAuthn/FIDO2/passkeys) and passwordless sign-on using journeys and strong authenticators.                                |
| [Context nodes (except PingOne Protect)](https://docs.pingidentity.com/pingoneaic/journeys/auth-nodes.html#contextual-authn-nodes) | Journey nodes that bring contextual signals (device, network, time, behavior, and so on) into authentication trees to drive adaptive, risk-aware decisions.                        |
| [Coarse and fine-grained authorization](https://docs.pingidentity.com/pingoneaic/am-authorization/preface.html)                    | Coarse-grained app access decisions and fine-grained, attribute-based authorization policies evaluated at runtime for APIs, pages, and actions.                                    |

#### Edge

Identity gateway and microservices layer that sits in front of apps and APIs to enforce access policies at the edge for Workforce and B2B identities.

| Feature                                                                                                                | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Identity Gateway](https://docs.pingidentity.com/platform/8/platform-guide/edge-security.html#identity-gateway-module) | Identity-aware reverse proxy based on PingGateway that secures web apps, APIs, IoT, and backend services with centralized authentication and authorization and policy enforcement. |
| [Microservices](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/microgateway-protect-service.html)     | Deploy PingGateway as a microgateway in front of individual microservices to apply OAuth 2.0 security, throttling, and policy enforcement close to each service.                   |

#### Enterprise Connect

Add-on capability for PingOne Advanced Identity Cloud and AM that brings rich MFA and stronger authentication to workstations, servers, VPNs, and other non-web resources.

| Feature                                                                                                                                               | Description                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Plug-n-Play Desktop](https://docs.pingidentity.com/enterprise-connect/latest/overview-ec.html)                                                       | Desktop integration that gives users a plug-and-play experience for workstation login and desktop SSO, layering MFA and passwordless over existing Windows and Mac logins. |
| [MFA for third-party authentication](https://docs.pingidentity.com/enterprise-connect/latest/windows-radius-proxy-3.0.2/configure-ssh-linux-pam.html) | Use Enterprise Connect (for example, the Windows RADIUS proxy) to add MFA in front of third-party systems such as VPNs, SSH, and other RADIUS-based services.              |

#### Enterprise Connect Passwordless

Add-on capability for PingOne Advanced Identity Cloud and AM that brings passwordless authentication to enterprise resources like workstations, servers, VPNs, and legacy apps.

| Feature                                                                                                          | Description                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [End-to-end Passwordless](https://docs.pingidentity.com/enterprise-connect/latest/overview-ec-passwordless.html) | Delivers an end-to-end passwordless experience by removing user interaction with passwords and handling any required password operations securely in the background.                                        |
| [Workforce authentication](https://docs.pingidentity.com/enterprise-connect/latest/index.html)                   | Focused on workforce authentication, enabling passwordless and MFA sign-on for Windows and Mac workstations, servers, VPNs, and other infrastructure integrated with PingOne Advanced Identity Cloud or AM. |

#### Lifecycle Automation

Identity lifecycle provisioning and management for Workforce and B2B.

| Feature                                                                                                                        | Description                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Provisioning and deprovisioning](https://docs.pingidentity.com/pingoneaic/identities/sync-identities.html)                    | Automate account creation, updates, and removal across target systems as users join, move, or leave, keeping access aligned with HR and identity changes.                              |
| [Outbound synchronization](https://docs.pingidentity.com/pingoneaic/idm-synchronization/sync-overview.html)                    | Continuously push identity and entitlement changes from PingOne Advanced Identity Cloud into external apps and directories using configured mappings and policies.                     |
| [Password synchronization plugin](https://docs.pingidentity.com/pingidm/8/pwd-plugin-guide/)                                   | Capture password changes in a source directory and securely synchronize them in near real time to other connected systems so users keep one password.                                  |
| [DS and AD plugins](https://docs.pingidentity.com/pingidm/8/pwd-plugin-guide/chap-sync-dj.html)                                | Native password-sync and identity plugins for DS and Microsoft Active Directory that feed changes into the lifecycle/sync engine.                                                      |
| [Pass-through authentication and JIT Migration](https://docs.pingidentity.com/pingoneaic/identities/sync-identities.html)      | Let users authenticate against existing directories or datastores while silently creating or updating their account in PingOne Advanced Identity Cloud "just-in-time" as they sign on. |
| [Personalization (privacy and consent)](https://docs.pingidentity.com/pingoneaic/app-management/provision-an-application.html) | Capture, store, and enforce user consent and communication preferences as part of lifecycle flows, and expose a privacy dashboard for users to manage their data.                      |

#### Identity Workflow

Workflow engine for IGA: workflow authoring, monitoring of workflow instances, and operational reporting, used to orchestrate identity lifecycle and approval flows (prerequisite for the other IGA modules).

| Feature                                                                                                            | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Workflow Authoring](https://docs.pingidentity.com/pingidm/8/workflow-guide/create-workflow.html)                  | Design and configure workflows (BPMN-style) for joiner/mover/leaver, approvals, escalations, access changes, and other IGA processes.                                          |
| [Workflow Instances Monitoring](https://docs.pingidentity.com/pingidm/8/workflow-guide/invoke-workflow.html)       | Monitor running and completed workflow instances (who requested what, current step, approvals, failures) to keep operations on track.                                          |
| [Workflow Operational Reporting](https://docs.pingidentity.com/pingidm/8/workflow-guide/about-workflow-tools.html) | Reporting and audit views over workflow executions to analyze volumes, bottlenecks, service level agreement (SLA) adherence, and compliance for identity and access processes. |

#### Access Request

Self-service access request and approval: access catalog, request submission and approval workflows, approver inbox, dashboards, entitlement management, and AI-driven governance recommendations for what access to grant or adjust.

| Feature                                                                                                                                        | Description                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Access Catalog](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/access-request-preface.html)                      | Curated catalog of applications, roles, and entitlements that users can browse and select when requesting new or changed access.                                |
| [Request Management](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/governance-request-types.html)                | Orchestrates the full lifecycle of access requests (create, change, remove), including routing to the right approvers and enforcing policies and prerequisites. |
| [Approval Inbox](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/governance-request-types.html)                    | Work queue for managers and approvers to review, approve, reject, or reassign incoming access requests with all relevant context.                               |
| [Request Dashboard](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/governance-request-types.html)                 | Dashboards and reports showing volumes, status, and aging of access requests to help operations and compliance teams monitor activity.                          |
| [Entitlement Mgmt](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/governance-request-types.html#request-settings) | Central management of entitlements (roles, groups, permissions), including how they map to target systems and which items appear in the access catalog.         |
| [Governance Recommendations](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/glossary.html)                        | Intelligence that suggests appropriate roles/entitlements or highlights risky requests based on policies, peer patterns, and governance rules.                  |

#### Access Review (Access Certifications)

Access certification and review module: campaign creation, reviewer inbox, inline compliance alerts, delegated and micro-certifications, remediation, and dashboards for tracking certification status and outcomes.

| Feature                                                                                                                                                 | Description                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Access Certifications Campaigns](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/access-review-certification-preface.html) | Define and run certification campaigns that periodically ask reviewers to confirm users' access to applications, roles, and entitlements.                             |
| [Remediation](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/example-violation-workflow.html)                              | Drive removal or adjustment of access identified as inappropriate during certifications, with workflows to revoke or modify entitlements in target systems.           |
| [Access Certifications Inbox](https://docs.pingidentity.com/pingoneaic/identity-governance/end-user/access-review-user-cert-items.html)                 | Work queue for certifiers to review, approve, revoke, or delegate access decisions for users and entitlements assigned to them in a campaign.                         |
| [Inline Compliance Alerts](https://docs.pingidentity.com/pingoneaic/identity-governance/end-user/sod-violations.html)                                   | Policy-driven alerts that surface risks or violations (for example, SoD or over-privilege) directly in the review experience to guide better certification decisions. |
| [Certifications Delegation](https://docs.pingidentity.com/pingoneaic/identity-governance/end-user/manage-user-lcm.html)                                 | Allow primary reviewers to delegate parts of a certification (for example, to application owners or local managers) while keeping overall campaign accountability.    |
| Micro Certifications                                                                                                                                    | Smaller, targeted certification events focused on specific apps, roles, or populations to reduce fatigue and support continuous compliance.                           |
| [Access Review Dashboard](https://docs.pingidentity.com/pingoneaic/identity-governance/end-user/manage-my-requests-preface.html)                        | Dashboards and reports that show campaign progress, completion rates, exceptions, and trends across access reviews for auditors and compliance teams.                 |

#### Segregation of Duties (SoD)

Segregation of duties policy and controls.

| Feature                                                                                                                          | Description                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SoD policy authoring](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/sod-policies.html)            | Define SoD rules that prevent users from holding toxic combinations of roles, entitlements, or access rights.                                               |
| [Access request and review guidance](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/sod-rules.html) | Surface SoD and compliance guidance directly in access request and review experiences so approvers can see potential conflicts before granting access.      |
| [Violation remediation](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/sod-rules.html)              | Identify and remediate SoD violations by adjusting roles/entitlements or reassigning duties to bring users back into compliance.                            |
| [SoD policy simulation](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/sod-policy-scans.html)       | Simulate the impact of proposed SoD policies or access changes to see which users would be affected and where violations would occur before enforcing them. |
| SoD policy certifications                                                                                                        | Run focused certification campaigns on SoD-relevant access so reviewers can confirm or revoke access that breaks defined SoD rules.                         |
| SoD impact analysis                                                                                                              | Analyze how SoD policies interact with current access, highlighting high-risk roles, entitlements, and users for deeper review.                             |
| Compliance analytics                                                                                                             | Dashboards and reports that provide visibility into SoD violations, remediation status, and overall governance posture for auditors and compliance teams.   |

#### Role Modeling

Role-based access design and optimization.

| Feature                                                                                     | Description                                                                                                                                     |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| [Role Discovery](https://docs.pingidentity.com/pingoneaic/idm-objects/roles-over-rest.html) | Analyze existing user-to-entitlement relationships to discover common patterns that can be turned into reusable roles.                          |
| Role Mining                                                                                 | Use analytics to cluster users and entitlements, suggesting candidate business and technical roles that reduce complexity and over-entitlement. |
| [Role Modelling](https://docs.pingidentity.com/pingoneaic/idm-objects/roles.html)           | Design, refine, and maintain role hierarchies (business/IT roles), including which entitlements each role grants and who should own them.       |

#### Agent IAM Core

Treats autonomous AI agents as first-class, governed identities in PingOne, so they authenticate, get scoped tokens, and access APIs, data, and tools under the same least-privilege policies and audit controls as human users and applications.

| Feature                                                                                                                                                             | Description                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [Governed AI agent identities](https://developer.pingidentity.com/identity-for-ai/getting-started/idai-what-is-identity-for-ai.html)                                | Treats AI agents as governed identities that authenticate, authorize, and audit like users and apps.             |
| [Agent models and trust boundaries](https://developer.pingidentity.com/identity-for-ai/identity/idai-agent-types.html)                                              | Defines agent types (personal, assistants, digital workers) and managed vs unmanaged based on control and trust. |
| [Delegated, least-privilege access](https://developer.pingidentity.com/identity-for-ai/getting-started/idai-what-is-identity-for-ai.html)                           | Applies delegation (not impersonation), scoped access, least privilege, and monitoring to AI agents.             |
| [Agent architecture and lifecycle](https://developer.pingidentity.com/identity-for-ai/agents/idai-what-are-agents.html)                                             | Models agents as LLM-driven systems that use tools, memory, and workflows in an iterative loop to do tasks.      |
| [Secure tool and API access](https://developer.pingidentity.com/identity-for-ai/agents/idai-tools-intro.html)                                                       | Treats tools/APIs as governed resources that agents call using structured commands under IAM control.            |
| [MCP and Agent2Agent (A2A) integration](https://developer.pingidentity.com/identity-for-ai/agents/idai-tools-intro.html#idai-mcp-and-a2a)                           | Uses MCP for secure agent-to-tool calls and A2A for agent-to-agent collaboration in multi-agent flows.           |
| [Central IAM benefits for PingOne Advanced Identity Cloud AI](https://developer.pingidentity.com/identity-for-ai/getting-started/idai-what-is-identity-for-ai.html) | Brings IAM benefits—secure access, governance, auditability, and risk controls—into AI agent use cases.          |

### PingOne Advanced Identity Cloud Infrastructure Add-Ons

| Add-on                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Additional sandbox environment](https://docs.pingidentity.com/pingoneaic/tenants/environments-sandbox.html)                                                                                 | Standalone sandbox tenant outside your dev/stage/prod chain, tracking the rapid release channel and allowing high-freedom experimentation.                                                                                                                                                                                                                                 |
| [Additional pre-production environment](https://docs.pingidentity.com/pingoneaic/tenants/environments-uat.html)                                                                              | Extra user acceptance testing (UAT) tenant inserted between development and staging, with the same capabilities as staging so you can run user acceptance testing in parallel with other non-prod testing.                                                                                                                                                                 |
| [Additional production tenant](https://docs.pingidentity.com/pingoneaic/tenants/environments.html)                                                                                           | An additional production tenant environment (Dev, Stage, Prod) with full isolation and operational support, used to separate regions, business lines, or major deployments while keeping standard PingOne Advanced Identity Cloud production characteristics. Is not aware of nor replicated with the primary tenant or any other PingOne Advanced Identity Cloud tenants. |
| [Multi-region high availability](https://docs.pingidentity.com/pingoneaic/product-information/high-availability-disaster-recovery.html)                                                      | Upgrades a tenant to multi-region HA, deploying active/standby capacity across regions with defined recovery time objective (RTO)/recovery point objective (RPO) so Ping Identity can restore service in a backup region if the primary region experiences an outage.                                                                                                      |
| [Secure Connect](https://docs.pingidentity.com/pingoneaic/tenants/secure-connect.html)                                                                                                       | Private network connectivity add-on that lets you create private network connections (for example using Equinix) from your network to PingOne Advanced Identity Cloud, often combined with a WAF to block direct internet access.                                                                                                                                          |
| [PingOne Advanced Identity Cloud Disaster Recovery Testing in Staging Environment](https://docs.pingidentity.com/pingoneaic/product-information/high-availability-disaster-recovery.html)    | Premium disaster recovery test for the staging environment: one inter-regional DR test per year to prove failover and failback between primary and secondary regions under a defined test plan.                                                                                                                                                                            |
| [PingOne Advanced Identity Cloud disaster recovery testing in production environment](https://docs.pingidentity.com/pingoneaic/product-information/high-availability-disaster-recovery.html) | Premium disaster recovery test for the production environment: one inter-regional DR test per year to validate production failover and failback between regions, with advance scheduling and defined scope.                                                                                                                                                                |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can review your current licenses and entitlements in the Ping Identity Support Portal. After signing on, go to the Licensing section. From this page, you can also access your support keys and open a support case if anything about your entitlements appears incorrect.You can find more information in Ping Identity's legal [Product terms and conditions](https://www.pingidentity.com/en/legal/product-terms.html). |

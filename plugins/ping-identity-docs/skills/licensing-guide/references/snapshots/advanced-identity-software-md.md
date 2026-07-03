---
title: Advanced Identity Software
description: Licensing information for Ping Identity advanced identity software products, including features, packaging, and managed (stored) identity unit of measure.
component: licensing-guide
page_id: licensing-guide::advanced-identity-software
canonical_url: https://docs.pingidentity.com/licensing-guide/advanced-identity-software.html
llms_txt: https://docs.pingidentity.com/licensing-guide/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  self-managed-products: Self-managed products
  pingaccess: PingAccess
  pingauthorize: PingAuthorize
  pingcentral: PingCentral
  pingdirectory: PingDirectory
  pingfederate: PingFederate
  pingam: PingAM
  pingds-directory-server-and-proxy: PingDS (Directory Server and Proxy)
  pinggateway: PingGateway
  pinggateway-edge-security-open-finance: PingGateway Edge Security - Open Finance
  pingidm: PingIDM
  pingone-platform-agent-iam-core: PingOne Platform Agent IAM Core
  agent-gateway: Agent Gateway
---

# Advanced Identity Software

These are **software products** that you install and operate:

* Deployed **on-premise** or in your own cloud.

* Licensing is enforced through **license keys**, **configuration**, or both in each product's admin console.

Software uses a **managed (stored) identity** unit of measure.

A **managed (stored) identity** is a **unique identifier** for a user, device, or other object that is **stored and managed** by the product, regardless of activity, such as the number of records or entries in the directory or identity store governed by the license.

![A diagram illustrating Ping Identity's product offerings from human to agentic with Ping Advanced Identity Software on the agentic end of the scale and highlighted](_images/pingadvancedidentitysoftware.png)

## Self-managed products

### PingAccess

Policy-based access management solution for web apps and APIs that enforces authentication and authorization decisions at the resource level using agents and gateways.

| Feature                                                                                                                                                         | Description                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Web access management](https://docs.pingidentity.com/pingaccess/latest/reference_guides/pa_web_access_management.html)                                         | Policy-based access control for web applications, enforcing authentication and authorization at the URL/resource level.                             |
| [API protection](https://docs.pingidentity.com/pingaccess/latest/pingaccess_use_cases/pa_protecting_an_api_with_pa_in_a_gateway_deployment.html)                | Protects APIs and services through reverse proxy or gateway mode, applying centralized policies and token validation.                               |
| [Agents and gateways](https://docs.pingidentity.com/pingaccess/latest/pingaccess_use_cases/pa_protecting_a_web_app_with_pa_in_an_agent_deployment.html)         | Uses lightweight agents or gateway deployment to integrate with a wide range of web servers and application platforms.                              |
| [Centralized policy model](https://docs.pingidentity.com/pingaccess/latest/reference_guides/pa_deploy_for_gateway_api_access_management.html)                   | Defines access policies once (conditions, rules, roles) and applies them consistently across many applications and APIs.                            |
| [Federation and SSO integration](https://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_pf_for_pa_sso_configuration.html) | Integrates with PingFederate and other IdPs to consume SAML/OpenID Connect (OIDC)/OAuth tokens and enforce single sign-on (SSO)-based access rules. |
| [High availability and scaling](https://docs.pingidentity.com/pingaccess/latest/reference_guides/pa_wam_gateway_production_deployment_architecture.html)        | Supports clustering and load-balanced deployments to provide resilient, scalable access enforcement for mission-critical applications and APIs.     |

### PingAuthorize

Fine-grained, externalized authorization engine that evaluates rich, attribute- and context-based policies to control access to APIs and data down to field and record level.

| Feature                                                                                                                                                          | Description                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| [Externalized authorization](https://docs.pingidentity.com/pingauthorize/latest/pingauthorize_server_administration_guide/paz_config_external_pdp.html)          | Central policy engine that moves authorization decisions out of apps/APIs into a centralized policy decision point (PDP) service.    |
| [Attribute-based access control (ABAC)](https://docs.pingidentity.com/pingauthorize/latest/pingauthorize_policy_administration_guide/paz_policy_management.html) | Uses identity, resource, and contextual attributes (time, device, risk, and so on) to make fine-grained allow/deny/filter decisions. |
| [Data-level security](https://docs.pingidentity.com/pingauthorize/latest/troubleshooting_pingauthorize_server/paz_working_with_collect_support_data.html)        | Enforces row/record, field/column, and value-level controls so you can mask, filter, or transform sensitive data per policy.         |
| [API and service integration](https://docs.pingidentity.com/pingauthorize/latest/pingauthorize_integrations/paz_integrations_main.html)                          | Protects APIs and services by evaluating policies at runtime through decision APIs or sidecar/gateway integrations.                  |
| Policy modeling and testing                                                                                                                                      | Tools to design, simulate, and debug authorization policies before and after deployment to reduce risk and misconfigurations.        |

### PingCentral

Centralized configuration and promotion hub that lets teams template, manage, and deploy PingFederate and PingAccess application integrations through a simplified, self-service workflow.

| Feature                                                                                                                                                                                     | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Centralized configuration hub](https://docs.pingidentity.com/pingcentral/latest/pingcentral_for_iam_administrators/pingcentral_promotion_processes/pingcentral_promotion_processes.html)   | Central place to manage and promote PingFederate and PingAccess configurations across environments (dev, test, prod) using consistent identity and access management (IAM) workflows. |
| [Self-service app onboarding](https://docs.pingidentity.com/pingcentral/latest/pingcentral_for_iam_administrators/pingcentral_mng_applications/pingcentral_manage_apps.html)                | Simplifies onboarding of new applications by giving app teams curated templates and guided flows instead of manual, expert-only configuration steps.                                  |
| [Templates and best-practice flows](https://docs.pingidentity.com/pingcentral/latest/pingcentral_for_iam_administrators/pingcentral_mng_templates/pingcentral_mng_templates.html)           | Uses reusable templates for common SSO/API patterns so teams can quickly stand up standards-compliant integrations with minimal custom work.                                          |
| [Environment promotion pipelines](https://docs.pingidentity.com/pingcentral/latest/pingcentral_for_iam_administrators/pingcentral_promotion_processes/pingcentral_promotion_processes.html) | Supports promoting configurations between environments with guardrails, reducing drift and manual errors in SSO/API policy deployment.                                                |
| [Visibility and governance](https://docs.pingidentity.com/pingcentral/latest/pingcentral_for_iam_administrators/pingcentral_mng_approvals/pingcentral_manage_approvals.html)                | Provides a central view of applications, connections, and versions, improving operational visibility and governance over identity integration changes.                                |

### PingDirectory

High-performance LDAP directory server for storing and serving identity and profile data at scale, with strong security, replication, and high availability for mission-critical IAM workloads.

| Feature                                                                                                                                                             | Description                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [High-performance LDAP directory](https://docs.pingidentity.com/pingdirectory/latest/managing_servers_and_certificates/pd_ds_ldap_starttls_extended_operation.html) | Low-latency, high-throughput LDAPv3 directory for storing and serving identity and profile data at scale.             |
| [Scalability and replication](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_manage_replication.html)           | Multi-master replication and proxy options to support large, globally distributed deployments with high availability. |
| [Access control and security](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_security_guide/pd_sec_access_control.html)                           | Fine-grained ACLs, strong password policies, encryption in transit/at rest, and detailed security/audit logging.      |
| [Flexible schema and extensibility](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_schema.html)                 | Custom objectClasses and attributes so you can model complex identity and application data requirements.              |
| [Operational tooling and monitoring](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_security_guide/pd_sec_monitor_entries.html)                   | Admin tools and APIs for backup/restore, tuning, monitoring, alerts, and troubleshooting.                             |
| [REST integration options](https://developer.pingidentity.com/pingdirectory/directory/)                                                                             | Optional REST/HTTP gateways to expose directory data to non-LDAP clients and modern applications.                     |

### PingFederate

Enterprise federation server that provides standards-based SSO and security token services using SAML, OAuth 2.0, and OpenID Connect for web, mobile, and API access.

| Feature                                                                                                                                                                   | Description                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Standards-based federation](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_integr_overview.html)                                      | SAML 2.0, OAuth 2.0, and OpenID Connect support for SSO and token services across web, mobile, and API applications.                                 |
| [Single sign-on (SSO) and logout](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) | Browser-based SSO and single logout for identity provider (IdP)-initiated and service provider (SP)-initiated flows across many federation profiles. |
| [Identity brokering and hub](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html)      | Acts as a hub between multiple identity providers and service providers, bridging many-to-many federation relationships.                             |
| [OAuth 2.0 / OIDC auth server](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_oidc_based_auth.html)                         | Full OAuth 2.0 authorization server and OpenID Connect provider with support for many grant types and client management.                             |
| [Security token services (STS)](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_wstrust_sts.html)                                       | WS-Trust-based security token service for issuing, transforming, and validating tokens between different systems and protocols.                      |
| [Token translation and mediation](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_access_token_management_instance.html)  | Converts between SAML, JSON Web Token (JWT), WS-Fed/WS-Trust, and other token formats to integrate legacy and modern apps.                           |
| [Adapters and integration kits](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_bundled_adapt_auth.html)                                | Rich library of bundled adapters and integration kits to connect to directories, IdPs, SPs, apps, and authentication sources.                        |
| [Enterprise deployment and HA](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_overview_cluster.html)                                        | Clustering, load balancing, and enterprise deployment features for high availability and scale in mission-critical environments.                     |

### PingAM

Access management server providing authentication journeys, SSO and federation (SAML, OIDC, and OAuth 2.0), adaptive and strong authentication, and authorization and User-Managed Access (UMA) for web, mobile, and API workloads.

| Feature                                                                                                          | Description                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Intelligent Access](https://docs.pingidentity.com/pingam/latest/am-authentication/auth-nodes-and-journeys.html) | Tree-based journeys that let you visually design authentication and step-up flows using nodes for risk, context, devices, and user interactions.                                                             |
| [Authorization](https://docs.pingidentity.com/pingam/latest/am-authorization/what-is-authz-decision.html)        | Policy-based, fine-grained authorization using attributes and context to make allow/deny decisions for applications, APIs, and resources.                                                                    |
| [Federation](https://docs.pingidentity.com/pingam/latest/am-oauth2/preface.html)                                 | Standards-based SSO and identity federation with SAML 2.0, OAuth 2.0, and OpenID Connect for web, mobile, and API use cases.                                                                                 |
| [Strong Authentication](https://docs.pingidentity.com/pingam/latest/am-authentication/authn-mfa-webauthn.html)   | Strong and adaptive authentication for customer identity and access management (CIAM), combining multi-factor authentication (MFA) factors, risk, and device/context signals in Intelligent Access journeys. |
| [User-Managed Access](https://docs.pingidentity.com/pingam/latest/uma/preface.html)                              | UMA-based access control that lets resource owners manage sharing and consent policies for their own protected resources.                                                                                    |

### PingDS (Directory Server and Proxy)

High-performance LDAP directory and proxy for storing and serving identity and profile data with strong security, replication, and high availability for large-scale deployments.

| Feature                                                                                                   | Description                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [LDAP directory services](https://docs.pingidentity.com/pingds/latest/ldap-guide/preface.html)            | High-performance LDAPv3 directory for storing and retrieving identity and configuration data. |
| [Replication and availability](https://docs.pingidentity.com/pingds/latest/config-guide/replication.html) | Multi-master replication and proxy options for high availability and geographic distribution. |
| [Access control and security](https://docs.pingidentity.com/pingds/latest/config-guide/admin-access.html) | Fine-grained access control, password policies, and encryption for protecting directory data. |

### PingGateway

Identity-aware gateway and micro-gateway that sits in front of web apps and APIs to enforce centralized authentication, authorization, token translation, and traffic controls at the edge.

| Feature                                                                                                      | Description                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [PingGateway Edge Security](https://docs.pingidentity.com/platform/latest/platform-guide/edge-security.html) | Gateway/edge security solution that fronts web apps and APIs with an identity-aware reverse proxy, enforcing centralized authentication, authorization, and traffic controls. |

### PingGateway Edge Security - Open Finance

Security overlay for PingGateway that provides financial-grade API compliance.

| Feature                                                                                                             | Description                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [FAPI Support](https://docs.pingidentity.com/platform/latest/platform-guide/edge-security.html#open-finance-module) | Logs FAPI interaction IDs and request metadata per transaction for regulatory compliance and audit. |

### PingIDM

Identity management and synchronization platform that handles identity lifecycle (joiner, mover, and leaver), relationships, self-service, and workflow-driven provisioning across systems.

| Feature                                                                                                              | Description                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [Lifecycle and relationship management](https://docs.pingidentity.com/pingidm/latest/getting-started/about-idm.html) | Model identities, relationships, and entitlements across systems to support full identity lifecycle.             |
| [Identity synchronization](https://docs.pingidentity.com/pingidm/latest/synchronization-guide/preface.html)          | Synchronize identity data between directories, databases, and applications using flexible mappings and policies. |
| [Self-service and workflow](https://docs.pingidentity.com/pingidm/latest/workflow-guide/preface.html)                | Self-service registration, profile management, and approval workflows for identity changes.                      |

### PingOne Platform Agent IAM Core

Treats autonomous artificial intelligence (AI) agents as first-class, governed identities in PingOne, so they authenticate, get scoped tokens, and access APIs, data, and tools under the same least-privilege policies and audit controls as human users and applications.

| Feature                                                                                                                               | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| [Identity for AI foundation](https://developer.pingidentity.com/identity-for-ai/getting-started/idai-what-is-identity-for-ai.html)    | Integrates AI agents into your IAM so they authenticate, authorize, and audit like users and apps.                 |
| [AI agent architecture](https://developer.pingidentity.com/identity-for-ai/agents/idai-what-are-agents.html)                          | Defines agents as autonomous systems that use LLMs, tools, memory, and workflows to complete tasks.                |
| [Agent types and trust model](https://developer.pingidentity.com/identity-for-ai/identity/idai-agent-types.html)                      | Classifies agents (personal, assistants, digital workers) and distinguishes managed vs unmanaged based on control. |
| [Tools and external actions](https://developer.pingidentity.com/identity-for-ai/agents/idai-tools-intro.html)                         | Treats tools as external APIs/functions agents call to access data or perform actions under IAM control.           |
| [MCP and A2A collaboration](https://developer.pingidentity.com/identity-for-ai/agents/idai-tools-intro.html#idai-mcp-and-a2a)         | Uses MCP for secure agent-tool calls and A2A for agent-agent coordination in multi-agent workflows.                |
| [IAM best practices for agents](https://developer.pingidentity.com/identity-for-ai/getting-started/idai-what-is-identity-for-ai.html) | Applies IAM principles like delegation (not impersonation), least privilege, and monitoring to agents.             |

### Agent Gateway

A runtime enforcement layer that sits between AI agents and the services and tools they use. It standardizes how agents call those services, applies fine-grained authorization, and centralizes monitoring and audit of agent activity.

| Feature                                                                                                    | Description                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| [MCP security gateway](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html)                    | Gateway in front of MCP servers and tools that brokers all agent-service traffic.                                                |
| [Per-action runtime enforcement](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html)          | Evaluates and enforces policy on every agent request in real time.                                                               |
| [Fine-grained authorization with PingOne](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html) | Uses PingOne Authorize, PingOne Protect, or PingOne Advanced Identity Cloud for rich, policy-based decisions beyond basic OAuth. |
| [Request validation and throttling](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html)       | Blocks invalid or unauthorized MCP calls and rate-limits agents to protect backends.                                             |
| [Token transformation](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html)                    | Adapts and transforms tokens so agents fit existing security and backend models.                                                 |
| [Central monitoring and audit](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html)            | Logs all agent activity for unified visibility, compliance, and troubleshooting.                                                 |
| [Least-privilege access](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html)                  | Ensures agents get only the minimal access needed for each action.                                                               |
| [Identity for AI integration](https://docs.pingidentity.com/pinggateway/latest/mcp/index.html)             | Pairs with Agent IAM Core: Core manages agent identity, while Gateway governs runtime actions.                                   |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can review your current licenses and entitlements in the Ping Identity Support Portal. After signing on, go to the Licensing section. From this page, you can also access your support keys and open a support case if anything about your entitlements appears incorrect.You can find more information in Ping Identity's legal [Product terms and conditions](https://www.pingidentity.com/en/legal/product-terms.html). |

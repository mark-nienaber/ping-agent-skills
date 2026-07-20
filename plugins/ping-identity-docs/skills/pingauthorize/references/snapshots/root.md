---
title: Introduction to PingAuthorize
description: PingAuthorize is a solution for fine-grained, attribute-based access control and dynamic authorization management.
component: pingauthorize
version: 11.1
page_id: pingauthorize::paz_introduction
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/paz_introduction.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 15, 2025
section_ids:
  pingauthorize-policy-editor: PingAuthorize Policy Editor
  pingauthorize-server: PingAuthorize Server
---

# Introduction to PingAuthorize

PingAuthorize is a solution for fine-grained, attribute-based access control and dynamic authorization management.

Digital transactions worldwide are increasing at exponential rates. At the heart of every transaction are questions of authorization:

* Can a given user perform this action or access this resource?

* How much data can a given partner access?

With more sophisticated use cases and more regulations for sensitive data, the rules that guide these questions of authorization get more complex. For example, a user can only transfer funds if their account is in good standing and they've agreed to the terms of service, or a partner can only access user data for those users who have given explicit consent.

Using traditional, static authorization solutions, like role-based access control (RBAC), to address complex authorization requirements lacks the full transaction context available only with dynamic, runtime authorization. PingAuthorize dynamic authorization can evaluate any identity attributes *(tooltip: \<div class="paragraph">
\<p>Distinct characteristics that describe a subject. If the subject is a website user, attributes can include a name, group affiliation, email address, and attributes alike.\</p>
\</div>)*, consents, entitlements, resources, or contexts to make attribute-based access control (ABAC) decisions in real time. PingAuthorize gives you centralized control over your digital transactions and application-level access to your protected resource *(tooltip: \<div class="paragraph">
\<p>Information, typically accessed through a web URL, that is protected by an access management system.\</p>
\</div>)*.

The following components provide the main capabilities for PingAuthorize.

## PingAuthorize Policy Editor

* Policy Administration and Delegation

  [PingAuthorize Policy Editor](pingauthorize_policy_administration_guide/paz_policy_management.html) enables nontechnical stakeholders to collaborate with IT and application developers to [build and test authorization policies](pingauthorize_policy_administration_guide/paz_policy_solutions.html) with a drag-and-drop UI. The editor supports fine-grained permissions and workflows to enable the right operational processes and delegated administration scenarios.

* Attribute Resolution and Orchestration

  Authorization policies depend on any combination of [attribute expressions](pingauthorize_policy_administration_guide/paz_attributes.html) that are evaluated at runtime by PingAuthorize Server. These attribute values might be present in the transaction itself, like an identifier of the authenticated user.

  PingAuthorize Policy Editor enables additional attribute values to be determined at runtime by configuring attribute source *(tooltip: \<div class="paragraph">
  \<p>Specific database or directory location containing data needed by an IdP to fulfill a connection partner's attribute contract or by an SP to look up additional attributes to fulfill an adapter contract.\</p>
  \</div>)* and [attribute processing](pingauthorize_policy_administration_guide/paz_value_processing.html) without writing any code.

## PingAuthorize Server

PingAuthorize Server includes the runtime policy decision service and multiple integration capabilities:

* Authorization Policy Decision APIs

  Applications or services obtain policy decisions at runtime using a policy decision point (PDP) application programming interface (API) *(tooltip: \<div class="paragraph">
  \<p>A specification of interactions available for building software to access an application or service.\</p>
  \</div>)*. Applications then enforce these decisions in their own application or service code. This integration configuration is the most flexible, supporting any application or service use case.

* API Security Gateway and Sideband API

  For fine-grained access control and data protection within application, platform, or microservice APIs, customers can integrate the API Security Gateway or Sideband API into their API architecture.

  In this configuration, PingAuthorize Server inspects API requests and responses, and then enforces policy by blocking, filtering, obfuscating, or otherwise modifying request and response data and attributes. This approach requires little or no code changes by the API developer.

* SCIM Service

  For fine-grained data access control and protection for structured datastore *(tooltip: \<div class="paragraph">
  \<p>A database or directory location containing user account records and associated user attributes.\</p>
  \</div>)* like Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
  \<p>An open, cross platform protocol used for interacting with directory services.\</p>
  \</div>)* and RDBMS, customers can deploy the System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
  \<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
  \</div>)* service in front of their [datastores](pingauthorize_server_administration_guide/paz_config_paz_user_store.html).

  In this configuration, PingAuthorize Server provides SCIM-based APIs through which clients create, read, update, and delete (CRUD) data. The [SCIM service](pingauthorize_server_administration_guide/paz_about_scim_service.html) enforces policy by blocking, filtering, obfuscating, or otherwise [modifying data and attributes](pingauthorize_policy_administration_guide/paz_create_policy_modify.html).

|   |                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The available enforcement features described above vary depending on your license. For more information, check your PingAuthorize license key or contact your Ping Identity account representative. |

Learn more about PingAuthorize architecture and policy decision environments in [PingAuthorize architectural overview](paz_architecture_overview.html).

---

---
title: PingAuthorize
description: PingAuthorize software provides fine-grained, attribute-based access control and dynamic authorization management, enabling you to protect resources and filter data for databases, applications, and APIs.
component: pingauthorize
version: 11.1
page_id: pingauthorize::paz_home_landing_page
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/paz_home_landing_page.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 13, 2026
page_aliases: ["_@pingauthorize::index.adoc"]
section_ids:
  release-notes: Release Notes
  get-started-with-pingauthorize: Get Started with PingAuthorize
  use-pingauthorize: Use PingAuthorize
  troubleshoot-pingauthorize: Troubleshoot PingAuthorize
  learn-more: Learn More
---

# PingAuthorize

PingAuthorize software provides fine-grained, attribute-based access control and dynamic authorization management, enabling you to protect resources and filter data for databases, applications, and APIs.

## Release Notes

* [Current](release_notes/paz_release_notes_legacy_home.html)

* [Previous releases](release_notes/paz_release_notes_legacy_home.html#previous_releases)

## Get Started with PingAuthorize

* [Introduction to PingAuthorize](paz_introduction.html)

* [Installing PingAuthorize](installing_and_uninstalling_pingauthorize/paz_install_pingauthorize.html)

## Use PingAuthorize

* [Use cases](pingauthorize_policy_administration_guide/paz_policy_solutions.html)

* [Server admin guide](pingauthorize_server_administration_guide/paz_server_admin_guide.html)

* [Policy admin guide](pingauthorize_policy_administration_guide/paz_policy_admin_guide.html)

* [Policy development and promotion](pingauthorize_server_administration_guide/paz_create_policies_dev_env.html)

* [API gateway integrations](pingauthorize_integrations/paz_integrations_main.html)

## Troubleshoot PingAuthorize

* [Enable detailed logging](pingauthorize_server_administration_guide/paz_enable_detailed_logging.html)

* [Capture debugging data](troubleshooting_pingauthorize_server/paz_working_with_collect_support_data.html)

* [Monitor server availability](pingauthorize_server_administration_guide/paz_server_availability.html)

* [Troubleshoot TLS-related issues](pingauthorize_server_administration_guide/paz_troubleshoot_tls_issues.html)

* [Configure LDAP health checks](pingauthorize_server_administration_guide/paz_config_health_check_dsconfig.html)

* [Visualize a policy decision response](pingauthorize_policy_administration_guide/paz_visualize_pol_resp.html)

## Learn More

* [PingAuthorize API Reference](https://developer.pingidentity.com/pingauthorize/pingauthorize/introduction.html)

* [PingAuthorize Server Docker image](https://hub.docker.com/r/pingidentity/pingauthorize)

* [PingAuthorize Policy Editor Docker image](https://hub.docker.com/r/pingidentity/pingauthorizepap)

* [PingAuthorize Community](https://support.pingidentity.com/s/topic/0TO1W000000dcxNWAQ/pingauthorize)

* [Ping Identity Support Portal](https://support.pingidentity.com/s/)

* [PingAuthorize customer training (existing customers only)](https://education.pingidentity.com/learn/course/1143/introduction-to-pingauthorize-90?generated_by=13429\&hash=d85bf6092a769d1b6671371d7fc89fa5b55dfd3b)

* [Partner Portal](https://www.pingidentity.com/en/account/sign-on.html?retURL=/bin/pic/sso/community?retURL=/PartnerPortal/s/)

---

---
title: PingAuthorize API Reference
description: The PingAuthorize Server and Policy Editor provide a collection of APIs for managing authorization resources and leveraging fine-grained authorization capabilities in your application or API service.
component: pingauthorize
version: 11.1
page_id: pingauthorize::paz_api_reference
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/paz_api_reference.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 13, 2026
---

# PingAuthorize API Reference

The PingAuthorize Server and Policy Editor provide a collection of APIs for managing authorization resources and leveraging fine-grained authorization capabilities in your application or API service.

* The Authorization Policy Decision APIs support non-API use cases where the PingAuthorize Server acts as the policy decision point (PDP), and your application server acts as the policy enforcement point (PEP). Learn more in the [Authorization Policy Decision API Reference](https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-decision.html).

* The Policy Editor APIs enable programmatic management of authorization resources, including:

  * Authorization policies, rules, targets, and statements

  * Trust Framework elements such as attributes, conditions, processors, and services

  * Branches, snapshots, and deployment packages

  * Test scenarios, test cases, and assertions

  Learn more in the [Policy Editor API Reference](https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-editor.html).

* The PingAuthorize Server's built-in System for Cross-domain Identity Management (SCIM) service provides a REST API for data that is stored in one or more external datastores, based on the [SCIM 2.0 standard](https://datatracker.ietf.org/doc/html/rfc7644). Learn more in the [SCIM API Reference](https://developer.pingidentity.com/pingauthorize/pingauthorize/scim.html).

---

---
title: PingAuthorize architectural overview
description: When planning your PingAuthorize dynamic authorization software deployment, you should review the components to install as well as the potential deployment methods, architectures, and environments.
component: pingauthorize
version: 11.1
page_id: pingauthorize::paz_architecture_overview
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/paz_architecture_overview.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 18, 2025
section_ids:
  components: Components
  implementation-architectures: Implementation architectures
  SCIM_API_to_datastores: SCIM API to datastores
  API_gateway_as_reverse_proxy: API security gateway as reverse proxy
  API_gateway_in_sideband: API security gateway in sideband configuration
  PDP_APIs_use_cases: PDP APIs for non-API use cases
  policy-decision-environments: Policy decision environments
---

# PingAuthorize architectural overview

When planning your PingAuthorize dynamic authorization software deployment, you should review the components to install as well as the potential deployment methods, architectures, and environments.

## Components

* Policy Editor

  The Policy Editor gives policy administrators the ability to develop and test data-access policies.

* PingAuthorize Server

  The PingAuthorize Server enforces policies to control fine-grained access to data.

When you configure a REST API to access data through the PingAuthorize Server, the server applies data-access policies that allow, block, filter, or modify protected resource *(tooltip: \<div class="paragraph">
\<p>Information, typically accessed through a web URL, that is protected by an access management system.\</p>
\</div>)* and data attributes *(tooltip: \<div class="paragraph">
\<p>Distinct characteristics that describe a subject. If the subject is a website user, attributes can include a name, group affiliation, email address, and attributes alike.\</p>
\</div>)*.

## Implementation architectures

PingAuthorize Server supports the following implementation and data flow architectures for enforcing fine-grained access to data:

* [SCIM API to datastores](#SCIM_API_to_datastores)

* [API security gateway as reverse proxy](#API_gateway_as_reverse_proxy)

* [API security gateway in sideband configuration](#API_gateway_in_sideband)

* [PDP APIs for non-API use cases](#PDP_APIs_use_cases)

The following sections describe these architectures in more detail.

### SCIM API to datastores

The PingAuthorize Server System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* service provides a REST API for data that is stored in one or more external datastores, based on the [SCIM 2.0 standard](https://datatracker.ietf.org/doc/html/rfc7644). Authorization policies are enforced by the SCIM service. Learn more in [SCIM API request and response flow](pingauthorize_server_administration_guide/paz_scim_request_response_flow.html).

![Diagram of the SCIM inbound and outbound request flow, showing traffic moving from the HTTP client through the SCIM API to the backend user store, with calls to an external policy information point as needed.](_images/pbr1654546084224.png)

### API security gateway as reverse proxy

You can configure PingAuthorize Server's API security gateway as a reverse proxy to an existing JSON REST API. In this architecture, PingAuthorize Server acts as an intermediary between clients and existing API services. Authorization policies are enforced by the API security gateway. Learn more in [API gateway request and response flow](pingauthorize_server_administration_guide/paz_sec_gw_request_response_flow.html).

![Diagram of the reverse proxy inbound and outbound request flow, showing traffic moving from the HTTP client through the PingAuthorize API security gateway to the backend API, with calls to an external policy information point as needed.](_images/njn1654546574817.png)

### API security gateway in sideband configuration

You can configure the PingAuthorize Server's API security gateway as an extension to an existing API lifecycle management gateway, commonly known as a sideband configuration. In this architecture, the API lifecycle management gateway functions as the intermediary between clients and existing API services and enforces policy decisions made by the PingAuthorize Server. Learn more in [API gateway integration](pingauthorize_server_administration_guide/paz_api_gw_integration.html).

![Diagram of the sideband inbound and outbound request flow, showing traffic from the HTTP client through the API Gateway to the backend API, with calls made to the PingAuthorize decision engine and external policy information points as needed.](_images/ahm1654547160165.png)

### PDP APIs for non-API use cases

You can implement either of the PingAuthorize Server's PDP APIs to support policy decisions in cases where you don't need to protect an API resource. Learn more about [Authorization Policy Decision APIs](pingauthorize_server_administration_guide/paz_authr_policy_decision.html).

![Diagram of the PDP API inbound and outbound request flow, showing traffic from the requestor through the servlet container to the PingAuthorize decision engine, and back again.](_images/ylq1654612582541.png)

## Policy decision environments

You can configure PingAuthorize for either of the following policy decision environments:

* Development environment (external PDP)

  Policies are developed in the Policy Editor. The Policy Editor serves as the external policy decision point (PDP), and the PingAuthorize Server serves as the policy enforcement point (PEP).

  This configuration accelerates policy deployment by putting the decision point closer to your policy updates, making it ideal for development or testing environments.

  |   |                                                                       |
  | - | --------------------------------------------------------------------- |
  |   | External PDP mode is not intended for use in production environments. |

  The following image shows PingAuthorize Server configured in a reverse proxy architecture. The [development environment](pingauthorize_server_administration_guide/paz_create_policies_dev_env.html) supports all PingAuthorize implementation and data flow architectures.

  ![Diagram of the external PDP mode inbound and outbound request flow, showing traffic from the HTTP client through the PingAuthorize server to the backend API, with calls made to the Policy Editor and external policy information points as needed.](_images/paz_external_reverse_proxy.png)

  Learn more about configuring PingAuthorize for development environments in [Configuring external PDP mode](pingauthorize_server_administration_guide/paz_config_external_pdp.html).

* Pre-production and production environments (embedded PDP)

  Policies are developed in the Policy Editor and deployed to the PingAuthorize Server, which serves as both the PEP and the PDP. This configuration supports policy testing in pre-production environments and live policy decisions in production environments.

  In these environments, the policy administrator [bundles policies into a deployment package](pingauthorize_server_administration_guide/paz_export_deployment_package.html) and then publishes them to the PingAuthorize Server. Embedding the policies in the PingAuthorize Server reduces latency in the decision request-response flow.

  The Policy Editor can deploy policy deployment packages to the PingAuthorize Server using one of the following methods:

  * Export the deployment package as a static file.

  * Publish to a cloud package store ([AWS S3](pingauthorize_server_administration_guide/paz_amazons3_deploy_package.html), [Azure](pingauthorize_server_administration_guide/paz_azure_deploy_package_store.html)) with the [Deployment Manager](pingauthorize_server_administration_guide/paz_deployment_manager.html).

  * Publish to a [file system package store](pingauthorize_server_administration_guide/paz_filesystem_deploy_package.html) with the [Deployment Manager](pingauthorize_server_administration_guide/paz_deployment_manager.html).

  The following image shows PingAuthorize Server configured in the reverse proxy architecture. Pre-production and production environments support all PingAuthorize implementation and data flow architectures.

  ![Diagram of the embedded PDP mode inbound and outbound request flow, showing traffic from the HTTP client through the PingAuthorize server to the backend API, with calls made to external policy information points as needed.](_images/paz_embedded_reverse_proxy.png)

  Learn more about configuring PingAuthorize for production environments in [Configuring embedded PDP mode](pingauthorize_server_administration_guide/paz_config_embedded_pdp.html).
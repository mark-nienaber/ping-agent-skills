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

---
title: Approach
description: Discover, rationalize, and implement identity data models aligned to business requirements
component: pingoneaic
page_id: pingoneaic:planning:plan-object-modeling-approach
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-object-modeling-approach.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Object modeling", "Data object model", "Framework", "Planning"]
page_aliases: ["plan-deploy:planning-object-modeling-approach.adoc"]
---

# Approach

The approach to data object modeling in PingOne Advanced Identity Cloud consists of three main phases: discovery, rationalization, and implementation.

* Discovery

  This stage involves the discovery of the current state of the identity and future requirements, including:

  * Sources of identity information, such as customer databases, directories, and third-party identity providers

  * Business application requirements, including the authorization model and identity data required for operation

  * Authentication requirements

  * Actors and entities within the identity space, including users, roles, and organizations

* Rationalization

  This stage involves analyzing the results from the discovery phase and defining privileges to deliver a workable object model. This step involves the following:

  * Includes all entities and attributes required for authentication, authorization, and identity management

  * Excludes identity data that is not relevant to business requirements

  * Defines all privileges for access to identity data at the field level

  * Maps all identity data from Advanced Identity Cloud to external repositories and vice-versa

* Implementation

  This stage involves configuring the managed data object model within the PingOne Advanced Identity Cloud tenant, following the detailed plan developed during the rationalization phase. This step includes the following configuration:

  * Ping Identity object attributes, roles, and internal privileges

  * Connector definitions for external repositories, including the attributes returned by each connector

  * Synchronization mappings for Advanced Identity Cloud to external repositories and vice-versa

---

---
title: Functionality differences when moving from self-managed
description: Understand feature differences when migrating from self-managed to Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:planning:plan-identity-cloud-functionality-differences
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-identity-cloud-functionality-differences.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Getting started", "Deployment", "Planning", "Migration"]
section_ids:
  key-areas-of-difference: Key areas of difference
  unsupported-features: Unsupported features
  no-planned-support: No planned support
  frequently-asked-questions: Frequently asked questions
  can-i-add-a-custom-cookie-domain: Can I add a custom cookie domain?
  can-i-customize-policy-evaluation-plugin: Can I customize policy evaluation with a plugin?
  can-i-customize-saml2-plugin: Can I customize SAML 2.0 with plugins?
  can-i-use-amster: Can I use Amster with Advanced Identity Cloud?
  can-i-use-ssoadm: Can I use ssoadm with Advanced Identity Cloud?
  can-i-have-multiple-realms: Can I have multiple realms?
  can-i-extend-the-schema: Can I extend the data model schema?
  can-i-connct-apps-to-ldap: Can I connect applications to LDAP (PingDS)?
  can-i-use-kerberos-desktop: Is Kerberos or desktop authentication supported in Advanced Identity Cloud?
  are-native-log-handlers-implemented: Are native log handlers implemented in Advanced Identity Cloud?
---

# Functionality differences when moving from self-managed

If you currently use PingAM and PingIDM on-premises or in a private cloud, you'll notice some differences in functionality when moving to PingOne Advanced Identity Cloud.

## Key areas of difference

| Key difference                          | Description                                                                                                                                                                                                                                                                      |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Advanced Identity Cloud is the platform | With Advanced Identity Cloud, you get the combined functionality of PingAM and PingIDM without the need for manual integration. For example, there's no requirement to deploy a datastore or the admin console, as these are included in the Advanced Identity Cloud deployment. |
| File system access                      | File system access isn't available in Advanced Identity Cloud. All functionality is accessed through the UI and REST APIs.                                                                                                                                                       |
| Direct access to the datastore          | Direct access to the datastore is not supported in Advanced Identity Cloud. Instead, Ping Identity manages the datastore for you and provides access through the UI and REST APIs. Configuration of PingDS isn't required.                                                       |
| Custom code and extensibility           | Advanced Identity Cloud supports extending the platform using JavaScript. Groovy and Java binaries aren't supported.                                                                                                                                                             |
| Extending the data model schema         | Advanced Identity Cloud supports creating managed objects through the UI. The storage of these objects is managed by Advanced Identity Cloud and cannot be explicitly configured.Learn more in [Can I extend the data model schema?](#can-i-extend-the-schema)                   |

## Unsupported features

The following features are not currently supported in Advanced Identity Cloud:

* Identity of Things (IoT)

* LDAP as a service

* Open Banking

* Security Token Service (STS)

* Sub-entry PingDS password policies

* User-Managed Access (UMA)

In addition, Advanced Identity Cloud only supports a subset of hashed passwords for import. Learn more in [Synchronize passwords](../identities/sync-identities.html#synchronize_passwords).

## No planned support

Ping Identity does not plan to support the following in Advanced Identity Cloud:

* AM XUI end-user sign on

* Authentication modules and chains

* Groovy

* Java binaries

* SOAP STS

## Frequently asked questions

### Can I add a custom cookie domain?

Yes. You can configure the cookie domains of your [custom domains](../realms/custom-domains.html) in Advanced Identity Cloud. Learn more in [Control cookie scope for custom domains](../realms/cookie-domains.html).

### Can I customize policy evaluation with a plugin?

Instead of a plugin, you can use scripted policy conditions to modify the actions taken by Advanced Identity Cloud during policy evaluation. Learn more in [Scripted policy conditions](../am-authorization/scripted-policy-condition.html).

### Can I customize SAML 2.0 with plugins?

Advanced Identity Cloud provides a scripting engine and template scripts for you to extend SAML 2.0 behavior. Java plugins aren't available with Advanced Identity Cloud. Learn more in [Customize SAML 2.0](../am-saml2/customize-saml2-plugins.html).

### Can I use Amster with Advanced Identity Cloud?

Amster is not supported in Advanced Identity Cloud deployments. However, several options are available for managing configuration data. These include:

* **Journey export and import**: You can export and import journeys through the Advanced Identity Cloud admin UI. This includes all dependencies such as nodes, inner journeys, scripts, and themes attached to a journey. Learn more in [Journeys](../journeys/journeys.html).

* **Postman collection**: Ping Identity provides a Postman collection with example requests organized by feature, making it easier to use and understand Advanced Identity Cloud REST APIs. Learn more in [Advanced Identity Cloud Postman collection](../developer-docs/postman-collection.html).

* **Open source tooling**: [Community-supported](https://support.pingidentity.com/s/question/0D5UJ00000MuxjN0AR/welcome-to-the-pingone-advanced-identity-cloud-community-page^) tools are also available for managing configuration.

### Can I use `ssoadm` with Advanced Identity Cloud?

The `ssoadm` feature isn't available in Advanced Identity Cloud. This is because `ssoadm` communicates directly with PingDS, which is not a requirement of Advanced Identity Cloud. Use the options mentioned in [Can I use Amster with Advanced Identity Cloud?](#can-i-use-amster) to help manage configuration data.

### Can I have multiple realms?

Advanced Identity Cloud tenants include two configurable realms, [Alpha and Bravo](../realms/alpha-bravo-realms.html). If you need to group identities further, you can use the [Organizations](../identities/organizations.html) feature.

### Can I extend the data model schema?

You can create managed objects through the UI. The storage of these objects is managed by Advanced Identity Cloud and cannot be explicitly configured.

Adding arbitrary custom attributes to the user schema is supported. However, there is a limitation on indexing custom attributes, so an indexed extension attribute is provided for this purpose.

Learn more in [Advanced Identity Cloud identity schema](../identities/identity-cloud-identity-schema.html).

### Can I connect applications to LDAP (PingDS)?

Not directly. The PingDS instance in Advanced Identity Cloud is not exposed for connecting applications. If you have an existing on-premises PingDS instance that your applications connect to, you will need to use a Remote Connector Server (RCS) to connect to your on-premises PingDS instance and then synchronize data using Advanced Identity Cloud. Learn more in [Sync identities](../identities/sync-identities.html).

### Is Kerberos or desktop authentication supported in Advanced Identity Cloud?

Yes. You can delegate Kerberos or desktop authentication via PingGateway, by using the [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html).

### Are native log handlers implemented in Advanced Identity Cloud?

In Advanced Identity Cloud, audit and debug log data is extracted through a consolidated REST endpoint. Learn more in [Get audit and debug logs](../tenants/audit-debug-logs.html).

---

---
title: Identity mappings
description: Plan how identity data flows and synchronizes between external systems and Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:planning:plan-object-modeling-identity-mappings
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-object-modeling-identity-mappings.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Object modeling", "Data object model", "Identity mappings"]
page_aliases: ["plan-deploy:planning-object-modeling-identity-mappings.adoc"]
---

# Identity mappings

When external identity data is synchronized with PingOne Advanced Identity Cloud, either as a one-time migration or on an ongoing basis, you should take into account the [synchronization strategy](../idm-synchronization/sync-config.html) into the data object model.

![Data object modeling](_images/object-modeling-identity-mappings.svg)

* Data mastering

  When identity information is [synchronized](../idm-synchronization/sync-overview.html) between environments, it is best to establish a single source of truth for that data. For example, if you create customer identities within a customer relationship management (CRM) system and then synchronize them into Advanced Identity Cloud, you should avoid the same customer information being updated in both Advanced Identity Cloud and the CRM system.

  This case can lead to a circular synchronization process, where changes are synchronized outbound to the CRM, then pulled back again at the next inbound sync, triggering another outbound sync, and so on.

* Data hygiene

  Prior to enabling synchronization, you should validate external identity data against the field policies set in Advanced Identity Cloud. You should resolve any discrepancies by updating existing data or by [mapping](../idm-synchronization/mappings.html) logic included in the synchronization process.

---

---
title: Key functions
description: Design identity models to support identification, authentication, authorization, and provisioning
component: pingoneaic
page_id: pingoneaic:planning:plan-object-modeling-key-functions
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-object-modeling-key-functions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Object modeling", "Data object model", "Functions"]
page_aliases: ["plan-deploy:planning-object-modeling-key-functions.adoc"]
---

# Key functions

The data object model in PingOne Advanced Identity Cloud should support the key functions of an identity platform including one or more of the following:

* **Identification**: Occurs when a user or entity makes a claim about their identity when attempting to gain access to a system or resource. For example, a user enters their username or ID to access a system. Learn how to achieve this via a journey in [login journey](../journeys/journeys.html#login).

* **Authentication**: Occurs when the user or entity proves their identity to the satisfaction of the access system. For example, a user enters their password or their identity is confirmed through some other process, which is verified by the system. Learn more in [Introduction to Authentication](../am-authentication/authn-introduction-authn.html).

* **Authorization**: Occurs when the system checks that the user or entity is allowed to access the resource or system after proper identification and authentication. Learn more in [Authorizations and policy decisions](../am-authorization/what-is-authz-decision.html).

* **Identity provisioning**: Ensures user accounts are created, updated, deleted, and assigned the proper access privileges to resources across applications and systems.

  You can achieve this in various ways in Advanced Identity Cloud:

  | Item                                                                          | Description                                                                                                                                                                                            |
  | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | [Application management](../app-management/applications.html)                 | Use a library of templates for OIDC applications that makes the process of registration, provisioning, and configuration quick and easy.                                                               |
  | [Bulk import identities](../identities/bulk-import-identities.html)           | Use a CSV file to import a set of identities. This is useful when you want to add a large number of identities to [Roles and assignments](../identities/roles-assignments.html) in a single operation. |
  | [Roles and assignments](../identities/roles-assignments.html)                 | Create an entitlements structure that fits the needs of each [realm](../realms/alpha-bravo-realms.html) by using roles and assignments.                                                                |
  | [Sync identities](../identities/sync-identities.html)                         | Synchronize identities from an external data store.                                                                                                                                                    |
  | [Pass-through authentication](../identities/pass-through-authentication.html) | Use pass-through authentication to validate user passwords via a remote service.                                                                                                                       |

![Object modeling key functions](_images/object-modeling.svg)Figure 1. Key functions of the data object model

---

---
title: Organize user communities
description: Separate user communities and choose properties to store on user identity profiles
component: pingoneaic
page_id: pingoneaic:planning:plan-object-modeling-user-data
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-object-modeling-user-data.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Object modeling", "Data object model", "User data", "Realms"]
page_aliases: ["plan-deploy:planning-object-modeling-modeling-user-data.adoc"]
section_ids:
  user_profiles: User profiles
  storing_user_properties_in_advanced_identity_cloud: Storing user properties in Advanced Identity Cloud
---

# Organize user communities

First, it is critical to decide if and how to use [realms](../realms/alpha-bravo-realms.html) when planning the object model.

You can organize distinct user communities, such as business partners and consumers in PingOne Advanced Identity Cloud. For example, you can distinguish users by implementing a shared property, such as a user type, or divide users by organizational membership.

The most complete separation of users is through the use of *realms*, which allows each community to have its own user properties, authentication and authorization policies, and journeys.

![User communities via realms](_images/object-modeling-user-communities.svg)

You can also separate users within realms through:

* [Organizations](../identities/organizations.html): Use organizations to separate identities with parent and children organizations.

* [Groups](../idm-objects/groups.html): Use groups to follow an organization structure or base groups on the needs and privileges of an arbitrary set of users.

## User profiles

Another critical stage in data object modeling is deciding which [properties](../identities/user-identity-properties-attributes-reference.html#reference-tables) to assign to users. This assignment is driven by your business application requirements. For example, you can assign properties to users based on the type and level of authentication required, and the level of access granted by passing authorization information to each application.

![Object modeling user profiles](_images/object-modeling-user-profiles.svg)

## Storing user properties in Advanced Identity Cloud

When considering which user properties to store in Advanced Identity Cloud, there are a number of important considerations for each property that fall under the following points

* Relevance

* Data validation

* Least privilege

* Search enablement

- Relevance

  You should only store user attributes in Advanced Identity Cloud if they are used for identity management, authentication, or authorization. For example, if a user's home address is never used during authentication and is never included in an ID or access token, then there is no requirement for this information to be stored in Advanced Identity Cloud.

  Defining properties not in use in Advanced Identity Cloud creates unnecessary overhead and can introduce potential privacy issues. Once the data object model is live, you can always add properties to the model, but it is much harder to *remove* properties that can affect existing users.

  Likewise, if the backend application fetches fine-grained user entitlements from an internal repository at access time, there is no need to include such entitlements in an access token; the token simply provides broad scope information to inform the application what constraints to apply for this method of access.

  ![Relevance](_images/object-modeling-relevance.svg)

  Also, when using OAuth2 access tokens, for example, the token can include a scope to indicate the broad permissions granted to the user; however, there is a balance between what authorization data Advanced Identity Cloud can deliver versus what additional entitlement checks can perform by the relying applications themselves. For example, the scopes and privileges included in an access token versus the resource access privileges held within an internal entitlements repository for the subject of that token. The commonality of authorization requirements between business applications also influences what authorization data can deliver.

- Data validation

  Each property should have a validation policy applied to it to maintain the integrity of the identity data. It is important to establish validation policies in full ahead of going live in production. Adjusting validation policies to live production data is complicated. Any policies applied retroactively to existing identity information cause issues when updating existing identities.

- Least privilege

  For each property defined in the data object model, you should apply the principle of *least privilege*. For properties that the user should not be able to update directly, the `user editable` setting should be disabled. For properties that should only be accessed internally, you should disable any `viewable` option, such as a managed object event trigger or custom endpoint. Learn more about setting this property in [Creating and modifying managed objects](../idm-objects/creating-modifying-managed-objects.html).

- Search enablement

  If a property is used to search for identities, such as retrieving a list of users by their surname or finding users who have not logged in for over a year, then the property must be a searchable field. Advanced Identity Cloud implements this as an indexed field. Learn more about the `searchable` field in [Creating and modifying managed objects](../idm-objects/creating-modifying-managed-objects.html).

  The property can either be a standard search field, such as `sn`, or an [indexed placeholder field](../identities/user-identity-properties-attributes-reference.html#general-purpose-extension-attributes), such as `frIndexedString1`. [Custom fields](../identities/identity-cloud-identity-schema.html#create-custom-attributes) added by the customer, for example `custom_userType`, cannot be searched upon. Since there are a limited number of searchable user fields, you must use care when using indexed placeholders for fields that will *never* be searched on.

---

---
title: Phase 1 - Assess and plan
description: Assess functional requirements and create a cloud adoption plan for Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:planning:plan-identity-cloud-assess-and-plan
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-identity-cloud-assess-and-plan.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Deployment", "Planning"]
page_aliases: ["plan-deploy:plan.adoc"]
---

# Phase 1 - Assess and plan

You create an overall cloud adoption plan to guide your project team and confirm how the PingOne Advanced Identity Cloud services will be used.

The best practices for creating a cloud adoption plan focuses on speed, efficiency, and repeatability of the migration processes.

The actions to take in this phase are:

* Review the most impactful use cases for Phase 1.

* Analyze functional requirements based on the IAM Domain:

  * [Plan for data object modeling](plan-object-modeling.html)

  * [Journeys](../journeys/journeys.html)

  * [Application integration](../app-management/applications.html)

  * [Authorization](../am-authorization/preface.html)

  * [UI and Theming](../end-user/end-user-ux-options.html)

* Review any existing Ping Identity platform configurations and extensions for S2S.

* Understand your tenant setup:

  * [Start here](../getting-started/getting-started.html)

  * [Tenant administrator settings](../tenants/tenant-administrator-settings.html)

  * [Tenant environments](../tenants/environments-development-staging-production.html)

  * [Data residency](../tenants/environments-data-residency.html)

* Analyze non-functional requirements for availability, operations, and data and application migration strategy.

* Establish communication logistics such as instant messaging channels, documentation, and issues tracking.

* Define teams and milestones for project governance.

* If you are moving from self-managed PingAM and PingIDM products, [understand the functionality differences](plan-identity-cloud-functionality-differences.html).

---

---
title: Phase 2 - Transform
description: Transform your deployment plan into a detailed technical architecture and migration strategy
component: pingoneaic
page_id: pingoneaic:planning:plan-identity-cloud-transform
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-identity-cloud-transform.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Deployment", "Action plan"]
page_aliases: ["plan-deploy:transform.adoc"]
---

# Phase 2 - Transform

Cloud adoption design helps you convert your cloud adoption project goals into an actionable plan. Use the cloud adoption design to guide and align your technical efforts with your organization's business strategy.

In consultation with your stakeholders, document the cloud adoption project goals and your desired business outcomes, and develop a technical architecture of the proposed solution.

The actions to take in this phase are:

* Develop the technical architecture of your deployment to the PingOne Advanced Identity Cloud

* Analyze and define [the data object model](plan-object-modeling.html#planning_considerations_for_data_object_modeling) for:

  * Users and groups

  * [Roles and assignments](../identities/roles-assignments.html)

  * [Organizations](../identities/organizations.html)

  * [Authentication and authorization requirements, such as KBA, OATH, and push devices](../am-authentication/preface.html)

* [Define attribute mappings between sources and Advanced Identity Cloud](../identities/user-identity-properties-attributes-reference.html)

* [Finalize the journeys (authentication flows) and sequence diagrams](../journeys/journeys.html)

* Analyze and define migration process:

  * [Required Remote Connector Service (RCS) connectors](https://docs.pingidentity.com/openicf/connector-reference/remote-connector.html)

  * [Password migration or pass-through authentication](../identities/pass-through-authentication.html)

  * [Configuration migration for S2S](../identities/sync-identities.html)

For further information on how to set up and configure Advanced Identity Cloud, view the article [Configuration management for ForgeRock Identity Cloud - Part 1](https://community.forgerock.com/t/configuration-management-for-forgerock-identity-cloud-part-1/).

---

---
title: Phase 3 - Adopt and refine
description: Execute adoption phase tasks to configure authentication, migration, and application integration
component: pingoneaic
page_id: pingoneaic:planning:plan-identity-cloud-adopt
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-identity-cloud-adopt.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Deployment", "Planning", "Refine"]
page_aliases: ["plan-deploy:adopt.adoc"]
---

# Phase 3 - Adopt and refine

After completing the transformation phase, your organization is ready to adopt PingOne Advanced Identity Cloud.

The actions to take in this phase are:

* Set up basic administration requirements:

  * Complete basic [tenant administration](../tenants/tenant-administrator-settings.html) tasks.

  * Review the [promotions process](../tenants/self-service-promotions.html) and [create ESVs](../tenants/esvs.html).

  * Establish and configure the [password policy](../realms/password-policy.html), [email templates](../tenants/email-templates.html) and [custom domains](../realms/custom-domains.html).

* Set up data migration:

  * Configure the required [connectors](../identities/sync-identities.html#about_identity_cloud_connectors) for data syncing.

  * Configure [synchronization](../idm-synchronization/mappings.html) mappings.

* Set up authentication and self-service [journeys](../journeys/journeys.html) (through [nodes](../journeys/auth-nodes.html)). Create [auth scripts](../developer-docs/scripting-auth.html) or [Custom endpoints](../developer-docs/scripting-custom-endpoints.html) for greater extensibility.

* Configure migration by levering appropriate S2S migration tools including:

  * [OAuth 2.0 and OpenID Connect](../realms/applications.html#oauth_2_0_and_openid_connect)

  * [SAML 2.0](../am-saml2/preface.html)

  * [Policies](../am-authorization/configuring-policies.html)

* Integrate applications with Advanced Identity Cloud:

  * Standard-based applications:

    * [OAuth 2.0 and OpenID Connect](../realms/applications.html#oauth_2_0_and_openid_connect)

    * [SAML 2.0](../am-saml2/preface.html)

  * Non-standard based applications such as [Gateways & agents](../realms/gateways-agents.html)

  * [SDK-integrated applications](../end-user/sdks.html)

* Design and configure [authorization policies](../am-authorization/configuring-policies.html).

* Determine the [UI](../end-user/end-user-ux-options.html) strategy for your organization.

---

---
title: Phase 4 - Enable
description: Transition Advanced Identity Cloud to production and hand over operations to support
component: pingoneaic
page_id: pingoneaic:planning:plan-identity-cloud-enable
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-identity-cloud-enable.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Deployment", "Enablement"]
page_aliases: ["plan-deploy:enable.adoc"]
---

# Phase 4 - Enable

After testing the PingOne Advanced Identity Cloud solution, you can transition it into production.

The actions to take in this phase are:

* Operations and monitoring: Monitor your tenant through [audit and debug logs](../tenants/audit-debug-logs.html).

  |   |                                                                                                                                   |
  | - | --------------------------------------------------------------------------------------------------------------------------------- |
  |   | The [Advanced Identity Cloud analytics dashboard](../tenants/analytics-dashboard.html) provides real-time metrics of your tenant. |

* Functional and performance testing for the new Advanced Identity Cloud deployment

* Phased migration plan for migrating applications to Advanced Identity Cloud

* Production transition to Advanced Identity Cloud

* Deprovision existing deployment

* Hand over to Ping Identity support team

---

---
title: Plan for Advanced Identity Cloud
description: Framework and phased approach for planning and executing Advanced Identity Cloud adoption
component: pingoneaic
page_id: pingoneaic:planning:plan-identity-cloud
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-identity-cloud.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Deployment", "Framework"]
page_aliases: ["plan-deploy:adopt-framework.adoc"]
section_ids:
  create_an_implementation_team: Create an implementation team
  gather_project_information: Gather project information
  adoption_phases: Adoption phases
  support: Support
---

# Plan for Advanced Identity Cloud

To plan for your organization's future using the cloud, you need a comprehensive, enterprise-grade identity platform that supports your priorities, such as:

* Intuitive usability

* Extensive customizations

* Detailed configuration options

* Wide-range of functionality

* Operational ease

The [Advanced Identity Cloud checklist](https://hub.pingidentity.com/c-s2s/4181-identity-cloud-checklist) highlights the top 10 considerations and best practices for your PingOne Advanced Identity Cloud strategy.

As you consider implementing Advanced Identity Cloud in your organization, the topics in the plan for Advanced Identity Cloud section (also referred to as the Adoption Framework Guide) provide guidance to help you effectively integrate the Advanced Identity Cloud services into your business environment.

Your transition into Advanced Identity Cloud does not have to be a hard transition. It can be a phased approach. For example, you can migrate a key business application into Advanced Identity Cloud and then transition other applications later.

|   |                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | There are functional differences between Advanced Identity Cloud and self-managed Ping Identity Platform.Learn more about migrating from a self-managed version of Ping Identity Platform to Advanced Identity Cloud in [Functionality differences when moving from self-managed](plan-identity-cloud-functionality-differences.html). |

The framework evolved from the best practices of Ping Identity employees, partners, and customers to help customers adopt Advanced Identity Cloud services. Proficiency in deploying, customizing, and administering the Advanced Identity Cloud is essential for the successful adoption of the Advanced Identity Cloud services. [Ping Training](https://training.pingidentity.com/) offers training to architect, build, and deploy your identity solution using the Ping Identity platform.

|   |                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The topics in the Plan for Advanced Identity Cloud section use Software to SaaS (S2S) to refer to the process of migrating customers from a self-managed deployment to Advanced Identity Cloud. |

## Create an implementation team

The successful adoption is dependent on establishing a project implementation team with the following roles or expertise:

* Project sponsor

* Project manager

* Implementation engineers

* UI developers

* JavaScript developers

* Enterprise architect

* Operations

* Performance testing

## Gather project information

Timely gathering of the following information is essential:

* Current project plan and important milestones

* Enterprise architecture diagrams

* Target system access and authentication methods

* Directory service information and data model (such as business units, user roles, groups, object hierarchy)

* Descriptions of existing identity and access management processes, procedures, and logic (such as sequence diagrams)

* Current and planned technical changes within the timeframe of the project

* Identity onboarding and offboarding flows

* Relevant system access and approval groups, as well as associated authority levels

## Adoption phases

The adoption of Advanced Identity Cloud services is best accomplished using existing products, proven methods, and reusable tools built from global field experience, in the following phases:

![Ping Identity Adoption Framework diagram with four phases](_images/new-adopt-fmwk.png)

1. [Assess and plan:](plan-identity-cloud-assess-and-plan.html)

   * Analyze functional and nonfunctional requirements

   * Review most significant use cases for phase 1

   * Review existing Ping Identity platform configurations for S2S movement

   * Provision tenants and set up project governance

2. [Transform:](plan-identity-cloud-transform.html)

   * Define overall architecture

   * Define required data models

   * Define migration path for application data and solution configurations

3. [Adopt and refine:](plan-identity-cloud-adopt.html)

   * Set up basic administration interfaces

   * Migrate data

   * Migrate configurations leveraging proven migration toolsets (for S2S)

   * Define journeys

   * Integrate applications

4. [Enable:](plan-identity-cloud-enable.html)

   * Set up operational and monitoring interfaces

   * Perform functional and performance tests

   * Transition to Advanced Identity Cloud in phases

   * Hand over to Ping Identity support team

## Support

Customers can access and manage the resources linked to their support subscription. Customer's nominated administrators can manage users, access policies, and application integration. Learn about getting started with Ping Identity support in the [Support Portal Administration Guide](https://support.pingidentity.com/s/article/Support-Portal-Administration-Guide).

---

---
title: Plan for data object modeling
description: Plan data object modeling to structure identity data for business and technical needs
component: pingoneaic
page_id: pingoneaic:planning:plan-object-modeling
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-object-modeling.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Object modeling", "Data object model", "Planning"]
page_aliases: ["pingoneaic::planning-object-modeling.adoc", "plan-deploy:planning-object-modeling.adoc"]
section_ids:
  planning_considerations_for_data_object_modeling: Planning considerations for data object modeling
---

# Plan for data object modeling

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | Learn more about the deployment process in [Plan for Advanced Identity Cloud](plan-identity-cloud.html). |

When preparing a PingOne Advanced Identity Cloud deployment, one of the most important phases of the planning process is *data object modeling*. Data object modeling is the process of creating an identity data model describing the data types, its structures, and its relationships that meet the business requirements of your company.

Successful deployment of Advanced Identity Cloud requires early and detailed consideration of the data object model. This applies as much to Advanced Identity Cloud as it does to a customer's own deployment of the Ping Identity software.

A structured approach of discovery and rationalization creates a solid foundation for the implementation of the object model, and allows for evolution over time in line with business requirements.

## Planning considerations for data object modeling

The key planning considerations for data object modeling are the following:

| Item                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [User communities](plan-object-modeling-user-data.html)          | Determine the different user communities the platform will serve, such as customers, business partners, and employees.                                                                                                                                                                                                                                                                                                                       |
| [Entities](../identities/identity-cloud-identity-schema.html)    | Determine the different entities and identities that make up each of these communities, such as end users, organizations, and devices.                                                                                                                                                                                                                                                                                                       |
| Authentication and authorization requirements                    | Determine the information needed for each of these entities to support your authentication and authorization requirements.Use [Introduction to Authentication](../am-authentication/authn-introduction-authn.html) to understand authentication. Use [Authorizations and policy decisions](../am-authorization/what-is-authz-decision.html) to understand authorization.Combine the two together with [Journeys](../journeys/journeys.html). |
| [Data organization](plan-object-modeling-relationships.html)     | Determine how end user identities (or data) are organized and how the organization affects authentication and authorization.Utilize realms, relationships, organizations, and groups to aggregate entities and identities into business units, standalone organizations, or families of users.                                                                                                                                               |
| [Identity mappings](plan-object-modeling-identity-mappings.html) | Determine the specific identity mappings required for your applications. It is important to understand how identity information is created or updated in Advanced Identity Cloud and which information is managed externally.                                                                                                                                                                                                                |

The development of the new identity model should preserve the entities and attributes relevant to your business requirements while leaving behind the identity data relevant only internally to your organization.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud uses schemas and other techniques to provide a common and consistent way to manage new and existing data sources across your organization. Advanced Identity Cloud offers extensive flexibility for identity profiles and their associated business processes. However, the overall object model is relatively fixed, as expected of a Software as a Service (SaaS) delivery model. The data object modeling process therefore involves some level of adaptation for any pre-existing customer identity model. It is unlikely—​and often undesirable—​that the existing model can be implemented exactly as-is within Advanced Identity Cloud. |

Learn more about the building blocks of the identity model in [object modeling](../idm-objects/preface.html).

---

---
title: Plan for security in Advanced Identity Cloud
description: Configure security controls, monitoring, and hardening for Advanced Identity Cloud deployments
component: pingoneaic
page_id: pingoneaic:planning:plan-security
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-security.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  network-connections: Network connections
  https-and-http: HTTPS and HTTP
  cookie-domain-configuration: Cookie domain configuration
  cors: CORS
  csrf-attacks: CSRF attacks
  identify-originating-client-ip-addresses: Identify originating client IP addresses
  identify-client-geolocation: Identify client geolocation
  request-data-size-limits: Request data size limits
  protect-applications: Protect applications
  protect-network-access-with-a-waf-or-a-cdn: Protect network access with a WAF or a CDN
  benefits-of-using-a-waf: Benefits of using a WAF
  benefits-of-using-a-cdn: Benefits of using a CDN
  sessions: Sessions
  set-expiry-time-for-sessions-and-jwt-tokens: Set expiry time for sessions and JWT tokens
  authentication-session-allowlisting: Journey session allowlisting
  session-invalidation-after-password-reset: Session invalidation after password reset
  access: Access
  remove-non-essential-access: Remove non-essential access
  deactivate-non-essential-features: Deactivate non-essential features
  harden-password-policy: Harden password policy
  account-lockout: Account lockout
  use-service-accounts-to-generate-access-tokens: Use service accounts to generate access tokens
  enforce-2-step-verification-for-tenant-administrators: Enforce 2-step verification for tenant administrators
  keys-secrets-and-encryption: Keys, secrets, and encryption
  update-cryptography: Update cryptography
  store-sensitive-data-in-secrets: Store sensitive data in secrets
  rotate-keys: Rotate keys
  encrypt-sensitive-data: Encrypt sensitive data
  encrypt-oidc-id-tokens: Encrypt OIDC ID tokens
  journeys: Journeys
  add-account-lockout-to-login-journeys: Add account lockout to login journeys
  add-email-confirmation-to-registration-journeys: Add email confirmation to registration journeys
  deactivate-unused-or-insecure-journeys: Deactivate unused or insecure journeys
  deactivate-hosted-pages: Deactivate hosted pages
  threats: Threats
  misconfiguration: Misconfiguration
  compromised-passwords: Compromised passwords
  audit-logging-and-monitoring: Audit logging and monitoring
---

# Plan for security in Advanced Identity Cloud

When you set up your PingOne Advanced Identity Cloud tenant environments, you must ensure that they are configured with security in mind.

The following topics lay out a comprehensive list of actions to take to help you set up Advanced Identity Cloud as securely as possible. However, security is a very broad subject, and every Advanced Identity Cloud customer has different use cases; you are expected to do your own research to complement the information found in these topics.

You should also ensure any changes you make to security settings in Advanced Identity Cloud follow your own corporate security policies, especially in relation to password complexity and active features.

## Network connections

### HTTPS and HTTP

Always use HTTPS for connections into Advanced Identity Cloud.

Advanced Identity Cloud does not accept connections over HTTP. However, a client making API calls to Advanced Identity Cloud over HTTP instead of over HTTPS can still send unprotected credentials in an HTTP Authorization header, inadvertently exposing sensitive information. Even though Advanced Identity Cloud rejects the request, the credentials could be leaked to eavesdroppers.

### Cookie domain configuration

Configure the cookie domain in your Advanced Identity Cloud tenant to ensure only users and entities from trusted domains can be authenticated.

By default, Advanced Identity Cloud sets the cookie domain based on the fully qualified hostname of a tenant, such as `id.mycompany.co.uk`. However, you might want to change the cookie domain to `mycompany.co.uk` so Advanced Identity Cloud can communicate with any subdomain.

Learn more in [Control cookie scope for custom domains](../realms/cookie-domains.html).

### CORS

Configure cross-origin resource sharing (CORS) to securely share browser resources across domains.

In Advanced Identity Cloud, you can configure CORS to allow browsers from trusted domains to access Advanced Identity Cloud protected resources. You can create as many individual CORS configurations as your applications need. The configurations combine to form the entire set of rules for resource sharing. The CORS service also collects the values of the JavaScript Origins property in each OAuth 2.0 client and adds them to the list of accepted origins.

Learn more in [Allow cross-domain requests with CORS](../tenants/cors.html).

### CSRF attacks

Advanced Identity Cloud includes a filter to harden protection against cross-site request forgery (CSRF) attacks. The filter applies to all REST endpoints under `/am/json/`. It requires all requests other than GET, HEAD, or OPTIONS to include at least one of the following headers:

* [X-Requested-With](../developer-docs/api-custom-headers.html#x-requested-with)

* Accept-API-Version: This header specifies which version of the REST API to use. Use this header in your requests to ensure future changes to the API do not affect your clients.

Failure to include at least one of the headers causes the REST request to fail with a `403 Forbidden` error.

Learn more about API versioning in [REST API versions](../am-rest/rest-api-versioning.html).

### Identify originating client IP addresses

The [X-Forwarded-For](../developer-docs/api-custom-headers.html#x-forwarded-for) HTTP header identifies the originating IP address of a client. However, as there are security and privacy concerns associated with its use, Advanced Identity Cloud includes two alternative HTTP headers:

* [X-Trusted-Forwarded-For](../developer-docs/api-custom-headers.html#x-trusted-forwarded-for)

* [X-Real-IP](../developer-docs/api-custom-headers.html#x-real-ip)

Consider using one of these headers as a trusted replacement for the `X-Forwarded-For` header, especially when making decisions concerning access.

### Identify client geolocation

Advanced Identity Cloud provides the following HTTP headers to let you identify the geographical location of client requests coming into your tenant environments:

* [X-Client-Region](../developer-docs/api-custom-headers.html#x-client-region)

* [X-Client-City](../developer-docs/api-custom-headers.html#x-client-city)

* [X-Client-City-Lat-Long](../developer-docs/api-custom-headers.html#x-client-city-lat-long)

Use these headers to implement region-specific behavior in your scripts and journeys. For example, you can enforce MFA for clients originating from a specific country or set of countries.

### Request data size limits

To protect against requests that contain large amounts of data, Advanced Identity Cloud rejects the following:

* Requests with a body size larger than 1 MiB (1,048,576 bytes).

* Requests that contain JWTs that expand to a size larger than 32 KiB (32,768 bytes) when decrypted.

### Protect applications

Ping Identity provides policy enforcement points (PEPs) to improve application security by enforcing Advanced Identity Cloud authentication and authorization decisions in your applications:

* Use PingGateway to protect your applications without modifying them or the infrastructure where they run—whether on-premises, in a public cloud, or in a private cloud. PingGateway acts as a reverse proxy, intercepting client requests and server responses to enforce authentication and authorization.

* Use Ping Identity web or Java policy agents to protect your applications when you have access to the infrastructure where they run. Policy agents natively plug into web or application servers and intercept inbound requests to enforce authentication and authorization. You can manage the policy agent configurations centrally from Advanced Identity Cloud.

Learn more in these guides:

* [Advanced Identity Cloud guide](https://docs.pingidentity.com/pinggateway/latest/aic/preface.html) for PingGateway

* [Advanced Identity Cloud guide](https://docs.pingidentity.com/web-agents/latest/identity-cloud-guide/preface.html) for Web Agent

* [Advanced Identity Cloud guide](https://docs.pingidentity.com/java-agents/latest/identity-cloud-guide/preface.html) for Java Agent

Learn more about protecting applications built using an SDK in [Security guide for SDKs](https://docs.pingidentity.com/sdks/latest/sdks/security/index.html).

### Protect network access with a WAF or a CDN

Use [Proxy Connect](../tenants/proxy-connect.html) to configure a proxy service, such as a web application firewall (WAF) or a content delivery network (CDN), in front of your Advanced Identity Cloud tenant environments.

#### Benefits of using a WAF

A web application firewall (WAF) is a network security tool. It sits in front of your network resources and inspects all incoming traffic to intercept and block malicious requests. It offers the following benefits:

* **Defence in depth**: Many large enterprises have a corporate security policy that mandates all internet-facing applications, including SaaS platforms like Advanced Identity Cloud, must be protected by a WAF. It acts as an additional, outer layer of security.

* **Protection from common web attacks**: It helps prevent common vulnerabilities and attacks, such as:

  * SQL injection

  * Cross-site scripting (XSS)

  * Malicious file uploads

* **Bot and scanner protection**: A WAF can identify and block automated bots and security scanners that are constantly probing your applications for weaknesses.

* **Rate limiting and brute-force prevention**: It can enforce rate limits on sensitive endpoints to prevent abuse, such as blocking an IP address that makes too many failed sign-on attempts in a short period (a classic brute-force or credential-stuffing attack).

* **DDoS mitigation**: WAFs are designed to absorb and mitigate distributed denial of service (DDoS) attacks, ensuring your sign-on and registration pages remain available during an attack.

#### Benefits of using a CDN

A content delivery network (CDN) is a network performance and availability tool, although modern CDNs often include WAF capabilities. It consists of a global network of servers that cache content closer to the geographical location of your users. It offers the following benefits:

* **Improved performance and lower latency**: For an application with a global user base, a CDN dramatically speeds up load times. It caches static assets (like images, CSS, JavaScript files) on servers all over the world. If your origin server is in North America, and a user in London accesses your sign-on page, they receive those assets from a nearby server in Europe instead of the origin server. This results in a faster, better user experience.

* **High availability and redundancy**: CDNs are highly resilient. If one of their data centers goes down, traffic is automatically rerouted to the next-closest location, adding a layer of availability to your network resources.

* **Reduced load on origin servers**: By serving cached content, the CDN reduces the number of direct requests to your network resources.

* **Cost savings**: By offloading traffic and reducing data transfer from the origin servers, a CDN can often lower bandwidth costs.

## Sessions

### Set expiry time for sessions and JWT tokens

To minimize the time an attacker has to attack an active session, set expiry times for Advanced Identity Cloud sessions and JWT tokens.

Ping Identity recommends setting an expiry time of 15 minutes. However, you should decide your expiry time according to the context of your deployment, balancing security and usability so that your end users can complete operations without their authenticated sessions frequently expiring. Learn more in the OWASP [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#session-expiration).

To update the expiry time for authenticated sessions and JWT tokens in Advanced Identity Cloud, learn more in [Configure session termination settings](../am-sessions/session-state-session-termination.html#session-termination-config).

### Journey session allowlisting

Enable journey session allowlisting to protect journey sessions from replay attacks, whereby a malicious user might try to rewind an authentication flow to a previous node.

Learn more in [Journey session allowlist](../am-sessions/about-sessions.html#journey_session_allowlist).

### Session invalidation after password reset

Advanced Identity Cloud has no automatic mechanism to delete authenticated sessions when a user changes their password. To implement automatic invalidation of authenticated sessions on password reset, consider one of the following approaches:

* Use the `logoutByUser` action, specifying the username in the request payload.

  This action can be used for server-side and client-side sessions and is described in [Invalidate all sessions for a user](../am-sessions/managing-sessions-REST.html#invalidate-sessions-user).

* Use a query to locate all sessions for a user, then use the `logoutByHandle` action to invalidate those sessions.

  This action can be used for server-side sessions only and is described in [Invalidate specific sessions](../am-sessions/managing-sessions-REST.html#invalidate-sessions-by-handle).

## Access

### Remove non-essential access

Make sure only authorized people can access Advanced Identity Cloud, and audit system access periodically.

### Deactivate non-essential features

The more features you have turned on, the greater the attack surface. If something is not being used, switch it off, or remove its configuration to deactivate it. These are some features to consider turning off:

* Hosted journey pages and/or hosted account pages (learn more in [Deactivate hosted pages](#deactivate-hosted-pages))

* Unused or insecure journeys (learn more in [Deactivate unused or insecure journeys](#deactivate-unused-or-insecure-journeys))

* Unused realms (learn more in [Manage realm settings](../realms/realm-settings.html#manage_realm_settings))

* RCS OAuth 2.0 client (learn more in [Deactivate the RCS OAuth 2.0 client](../identities/sync-identities.html#deactivate_the_rcs_oauth_2_0_client))

### Harden password policy

Ensure you harden your password policy for each realm. These are some common ways to harden a password policy:

* Require a minimum of 12 characters

* Prevent the use of repetitive characters

* Prevent the use of commonly used passwords

* Prevent reuse of the last three passwords

* Validate against user attribute values such as username

Learn more in [Password policy](../realms/password-policy.html).

### Account lockout

Account lockout is a security mechanism that locks a user account after repeated failed login attempts. You can use it to supplement your password policy to slow down brute-force attacks.

Ping Identity recommends using a persistent lockout. If that's not compatible with your company's preferences, Ping Identity recommends using a duration lockout of at least 15 minutes.

Learn how to configure account lockout and implement account lockout in your journeys in [Account lockout](../am-authentication/account-lockout.html).

### Use service accounts to generate access tokens

Ensure any automated scripts do not rely on a tenant administrator account to generate an access token. Instead, use a service account. Additionally, restrict the scopes that a service account can grant only to those needed by the automated script.

Learn more in [Service accounts](../tenants/service-accounts.html).

### Enforce 2-step verification for tenant administrators

Make sure 2-step verification is mandatory for tenant administrators.

Learn more in [Tenant administrator mandatory 2-step verification FAQ](../product-information/migration-dependent-features/tenant-administrator-mandatory-2-step-verification-faq.html).

## Keys, secrets, and encryption

### Update cryptography

Different algorithms and methods are discovered and tested over time, and communities of experts decide which are the most secure for different uses. Use up-to-date cryptographic methods and algorithms to generate keys.

Small keys are easily compromised. Use at least the [recommended key size](https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29).

### Store sensitive data in secrets

Ensure sensitive data such as passwords and encryption keys are stored in ESV secrets, and never embedded directly in configuration or scripts.

Learn more in the [Secrets](../tenants/esvs.html#secrets) section of [ESVs](../tenants/esvs.html).

### Rotate keys

These are some reasons to rotate keys regularly:

* To limit the amount of data protected by a single key.

* To reduce dependence on specific keys, making it easier to migrate to stronger algorithms.

* To prepare for when a key becomes compromised. The first time you try key rotation, it shouldn't be during a real-time recovery.

* To conform to internal business compliance requirements.

Learn more in [Use ESVs for signing and encryption keys](../tenants/esvs-signing-encryption.html).

### Encrypt sensitive data

Advanced Identity Cloud supports encryption of data stored in the repository. Data can be encrypted using reversible encryption or one-way encryption.

Ping Identity recommends you encrypt all sensitive data. These are examples of sensitive data:

* Passwords

* Authentication questions

* Credit card numbers

* Government benefit ID numbers

Learn more in [Secure identity data](../idm-security/secure-sensitive-data.html).

### Encrypt OIDC ID tokens

OpenID Connect 1.0 (OIDC) ID tokens can contain sensitive data and personally identifiable information (PII). Ping Identity recommends you encrypt all ID tokens.

Learn more in [Encrypt ID tokens and backchannel logout tokens](../am-oidc1/encrypting-oidc-idtokens.html).

## Journeys

### Add account lockout to login journeys

Login journeys are vulnerable to brute force attacks. You can mitigate this risk by adding [account lockout](#account-lockout) to your login journeys.

### Add email confirmation to registration journeys

Registration journeys are vulnerable to denial-of-service attacks, where attackers try to create extremely high numbers of new users with the intention of exhausting system resources and creating an outage. You can mitigate this risk by using the Email Suspend node in your registration journeys to prevent new users from being created until an email address is verified.

Learn more in [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html).

### Deactivate unused or insecure journeys

Advanced Identity Cloud is preconfigured with default journeys to get you started. However, Ping Identity recommends you harden these default journeys or implement your own journeys using security best practices; for example, by adding MFA to a login journey to confirm user identity using a device.

Once you have built your journeys, ensure you deactivate any unused journeys, particularly insecure login journeys that only require a username and password.

Learn more in the [Deactivate a journey](../journeys/journeys.html#deactivate-journeys) section of [Journeys](../journeys/journeys.html).

### Deactivate hosted pages

If you have developed your own end-user journey and account experience using Ping SDKs or APIs, Ping Identity recommends that you deactivate the hosted journey pages and/or the hosted account pages to ensure there is no risk of unauthorized access by a malicious user.

Learn more in [Advanced Identity Cloud hosted pages](../end-user/hosted-pages.html).

## Threats

### Misconfiguration

Misconfiguration can arise from bad or mistaken configuration decisions and poor change management. Depending on the configuration error, features can stop working in obvious or subtle ways and potentially introduce security vulnerabilities.

To guard against bad configuration decisions, implement good change management:

* For all enabled features, document why they are enabled and what your configuration choices mean. This implies a review of configuration settings, including default settings that you accept.

* Validate configuration decisions with thorough testing.

* Maintain a record of your configurations and the changes applied.

* Use version control software for any configuration scripts and to record changes to configuration files.

### Compromised passwords

Despite efforts to improve how people manage passwords, users have more passwords than ever before, and many use weak passwords. You are strongly encouraged to use a password manager to generate secure passwords.

### Audit logging and monitoring

Advanced Identity Cloud provides an audit logging service that captures key auditing events critical for system security, troubleshooting, and regulatory compliance.

Audit logs gather operational information about events that occur within an Advanced Identity Cloud tenant. They track processes and security data, such as authentication mechanisms, system access, user and administrator activity, error messages, and configuration changes.

You are strongly encouraged to set up systems to monitor your audit logs and alert you to unusual patterns of behavior.

Learn more in [Monitor your tenant](../tenants/monitoring.html).

---

---
title: Relationships
description: Organize identities using relationships and relationship-derived virtual properties
component: pingoneaic
page_id: pingoneaic:planning:plan-object-modeling-relationships
canonical_url: https://docs.pingidentity.com/pingoneaic/planning/plan-object-modeling-relationships.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Object modeling", "Data object model", "Relationships", "Virtual Properties"]
page_aliases: ["plan-deploy:planning-object-modeling-modeling-relationships.adoc"]
---

# Relationships

*Relationships* are a key consideration in the identity model. You can use relationships in various ways to organize identities and to drive authentication and authorization policies. Relationships exist between users, between users and organizations, and between organizations.

![Data object modeling relationships](_images/object-modeling-relationships.svg)

* Relationship-derived virtual properties

  For those relationships that exist in the PingOne Advanced Identity Cloud default schema, consider using [relationship-derived virtual properties](../idm-objects/managed-object-virtual-properties.html#relationship-derived-virtual-properties) (RDVPs) for any information that can be used for authentication or included in authorization tokens. For example, if you use an organizational property to determine whether to enforce multi-factor authentication at login, then it is more efficient to store a copy of that property in the profile of each member of the organization, rather than looking up the organization properties using the relationship each time.

  The caveat is that each update to the organization properties triggers an update to the users belonging to that organization if you mirror the organization properties using an relationship-derived virtual property. This overhead is amplified if the RDVP is included in outbound synchronization to any external repositories.

* Relationship properties

  In some cases, relationships are not completely binary in nature. For example, if a user belongs to multiple organizations, the relationship may be different for each organization. A user can be authorized to represent multiple organizations, but have a different role at each. You may also want to store additional information about the relationship. For example, a user can be an alumni of multiple educational establishments and have a start/end date for each one.

  In this case, you can consider defining relationship properties in the data object model. One or more properties can be defined for the relationship itself, such as role, date range, privileges, and others. You can include these properties in authentication decisions and access tokens.

  ![Data object modeling](_images/object-modeling-relationships-properties.svg)

* Custom relationships

  The Advanced Identity Cloud schema supports custom relationships. Custom relationship properties allow you to define custom relationships between managed objects. For example, you could model a parent-child relationship by creating the custom\_Parents and custom\_Children properties and configuring them as one-way one-to-many relationships. Learn more in [Configure relationships](../identities/configure-relationships.html).
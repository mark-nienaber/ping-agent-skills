---
title: About the getting started guide
description: Understand the purpose, goals, prerequisites, and structure of the Advanced Identity Cloud getting started guide
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-about
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-about.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  gs-about-goals: Goals
  gs-about-before-begin: Before you begin
---

# About the getting started guide

This guide is for new Advanced Identity Cloud tenant administrators. It provides a step-by-step path to build a working solution and get up and running.

To get started, it's best to begin with the basics and add more complex workflows and customizations later. The guide provides best practices and next steps so you can explore further after you've mastered the basics.

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | Before you begin, familiarize yourself with the [Key concepts](getting-started-concepts.html) in Advanced Identity Cloud. |

## Goals

By following this guide, you'll achieve the following goals:

* Register your tenant and invite other tenant administrators

* Explore the Advanced Identity Cloud platform

* Create end users to represent your customers or employees

* Configure and test basic end-user experiences, including:

  * Registration

  * Authentication

  * Account recovery

  * Profile management

* Apply basic branding (logo, colors) to your end-user pages

* Learn how to integrate an OpenID Connect (OIDC) application for single sign-on (SSO).

## Before you begin

Before getting started, make sure you meet the following prerequisites.

* **Knowledge requirements**:

  * A basic understanding of identity and access management (IAM) concepts. Learn more in [Identity Fundamentals](https://www.pingidentity.com/en/resources/identity-fundamentals.html).

  * A basic understanding of what Advanced Identity Cloud is. Learn more in [PingOne Advanced Identity Cloud](https://www.pingidentity.com/en/platform/pingone-advanced-identity-cloud.html).

* **System requirements**: A working Advanced Identity Cloud tenant with super administrator or tenant administrator access.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Advanced Identity Cloud has four administrator roles:* **Tenant administrator**: Can manage most tenant and realm settings, but can't manage other administrators.

* **Super administrator**: Has full administrative access, including the ability to manage other administrators. The initial account for a new tenant has this role.

* **Tenant auditor**: Has read-only access to all tenant settings and data.

* **Brand administrator**: Has permissions to only manage hosted pages settings.Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups). |

---

---
title: Getting help
description: Access support resources including the Ping Identity support portal, training courses, and community forums
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-help
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-help.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  support_and_customer_success: Support and customer success
  training: Training
  community: Community
---

# Getting help

Ping Identity is here to help you with your identity journey. If you need assistance, several resources are available.

## Support and customer success

You'll have a dedicated team to help you achieve your goals. To find answers to common questions, create a support case, access training, and more, visit the [Ping Identity Support Portal](https://support.pingidentity.com).

Learn about getting started with Ping Identity support in the [Support Portal Administration Guide](https://support.pingidentity.com/s/article/Support-Portal-Administration-Guide).

## Training

Ping Identity offers a wide range of on-demand and instructor-led training courses to help you master Advanced Identity Cloud.

Explore the catalog at [Ping Training](https://training.pingidentity.com/).

## Community

Join the conversation, ask questions, and share solutions with other users and Advanced Identity Cloud experts.

Visit the [Ping Identity Community](https://support.pingidentity.com/s/community-home).

---

---
title: "Getting started: Next steps"
description: Plan your next steps after completing the getting started guide including training, deployment planning, and production preparation
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-next-steps
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-next-steps.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
---

# Getting started: Next steps

Congratulations! You've completed all the steps for getting started with Advanced Identity Cloud and have a solid foundation to build upon.

Ping Identity recommends the following next steps to help you prepare for a successful production launch:

* **Get release notifications**: Learn more about the Advanced Identity Cloud [release process](../release-notes/release-process.html) and how to stay up to date with the latest features and enhancements.

* **Training**: Take training courses to build your knowledge of Advanced Identity Cloud features and capabilities:

  * [On-Demand Training](https://backstage.pingidentity.com/university/category/PING)

  * [Curriculum](https://backstage.pingidentity.com/university/courses/)

* **Try out use cases**: Walk through common Advanced Identity Cloud administration, configuration, and integration tasks in the [use case catalog](../use-cases/preface-pages/about-use-case-catalog.html).

* **Explore developer resources**:

  * Explore how to integrate your mobile and web apps with [Ping SDKs](https://docs.pingidentity.com/sdks/latest).

  * Access standalone [API reference content](https://developer.pingidentity.com/pingoneaic-api/) designed for developers integrating with Advanced Identity Cloud.

  * Find more information about developing with Ping Identity on our [developer portal](https://developer.pingidentity.com/pingoneaic.html).

* **Plan your deployment**: Review the documentation planning sections to help you prepare for production deployment. Learn more in [Plan for Advanced Identity Cloud](../planning/plan-identity-cloud.html), [Plan for data object modeling](../planning/plan-object-modeling.html), and [Plan for security](../planning/plan-security.html).

* **Review best practices**: Revisit the "Best practices and next steps" sections in this guide to help you with your production deployment.

* **Review performance and load testing guidelines**: Understand the Advanced Identity Cloud [performance and load testing policy](../product-information/penetration-and-load-testing-policy.html), including expectations, constraints, and best practices for validating your tenant.

* **Stream logs to external tools**: Learn how to [stream audit and debug logs](../tenants/audit-debug-logs-push.html) from Advanced Identity Cloud to your external monitoring and security tools.

* **Secure your own email provider before go live**: If you used the Advanced Identity Cloud email service for testing purposes, make sure to set up and configure your own [email provider](../tenants/email-provider.html) before going live.

* **Join the community**: If you haven't already done so, join the [Ping Identity Community](https://support.pingidentity.com/s/community-home) to connect with other users and Advanced Identity Cloud experts.

---

---
title: Key concepts
description: Understand key Advanced Identity Cloud concepts including tenants, realms, journeys, managed identities, applications, and synchronization
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-concepts
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-concepts.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  gs-tenants: Tenants
  tenant-environments: Tenant environments
  promotion_model: Promotion model
  realms: Realms
  release_cycles: Release cycles
  tenant_versions: Tenant versions
  gs-add-ons: Add-on capabilities
  user_interfaces: User interfaces
  apis: APIs
  audit_logs: Audit logs
  gs-core-components: Core components
  journeys: Journeys
  managed-objects: Managed objects
  applications: Applications
  identity_synchronization: Identity synchronization
  email_providers: Email providers
---

# Key concepts

Take some time to familiarize yourself with some key concepts in Advanced Identity Cloud. You can find more detailed information about each topic in the linked pages.

## Tenants

|   |                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about Advanced Identity Cloud tenants in [Explain tenant environments](https://backstage.pingidentity.com/university/on-demand/course/TGVhcm5pbmdQYXRoOjk4/module/Q291cnNlOjI0Nzky/chapter/Q29udGVudDo0Mzcx/play/Q29udGVudDo0Mzcy) on-demand training (9.30 minutes). |

### Tenant environments

Advanced Identity Cloud provides *development*, *staging*, and *production* environments for you to build, test, and deploy your identity and access management (IAM) configuration and applications. These three environments share the same configuration.

Additionally, you can have two other environment types as [add-on capabilities](#gs-add-ons):

* A *user acceptance testing (UAT)* environment for testing new features in a production-like setting. You can have as many UAT environments as you need, and they share configuration with your development, staging, and production environments.

* A standalone *sandbox* environment for experimenting with new features. This environment is linked to the rapid release channel, meaning it receives the newest Ping Identity features and fixes before they're deployed to your other environments. You can have more than one sandbox environment.

![Tenant environments](_images/tenant-environments-all.png)

Learn more in [Tenant environments](../tenants/environments.html).

### Promotion model

Configuration in Advanced Identity Cloud is managed through a *promotion model*. You make changes to your static configuration (such as user journeys or scripts) in your development environment, and then promote those changes to staging for testing, and finally to production. This ensures a safe and repeatable process for deploying your changes. Any static configuration changes are applied immediately when you promote your changes to production.

You can use [Environment Secrets and Variables (ESVs)](../tenants/esvs.html) to manage sensitive data or values that need to be different for each environment, such as API keys or external URLs.

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | There is no automated process for promoting changes from a sandbox environment to a development environment. Non-sequential promotions (between the development environment and the production environment) are not supported. |

Learn more in [Introduction to self-service promotions](../tenants/self-service-promotions.html).

### Realms

A *realm* is a self-contained unit within your tenant used to manage separate groups of users and applications. For example, you might use one realm for your employees and one realm for your customers.

Advanced Identity Cloud provides two realms: *Alpha* and *Bravo*. These realms are configurable, unlike the top-level realm that Advanced Identity Cloud configures for tenant administrator identities. You can't add more realms. You can switch between realms in the Advanced Identity Cloud admin console.

Learn more in [Realm settings](../realms/realm-settings.html).

### Release cycles

Ping Identity delivers new features, fixes, and security updates through continuous general availability (GA) releases. These releases are deployed through two main channels:

* **Rapid channel**: Used for sandbox\[[1](#_footnotedef_1 "View footnote.")] environments and contains the absolute newest GA features and fixes. This lets Ping Identity qualify and establish GA releases through cumulative usage and soak testing, typically over a 2-week period. When a GA release has been established, it's allocated to the regular channel.

* **Regular channel**: Used for development, UAT\[[2](#_footnotedef_2 "View footnote.")], staging, and production environments and contains more established GA features and fixes.

Learn more in [Release process](../release-notes/release-process.html).

### Tenant versions

Ping Identity assigns each release a unique version number, which helps track what's included and when it's released to a tenant. You can check the version in the Advanced Identity Cloud admin console, in the page footer.

Learn more in [Release information](../tenants/environments-release-information.html).

### Add-on capabilities

Add-on capabilities are features or products not included in the standard Advanced Identity Cloud offering that can be added to your subscription.

Learn more in [Add-on capabilities](../product-information/add-on-capabilities.html).

### User interfaces

Administrators and end users interact with the platform through these web interfaces:

* **Advanced Identity Cloud admin console**: The administrative consoles where you configure tenants, design journeys, manage users, and set up applications. As an administrator, you'll spend most of your time in this UI. Learn more in [Task 2: Explore the platform](getting-started-explore-platform.html).

* **Hosted account pages**: A customizable dashboard for your end users. After signing on, end users can manage their profile, view their applications, and handle security settings such as changing their password or registering multi-factor authentication (MFA) devices. Learn more in [Hosted account pages](../end-user/hosted-pages-account.html).

* **Hosted journey pages**: The pages presented to end-users when signing on. Learn more in [Hosted pages](../end-user/hosted-pages.html).

### APIs

Many of the features available through Advanced Identity Cloud UIs are also available through REST APIs. This allows you to manage your identity solution programmatically using tools such as Postman, cURL, or custom scripts.

Learn more in [Advanced Identity Cloud API reference](../developer-docs/api-reference.html).

### Audit logs

Advanced Identity Cloud records detailed audit and debug logs for security and troubleshooting purposes. These logs capture important events related to authentication, administrative changes, and user activity. You can retrieve logs programmatically using APIs, stream them to an external monitoring tool or security information and event management (SIEM) system, or view them in the Advanced Identity Cloud admin console.

Learn more in [Get audit and debug logs](../tenants/audit-debug-logs.html).

## Core components

### Journeys

In Advanced Identity Cloud, a *journey* is a visual workflow that guides your end users through processes such as signing on, registering for a new account, or resetting a password. Advanced Identity Cloud provides several pre-configured journeys for these common tasks, which you can customize with a drag-and-drop editor to meet your own requirements.

The editor also includes annotation features such as sticky notes and comments, which help you document complex logic or leave notes for other administrators.

Learn more in:

* [Create authentication flows with journeys](../journeys/journeys.html)

* On-demand training: [Explain Advanced Identity Cloud journeys](https://backstage.pingidentity.com/university/on-demand/course/TGVhcm5pbmdQYXRoOjk4/module/Q291cnNlOjI0Nzky/chapter/Q29udGVudDo0Mzcx/play/Q29udGVudDo0Mzc5) (12.57 minutes)

|   |                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [Ping Identity Marketplace](https://marketplace.pingone.com/) includes several preconfigured journeys, including threat detection with PingOne Protect and financial services journeys. You can download and import these journeys, and adapt them to suit your needs. |

### Managed objects

A *managed object* is an identity-related entity or resource managed by Advanced Identity Cloud.

The main managed objects are:

* **Users**: Your customers, employees, or partners.

* **Roles**: Collections of permissions that define what a user can do.

* **Assignments**: The link that grants a role to a user or group.

* **Groups**: Collections of users, often used to simplify role assignments.

* **Organizations**: Hierarchical structures for organizing users, such as business departments.

Learn more in:

* [Advanced Identity Cloud identity schema](../identities/identity-cloud-identity-schema.html), [Configure managed objects](../identities/configure-object-types.html), [Manage identities](../identities/manage-identities.html), [Groups](../idm-objects/groups.html)

* On-demand training: [Introduce user profiles](https://backstage.pingidentity.com/university/on-demand/course/TGVhcm5pbmdQYXRoOjk4/module/Q291cnNlOjI0Nzky/chapter/Q29udGVudDo0Mzcx/play/Q29udGVudDo0Mzg2) (5.49 minutes)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - When preparing a Advanced Identity Cloud deployment, one of the most important phases of the planning process is identity data object modeling. Learn more in [Plan for data object modeling](../planning/plan-object-modeling.html).

- Advanced Identity Cloud has two main services: Access Management (AM) and Identity Management (IDM). It's important to note that these services use different conventions for the same managed identity attributes. Learn more in [User identity attributes and properties reference](../identities/user-identity-properties-attributes-reference.html). |

### Applications

In Advanced Identity Cloud, an *application* is a connection to an external application that you manage. You can configure an application for user provisioning or single sign-on (SSO):

* User provisioning automates the creation and management of user accounts in external applications. For example, when a new employee is created in Advanced Identity Cloud, an account is automatically created for them in a target application, such as Workday or Salesforce.

* SSO lets end users access external applications using their Advanced Identity Cloud credentials, through standard protocols such as OpenID Connect (OIDC), SAML, or WS-Federation.

Learn more in [Application management](../app-management/applications.html).

### Identity synchronization

With identity synchronization, you connect Advanced Identity Cloud to your existing user datastores, such as an on-premises LDAP directory or a database, to synchronize identities. This lets you keep user profiles consistent across systems, migrate users into the platform, or provision accounts to downstream applications.

Learn more in:

* [Sync identities with an external resource](../identities/sync-identities.html).

* On-demand training: [Explain identity synchronization](https://backstage.pingidentity.com/university/on-demand/course/TGVhcm5pbmdQYXRoOjk4/module/Q291cnNlOjI0Nzky/chapter/Q29udGVudDo0Mzcx/play/Q29udGVudDo0Mzg4) (10.40 minutes)

### Email providers

*Email providers* in Advanced Identity Cloud are services that handle sending emails on behalf of your tenant. These emails are for critical user interactions, such as completing a registration or resetting a forgotten password.

To help you get started, your tenant includes a built-in email service. This lets you quickly create and test email-dependent journeys in your development tenant environment.

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | Before you go live, you must configure Advanced Identity Cloud to use your organization's own email provider. |

Learn more in [Email provider](../tenants/email-provider.html).

***

[1](#_footnoteref_1). A [sandbox environment](../tenants/environments-sandbox.html) is an [add-on capability](../product-information/add-on-capabilities.html).[2](#_footnoteref_2). A [user acceptance testing (UAT) environment](../tenants/environments-uat.html) is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: PingOne Advanced Identity Cloud
description: Learn what Advanced Identity Cloud is and its core capabilities for managing identities across workforce, consumer, and B2B use cases
component: pingoneaic
page_id: pingoneaic:getting-started:overview
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/overview.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud"]
---

# PingOne Advanced Identity Cloud

PingOne Advanced Identity Cloud is a SaaS-based digital identity and access management (IAM) solution designed for workforce, consumer, and B2B identities. Ping Identity handles the deployment, management, upgrades, and monitoring of the platform's various software components, ensuring a seamless and secure experience.

With Advanced Identity Cloud, you can manage the complete lifecycle of identities including:

* Flexible and extensible [user journeys](../journeys/journeys.html)

* [Application management](../app-management/applications.html)

* [Identity management](../identities/manage-identities.html)

* [Implement SSO and SLO](../am-saml2/saml2-sso-slo.html)

* Real-time [identity synchronization](../identities/sync-identities.html#about_identity_cloud_connectors) between cloud and on premises

* [Policy enforcement](https://docs.pingidentity.com/pinggateway/latest/gateway-guide/policy-enforcement.html) using PingGateway

* [Device-profiling authentication](../solution-configure-device-profiling.html) in user journeys using Ping SDKs

And much more...

---

---
title: Start here
description: Start with the foundational getting started guide covering key tasks from tenant access to OIDC application integration
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
page_aliases: ["pingoneaic::landing-getting-started.adoc"]
---

# Start here

[icon: circle-info, set=far, size=3x]

#### [About the getting started guide](getting-started-about.html)

Understand the purpose and structure of this guide

[icon: memo-circle-info, set=far, size=3x]

#### [Key concepts](getting-started-concepts.html)

Learn about key Advanced Identity Cloud concepts

[icon: circle-question, set=far, size=3x]

#### [Getting help](getting-started-help.html)

Get help with Advanced Identity Cloud

[icon: arrow-right-to-bracket, set=far, size=3x]

#### [Task 1: Get access to your tenant](getting-started-access-tenant.html)

Get access to your Advanced Identity Cloud tenant

[icon: desktop, set=far, size=3x]

#### [Task 2: Explore the platform](getting-started-explore-platform.html)

Explore the Advanced Identity Cloud consoles

[icon: users, set=far, size=3x]

#### [Task 3: Add end users](getting-started-create-users.html)

Add your first end users

[icon: circle-user-circle-plus, set=far, size=3x]

#### [Task 4: Design self-registration experiences](getting-started-self-registration.html)

Enable users to sign up to applications and services

[icon: user-key, set=far, size=3x]

#### [Task 5: Design user authentication experiences](getting-started-authentication.html)

Enable users to authenticate to applications and services

[icon: unlock, set=far, size=3x]

#### [Task 6: Enable customer account recovery](getting-started-account-recovery.html)

Enable users to recover their accounts

[icon: circle-user, set=far, size=3x]

#### [Task 7: Enable customer profile management](getting-started-profile-management.html)

Enable users to manage their profiles

[icon: palette, set=far, size=3x]

#### [Task 8: Add basic branding](getting-started-branding.html)

Add basic branding to your end user screens

[icon: file-shield, set=far, size=3x]

#### [Task 9: Integrate an OIDC application](getting-started-oidc-app.html)

Integrate an OpenID Connect (OIDC) application for single sign-on (SSO)

[icon: plane-departure, set=far, size=3x]

#### [Task 10: Next steps](getting-started-next-steps.html)

Get going with Advanced Identity Cloud

---

---
title: "Task 1: Get access to your tenant"
description: Register and access your Advanced Identity Cloud tenant as a super administrator or invited tenant administrator
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-access-tenant
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-access-tenant.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  gs-register-first-super-admin: Register as the first super administrator
  gs-invite-other-admins: Invite other administrators
  gs-register-invited-admin: Register as an invited administrator
  gs-sign-in-admin: Sign on as an administrator
---

# Task 1: Get access to your tenant

This task guides you through the process of accessing your Advanced Identity Cloud tenant, either as the initial super administrator for your organization or as an administrator invited by a super administrator.

## Register as the first super administrator

After your organization purchases Advanced Identity Cloud and requests a tenant, Ping Identity prepares the tenant for initial use. It then sends a registration email to the person designated as the super administrator in your organization. You'll receive a separate email for each tenant environment.

To register as the first super administrator:

1. In the registration email from Ping Identity, click Start Registration.

2. On the Welcome to PingOne Advanced Identity Cloud page, click Send Verification Code.

3. Check your email for a message from Ping Identity containing your one-time verification code.

4. On the Admin Invite Code page, enter your 6-digit verification code, and click Next.

5. On the Register Your Account page, enter your first name, last name, and a password, then click Next.

6. Choose a country of residency, accept Ping Identity's privacy policy, and click Next.

7. Click Set Up and follow the instructions to register an MFA method to protect your account.

   |   |                                                                 |
   | - | --------------------------------------------------------------- |
   |   | When setting up MFA, store your recovery codes in a safe place. |

8. Authenticate with your chosen MFA method.

After successful authentication, you're signed on to the Advanced Identity Cloud admin console as a super administrator.

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you haven't received a registration email, contact your Ping Identity representative. |

## Invite other administrators

Only super administrators can invite other administrators.

Choose one of the following:

* To give administrator access to a group of administrators in another identity provider (IdP), set up federated access. Learn more in [Configure federated access for tenant administrators](../federation/configure-federated-access-for-tenant-administrators.html).

* To invite other administrators manually:

  1. In the Advanced Identity Cloud admin console, open the Tenant menu (upper right).

     ![Advanced Identity Cloud tenant menu](../tenants/_images/tenant-menu.png)

  2. Click Invite admins.

  3. In the Invite Admins modal, enter the email addresses of the people you want to invite.

     ![Invite admins modal](_images/invite-admins.png)

  4. Select the administrator role to grant them either Super Admin or Tenant Admin access.

  5. Click Send Invitations.

     Advanced Identity Cloud sends an email to each address, containing instructions to set up an administrator account.

  6. Click Done to return to the tenant administrators list.

## Register as an invited administrator

If you've been invited as a tenant administrator, you'll receive an email with the subject `Complete your Ping Identity Advanced Identity Cloud registration`.

1. In the registration email, click Start Registration.

2. On the Welcome to PingOne Advanced Identity Cloud page, click Send Verification Code.

3. Check your email for a message from Ping Identity containing your one-time verification code.

4. On the Admin Invite Code page, enter your 6-digit verification code and click Next.

5. On the Register Your Account page, enter your first name, last name, and a password, then click Next.

6. Choose a country of residency, accept Ping Identity's privacy policy, and click Next.

7. Click Set Up and follow the instructions to register a multi-factor authentication (MFA) method to protect your account.

   |   |                                                                 |
   | - | --------------------------------------------------------------- |
   |   | When setting up MFA, store your recovery codes in a safe place. |

8. Authenticate with your chosen MFA method.

After successful authentication, you're signed on to the Advanced Identity Cloud admin console as an administrator.

![Advanced Identity Cloud dashboard](_images/aic-dashboard-empty.png)

|   |                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you first sign on, your username defaults to your email address. You can edit your profile settings, including your username, from the TENANT menu (upper right). Learn more in [Edit your own tenant administrator profile](../tenants/tenant-administrator-settings.html#edit-your-own-tenant-administrator-profile). |

## Sign on as an administrator

After you've registered, use these steps any time to sign on to the Advanced Identity Cloud admin console.

1. In a [supported web browser](../product-information/supported-browsers.html), go to the following URL:

   `https://<tenant-env-fqdn>/login/admin`

   For example, if your [tenant environment FQDN](../tenants/environments.html#tenant-environment-fqdns) is `openam-mycompany-ew2.id.forgerock.io`, use the URL `https://openam-mycompany-ew2.id.forgerock.io/login/admin`.

2. Enter your email address and password.

3. Click Next.

4. Authenticate with your chosen MFA method.

After successful authentication, you're signed on to the Advanced Identity Cloud admin console.

---

---
title: "Task 2: Explore the platform"
description: Explore the three administrative consoles that help you manage your Advanced Identity Cloud tenant and understand their primary functions
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-explore-platform
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-explore-platform.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  ges-platform-main-console: Advanced Identity Cloud admin console
  find_the_release_version_and_release_notes: Find the release version and release notes
  gs-platform-native-consoles: Native admin consoles
  am_admin_ui_native_console: AM admin UI (native console)
  idm_native_admin_console: IDM native admin console
---

# Task 2: Explore the platform

Advanced Identity Cloud provides three administrative consoles to help you manage your tenant. Take some time to explore these consoles and understand their primary functions.

![Overview of the three admin consoles](_images/aic-admin-consoles.png)

1. a Advanced Identity Cloud admin console

2. b AM admin UI (native console)

3. c IDM admin console

|   |                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | While the administration consoles are ideal for many tasks, you can also manage your tenant using REST APIs. Learn more in [Advanced Identity Cloud API reference](../developer-docs/api-reference.html). |

Learn more about the Advanced Identity Cloud admin consoles in this demo: [Demo: Navigate the Advanced Identity Cloud Admin UI](https://backstage.pingidentity.com/university/on-demand/course/TGVhcm5pbmdQYXRoOjk4/module/Q291cnNlOjI0Nzky/chapter/Q29udGVudDo0Mzcx/play/Q29udGVudDo0Mzc1) (10.33 minutes)

## Advanced Identity Cloud admin console

This is the primary console, designed to handle most day-to-day tasks associated with managing your tenant. Use the Advanced Identity Cloud admin console to manage all aspects of your tenant including realms, identities, applications, user journeys, and password policy.

> **Collapse: Summary of tasks you can perform in the Advanced Identity Cloud admin console**
>
> | Task type                               | Example tasks                                                                                                                                                                                                                                                                                             |
> | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | Tenant administration and configuration | * Invite administrators.
>
> * Set up federated access to the tenant.
>
> * Manage global settings, such as:
>
>   * Cross-Origin Resource Sharing (CORS)
>
>   * Environment Secrets & Variables (ESVs)
>
>   * Log API keys
>
>   * Service accounts
>
>   * Content Security Policy (CSP)
>
>   * Outbound static IP addresses |
> | Monitoring and reporting                | - View system usage on an analytics dashboard.
>
> - Run basic reports, monitor jobs, and view audit logs.                                                                                                                                                                                                   |
> | Identity configuration                  | * Manage object types (managed objects) and their properties.
>
> * Manage relationships between managed object types.                                                                                                                                                                                       |
> | Identity management                     | - Manage end-user profiles and accounts.
>
> - Manage security options such as password policies for end users.
>
> - Set up terms and conditions for end users.                                                                                                                                                |
> | Application and access management       | * Register and manage applications and OAuth 2.0 clients.
>
> * Manage gateways and agents for connecting to your resources.                                                                                                                                                                                 |
> | End-user experience and journeys        | - Create authentication and self-service journeys.
>
> - Set up and brand hosted pages.
>
> - Customize email templates for user communication.                                                                                                                                                                 |
> | Automation and extensibility            | * Create scripts to customize platform behavior.
>
> * Create event hooks to trigger external workflows.                                                                                                                                                                                                     |

### Find the release version and release notes

To check the release version and view the latest release notes:

1. In Advanced Identity Cloud admin console, scroll to the page footer and click the release version. For example, PingOne Advanced Identity Cloud 19573.0. The Tenant Settings page opens.

2. On the Tenant Settings > Details tab, click Release Notes to display the release notes for the latest version.

   ![View release notes](_images/tenant-settings-rel-notes.png)

|   |                                                                                             |
| - | ------------------------------------------------------------------------------------------- |
|   | The Tenant Settings page displays a banner showing the next scheduled regular release date. |

## Native admin consoles

These are secondary consoles, intended for specialist tasks when configuring access management (AM) and identity management (IDM). They let you access functionality not yet available in the Advanced Identity Cloud admin console.

You don't need separate credentials to access these consoles. If you're signed onto the Advanced Identity Cloud admin console, you can seamlessly switch from one console to another.

### AM admin UI (native console)

Use the AM admin UI (native console) to configure advanced access and security features needed for your identity solution.

> **Collapse: Summary of tasks you can perform in the AM admin UI (native console)**
>
> | Task type                                | Description                                                                                                                                                                 |
> | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | SAML 2.0 configuration                   | While you can create basic SAML applications in the main admin console, use the native console for deeper SAML entity configuration.                                        |
> | Advanced authorization policy management | Configure detailed validation policies.                                                                                                                                     |
> | Advanced realm services                  | Configure low-level, realm-specific services, such as advanced OAuth 2.0 provider settings and realm-specific session policies.                                             |
> | Secret store mapping                     | Map secrets stored in the ESVs to the underlying access management configuration, when integrating with other Ping Identity components or services such as PingOne Protect. |

To open the AM admin UI (native console):

* In the Advanced Identity Cloud admin console, click Native Consoles > Access Management.

### IDM native admin console

Use the IDM native admin console for advanced data modeling, synchronization setup, and resource connection configuration.

> **Collapse: Summary of tasks you can perform in the IDM native admin console**
>
> | Task type         | Description                                                                                                                                                                                                                                                                                                                 |
> | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | Identity modeling | Configure managed objects and policy enforcement.	The Advanced Identity Cloud admin console is the recommended console for configuring managed objects. The IDM native admin console has limited functionality and doesn't support features such as relationship fields and enums. Learn more in Configure managed objects. |
> | Sync/provisioning | Configure connectors (connection details, complex attribute mapping, data transformation scripts).                                                                                                                                                                                                                          |

To open the IDM native admin console:

* In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

---

---
title: "Task 3: Add end users"
description: Add end users to your system through manual creation, self-registration, bulk import, API calls, or identity synchronization
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-create-users
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-create-users.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  gs-add-users: Methods for adding end users
  gs-manual-create-user: Manually create a test end user
  gs-create-additional-users: Best practices and next steps
---

# Task 3: Add end users

End users are the identities that interact with your applications, such as your customers or employees. They are distinct from the administrator users who manage the tenant configuration.

## Methods for adding end users

There are several methods for adding end users in Advanced Identity Cloud, depending on your use case. Familiarize yourself with these methods.

| Method                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use case                                                                          |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| User self-registration                    | Let end users create their own accounts through a registration journey.Learn more in [User self-registration](../self-service/self-registration.html).                                                                                                                                                                                                                                                                                                                                                                                                 | Customer-facing applications where end users sign up for a service.               |
| Manual creation by a tenant administrator | Manually create individual end user accounts directly within the Advanced Identity Cloud admin consoleLearn more in [Manage identities](../identities/manage-identities.html).                                                                                                                                                                                                                                                                                                                                                                         | Add a small number of end users or add end users for testing.                     |
| Bulk import                               | Import many end users into the platform, typically using a file-based process, for example, a CSV file.Learn more in [Bulk import identities](../identities/bulk-import-identities.html).                                                                                                                                                                                                                                                                                                                                                              | Large-scale initial onboarding or migrating end users from a legacy system.       |
| API calls                                 | Use the Advanced Identity Cloud API to programmatically add end users.Learn more in [Managed users](../idm-rest-api/endpoints/rest-managed-users.html).                                                                                                                                                                                                                                                                                                                                                                                                | Integrate end user creation into a custom application, script, or workflow.       |
| Identity synchronization and provisioning | Synchronize end users from an external identity source, such as an LDAP directory, Active Directory, or another IdP.For common workforce applications, such as Salesforce or Workday, you can create a provisioning application for synchronization and provisioning. Learn more in [Application management](../app-management/applications.html).Other external identity provisioning requires connector configuration. Learn more in [About Advanced Identity Cloud connectors](../identities/sync-identities.html#about_identity_cloud_connectors). | Enterprise environments that manage end user identities in an existing directory. |

## Manually create a test end user

This task demonstrates how to add an end user in the Advanced Identity Cloud admin console. Although you're unlikely to add end users in this way, other than for testing purposes, it demonstrates how to get your first end user in the system.

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage.

   ![Add new user](../use-cases/_images/test-users-and-roles/create-user.png)

2. On the Manage Identities page, click + Alpha realm - Users and New Alpha realm - User.

3. On the New Alpha realm - User page, enter the following information for the end user, and then click Save:

   | Field         | Value                    |
   | ------------- | ------------------------ |
   | Username      | `acruse`                 |
   | First Name    | `Alex`                   |
   | Last Name     | `Cruse`                  |
   | Email Address | `alex.cruse@example.com` |
   | Password      | `Secret12!`              |

You now have your first end user in your Alpha realm.

![New user created in Manage Identities page](_images/manage-identities.png)

## Best practices and next steps

Adding end users is just the first step. To build a secure and user-friendly identity solution, consider these common next steps for managing your end users:

* **Grant access control**: Manage user access through roles, groups, and assignments. This implements the principle of least privilege, ensuring users can only access the applications and data appropriate for their job function. Learn more in [Manage identities](../identities/manage-identities.html "Opens in a new tab"), [Roles and assignments](../identities/roles-assignments.html "Opens in a new tab"), and [Groups](../idm-objects/groups.html "Opens in a new tab").

* **Force password changes**: Ensure end users created with temporary passwords (for example, through bulk import) are forced to change them on initial sign-on. This critical security step transfers ownership of the credential from the administrator to the end user, eliminating the risk of a shared or known temporary password being compromised. Learn more in [Password reset](../self-service/password-reset.html "Opens in a new tab").

* **Enforce password policies**: Create password policies to enforce password strength and complexity requirements for all end users. Enforcing strong policies makes accounts significantly more resistant to brute-force attacks, protecting both the user and your systems. Learn more in [Password policy](../realms/password-policy.html "Opens in a new tab").

* **Verify accounts**: For users created without immediate verification, for example through an import, trigger a verification flow (often part of a journey) to confirm the user owns the contact information associated with their account. This is crucial for enabling self-service account recovery and ensuring that security notifications are delivered to the correct person. Learn more in [Multi-factor authentication (MFA)](../am-authentication/authn-mfa.html "Opens in a new tab").

* **Enforce multi-factor authentication (MFA)**: Secure user accounts by creating journeys that require users to enroll an [MFA method](../am-authentication/authn-mfa.html), such as the PingID app or SMS, on their first sign-on. MFA adds a critical second layer of security, ensuring that an attacker can't access the account without the user's physical device.

* **Provision to target applications**: Map end users to their correct target applications. If your applications have provisioning enabled, verify that the end-user account is created or updated in the target application (such as Salesforce or an HR system). Automating this process ensures users have immediate access to the tools they need on their first day and that their access is instantly revoked across all systems when they leave the organization. Learn more in [Application management](../app-management/applications.html "Opens in a new tab").

---

---
title: "Task 4: Design user self-registration experiences"
description: Create a self-registration journey allowing end users to sign up for applications and services with email verification and custom attributes
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-self-registration
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-self-registration.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  gs-test-registration-default-journey: Test the default registration journey
  gs-adapt-registration-journey: Adapt the registration journey
  gs-duplicate-registration-steps: Duplicate the journey
  gs-modify-registration-journey: Modify the journey
  gs-test-adapted-registration-journey: Test the adapted journey
  gs-registration-best-practices: Best practices and next steps
---

# Task 4: Design user self-registration experiences

Advanced Identity Cloud includes a preconfigured default [registration journey](../self-service/self-registration.html) that lets end users create their own account for an app or service. Although this provides a functional starting point, most real-world implementations require additional customization.

This task guides you through adapting the default journey to create a more robust and user-friendly flow. You'll test the default journey, then modify it to include common features, such as prompting for a password only after email verification and sending a welcome email to new users.

The [Best practices and next steps](#gs-registration-best-practices) section then offers guidance and resources for enhancing these experiences after you've mastered the basics.

## Test the default registration journey

To preview the default journey and register a new end user:

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys and click the Registration journey.

2. Click the ellipsis icon ([icon: ellipsis-h, set=fa]) and select Edit to view the journey.

   ![Registration journey](_images/user-registration-journey-default.png)

   1. a Collects the username, user details, password, security questions (KBAs), and terms and conditions, and presents them on the same page.

   2. b Emails the end user so they can confirm their email address.

   3. c Creates the new end user in Advanced Identity Cloud.

   4. d Increments the successful login count property for the end user.

3. In the Preview URL field, click [icon: copy, set=material, size=inline] and paste the URL into an incognito window.

   |   |                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------- |
   |   | Use incognito mode for testing to avoid caching issues and so that no current sessions interfere with your test. |

   The Sign Up page opens.

   > **Collapse: Show the page**
   >
   > ![Sign up page](_images/sign-up-page-default.png)

4. On the Sign Up page, complete the fields and click Next.

   |   |                                                        |
   | - | ------------------------------------------------------ |
   |   | Ensure you enter an email address that you can access. |

   An email is sent to the email address you entered, with the subject `Register new account`.

5. Open the email and click the email verification link. This creates the new user account in Advanced Identity Cloud.

6. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage.

   The newly created end user is shown with the details you entered above.

## Adapt the registration journey

In this section, you'll modify the journey to:

* Remove the security questions (KBA) step.

* Prompt for a password after a verification email has been sent.

* Send a welcome email upon successful registration.

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | This task uses email templates for sending emails to end users. Learn more in [Email templates](../tenants/email-templates.html). |

### Duplicate the journey

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys.

2. On the Journeys page, click the ellipsis icon ([icon: ellipsis-h, set=fa]) for the `Registration` journey and select Duplicate.

3. In the Duplicate Journey modal, enter the following details:

   | Field           | Value                                    |
   | --------------- | ---------------------------------------- |
   | Name            | `User Registration`                      |
   | Identity Object | Alpha realm - Users `managed/alpha_user` |
   | Description     | `Updated user registration journey.`     |

4. Click Save.

   The journey editor opens displaying a visual workspace known as the *journey canvas*. This is where you'll arrange nodes to define the user registration experience.

### Modify the journey

1. In the journey editor, select the KBA Definition node in the Page Node and click the delete icon ([icon: delete, set=material, size=inline]) to delete this node.

   This removes the security questions from the registration process.

2. Select the Platform Password node in the Page Node and drag it out of the node on to the journey canvas.

3. Configure the following connections:

   * Connect the Email Suspend Node outcome to the Platform Password node input.

   * Connect the Platform Password node outcome to the Create Object node input.

4. In the Filter nodes field in the upper left, search for the Email Template Node and drag it on to the journey canvas.

   The Email Template Node sends a welcome email to the end user after they've registered.

   |   |                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------ |
   |   | Click the Email Template Node to review the default settings. The default email template is `welcome`. |

5. Configure the following connections:

   * Connect the *Created* outcome of the Create Object node outcome to the Email Template Node input.

   * Connect the *Email Sent* outcome of the Email Template Node to the Increment Login Count node.

   * Connect the *Email Not Sent* outcome of the Email Template Node to the Failure node.

     ![User registration journey](_images/user-registration-journey-updated.png)

   1. a Collects the username, user details, and terms and conditions, and presents them on the same page.

   2. b Emails the end user so they can confirm their email address.

   3. c After confirmation, collects the end user's password.

   4. d Creates the new end user in Advanced Identity Cloud.

   5. e Sends a welcome email to the end user.

   6. f Increments the successful login count property for the end user.

6. Click Save to save the journey.

|   |                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can [annotate journeys](../journeys/journeys.html#annotate-journeys) with comments and sticky notes to help explain the purpose of each node and the overall flow. |

### Test the adapted journey

Now that you've created a new user registration journey, you're ready to test it out.

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys and click on the `User Registration` journey you've just created.

2. In the Preview URL field, click [icon: copy, set=material, size=inline] and paste the URL into an incognito window.

   The Sign Up page opens.

   ![Sign up page](_images/sign-up-page.png)

3. Complete the fields and click Next.

   |   |                                                        |
   | - | ------------------------------------------------------ |
   |   | Ensure you enter an email address that you can access. |

   An email is sent to the email address you provided.

4. Open the email and click the email verification link.

5. Enter a password and click Next.

6. Check your email account and confirm you have received a welcome email with the subject `Your account has been created`.

7. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage.

The end user is displayed with the details you entered above.

## Best practices and next steps

To enhance security and reduce friction in the registration flow, consider these common enhancements when designing your registration journeys:

* **Identity verification**: For higher-security applications, integrate an identity verification service such as PingOne Verify to confirm that a user is who they claim to be by checking government issued ID. This is crucial for preventing fraud and meeting regulatory requirements (such as KYC) in banking and healthcare industries. Learn more in [Use PingOne Verify for identity verification and proofing capabilities](../integrations/pingone-verify.html "Opens in a new tab").

  |   |                                                                                                                                                                                                                   |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Advanced Identity Cloud also includes many third-party identity verification services using [marketplace nodes](../journeys/marketplace.html "Opens in a new tab"), which you can incorporate into your journeys. |

* **Progressive profiling**: Keep the initial registration form short and simple. Ask for additional user information later, such as when they sign on for a second time or access a specific service. By asking only for essential information upfront, you dramatically reduce friction and increase conversion rates. Learn more in [Progressive profile](../self-service/progressive-profile.html "Opens in a new tab").

* **Social registration**: Allow users to register with their existing social media accounts, such as Google or Facebook. This simplifies the sign-on process, reduces password fatigue, and can increase user adoption by using familiar credentials. Learn more in [Social authentication](../self-service/social-registration.html "Opens in a new tab").

---

---
title: "Task 5: Design user authentication experiences"
description: Design user authentication experiences with support for multi-factor authentication, social sign-on, and passwordless login
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-authentication
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-authentication.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  gstest-authentication-default-journey: Test the default login journey
  gs-authentication-best-practices: Best practices and next steps
---

# Task 5: Design user authentication experiences

Advanced Identity Cloud includes a preconfigured default [login journey](../self-service/login.html) that lets end users authenticate with a username and password. Although this provides a functional starting point, most real-world implementations require additional customization.

This task guides you through testing the default login journey to establish a baseline. The [Best practices and next steps](#gs-authentication-best-practices) section then offers guidance and resources for implementing more advanced features, such as multi-factor, social, and passwordless sign-on.

## Test the default login journey

To preview the default login journey and authenticate as an end user:

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys and click the default Login journey.

2. Click the ellipsis icon ([icon: ellipsis-h, set=fa]) and select Edit to view the journey.

   ![Login journey](_images/login-journey-default.png)

   1. a Collects the end user's username and password, and presents them on the same page.

   2. b Validates the username and password match an existing end user in the identity store.

   3. c Increments the successful login count property of the end user.

   4. d Tracks failed authentications. If the number of failed authentications is under a specified retry limit, the end user can attempt authentication again. Otherwise, the node forwards to the Account Lockout node to lock the end-user account.

   5. e Increments the successful login count property for the end user.

   6. f Sends the successfully authenticated end user through a separate [progressive profile journey](../self-service/progressive-profile.html).

3. In the Preview URL field, click [icon: copy, set=material, size=inline] and paste the URL into an incognito window.

   The Sign In page opens.

   ![End-user Sign in page](_images/user-sign-in-page.png)

   |   |                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The Sign In page provides links for users who need to create an account or have forgotten their username or password. These links open the journeys configured in the journey's Page Node. |

4. On the Sign In page, enter the username and password of one of the users you created in the previous tasks.

5. Click Next.

   You're signed on to the Advanced Identity Cloud end-user UI as the end user.

   ![Dashboard for signed-in end user](_images/end-user-dashboard.png)

## Best practices and next steps

To increase security in the authentication flow, consider these common enhancements when designing your authentication journeys:

* **Multi-factor authentication (MFA)**: Prompt end users to provide a second form of verification, such as a one-time passcode (OTP) from an authenticator app, a push notification, or a security key. This additional layer of security significantly reduces the risk of account compromise, even if a password is stolen or guessed. Learn more in [Multi-factor authentication](../am-authentication/authn-introduction-authn.html#about-mfa "Opens in a new tab").

* **Risk-based authentication and fraud detection with PingOne Protect**: Add risk-based authentication and fraud detection to your authentication journeys. This adaptive security approach evaluates the context of each authentication attempt (such as device, location, and behavior) to dynamically adjust the level of authentication required, enhancing security without compromising user experience. Learn more in [Use PingOne Protect for risk-based authentication and fraud detection](../integrations/pingone-protect.html "Opens in a new tab").

* **Social sign-on**: Let end users sign on with their existing accounts from providers such as Google or Facebook. This simplifies the sign-on process, reduces password fatigue, and can increase user adoption by using familiar credentials. Learn more in [Social authentication](../self-service/social-registration.html "Opens in a new tab").

* **Passwordless login**: Let end users sign on using biometrics (such as Face ID or a fingerprint) or by clicking a magic link sent to their email, removing the need for a password. This enhances and user convenience and security by eliminating password-related vulnerabilities. Learn more [MFA: Authenticate using a device with WebAuthn and passkeys](../am-authentication/authn-mfa-webauthn.html "Opens in a new tab") and [Suspend journey progress](../am-authentication/suspended-auth.html "Opens in a new tab").

  |   |                                                                                                                                                                                                       |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Advanced Identity Cloud also includes many third-party biometric services using [marketplace nodes](../journeys/marketplace.html "Opens in a new tab"), which you can incorporate into your journeys. |

Learn more about Advanced Identity Cloud authentication in [Introduction to authentication](../am-authentication/authn-introduction-authn.html "Opens in a new tab").

---

---
title: "Task 6: Design account recovery experiences"
description: Design account recovery experiences enabling users to reset passwords, recover usernames, unlock accounts, and recover lost MFA devices
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-account-recovery
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-account-recovery.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  gs-test-default-account-recovery-journey: Test the default reset password journey
  gs-test-username-recovery-journey: Test the default username recovery journey
  gs-account-unlock: Account unlock
  gs-mfa-device-recovery: MFA device recovery (lost device)
  gs-account-recovery-best-practices: Best practices and next steps
---

# Task 6: Design account recovery experiences

Designing effective account recovery experiences is crucial for user satisfaction and security. Advanced Identity Cloud provides several mechanisms to help end users recover access to their accounts.

This task guides you through common account recovery experiences:

* [Password reset](#gs-test-default-account-recovery-journey): For end users who've forgotten their password.

* [Username recovery](#gs-test-username-recovery-journey): For end users who've forgotten their username.

* [Account unlock](#gs-account-unlock): For end users whose accounts are locked after too many failed sign-on attempts.

* [MFA device recovery](#gs-mfa-device-recovery): For end users who've lost access to their registered multi-factor authentication (MFA) device.

The [Best practices and next steps](#gs-account-recovery-best-practices) section offers guidance and resources for enhancing these experiences after you've mastered the basics.

## Test the default reset password journey

Advanced Identity Cloud includes a preconfigured default [reset password](../self-service/password-reset.html) journey that lets the end user reset their password.

To preview the default journey and test it as an end user:

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys and click the ResetPassword journey.

2. Click the ellipsis icon ([icon: ellipsis-h, set=fa]) and select Edit to view the journey.

   ![ResetPassword journey](_images/reset-password-journey-default.png)

   1. a Collects the end user's email address.

   2. b Validates the email address matches an existing user identity in the Advanced Identity Cloud identity store.

   3. c Sends an email to the end user with a password reset link.

   4. d Collects the end user's new password and validates the new password against password policies.

   5. e Updates the end user's password in the identity store.

3. To test the user experience, open the default Login journey:

   1. Go back to the Journeys page.

   2. Select the Login (default) journey.

   3. In the Preview URL field, click [icon: copy, set=material, size=inline] and paste the URL into an incognito window.

4. On the Sign In page, click Forgot password?.

   ![Forgot password link on Sign In page](_images/end-user-sign-in-forgot-password.png)

   The Forgot password link initiates the default ResetPassword journey.

   ![Forgot Password page](_images/reset-password-enter-email.png)

5. On the Reset Password page, enter the end user's email address and click Next.

   |   |                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For this test to succeed, use an email address that belongs to an existing user in your tenant. You'll need to access this email account to receive the password reset link. |

   Advanced Identity Cloud checks if an account exists and sends a password reset link to the end user's registered email address.

6. Copy the Password reset link from the email and open it in an incognito browser window.

7. On the Reset Password page, enter a new password and click Next.

   ![Reset Password page](_images/reset-password.png)

   The password is successfully reset, and you're signed on to the Advanced Identity Cloud account pages as the end user.

## Test the default username recovery journey

Advanced Identity Cloud includes a preconfigured default [forgotten username](../self-service/username-recovery.html) journey that lets end users recover their accounts if they've forgotten their username.

To preview the default journey and test it as an end user:

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys and click the ForgottenUsername journey.

2. Click [icon: ellipsis-h, set=fa]and select Edit to view the journey.

   ![ForgottenUsername journey](_images/forgotten-username-journey-default.png)

   1. a Collects the end user's email address.

   2. b Validates the email address matches an existing end user in the Advanced Identity Cloud identity store.

   3. c Sends an email to the end user with their username and a sign-on link.

   4. d Initiates the **Login** journey to sign the user on.

   |   |                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Both **Identify Existing User** node *True* and *False* outcomes are mapped to the **Email Suspend** node to reduce potential data leakage. If the journey finds a matching user, the email includes their username and a link to resume the sign-on journey. |

3. To test the user experience, open the default Login journey:

   1. Go back to the Journeys page.

   2. Select the Login (default) journey.

   3. In the Preview URL field, click [icon: copy, set=material, size=inline] and paste the URL into an incognito window.

4. On the Sign In page, click Forgot username?.

   ![Forgot Username link on Sign In page](_images/end-user-sign-in-forgot-username.png)

   The Forgot Username link initiates the default **ForgottenUsername** journey.

   ![Forgot Username page](_images/forgotten-username-enter-email.png)

5. On the Forgotten Username page, enter the end user's email address and click Next.

   |   |                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For this test to succeed, use an email address that belongs to an existing user in your tenant. You'll need to access this email account to receive the recovery link. |

   Advanced Identity Cloud checks if an account exists and sends an email to the user's registered email address with their username and a sign-on link.

6. Copy the Click here to login link from the email and open it in an incognito browser window.

7. On the Sign In page, enter the username and password and click Next.

   You're signed on to the Advanced Identity Cloud hosted account pages as the end user.

## Account unlock

If an end user's account is locked after too many failed sign-on attempts, the recovery process will depend on how you configure account lockout. Advanced Identity Cloud supports two main types of lockout:

* **Duration lockout**: The account is locked for a specific time period (for example, 15 minutes). The end user must wait for this time to pass, after which the account automatically unlocks.

* **Persistent lockout** (default): The account is locked indefinitely and must be unlocked manually. This is the recommended setting. An account can be unlocked in two ways:

  * An administrator can manually unlock the account in the Advanced Identity Cloud admin console.

  * In some configurations, a user can unlock their own account by successfully completing the password reset process.

As a tenant administrator, you can fine-tune the lockout policy, such as the number of failed attempts allowed and the lockout duration, to match your organization's security requirements.

Learn more in [Account lockout](../am-authentication/account-lockout.html).

## MFA device recovery (lost device)

If a user loses access to a device used for MFA, they have several paths to recovery:

* **Using an alternative MFA method**: If the user has previously registered multiple MFA methods (for example, both an authenticator app and SMS), they can use an alternative method to authenticate and then register a new device or reset their existing registered devices.

* **Using a recovery code**: During MFA device registration, users are often prompted to save one-time recovery codes. They can use one of these codes in place of their MFA device to sign on.

* **Administrator assistance**: If a recovery code isn't an option, a tenant administrator might need to use the Advanced Identity Cloud API or console to manually reset the user's registered devices.

Learn more in [Recover after replacing a lost device](../am-authentication/authn-mfa-using-lost.html).

## Best practices and next steps

Consider the following best practices and enhancements when designing your account recovery experiences:

* **Secure recovery with step-up authentication**: Account recovery is a high-risk event. To reduce the risk of account takeover, consider adding step-up authentication to your recovery journeys. For example, after a user resets their password, you could require a second factor, such as a code from an authenticator app, before granting access. Learn more in [Multi-factor authentication](../am-authentication/authn-mfa.html "Opens in a new tab").

  You can also use risk-based signals to determine when step-up authentication is required. Services such as [PingOne Protect](../integrations/pingone-protect.html "Opens in a new tab") can evaluate contextual and behavioral signals during recovery and trigger additional verification only when risk is elevated, helping balance security and user experience.

* **Verify user identity with document and biometric checks**: For applications with higher assurance requirements, consider integrating an identity verification service such as [PingOne Verify](../integrations/pingone-verify.html "Opens in a new tab"). Identity verification can help confirm that a user is who they claim to be by validating government-issued identity documents and biometric data during recovery.

  |   |                                                                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Advanced Identity Cloud also includes many third-party identity verification services using [marketplace nodes](../journeys/marketplace.html "Opens in a new tab"), which you can incorporate in your journeys. |

* **Fine-tune account lockout policies**: Configure account lockout policies to align with your organization's security posture and risk tolerance. This includes defining the number of failed sign-on attempts allowed and whether accounts are locked for a fixed duration or indefinitely. Well-tuned lockout policies help prevent brute-force attacks while minimizing unnecessary user disruption. Learn more in [Configure account lockout](../am-authentication/account-lockout.html "Opens in a new tab").

* **Ensure high-quality recovery data**: The quality and integrity of your user data directly impacts the security and reliability of your recovery processes. Carefully consider which identifiers are used for account recovery and how they are managed. Wherever possible:

  * Enforce uniqueness for primary recovery identifiers, such as email addresses or mobile phone numbers.

  * Ensure recovery identifiers are verified (for example, through email or SMS confirmation) before they can be used.

  * Validate the format and quality of user data at the time of creation or update. For example, use policies to ensure a phone number is in a valid format or that a username meets specific criteria. Learn more in [Apply policies to managed objects](../idm-objects/configuring-default-policy.html "Opens in a new tab").

  * Define clear rules for handling identifier changes to reduce the risk of unauthorized account recovery.

  * Avoid relying on identifiers that might be shared across users unless additional verification steps are in place.

  Strong identifier management improves recovery reliability and reduces the risk of account takeover.

* **Enable recovery through SMS or voice**: Some users might prefer to recover their account using a mobile phone number. You can integrate with an SMS or voice provider and update your recovery journeys to send one-time passcodes (OTPs) through text message or voice call.

  Advanced Identity Cloud includes [marketplace nodes](../journeys/marketplace.html "Opens in a new tab") for third-party SMS and voice providers. You can also build your own custom integration using the [OTP SMS Sender](https://docs.pingidentity.com/auth-node-ref/latest/otp-sms-sender.html "Opens in a new tab") node.

* **Incorporate social identity recovery**: If your application supports social sign-on (such as Google or Facebook), consider allowing users to recover their accounts using these social identities. When doing so, ensure that appropriate risk controls and verification steps are in place. Learn more in [Social authentication](../self-service/social-registration.html "Opens in a new tab").

* **Customize email templates**: Customize the content and branding of the emails sent during password reset and username recovery. Consistent branding helps users recognize legitimate recovery messages and reduces the risk of phishing or social engineering attacks Learn more in [Email templates](../tenants/email-templates.html "Opens in a new tab").

* **Regularly review and update recovery processes**: As threats, regulations, and user expectations evolve, regularly review your account recovery journeys to ensure they remain secure, effective and user-friendly.

---

---
title: "Task 7: Design profile management experiences"
description: Enable end users to manage their profiles by updating personal information, changing passwords, and configuring profile settings
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-profile-management
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-profile-management.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  gs-update-personal-info: Test updating personal information
  gs-update-password-journey: Test the default update password journey
  gs-profile-management-settings: Profile management settings
  gs-profile-management-best-practices: Best practices and next steps
---

# Task 7: Design profile management experiences

Providing self-service profile management capabilities improves the end-user experience and reduces administrative overhead. With Advanced Identity Cloud, you can create self-service experiences that let end users update their personal information, change their passwords, and manage other profile settings.

This task guides you through three key aspects of profile management:

* [Update personal information](#gs-update-personal-info): End users can update their personal information after signing on.

* [Update password](#gs-update-password-journey): End users can update their passwords while signed on using an update password journey.

* [Manage profile settings](#gs-profile-management-settings): Tenant administrators can configure profile management settings to tailor the experience for your organization.

The [Best practices and next steps](#gs-profile-management-best-practices) section then offers guidance for customizing the experience after you've mastered the basics.

## Test updating personal information

End users can manage their profile information in the hosted account pages after they've signed on.

To test updating personal information:

1. In an incognito browser window, sign on to the Advanced Identity Cloud as an end user.

2. Click Profile to display the end user's profile information.

   ![End User Profile Page](_images/end-user-profile-page.png)

   |   |                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------ |
   |   | You'll see additional menu items on the left if you have the Identity Governance add-on feature. |

3. Click Edit personal info.

4. Update the end user's email, first name, last name and address.

5. Click Save to save the changes.

   The changes are saved to the end user's profile, and you're returned to the profile page.

## Test the default update password journey

Advanced Identity Cloud includes a preconfigured default [update password](../self-service/update-password.html) journey that lets end users update their passwords while signed on.

To preview the default journey and test it as an end user:

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys and click the UpdatePassword journey.

2. Click the ellipsis icon ([icon: ellipsis-h, set=fa]) and select Edit to view the journey.

   ![UpdatePassword journey](_images/update-password-journey-default.png)

   1. a Identifies the signed-on end user from their session

   2. b Verifies that the end-user's password is present.

   3. c Prompts the end user to enter their existing password.

   4. d Sends an email to the end user with a password reset link, if an existing password isn't present.

   5. e Validates the username and password match an existing user identity in the identity store.

   6. f Collects the end-user's new password and validates the new password against password policies.

   7. g Updates the end user's password in the identity store.

3. In an incognito browser window, sign on to the Advanced Identity Cloud as an end user.

4. Click Profile to display the end user's profile information.

5. On the Password row, click Reset.

   ![End User Profile Page with Reset Password link](_images/end-user-profile-page-reset.png)

   The Verify Existing Password page opens. This is the first step in the default **UpdatePassword** journey.

   ![Verify Existing Password page](_images/verify-existing-password.png)

6. Enter the end user's existing password and click Next.

   The Update Password page opens.

   ![Veryfy Existing Password page](_images/update-password.png)

7. Enter a new password.

8. Click Next.

   The new password is saved with the user's profile, and you're returned to the profile page.

## Profile management settings

As a tenant administrator, you can configure self-service settings to control which profile fields end users can view and edit in the hosted account pages. This lets you tailor the profile management experience to your organization's requirements.

Settings include:

* Enabling or disabling profile management features.

* Specifying which profile fields are editable by end users.

* Configuring validation rules for profile fields.

Learn more in [Configure visible information and end-user actions](../end-user/hosted-pages-customize.html#configure-visible-information-and-end-user-actions).

## Best practices and next steps

Consider the following best practices and enhancements when designing your end-user profile management experiences:

* **Configure which attributes are visible and editable**: This gives you granular control over your data. For example, you might want to display an `employeeId` but make it read-only. Learn more in [Configure actions and information for end users](../end-user/hosted-pages-customize.html#configure-actions-and-information-for-end-users "Opens in a new tab").

* **Add custom attributes to the user profile**: If your organization needs to store information not included in the default schema (such as a `department` or `location`), you can add custom attributes to the user profile. Once added, you can make it available on the profile page. Learn more in [Customize user identities](../identities/identity-cloud-identity-schema.html#customize-user-identities "Opens in a new tab").

* **Notify users of critical account changes**: This is a critical security measure against account takeover. After a sensitive change is completed (like a password change) use an `Email Template Node` in your journey to send a notification to the user. For an email address change, this notification should be sent to the **old** email address to alert the legitimate user of potentially fraudulent activity. Learn more in [Email templates](../tenants/email-templates.html "Opens in a new tab").

* **Continuously validate the user experience** Regularly review how users interact with profile and recovery flows using usability testing, accessibility checks and behavioural signals (such as drop-off points or repeated recovery attempts). Combine these insights with user feedback to inform and prioritize incremental improvements over time.

---

---
title: "Task 8: Apply basic branding to journey and account pages"
description: Apply basic branding including logos and colors to your end-user sign-on and account management pages
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-branding
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-branding.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  gs-branding-apply-basic-branding: Apply basic branding with a theme
  gs-branding-best-practices: Best practices and next steps
---

# Task 8: Apply basic branding to journey and account pages

A consistent and familiar user experience is key to building trust with your end users. When you integrate your applications with Advanced Identity Cloud, you can customize the user interface (UI) to match your organization's look and feel.

Advanced Identity Cloud provides several UI customization options:

* **Hosted pages**: Built-in sign-on and account management pages that you can brand using themes. Learn more in [Hosted pages](../end-user/hosted-pages.html).

* **REST APIs**: APIs that let you build a completely custom user interface for sign-on and account management. Learn more in [Advanced Identity Cloud REST API](../developer-docs/authenticate-to-rest-api-overview.html).

* **Ping SDKs**: Software Development Kits (SDKs) that simplify integration with your applications. Learn more in [Ping SDKs](../end-user/sdks.html).

* **Ping (ForgeRock) Login Widget** A widget that allows you to embed authentication journeys directly into your application. Learn more in [Ping (ForgeRock) Login Widget](https://docs.pingidentity.com/sdks/latest/login-widget/index.html).

These UI customization options aren't mutually exclusive, and you might need a combination of them to meet your requirements. Many companies build their own UIs with APIs or SDKs but also use the built-in hosted pages to quickly test use cases. You can find a comparison in [Compare end-user UX options](../end-user/end-user-ux-options-compare.html).

This task focuses on branding the built-in hosted pages to help you get started quickly. The [Best practices and next steps](#gs-branding-best-practices) section then offers guidance on how to enhance these experiences after you've mastered the basics.

## Apply basic branding with a theme

Themes let you customize the look and feel of Advanced Identity Cloud hosted journey and account pages, including the information presented to end users and the actions they can take.

To create your own theme:

1. In the Advanced Identity Cloud admin console, go to [icon: wysiwyg, set=material, size=inline] Hosted Pages.

   ![Hosted Pages page](_images/hosted-pages.png)

2. Click [icon: add, set=material, size=inline] New Theme.

3. In the New Theme modal, enter a name for the new theme (for example, `Getting Started theme`) and click Save.

   The Hosted Pages editor opens.

   ![Edit theme page](_images/edit-theme-page.png)

4. On the Global Settings > Styles tab, change the brand colors, typography, buttons, and links to match your organization's branding.

   |   |                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | From Global Settings, you can also:- Set a custom favicon for all journey and account pages on the Favicon tab.

   - Rename the theme and apply it to specific journeys on the Settings tab. |

5. Click Journey Pages and change the page background color to match your organization's branding, and add your organization's logo.

6. Click Account Pages and make the following changes:

   1. Change the navigation and page styles to match your organization's branding, and add your organization's logo.

   2. Under Profile Page, select and deselect the account controls you want your end users to access from their profile page.

      |   |                                                                                                                                                                                                                                                                        |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | End users can only view the information and take actions for the items you enable in the Profile Page. Learn more in [Configure visible information and end-user actions](../end-user/hosted-pages-customize.html#configure-visible-information-and-end-user-actions). |

7. Click Save.

8. Set the new theme as the default theme:

   1. Go back to [icon: wysiwyg, set=material, size=inline] Hosted Pages.

   2. Click the ellipsis icon ([icon: ellipsis-h, set=fa]) for the Getting Started theme and select Set as Realm Default.

9. In an incognito browser window, sign on to the Advanced Identity Cloud as an end user.

   The hosted sign-on page and account pages reflect the branding changes you made in the Getting Started theme.

Learn more in [Add a custom theme](../end-user/hosted-pages-customize.html#add-a-custom-theme).

## Best practices and next steps

Now that you've explored basic branding, consider these enhancements to create a more polished and professional user experience:

* **Apply themes to specific journeys**: This allows you to tailor the experience for different brands or applications within the same tenant. For example, you can apply distinct themes for each consumer brand while sharing the same underlying identity platform. Learn more in [Custom journeys](../journeys/journeys.html#custom-journey "Opens in a new tab").

* **Use a custom domain**: Using your own domain (like `login.mycompany.com`) instead of the default Ping Identity domain is crucial for building user trust and reinforcing your brand identity. Replace the default Ping Identity domain with your own branded domain for hosted pages. Learn more in [Configure customer-friendly domain names](../realms/custom-domains.html "Opens in a new tab").

* **Brand your email templates**: Customize your email templates to match the branding of your hosted pages for a consistent and trustworthy user journey. Learn more in [Email templates](../tenants/email-templates.html "Opens in a new tab").

* **Localize the user interface**: If you have users in different regions, you can provide a localized experience by creating language-specific versions of your hosted pages and themes. Learn more in [Localize hosted pages](../end-user/hosted-pages-localize.html "Opens in a new tab").

* **Preview your changes**: Before setting a theme as the default or assigning it to a production application, always preview it first. Remember to test different browsers, screen sizes, and user flows.

For greater control over the user experience:

* **Build custom UIs with REST APIs**: If the hosted pages don't meet your requirements, use the Advanced Identity Cloud REST APIs to build fully custom sign-on and account management experiences. Learn more in [Authenticate to Advanced Identity Cloud REST API](../developer-docs/authenticate-to-rest-api-overview.html "Opens in a new tab").

* **Integrate with SDKs**: Use platform-specific SDKs (JavaScript, iOS, Android) to embed authentication directly in your applications. Learn more in [Ping SDKs](../end-user/sdks.html "Opens in a new tab")

---

---
title: "Task 9: Integrate an OIDC application for SSO"
description: Integrate an OpenID Connect application with Advanced Identity Cloud to enable single sign-on without exposing user passwords
component: pingoneaic
page_id: pingoneaic:getting-started:getting-started-oidc-app
canonical_url: https://docs.pingidentity.com/pingoneaic/getting-started/getting-started-oidc-app.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "Getting started"]
section_ids:
  gs-oidc-configure-op: Configure Advanced Identity Cloud as an OpenID Provider
  gs-oidc-configure-app: Application configuration example
  gs-oidc-understand-auth-flow: Understand the authentication flow
  gs-oidc-integration-best-practices: Best practices and next steps
---

# Task 9: Integrate an OIDC application for SSO

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Unlike previous tasks, this is a conceptual walkthrough. It explains how to integrate an application, but you won't be required to configure a live application yourself. |

This task walks you through integrating an OpenID Connect (OIDC) application with Advanced Identity Cloud to enable single sign-on (SSO). By delegating authentication to Advanced Identity Cloud, you can secure your applications without building your own sign-on pages or managing passwords.

After an end user signs on through Advanced Identity Cloud, they can access all of your connected applications without re-entering their credentials. This trust is established using secure ID tokens (JWTs), which prove an end user's identity to your application without it ever handling a password.

In this task, you'll learn these integration skills:

* [Configuring Advanced Identity Cloud as an OpenID Provider](#gs-oidc-configure-op)

* [Examining an example application configuration](#gs-oidc-configure-app)

* [Understanding the authentication flow](#gs-oidc-understand-auth-flow)

The [Best practices and next steps](#gs-oidc-integration-best-practices) section offers guidance and resources for integrating OIDC apps in your production environments, after you've mastered the basics.

## Configure Advanced Identity Cloud as an OpenID Provider

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications > [icon: add, set=material, size=inline] Custom Application > OIDC - OpenId Connect > Web.

2. On the Application Details page, add the following configuration and click Next:

   | Field       | Value                                       |
   | ----------- | ------------------------------------------- |
   | Name        | `demo_oidc_app`                             |
   | Description | `Demo OIDC application for getting started` |
   | Owners      | Select an owner                             |

3. On the Web Settings page, add the following configuration, and then click Create Application:

   | Field         | Value                                        |
   | ------------- | -------------------------------------------- |
   | Client ID     | `demo_oidc_app`                              |
   | Client Secret | Enter a secure password for the application. |

4. Click the Sign On tab, add the following configuration and click Save:

   | Field        | Value                            |
   | ------------ | -------------------------------- |
   | Sign-in URLs | `http://localhost:3000/callback` |
   | Grant Types  | `Authorization Code`             |
   | Scopes       | `openid`, `profile`, `email`     |

5. Note the following values from your application configuration. You'll see how they're used in the next section:

   * Client ID: `demo_oidc_app`

   * Client Secret: The password you created

   * Authorization endpoint: `https://<tenant-env-fqdn>/am/oauth2/alpha/authorize`

   * Token endpoint: `https://<tenant-env-fqdn>/am/oauth2/alpha/access_token`

   * Userinfo endpoint: `https://<tenant-env-fqdn>/am/oauth2/alpha/userinfo`

## Application configuration example

|   |                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This task uses a demonstration application to show OIDC concepts. For production integrations, refer to the specific documentation for your application framework. |

The values you configured in Advanced Identity Cloud are used by your application developer to set up an OIDC client. While the exact code depends on the programming language, the concepts are universal. The client needs to know:

* Who is the authority? (`Issuer URL`)

* What application is this? (`Client ID` and `Client Secret`)

* Where should users be sent back to? (`Sign-in URL`, `callbackURL`)

The following is an example of how those values are used in a typical configuration for a Node.js application. This example is for illustration only.

```JavaScript
const clientID = process.env.OIDC_CLIENT_ID || 'demo_oidc_app';
const clientSecret = process.env.OIDC_CLIENT_SECRET; // Load from environment in production
const issuer = process.env.OIDC_ISSUER || 'https://<tenant-env-fqdn>/am/oauth2/alpha';

passport.use('oidc', new OidcStrategy({
  // By providing the issuer, the library can automatically discover the other endpoints
  issuer: issuer,
  clientID: clientID,
  clientSecret: clientSecret,
  callbackURL: 'http://localhost:3000/callback',
  scope: 'openid profile email',
  // Using PKCE is a security best practice, even for confidential web clients
  pkce: true,
  // The 'state' parameter is also a security best practice, enabled by default
  state: true
}, (issuer, profile, done) => {
  // In a real app, you would find or create an end user in your database here
  return done(null, profile);
}));
```

## Understand the authentication flow

With the application configured, the sign-on process follows the OAuth 2.0 authorization code flow. This is a secure sequence of redirects that establishes trust between the application and Advanced Identity Cloud.

![OIDC authentication flow](_images/oidc-flow.png)

1. 1 An end user clicks a sign-on button in the application.

2. 2 The application redirects the end user's browser to the Advanced Identity Cloud authorization endpoint.

3. 3 The end user signs on directly with Advanced Identity Cloud, which authenticates them and checks for consent. The application never sees the end user's password.

4. 4 After a successful sign-on, Advanced Identity Cloud redirects the end user back to the application's sign-in URL (`callbackURL`).

5. 5 The application browser provides a temporary, one-time-use authorization code to the backend server.

6. 6 The application's backend server securely sends the authorization code, along with its `Client ID` and `Client Secret`, to the Advanced Identity Cloud token endpoint.

7. 7 Advanced Identity Cloud validates the code and credentials, then returns a secure ID token to the application.

8. 8 The application validates the ID token's signature and claims, confirming the end user's identity.

9. 9 The application creates a session for the end user, completing the sign-on process.

This flow ensures that sensitive tokens are passed directly between servers and aren't exposed in the end user's browser, providing a high level of security.

## Best practices and next steps

Consider these best practices when integrating OIDC applications with Advanced Identity Cloud:

* **Validate ID tokens**: An ID token is a claim of identity, but it must be verified. Your application should always validate the token's signature, issuer, and audience (`aud`) claim. This is a critical security step to confirm the user's identity and ensure the token was issued by Advanced Identity Cloud and intended for your application. Learn more in [Token validation](../am-oidc1/rest-api-oidc-idtoken-validation.html#rest-api-oidc-idtoken-validation "Opens in a new tab").

* **Use PKCE for enhanced security (PKCE)**: PKCE is a security extension that prevents authorization code interception attacks. While it's mandatory for public clients like single-page applications (SPAs) and mobile apps, it's also a recommended best practice for confidential web applications as a security measure. Learn more in [PKCE](../am-oauth2/oauth2-authz-grant-pkce.html).

* **Implement logout**: To achieve single logout (SLO), the application should redirect the end user to the Advanced Identity Cloud OIDC `endSession` endpoint. This terminates their central session, ensuring they're also signed out of all other applications they accessed. Learn more in [Session management](../am-oidc1/session-management.html "Opens in a new tab").

* **Request custom scopes and claims**: The standard `openid`, `profile`, and `email` scopes are great for basic user information. For application-specific data (such as roles, permissions, or a department ID), you can create custom scopes and configure Advanced Identity Cloud to include corresponding custom claims in the ID token. Learn more in [OIDC claims](../am-oauth2/plugins-user-info-claims.html "Opens in a new tab").

* **Manage sessions with refresh tokens**: Access tokens are intentionally short lived to limit the damage if one is compromised. For an application to maintain access to a protected API without forcing the user to sign on again, it should use a *refresh token*. For example, if your application has a dashboard that automatically refreshes every 15 minutes by calling a secure API, the initial access token may expire. In that case, the application's backend can use a stored refresh token to silently get a new access token from Advanced Identity Cloud. Learn more in [Refresh tokens](../am-oauth2/oauth2-refresh-tokens.html "Opens in a new tab").
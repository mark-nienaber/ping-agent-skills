---
title: Introduction to PingOne
description: PingOne is a multi-tenant cloud-based identity as a service (IDaaS) platform for secure identity access management.
component: pingone
page_id: pingone:introduction_to_pingone:p1_introduction
canonical_url: https://docs.pingidentity.com/pingone/introduction_to_pingone/p1_introduction.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 18, 2024
section_ids:
  p1-organizations: Organizations
  p1-environments-intro: Environments
  environment-usage: Environment usage
  identities-and-source-environments: Identities and source environments
  p1-env-types: Sandbox and Production environments
  administrators-environment: Administrators environment
  environment-contents: Environment contents
  p1-admin-roles-perms-intro: Administrator roles and permissions
  p1-groups-pops-intro: Groups and populations
  p1-app-portal: PingOne application portal
  search-bar: Search bar
  favorites-and-all-applications: Favorites and All Applications
  user-control-panel: User control panel
  how-the-pingone-application-portal-works: How the PingOne application portal works
  showing-or-hiding-applications: Showing or hiding applications
  preview-the-pingone-application-portal: Preview the PingOne application portal
  p1-dashboards-intro: PingOne dashboards
  p1-solutions-main: PingOne Solutions
  p1-customer-solution: PingOne for Customers
  p1-b2b-solution: PingOne for B2B
  p1-workforce-solution: PingOne for Workforce
  agent_iam_core: Agent IAM Core
---

# Introduction to PingOne

PingOne is a multi-tenant cloud-based identity as a service (IDaaS) *(tooltip: \<div class="paragraph">
\<p>Cloud-based authentication solutions for identity and access management (IAM).\</p>
\</div>)* platform for secure identity access management. PingOne uses an organization-based model to define tenant accounts and their related entities within the platform.

To fully leverage the administrator capabilities of PingOne, familiarize yourself with the following key concepts.

## Organizations

In PingOne, the organization is the top-level identifier and defines your enterprise within the platform. Each organization contains one or more tenants, known as environments, which define separate working domains within an organization.

Each organization is based in a specific geography, such as North America (US) or Asia Pacific. All environment resources for the organization are hosted in this geography. You should have organizations in each of the geographies in which you operate. Learn more in the [IP address and domain reference](../developer_tools/p1_ip_address_domain_reference.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne is available worldwide. For optimum performance, use the PingOne geography closest to you.Some geographies span multiple sites and provide a multi-primary configuration, which means that multiple sites are active and available to serve requests. This architecture enables load balancing and limits system downtime.Examples throughout this documentation use URLs for the North America (US) geography. To view URLs for geographies other than North America (US), expand the **PingOne URLs by geography** table. |

> **Collapse: PingOne URLs by geography**
>
> | Geography                                                                                                                                                                                                                           | Admin console          | User self-service   | Management API endpoints | Authentication and authorization API endpoints |
> | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------- | ------------------------ | ---------------------------------------------- |
> | Australia                                                                                                                                                                                                                           | console.pingone.com.au | apps.pingone.com.au | api.pingone.com.au       | auth.pingone.com.au                            |
> | Canada                                                                                                                                                                                                                              | console.pingone.ca     | apps.pingone.ca     | api.pingone.ca           | auth.pingone.ca                                |
> | Europe                                                                                                                                                                                                                              | console.pingone.eu     | apps.pingone.eu     | api.pingone.eu           | auth.pingone.eu                                |
> | Singapore                                                                                                                                                                                                                           | console.pingone.sg     | apps.pingone.sg     | api.pingone.sg           | auth.pingone.sg                                |
> | Asia Pacific                                                                                                                                                                                                                        | console.pingone.asia   | apps.pingone.asia   | api.pingone.asia         | auth.pingone.asia                              |
> | In Asia Pacific, new organizations are registered under the pingone.com.au domain. Ping Identity also supports existing organizations registered under the pingone.asia domain. Both domains provide Australia-only data residency. |                        |                     |                          |                                                |

When an organization is created, an **Administrators** environment is created automatically. Learn more in [Environments](#p1-environments-intro).

![Diagram showing an organization that contains an Administrators environment and two additional environments. The environments include the resources they contain, such as applications, directory, identity providers, and so on.](_images/btq1723825050591.png)

After you create your organization, you can create the environments that meet the requirements of your business.

## Environments

In PingOne, tenants are called environments. Environments define separate working domains within an organization and contain assets such as your PingOne services and Ping Identity products, application connections, and user identities.

### Environment usage

There are many ways to use environments within an organization. If your company is made up of several different business units, you can use environments to define those units and ensure each one has access only to the assets that pertain to their business. For example, if you use PingOne for both customer and employee (workforce) use cases, you could have a Customer environment and an Employee environment. Those environments would include services, applications, and policies applicable only to those use cases.

You can also create Sandbox environments to deploy and test new features or configuration changes before releasing them to your Production environments.

After reviewing this section, learn more about creating environments in [Adding an environment](../settings/p1_addenvironment.html).

To access the **Environments** page, click the Ping Identity logo on the sidebar or the **Home** icon at the top of the admin console.

### Identities and source environments

In PingOne, every identity resides in a single source environment, which is the environment where the identity exists. For example, if you create an identity in the **Administrators** environment, then the **Administrators** environment is that identity's source environment.

In most cases, you should create all administrator identities in the **Administrators** environment to make it easier to manage them and to help prevent privilege escalation.

|   |                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Identities don't have to reside in the same environments to which they have access.End users and customers should reside in a separate environment from your administrator identities. |

In some scenarios, you might not have administrator access to the source environment for your identity (where your identity resides). In this case, your source environment is different from the environment you can work in, but you authenticate to your source environment.

Users with the Identity Data Admin role, for example, are the only users who can have access to their identity's source environment to manage other administrators and their roles. Administrators with other built-in roles assigned do not have access to their source environment.

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Different administrators can be assigned different roles that determine what they have access to and in where they have that access. You can find more details in [Administrator roles and permissions](#p1-admin-roles-perms-intro). |

### Sandbox and Production environments

When you create an environment, you can select **Sandbox** or **Production** for the environment type. Sandbox environments allow you to test configuration changes before you deploy them to production. Production environments are intended for live configurations that are deployed for real-world use. Both environment types count toward your license entitlements.

You can promote a Sandbox environment to Production, but Production environments can't be demoted to Sandbox. Learn more in [Promoting a Sandbox environment to Production](../settings/p1_promote_sandbox_environment_to_prod.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When you delete a Sandbox environment, the environment is removed immediately and can't be recovered. When you delete a Production environment, the environment is unusable and moved into a pending deletion status for 30 days. The environment is still listed on the **Environments** page and is recoverable within that 30-day period. Learn more in [Deleting an environment](../settings/p1_deleteenvironment.html).If you have a trial license, you can't create Production environments or promote Sandbox environments to production. |

|   |                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Don't use Sandbox environments for production activities. Production environments include deletion protection to safeguard important data. Learn more in [Deleting an environment](../settings/p1_deleteenvironment.html). |

### Administrators environment

An **Administrators** environment is created automatically when an organization is created in PingOne. You should create all administrators for the organization in the **Administrators** environment to keep them separate from your end users and to improve security.

By default, the **Administrators** environment includes the PingOne SSO and PingOne MFA services.

|   |                                                                              |
| - | ---------------------------------------------------------------------------- |
|   | Do not add other services or products to the **Administrators** environment. |

In PingOne, administrators don't need to belong to an environment to administer that environment. When you assign roles to your administrators, you can decide for which environments they have those roles. For some roles, you can limit the role scope to a particular population or application within the environment. Learn more in [Managing administrator roles](../getting_started_with_pingone/p1_manage_admin_roles.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Organizations created before July 1, 2020 might not include an administrator license or a dedicated administrators environment. However, you should still create and manage your PingOne administrator accounts in a single environment.If your **Administrators** environment was renamed, but is still assigned the ADMIN license, use that environment for storing administrator identities.If you do not have an administrator license, contact your Ping representative. Certain PingOne functionality is available only with an administrator license.Throughout this documentation, the **Administrators** environment refers to the environment in your organization that is assigned the ADMIN license. |

If your **Administrators** environment was created automatically when your organization was created, it has several restrictions to ensure that:

* You can't change the license assigned to the **Administrators** environment.

* You can't delete the **Administrators** environment.

### Environment contents

Environments encompass:

* PingOne services and other Ping product integrations

  PingOne services provide distinct, advanced capabilities in PingOne. Services are deployed at the environment level, and the services available to you depend on your PingOne license. PingOne services provide the following capabilities:

  * Single sign-on (SSO) with PingOne SSO: Allows users to use SSO to access all their applications and services with one set of credentials. Learn more in [PingOne SSO](../getting_started_with_pingone/p1_p1sso_start.html).

  * Strong authentication (MFA): Provides MFA with PingOne MFA for Customer environments, and PingID for Workforce environments. Learn more in [Strong Authentication (MFA)](../strong_authentication_mfa/p1_strong_authentication_start.html).

  * Threat protection with PingOne Protect: Prevents identity fraud by incorporating advanced features and real-time detection and enables customers to combat bad actors and address both password and MFA fatigue. Learn more in [Threat Protection using PingOne Protect](../threat_protection_using_pingone_protect/p1_protect_overview.html).

  * Identity verification with PingOne Verify: Enables secure user verification based on a government-issued document and live face capture (a selfie). Learn more in [Identity Verification using PingOne Verify](../identity_verification_using_pingone_verify/p1_verify_start.html).

  * Digital credentials with PingOne Credentials: Allows an issuer to create verifiable credentials that they can send to a compatible wallet app. Learn more in [Digital Credentials using PingOne Credentials](../digital_credentials_using_pingone_credentials/p1_credentials_start.html).

  * Authorization with PingOne Authorize: Controls what end users can see and do inside of applications and APIs. Learn more in [Authorization using PingOne Authorize](../authorization_using_pingone_authorize/p1az_overview.html).

Your environments can also be used to configure SSO to other Ping Identity products you use, such as PingFederate and PingOne Advanced Identity Cloud.

* Populations

  A population defines a set of users, similar to an organizational unit (OU). In a given environment, you can use populations to simplify the management of users. For example, you can create a population for similar types of users and apply a password policy to that population. You must create at least one population before you can create users. Learn more in [Populations](../directory/p1_populations.html).

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | An individual user can't belong to more than one population at the same time, but you can move a user to a different population. |

* Groups

  Groups are used to organize a collection of user identities and make it easier to manage access to applications. Groups offer more fine-grained access control than populations. A user can belong to multiple groups, but only one population. For example, you could use a population to contain all your employees and use a group to define subsets, such as Marketing, HR, Contractors, or US Employees. Learn more in [Groups](../directory/p1_groups.html).

* Users

  A user is a unique identity that interacts with the applications and services in the environment to which the user is assigned. An identity is the full representation of a user profile, including relationships, roles, and attributes. Users are associated with populations instead of being defined within a population. Learn more in [Users](../directory/p1_aboutusers.html).

* Applications

  Application resources define the connection between PingOne and the actual application, also known as a client connection. Connections to external resources use open standards protocols. Client connections define the configuration for OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
  \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
  \</div>)* and OAuth *(tooltip: \<div class="paragraph">
  \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
  \</div>)* clients.

Application grants describe which scopes the application can request. Scopes define the permissions for the application. Learn more in [Applications](../applications/p1_application_types.html) and [Editing an application](../applications/p1_editing_applications.html).

* Environment dashboard

  The environment dashboard is accessed by clicking **Overview** in the sidebar. This dashboard provides:

  * A list of the products and services included in the environment

  * A graph showing the activity that has occurred within the environment (if the environment contains PingOne services)

  * Links to documentation, APIs, and code examples for each product and service in the environment

![A screenshot of the environment dashboard showing sign-on activity and included services.](../_images/zla1676309052731.png)

* Activities

  Activities, or events, are collections of user-activity information, such as sign-on attempts, password reset attempts, and total active user counts. This audit data can be exported, reported on, or streamed out to customer SIEM (Security Information and Event Management) solutions. Learn more about auditing events and running audit reports in [Audit](../monitoring/p1_reporting.html).

* Branding and images

  User interface branding elements are defined in the branding resource. This resource contains configuration properties for customizable elements of the PingOne user interface. All end user interfaces are branded according to the theme defined in the branding resource. Learn more in [Branding and Themes](../user_experience/p1_branding_themes.html).

* Password policies

  Password policies define the strength and complexity requirements for a password for users within an environment. Learn more in [Password policies](../authentication/p1_passwordpolicies.html).

* Authentication policies

  Authentication policies dictate how the user's identity will be verified. For example, a single-factor authentication policy requires a single piece of evidence to verify a user's identity, such as a password. A multi-factor policy could require evidence to verify a user's identity, such as a TOTP authenticator app, FIDO2 biometrics, a push notification sent to the user's mobile device, or a one-time passcode (OTP) *(tooltip: \<div class="paragraph">
  \<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
  \</div>)* sent over SMS, voice, or email. Learn more in [Authentication policies](../authentication/p1_authenticationpolicies.html).

* Notification templates

  Notification templates are used to create messages that inform end users about certain events, such as device pairing and password resets. You can create templates for SMS, email, or voice messages. Learn more in [Notification Templates](../user_experience/p1_notifications.html).

* External identity providers

  External identity providers (IdPs) allow linked users to authenticate using the credentials provided by the external identity provider (IdP) *(tooltip: \<div class="paragraph">
  \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
  \</div>)*. An external IdP includes mapping PingOne user attributes to attributes from the IdP.

You can also use an external IdP to secure the PingOne admin console.

Learn more in [External IdPs](../integrations/p1_external_idps.html).

* Certificates and key pairs

  When you create a new environment, PingOne creates two default key pairs: one for signing and one for encryption. You can create additional certificate and key pairs as necessary for your environment. Learn more in [Certificates and key pairs](../settings/p1_certs_and_keypairs.html).

## Administrator roles and permissions

An administrator role is a collection of permissions that can be assigned to a user, application, or connection, and then applied to a level, or scope, within PingOne. The combination of the role permissions and the level at which the role is applied determines what an administrator can do (permissions) and where they can do it (level or scope).

In PingOne, roles can be applied to the organization, environment, population, or application level, although not all roles can be applied at all levels.

PingOne includes a number of built-in administrator roles. These roles are not hierarchical, and there is no super admin role that has permissions to perform every action at every level in PingOne. The roles available to your organization depend on your configuration and licensing.

|   |                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Add all of your PingOne administrators to the **Administrators** environment to keep them separate from end users and to improve security. Administrators do not have to belong to an environment to have administrator permissions over that environment. Learn more in [Environments](#p1-environments-intro). |

PingOne administrators can have multiple administrator identities across multiple environments in a single organization, a single administrator identity over multiple environments, or a combination of both. They can also have different roles that apply in those different contexts.

![A diagram showing an administrator with access to three environments: Administrators, Test, and Production. The Administrators environment is the source environment.](_images/lrm1669653236024.png)

For some complex use cases, you might need multiple administrator identities to configure multiple organizations. An example use case is a contractor working with more than one company to configure environments. In this scenario, the contractor would need an administrator identity in each company's organization. Similarly, if a company has organizations in multiple geographies, an administrator who needs to manage all of those organizations needs an identity in each organization.

|   |                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't have more than one instance of the same identity in a single environment. For these complex use cases, you must create those identities in multiple environments. |

If you have multiple administrator identities associated with the same email address, you can select which organization you want to authenticate to after signing on. You'll need to choose the identity with the right permissions based on the actions you intend to take.

![A diagram showing an administrator with two PingOne identities and the environments in each organization.](_images/pxq1668634964063.png)

Learn more about administrators and their roles in:

* [Managing administrators](../getting_started_with_pingone/p1_manage_administrators.html)

* [Managing administrator roles](../getting_started_with_pingone/p1_manage_admin_roles.html)

* [Environments](#p1-environments-intro)

* [Configuring roles for a worker application](../applications/p1_configurerolesforworkerapplication.html)

## Groups and populations

Groups and populations are both used to organize users, but they differ in several ways.

A user can belong to multiple groups, but only one population. A population is a fundamental organizational unit to which you can assign a particular sign-on policy and IdP, while groups offer more fine-grained control over user access to applications.

For example, you could create two populations in your environment. One population would contain all of your finance employees, and the other would contain your engineering and support staff. You can assign each of these populations a different sign-on policy, and can also set different IdPs for each.

Within each population, you can create groups to define subsets of the population. Although a user can belong to only one population at a time, they can belong to multiple groups. These groups can then be given access to different applications. For example, in your employee population, you might have groups for different departmental organizations such as Marketing, Engineering, and Payroll.

You can create groups at the population level or the environment level. A population-level group can contain users from that population only, but an environment-level group can contain users from different populations in the same environment. Administrators who are assigned roles scoped only to the population level can create groups for those populations only and cannot create groups at the environment level.

Key differences between groups and populations are summarized in the following table:

**Populations and Groups comparison**

| Populations                                                                                                                                                                                                                           | Groups                                                                                                                                                                                                                                                                                   | Both                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| * Users can belong to only one population

* You can assign a sign-on policy to a population

* You can assign an identity provider to a population

* You can create groups within a population to define subsets of that population | - Users can belong to more than one group

- Groups can contain users from more than one population

- Sign-on policies and identity providers can't be assigned to groups

- You can create groups within a population

- Groups allow fine-grained control over access to applications | * Populations and groups are defined at the environment level

* Administrator roles can be assigned to groups and populations |

On the **Groups** page, population-level groups include the name of the population under the group name.

Learn more in [Groups](../directory/p1_groups.html) and [Populations](../directory/p1_populations.html).

## PingOne application portal

The PingOne application portal is a unified interface that enables your users to use SSO to access the applications you've added for your organization.

![Screen capture of the PingOne application portal with sections numbered for reference.](_images/obj1697813224004.png)

PingOne application portal key sections:

1. Search bar

2. **Favorites** section

3. **All Applications** section

4. User avatar

5. User control panel

### Search bar

When you enter a search string, the search bar generates a list of the closest matches. Click the application row to launch the application directly from the results list.

### Favorites and All Applications

* Click an application icon to launch the application in a new browser tab.

* To add an application to favorites on the desktop version, drag it into the **Favorites** section.

* Hover over the application's icon to see its description. You can also click the star in the description to add or remove an application from favorites.

* To remove an application from favorites in the desktop version, drag it back to the **All Applications** section.

* In the desktop version, you can reorder application icons in the **Favorites** area by dragging and dropping them.

  |   |                                                    |
  | - | -------------------------------------------------- |
  |   | You can't reorder favorites in the mobile version. |

* To add an application to favorites in the mobile version, tap the **Star** on the application line, either on the **All Apps** tab or from the search bar.

* To remove an application from favorites in the mobile version, tap the **Pencil** icon, and then tap the **Star** on the line of the application that you want to remove. When you're finished, tap **Done**.

### User control panel

* Click the **User avatar** to access the **User control panel**.

* Click **Account** to access your PingOne profile. Learn more in [End users: Accessing your PingOne profile](../managing_your_pingone_user_profile/p1_signinselfservice.html).

* Click **Authentication** to manage your multi-factor authentication (MFA) devices.

* Click **Sign Off** to sign off of all applications and end your PingOne session.

### How the PingOne application portal works

The PingOne application portal grants users access to SAML and OpenID Connect applications. The applications that a user sees depend on the access controls for each application. Learn more about adding an application in [Adding an application](../applications/p1_applications_add_applications.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To make an OIDC application available on the PingOne application portal, the application must have an **Initiate Single Sign-on URL**. You can add this URL after creating the application by going to the **Configuration** tab and entering the URL into the **Initiate Login URI** field.Learn more in [Editing an application - OIDC](../applications/p1_edit_application_oidc.html). |

### Showing or hiding applications

Even if a user has access to an application, you can specify whether to include it in the application portal. For example, you could show or hide an application if the SSO flow is being triggered through means other than on the application portal. Learn more in [Application access control](../applications/p1_application_access_control.html) and [Editing an application](../applications/p1_editing_applications.html).

### Preview the PingOne application portal

1. In the PingOne admin console, go to **Applications > Applications**.

2. Click the **PingOne Application Portal** application.

3. Copy the **Home Page URL** and paste it into a new browser tab.

4. Enter a user's credentials in the **Username** and **Password** fields.

5. Click **Sign On**.

## PingOne dashboards

Administrators can use PingOne dashboards to view and monitor activities for a service.

Learn more about the information each dashboard provides in the following sections:

* [Overview page](../p1_overview_p1.html)

* [Authentication dashboard](../monitoring/p1_auth_dashboard.html)

* [Authorization Dashboard](../authorization_using_pingone_authorize/p1_az_dashboard.html)

* [Identity Verification Dashboard](../identity_verification_using_pingone_verify/p1_verify_monitoring.html#p1_verify_dashboard)

* [MFA dashboard](../monitoring/p1_mfa_dashboard.html)

* [Threat Protection Dashboard](../threat_protection_using_pingone_protect/p1_protect_dashboard.html)

* [User Demographics Dashboard](../monitoring/p1_user_demographic_dashboard.html)

## PingOne Solutions

PingOne uses PingOne Services to help solve a wide variety of identity problems.

PingOne Solutions packages are packages of PingOne Services designed to help you easily manage your organization's identity challenges by allowing you to choose the package that's right for you, whether your organization is small with basic requirements or large with a complex deployment.

PingOne for Customers, PingOne for B2B, and PingOne for Workforce packages are each available in two package tiers: Essential and Plus. You can add other PingOne Services to a package if your solution requires additional capabilities.

Every PingOne for Customers, PingOne for B2B, and PingOne for Workforce solution package lets you orchestrate Ping Identity products seamlessly using [PingOne DaVinci](https://docs.pingidentity.com/davinci/davinci_introduction.html). With DaVinci, you can rapidly build, test, and optimize identity experiences using a drag-and-drop interface and no-code orchestration to weave together Ping Identity services and capabilities.

We also offer solutions that combine DaVinci flows with PingOne and other tools to address complex business challenges. The PingOne for Customers Passwordless solution uses a set of tailored DaVinci flows to create a registration and sign-on process that incorporates passwordless, password, and MFA options.

Learn about PingOne Solutions packages and their included capabilities:

* [PingOne for Customers](#p1-customer-solution) is a cloud solution designed to improve customer experiences and meet business needs by combining no code orchestration with SSO and MFA authentication services.

* [PingOne for B2B](#p1-b2b-solution) is a cloud solution designed to improve the business-to-business experience and meet the needs of partners and customers by combining no code orchestration with SSO and multi-factor authentication (MFA) services.

* [PingOne for Workforce](#p1-workforce-solution) is a cloud-based solution that helps you orchestrate the experiences your work-anywhere employees need.

* [Agent IAM Core](#agent_iam_core) is a cloud solution combining artificial intelligence (AI) agent management with authentication, user management, and MFA services in a single package.

* PingOne Neo is a decentralized identity solution that gives control of identity data back to users. PingOne Neo empowers businesses to give their users full control over how they securely store and share verified credentials without unnecessary friction.

* [PingOne for Customers Passwordless](https://docs.pingidentity.com/pingone-solutions/pingone-customers-passwordless/index.html) lets you offer your end users a variety of flexible passwordless options for account creation, sign-on, profile management, and account recovery using a simple Getting Started experience and pre-built DaVinci flows.

### PingOne for Customers

PingOne for Customers is a cloud solution combining no-code orchestration with authentication, user management, and multi-factor authentication (MFA) services to meet business needs and improve customer experiences.

PingOne for Customers is available in two solution packages:

* Essential: Rapidly build identity experiences using no-code orchestration with authentication and user management.

* Plus: Enhance security with MFA alternatives to passwords to streamline the sign-on process.

Additional capabilities are available as add-ons based on your solution requirements. [Try PingOne](https://www.pingidentity.com/en/try-ping.html) today with a no-cost 30-day trial to see how your organization can leverage cloud-based identity solutions to meet your unique business needs.

The following table details the available solution packages, optional add-ons, and trial offerings:

**PingOne for Customers Solution Package Capabilities**

| Capability                          | Essential | Plus | Add-on | Trial |
| ----------------------------------- | --------- | ---- | ------ | ----- |
| Authentication and SSO              | Yes       | Yes  |        | Yes   |
| Directory                           | Yes       | Yes  |        | Yes   |
| Outbound Provisioning               | Yes       | Yes  |        | Yes   |
| Orchestration Starter Pack          | Yes       | Yes  |        |       |
| Connect to external LDAP            | Yes       | Yes  |        | Yes   |
| Multi-factor Authentication         |           | Yes  |        | Yes   |
| API Access Management               |           | Yes  |        |       |
| Advanced Access Security            |           |      | Yes    |       |
| Risk Management                     |           |      | Yes    | Yes   |
| Identity Verification               |           |      | Yes    | Yes   |
| Dynamic Authorization               |           |      | Yes    | Yes   |
| Fraud Detection                     |           |      | Yes    |       |
| Advanced Authorization              |           |      | Yes    |       |
| Additional Geographies/Environments |           |      | Yes    |       |

### PingOne for B2B

PingOne for B2B is a cloud solution combining no-code orchestration with authentication, user management, and multi-factor authentication (MFA) services to meet business-to-business needs and improve the security of your third-party access experiences.

PingOne for B2B is available in two solution packages:

* Essential: Rapidly build identity experiences using no-code orchestration with authentication and user management.

* Plus: Enhance security with MFA alternatives to passwords to streamline the sign-on process.

Additional capabilities are available as add-ons based on your solution requirements. [Try PingOne](https://www.pingidentity.com/en/try-ping.html) today with a no-cost 30-day trial to see how your organization can leverage cloud-based identity solutions to meet your unique business needs.

The following table details the available solution packages, optional add-ons, and trial offerings:

**PingOne for B2B Solution Package Capabilities**

| Capability                          | Essential | Plus | Add-on | Trial |
| ----------------------------------- | --------- | ---- | ------ | ----- |
| Authentication and SSO              | Yes       | Yes  |        | Yes   |
| Directory                           | Yes       | Yes  |        | Yes   |
| Outbound Provisioning               | Yes       | Yes  |        | Yes   |
| Orchestration Starter Pack          | Yes       | Yes  |        |       |
| Connect to external LDAP            | Yes       | Yes  |        | Yes   |
| Multi-factor Authentication         |           | Yes  |        | Yes   |
| API Access Management               |           | Yes  |        |       |
| Advanced Access Security            |           |      | Yes    |       |
| Risk Management                     |           |      | Yes    | Yes   |
| Identity Verification               |           |      | Yes    | Yes   |
| Dynamic Authorization               |           |      | Yes    | Yes   |
| Fraud Detection                     |           |      | Yes    |       |
| Advanced Authorization              |           |      | Yes    |       |
| Additional Geographies/Environments |           |      | Yes    |       |

### PingOne for Workforce

PingOne for Workforce is a cloud-based solution that helps you orchestrate the experiences your work-anywhere employees need.

Featuring identity intelligence, drag-and-drop workflows, passwordless sign-on, centralized authentication and a unified admin portal, PingOne for Workforce is available in two solution packages:

* Essential: Centralize single sign-on (SSO), Directory, and basic MFA for software as a service (SaaS) apps, and integrate with your Microsoft environment

* Plus: Create an LDAP connection to on-prem identity data, and enhance security and experience with intelligent, adaptive authentication

Additional capabilities are available as add-ons based on your solution requirements. [Try PingOne](https://www.pingidentity.com/en/try-ping.html) today with a no-cost 30-day trial and start delivering the seamless, secure experiences that your employees are looking for.

**PingOne for Workforce Solution Package Capabilities**

| Capability                                                                    | Essential | Plus | Add-on | Trial |
| ----------------------------------------------------------------------------- | --------- | ---- | ------ | ----- |
| Standards-based AuthN/SSO (OIDC/SAML)                                         | Yes       | Yes  |        | Yes   |
| Directory                                                                     | Yes       | Yes  |        | Yes   |
| Application Portal                                                            | Yes       | Yes  |        | Yes   |
| Outbound provisioning                                                         | Yes       | Yes  |        | Yes   |
| Application Catalog                                                           | Yes       | Yes  |        | Yes   |
| O365 with WS-Fed/WS-Trust                                                     | Yes       | Yes  |        | Yes   |
| Basic MFA                                                                     | Yes       | Yes  |        | Yes   |
| Inbound provisioning (SCIM, Workday, User onboarding through AD/LDAP Gateway) |           | Yes  |        | Yes   |
| Adaptive Multi-Factor Authentication                                          |           | Yes  |        | Yes   |
| Gateway - Integrate with AD/LDAP                                              |           | Yes  |        | Yes   |
| Orchestration Starter Pack                                                    | Yes       | Yes  |        |       |
| Advanced, including non-standards based, SSO                                  |           |      |        | Yes   |
| Risk Management                                                               |           |      |        | Yes   |
| Advanced Authorization                                                        |           |      | Yes    |       |
| Additional Geographies/Environments/Perf Reqs.                                |           |      |        | Yes   |

### Agent IAM Core

Agent IAM Core is a cloud solution that combines AI agent management with authentication, user management, and MFA services in a single package. In addition to enhanced MFA, it unlocks [AI agent capabilities](../ai_agents/p1_ai_agents.html) in PingOne for all environments associated with the license. Licensing is based on the number of human identities the agents act on behalf of and the number of configured agents.

For environments that aren't licensed for Agent IAM Core, you'll see an option to unlock AI agent capabilities by contacting Ping Identity Sales.

Additional capabilities are available as add-ons based on your solution requirements. [Try PingOne](https://www.pingidentity.com/en/try-ping.html) today with a no-cost 30-day trial to see how your organization can leverage cloud-based identity solutions to meet your unique business needs.

The following table details the included capabilities, optional add-ons, and trial offerings:

| Capability                          | Included? | Add-on | Trial |
| ----------------------------------- | --------- | ------ | ----- |
| AI Agents                           | Yes       |        | Yes   |
| Authentication and SSO              | Yes       |        | Yes   |
| Directory                           | Yes       |        | Yes   |
| Outbound Provisioning               | Yes       |        | Yes   |
| Orchestration Starter Pack          | Yes       |        |       |
| Connect to external LDAP            | Yes       |        | Yes   |
| Multi-factor Authentication         | Yes       |        | Yes   |
| API Access Management               | Yes       |        |       |
| Advanced Access Security            |           | Yes    |       |
| Risk Management                     |           | Yes    | Yes   |
| Identity Verification               |           | Yes    | Yes   |
| Dynamic Authorization               |           | Yes    | Yes   |
| Fraud Detection                     |           | Yes    |       |
| Advanced Authorization              |           | Yes    |       |
| Additional Geographies/Environments |           | Yes    |       |
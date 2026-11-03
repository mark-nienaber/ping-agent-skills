---
title: About the use case catalog
description: Discover administrator-focused use cases for configuring Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:use-cases:preface-pages/about-use-case-catalog
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/preface-pages/about-use-case-catalog.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Use Case"]
---

# About the use case catalog

The use case catalog contains administrator-focused use cases that explain how to configure PingOne Advanced Identity Cloud and select third-party products to meet your organizational needs.

---

---
title: Administration
description: Administer tenant settings and audit logs in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:use-cases:preface-pages/administration
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/preface-pages/administration.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Administration", "Use Case"]
---

# Administration

In PingOne Advanced Identity Cloud, tenant administrators can invite other tenant administrators, promote static configuration changes between environments, monitor their environments, read audit logs, or allow cross-domain service requests (CORS).

The use cases in this section focus on tenant-related administration activities.

| Use case                                                     | Description                                                                                                                            |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| [Set up administrators](../use-case-add-tenant-admins.html)  | Operate as a super administrator and run tasks to view the tenant settings and invite other administrators on Advanced Identity Cloud. |
| [Read audit logs using REST](../use-case-audit-logging.html) | Examine audit logs to investigate user behavior, and you use debug logs to investigate system behavior.                                |

---

---
title: Advanced Identity Cloud as a Temenos identity provider
description: Configure Advanced Identity Cloud as the Temenos identity provider for banking application authentication
component: pingoneaic
page_id: pingoneaic:use-cases:use-case-temenos
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/use-case-temenos.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 19, 2025
keywords: ["Advanced Identity Cloud", "Use Case"]
section_ids:
  temenos-goals: Goals
  temenos-process: What you'll do
  temenos-prerequisites: Before you begin
  temenos-tasks: Tasks
  temenos-task-1: "Task 1: Configure Advanced Identity Cloud as an OpenID Provider"
  temenos-task-2: "Task 2: Add Advanced Identity Cloud as an OAuth 2.0 identity service in Temenos"
  temenos-reference-material: Reference material
---

# Advanced Identity Cloud as a Temenos identity provider

Estimated time to complete: 30 minutes *(tooltip: This assumes you've already completed the prerequisites.)*.

This use case shows how Temenos can use Advanced Identity Cloud as an OpenID Provider (OP) to authenticate end users. Specifically, you set up Advanced Identity Cloud as an OAuth 2.0 identity service in Temenos Quantum Fabric.

Advanced Identity Cloud supports OAuth 2.0 and OpenID Connect (OIDC) natively, making it a good choice for integrating with Temenos and other standards-based applications.

## Goals

After completing this use case, you'll know how to do the following:

* Configure Advanced Identity Cloud as an OIDC identity provider

* Configure Temenos to use Advanced Identity Cloud as an OIDC identity provider

## What you'll do

* Create an OIDC application for Temenos.

* Configure a Temenos identity service to connect as the application to Advanced Identity Cloud.

## Before you begin

Before you start, make sure you have:

* A basic understanding of:

  * The Advanced Identity Cloud admin console and hosted pages

  * OAuth 2.0

  * OIDC

* Completed the [Create test users and roles](use-case-test-users-and-roles.html) use case

* Access to your test Advanced Identity Cloud environment as an administrator

* Access to a Temenos development environment as an administrator

## Tasks

|   |                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------- |
|   | This use case requires the use of third-party services. Use your environment-specific details where necessary. |

### Task 1: Configure Advanced Identity Cloud as an OpenID Provider

1. Sign on to the Advanced Identity Cloud admin console as an administrator.

2. Go to [icon: apps, set=material, size=inline] Applications > Applications > [icon: add, set=material, size=inline] Custom Application > OIDC - OpenId Connect > Web.

3. On the Application Details page, add a web application with the following configuration and click Next:

   | Field       | Value          |
   | ----------- | -------------- |
   | Name        | `temenos_oidc` |
   | Description | `Temenos OIDC` |
   | Owners      | `App Owner`    |

4. On the Web Settings page, add the following configuration, and then click Create Application:

   | Field         | Value                                                                                            |
   | ------------- | ------------------------------------------------------------------------------------------------ |
   | Client ID     | `temenos_oidc`                                                                                   |
   | Client Secret | Enter a password for the client. Remember the password because you need it to configure Temenos. |

   The Temenos OIDC client page opens.

5. On the Temenos OIDC client page, click the Sign On tab, add the following configuration and click Save:

   | Field        | Value                                                                                                  |
   | ------------ | ------------------------------------------------------------------------------------------------------ |
   | Sign-in URLs | `https://<accountID>.auth.konycloud.com/OAuth2/Callback` where \<accountID> is the Temenos account ID. |
   | Grant Types  | `Authorization Code`                                                                                   |
   | Scopes       | `openid`, `profile`, `email`, `phone`                                                                  |

6. (Optional) Require Advanced Identity Cloud to ask for consent to share information during authorization flows.

   Go to General Settings, click Show advanced settings, and select Authentication.

   Clear Implied Consent.

### Task 2: Add Advanced Identity Cloud as an OAuth 2.0 identity service in Temenos

|   |                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These instructions include steps for a third-party product. We've verified them to the best of our ability, but third-party functionality and interfaces may change. Read [the official Temenos documentation](https://docs.kony.com/konylibrary/konyfabric/kony_fabric_user_guide/Content/Identity10_Kony_OAuth2.htm#OAuth2ID) if you notice any differences. |

1. Sign on to the Temenos development environment as an administrator.

2. Go to the Quantum Fabric identity service designer page, create a new identity service with the following configuration, and click Save:

   | Field                                                 | Value                                                                        |
   | ----------------------------------------------------- | ---------------------------------------------------------------------------- |
   | Name                                                  | `Advanced Identity Cloud`                                                    |
   | Type of Identity                                      | `OAuth 2.0`                                                                  |
   | Provider Details > Grant Type                         | `Authorization Code`                                                         |
   | Provider Details > Authorize endpoint                 | `https://<tenant-env-fqdn>/am/oauth2/alpha/authorize`                        |
   | Provider Details > Token endpoint                     | `https://<tenant-env-fqdn>/am/oauth2/alpha/access_token`                     |
   | Provider Details > Scope                              | `openid`, `profile`, `email`, `phone`                                        |
   | Client Details > Client Assertion Type                | `Basic authentication`                                                       |
   | Client Details > Client ID                            | `temenos_oidc`                                                               |
   | Client Details > Client Secret                        | The password for the `temenos_oidc` client you created in the previous task. |
   | User Profile Endpoint Details > Profile Endpoint Type | `Profile in response of URL`                                                 |
   | User Profile Endpoint Details > URL                   | `https://<tenant-env-fqdn>/am/oauth2/alpha/userinfo`                         |
   | User Attribute Selectors > Federation ID              | `_id`                                                                        |

3. Use the Test Login feature to test the identity service.

   Sign on as an Advanced Identity Cloud test user you created in the [Create test users and roles](use-case-test-users-and-roles.html) use case.

4. When the service works as expected, publish the Fabric application.

## Reference material

Find background information for the procedures in this use case in the following documentation:

* Learn how to connect any OIDC relying party to Advanced Identity Cloud in [Register a custom OIDC application](../app-management/register-a-custom-application.html#openid-connect-oidc).

* Learn how to configure a Quantum Fabric OAuth 2.0 Identity Service in [Temenos Quantum Fabric OAuth 2.0 Identity Service](https://docs.kony.com/konylibrary/konyfabric/kony_fabric_user_guide/Content/Identity10_Kony_OAuth2.htm#OAuth2ID).

---

---
title: Assign roles to users dynamically
description: Assign roles to Advanced Identity Cloud users dynamically based on conditions
component: pingoneaic
page_id: pingoneaic:use-cases:use-case-dynamic-role
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/use-case-dynamic-role.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Users", "Roles", "Assignments", "Setup &amp; Configuration"]
page_aliases: ["implementation:use-case-dynamic-role.adoc"]
section_ids:
  dynamic-roles-description: Description
  dynamic-roles-goals: Goals
  dynamic-prerequisites: Prerequisites
  dynamic-roles-tasks: Tasks
  dynamic-roles-user: "Task 1: Assign an inactive status to a user"
  dynamic-roles-condition: "Task 2: Add a condition to a role"
  dynamic-roles-validation: Validation
  dynamic-roles-explore-further: Explore further
  dynamic-roles-reference: Reference material
---

# Assign roles to users dynamically

## Description

Estimated time to complete: 10 minutes *(tooltip: This assumes you have first completed the prerequisites.)*

In the use case [Create test users and roles](use-case-test-users-and-roles.html), you created two users and a role and then assigned the role users to the users. In this use case, you are going to:

* Assign an inactive status to one of the users

* Add a condition to the role so that it applies only to active users

## Goals

After completing this use case, you will know how to:

* Change the properties of a user

* Add a condition to a role

## Prerequisites

Before you start, make sure you have:

* A basic understanding of these Ping Identity concepts:

  * Advanced Identity Cloud admin console

  * Hosted pages

* Completed the use case in [Create test users and roles](use-case-test-users-and-roles.html)

## Tasks

### Task 1: Assign an inactive status to a user

In this task, you select one of the users you created in [Create test users and roles](use-case-test-users-and-roles.html) and change their status to inactive.

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage > [icon: people, set=material, size=inline] Alpha realm - Users.

2. Click on the user `acruse`.

3. On the user details page, change the Status from the default value `active` to `inactive` and save the change.

### Task 2: Add a condition to a role

In this task, you create a condition so that the role applies only to active users.

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage > [icon: assignment_ind, set=material, size=inline] Alpha Realm - Roles.

2. Click on the `employee` role and then click on Settings.

   ![Add new role](_images/use-case-dynamic-roles/role-settings.png)

3. In the Condition panel, click on Set up to create the following condition for the role and save the condition:

   | Field                                                                                                   | Value    |
   | ------------------------------------------------------------------------------------------------------- | -------- |
   | A conditional filter for this role                                                                      | Enable   |
   | Assign to alpha_user if *Any [icon: keyboard_arrow_down, set=material, size=inline]* conditions are met | `Any`    |
   | Alpha_user properties [icon: keyboard_arrow_down, set=material, size=inline]                            | `Status` |
   | contains [icon: keyboard_arrow_down, set=material, size=inline]                                         | `is`     |
   | Blank                                                                                                   | `active` |

   ![Add new role](_images/use-case-dynamic-roles/role-condition.png)

4. (Optional) Click on [icon: add, set=material, size=inline] Add Rule to add another condition and take a moment to browse the other conditions that can apply to roles.

Check in

At this point, you:

[icon: check, set=fa]Made a user inactive

[icon: check, set=fa]Added a condition to a role

## Validation

In [Create test users and roles](use-case-test-users-and-roles.html), you created the `employee` role and manually assigned it to `braman` and `acruse`. To validate this use case, make sure the role is no longer assigned to `acruse`.

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage > Role Members.

2. Make sure `braman` is in the list but `acruse` is not.

3. Change the status of `braman` to `inactive` and `acruse` to `active`, then make sure `acruse` is in the list but `braman` is not.

## Explore further

### Reference material

| **Reference**                                                                             | **Description**                                 |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------- |
| [Roles](../identities/roles-assignments.html#roles)                                       | Information about roles                         |
| [Grant roles dynamically](../idm-objects/roles-over-rest.html#to-grant-roles-dynamically) | Information about how to assign roles over REST |

---

---
title: Authentication
description: Implement authentication methods including SSO, MFA, and federation in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:use-cases:preface-pages/authentication
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/preface-pages/authentication.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Use Case"]
---

# Authentication

*Authentication* is the act of confirming a user's identity, for example, by providing a set of credentials.

In PingOne Advanced Identity Cloud, you primarily use journeys to create your authentication flows; However, you can also set up an external application to act as an identity provider.

Since there are many ways to implement authentication based on your needs, use cases vary and can include:

| Item                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single sign-on (SSO)              | SSO lets authenticated users access multiple independent services from a single login session by storing user sessions as [HTTP cookies](../../am-authentication/about-sso.html#http-cookies). You can configure Advanced Identity Cloud to let users use SSO with other applications, or let users of other applications use SSO with Advanced Identity Cloud.This includes creating applications to use popular federation protocols such as SAML and OAuth 2.0/OIDC. |
| Multi-factor authentication (MFA) | MFA is an authentication technique that requires users to provide multiple forms of identification when authenticating.MFA provides a more secure method for users to access their accounts with the help of a device *(tooltip: A piece of equipment that can display a one-time password or that supports push notifications using protocols supported by Advanced Identity Cloud MFA.)*.                                                                             |
| Pass-through authentication (PTA) | PTA lets you validate passwords with a remote service. This allows you to retain a remote service for authentication or to migrate passwords to Advanced Identity Cloud as part of authentication (just-in-time synchronization).                                                                                                                                                                                                                                       |

The use cases in this section focus on authentication:

| Use case                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Sign on with MFA using push notifications](../use-case-mfa-with-push.html)                      | Authenticate a user with MFA by setting up an authenticator app for push notification *(tooltip: A notification from Advanced Identity Cloud sent to an authenticator app on your smartphone that serves as an additional factor when logging in.)* on a smartphone.                                                                                                                                                                                                                                                                                                                                                      |
| [Replace lost second-factor authentication devices](../use-case-lost-second-factor.html)         | Authenticate users who've lost their second-factor authentication device. The journey allows them to sign on using a recovery code instead of their missing device. After authentication, they're prompted to register a new device and create a new passkey, securely restoring their account access.                                                                                                                                                                                                                                                                                                                    |
| [Salesforce as SP (SAML)](../use-case-sso-saml-salesforce-sp.html)                               | Configure SSO using SAML federated identities *(tooltip: Identity federation provides a means for partner services to establish a shared user identifier in order to share user information across organizational boundaries.)* with Advanced Identity Cloud as the Identity provider (IDP) *(tooltip: An identity provider authenticates a user.)* and Salesforce as the Service provider (SP) *(tooltip: A service provider authorizes the authenticated user to access its resources based on the its own access policies.)*.Specifically, you configure Advanced Identity Cloud as the IDP for Salesforce using SAML. |
| [Microsoft Entra ID (Azure AD) as OpenID provider](../use-case-sso-oidc-entra-id.html)           | Configure Advanced Identity Cloud to be a relying party (RP), or client, with [Microsoft Entra ID (formerly known as Azure AD)](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) as the OpenID provider (IDP).You also create a journey that lets end users sign on to Advanced Identity Cloud optionally using Microsoft Entra ID.                                                                                                                                                                                                                                                  |
| [Okta as RP (OIDC)](../use-case-sso-oidc-sp-okta.html)                                           | Configure Okta to be the RP with Advanced Identity Cloud as the IDP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Pass-through auth (PTA) with Microsoft Entra ID (Azure AD)](../use-case-pass-through-auth.html) | Enable pass-through authentication (PTA) to Microsoft Entra ID and let Advanced Identity Cloud capture the Microsoft Entra ID password for future logins.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Advanced Identity Cloud as a Temenos identity provider](../use-case-temenos.html)               | Configure Temenos to use Advanced Identity Cloud as an OpenID Provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

---

---
title: Authorization
description: Implement authorization policies for applications and protected resources in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:use-cases:preface-pages/authorization
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/preface-pages/authorization.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Use Case"]
---

# Authorization

*Authorization* is the act of determining whether an authenticated user is allowed to access a resource or perform an action.

In PingOne Advanced Identity Cloud, you use authorization policies to control access to applications, APIs, and protected resources. You can evaluate these policies during authentication, when a client requests access, or when a user must approve a sensitive action before proceeding.

The following table describes some of the use cases for authorization:

| Item                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Application authorization in journeys | Application journeys let you enforce application-specific access rules during sign-on.For example, you can associate a journey with an OIDC or SAML application and use the [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html) to evaluate whether the authenticated user is allowed to access that application.Learn more in [Authorize application access in journeys](../use-case-app-authz-journeys.html).      |
| Transactional authorization           | Transactional authorization requires a user to authorize each access to a protected resource.For example, a user might need to approve a financial transaction with a one-time password (OTP) or confirm an action with a push notification. Access is granted only for that single request, and later attempts require authorization again.Learn more in [Authorize one-time access with transactional authz](../../am-authorization/transactional-authorization.html). |
| Dynamic OAuth 2.0 authorization       | Dynamic OAuth 2.0 authorization uses policies to grant or deny requested scopes at runtime.This lets Advanced Identity Cloud decide which scopes to allow for a specific user, client, or request context instead of always granting the same scopes for every token request.Learn more in [Dynamic OAuth 2.0 authorization](../../am-authorization/oauth2-authorization.html).                                                                                          |

This section describes the following authorization use case in more detail.

| Use case                                                                        | Description                                                                                                             |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [Authorize application access in journeys](../use-case-app-authz-journeys.html) | Control access to an OIDC application by evaluating the application's access policy in a journey during authentication. |

---

---
title: Authorize application access in journeys
description: Control access to OIDC applications by evaluating authorization policies in Advanced Identity Cloud journeys
component: pingoneaic
page_id: pingoneaic:use-cases:use-case-app-authz-journeys
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/use-case-app-authz-journeys.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Use Case", "Journeys", "Authorization", "Policy", "SAML", "OIDC", "Application"]
section_ids:
  app-authz-journeys-description: Description
  app-authz-journeys-goals: Goals
  app-authz-journeys-prereqs: Prerequisites
  app-authz-journeys-tasks: Tasks
  app-authz-journeys-task-1: "Task 1: Create a custom application"
  app-authz-journeys-task-2: "Task 2: Assign the test user to the application"
  app-authz-journeys-task-3: "Task 3: Restrict access to the application"
  app-authz-journeys-task-4: "Task 4: Create a journey to control application access"
  app-authz-journeys-task-5: "Task 5: Associate the journey with the application"
  app-authz-journeys-validation: Validation
  app-authz-journeys-validation-steps: Steps
  app-authz-explore-further: Explore further
  oidc-idp-reference: Reference material
---

# Authorize application access in journeys

## Description

Estimated time to complete: 30 minutes *(tooltip: This estimate assumes you complete the prerequisites first.)*

In this use case, you register an internal high-risk application named PayrollHub and add an access policy that allows only members of the `Managers` group to sign in during business hours.

You then add an [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html) to a journey so that Advanced Identity Cloud automatically evaluates policy during authentication. This lets you verify access before sign-on completes, without writing custom scripts or configuring authorization separately.

The journey is also configured to run on every access attempt, so the authorization policy is evaluated each time an employee opens PayrollHub, even if they already have a session.

### Goals

After completing this use case, you'll know how to do the following:

* Onboard an OpenID Connect (OIDC) web application in Advanced Identity Cloud.

* Enforce application-specific authorization rules during authentication, filtering access by group membership and time-of-day restrictions.

* Use the App Policy Decision node in a journey to evaluate the application's access policy.

## Prerequisites

Before you start, make sure you have the following:

* A basic understanding of:

  * [Journeys and nodes](../journeys/journeys.html).

  * [Authorization and policy decisions](../am-authorization/what-is-authz-decision.html).

* Access to your Advanced Identity Cloud development environment as a tenant administrator.

* A test user [added to the Managers group](../idm-objects/manage-groups.html#create-a-group).

## Tasks

### Task 1: Create a custom application

In this task, you register PayrollHub as a custom OIDC web application in Advanced Identity Cloud. This represents the internal application that employees access from their company website.

1. In the Advanced Identity Cloud admin console, go to Applications > Applications and click [icon: add, set=material, size=inline] Custom Application.

2. Select OIDC - OpenId Connect as the sign-in method and Web as the application type.

3. On the Application Details page, enter `PayrollHub` as the application name, select an application owner from the list, and click Next.

4. Enter a client secret.

   Make a note of the Client ID and Client Secret values.

5. Click Create Application.

6. On the Sign On tab, configure the following:

   | Field        | Value                                |
   | ------------ | ------------------------------------ |
   | Sign-in URLs | `https://PayrollHub.internal/signin` |
   | Grant Types  | `Authorization Code`                 |
   | Scopes       | `openid profile`                     |

7. Click Save.

### Task 2: Assign the test user to the application

1. In the PayrollHub application, click the Users & Roles tab.

2. Click Add Member and select your test user.

3. Click Assign.

The test user is now able to sign on to PayrollHub.

### Task 3: Restrict access to the application

In this task, you add an access policy to PayrollHub that restricts sign-on to managers who have been given access to the application and are signing on during business hours.

The [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html) evaluates this policy automatically during the authentication journey. Learn more in [Configure an application authorization policy](../app-management/configure-app-authorization-policy.html).

1. In the Advanced Identity Cloud admin console, go to Applications > Applications and open PayrollHub.

2. Click the Sign On tab.

3. In the Access Policy section, click [icon: add, set=material, size=inline] Create a Policy.

4. In the Add Access Policy modal, select Group-based Access and click Next.

5. Select All to restrict access to users who meet all criteria.

6. For the first policy condition, set the following values:

   |           |                         |
   | --------- | ----------------------- |
   | Condition | `User Group Membership` |
   | equals    |                         |
   | Value     | `Managers`              |

7. Click [icon: add, set=material, size=inline] then Add Condition.

8. For the second policy condition, set the following values:

   |            |                            |
   | ---------- | -------------------------- |
   | Condition  | `Day, Date, or Time Range` |
   | Time Range |                            |
   | Start Time | `08:00`                    |
   | End Time   | `18:00`                    |

9. Click [icon: add, set=material, size=inline] then Add Condition.

10. For the third condition, set the following values:

    |           |                               |
    | --------- | ----------------------------- |
    | Condition | `User Application Membership` |

11. Click Save.

The saved access policy looks similar to this:

![Access policy](_images/use-case-app-authz-journeys/app-authz-access-policy.png)

Only users who are in the Managers group, have access to the PayrollHub application, and sign on between 8am and 6pm can access PayrollHub.

All other users are denied access.

### Task 4: Create a journey to control application access

In this task, you create a custom journey to control access to the PayrollHub application.

The journey uses the [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html) to check the application's access policy during authentication.

1. In the Advanced Identity Cloud admin console, click Journeys > Journeys.

2. Click [icon: add, set=material, size=inline] Add Journey, select Start from scratch, and then click Next.

3. Enter a name, for example `AppAuthorizationJourney`.

4. Select `people Alpha Realm Users - managed/alpha_user` as the identity object.

5. Save your changes.

   |   |                                                                                                                                                                                                                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You don't need to select the option to run the journey for all users regardless of current sessions because this is enabled by default for application journeys.Learn more in [Configure an authentication journey to always run](../am-authentication/configure-authentication-trees.html#enable-journey-completion) and [Custom journeys](../journeys/journeys.html#custom-journey). |

6. Add these nodes to the canvas:

   * Page node containing:

     * Platform Username node

     * Platform Password node

   * Data Store Decision node

   * App Policy Decision node

   * Failure

   * Success

7. Connect the nodes as follows:

   ![Get access token journey](_images/use-case-app-authz-journeys/app-authz-journey.png)

   |   |                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You could add an extra level of security by requiring multi-factor authentication (MFA) for users who are granted access by the App Policy Decision node. |

8. Click Save.

The App Policy Decision node identifies the calling application from the authentication request and evaluates the access policy configured on that application.

### Task 5: Associate the journey with the application

In this task, you configure PayrollHub to use the journey you created.

1. In the Advanced Identity Cloud admin console, go to Applications > Applications and open PayrollHub.

2. Go to Sign On > General Settings > Show advanced settings > Authentication.

3. Click Use a journey to authenticate users to this application.

4. In the Journey field, select `AppAuthorizationJourney`.

5. Click Save.

The application is now configured to use the journey you created to control access.

## Validation

Test that the journey correctly enforces your authorization policy.

### Steps

1. Open a browser in incognito mode and start an OAuth 2.0 authorization code sign-in flow, for example:

   `https://<tenant-env-fqdn>/am/oauth2/alpha/authorize?client_id=PayrollHub&redirectUri=http://www.PayrollHub.internal/signin&scope=openid&response_type=code`

2. Sign on between the hours of 8am and 6pm with a user who is a member of the `Managers` group and has access to PayrollHub.

   The user should be granted access and redirected to the application with an authorization code.

3. Sign on again with a user who isn't a member of the `Managers` group.

   The user should be denied access and the journey should reach the Failure node.

4. Sign on again with a valid user, then immediately start a second authorization code flow.

   Advanced Identity Cloud should prompt for credentials even though an active session exists, because the journey is configured to always run.

## Explore further

### Reference material

| **Reference**                                                                                           | **Description**                                                                                                          |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html) | Provides information about the node configuration and outcomes, including evaluation of the application's access policy. |
| [Application access policy](../app-management/configure-app-authorization-policy.html).                 | How to configure an application access policy.                                                                           |
| [Default policy sets](../am-authorization/configuring-policy-sets.html#default-policy-sets)             | Information about the app authorization policy set included in Advanced Identity Cloud.                                  |
| [Application journeys](../app-management/application-journeys.html)                                     | Associate a journey with an OIDC or SAML app so users authenticate with a flow tailored to that application.             |

---

---
title: Create a script in a journey to record last login time
description: Record last login time in Advanced Identity Cloud using a journey script
component: pingoneaic
page_id: pingoneaic:use-cases:use-case-last-login-time
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/use-case-last-login-time.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Implementation Guide", "JavaScript", "Scripts", "Use Case"]
page_aliases: ["implementation:use-case-last-login-time.adoc"]
section_ids:
  description: Description
  goals: Goals
  prerequisites: Prerequisites
  tasks: Tasks
  task_1_create_a_journey_decision_script: "Task 1: Create a journey decision script"
  task_2_update_the_target_managed_user_field: "Task 2: Update the target managed user field"
  task_3_create_a_last_login_journey: "Task 3: Create a last login journey"
  duplicate_the_default_login_journey: Duplicate the default login journey
  configure_your_last_login_time_journey: Configure your last login time journey
  task_4_check_journey_path_connections: "Task 4: Check journey path connections"
  validation: Validation
  steps: Steps
  video_of_validation: Video of validation
  explore_further: Explore further
  reference_material: Reference material
  nodes_used: Nodes used
---

# Create a script in a journey to record last login time

## Description

Estimated time to complete: 20 minutes *(tooltip: This assumes you complete the prerequisites beforehand.)*

In this use case, you duplicate an existing journey and modify it to record the time the user signs on to the hosted account pages. You use a script in your journey to record the login time.

### Goals

After completing this use case, you will know how to do the following:

* Create a script to use in a journey, referred to as a *journey decision script*.

* Change a field name in the end user profile.

* Adapt a journey to record shared state data in the end user profile.

## Prerequisites

Before you start work on this use case, make sure you have:

* A basic understanding of:

  * JavaScript

  * Journeys and nodes

  * Realms

  * The Advanced Identity Cloud admin console and hosted pages

  * The `managed/alpha_user` object schema

* Access to your Advanced Identity Cloud development environment as an administrator

* A test identity in Advanced Identity Cloud

## Tasks

### Task 1: Create a journey decision script

A journey decision script runs in Advanced Identity Cloud during an authentication journey. It's called a *decision* script because it's programmed to decide how the journey continues.

When the script runs, it can also read and change the shared state *(tooltip: An object nodes use to share information during the authentication journey.)* of the journey. In this example, the script adds a timestamp to record when it runs in the shared state.

Later, nodes can use the shared state data to take action. You can configure nodes to use shared state data and script the actions Advanced Identity Cloud takes. In this example, a later node writes the timestamp in the authenticating user's profile.

1. Sign on to the Advanced Identity Cloud admin console as an administrator.

   Select the `alpha` realm if it is not selected by default.

2. Go to [icon: code, set=material, size=inline] Extensions > Scripts, then click + New script.

3. Select Journey Decision Node and click Next to open the script editor.

4. Set the fields as follows and click Save and Close:

   | Field       | Value                                                                                                                                                                                                                                                                                                                                                                 |
   | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Name        | `last-login-time`                                                                                                                                                                                                                                                                                                                                                     |
   | Description | `Set last login time. Use this after successful authentication.`                                                                                                                                                                                                                                                                                                      |
   | JavaScript  | ```JavaScript
   function tag(message) {
       return '*** last-login-time: '.concat(message)
   }

   var lastLoginAttribute = 'frUnindexedDate1'
   var lastLoginTime = new Date().toISOString()
   sharedState.get('objectAttributes').put(lastLoginAttribute, lastLoginTime)
   logger.message(tag('Setting ' + lastLoginAttribute + ' to ' + lastLoginTime))
   outcome = 'Success'
   ``` |

   The script sets the shared state `objectAttributes.frUnindexedDate1` to the current time as an ISO date string. Managed users have [many optional fields](../identities/user-identity-properties-attributes-reference.html). The `frUnindexedDate1` field is one of them. The script sets this field in `objectAttributes`, the attributes of the managed user object, so a later node can write the updated `frUnindexedDate1` value from shared state to the user's profile.

   |   |                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `frUnindexedDate1` field is an *unindexed* field, meaning Advanced Identity Cloud does not maintain a search index for the field. If applications look up profiles based on the last login time, use one of the `frIndexedDate*` fields instead. |

   Notice the following objects from Advanced Identity Cloud bound to the journey decision script execution context; the script uses them directly without having to define them first:

   * `sharedState`: Use this to access the shared journey state.

   * `logger`: Use this to log debug messages.

   * `outcome`: Set the outcome to a string as the last processing step.

   There is no authentication decision to make, so the script's only outcome is `Success`. You include each outcome in the Scripted Decision node Outcomes setting when using the script in a journey.

Check in

At this point, you:

[icon: check, set=fa]Created a script to add last login time to the journey's shared state data.

### Task 2: Update the target managed user field

By default, the label in the hosted account pages for the `frUnindexedDate1` field is `Generic Unindexed Date 1`. The journey uses this field for last login times; therefore, you change the label to `Last Login Time` for readability.

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Configure.

2. Click Alpha realm - User > Properties to edit the managed object properties.

3. Scroll to the `frUnindexedDate1` row and click it to edit the property.

4. On the property's Details page, set Display Label to `Last Login Time` and click Save.

This changes the label in the hosted account pages.

Check in

At this point, you:

[icon: check, set=fa]Created a script to add last login time to the journey's shared state data.

[icon: check, set=fa]Configured the `Last Login Time` label in the hosted account pages.

### Task 3: Create a last login journey

You base the last login journey on the default Login journey. To reference the script, you add a Scripted Decision node. To write the last login time to the user's profile, you add a Patch Object node.

#### Duplicate the default login journey

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys.

2. Select the More ([icon: ellipsis-h, set=fa]) menu for the default Login journey and select Duplicate to display the Duplicate Journey modal.

3. Set the fields as follows and click Save:

   | Field           | Value                                                               |
   | --------------- | ------------------------------------------------------------------- |
   | Name            | `Log in and set last login time`                                    |
   | Identity Object | Alpha realm - Users `managed/alpha_user`                            |
   | Description     | `Duplicate of default Login journey that also sets last login time` |

   The Advanced Identity Cloud admin console displays the journey editor.

#### Configure your last login time journey

1. In the journey editor, find these nodes to drag and drop them onto the journey canvas:

   * Scripted Decision node

   * Patch Object node

2. Select the Scripted Decision node and set the fields as follows:

   | Field    | Value             |
   | -------- | ----------------- |
   | Name     | `Last login time` |
   | Script   | `last-login-time` |
   | Outcomes | `Success`         |

   Leave the default settings for other fields.

   When the journey reaches this node, your journey decision script runs.

3. Select the Patch Object node and set the fields as follows:

   | Field             | Value                |
   | ----------------- | -------------------- |
   | Identity Resource | `managed/alpha_user` |

   Leave the default settings for other fields.

   When the journey reaches this node, it updates the `managed/alpha_user` object properties with the shared state `objectAttributes` fields including the `frUnindexedDate1` field set by your script. This update stores the last login time in the end user's profile.

4. Reconnect the Scripted Decision node `True` outcome to the `Last login time` node input.

5. Connect the `Last login time` node outcome to the Patch Object node input.

6. Connect the Patch Object node `Patched` outcome to the Increment Login Count node input.

7. Connect the Patch Object node `Failed` outcome to the Failure node.

At this point, the authentication journey is complete. The following shows a rectangle around the nodes you added after duplicating the default journey:

![Last login time journey](_images/last-login-time/last-login-time.png)

* a Collects the username and password.

* b Validates the username and password.

* c Records the time in the shared state object attributes on `frUnindexedDate1`.

* d Writes the time to the user's profile.

* e Increments the number of authentications.

* f Triggers an inner journey; in this case, a journey for progressive profiling.

Check in

At this point, you:

[icon: check, set=fa]Created a script to add last login time to the journey's shared state data.

[icon: check, set=fa]Configured the `Last Login Time` label in the hosted account pages.

[icon: check, set=fa]Duplicate and configured a journey to record the last Login time.

### Task 4: Check journey path connections

Use the following table to check the connections for each node in the `Log in and set last login time` journey.

Some nodes have more than one outcome. The → symbol means the node only has one outcome path.

| Source node                                                             | Outcome path | Target node                               |
| ----------------------------------------------------------------------- | ------------ | ----------------------------------------- |
| Start (person icon)                                                     | →            | Page node                                 |
| Page node containing:- Platform Username node

- Platform Password node | →            | Data Store Decision node                  |
| Data Store Decision node                                                | `True`       | Scripted Decision node(`Last login time`) |
|                                                                         | `False`      | Failure node                              |
| Scripted Decision node(`Last login time`)                               | →            | Patch Object node                         |
| Patch Object node                                                       | `Patched`    | Increment Login Count node                |
|                                                                         | `Failed`     | Failure node                              |
| Increment Login Count node                                              | →            | Inner Tree Evaluator node                 |
| Inner Tree Evaluator node                                               | `True`       | Success node                              |
|                                                                         | `False`      | Failure node                              |

## Validation

Now that you have created your script, updated a label in the hosted account pages, duplicated the default Login journey, and updated the copy to record the last login time in the user's profile, you are ready to validate the journey.

Before validating, make sure you have a test user in the `alpha` realm.

### Steps

1. Get a URL you can use to test the journey:

   1. Log in to the Advanced Identity Cloud admin console as an administrator.

   2. Go to [icon: account_tree, set=material, size=inline] Journeys > Journeys.

   3. Select the journey you created, Log in and set last login time.

      A preview screen of the journey displays.

   4. Click the copy icon next to Preview URL, a URL you can use to test the journey as an end user:

      ![Copy the test URL for the journey](_images/last-login-time/copy-test-url.png)

2. Sign on to the hosted pages:

   1. Paste the URL into an incognito window. Use incognito mode for testing to avoid caching issues and interference with any current sessions.

   2. In the sign-on page, enter the test user's username and password.

   3. Click Next.

      The hosted account pages display the test user's profile.

3. Click Edit Your Profile to display the profile screen then Edit Personal Info to display the profile fields.

4. Scroll to the Last Login Time field.

   The field contains the timestamp written when the test user signed on:

   ![Last login timestamp](_images/last-login-time/last-login-time-field.png)

   The hosted account pages append `(optional)` to the field name for managed object properties without Required enabled.

### Video of validation

From the end user's perspective, the journey works as follows. The video starts with the test user signed on before trying the last login time journey:

**Video (Brightcove)**

\<https\://players.brightcove.net/771836189001/default_default/index.html?videoId=6343466376112>

## Explore further

### Reference material

| Reference                                                                                                                                                                              | Description                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [Admin consoles in Advanced Identity Cloud](../getting-started/getting-started-explore-platform.html)                                                                                  | Get to know the admin interfaces; Advanced Identity Cloud admin console, AM native admin console, and IDM admin console. |
| [Journeys](../journeys/journeys.html)                                                                                                                                                  | Conceptual information on journeys and their purpose in Advanced Identity Cloud.                                         |
| [Introduction to journeys with ForgeRock University](https://backstage.forgerock.com/university/on-demand/path/TGVhcm5pbmdQYXRoOjY%3D/chapter/Q291cnNlOjE1Nzg0/video/Q29udGVudDoxNDA4) | A guided video of journeys in Advanced Identity Cloud and how to use them.                                               |
| [Journey nodes](../journeys/auth-nodes.html)                                                                                                                                           | Learn about the configurable nodes Advanced Identity Cloud offers for use in journeys.                                   |
| [User identity attributes and properties reference](../identities/user-identity-properties-attributes-reference.html)                                                                  | Reference information for end user profile properties.                                                                   |
| [Scripted Decision node API](../am-scripting/scripting-api-node.html)                                                                                                                  | Reference information for journey decision node scripts.                                                                 |

### Nodes used

The last login time journey uses the following nodes:

* [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)

* [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)

* [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)

* [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)

* [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html)

* [Patch Object node](https://docs.pingidentity.com/auth-node-ref/latest/patch-object.html)

* [Increment Login Count node](https://docs.pingidentity.com/auth-node-ref/latest/increment-login-count.html)

* [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html)

* [Success node](https://docs.pingidentity.com/auth-node-ref/latest/success.html)

* [Failure node](https://docs.pingidentity.com/auth-node-ref/latest/failure.html)

---

---
title: Create organizations to delegate administration
description: Create organizations in Advanced Identity Cloud and delegate user administration to separate groups
component: pingoneaic
page_id: pingoneaic:use-cases:use-case-create-orgs
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/use-case-create-orgs.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Implementation Guide", "Use Case", "Organizations", "Identities"]
page_aliases: ["implementation:use-case-create-orgs.adoc"]
section_ids:
  organizations-description: Description
  organizations-goals: Goals
  organizations-prereqs: Prerequisites
  organizations-tasks: Tasks
  organizations-task-1: "Task 1: Create organization administrators and users"
  organizations-task-2: "Task 2: Create two organizations and assign administrators"
  organizations-task-3: "Task 3: Add members to the organizations"
  organizations-validation: Validation
  organizations-validation-steps: Steps
  organizations-explore-further: Explore further
  organizations-reference-material: Reference material
---

# Create organizations to delegate administration

## Description

Estimated time to complete: 20 minutes *(tooltip: This assumes you complete the prerequisites beforehand.)*

In this use case, you configure Advanced Identity Cloud to group users into organizations. Use organizations to delegate user administration to different groups of users.

### Goals

After completing this use case, you will know how to do the following:

* Create users.

* Create organizations.

* Assign administrators to organizations for delegated administration.

* Add users (members) to organizations.

* Use the hosted account pages to manage users in an organization as an organization administrator.

## Prerequisites

Before you start work on this use case, ensure you have these prerequisites:

* Access to your Advanced Identity Cloud development environment as an administrator.

* A basic understanding of realms.

## Tasks

### Task 1: Create organization administrators and users

In this task, you create six test users. Two users will be administrators for `OrgA` and `OrgB`, respectively. The other four are members of `OrgA` and `OrgB`.

1. Log in to the Advanced Identity Cloud admin console as an administrator.

2. Go to [icon: people, set=material, size=inline] Identities > Manage.

3. Click [icon: people, set=material, size=inline] Alpha realm - Users and [icon: add, set=material, size=inline] New Alpha realm - User.

4. On the New Alpha realm - User page, enter the following information for the user, and then click Save:

   | Field         | Value                   |
   | ------------- | ----------------------- |
   | Username      | `orga_admin`            |
   | First Name    | `OrgA`                  |
   | Last Name     | `Admin`                 |
   | Email Address | `orgaadmin@example.com` |
   | Password      | `Secret12!`             |

5. Go back to the New Alpha realm - User page and repeat steps 3 and 4 to add another administrator user with the following values:

   | Field         | Value                   |
   | ------------- | ----------------------- |
   | Username      | `orgb_admin`            |
   | First Name    | `OrgB`                  |
   | Last Name     | `Admin`                 |
   | Email Address | `orgbadmin@example.com` |
   | Password      | `Secret12!`             |

6. Go back to the New Alpha realm - User page and repeat steps 3 and 4 to add four more users with the following values:

   * User1 in OrgA:

     | Field         | Value                 |
     | ------------- | --------------------- |
     | Username      | `orga_emorris`        |
     | First Name    | `Elysia`              |
     | Last Name     | `Morris`              |
     | Email Address | `emorris@example.com` |
     | Password      | `Secret12!`           |

   * User2 in OrgA:

     | Field         | Value                 |
     | ------------- | --------------------- |
     | Username      | `orga_flandry`        |
     | First Name    | `Fatma`               |
     | Last Name     | `Landry`              |
     | Email Address | `flandry@example.com` |
     | Password      | `Secret12!`           |

   * User1 in OrgB

     | Field         | Value                 |
     | ------------- | --------------------- |
     | Username      | `orgb_ajarvis`        |
     | First Name    | `Amin`                |
     | Last Name     | `Jarvis`              |
     | Email Address | `ajarvis@example.com` |
     | Password      | `Secret12!`           |

   * User2 in OrgB

     | Field         | Value                   |
     | ------------- | ----------------------- |
     | Username      | `orgb_mpattison`        |
     | Fist Name     | `Morgan`                |
     | Last Name     | `Pattison`              |
     | Email Address | `mpattison@example.com` |
     | Password      | `Secret12!`             |

Six new users now display in the alpha realm.

![New users in the alpha realm](_images/orgs-delegated-admin/use-case-orgs-new-users.png)

### Task 2: Create two organizations and assign administrators

In this task, you create two parent organizations, `OrgA` and `OrgB`, and assign administrators to them.

|   |                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Parent organizations can only be created by super or tenant administrators. Sub-organizations are allowed within an organization, and organization administrators can create them within their respective organizations. |

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage.

2. On the Manage Identities page, click [icon: settings_system_daydream, set=material, size=inline] Alpha realm - Organizations.

3. Create `OrgA` and assign an administrator:

   1. Click [icon: add, set=material, size=inline] New Alpha realm - Organization.

   2. In the Name field, enter `OrgA`, and then click Save.

   3. In the Description field, enter `Organization A - employees`, and then click Save.

      ![Create OrgA](_images/orgs-delegated-admin/use-case-orgs-org-a.png)

   4. Click Administrators and [icon: add, set=material, size=inline] Add Administrators.

   5. Search for and select the user `orga_admin`, and then click Save.

      ![Add OrgA admin](_images/orgs-delegated-admin/use-case-orgs-org-a-admin.png)

4. Go back to the Alpha realm - Organization page.

5. Create `OrgB` and assign an administrator:

   1. Click [icon: add, set=material, size=inline] New Alpha realm - Organization.

   2. In the Name field, enter `OrgB`, and then click Save.

   3. In the Description field, enter `Organization B - contractors`, and then click Save.

   4. Click Administrators and [icon: add, set=material, size=inline] Add Administrators.

   5. Search for and select the user `orgb_admin`, and then click Save.

6. Go back to the Alpha realm - Organization page.

You now have two alpha realm organizations, `OrgA` and `OrgB`, each with an assigned administrator.

![New organizations in the alpha realm](_images/orgs-delegated-admin/use-case-orgs-new-orgs-list.png)

### Task 3: Add members to the organizations

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage.

2. On the Manage Identities page, click [icon: settings_system_daydream, set=material, size=inline] Alpha realm - Organizations.

3. Add members to `OrgA`:

   1. Click `OrgA`.

   2. Click Members and [icon: add, set=material, size=inline] Add Members.

   3. Search for and select `orga_emorris` and `orga_flandry`, and then click Save.

      The selected users are added to OrgA.

      ![OrgA members](_images/orgs-delegated-admin/use-case-orgs-org-a-members-added.png)

4. Go back to the Alpha realm - Organization page.

5. Add members to `OrgB`:

   1. Click `OrgB`.

   2. Click Members and [icon: add, set=material, size=inline] Add Members.

   3. Search for and select `orgb_ajarvis` and `orgb_mpattison`, and then click Save.

      The selected users are added to `OrgB`.

      ![OrgB members](_images/orgs-delegated-admin/use-case-orgs-org-b-members-added.png)

6. Go back to the Alpha realm - Organization page.

Check in

At this point, you:

|                                                                      |                                                                    |
| -------------------------------------------------------------------- | ------------------------------------------------------------------ |
| [icon: check, set=fa]Created new users in the alpha realm.           | [icon: check, set=fa]Created two organizations in the alpha realm. |
| [icon: check, set=fa]Assigned an administrator to each organization. | [icon: check, set=fa]Added two members to each organization.       |

## Validation

Now that you have set up your organizations and assigned administrators to them, you are ready to validate the configuration.

The steps in this validation check that organization administrators only have access to users who are members of their organizations. An additional step checks that the organization administrator can update the details of an individual user within their organization.

|   |                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To restrict the access organization (delegated) administrators have in Advanced Identity Cloud, organization administrators access user management functions through the hosted account pages and not the Advanced Identity Cloud admin console. |

### Steps

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys and click on the `Login` journey provided as default in Advanced Identity Cloud.

2. Copy and paste the `Preview URL` into an incognito window.

   The login page for the tenant displays.

3. In the Sign In page, enter the username and password for `orga_admin`, and then click Next.

   You are signed on to the hosted account pages as the `OrgA` admin. The left panel includes two administration menu items: [icon: settings_system_daydream, set=material, size=inline] Alpha realm - organization and [icon: people, set=material, size=inline] Alpha realm - user. These menu items display to an end user when they are a delegated administrator.

   ![Org administrator end user dashboard](_images/orgs-delegated-admin/use-case-orgs-org-a-admin-end-user-dashboard.png)

4. Click [icon: people, set=material, size=inline] Alpha realm - user.

   Only the users you added as `OrgA` members are listed (`orga_emorris` and `orga_flandry`).

   ![OrgA members](_images/orgs-delegated-admin/use-case-orgs-org-a-admin-end-user-users.png)

5. Log out of the hosted account pages.

6. In the Sign In screen, enter the username and password for `orgb_admin`, and then click Next.

7. Click [icon: people, set=material, size=inline] Alpha realm - user.

   Only the users you added as `OrgB` members are listed (`orgb_ajarvis` and `orgb_mpattison`).

   ![OrgB members](_images/orgs-delegated-admin/use-case-orgs-org-b-admin-end-user-users.png)

8. Click on `orgb_mpattison`.

9. Enter a phone number in the Telephone Number field, and then click Save.

10. Verify the updated user details:

    1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage

    2. Search for `orgb_mpattison`.

       The phone number you added as the `OrgA` administrator is shown in the Telephone Number field.

       ![User with a telephone number added by the organization admistrator](_images/orgs-delegated-admin/use-case-orgs-admin-telephone-updated.png)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To explore the role of organization administrators further, check out the other options in the hosted account pages. Organization administrators can do the following within their organization:- Add and update organization members.

- Add and update sub-organizations.

- Delegate user identity administration through roles and assignments.Learn more in [Administration](../identities/organizations.html#administrators). |

## Explore further

### Reference material

| Reference                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Structure identities using organizations](../identities/organizations.html)                                                                                                        | An overview of organizations in Advanced Identity Cloud. Includes an example to help explain organization concepts.                                                                                                                                                                                  |
| [Organizations](../idm-objects/organizations.html)                                                                                                                                  | A deeper dive into organizations.                                                                                                                                                                                                                                                                    |
| [Realms](../realms/realm-settings.html)                                                                                                                                             | Realms are administrative units that group configurations and identities together.Realms let you manage different sets of identities and applications within the same Advanced Identity Cloud tenant. Each realm is fully self-contained and operates independently of other realms within a tenant. |
| [Use case: Configure organizations in PingOne Advanced Identity Cloud](https://community.forgerock.com/t/use-case-configure-organizations-in-forgerock-identity-cloud/1989)         | A guided walkthrough on configuring organizations, including setting up owners, administrators, and members.Also explores how to delegate a subset of administration tasks to certain users based on an internal role.                                                                               |
| [Organization roles and privileges - Ping Identity Training](https://training.pingidentity.com//on-demand/path/TGVhcm5pbmdQYXRoOjEy/chapter/Q291cnNlOjE2MTgx/play/Q29udGVudDoxNjU2) | A guided walkthrough video describing the Organization managed object.                                                                                                                                                                                                                               |
| [Demo: Implement the organization - Ping Identity Training](https://training.pingidentity.com//on-demand/path/TGVhcm5pbmdQYXRoOjEy/chapter/Q291cnNlOjE2MTgx/play/Q29udGVudDoxNjkz)  | A guided walkthrough video demonstrating how to build an example organization.                                                                                                                                                                                                                       |

---

---
title: Create test users and roles
description: Create test users and roles in Advanced Identity Cloud and assign roles to users
component: pingoneaic
page_id: pingoneaic:use-cases:use-case-test-users-and-roles
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/use-case-test-users-and-roles.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Users", "Roles", "Assignments", "Setup &amp; Configuration"]
page_aliases: ["implementation:use-case-users-and-roles.adoc"]
section_ids:
  test-users-and-roles-description: Description
  test-users-and-roles-goals: Goals
  test-users-and-roles-prerequisites: Prerequisites
  test-users-and-roles-tasks: Tasks
  test-users-and-roles-register-user: "Task 1: Create new users"
  test-users-and-roles-register-role: "Task 2: Create a role"
  test-users-and-roles-validation: Validation
  test-users-and-roles-explore-further: Explore further
  test-users-and-roles-reference: Reference material
---

# Create test users and roles

## Description

Estimated time to complete: 10 minutes *(tooltip: This assumes you complete the prerequisites beforehand.)*

In this use case, you create test users and roles, assign users to roles, and sign on to the hosted account pages as one of the users.

## Goals

After completing this use case, you will know how to do the following:

* Create new users

* Create a role

* Assign the role to the users

## Prerequisites

Before you start, make sure you have a basic understanding of these Advanced Identity Cloud concepts:

* Advanced Identity Cloud admin console

* Hosted pages

## Tasks

### Task 1: Create new users

In this task, you create two new users.

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage.

   ![Add new user](_images/test-users-and-roles/create-user.png)

2. On the Manage Identities page, click [icon: people, set=material, size=inline] Alpha realm - Users and [icon: add, set=material, size=inline] New Alpha realm - User.

3. On the New Alpha realm - User page, enter the following information for the user, and then click Save:

   | Field         | Value                    |
   | ------------- | ------------------------ |
   | Username      | `acruse`                 |
   | First Name    | `alex`                   |
   | Last Name     | `cruse`                  |
   | Email Address | `alex.cruse@example.com` |
   | Password      | `Secret12!`              |

4. Go back to the New Alpha realm - User page and repeat the last step to add another user with the following values:

   | Field         | Value                    |
   | ------------- | ------------------------ |
   | Username      | `braman`                 |
   | First name    | `bina`                   |
   | Last name     | `raman`                  |
   | Email Address | `bina.raman@example.com` |
   | Password      | `Secret12!`              |

### Task 2: Create a role

In this task, you create a role called `employee`. Roles define privileges for user and device identities. Although the role isn't required for this use case, you can bulk assign users to an application when they are assigned a role.

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage.

   ![Add new role](_images/test-users-and-roles/create-role.png)

2. On the Manage Identities page, click [icon: assignment_ind, set=material, size=inline] Alpha Realm - Roles > [icon: add, set=material, size=inline] New Alpha realm - Role.

3. On the role page, enter the following information for the role and then click Next:

   | Field       | Value                                            |
   | ----------- | ------------------------------------------------ |
   | Name        | `employee`                                       |
   | Description | `Role granted to workers on the company payroll` |

4. Skip the option to assign the role conditionally, and click Next.

5. Skip the option to assign the role temporarily, and click Save.

   The `employee` role page is displayed.

6. Click Role Members > [icon: add, set=material, size=inline] Add Role Members.

7. Select your users from the drop-down list and then click Save.

   The role is assigned to the users.

Check in

At this point, you:

[icon: check, set=fa]Created two new users

[icon: check, set=fa]Created a role

[icon: check, set=fa]Assigned the role to the users

## Validation

To validate your work:

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys and click on the `Login` journey provided as default in Advanced Identity Cloud.

2. Copy and paste the `Preview URL` into an incognito window.

   The sign-on page for the tenant is displayed.

3. Sign on to the tenant as one of the new users and view the profile page for the user.

## Explore further

### Reference material

| **Reference**                                       | **Description**                             |
| --------------------------------------------------- | ------------------------------------------- |
| [Roles](../identities/roles-assignments.html#roles) | Information about roles                     |
| [Login](../journeys/journeys.html#login)            | Information about the default login journey |

---

---
title: Creating a custom report using Advanced Reporting
description: Create custom advanced reports in Advanced Identity Cloud for experts within your organization
component: pingoneaic
page_id: pingoneaic:use-cases:use-case-advanced-reporting
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/use-case-advanced-reporting.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Feb. 4, 2025
keywords: ["Advanced Identity Cloud", "Reports", "Template", "Custom reports", "Use Case"]
section_ids:
  description: Description
  goals: Goals
  before_you_begin: Before you begin
  tasks: Tasks
  creating_a_new_custom_report_draft: Creating a new custom report draft
  adding_a_data_source_and_user_provided_parameters: Adding a data source and user-provided parameters
  adding_filters_for_the_reports_data: Adding filters for the report's data
  running_and_viewing_the_report: Running and viewing the report
  publishing_the_report: Publishing the report
  duplicating_the_report: Duplicating the report
  editing_the_copy_and_adding_an_aggregate_count_to_the_report: Editing the copy and adding an aggregate count to the report
  exporting_and_downloading_the_report: Exporting and downloading the report
  showing_how_the_end_user_can_access_the_report: Showing how the end user can access the report
  validation: Validation
  video_of_validation: Video of validation
  troubleshooting: Troubleshooting
  error_when_running_a_report: Error when running a report
  explore_further: Explore further
  reference_material: Reference material
---

# Creating a custom report using Advanced Reporting

|   |                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud add-on capabilityContact your Ping Identity representative if you want to add Advanced Reporting to your Advanced Identity Cloud subscription. |

## Description

Estimated time to complete: 15 minutes *(tooltip: This assumes you complete the prerequisites beforehand.)*

In this use case, you create a custom report called `Userlist by Expertise by Organization` that generates a list of experts within an organization. The use case also shows how to create a duplicate of the report called `Count of Userlist By Expertise By Organization` that generates a count of experts within an organization.

## Goals

After completing this use case, you'll know how to do the following:

* Create a new custom report draft.

* Add a data source and user-provided parameters.

* Add filters for the report's data.

* Run and view the report.

* Publish the report.

* Duplicate the report.

* Edit the report and add an aggregate count to the report.

* Export and download the report.

* Show how the end user can access the report.

## Before you begin

For this use case, you'll need to have:

* A basic understanding of Advanced Identity Cloud concepts:

  * Advanced Reporting

  * Journeys

* An Advanced Identity Cloud tenant with the Advanced Reporting feature.

* Access to the tenant as an administrator.

* A set of test data to help correctly configure the report.

* An end user test account.

## Tasks

### Creating a new custom report draft

1. In the Advanced Identity Cloud admin console, go to Reports > [icon: plus, set=fa]New Report.

2. In the New Report modal, enter the following:

   * Name: Enter a descriptive name for the report. For this example, enter `Userlist by Expertise by Organization`.

   * Description (optional): Enter a description for the report.

   * Who Can Run: Enter users who can run the report. For example, enter a test user in your database, such as `john.doe`.

3. Click Next.

Check in

At this point, you've:

[icon: check, set=fa]Created a new custom report draft

### Adding a data source and user-provided parameters

1. Click [icon: plus, set=fa]Data Source.

   1. In the Add a Data Source modal, select Users. This data source provides access to the user database.

   2. Click Next.

2. In the right pane, under Settings, click Data and select the following columns:

   * Username

   * Generic Indexed String 1

3. In the right pane, click Organizations to which I Belong.

   1. Click [icon: plus, set=fa]and then click [icon: plus, set=fa]Add as Data Source.

   2. Under users/orgs, select the Org Name checkbox.

4. Next, add report parameters for `orgName` and `expertise`:

   1. Scroll down to Parameters and click [icon: plus, set=fa]for the `orgName` parameter.

   2. In the Add a Parameter modal, enter the following:

      * Name: Enter `orgName` for the parameter's descriptive name.

      * Input Label: Enter `Org Name` for the parameter's input label.

      * Input Type: Select String for the parameter's input type.

   3. Click Save.

5. Click [icon: plus, set=fa]to add the next parameter.

   * Name: Select `expertise` for the parameter's descriptive name.

   * Input Label: Select `Expertise` for the parameter's input label.

   * Input Type: Select String for the parameter's input type.

   * Multivalued: Select the Multivalued checkbox to accept one or more values.

6. Click Save.

Check in

At this point, you've:

[icon: check, set=fa]Created a new custom report draft

[icon: check, set=fa]Added a data source

[icon: check, set=fa]Added user-provided parameters

### Adding filters for the report's data

You need to configure filters for retrieving the correct data from your database. Create two filter rules for the `orgName` and `expertise` variables.

1. In the right pane, click [icon: plus, set=fa]next to Filters.

2. In the Add Filters modal, enter or select the following:

   * Any|All: Select All to require that all conditions must be met to be included in the filter.

   * Value: Select the users.orgs.name value for the filter rule.

   * Condition: Select the equals to condition for the filter rule.

   * Literal or Variable: Select Variable# for the filter, and then select the value, orgName.

3. Click [icon: plus, set=fa], and then click Add Rule.

   1. Value: Select the `users.frIndexedString1` for the filter rule.

   2. Condition: Select the contains condition for the filter rule.

   3. Select Variable for the filter, and then select the value, expertise.

      ![Add filters to a custom report.](_images/use-case-advanced-reporting/use-case-add-filters.png)

4. Click Save.

Check in

At this point, you've:

[icon: check, set=fa]Created a new custom report draft

[icon: check, set=fa]Added a data source

[icon: check, set=fa]Added user-provided parameters

[icon: check, set=fa]Added report filters

### Running and viewing the report

1. In the Advanced Identity Cloud admin console, return to the Reports page.

2. Locate your newly created report, Userlist by Expertise by Organization. In the report file, click Run.

3. On the Reports page, enter the following input parameters for the report:

   * Org Name: Enter `Data Science` for the organization name.

   * Expertise: Enter `Programming`, `Machine Learning`, and `Data Modeling`.

4. Click Run Report.

5. On the Run History tab, click View Report.

   ![Run the custom report Userlist by Expertise by Organization showing the username, generic indexed string1, and Org Name columns.](_images/use-case-advanced-reporting/use-case-run-report.png)

Check in

At this point, you've:

[icon: check, set=fa]Created a new custom report draft

[icon: check, set=fa]Added a data source

[icon: check, set=fa]Added user-provided parameters

[icon: check, set=fa]Added report filters

[icon: check, set=fa]Run the report

[icon: check, set=fa]Viewed the report

### Publishing the report

1. After reviewing the draft of your report, return to the Reports page and look for your report.

2. On the report tile, click [icon: ellipsis, set=fa], and then click Publish. The Published icon appears in the top right of the report tile.

Check in

At this point, you've:

[icon: check, set=fa]Created a new custom report draft

[icon: check, set=fa]Added a data source

[icon: check, set=fa]Added user-provided parameters

[icon: check, set=fa]Added report filters

[icon: check, set=fa]Run the report

[icon: check, set=fa]Viewed the report

[icon: check, set=fa]Published the report

### Duplicating the report

You can create a similar report with different parameters or columns by duplicating the original report and editing the new report copy. In this example, you'll create a new report listing the count of users by expertise in an organization.

1. On the Reports page, search for a report you want to copy. In this example, you'll search for `Userlist by Expertise by Organization`.

2. Click [icon: ellipsis, set=fa], and then click Duplicate.

3. In the Duplicate Report modal, enter the following:

   * Name: Enter `Count of Userlist By Expertise By Organization` for the report name.

   * Description (optional): Enter a general description for the new duplicate report.

   * Users: Select a test user in your database, such as `john-doe`.

4. Click Duplicate.

Check in

At this point, you've:

[icon: check, set=fa]Created a new custom report draft

[icon: check, set=fa]Added a data source

[icon: check, set=fa]Added user-provided parameters

[icon: check, set=fa]Added report filters

[icon: check, set=fa]Run the report

[icon: check, set=fa]Viewed the report

[icon: check, set=fa]Published the report

[icon: check, set=fa]Duplicated the report

### Editing the copy and adding an aggregate count to the report

1. On the Reports page, locate your report. In this example, search for `Count of Userlist By Expertise By Organization`.

2. Click [icon: ellipsis, set=fa], and then click Edit.

3. In the right pane, scroll down the users data source properties, and clear the Username checkbox.

4. In the right pane, scroll down to Aggregate, and click [icon: plus, set=fa].

   1. In the Add an Aggregate modal, enter the following:

      * Name: Enter `Count of Users` for a descriptive name.

      * Type: Select `Count of specific rows` for the type of parameter.

      * Value: Select `users.frIndexedString1` for the parameter value.

   2. Click Save.

5. Click Save at the upper right of the page to apply your edits to the report.

6. On the Reports page, locate your report, and click Run.

   1. On the Reports page, enter the following input parameters for the report:

      * Org Name: Enter `Data Science` for the organization name.

      * Expertise: Enter `Programming`, `Machine Learning`, and `Data Modeling`.

   2. Click Run Report, and then click View Report.

      ![Run the duplicate report.](_images/use-case-advanced-reporting/use-case-run-report-duplicate.png)

Check in

At this point, you've:

[icon: check, set=fa]Created a new custom report draft

[icon: check, set=fa]Added a data source

[icon: check, set=fa]Added user-provided parameters

[icon: check, set=fa]Added report filters

[icon: check, set=fa]Run the report

[icon: check, set=fa]Viewed the report

[icon: check, set=fa]Published the report

[icon: check, set=fa]Duplicated the report

[icon: check, set=fa]Edited the copy and added an aggregate count to the report

### Exporting and downloading the report

1. On the Reports page, locate your report.

2. Click [icon: ellipsis, set=fa], and then click Run History. If the report isn't available, run the report again.

3. Click the Download icon ([icon: file_download, set=material, size=inline]), and select Export CSV.

4. After the download generates, click Download Report (CSV).

5. Open the CSV file to review the results.

Check in

At this point, you've:

[icon: check, set=fa]Created a new custom report draft

[icon: check, set=fa]Added a data source

[icon: check, set=fa]Added user-provided parameters

[icon: check, set=fa]Added report filters

[icon: check, set=fa]Run the report

[icon: check, set=fa]Viewed the report

[icon: check, set=fa]Published the report

[icon: check, set=fa]Duplicated the report

[icon: check, set=fa]Edited the copy and added an aggregate count to the report

[icon: check, set=fa]Exported and downloaded the report

### Showing how the end user can access the report

1. In the Advanced Identity Cloud admin console, click Journeys > Journeys.

2. Click the Login journey.

3. In the Preview URL field, click [icon: copy, set=material, size=inline] and paste the URL into an incognito window.

4. In the end-user sign-on page, enter the end user's `User Name` and `Password`. The end user should be the one who can run the report, such as `john.doe`.

5. In the hosted account pages, click Reports. The Reports page displays the reports.

   ![End user view of the reports](_images/use-case-advanced-reporting/use-case-end-user-view.png)

Check in

At this point, you've:

[icon: check, set=fa]Created a new custom report draft

[icon: check, set=fa]Added a data source

[icon: check, set=fa]Added user-provided parameters

[icon: check, set=fa]Added report filters

[icon: check, set=fa]Run the report

[icon: check, set=fa]Viewed the report

[icon: check, set=fa]Published the report

[icon: check, set=fa]Duplicated the report

[icon: check, set=fa]Edited the copy and added an aggregate count to the report

[icon: check, set=fa]Exported and downloaded the report

[icon: check, set=fa]Shown how the end user can access the report

## Validation

To validate your work:

1. In the Advanced Identity Cloud admin console, go to Reports.

2. On the Reports page, enter `userlist` in the search box.

3. Click Userlist By Expertise By Organization.

4. Click [icon: ellipsis, set=fa]and then Run History.

5. On the Run History tab, check the report status. If the report displays `Expired`, you need to run the report again.

6. Click the Run Report tab, enter the following parameters:

   * Org Name: Enter `Data Science`.

   * Expertise: Enter `Programming`, `Machine Learning`, and `Data Modeling`.

7. Click Run Report.

8. View the report to check that the report displays the data configured for it.

### Video of validation

The following video displays the validating steps by running your custom report:

**Video (Video)**

<\_images/mp4/use-case-advanced-reporting-validation.mp4>

## Troubleshooting

### Error when running a report

If you run a report and encounter an error, it's likely because of an incorrect mapping of parameters and variables that's preventing the system from retrieving the user's data from the database.

![Userlist by Expertise by Organization report showing an error in the status columnof the report's run history.](_images/use-case-advanced-reporting/report-error.png)

* **Check the report's filters**

  1. In the Advanced Identity Cloud admin console, click Reports and locate your report.

  2. Go to [icon: ellipsis, set=fa]> Edit.

  3. In the right pane, scroll down to Filters and go to [icon: ellipsis, set=fa]> Edit Filter.

  4. Review which variables are mapped to the reports parameters.

* **Check user details**:

  1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

  2. Search for a test user.

  3. On the Details tab, check the variables used for your report. For example, in this use case, check the following:

     * `Generic Indexed String1`

  4. On the user's page, click Organizations to which I Belong. Check the user's organizations.

* **Edit your filters**:

  1. In the Advanced Identity Cloud admin console, click Reports and locate your report.

  2. Go to [icon: ellipsis, set=fa]> Edit.

  3. In the right pane, scroll down to Filters and go to [icon: ellipsis, set=fa]> Edit Filter.

  4. Make changes to the filters.

  5. Click Save.

  6. Run the report and check that it contains the correct data.

## Explore further

### Reference material

| Reference                                                                                                                          | Description                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [Entities and attributes available in advanced reporting](../reports/administration/advanced-reports.html#entities-and-attributes) | Get a list of entities and their attributes for use in a custom report. |

---

---
title: Customization
description: Customize branding, emails, journeys, and integrations in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:use-cases:preface-pages/customization
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/preface-pages/customization.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Customization", "Use Case"]
---

# Customization

PingOne Advanced Identity Cloud is highly customizable. For example, you can tailor the end-user experience or script a custom action within an authentication journey. Therefore, the use cases in this section focus on customization, from branding to code:

| Use case                                                                                                   | Description                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Customize a theme for hosted pages](../use-case-customize-theme.html)                                     | Customize the look and feel of the hosted pages to match your organization's branding.                                                                                            |
| [Customize emails](../use-case-email-template.html)                                                        | Customize an email template to match your organization's branding.                                                                                                                |
| [Create a script in a journey to record last login time](../use-case-last-login-time.html)                 | Duplicate an existing journey and modify it to record the time the user logs in to the hosted account pages. You use a script in a journey to record the login time.              |
| [Get an access token in a journey](../use-case-access-token-for-journeys.html)                             | Create a script to get a service account access token within your journeys. Then, create a simple journey with this script to prove you can successfully request an access token. |
| [Expose journey session properties in the OIDC ID token](../use-case-journey-session-properties-oidc.html) | Create a sign-on journey that stores a custom session property. Then, create a custom OIDC claims script to and add the session property to the ID token as a custom claim.       |

---

---
title: Customize a theme for hosted pages
description: "Customize the look and feel of Advanced Identity Cloud hosted pages to match your organization's branding"
component: pingoneaic
page_id: pingoneaic:use-cases:use-case-customize-theme
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/use-case-customize-theme.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Implementation Guide", "Use Case", "Journeys", "Hosted Pages", "Authentication"]
page_aliases: ["implementation:use-case-customize-theme.adoc"]
section_ids:
  themes-description: Description
  themes-goals: Goals
  themes-prereqs: Prerequisites
  themes-tasks: Tasks
  themes-task-1: "Task 1: Create a new theme and define the branding"
  themses-task-2: "Task 2: Set the new theme as the default theme"
  themes-validation: Validation
  themes-validation-steps: Steps
  themes-video-validation: Video of validation
  themes-explore-further: Explore further
  themes-reference-material: Reference material
---

# Customize a theme for hosted pages

## Description

Estimated time to complete: 20 minutes *(tooltip: This assumes you complete the prerequisites beforehand.)*.

In this use case, you customize the look and feel of the hosted pages to match your organization's branding.

### Goals

After completing this use case, you will know how to do the following:

* Create a new theme in Advanced Identity Cloud.

* Define the branding for end-user journey pages and account pages.

* Enable account controls so that end users can download and delete their data from their profile page.

* Set the new theme as the default theme for the hosted pages.

## Prerequisites

Before you start work on this use case, ensure you have these prerequisites:

* Access to your Advanced Identity Cloud development environment as an administrator.

* A URL that specifies the location of a logo image. The URL must be publicly accessible.

* A proficient understanding of HTML. Ping Identity allows you to customize pages with your own custom HTML.

* You have completed the use case [create test users and roles](use-case-test-users-and-roles.html). Specifically, you have created the test user `acruse`.

## Tasks

### Task 1: Create a new theme and define the branding

In this task, you create a new theme for end-user hosted pages and define the branding.

1. Sign on to the Advanced Identity Cloud admin console as an administrator.

2. Go to [icon: touch_app, set=material, size=inline] User Experience > Hosted Pages and [icon: add, set=material, size=inline] New Theme.

3. Enter `My Organization Theme`, and then click Save.

   The Hosted Pages editor displays.

4. In Global Settings make the following branding changes:

   | Tab    | Option       | Customize                                                            |
   | ------ | ------------ | -------------------------------------------------------------------- |
   | Styles | Brand Colors | Click the Brand Color field and enter the hex value `#009C80`.       |
   |        |              | Click the Brand Hover Color field and enter the hex value `#007661`. |

5. Click Journey Pages and make the following branding changes:

   | Tab    | Option          | Customize                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | ------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Styles | Page Background | Click the Page Background Color field and enter the hex value `#007661`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | Logo   | Logo            | Click the pencil icon ([icon: pencil-alt, set=fa]), enter your logo URL in the Logo URL field, and then click Update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | Layout | Footer          | Enable the Footer switch.Click the pencil icon ([icon: pencil-alt, set=fa]), edit the HTML, and then click Update. For example, enter the following:```html
   <div class="d-flex justify-content-center py-4 w-100">
   <span class="pr-1">© 2023</span>
   <a href="https://www.my-example-org.com" class="text-body">My Organization</a>
   <a href="https://www.my-example-org.com/privacy-policy" style="color:#0000ee" class="pl-3 text-body">Privacy Policy</a>
   <a href="https://www.my-example-org.com/terms-conditions" style="color:#0000ee" class="pl-3 text-body">Terms &amp; Conditions</a>
   </div>
   ``` |

6. Click Account Pages and make the following branding changes:

   | Tab    | Option            | Customize                                                                                                                                                                                                                                                                                                                                                      |
   | ------ | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Logo   | Expanded Version  | Click the pencil icon ([icon: pencil-alt, set=fa]), enter your logo URL in the Logo URL field, and then click Update.                                                                                                                                                                                                                                          |
   |        | Collapsed Version | Click the pencil icon ([icon: pencil-alt, set=fa]), enter your logo URL in the Logo URL field, and then click Update.                                                                                                                                                                                                                                          |
   | Layout | Profile Page      | Enable Account Controls.Account controls allow end users to download the data Identity Cloud has about them in a JSON format and allow end users to delete their account information.	End users can only view the information and take actions for the items you enable in the Profile Page. Learn more in Configure visible information and end-user actions. |

7. Click Global to review your changes.

   ![Customized theme](_images/use-case-customize-theme/use-themes-my-org-theme.png)

8. Click Save.

### Task 2: Set the new theme as the default theme

1. In the Advanced Identity Cloud admin console, go to [icon: touch_app, set=material, size=inline] User Experience > Hosted Pages.

2. Click the ellipsis icon ([icon: ellipsis-h, set=fa]) for the `My Organization Theme` and select Set as Realm Default.

   `My Organization Theme` is now the realm default theme.

![Default realm theme](_images/use-case-customize-theme/use-case-theme-realm-default.png)

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The default theme applies to the hosted journey and account pages. You can add custom themes so that your end users are presented with screens specific to their authentication journey. Learn more in [Add a custom theme](../end-user/hosted-pages-customize.html#add-a-custom-theme). |

Check in

At this point, you:

|                                                                            |                                                                                             |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [icon: check, set=fa]Created a new theme.                                  | [icon: check, set=fa]Defined the branding for the theme.                                    |
| [icon: check, set=fa]Enabled account controls in the hosted account pages. | [icon: check, set=fa]Set the new theme as the default for hosted journey and account pages. |

## Validation

Now that you have created your new theme and set it as the default, you are ready to validate the configuration.

The steps in this validation check that the hosted journey and account pages display the new theme, including letting end users download and delete their account data.

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In this validation task you sign on as `acruse`, who is one of the users created in [Create users and roles](use-case-test-users-and-roles.html). |

### Steps

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys and click on the `Login` journey provided as default in Advanced Identity Cloud.

2. Copy and paste the `Preview URL` into an incognito window.

   The Sign In page for the tenant displays with the `My Organization Theme` branding.

   ![Login page with customized theme](_images/use-case-customize-theme/use-case-theme-sign-in.png)

3. Enter the username and password for `acruse`, and then click Next.

   You are signed on to the hosted account pages.

4. Click Edit Your Profile.

   The Profile page displays, including Account Controls.

   ![Profile page with customized theme](_images/use-case-customize-theme/use-case-theme-account-controls.png)

5. In the Advanced Identity Cloud admin console, go to [icon: touch_app, set=material, size=inline] User Experience > Hosted Pages.

6. Click the ellipsis icon ([icon: ellipsis-h, set=fa]) for a different theme and select Set as Realm Default.

7. Go back to the hosted account pages (in the incognito window) and refresh the browser.

   The look and feel of the hosted pages changes to the theme you selected as the default.

### Video of validation

The following video displays the expected validation of logging in with the new theme and changing to a different default theme:

**Video (Brightcove)**

\<https\://players.brightcove.net/771836189001/default_default/index.html?videoId=6343467830112>

## Explore further

### Reference material

| Reference                                                                                                                                                                                                       | Description                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [Identity Cloud hosted pages](../end-user/hosted-pages.html)                                                                                                                                                    | Learn about hosted pages.                                                                                                  |
| [Demo: Configure themes for the Alpha and Bravo realms - ForgeRock University](https://backstage.forgerock.com/university/on-demand/path/TGVhcm5pbmdQYXRoOjY%3D/chapter/Q291cnNlOjE1Nzgw/play/Q29udGVudDoxNzIx) | A guided walkthrough video demonstrating how to configure themes for the hosted pages.                                     |
| [Use case: Create dynamically branded journeys in Advanced Identity Cloud](https://community.forgerock.com/t/use-case-create-dynamically-branded-journeys-in-forgerock-identity-cloud/3185)                     | A guided walkthrough demonstrating how to apply themes dynamically during a journey, based on the end user's organization. |

---

---
title: Customize emails
description: "Customize email templates in Advanced Identity Cloud to match your organization's branding"
component: pingoneaic
page_id: pingoneaic:use-cases:use-case-email-template
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/use-case-email-template.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Implementation Guide", "Use Case", "Customization"]
page_aliases: ["implementation:use-case-customize-email-template.adoc"]
section_ids:
  emails-description: Description
  emails-goals: Goals
  emails-prereqs: Prerequisites
  emails-tasks: Tasks
  emails-tasks-1: "Task 1: Create a new user registration email template"
  emails-duplicate-email: Duplicate the default user registration email
  emails-customize-email: Customize the new email template
  emails-tasks-2: "Task 2: Update the user registration journey"
  emails-validation: Validation
  emails-validation-steps: Steps
  emails-video: Video
  emails-explore-further: Explore further
  emails-reference-material: Reference material
---

# Customize emails

## Description

Estimated time to complete: 20 minutes *(tooltip: This assumes you complete the prerequisites beforehand.)*

In this use case, you:

* Duplicate the default registration email

* Customize the duplicated email to match your organization's branding

* Add the new email template to the `User Registration` journey (you must complete the [User registration](use-case-user-registration.html) use case)

* Register as a new end user to test the newly branded email

### Goals

After completing this use case, you will know how to do the following:

* Create new email templates

* Update journeys to use different email templates

## Prerequisites

Before you start work on this use case, ensure you have these prerequisites:

* You have completed the [User registration](use-case-user-registration.html) use case

* Access to your Advanced Identity Cloud development environment as an administrator

* A basic understanding of journeys and nodes

* A basic understanding of CSS

## Tasks

### Task 1: Create a new user registration email template

|   |                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In your staging, UAT\[[1](#_footnotedef_1 "View footnote.")], and production tenant environments, you *must* update the [email provider configuration](../tenants/email-provider.html#email-provider-configuration-workflow) to use your own external email provider. |

#### Duplicate the default user registration email

1. In the Advanced Identity Cloud admin console, go to [icon: touch_app, set=material, size=inline] User Experience > Email Templates.

2. On the Email Templates page, click the ellipsis icon ([icon: ellipsis-h, set=fa]) for the `Registration` template and select Duplicate.

3. In the Duplicate Template window, enter the following details:

   | Field         | Value                                                                 |
   | ------------- | --------------------------------------------------------------------- |
   | Template Name | `Branded Registration`                                                |
   | From Address  | Enter an email address for the group or individual sending the email. |
   | From Name     | Enter a name for the group or individual sending the email.           |
   | Description   | `Branded version of the default Registration email.`                  |

4. Click Save.

   The email templates editor displays.

#### Customize the new email template

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can add images to your email template if they are hosted online. Learn more in [Add an image to an email template](../tenants/email-templates.html#add-email-template-images). |

1. In the email templates editor, make the following changes to the `Branded Registration` email template:

   | Change                                  | Detail                                                                                                                                               |
   | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Update the heading text                 | Replace the heading text in line 1 with `Thank you for registering`.Leave the `#` characters. This indicates a heading, in this case, an H3 heading. |
   | Update the email verification link text | Update the email verification link text in line 3 to:```
   To confirm your email address, click [verify email](<{{object.resumeURI}}>).
   ```            |

2. Click Save.

3. Click Styles to change the look and feel of the email template. Make the following changes:

   | Change                  | Detail                                                                             |
   | ----------------------- | ---------------------------------------------------------------------------------- |
   | Update the font         | Add `font-family:arial;` under *.content* to change the font used in the email.    |
   | Change the link color   | Change the color value under *a* to `#0C85CF`.                                     |
   | Format the heading text | Add the following CSS to format the heading text:```css
   h3{
      color:#324054
   }
   ``` |

   ![Registration email preview](_images/use-case-customize-email-template/email-template-styles.png)

4. Click Save.

   The email preview shows the updated email template:

   ![Registration email preview](_images/use-case-customize-email-template/register-email-preview.png)

5. In the URL, copy the email template name shown after /edit (`brandedRegistration`). You will need this in the next task.

   ![Email template name](_images/use-case-customize-email-template/email-template-name.png)

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can send yourself a test email to check everything looks correct before proceeding. Click Send Test Email, enter your email address, and click Send. |

### Task 2: Update the user registration journey

In this task, you update the `User Registration` journey to use your new email template.

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys.

2. Click the ellipsis icon ([icon: ellipsis-h, set=fa]) for the `Registration` journey and select Edit.

3. Click the Email Suspend Node and enter `brandedRegistration` in the Email Template Name field.

   The name you enter must exactly match the name shown in the URL when you customized the email template.

4. Click Save.

Check in

At this point, you:

|                                                                                            |                                                                                       |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| [icon: check, set=fa]Created a new email template for user registration.                   | [icon: check, set=fa]Customized the email to use your organization's font and colors. |
| [icon: check, set=fa]Updated the User Registration journey to use your new email template. |                                                                                       |

## Validation

Now that you have created a new email template for user registration and added it to the `User Registration` journey, you are ready to validate the email.

The steps in this validation register a new end user in Advanced Identity Cloud so you can check they receive the branded email during the registration process.

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | When you register the new end user, ensure you use an email address that you can access. |

### Steps

1. In the Advanced Identity Cloud admin console, go to [icon: account_tree, set=material, size=inline] Journeys > Journeys and click on the `User Registration` journey you just updated.

2. In the Preview URL field, click [icon: copy, set=material, size=inline] and paste the URL into an incognito window.

   The Sign Up page for the tenant displays.

3. In the Sign Up page, enter the following details:

   | Field         | Value                                                                                 |
   | ------------- | ------------------------------------------------------------------------------------- |
   | Username      | `cbarnes`                                                                             |
   | First Name    | `Charlie`                                                                             |
   | Last Name     | `Barnes`                                                                              |
   | Email Address | Enter an email address for this new user. You must have access to this email account. |

4. Click Next. A message displays informing you an email has been sent.

5. Check the inbox for the email address you entered and view the registration email. Confirm it has been branded as expected.

6. Click the link in the email to confirm your email address and continue registration.

7. Enter `Ch4ng3it!` in the Password field.

8. Click Next.

   You are signed on to the hosted account pages as Charlie Barnes.

### Video

The following video displays the expected validation of registering a new end user using the updated email template:

**Video (Brightcove)**

\<https\://players.brightcove.net/771836189001/default_default/index.html?videoId=6343466377112>

## Explore further

### Reference material

| Reference                                                                                                  | Description                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [Email templates](../tenants/email-templates.html)                                                         | Learn about creating, editing and managing email templates.                                    |
| [Use HTML formatting in an email template](../tenants/email-templates.html#email-template-html-formatting) | Steps for enhancing email templates in Advanced Identity Cloud with images and HTML formatting |
| [Use ESV variables in an email template](../tenants/email-templates.html#email-template-esvs)              | Steps for including Environment secrets and variables (ESVs) in email templates.               |
| [Manage email template locales](../tenants/email-templates.html#manage-email-template-locales)             | Steps to send localized emails from a journey.                                                 |
| [Journeys](../journeys/journeys.html)                                                                      | Conceptual information on journeys and their purpose in Advanced Identity Cloud.               |

***

[1](#_footnoteref_1). A [user acceptance testing (UAT) environment](../tenants/environments-uat.html) is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Data (identity) management
description: Manage identities, organizations, roles, and applications in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:use-cases:preface-pages/data-identity-management
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/preface-pages/data-identity-management.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Management", "Use Case"]
---

# Data (identity) management

In PingOne Advanced Identity Cloud, data management covers a wide-range of activities including:

| Item                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identity object schema | The model for your data including users, roles, and applications. Create new objects or modify existing ones so that each object represents the properties your organizations requires.                                                                                                                                                                                                                                                                             |
| Organizations          | Create organizations in PingOne Advanced Identity Cloud when you want to group identities to suit your business needs.For example, you can build an organization structure modeled after your brand hierarchy. This lets you control access to business applications with tailored sign-on experiences. You can also use organizations to delegate user administration.                                                                                             |
| Roles                  | Roles define privileges for user and device identities. Roles let you automatically assign and update privileges in numerous identity profiles. For further information about roles and assignments, refer to [Roles and assignments](../../identities/roles-assignments.html).The *role* object is a managed object type that uses the [relationships](../../idm-objects/relationships.html) mechanism to link the role to the managed object to which it applies. |
| Applications           | While you can use applications for authentication, applications are also used for provisioning and synchronization.                                                                                                                                                                                                                                                                                                                                                 |

The use cases in this section focus on data management in a holistic way:

| Use case                                                                                                     | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Create test users and roles](../use-case-test-users-and-roles.html)                                         | Create test users and roles, assign users to roles, and sign on to the hosted account pages as one of the users.                                                         |
| [Assign roles to users dynamically](../use-case-dynamic-role.html)                                           | Dynamically assign a user to a role based off a criteria being met.                                                                                                      |
| [Provision data between Advanced Identity Cloud and PingDirectory](../use-case-idc-with-ping-directory.html) | Provision accounts to and from Advanced Identity Cloud and PingDirectory.                                                                                                |
| [Create organizations to delegate administration](../use-case-create-orgs.html)                              | Configure Advanced Identity Cloud to group users into organizations. Use organizations to delegate user administration to different groups of users.                     |
| [Enable managers to manage their direct reports](../use-case-manage-reports.html)                            | Configure Advanced Identity Cloud to enable managers to update their direct reports' information and assign provisioning roles to them through the hosted account pages. |
| [Provision users from Microsoft Entra](../use-case-provision-from-entra-id.html)                             | Provision accounts from Microsoft Entra ID (formerly Azure AD) into Advanced Identity Cloud.                                                                             |
| [Provision data from Active Directory (AD) using RCS](../use-case-provision-rcs-ad.html)                     | Provision accounts from an on-premise Active Directory (AD) server into Advanced Identity Cloud.                                                                         |

---

---
title: Enable managers to manage their direct reports
description: Enable managers to manage their direct reports through Advanced Identity Cloud hosted pages
component: pingoneaic
page_id: pingoneaic:use-cases:use-case-manage-reports
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/use-case-manage-reports.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Implementation Guide", "Use Case", "Identities"]
page_aliases: ["implementation:use-case-manage-reports.adoc"]
section_ids:
  managers-description: Description
  managers-goals: Goals
  managers-prereqs: Prerequisites
  managers-tasks: Tasks
  managers-task-1: "Task 1: Define a virtual property to use as a privilege filter"
  managers-task-2: "Task 2: Set up relationship notifications"
  managers-task-3: "Task 3: Assign a manager user (testmanager1) to a report user (testuser1)"
  managers-task-4: "Task 4: Configure delegated administration privileges"
  create_an_internal_managers_role_with_privileges: Create an internal managers role with privileges
  assign_the_internal_role_to_the_manager_user_testmanager1: Assign the internal role to the manager user (testmanager1)
  managers-validation: Validation
  managers-validation-steps: Steps
  managers-explore-further: Explore further
  managers-reference-material: Reference material
---

# Enable managers to manage their direct reports

## Description

Estimated time to complete: 20 minutes *(tooltip: This assumes you complete the prerequisites beforehand.)*

In this use case, you configure delegated administration to let managers update their direct reports' information and assign provisioning roles to them through the hosted account pages.

You'll need to use [Relationship-derived virtual properties (RDVPs)](../idm-objects/managed-object-virtual-properties.html#relationship-derived-virtual-properties) to filter users based on their manager relationships in the hosted account pages. This approach stores references to the target objects of a relationship as a property of the source object, enabling their use in privilege filters.

### Goals

After completing this use case, you will know how to do the following:

* Define a virtual property to use as a privilege filter.

* Set up relationship notifications.

* Configure delegated administration by creating an internal role with privileges.

* Test delegated administration in the hosted account pages.

## Prerequisites

Before you start work on this use case, ensure you have these prerequisites:

* Access to your Advanced Identity Cloud development environment as an administrator.

* A basic understanding of:

  * The [Advanced Identity Cloud identity schema](../identities/identity-cloud-identity-schema.html)

  * [Relationships](../planning/plan-object-modeling-relationships.html)

  * [Relationship-derived virtual properties (RDVPs)](../idm-objects/managed-object-virtual-properties.html#relationship-derived-virtual-properties)

* Two users in the alpha realm:

  * A manager user, with username `testmanager1`

  * A report user, with username `testuser1`

Learn more about creating test users in [Create test users and roles](use-case-test-users-and-roles.html).

## Tasks

### Task 1: Define a virtual property to use as a privilege filter

In this task, you define a virtual property to store the manager ID. To achieve this, you can modify an indexed [general purpose extension attribute](../identities/user-identity-properties-attributes-reference.html#general-purpose-extension-attributes). The example uses `frindexedstring1`.

1. In the Advanced Identity Cloud admin console, go to Identities > Configure.

2. On the Managed Object Types page, select Alpha realm - User.

3. Click the Properties tab, locate frIndexedString1, and click it to edit its settings.

4. On the Details tab, enter the following information:

   | Field         | Value              |
   | ------------- | ------------------ |
   | Display Label | `custom_managerID` |
   | Description   | `Manager's ID`     |

5. Click the Property Value tab and configure the relationship source:

   1. Under Choose how the value is set for the property, select Relationship.

   2. In the Source(s) section, select Manager.

   3. In the Referenced Object Properties section, choose Select Properties and select `_id`.

   4. Select Flatten properties.

   5. Select Return By Default.

6. Click Save.

With this configuration, whenever an `alpha_user` object is updated, Advanced Identity Cloud will resolve its manager relationship and store the relationship data in the `frindexedstring1` property along with the updated object.

### Task 2: Set up relationship notifications

In this task, you configure relationship notifications so that a user object is notified whenever its manager relationship changes. Relationship notifications are triggered by any activities related to an object update, including the `onUpdate` and `postUpdate` [script hooks](../idm-objects/managed-objects-scripts.html), and [implicit synchronization](../idm-synchronization/sync-types.html).

Relationship notifications are necessary because an object can be impacted by a relationship change even if it is not the direct target of the change. Without these notifications, the user object won't receive updates. Since `manager`/`reports` is a reverse relationship *(tooltip: A reverse relationship means both sides point to the other in a bidirectional flow.)*, you must ensure the user object is notified when a report is added to a manager.

To set up relationship notifications:

1. In the Advanced Identity Cloud admin console, go to Identities > Configure.

2. On the Managed Object Types page, select Alpha realm - User.

3. Click the Relationships tab, and then select the Manager / Direct reports relationship.

4. On the Relationship Property tab:

   1. On the alpha_user.manager side, select Notify Self.

   2. On the alpha_user.reports side, select Notify.

5. Click Save.

### Task 3: Assign a manager user (`testmanager1`) to a report user (`testuser1`)

In this task, you assign a manager to the report user.

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage.

2. On the Manage Identities page, click [icon: settings_system_daydream, set=material, size=inline] Alpha realm - Users.

3. Search for and select `testuser1`.

4. Scroll down to the Manager field and enter the manager. In our example, this is `testmanager1`.

   ![Test user record with manager populated](_images/use-case-manage-reports/use-case-managers-test-user-with-test-manager.png)

5. Click Save.

6. Click \[.label]Raw JSON# and notice that the `frIndexedString1` field is populated, similar to this:

   ```json
    "frIndexedString1": "4d130ce4-1cc9-40c8-899d-468ec1ef0161"
   ```

Check in

At this point, you:

|                                                                                                  |                                                         |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| [icon: check, set=fa]Defined a virtual property in the Alpha realm to use as a privilege filter. | [icon: check, set=fa]Set up relationship notifications. |
| [icon: check, set=fa]Added the test manager to the test user.                                    |                                                         |

### Task 4: Configure delegated administration privileges

In this task, you create an internal role with privileges and assign it to managers, enabling them to view and manage their direct reports through the hosted account pages.

#### Create an internal managers role with privileges

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Manage.

2. On the Manage Identities page, click [icon: people, set=material, size=inline]Internal Roles.

3. Click + New Internal Role.

4. Enter the following information, and then click Next:

   | Field       | Value               |
   | ----------- | ------------------- |
   | Name        | `managers`          |
   | Description | `Role for managers` |

5. Select `Alpha Realm Users - managed/alpha_user` from the drop-down list, and then click Add.

6. Select the View and Update checkboxes, and then click Show advanced.

7. Under Attribute Permissions, click set all attributes, and select `None`.

8. Scroll through the list of attributes and enable the ones to be exposed to the manager:

   * Set `userName`, `givenName`, `cn` and `sn` to Read.

   * Set `description` and `roles` to Read/Write.

     ![Internal managers role permissions](_images/use-case-manage-reports/use-case-managers-internal-role-permissions.png)

9. Select Administer only a subset of Alpha realm - Users by applying a filter.

10. Click Advanced Editor and enter the following query expression:

    ```js
    frIndexedString1 eq "{{_id}}""
    ```

    This filter condition means that only objects that have a property named `frIndexedString1` whose value matches the value of the authenticated user's `_id` are returned.

    ![Internal role permissions query expression](_images/use-case-manage-reports/use-case-managers-internal-role-query-expresion.png)

11. Click Next.

12. Click Next (without setting a dynamic internal role assignment).

13. Click Save (without setting a time constraint).

#### Assign the internal role to the manager user (`testmanager1`)

1. Click the Members tab for the newly created `manager` internal role.

2. Click Add Members.

3. Select `testmanager1`.

4. Click Save.

![Internal managers role assigned to test manager](_images/use-case-manage-reports/use-case-managers-internal-role-test-manager.png)Check in

At this point, you:

|                                                                                                  |                                                                                                                                 |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| [icon: check, set=fa]Defined a virtual property in the Alpha realm to use as a privilege filter. | [icon: check, set=fa]Set up a relationship notifications.                                                                       |
| [icon: check, set=fa]Added the test manager to the test user.                                    | [icon: check, set=fa]Created an internal managers role with privileges and assigned the internal role to the test manager user. |

## Validation

You are now ready to validate the configuration.

### Steps

1. In an incognito browser window, go to the hosted pages sign-on URL.

2. In the Sign In page, enter the username and password for `testmanager1`, and then click Next.

   Alpha realm - User appears as a menu option on the left menu pane, enabling managers to view and manage their direct reports.

   ![Manage reports through though the hosted account pages](_images/use-case-manage-reports/use-case-managers-end-user-ui.png)

3. Click Alpha realm - User.

   The manager's direct reports are listed (just `testuser1` in this example).

   ![Manager's reports listed in the hosted account pages](_images/use-case-manage-reports/use-case-managers-end-user-ui-test-users.png)

4. Click `testuser1`.

   ![Testuser1 details in hosted account pages](_images/use-case-manage-reports/use-case-managers-end-user-managed-user.png)

The manager can make updates to their report users' details based on the attribute permissions defined in the internal role.

## Explore further

### Reference material

| Reference                                                                                                                                                       | Description                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [Advanced Identity Cloud identity schema](../identities/identity-cloud-identity-schema.html)                                                                    | An overview of the identity schema used to organize users, roles, assignments, groups, organizations, and applications. |
| [Relationships](../planning/plan-object-modeling-relationships.html)                                                                                            | An overview of relationships in the identity model.                                                                     |
| [Relationship-derived virtual properties (RDVPs)](../idm-objects/managed-object-virtual-properties.html)                                                        | An overview of virtual properties that can be calculated based on relationships and relationship notifications.         |
| [Roles and assignments](../identities/roles-assignments.html)                                                                                                   | An overview of building an entitlement structure in Advanced Identity Cloud.                                            |
| [Modeling Identities - ForgeRock University](https://backstage.forgerock.com/university/forgerock/on-demand/path/TGVhcm5pbmdQYXRoOjEy/chapter/Q291cnNlOjE2MTgx) | On-demand training videos and demos on identity modeling in Advanced Identity Cloud.                                    |

---

---
title: Expose journey session properties in the OIDC ID token
description: Expose Advanced Identity Cloud journey session properties in OIDC ID tokens as custom claims
component: pingoneaic
page_id: pingoneaic:use-cases:use-case-journey-session-properties-oidc
canonical_url: https://docs.pingidentity.com/pingoneaic/use-cases/use-case-journey-session-properties-oidc.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Use Case", "Journeys", "Scripts", "OIDC", "Setup &amp; Configuration"]
section_ids:
  session-properties-journey-description: Description
  session-properties-journey-goals: Goals
  session-properties-journey-prereqs: Prerequisites
  session-properties-journey-tasks: Tasks
  session-properties-journey-task-1: "Task 1: Create a sign-on journey"
  session-properties-journey-task-2: "Task 2: Allowlist the session property"
  session-properties-journey-task-3: "Task 3: Create a custom claims script"
  session-properties-journey-task-4: "Task 4: Configure the OAuth 2.0 provider to return claims in the ID token"
  session-properties-journey-task-5: "Task 5: Create an OIDC relying party profile"
  session-properties-create-client: Create a confidential OAuth 2.0 client
  override_oauth_2_0_provider_settings_for_this_client: Override OAuth 2.0 provider settings for this client
  session-properties-journey-validation: Validation
  session-properties-journey-validaion-steps: Steps
  session-properties-journey-explore-further: Explore further
  session-properties-journey-reference-material: Reference material
  session-properties-journey-nodes-used: Nodes used
---

# Expose journey session properties in the OIDC ID token

## Description

Estimated time to complete: 20 minutes *(tooltip: This assumes you complete the prerequisites beforehand.)*

In this use case, you create a PingOne Advanced Identity Cloud sign-on journey that collects end-user details and stores them as session properties on successful authentication. You then create an OIDC claims script that defines a custom claim. This script lets you retrieve a stored session property and include it in the ID token as a custom claim.

For testing purposes, the example uses a custom session property called `mySessionProperty` and an additional scope called `myCustomScope`, which adds the session property to the ID token.

|   |                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about adding a session property claim to the profile scope in [Add a session property claim to the profile scope](../am-oauth2/plugins-user-info-claims.html#example-add-session-claim-profile-scope). |

### Goals

After completing this use case, you will know how to do the following:

* Make journey session properties available in the OIDC ID token.

## Prerequisites

Before you start work on this use case, ensure you have these prerequisites:

* A basic understanding of:

  * Journeys and nodes

  * OIDC

* Access to your Advanced Identity Cloud development environment as a tenant administrator.

* A test end user in the Alpha realm. Learn more about creating test users in [Create test users and roles](use-case-test-users-and-roles.html).

## Tasks

### Task 1: Create a sign-on journey

In this task, you create a journey that adds a custom property to the end user's session on successful authentication.

1. Sign on to the Advanced Identity Cloud admin console as a tenant administrator.

2. In the Advanced Identity Cloud admin console, click Journeys > Journeys.

3. Click [icon: add, set=material, size=inline] Add Journey, select Start from scratch, and then click Next.

4. Set the following before clicking Save:

   | Field           | Value                  |
   | --------------- | ---------------------- |
   | Name            | `SetSessionProperties` |
   | Identity Object | `managed/alpha_user`   |

5. Drag the following nodes onto the journey editor canvas:

   * [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html) containing:

     * [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)

     * [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)

   * [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)

   * [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/latest/set-session-properties.html)

6. Connect the nodes, clicking Save from time to time to keep your work:

   ![Login with session properties journey](_images/journey-session-properties/use-case-session-properties-journey.png)

7. Click the Set Session Properties node and add a session property:

   1. Click +, then Add + in the Properties modal.

   2. Enter `mySessionProperty` in the Key field and `customValue` in the Value field.

   3. Click Done.

   4. Click Save.

8. Click Save to save the journey.

### Task 2: Allowlist the session property

In this task, you provide access to the `mySessionProperty` property to allow it to be output in the ID token.

1. Under Native Consoles > Access Management, select Realms > alpha > Services > Session Property Whitelist Service.

2. Add `mySessionProperty` to the Allowlisted Session Property Names field.

3. Save your changes.

### Task 3: Create a custom claims script

In this task, you create a new OIDC claims script to map a session property claim.

1. In the Advanced Identity Cloud admin console, [create a new](../developer-docs/scripting-auth.html#create-a-new-auth-script) OIDC Claims script.

   |   |                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This example uses a legacy script. Find a next-generation example in [Example using a next-generation script](../am-oauth2/plugins-user-info-claims.html#example-oidc-claims-nextgen). |

2. Name the script `Demo OIDC claims`.

3. Edit the default JavaScript as follows:

   * In the `utils.setScopeClaimsMap` function call, add the `mySessionProperty` claim to a new scope named `myCustomScope`:

     ```javascript
     utils.setScopeClaimsMap({
            profile: [
                 'name',
                 'family_name',
                 'given_name',
                 'zoneinfo',
                 'locale'
             ],
             email: ['email'],
             address: ['address'],
             phone: ['phone_number'],
             myCustomScope: ['mySessionProperty']
     ```

   * In the `utils.setClaimResolvers` function call, insert `mySessionProperty` after the `phone_number` claim:

     ```javascript
     utils.setClaimResolvers({
             ...
             phone_number: utils.getUserProfileClaimResolver('telephonenumber'),
             mySessionProperty: function () {
                 return session.getProperty('mySessionProperty');
             }

         });
     ```

4. Save your changes.

The new claims script is now ready to retrieve a session property claim for `myCustomScope`.

### Task 4: Configure the OAuth 2.0 provider to return claims in the ID token

In this task, you configure the OAuth 2.0 provider to always return scope-derived claims in the ID token.

|   |                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This option is disabled by default because of the security concerns of returning claims that may contain sensitive user information. Learn more in [Request claims in ID tokens](../am-oidc1/understanding-openid-connect-scopes-and-claims.html#request-claims-tokens). |

1. In the Advanced Identity Cloud admin console, go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Advanced OpenID Connect.

2. Enable Always Return Claims in ID Tokens.

3. Save your changes.

### Task 5: Create an OIDC relying party profile

In this task, you create an OIDC relying party (client) profile that overrides the OAuth 2.0 provider settings. The override lets you test the script you created in Task 3 without affecting ID and access tokens issued to other applications.

Learn more in [Register a client application](../app-management/register-a-custom-application.html).

#### Create a confidential OAuth 2.0 client

1. In the Advanced Identity Cloud admin console, go to Applications > Applications and click + Custom Application.

2. Select the sign-in method as OIDC - OpenId Connect and application type as Web.

3. Create the application, providing the following details:

   * Name

     `myClient`

   * Owners

     `<resource-owner>`

   * Client ID

     `myClient`

   * Client Secret

     `mySecret`

4. Switch to the Sign On tab and under General Settings, make the following changes:

   * Sign-in URLs

     `https://www.example.com:443/callback`

   * Grant Types

     `Implicit`

   * Scopes

     `openid` `myCustomScope`

5. Click Show advanced settings, select the Access tab and make the following changes:

   * Response Types

     `token id_token`

6. Select the Authentication tab and make the following changes:

   * Token Endpoint Authentication Method

     `None`

7. Save your changes.

#### Override OAuth 2.0 provider settings for this client

1. Under Native Consoles > Access Management, select Realms > alpha > Applications > OAuth 2.0 > Clients > myClient, switch to the OAuth2 Provider Overrides tab and update the following settings:

   * Enable OAuth2 Provider Overrides

     Enabled

   * OIDC Claims Plugin Type

     `SCRIPTED`

   * OIDC Claims Script

     `Demo OIDC claims`

2. Save your changes.

Check in

At this point, you:

|                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------- |
| [icon: check, set=fa]Created a sign-on journey that captures a custom session property on successful authentication. |
| [icon: check, set=fa]Allowlisted the custom session property.                                                        |
| [icon: check, set=fa]Created an OIDC claims script to map the session property claim.                                |
| [icon: check, set=fa]Configured the OAuth 2.0 provider to always return scope-derived claims in the ID token.        |
| [icon: check, set=fa]Created an OIDC relying party to override the default OAuth 2.0 provider settings.              |
|                                                                                                                      |

## Validation

You are now ready to validate the use case by authenticating to the `Set session properties` journey as a test end user, and then calling the `/oauth2/idtokeninfo` endpoint to inspect the session property claim values.

### Steps

1. In an incognito window, enter the following URL:

   ```none
   https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize?client_id=myClient&response_type=id_token&scope=openid%20myCustomScope&redirect_uri=https://www.example.com:443/callback&service=SetSessionProperties&nonce=abc123&state=123abc (1)(2)(3)(4)
   ```

   |       |                                                                          |
   | ----- | ------------------------------------------------------------------------ |
   | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.     |
   | **2** | `myClient` is the name of the client you created in Task 5.              |
   | **3** | `openid` and `myCustomScope` are the scopes configured in your client.   |
   | **4** | `SetSessionProperties` is the name of the journey you created in Task 1. |

2. On the Sign in page, enter the username and password for your test end user and click Next.

3. Allow access to your account when prompted for consent.

4. After successful authentication, copy the value of the `id_token` in the URL. You'll need this value in the next step.

5. Call the [/oauth2/idtokeninfo](../am-oidc1/rest-api-oidc-idtoken-validation.html) endpoint to inspect the session property claim values, including the ID token obtained from the previous request:

   ```bash
   $ curl \
   --request POST \
   --user myClient:mySecret \
   --data 'id_token=<id-token>' \(1)
   "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/idtokeninfo" (2)
   ```

   |       |                                                                      |
   | ----- | -------------------------------------------------------------------- |
   | **1** | Replace \<id_token> with the id_token copied in step 4.              |
   | **2** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment. |

   Example output:

   ```json
   {
     "sub": "6bc9650a-05fa-400c-8529-98d4a701381d",
     "auditTrackingId": "7734d5b8-5ac5-4c21-a211-0a4dfc299dfd-624957",
     "subname": "6bc9650a-05fa-400c-8529-98d4a701381d",
     "iss": "https://<tenant-env-fqdn>:443/am/oauth2/realms/root/realms/alpha",
     "tokenName": "id_token",
     "nonce": "abc123",
     "sid": "5WoPI3klaBoa3K1MvjYpcKbe9/4Tm58dKX+gE501ZRw=",
     "aud": "myClient",
     "acr": "username-password",
     "org.forgerock.openidconnect.ops": "H-oyuSQJJCY46ObWRGM5ULmwF8I",
     "s_hash": "3RMKhJ17KeVUGwXS9_hqSg",
     "azp": "myClient",
     "auth_time": 1734864493,
     "mySessionProperty": "customValue", (1)
     "realm": "/alpha",
     "exp": 1734868156,
     "tokenType": "JWTToken",
     "iat": 1734864556
   }
   ```

   |       |                                                                                |
   | ----- | ------------------------------------------------------------------------------ |
   | **1** | `mySessionProperty` is the custom session property you defined in the journey. |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you use PingGateway to consume the resulting ID token, the session property might be null. This can happen when the ID token is issued successfully with the custom claim containing your session property. Subsequently, PingGateway makes a call to `/userinfo`, which causes the OIDC claims script to be invoked again, but this time there is no session, which leads to a null session property.If you experience this issue, modify the OIDC claims script to ensure it only adds claims when a session exists. |

## Explore further

### Reference material

| Reference                                                                 | Description                                                                            |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [Journeys](../journeys/journeys.html)                                     | Conceptual information on journeys and their purpose in Advanced Identity Cloud.       |
| [Journeys](../journeys/journeys.html)                                     | Learn about the configurable nodes Advanced Identity Cloud offers for use in journeys. |
| [Claims](../am-oidc1/understanding-openid-connect-scopes-and-claims.html) | Learn about OIDC claims and ID tokens in Advanced Identity Cloud.                      |
| [OIDC claims](../am-oauth2/plugins-user-info-claims.html)                 | Learn about modifying and overriding claims in an ID token in Advanced Identity Cloud. |

### Nodes used

|   |                                                                         |
| - | ----------------------------------------------------------------------- |
|   | The following nodes are listed in the order they appear in the journey. |

* [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html) containing:

  * [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)

  * [Platform Password node](https://docs.pingidentity.com/auth-node-ref/latest/platform-password.html)

* [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/data-store-decision.html)

* [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/latest/set-session-properties.html)
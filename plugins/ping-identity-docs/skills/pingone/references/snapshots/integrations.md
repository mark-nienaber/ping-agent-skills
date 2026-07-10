---
title: Adding the RADIUS Gateway service
description: Download the ZIP archive and extract it to the computer that will run the gateway.
component: pingone
page_id: pingone:integrations:p1_add_radius_gateway_windows_service
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_radius_gateway_windows_service.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 8, 2024
section_ids:
  steps: Steps
---

# Adding the RADIUS Gateway service

Download the ZIP archive and extract it to the computer that will run the gateway.

## Steps

1. In the PingOne admin console, go to **Integrations → Gateways**.

2. Click the appropriate gateway entry to open the details panel.

3. Click the **Download** tab.

4. Click the download link to download the `.zip` archive.

5. Extract the `.zip` archive to the computer that will run the gateway. We recommend that you use a common location as the parent directory, such as `C:\Program Files\Ping Identity`.

6. Follow the instructions in the `README.txt` file to:

   1. Configure the `run.properties` file, including providing the gateway credential information. The run.properties file is located in the config directory. For example: `C:\Program Files\Ping Identity\pingone-radius-gateway-1.2.0\config`.

   2. (Optional) To configure a RADIUS Gateway client application to use a forward web proxy server to handle traffic between the gateway and PingOne, in the `run.properties` file provide the relevant access information.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | * You must configure the web proxy settings locally for each running instance. For example, if you are running two gateway client applications, you must configure web proxy settings for each instance separately.

      * For basic authentication to support international characters, the proxy server must also be configured to support international characters.

      * Digest authentication does not support the use of international characters. |

7. Sign on to Windows with administrator privileges.

8. Start a Command Prompt or PowerShell.

9. Run the `install-service.bat` file without any parameters. By design, the `install-service.bat` file does not start the service automatically after completion. However, the service is configured to start automatically at the next and subsequent restarts of the Windows operating system.

10. In the Services system application, start the PingOne RADIUS Gateway service.

---

---
title: Authentication for Authorize gateway endpoints
description: Configure shared secret client authentication for Authorize gateway endpoints.
component: pingone
page_id: pingone:integrations:p1_authenicate_authz_gateway_endpoints
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_authenicate_authz_gateway_endpoints.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2026
---

# Authentication for Authorize gateway endpoints

To enhance security for certain endpoints, the gateway instance can enforce client authentication using a shared secret.

Shared secrets are enforced per gateway instance and not shared between instances. To define a shared secret, use one of the available [configuration methods](p1_configure_authz_gateway_instance.html) to pass the authentication JSON object to your gateway instance.

Example `authentication` object:

```json
{
  "authentication": {
    "type": "sharedsecret",
    "keys": ["example-secret-key"]
  }
}
```

Configuration properties for the `authentication` object:

* `type`: A constant set to `sharedsecret`.

* `keys`: An array containing shared secrets as strings.

|   |                                        |
| - | -------------------------------------- |
|   | Secret keys must be at least 128 bits. |

To avoid service interruptions, the gateway instance allows authenticated endpoints to accept multiple, distinct shared secrets at the same time. This allows time to update the gateway instance's configuration to use a new shared secret.

For example:

```json
{
  "authentication": {
    "type": "sharedsecret",
    "keys": ["example-secret", "example-secret-2"]
  }
}
```

After it's enabled, the gateway instance will require authentication for the following endpoints:

* `/api/authorize`

* `/actuator/state`

* `/actuator/metrics`

  * `/actuator/metrics/*`

Any request made to these endpoints must provide the configured shared secret with the `Authorization` header.

For example:

```
curl --location 'http://localhost:8080/api/authorize' \
  --header 'Authorization: Bearer example-secret' \
  --header 'Content-Type: application/json' \
  --data '
{
  "parameters": {
    "Amount": "990",
    "Account": "Basic checking",
    "Payment.consentId": "{{consentID}}"
  }
}'
```

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | If you have defined multiple shared secrets for secret rotation, the `Authorization` header can include any of these secrets. |

Authentication is not supported for the following endpoints:

* `/actuator`

* `/actuator/health`

  * `/actuator/health/liveness`

  * `/actuator/health/readiness`

---

---
title: Authoritative identity providers
description: An authoritative identity provider (IdP) in PingOne is the IdP that has authority over user credentials and defines where a user authenticates.
component: pingone
page_id: pingone:integrations:p1_authoritative_idps
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_authoritative_idps.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 24, 2025
section_ids:
  setting-the-idp: Setting the IdP
  just-in-time-provisioning: Just-in-time provisioning
  identifier-first-authentication: Identifier-first authentication
  related-links: Related links
---

# Authoritative identity providers

An authoritative identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* is the IdP that has authority over user records and credentials and defines where a user normally authenticates. By default, PingOne is a user's authoritative IdP, meaning users authenticate with a PingOne username and password.

If a user authenticates from an external IdP that's different from their authoritative IdP set in PingOne, and they do not have an existing account link for that IdP, the user must link their account by signing on through the authoritative IdP first (for example, by entering their PingOne username and password). This creates an account link between the external IdP and the PingOne user. Learn more in [Adding an external identity provider sign-on step](../authentication/p1_add_idp_signon_step.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For a user to link their account with multiple external IdPs, their authoritative IdP must be set to PingOne. Account linking only applies when the user's authoritative IdP is PingOne.If a user's authoritative IdP is PingOne, but they don't have a PingOne password, the user can't sign on through an external IdP and can't link their account between the external IdP and PingOne. This can occur when users are created through an external integration that does not set an authoritative IdP or password, such as through the PingID or PingOne MFA adapters for PingFederate. This can also occur with any other custom integration that creates users without setting an authoritative IdP or password. |

## Setting the IdP

The authoritative IdP can be set either on the user or on a population in PingOne. Setting the authoritative IdP on a population means that all users in that population whose authoritative IdP is not set explicitly on the user record will use the authoritative IdP set on the population. If the user record does not include an authoritative IdP, and the user is not part a population that has an authoritative IdP applied, the authoritative IdP defaults to PingOne.

For example, if you're using the PingID or PingOne MFA adapters, users can be created by the adapters without an authoritative IdP or password, and they cannot sign on to PingOne. In this scenario, setting the authoritative IdP as PingFederate for that population applies the authoritative IdP to the users created by the adapters. Learn more in [Adding a user in PingOne](../directory/p1_adduser.html) and [Managing populations](../directory/p1_manage_populations.html).

You can change a user's authoritative IdP in the PingOne admin console or using the API. For example, if a user's authoritative IdP is PingOne but you want them to authenticate through an external IdP without needing a PingOne password, set their authoritative IdP to that external IdP. Learn more about using the API in [Update User Identity Provider](https://developer.pingidentity.com/pingone-api/platform/users/users-1/update-user-identity-provider.html).

### Just-in-time provisioning

With just-in-time (JIT) provisioning, you can automate user registration and account creation. If a user authenticates through an external IdP that has registration enabled, and the user doesn't already exist in PingOne, the user is automatically created through JIT provisioning without their authoritative IdP set to the external IdP.

Users that are JIT provisioned automatically have the authoritative IdP configured and linked with the user account at the IdP.

To enable JIT provisioning, you must select a population when you configure a new external IdP or edit an existing external IdP. Selecting a population enables JIT provisioning for the configured IdP and overrides the population set in the authentication policy in the **Enable registration** section. Learn more in [Configuring an authoritative identity provider](p1_configure_authoritative_idp.html).

## Identifier-first authentication

With identifier-first authentication, you can identify users before you authenticate them. If the user has an authoritative IdP, PingOne redirects the user to that IdP for authentication after they enter their email or username.

If a user account in PingOne is preregistered and the user authenticates through their authoritative IdP for the first time, PingOne links the user account without requiring the user to verify their account or password. If you use a login authentication step instead, users must choose their IdP from a list that you can configure. Learn more in [Adding an identifier first authentication step](../authentication/p1_add_identifier_first_auth.html) and [Adding a login authentication step](../authentication/p1_add_login_auth_step.html).

## Related links

* [External IdPs](p1_external_idps.html)

* [Authentication policies](../authentication/p1_authenticationpolicies.html)

* [Configuring an authoritative identity provider](p1_configure_authoritative_idp.html)

---

---
title: Authorize gateway support lifecycle
description: Stay informed about the Authorize gateway support lifecycle to ensure continued access to the latest features and technical support.
component: pingone
page_id: pingone:integrations:p1_authz_gateway_support_lifecycle
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_authz_gateway_support_lifecycle.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 26, 2025
section_ids:
  support-policy: Support policy
  faqs: FAQs
---

# Authorize gateway support lifecycle

Stay informed about the Authorize gateway support lifecycle to ensure continued access to the latest features and technical support. Regular upgrades of your gateway versions help maintain optimal performance and compatibility.

## Support policy

Ping Identity supports an Authorize gateway version for 1 year after a newer gateway version is released. The end of support date is rounded to the end of the month. After support ends, the version is no longer guaranteed to work with PingOne APIs and might not be usable.

For example:

* Authorize gateway version 1.0.0 was released on January 20, 2025.

* The release of the next version (1.1.0) on August 27, 2025 initiates the 1-year support window for version 1.0.0 and sets its end of support date to August 31, 2026.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Read One Gateway and Read All Gateways endpoints provide the `supportEndsOn` date and number of `daysUntilSupportEnds` for each gateway version. Learn more in [Read All Gateways](https://developer.pingidentity.com/pingone-api/platform/gateway-management/gateways/read-all-gateways.html) and [Read One Gateway](https://developer.pingidentity.com/pingone-api/platform/gateway-management/gateways/read-one-gateway.html) in the PingOne Platform API Reference documentation. |

Previous gateway versions aren't updated. Instead, any improvements are released in a new gateway version.

You can find version history and end of support dates in [Authorize gateway version history](p1_authz_gateway_version_history.html).

## FAQs

> **Collapse: How long is a version supported?**
>
> Authorize gateway versions are supported for 1 year after the release of a newer gateway version, rounded to the end of the month. For example, when a new version is released on August 27, 2025, the previous version is supported until August 31, 2026.

> **Collapse: What happens if I use a version that's no longer supported?**
>
> You can continue to use an unsupported version; however, you won't have access to the latest features. If you have problems with an unsupported version, you must [upgrade](p1_upgrade_authz_gateway_instance.html) to a newer version that's supported.
>
> After support ends, the Authorize gateway version is no longer guaranteed to work with PingOne APIs and might not be usable.

> **Collapse: How do I get the latest Authorize gateway features?**
>
> Upgrade your gateway instances to take advantage of features in the latest version. You must upgrade each gateway instance and restart each container.
>
> Learn more in [Upgrading an Authorize gateway instance](p1_upgrade_authz_gateway_instance.html).

> **Collapse: Can I upgrade a gateway instance if its version is still supported?**
>
> Yes, you can upgrade as soon as a newer version is released. This allows you to use the latest features.

> **Collapse: What if I have a problem with a new version?**
>
> If you experience an issue after upgrading, check [version history](p1_authz_gateway_version_history.html) for known limitations. If the problem persists, contact [Ping Identity Support](https://support.pingidentity.com/s/) for assistance.
>
> As a temporary workaround, you can roll back to the previous version until the issue is resolved.

> **Collapse: I'm currently using a trial version of PingOne. What happens when my trial ends?**
>
> To continue using PingOne, contact your account representative for licensing options.

---

---
title: Authorize gateway version history
description: History of Authorize gateway versions, including release dates, highlights, limitations, and end of support information.
component: pingone
page_id: pingone:integrations:p1_authz_gateway_version_history
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_authz_gateway_version_history.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 15, 2026
keywords: ["version history", "authorize gateway", "limitations", "support"]
section_ids:
  version-1-2-1: Version 1.2.1
  highlights: Highlights
  security-updates: Security updates
  gateway-instance-startup-message: Gateway instance startup message
  structured-errors-for-invalid-decision-requests: Structured errors for invalid decision requests
  limitations: Limitations
  policies: Policies
  information-points: Information points
  version-1-2-0: Version 1.2.0
  highlights-2: Highlights
  bulk-decision-requests: Bulk decision requests
  enhanced-logging: Enhanced logging
  limitations-2: Limitations
  policies-2: Policies
  information-points-2: Information points
  version-1-1-0: Version 1.1.0
  highlights-3: Highlights
  policy-authoring: Policy authoring
  administrator-permissions: Administrator permissions
  logging: Logging
  additional-enhancements: Additional enhancements
  limitations-3: Limitations
  policies-3: Policies
  information-points-3: Information points
  version-1-0-0: Version 1.0.0
  highlights-4: Highlights
  limitations-4: Limitations
  policies-4: Policies
  information-points-4: Information points
---

# Authorize gateway version history

This page provides details about Authorize gateway versions, including release dates, a summary of features and known limitations, and critical end-of-support information for each version.

Learn more about gateway support policies in [Authorize gateway support lifecycle](p1_authz_gateway_support_lifecycle.html).

You can find information about upgrading gateway versions in [Upgrading an Authorize gateway instance](p1_upgrade_authz_gateway_instance.html).

## Version 1.2.1

| Milestone | Date         |
| --------- | ------------ |
| Release   | May 21, 2026 |

### Highlights

#### Security updates

We've updated underlying runtime components to address potential security vulnerabilities in the HTTP network stack and Docker base image.

#### Gateway instance startup message

To help manage Authorize gateways across multiple environments, gateway instances now log identifying information on startup for the associated gateway and PingOne environment. Learn more in [Startup logging](p1_logging_authz_gateway_instances.html#p1_az_gateway_startup_logging).

#### Structured errors for invalid decision requests

Gateway instances now return structured, field-level error responses for invalid `userContext` values in decision requests. Previously, such requests returned a generic error message without identifying the specific field or validation failure.

### Limitations

The following features aren't supported for Authorize gateway deployments:

* Calls to gateway instances from the PingOne Authorize DaVinci connector.

* API Access Management in PingOne Authorize.

* The **Authorization Dashboard** doesn't track metrics for decision evaluations made by gateway instances.

#### Policies

The following policy features aren't supported:

* The **Has Permissions** condition comparator in policies and rules.

* Attributes listed under **PingOne > API Access Management** on the **Attributes** tab.

#### Information points

The following features aren't supported:

* You can't use an **LDAP Gateway** service to access user information stored in a self-managed LDAP directory.

* When [testing services](../authorization_using_pingone_authorize/p1_az_testing_tf_elements.html), you can't test calls to your local or private services. However, you can use overrides to mock the service response.

## Version 1.2.0

| Milestone            | Date               |
| -------------------- | ------------------ |
| Release              | September 30, 2025 |
| End of support       | May 31, 2027       |
| Support notification | May 21, 2026       |

### Highlights

#### Bulk decision requests

Authorize gateway instances now support bulk decision requests, allowing you to evaluate multiple access scenarios with a single API call. Bulk requests reduce both network overhead and overall decision latency, improving performance in high-throughput environments.

Learn more in [Making decision requests to Authorize gateway instances](p1_make_decision_requests_to_authz_gateway_instances.html).

#### Enhanced logging

When you start a gateway instance that doesn't support features in the authorization policy version published to the gateway, the system now logs a detailed error message. This message explains that the instance can't retrieve the PingOne configuration and directs you to upgrade to a supported version.

Learn more in [Logging for Authorize gateway instances](p1_logging_authz_gateway_instances.html).

### Limitations

The following features aren't supported for Authorize gateway deployments:

* Calls to gateway instances from the PingOne Authorize DaVinci connector.

* API Access Management in PingOne Authorize.

* The **Authorization Dashboard** doesn't track metrics for decision evaluations made by gateway instances.

#### Policies

The following policy features aren't supported:

* The **Has Permissions** condition comparator in policies and rules.

* Attributes listed under **PingOne > API Access Management** on the **Attributes** tab.

#### Information points

The following features aren't supported:

* You can't use an **LDAP Gateway** service to access user information stored in a self-managed LDAP directory.

* When [testing services](../authorization_using_pingone_authorize/p1_az_testing_tf_elements.html), you can't test calls to your local or private services. However, you can use overrides to mock the service response.

## Version 1.1.0

| Milestone            | Date               |
| -------------------- | ------------------ |
| Release              | August 27, 2025    |
| End of support       | October 31, 2026   |
| Support notification | September 30, 2025 |

### Highlights

#### Policy authoring

Authorize gateways now support:

* The **Is Member Of** and **Is Not Member Of** condition comparators in policies and rules

* **User** attributes listed under **PingOne** on the **Attributes** tab

* The **PingOne User** and **PingOne User ID** resolvers in attributes

#### Administrator permissions

* The new **Authorize Gateway Policy Evaluator** built-in role is automatically assigned to Authorize gateways. This role provides least-privilege permissions for reading Authorize gateways and authorization deployments.

* To grant an Authorize gateway additional policy evaluation permissions, such as reading user details, checking group membership, and evaluating risk scores, create a custom role on the new **Roles** tab.

Learn more about built-in and custom roles in [Managing Authorize gateway roles](p1_manage_authz_gateway_roles.html).

#### Logging

* Authorize gateways now log all service calls made to PingOne. You can use entries in the `PINGONE_SERVICE_AUDIT` log to monitor and troubleshoot policy interactions with PingOne, such as user attribute resolution and group membership checks.

* As in the previous version, logs are omitted when they include sensitive terms. You can set `logging.allowSensitiveMaterial:true` to disable log filtering.

Learn more in [Logging for Authorize gateway instances](p1_logging_authz_gateway_instances.html).

#### Additional enhancements

* You can now use a **Connector** type service to provide risk signals to gateway instances. Learn more in [Connecting to PingOne Protect](../authorization_using_pingone_authorize/p1_az_connecting_p1_risk.html).

* Service caching TTLs and timeouts for PingOne calls are now configurable. Learn more in [Service caching and timeouts for Authorize gateway instances](p1_service_caching_authz_gateway_instances.html).

### Limitations

The following features aren't supported for Authorize gateway deployments:

* Calls to gateway instances from the PingOne Authorize DaVinci connector.

* API Access Management in PingOne Authorize.

* The **Authorization Dashboard** doesn't track metrics for decision evaluations made by gateway instances.

#### Policies

The following policy features aren't supported:

* The **Has Permissions** condition comparator in policies and rules

* Attributes listed under **PingOne > API Access Management** on the **Attributes** tab

Policy features that rely on PingOne might increase decision request latency. These include:

* **PingOne User** and **PingOne User ID** attribute resolvers

* **Is Member Of** and **Is Not Member Of** condition comparators

* PingOne Protect **Connector** services that provide risk information to gateway instances

If your policies include these features, you must assign a built-in or custom administrator role to the Authorize gateway to give it additional permissions in PingOne. Learn more in [Managing Authorize gateway roles](p1_manage_authz_gateway_roles.html).

#### Information points

The following features aren't supported:

* You can't use an **LDAP Gateway** service to access user information stored in a self-managed LDAP directory.

* When [testing services](../authorization_using_pingone_authorize/p1_az_testing_tf_elements.html), you can't test calls to your local or private services. However, you can use overrides to mock the service response.

## Version 1.0.0

| Milestone            | Date             |
| -------------------- | ---------------- |
| Release              | January 20, 2025 |
| End of support       | August 31, 2026  |
| Support notification | August 27, 2025  |

### Highlights

Version 1.0.0 is the first Authorize gateway release.

To reduce authorization latency, you can deploy authorization policies managed in PingOne to Authorize gateway instances located on-premise or in your private cloud. In highly regulated environments, this ensures data privacy by keeping sensitive data for authorization decisions within your secure trust boundary.

### Limitations

The following features aren't supported in version 1.0.0:

* Calls to gateway instances from the PingOne Authorize DaVinci connector.

* API Access Management in PingOne Authorize.

* The **Authorization Dashboard** doesn't track metrics for decision evaluations made by gateway instances.

#### Policies

You can use many of the policy authoring features available in PingOne Authorize. However, the following features aren't supported in version 1.0.0:

* The **Has Permissions**, **Is Member Of**, and **Is Not Member Of** condition comparators in policies and rules

* Attributes listed under **PingOne** on the **Attributes** tab, including **User** and **API Access Management** attributes

* The **PingOne User** and **PingOne User ID** resolvers in attributes

#### Information points

You can make calls to information points and self-managed services directly from gateway instances. When you [set up an HTTP service](../authorization_using_pingone_authorize/p1_az_connecting_an_http_service.html) in PingOne, use URLs for your local or private services instead of public URLs.

The following features aren't supported:

* You can't use an **LDAP Gateway** service to access user information stored in a self-managed LDAP directory.

* You can't use a **Connector** service to provide risk information to gateway instances.

* When [testing services](../authorization_using_pingone_authorize/p1_az_testing_tf_elements.html), you can't test calls to your local or private services. However, you can use overrides to mock the service response.

---

---
title: Authorize gateways
description: Authorize gateways combine the advantages of centralized policy administration with the benefits of self-managed decision evaluation and enforcement.
component: pingone
page_id: pingone:integrations:p1_authz_gateways
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_authz_gateways.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  how-authorize-gateways-work: How Authorize gateways work
---

# Authorize gateways

Authorize gateways combine the advantages of centralized policy administration with the benefits of self-managed decision evaluation and enforcement.

An Authorize gateway acts as a bridge between policy management components in PingOne and runtime gateway instances in your organization's infrastructure or cloud data center. Gateway instances have a small footprint and are easy to deploy across your staging pipelines.

Authorize gateways provide the following benefits:

* Cloud administration of policies

  Use the latest features of the admin console for policy authoring and management in one place, without having to manage a policy administration point in your infrastructure.

* Reduced latency

  Minimize latency by deploying multiple gateway instances alongside the resources you are protecting.

  Authorize gateways excel in high-volume, low-latency scenarios, such as high-throughput transactions or API traffic. You can deploy policy-enforcing applications and decision evaluation gateway instances in close proximity, eliminating the need for traffic to flow through the PingOne platform.

* Data residency

  If compliance and security considerations make self-managed deployment a requirement for your application, gateway instances enable access to your self-managed datastores without exposing sensitive data outside of your organization's infrastructure.

* Privacy for internal services

  Gateway instances can call private HTTP services within your network for authorization context, without exposing those services to the public internet.

## How Authorize gateways work

Authorize gateway instances process authorization decisions within the boundaries of your network and under your control, while policy management and deployment services run in the cloud-based PingOne platform.

The following components are involved:

![Flow diagram showing the components involved in an Authorize gateway flow.](_images/p1-az-gateway-diagram.png)

**Management in PingOne**

| Component                   | Description                                                                                                                                                                                                                                                                                                                                           |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Policy administration point | PingOne Authorize serves as the centralized policy administration point where you configure and manage authorization policies and the attributes and services that provide context in authorization decisions.Learn more about PingOne Authorize in [Introduction to Authorization](../authorization_using_pingone_authorize/p1az_introduction.html). |
| Authorize gateway           | The Authorize gateway communicates between PingOne and gateway instances in your organization's infrastructure. Use Authorize gateways to publish authorization policy versions to gateway instances and keep them up-to-date.                                                                                                                        |

**Self-managed decision evaluations**

| Component                 | Description                                                                                                                                                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Gateway instances         | Authorize gateway instances evaluate authorization policy versions published from PingOne in order to make authorization decisions.Gateway instances are distributed as containerized images, and they maintain a WebSocket Secure connection with the PingOne platform. |
| Information points        | Information points are HTTP services that provide context for authorization decisions.Information points can be publicly available services or services maintained in your infrastructure.                                                                               |
| Policy enforcement points | Enforcement points are applications that consume authorization decisions. They're maintained by your organization in your infrastructure.                                                                                                                                |

A WebSocket Secure connection maintains two-way communication between Authorize gateways in PingOne and gateway instances in your infrastructure as follows:

* PingOne sends gateway configuration changes to gateway instances.

* Gateway instances send errors and alerts, error logs, health state, and metrics to PingOne.

  |   |                                                                                                                                                                                                                                                                                                                                 |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Error logs and metrics are collected for monitoring purposes only. This information isn't exposed in the PingOne admin console, except for CPU **% busy** and **Transaction time**.Gateway instances initiate the WebSocket connection, ensuring that you don't have to open inbound firewalls in your network to this traffic. |

Authorize gateways use publicly authenticated HTTPS APIs in PingOne for the following:

* Token exchange to get an access token for PingOne APIs

* Downloading authorization policy version deployments

* PingOne service calls to get user details, group memberships, and risk information

---

---
title: Before configuring an LDAP gateway
description: Review these prerequisites before setting up an LDAP gateway in PingOne.
component: pingone
page_id: pingone:integrations:p1_gateway_prereqs
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_gateway_prereqs.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 7, 2024
section_ids:
  details-about-the-directory: Details about the directory
  system-requirements: System requirements
  gateway-access: Gateway access
  pingone-user-privileges: PingOne user privileges
  forward-web-proxy-server: Forward web proxy server
---

# Before configuring an LDAP gateway

Before you set up an LDAP *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* gateway, ensure that you have:

* LDAP or AD servers and their TLS certificates.

* A runtime environment that meets the minimum requirements.

* An administrator account in PingOne.

* (Optional) a forward proxy server.

## Details about the directory

You'll need the following information about the LDAP directory:

* The host name and port for all server instances.

* A service account from the directory server that the PingOne gateway will use to access the directory (`bind DN` and `bind password`).

  Learn more about configuring the service account and granting the required permissions in [Creating a service account for LDAP gateways](p1_creating_service_account_ldap_gateway.html).

  |   |                                                                                    |
  | - | ---------------------------------------------------------------------------------- |
  |   | The service account must be able to search for users in the directory by username. |

* Whether the directory instances support TLS and StartTLS. If the TLS certificates for the servers were signed by a non-default certificate authority (CA) *(tooltip: \<div class="paragraph">
  \<p>An entity that issues digital certificates.\</p>
  \</div>)*, you must have the CA's signing certificates available to upload to PingOne. Learn more in [Importing an LDAP certificate to PingOne](p1_import_ldap_certificate.html).

* A method for correlating a directory user with a PingOne user, including the base DN for issuing searches against the directory and the attribute that corresponds to the PingOne `username` attribute.

## System requirements

You can run the gateway in a Docker container, as a standalone Java application, or as a Windows application.

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The LDAP gateway is OS-agnostic. As long as the environment supports Docker or the required Java, the gateway can be deployed on various Linux distributions, Windows Server versions, or cloud-native environments. |

The computer, virtual machine, or Docker environment must have the following resources dedicated to the gateway:

| Resource  | Requirement              |
| --------- | ------------------------ |
| Processor | Two CPUs or virtual CPUs |
| RAM       | 1 GB                     |
| Storage   | 1 GB                     |

* Docker: If you plan to run the gateway in a Docker container, you must have Docker installed on the computer that will run the gateway.

* Java: If you plan to run the gateway as a standalone Java or Windows application, verify the Java version is Java 21 LTS or Java 25 LTS.

## Gateway access

The gateway requires access to the LDAP directory server over the network as well as the ability to initiate outbound requests over the internet to establish a WebSocket Secure connection to PingOne.

The WebSocket Secure address varies depending on your geography. Ensure that the gateway can access the WebSocket Secure address for your geography, as listed in the following table.

If provisioning will be used, the gateway must be able to establish an outbound connection to the API endpoints for your geography, as listed in the following table. Learn more in [Creating an LDAP gateway provisioning connection](p1_create_provisioning_connection_gateway.html).

| Geography                                                                   | Address                                                                                                           | API Endpoints                         |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| Australia                                                                   | wss\://gateways.pingone.com.au/wss\://gateways-ap-southeast-2.pingone.com.au/                                     | auth.pingone.com.auapi.pingone.com.au |
| Canada                                                                      | wss\://gateways.pingone.ca/wss\://gateways-ca-central-1a.pingone.ca/wss\://gateways-ca-central-1b.pingone.ca/     | auth.pingone.caapi.pingone.ca         |
| Europe                                                                      | wss\://gateways.pingone.eu/wss\://gateways-eu-central-1.pingone.eu/wss\://gateways-eu-west-1.pingone.eu/          | auth.pingone.euapi.pingone.eu         |
| North America (US)                                                          | wss\://gateways.pingone.com/wss\://gateways-us-east-2.pingone.com/wss\://gateways-us-west-2.pingone.com/          | auth.pingone.comapi.pingone.com       |
| Singapore                                                                   | wss\://gateways.pingone.sg/wss\://gateways-ap-southeast-1y.pingone.sg/wss\://gateways-ap-southeast-1z.pingone.sg/ | auth.pingone.sgapi.pingone.sg         |
| Asia Pacific (legacy)&#xA;&#xA;Available only for existing .asia customers. | wss\://gateways.pingone.asia/wss\://gateways-ap-southeast-2.pingone.asia/                                         | auth.pingone.asiaauth.pingone.asia    |

## PingOne user privileges

The administrator setting up the gateway must have the **Environment admin** role. To confirm, open the PingOne console, locate the administrator identity, and confirm its roles.

## Forward web proxy server

You can optionally configure the client application to use a forward web proxy server to handle WebSocket traffic between the gateway client and PingOne. You'll need to provide:

* The IP address and the port of the web proxy

* Access credentials if the web proxy requires authentication. An LDAP gateway client version of 3.3.0 or higher is required.

|   |                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - The web proxy server must support the WebSocket protocol.

- Digest authentication does not support international characters.

- Basic authentication requires configuration in the proxy server to support international characters. |

Learn more about configuring a web proxy in [Starting a gateway instance](p1_starting_gateway_instance_ldap.html).

---

---
title: Before you begin configuring a RADIUS gateway
description: Review these prerequisites before setting up a RADIUS gateway in PingOne.
component: pingone
page_id: pingone:integrations:p1_radius_gateway_prereqs
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_radius_gateway_prereqs.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 30, 2024
section_ids:
  prerequisites: Prerequisites
  docker: Docker
  system-requirements: System requirements
  gateway-access: Gateway access
  pingone-user-privileges: PingOne user privileges
---

# Before you begin configuring a RADIUS gateway

Before you start setting up a gateway, ensure that you have the following information.

## Prerequisites

To enable communication between PingOne Remote Authentication Dial-In User Service (RADIUS) *(tooltip: \<div class="paragraph">
\<p>A client/server networking protocol providing centralized user management.\</p>
\</div>)* gateway and your RADIUS clients, you'll need:

* To add the PingOne DaVinci service to your PingOne environment.

* A RADIUS Client IP and Shared Secret for each RADIUS client.

* A DaVinci flow with a DaVinci policy. You should add the RADIUS gateway connector, the PingID connector, and use an out-of-the-box RADIUS gateway flow. Learn more in the [PingOne RADIUS gateway connector](https://docs.pingidentity.com/connectors/p1_radius_gateway_connector.html) documentation. Learn more about PingOne DaVinci policies in [DaVinci flow policies](https://docs.pingidentity.com/davinci/applications/davinci_flow_policies.html).

* (Optional) If you want to perform multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
  \<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
  \</div>)* using PingID, you'll also need to configure the RADIUS gateway in a PingOne environment that has PingID linked as a service.

* RADIUS gateway currently supports PAP, MS-CHAP v2, and EAP-MSCHAPv2 protocols. If you want to use the MS-CHAP v2, or EAP-MS-CHAP v2 protocol, you need a Network Policy Server (NPS). You'll also need to enable users to enter an one-time passcode (OTP) *(tooltip: \<div class="paragraph">
  \<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
  \</div>)* with their username. Learn more in [Enable users to enter an OTP with their username in MS-CHAP v2, or EAP-MSCHAPv2 mode](p1_enable_users_to_enter_otp_with_username.html).

* (Optional) When using the PAP protocol, you can also incorporate an NPS into a flow.

## Docker

You can run the gateway in a Docker container or as a standalone Java application. If you plan to run the gateway in a Docker container, ensure that you have Docker installed on the computer that will run the gateway.

## System requirements

The computer, virtual machine, or Docker environment that will run the gateway should have the following resources dedicated to the gateway:

* Processor: 2 CPUs or virtual CPUs

* RAM: 1 GB

* Storage: 1 GB

## Gateway access

The gateway requires access to the RADIUS client over the network as well as the ability to initiate outbound requests over the internet to establish a WebSocket Secure connection to PingOne.

The WebSocket Secure address varies depending on your geography. Ensure that the gateway can access the WebSocket Secure address for your geography.

| Geography                                                                   | Address                                                                                                           |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Australia                                                                   | wss\://gateways.pingone.com.au/wss\://gateways-ap-southeast-2.pingone.com.au/                                     |
| Canada                                                                      | wss\://gateways.pingone.ca/wss\://gateways-ca-central-1a.pingone.ca/wss\://gateways-ca-central-1b.pingone.ca/     |
| Europe                                                                      | wss\://gateways.pingone.eu/wss\://gateways-eu-central-1.pingone.eu/wss\://gateways-eu-west-1.pingone.eu/          |
| North America (US)                                                          | wss\://gateways.pingone.com/wss\://gateways-us-east-2.pingone.com/wss\://gateways-us-west-2.pingone.com/          |
| Singapore                                                                   | wss\://gateways.pingone.sg/wss\://gateways-ap-southeast-1y.pingone.sg/wss\://gateways-ap-southeast-1z.pingone.sg/ |
| Asia Pacific (legacy)&#xA;&#xA;Available only for existing .asia customers. | wss\://gateways.pingone.asia/wss\://gateways-ap-southeast-2.pingone.asia/                                         |

## PingOne user privileges

The administrator setting up the gateway should have the `Environment admin` role. To confirm, open the PingOne console, locate the administrator identity, and confirm its roles.

---

---
title: Clearing credentials
description: If you suspect that your credentials are out of date or compromised, you can clear all previously retained service account credentials.
component: pingone
page_id: pingone:integrations:p1_clearing_credentials
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_clearing_credentials.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 7, 2023
section_ids:
  steps: Steps
---

# Clearing credentials

If you suspect that your credentials are out of date or compromised, you can clear all previously retained service account credentials.

## Steps

1. Go to **Integrations → Gateways**.

2. Select the applicable gateway configuration.

3. Click the **Connection** tab and then click **Edit**.

4. Clear the **Retain Previous Credentials** checkbox.

5. Enter a new password into the **Service Account Password** field.

6. Click **Save**.

7. Ask the Active Directory admin to update the service account password in Active Directory. Shortly after the AD admin updates the password in AD, the INFO alert disappears from the PingOne admin console.

---

---
title: Cloning a rule
description: Clone an existing provisioning rule in PingOne.
component: pingone
page_id: pingone:integrations:p1_provisioning_cloning_rule
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_provisioning_cloning_rule.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2026
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Cloning a rule

Cloning an existing provisioning rule reduces repetitive configuration, minimizes manual entry errors, and repurposes complex logic for different groups or attributes.

Cloning a rule can be beneficial in the following situations:

* **Onboarding new applications**: Quickly set up a new application that requires the same mappings as an existing one. You can then make minor adjustments, such as a different target connection or a specific group filter, as needed.

* **Safe testing and improvement**: Safely test new changes, such as mapping or filter improvements, by cloning a rule that's already in use. This lets you try out ways to fix errors or make things run faster without changing your current setup.

|   |                                                       |
| - | ----------------------------------------------------- |
|   | You can only clone rules within the same environment. |

## Steps

1. In the PingOne admin console, go to **Integrations > Provisioning**.

2. On the **Rules** tab, find the appropriate rule and click the **More Options (⋮)** icon.

3. Click **Clone Rule** and then click **Continue** in the confirmation modal.

   |   |                                                                                       |
   | - | ------------------------------------------------------------------------------------- |
   |   | PingOne allows only one enabled inbound rule with a specific configuration at a time. |

   ### Result:

   A new disabled rule using the naming convention **Clone\_\<Rule name>** is created. If a clone with that name already exists, PingOne automatically adds a numeric suffix. For example, **Clone\_\<Rule name> (2)**.

4. (Optional) Give the clone a unique, descriptive name to avoid confusion with the original.

5. Review the settings of the cloned rule and verify copied mappings, filters, and connection references are what you expected.

6. To enable the cloned rule, click the toggle to the right (blue).

   |   |                                                                            |
   | - | -------------------------------------------------------------------------- |
   |   | You can disable the cloned rule by clicking the toggle to the left (gray). |

## Next steps

After enabling a cloned rule, ensure you validate the resync and real-time sync behavior. Learn more in [Viewing sync status](p1_view_sync_status.html).

---

---
title: Configuring an authoritative identity provider
description: Configure an identity provider (IdP) in PingOne as an authoritative IdP, which allows it to provision users without any registration or sign-on steps.
component: pingone
page_id: pingone:integrations:p1_configure_authoritative_idp
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_configure_authoritative_idp.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 24, 2025
section_ids:
  about-this-task: About this task
  before-you-begin: Before you begin
  steps: Steps
---

# Configuring an authoritative identity provider

You can configure an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* as an authoritative IdP, which allows it to provision users without any registration or sign-on steps.

## About this task

Set up an IdP as usual, edit the IdP to configure it as an authoritative IdP, and then specify which population should contain the provisioned users.

## Before you begin

Set up an external IdP if you haven't already. Learn more in [External IdPs](p1_external_idps.html).

## Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and browse or search for the IdP that you want to edit.

2. Click the IdP entry to open the details panel.

3. On the **Profile** tab, click the **Pencil** icon.

4. In the **Population** list, select the population to which you want to provision users.

   Selecting a population enables just-in-time (JIT) provisioning for the configured IdP and overrides the population set in the authentication policy under **Enable registration**.

5. Click **Save**.

---

---
title: Configuring an Authorize gateway instance
description: Customize the environment and behavior of the gateway instance to suit your business needs.
component: pingone
page_id: pingone:integrations:p1_configure_authz_gateway_instance
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_configure_authz_gateway_instance.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  config_docker_run: Steps
  result: Result
  config_docker_compose: Steps
  result-2: Result
  next-steps: Next steps
---

# Configuring an Authorize gateway instance

Customize the environment and behavior of the gateway instance to suit your business needs.

Use the `docker run` command or Docker Compose to pass configuration information to your gateway instance as a JSON object. You can configure:

* [Decision logging](p1_logging_authz_gateway_instances.html#p1_authz_gateway_decision_logging)

* [Authentication](p1_authenicate_authz_gateway_endpoints.html)

* [Service caching](p1_service_caching_authz_gateway_instances.html)

* [PingOne service timeouts](p1_service_caching_authz_gateway_instances.html#p1_config_p1_service_timeouts)

- `docker run`

- Docker Compose

## Steps

1. Stop the gateway instance container.

2. Using the `SPRING_APPLICATION_JSON` environment variable, modify the `docker run` command to include the relevant configuration object.

   For example, to configure decision logging for the gateway instance, the command should look something like this (line breaks are included for readability and aren't necessary in your command):

   ```
   docker run --init \
     -e PING_IDENTITY_ACCEPT_EULA=yes \
     -e gatewayCredential=<your-gateway-credential> \
     -e SPRING_APPLICATION_JSON='{"decision-logging":[{"name":"debugLog","details":["decisionTree"],"log-format":"%date{yyyy-MM-dd'\''T'\''HH:mm:ss.SSSXXX,UTC} [%logger] %mdc_properties %msg%n"}]}' \
     -p 8080:8080 pingidentity/pingone-authorize-gateway:1.2.1
   ```

   Learn more about [starting a gateway instance](p1_start_authz_gateway_instance.html).

3. Run the command.

   ### Result

   The gateway instance container starts and applies the specified configuration.

Docker Compose simplifies the management of multi-container applications. By defining your services, networks, and volumes in a single YAML file, you can start or stop your entire application stack with simple commands like `docker compose up` and `docker compose down`.

## Steps

1. Stop the gateway instance container.

2. In your project directory on the host server, create a file named `docker-compose.yml`.

   For example:

   ```
   touch docker-compose.yml
   ```

   Learn more in [Docker Compose Quickstart](https://docs.docker.com/compose/gettingstarted/) in the Docker Compose documentation.

3. In the newly created `docker-compose.yml` file, use the `environment.SPRING_APPLICATION_JSON` variable to pass in the relevant configuration object.

   For example, to configure decision logging for the gateway instance, the `docker-compose.yml` file should look something like this:

   ```
   services:
     authorize-gateway:
       image: pingidentity/pingone-authorize-gateway:1.2.1
       init: true
       environment:
         PING_IDENTITY_ACCEPT_EULA: "yes"
         gatewayCredential: <your-gateway-credential>
         SPRING_APPLICATION_JSON: |
           {
             "decision-logging": [
               {
                 "name": "debugLog",
                 "details": ["decisionTree"],
                 "log-format": "%date{yyyy-MM-dd'T'HH:mm:ss.SSSXXX,UTC} [%logger] %mdc_properties %msg%n"
               }
             ]
           }
       ports:
         - "8080:8080"
   ```

4. From your gateway instance directory, start the application by running `docker compose up`.

   ### Result

   The gateway instance container starts and applies the specified configuration.

## Next steps

Learn more about the Docker Compose CLI in [How Compose works](https://docs.docker.com/compose/intro/compose-application-model/#cli) in the Docker Compose documentation.

---

---
title: Configuring end user browsers
description: To support Kerberos authentication in PingOne, you must add two trusted URIs to end user browsers.
component: pingone
page_id: pingone:integrations:p1_configuring_end_user_browsers
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_configuring_end_user_browsers.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 2, 2025
section_ids:
  custom-domains: Custom domains
  browser-uri-reference: Browser URI reference
---

# Configuring end user browsers

To support Kerberos authentication, you must add two trusted URIs to end user browsers.

The purpose of two URIs is future proofing. Ping Identity will migrate its infrastructure in the coming months. Adding the second URI ensures that your configuration will continue to work after the migration.

## Custom domains

If the environment is configured with a custom domain, `auth.pingone.com` and `kerberos.pingone.com` are irrelevant. Instead, add the custom domain as the trusted URI.

## Browser URI reference

When configuring end user browsers, use the following trusted URI values for the various PingOne geographies:

| Geography                                                                   | URI 1               | URI 2                   |
| --------------------------------------------------------------------------- | ------------------- | ----------------------- |
| Australia                                                                   | auth.pingone.com.au | kerberos.pingone.com.au |
| Canada                                                                      | auth.pingone.ca     | kerberos.pingone.ca     |
| Europe                                                                      | auth.pingone.eu     | kerberos.pingone.eu     |
| North America (US)                                                          | auth.pingone.com    | kerberos.pingone.com    |
| Singapore                                                                   | auth.pingone.sg     | kerberos.pingone.sg     |
| Asia Pacific (legacy)&#xA;&#xA;Available only for existing .asia customers. | auth.pingone.asia   | kerberos.pingone.asia   |

---

---
title: Configuring Google Chrome
description: Configure Kerberos authentication for the Google Chrome browser.
component: pingone
page_id: pingone:integrations:p1_configuring_chrome
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_configuring_chrome.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 9, 2023
section_ids:
  about-this-task: About this task
---

# Configuring Google Chrome

Configure Kerberos authentication for the Google Chrome browser.

## About this task

On Windows, Google Chrome uses the same configuration values as Microsoft Edge. For more information, see [Configuring Microsoft Edge](p1_configuring_edge.html).

---

---
title: Configuring Microsoft Edge
description: Use the Group Policy Management editor in PingOne to configure Microsoft Edge.
component: pingone
page_id: pingone:integrations:p1_configuring_edge
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_configuring_edge.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Configuring Microsoft Edge

Ensure that the Microsoft Edge browser on the end user's system is configured to support Kerberos authentication. Use the Group Policy Management Editor to configure the browser.

## Steps

1. Start the Group Policy Management Editor from Windows Administrative Tools.

   |   |                                                                                        |
   | - | -------------------------------------------------------------------------------------- |
   |   | The path to the Microsoft Edge settings can vary depending on your version of Windows. |

2. Define the applicable trusted URIs as Intranet sites.

   1. Go to **User Configuration > Administrative Templates > Windows Components > Internet Explorer > Internet Control Panel > Security Page**.

   2. Double-click **Site to Zone Assignment List**.

   3. Select **Enabled** if it's not already selected.

   4. Click **Show** to open the **Show Contents** window.

   5. Enter the applicable trust URIs as intranet sites.

      Do one of the following:

      ### Choose from:

      * **If the environment is configured with a custom domain**: In the **Value Name** field, enter the custom domain, and in the **Value** field, enter `1`.

      * **If the environment isn't configured with a custom domain**: In the **Value Name** field, enter the trusted URIs found in [Configuring end user browsers](p1_configuring_end_user_browsers.html) and in the **Value** field, enter `1`.

   6. Click **OK**.

3. Configure the Intranet Zone options.

   1. Go to **User Configuration > Administrative Templates > Windows Components > Internet Explorer > Internet Control Panel > Security Page > Intranet Zone > Logon options**.

   2. In the **Logon options** window and list, select **Automatic logon with current user name and password**. Click **OK**.

---

---
title: Configuring Mozilla Firefox
description: Configure Kerberos authentication for the Firefox browser.
component: pingone
page_id: pingone:integrations:p1_configuring_mozilla
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_configuring_mozilla.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 9, 2023
section_ids:
  steps: Steps
---

# Configuring Mozilla Firefox

Configure Kerberos authentication for the Firefox browser.

## Steps

1. Start the Firefox browser.

2. In the address bar, enter `about:config`.

3. If you are presented with a security warning, click **Accept the risk and continue**.

4. In the **Search** field, enter `network.negotiate-auth.trusted-uris` and then click the pencil icon.

5. Do one of the following:

   * If the environment is not configured with a custom domain, enter the two trusted addresses separated by a comma, and then click the check mark icon.

   * If the environment is configured with a custom domain, enter the custom domain and then click the check mark icon.

     For more information about the trusted URI values, see [Configuring end user browsers](p1_configuring_end_user_browsers.html).

---

---
title: Configuring multiple Authorize gateway instances
description: To achieve high-availability and scalability, you can configure multiple Authorize gateway instances and deploy their Docker containers across multiple servers.
component: pingone
page_id: pingone:integrations:p1_configure_multiple_authz_gateway_instances
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_configure_multiple_authz_gateway_instances.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  managing-credentials: Managing credentials
  ensuring-version-compatibility: Ensuring version compatibility
---

# Configuring multiple Authorize gateway instances

To achieve high-availability and scalability, you can configure multiple Authorize gateway instances and deploy their Docker containers across multiple servers.

When multiple gateway instances are connected to an Authorize gateway, PingOne maintains a list of the active connections for each gateway. If a gateway instance isn't available, it's excluded from the list of active gateway instances.

![Screen capture of an Authorize gateway with multiple gateway instances connected.](_images/p1-az-gateway-multiple-instances.png)

## Managing credentials

You can set up an Authorize gateway with one gateway credential and have multiple gateway instances share this same credential. If necessary, you can revoke the credential from the Authorize gateway to stop all gateway traffic. Revoking the credential breaks the connection to PingOne, but doesn't stop gateway instances or decision request evaluation.

When there's no connection to PingOne, gateway instances keep running with the last successful gateway configuration. However, new authorization policy versions aren't deployed to any gateway instances that rely on a revoked credential.

|   |                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------- |
|   | Use a different credential for each gateway instance. This allows you to revoke access to individual gateway instances. |

Gateway instances log connection failures with PingOne. Learn more in [Logging for Authorize gateway instances](p1_logging_authz_gateway_instances.html).

## Ensuring version compatibility

Authorization policy versions sometimes contain features that aren't compatible with older gateway instances. To ensure all policy features are supported, every authorization policy version specifies a minimum required gateway instance version. To successfully publish an authorization policy version to a gateway, all of the gateway's associated gateway instances must meet or exceed this minimum version.

Before you publish a new authorization policy version to a gateway, [upgrade each gateway instance](p1_upgrade_authz_gateway_instance.html) to meet or exceed the minimum required gateway instance version.

---

---
title: Configuring multiple gateway instances
description: For high-availability applications or scalability, you can configure multiple gateway instances. You can then run the Windows service, Docker container, or Java application on multiple servers.
component: pingone
page_id: pingone:integrations:p1_configure_multiple_gateways_ldap
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_configure_multiple_gateways_ldap.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 4, 2024
---

# Configuring multiple gateway instances

For high-availability applications or scalability, you can configure multiple gateway instances. You can then run the Windows service, Docker container, or Java application on multiple servers.

When multiple gateway instances are connected to PingOne, PingOne maintains a list of the active gateway instances connection. PingOne will load balance based on each connection with lower load and latency. If a gateway instance is not available, it is excluded from the list of active gateway instances.

You can set up one PingOne gateway with one gateway credential, with multiple gateway instances that share the same credential. If needed, you can remove the credential from the PingOne gateway to stop all gateway traffic.

|   |                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We recommend that you use a different credential for each gateway instance. Using different credentials allows you to easily revoke access to individual gateway instances. |

---

---
title: Configuring multiple gateways
description: For high-availability applications or scalability, you can configure multiple gateways. You can then run the Docker container or Java application on multiple servers.
component: pingone
page_id: pingone:integrations:p1_configure_multiple_gateways_radius
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_configure_multiple_gateways_radius.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 24, 2025
---

# Configuring multiple gateways

For high-availability applications or scalability, you can configure multiple gateways. You can then run the Docker container or Java application on multiple servers.

When multiple gateways are configured, load balancing across these instances is handled by your RADIUS client's load balancing mechanism rather than by PingOne. Your client is responsible for distributing authentication requests among the gateway instances. The gateway instance that receives an authentication request is the same instance that processes and returns the response for that transaction.

You can set up a single PingOne logical gateway with one gateway credential and have multiple physical gateways that share the same credential. If needed, you can remove the credential from the logical gateway to stop all gateway traffic.

---

---
title: Configuring outbound group provisioning
description: Sync groups along with their memberships out of PingOne.
component: pingone
page_id: pingone:integrations:p1_provisioning_configuring_outbound_group_provisioning
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_provisioning_configuring_outbound_group_provisioning.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 12, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configuring outbound group provisioning

Use PingOne provisioning to sync groups along with their memberships out of PingOne to a connected software as a service (SaaS) application.

## Before you begin

You must create a group in your PingOne admin console to select for outbound provisioning

|   |                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The recommended number of groups supported in a provisioning rule for outbound group provisioning is 1000.When syncing, you cannot sync external groups. This capability is limited to internal groups for outbound group provisioning. |

Learn more in [Creating a group](../directory/p1_create_group.html).

## About this task

The following provisioners support group provisioning:

* [GitHub EMU](p1_create_github_emu_connection.html)

* [Google](p1_create_google_workspace_connection.html)

* [Microsoft Azure Office 365](p1_create_azure_connection.html)

* [Salesforce communities](p1_create_connection_salesforce_communities.html)

* [Salesforce workforce](p1_create_salesforce_workforce_connection.html)

* [SCIM](p1_create_scim_connection.html)

* [Slack](p1_creating_slack_connection.html)

| Membership type   | Description                                                                                                                                                                                                          |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Group memberships | Memberships are a part of a group. Provisioners that support group memberships are:* GitHub EMU

* SCIM

* Slack                                                                                                     |
| User memberships  | Memberships are a part of a user. Provisioners that support user memberships are:* Google

* SalesforceIf there's an existing group with the same name on the target, provisioning merges the group and its members. |

## Steps

1. In the PingOne admin console, go to to **Integrations > Provisioning**.

2. On the **Rules** tab, locate and click the rule to open the details panel.

3. On the **Directory** tab, click the **Pencil** icon ([icon: pencil, set=fa]) next to **Groups** .

   * To search groups, enter a group name in the **Search Group Name** field.

   * To add groups, select a group in **All Groups**.

   * To remove a group, clear the checkbox for the group in **All Groups**.

   * To view provisioned groups, click **Selected Groups**.

   * To accept a merge or overwrite memberships when a group with the same name exists on the target, select the checkbox next to **I understand and want to continue** in the modal.

     |   |                                                                                                                                                                                                                                                                                                                                      |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | Merging or overwriting memberships only applies to SCIM, Slack, and GitHub EMU provisioning connections. Learn more in [Creating a Slack connection](p1_creating_slack_connection.html), [Creating a SCIM connection](p1_create_scim_connection.html), and [Creating a GitHub EMU connection](p1_create_github_emu_connection.html). |

4. Click **Save**.
---
title: Configuration Management
description: The Configuration Management service gives you a secure and flexible approach to automating (promoting) configurations across multiple environments, enabling the seamless creation, updating, and deletion of resources while supporting dynamic configurations through variable management. Resource dependencies are maintained, ensuring smooth cross-environment transitions and promotions. Auditing and reporting enhance oversight and compliance.
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management.html
section_ids:
  special-handling: Resources requiring special handling
  secrets-and-passwords: Secrets and passwords
  certificates: Certificates
  user-attributes: User attributes
  ldap-gateway: LDAP Gateway
  notification-settings: Notification settings
  davinci-resources: DaVinci resources
  davinci-flows: DaVinci flows
  davinci-flow-policies: DaVinci flow policies
  davinci-applications: DaVinci applications
  deleted-configuration-resources: Deleted configuration resources
  if-you-want-to-use-postman: If you want to use Postman
---

# Configuration Management

The Configuration Management service gives you a secure and flexible approach to automating (promoting) configurations across multiple environments, enabling the seamless creation, updating, and deletion of resources while supporting dynamic configurations through variable management. Resource dependencies are maintained, ensuring smooth cross-environment transitions and promotions. Auditing and reporting enhance oversight and compliance.

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | Currently, you can promote configurations only to environments within the same PingOne tenant. |

To use the Configuration Management service you need to have the Environment Admin role for at least two environments. The general workflow is:

* Select configurations that you want to promote from one environment to another (generally, through development, testing, and production stages).

* If desired, use promotion variables to dynamically substitute different property values for a configuration resource included in a promotion operation.

* Execute the promotion plan returned by the [Read One Promotion](configuration-management/promotions/get-one-promotion.html) or [Read All Promotions](configuration-management/promotions/get-all-promotions.html) to move the configuration from the source environment to the target environment.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Only resources used for PingOne configurations are contained in a snapshot (such as applications, policies, and flows). Other PingOne resources not used for configuration purposes, are not tracked by the Configuration Management service. Such resources are excluded from promotions, and include:* Users and user profiles

* Admin role assignments

* Environment properties

* Externally provisioned groups

* Audit logs |

The Configuration Management service is comprised of these sub-services:

* [Snapshots](configuration-management/snapshots.html)

* [Promotions](configuration-management/promotions.html)

* [Promotion Variables](configuration-management/promotion-variables.html)

* [Promotion Configuration](configuration-management/promotion-configuration.html)

## Resources requiring special handling

Some resources can't be promoted. Excluded resources generally fall into the following categories:

* User and operational data: Resources that contain user-specific or operational data, such as audit logs, user profiles, or device and session data, are excluded from promotion to prevent data integrity issues.

* Environment-specific secrets and keys: These resources are inherently tied to a specific environment for security reasons and can't be promoted or used by another environment.

* Roles and permissions: While you can promote resources that require permissions or roles, the administrative access to them isn't promoted. This includes administrator role assignment and application role assignments. After the resource is promoted, you must manually assign the appropriate roles and permissions to the resource in the target environment.

You'll find a complete list of excluded resources in [Excluded Resources](configuration-management/promotions/excluded-resources.html).

### Secrets and passwords

Many configuration resources in PingOne use secrets or passwords to connect third-party services such as an external identity provider or a PingOne DaVinci connector. When you select to promote a resource that includes attributes for secrets or passwords, PingOne requires you to create sensitive variables for promotion, which are stored securely and encrypted anywhere they appear.

### Certificates

Certificates can't be promoted directly, and certificate references in other resources require special handling:

* Default certificates: If a resource in the source environment references a default certificate, the promotion service automatically maps that reference to the default certificate in the target environment during the promotion.

* Certificates as variables: For non-default certificates, you must create promotion variables to store the certificate IDs for both the source and target environments. During the promotion, the service substitutes the variable value for the certificate ID in the target environment.

The following example illustrates this process:

1. Create verification certificates in both the source and target environments.

2. Create a SAML application in the source environment that uses the verification certificate for that environment.

3. Create a promotion variable for the certificate ID attribute of the SAML application, setting the source environment value to the certificate ID in the source environment and the target environment value to the certificate ID in the target environment.

4. Promote the SAML application from the source environment to the target environment.

The SAML application in the source environment uses the certificate ID defined in the variable for that environment. The SAML application promoted to the target environment uses the certificate ID defined in the variable for the target environment.

### User attributes

Individual user attributes are supported for promotion. However, when you promote an application or FIDO policy that references custom user attributes, all schema attributes are added to the promotion plan. You can manually exclude them before you run the promotion.

### LDAP Gateway

Gateway credentials can't be promoted or managed using promotion variables. These credentials must be created in each environment after the gateway is promoted.

### Notification settings

Email notification settings can be promoted, but if you're using the allow list capability, you must configure the allow list in each environment. The allow list itself can't be promoted directly.

### DaVinci resources

The promotion service fully supports the promotion of PingOne DaVinci resources, including flows, subflows, flow policies, connectors, and DaVinci applications. However, there are several differences in how certain types of DaVinci resources are processed during promotion.

As with other types of configuration resources, you can map DaVinci dependencies to existing resources if they exist in the target environment, or create them as new resources if they don't, but dependency behavior varies depending on the resource you select for direct promotion.

#### DaVinci flows

When you promote a DaVinci flow, the promotion service identifies all of the dependent configurations used in the flow if they're referenced correctly. Only the most recent deployed version of the flow is promoted to the target environment. For example, if your flow has four versions, and version 3 is the most recent deployed version, only version 3 is promoted. Similarly, if the flow includes subflows, only the subflow versions referenced by the flow are promoted.

#### DaVinci flow policies

When you promote a DaVinci flow policy, the promotion service identifies the flows referenced by the policy and the specific versions of the flows referenced. All flow versions used in the policy are promoted as dependencies of the policy.

For example, if you are promoting a flow policy that references two flows, and the policy uses version 2 of flow A and versions 1 and 3 of flow B, version 2 of flow A and versions 1 and 3 of flow B are promoted as dependencies of the flow policy.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | DaVinci flow policies are always linked to a DaVinci application. If you promote a flow policy directly, the associated DaVinci application is promoted as a dependency of the flow policy. This application won't be listed in the PingOne admin console **Auto-Selected Dependencies** page when you configure the promotion, but it will be listed when you confirm the promotion configuration.If the application has additional flow policies associated with it, those policies aren't promoted as dependencies of the application.To promote all flow policies associated with a DaVinci application, promote the application directly instead of promoting the flow policies individually. |

#### DaVinci applications

When you promote a DaVinci application, the promotion service identifies all associated flow policies and promotes them as dependencies of the application. The specific versions of the flow policies referenced by the application are promoted.

### Deleted configuration resources

When you delete a configuration resource from the source environment after it has been promoted to the target environment, that resource remains in the target environment until you explicitly delete it there. You can use the promotion service to handle the deletion. A deletion promotion works similarly to a standard promotion, but instead of creating or updating the resource in the target environment, the promotion service deletes it.

## If you want to use Postman

You can download or fork the Postman collection for the early access Configuration Management APIs, and test them in your Postman environment. If you don't already have a Postman installation, you can install the free version. Refer to [Download Postman](https://www.postman.com/downloads/).

Import or fork the Postman collection `PingOne Configuration Management APIs - Early Access` into your Postman installation by clicking the **Run in Postman** button below:

[Run in Postman](https://god.gw.postman.com/run-collection/5375867-3dcb7dec-86a1-4ba9-a429-f33fe07b6583?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D5375867-3dcb7dec-86a1-4ba9-a429-f33fe07b6583%26entityType%3Dcollection%26workspaceId%3D936f1637-06aa-461a-b23d-0964e90621c6)

Refer to [Postman and the PingOne APIs](https://developer.pingidentity.com/pingone-api/platform/working-with-pingone-apis/postman-and-pingone.html) for more information.

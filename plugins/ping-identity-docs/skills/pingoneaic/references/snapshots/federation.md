---
title: Configure federated access for tenant administrators
description: Configure federated SSO for Advanced Identity Cloud tenant admins using PingOne, Microsoft Entra ID, AD FS, or any OIDC-compliant IdP
component: pingoneaic
page_id: pingoneaic:federation:configure-federated-access-for-tenant-administrators
canonical_url: https://docs.pingidentity.com/pingoneaic/federation/configure-federated-access-for-tenant-administrators.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Federation", "Authentication", "Single Sign-on (SSO)"]
page_aliases: ["federation:activate-deactivate-a-federation-provider.adoc", "federation:enable-federation-for-your-tenant.adoc", "federation:grant-or-revoke-super-administrator-access.adoc", "federation:overview.adoc", "federation:set-federation-login-requirements.adoc", "federation:set-up-a-federation-provider.adoc", "federation:store-client-secrets-in-esvs.adoc"]
section_ids:
  configure-federated-access-using-pingone: Configure federated access using PingOne
  configure-federated-access-using-pingone-advanced-identity-cloud: Configure federated access using PingOne Advanced Identity Cloud
  configure-federated-access-across-your-tenant-environments: Configure federated access across your tenant environments
  set-up-a-federation-idp: Set up a federation IdP
  configure-a-mutable-environment-to-use-a-federation-idp: Configure a mutable environment to use a federation IdP
  configure-federation-sign-on-requirements: Configure federation sign-on requirements
  deactivate-a-federation-idp: Deactivate a federation IdP
  rotate-a-federation-idp-client-secret: Rotate a federation IdP client secret
---

# Configure federated access for tenant administrators

Federated access lets tenant administrators use your company's single sign-on (SSO) to sign on to your PingOne Advanced Identity Cloud tenant environments.

By using federation to authenticate your tenant administrators to Advanced Identity Cloud, you can quickly and easily provision and deprovision users from your centralized identity provider (IdP) instead of managing them separately in each Advanced Identity Cloud tenant environment.

The groups feature allows you to add and remove tenant administrators depending on their group membership in your IdP. You can also specify the level of administrator access (super administrator\[[1](#_footnotedef_1 "View footnote.")] or tenant administrator) for groups of users.

Advanced Identity Cloud lets you configure federated access in two main ways:

* You can use PingOne to configure PingOne itself as an IdP for Advanced Identity Cloud. Learn more in [Configure federated access using PingOne](#configure-federated-access-using-pingone).

* You can use the Advanced Identity Cloud admin console to configure Microsoft Entra ID (Entra ID)\[[2](#_footnotedef_2 "View footnote.")] or Microsoft Active Directory Federation Services (AD FS) as IdPs, or any other IdP that's [OpenID Connect](https://openid.net/connect/) (OIDC) compliant. Learn more in [Configure federated access using PingOne Advanced Identity Cloud](#configure-federated-access-using-pingone-advanced-identity-cloud).

## Configure federated access using PingOne

You can configure PingOne as a federation IdP for PingOne Advanced Identity Cloud. To do this, configure it in PingOne itself. Learn more in [Set up SSO to PingOne Advanced Identity Cloud](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_set_up_sso_p1_advanced_identity_cloud.html).

After you configure PingOne as a federation IdP, each configured tenant environment in Advanced Identity Cloud automatically displays PingOne in its list of federation IdPs:

1. Sign on to the Advanced Identity Cloud admin console for any of the environments [you configured for federated access using PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_set_up_sso_p1_advanced_identity_cloud.html).

2. Go to Tenant settings.

3. Click Federation.

4. If configured correctly in PingOne, the list contains an active PingOne federation IdP:

   ![Federation IdP list containing an active PingOne federation IdP](_images/federation-pingone-list-item.png)

5. Click the PingOne list item to view its configuration settings page. For PingOne, this is a basic page containing the Status and the Well-Known Endpoint of the PingOne federation IdP:

   ![PingOne federation IdP configuration settings page](_images/federation-pingone-configuration-settings-page.png)

If you configure a federation IdP in PingOne, the corresponding Advanced Identity Cloud tenant environments are configured automatically. You do not need to promote configuration changes.

## Configure federated access using PingOne Advanced Identity Cloud

You can configure the following federation IdPs using the Advanced Identity Cloud admin console:

* [Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/whatis)\[[2](#_footnotedef_2 "View footnote.")] using OIDC.

* [AD FS](https://learn.microsoft.com/en-us/windows-server/identity/active-directory-federation-services) using OIDC.

* Any other federation IdP that's OIDC compliant.

If you configure a federation IdP using the Advanced Identity Cloud admin console, you must do so in your development environment and promote the configuration changes. You must also store the federation IdP secrets for each of your environments in [ESV secrets](../tenants/esvs.html#secrets) and set corresponding placeholders in your configuration. Learn more in [Configure federated access across your tenant environments](#configure-federated-access-across-your-tenant-environments).

### Configure federated access across your tenant environments

The high-level process to set up federated access across your tenant environments is as follows:

1. [Set up a federation IdP](#set-up-a-federation-idp) for your development environment:

   * You can use the same federation IdP for all your tenant environments, or you can use a different federation IdP for each environment.

   * If you use the same federation IdP for multiple environments, you must configure it with redirect URLs for each environment. The redirect URL for a tenant environment has the following format:

     https\://\<tenant-env-fqdn>/login/admin

   * Note the client secret of the IdP, as you might not be able to retrieve it later.

2. In your development environment:

   1. Create the following [ESVs](../tenants/esvs.html) using the values from the federation IdP configuration:

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can create variables and secrets using the Advanced Identity Cloud admin console or the API.- [Create a variable](../tenants/esvs-manage-ui.html#create-variables) or [create a secret](../tenants/esvs-manage-ui.html#create-secrets) using the Advanced Identity Cloud admin console.

      - [Create a variable](https://docs.pingidentity.com/pingoneaic/_attachments/api/#operation/createVariables) or [create a secret](https://docs.pingidentity.com/pingoneaic/_attachments/api/#operation/createSecret) using the API. |

      * Federation IdP fields:

        | ESV name                                                             | ESV type | Expression type | Example value                              |
        | -------------------------------------------------------------------- | -------- | --------------- | ------------------------------------------ |
        | `esv-idp-client-id`                                                  | Variable | String          | 6b05a314-c721-4aa6-baad-7f533cbd25b0       |
        | `esv-idp-client-secret`                                              | Secret   | String          | changeit                                   |
        | `esv-idp-user-info-endpoint`\[[3](#_footnotedef_3 "View footnote.")] | Variable | String          | https\://graph.microsoft.com/oidc/userinfo |

      * Federation IdP endpoint fields (choose one of the following):

        * **Option 1**: Create a single ESV containing the well-known endpoint ID:

          | ESV name                         | ESV type | Expression type | Example value                        |
          | -------------------------------- | -------- | --------------- | ------------------------------------ |
          | `esv-idp-well-known-endpoint-id` | Variable | String          | 0e076864-135f-4914-9b72-80efaa4c3dcf |

        * **Option 2**: Create an ESV for each of these endpoint fields:

          | ESV name                         | ESV type | Expression type | Example value                                                                                                 |
          | -------------------------------- | -------- | --------------- | ------------------------------------------------------------------------------------------------------------- |
          | `esv-idp-well-known-endpoint`    | Variable | String          | https\://login.microsoftonline.com/0e076864-135f-4914-9b72-80efaa4c3dcf/v2.0/.well-known/openid-configuration |
          | `esv-idp-authorization-endpoint` | Variable | String          | https\://login.microsoftonline.com/0e076864-135f-4914-9b72-80efaa4c3dcf/oauth2/v2.0/authorize                 |
          | `esv-idp-token-endpoint`         | Variable | String          | https\://login.microsoftonline.com/0e076864-135f-4914-9b72-80efaa4c3dcf/oauth2/v2.0/token                     |
          | `esv-idp-issuer`                 | Variable | String          | https\://login.microsoftonline.com/0e076753-135f-4914-9b72-80efaa4c3dcf/v2.0                                  |

        |   |                                                                                                                                               |
        | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | You don't need to create an ESV for the redirect URL, as Advanced Identity Cloud automatically configures it based on the environment's FQDN. |

      * (Optional) Federation IdP groups fields:

        | ESV name                        | ESV type | Expression type | Example value                        |
        | ------------------------------- | -------- | --------------- | ------------------------------------ |
        | `esv-idp-group-super-admins`    | Variable | String          | 8c578f67-cac4-49eb-8f28-8e4f2c22945e |
        | `esv-idp-group-tenant-admins`   | Variable | String          | 3623050d-3604-45a2-942e-f6be9ec9f9ed |
        | `esv-idp-group-tenant-auditors` | Variable | String          | eeb11282-cb38-42b9-909f-439cad25550e |
        | `esv-idp-group-brand-admins`    | Variable | String          | 47e677ad-dfac-4e02-be5f-cff56fb31ed4 |

   2. [Restart Advanced Identity Cloud services](../tenants/configuration-placeholders.html#restart-identity-cloud-services).

   3. Follow the instructions in [Configure a mutable environment to use a federation IdP](#configure-a-mutable-environment-to-use-a-federation-idp), entering the following ESV placeholders in the relevant fields:

      * Federation IdP fields:

        | Field name                                                 | ESV placeholder                 |
        | ---------------------------------------------------------- | ------------------------------- |
        | Application ID                                             | `&{esv.idp.client.id}`          |
        | Application secret                                         | `&{esv.idp.client.secret}`      |
        | User Info endpoint\[[3](#_footnotedef_3 "View footnote.")] | `&{esv.idp.user.info.endpoint}` |

      * Federation IdP endpoint fields (choose one of the following):

        * **Option 1**: If you created a single ESV for the well-known endpoint ID, replace the ID portion of the endpoint's value with the ESV placeholder. Use the following examples as guidance:

          | Field name             | Example using ESV placeholder                                                                                |
          | ---------------------- | ------------------------------------------------------------------------------------------------------------ |
          | Well-known endpoint    | https\://login.microsoftonline.com/`&{esv.idp.well.known.endpoint.id}`/v2.0/.well-known/openid-configuration |
          | Authorization endpoint | https\://login.microsoftonline.com/`&{esv.idp.well.known.endpoint.id}`/oauth2/v2.0/authorize                 |
          | Token endpoint         | https\://login.microsoftonline.com/`&{esv.idp.well.known.endpoint.id}`/oauth2/v2.0/token                     |
          | Issuer                 | https\://login.microsoftonline.com/`&{esv.idp.well.known.endpoint.id}`/v2.0                                  |

        * **Option 2**: If you created an ESV for each endpoint, insert the ESV placeholders into their respective endpoint fields:

          | Field name             | ESV placeholder                     |
          | ---------------------- | ----------------------------------- |
          | Well-known endpoint    | `&{esv.idp.well.known.endpoint}`    |
          | Authorization endpoint | `&{esv.idp.authorization.endpoint}` |
          | Token endpoint         | `&{esv.idp.token.endpoint}`         |
          | Issuer                 | `&{esv.idp.issuer}`                 |

      * (Optional) Federation IdP groups fields:

        | Field name                                            | ESV placeholder                    |
        | ----------------------------------------------------- | ---------------------------------- |
        | Group Identifiers field to the left of Super Admins   | `&{esv.idp.group.super.admins}`    |
        | Group Identifiers field to the left of Tenant Admins  | `&{esv.idp.group.tenant.admins}`   |
        | Group Identifiers field to the left of Tenant Auditor | `&{esv.idp.group.tenant.auditors}` |
        | Group Identifiers field to the left of Brand Admin    | `&{esv.idp.group.brand.admins}`    |

3. Determine the promotion order of your tenant environments. This will depend on whether you have a [standard promotion group of environments](../tenants/self-service-promotions.html#standard-promotion-group-of-environments) or whether you also have [additional UAT environments](../tenants/self-service-promotions.html#additional-uat-environments).

4. In promotion order, for each of the tenant environments in your promotion group, perform the following steps:

   1. Repeat step 1 to create a federation IdP for the tenant environment.

   2. Repeat step 2a to create the same ESVs in the tenant environment. Ensure the ESV values match those from the tenant environment's federation IdP configuration.

   3. Run a promotion to move the configuration changes to the tenant environment from its respective lower tenant environment. Learn more in:

      * [Manage self-service promotions using the admin console](../tenants/self-service-promotions-ui.html)

      * [Manage self-service promotions using the API](../tenants/self-service-promotions-api.html)

5. (Optional) If you have sandbox\[[4](#_footnotedef_4 "View footnote.")] environments, repeat steps 1 and 2 for each sandbox environment.

#### Set up a federation IdP

You can find instructions for setting up a federation IdP in the following guides:

* [Set up Microsoft Entra ID as a federation IdP](set-up-federation-idp-microsoft-entra-id.html)

* [Set up Microsoft Active Directory Federation Services as a federation IdP](set-up-federation-idp-microsoft-ad-fs.html)

* [Set up an OIDC-compliant IdP as a federation IdP](set-up-federation-idp-oidc.html)

#### Configure a mutable environment to use a federation IdP

After you've set up a federation IdP, you can configure it in a mutable environment (development or sandbox\[[4](#_footnotedef_4 "View footnote.")]) to provide federated access to tenant administrators.

|   |                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To understand how the instructions in this section fit into the process of configuring federated access across your tenant environments, refer to step 2a in the [high-level process](#configure-federated-access-across-your-tenant-environments). |

1. Sign on to the Advanced Identity Cloud admin console of your mutable environment (development or sandbox\[[4](#_footnotedef_4 "View footnote.")]) as a super administrator\[[1](#_footnotedef_1 "View footnote.")].

2. Go to Tenant settings.

3. Click Federation.

4. Click + Identity Provider.

5. In the Add Sign On Method modal, select the federation provider to use:

   * Microsoft Azure

   * ADFS

   * OIDC

6. Click Next.

7. In the Configure Application modal, click Next.

8. In the Identity Provider Details modal:

   1. Complete the following fields:

      * Name: The name of the provider.

      * Application ID: The ID for the application.

      * Application Secret: The client secret for the application.

      * Well-known Endpoint:

        * For Entra ID, this is the URL from the OpenID Connect metadata document field. In the URL, make sure to replace `organization` with the actual tenant ID for your tenant.

        * For AD FS, this is the endpoint from the OpenID Connect section.

        * For OIDC, refer to your IdP vendor's documentation on locating a client's well-known endpoint.

        When you populate the Well-known Endpoint field with a valid URL, the following fields are automatically populated:

        * Authorization Endpoint: The endpoint for authentication and authorization. The endpoint returns an authorization code to the client.

        * Token Endpoint: The endpoint that receives an authorization code. The endpoint returns an access token.

        * User Info Endpoint: The endpoint that receives an access token. The endpoint returns user attributes.

      * (For OIDC only): OAuth Scopes: The scopes the application uses for user authentication. The default scopes are `openid`, `profile`, and `email`.

      * (For OIDC only): Client Authentication Method: Options are `client_secret_post` and `client_secret_basic`. The default option is `client_secret_post`.

      * Button Text: The text for the application button that's displayed on the tenant's sign-on page.

   2. Click Save. By default all users are given the tenant administrator level of access when they access the tenant using your IdP. To give some or all users super administrator\[[1](#_footnotedef_1 "View footnote.")], tenant auditor\[[5](#_footnotedef_5 "View footnote.")], or brand administrator\[[6](#_footnotedef_6 "View footnote.")] levels of access, configure groups in the next step.

9. (Optional) Configure group membership to determine administrator access level (super administrator\[[1](#_footnotedef_1 "View footnote.")] or tenant administrator).

   1. Set up groups in your IdP:

      * For Entra ID: Follow the instructions in [Use group membership to enable federation in Entra ID](set-up-federation-idp-microsoft-entra-id.html#use-group-membership-to-enable-federation-in-entra-id).

      * For AD FS: Follow the instructions in [Use group membership to enable federation in AD FS](set-up-federation-idp-microsoft-ad-fs.html#use-group-membership-to-enable-federation-in-ad-fs).

      * For OIDC: Follow the instructions in [Use group membership to enable federation in an OIDC-compliant IdP](set-up-federation-idp-oidc.html#use-group-membership-to-enable-federation-in-oidc).

   2. On the Identity Provider Details page:

      1. Select one of the following options:

         * For Entra ID: Enable Use group membership to allow federated sign on to Ping Identity.

         * For AD FS: Enable Use ADFS group membership to allow federated sign on to Ping Identity.

         * For OIDC: Enable Use OIDC group membership to allow federated sign on to Ping Identity.

      2. Enter the name of the group claim in the Group Claim Name field. For example, `groups`.

         |   |                                                                                                                   |
         | - | ----------------------------------------------------------------------------------------------------------------- |
         |   | By default, Entra ID sends the `ID` of the group. You might need to configure it to send the `name` of the group. |

      3. To apply an access level to specific IdP groups:

         * To apply the super administrator\[[1](#_footnotedef_1 "View footnote.")] access level:

           1. Locate the Group Identifiers field to the left of `Super Admins`.

           2. Enter one or more group identifiers. For example, `8c578f67-cac4-49eb-8f28-8e4f2c22945e`.

         * (Optional) To apply the tenant administrator access level:

           1. Locate the Group Identifiers field to the left of `Tenant Admins`.

           2. Enter one or more group identifiers. For example, `3623050d-3604-45a2-942e-f6be9ec9f9ed`.

         * (Optional) To apply the tenant auditor\[[5](#_footnotedef_5 "View footnote.")] access level:

           1. Locate the Group Identifiers field to the left of `Tenant Auditor`.

           2. Enter one or more group identifiers. For example, `eeb11282-cb38-42b9-909f-439cad25550e`.

         * (Optional) To apply the brand administrator\[[6](#_footnotedef_6 "View footnote.")] access level:

           1. Locate the Group Identifiers field to the left of `Brand Admin`.

           2. Enter one or more group identifiers. For example, `47e677ad-dfac-4e02-be5f-cff56fb31ed4`.

      4. Click Save.

#### Configure federation sign-on requirements

After you have enabled federated access to your tenant environments, you can choose how strictly to enforce it. It can be enforced for just tenant administrators or for both tenant administrators and super administrators\[[1](#_footnotedef_1 "View footnote.")]. These settings are stored in dynamic configuration, so need to be configured per environment.

|   |                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To understand how the instructions in this section fit into the process of configuring federated access across your tenant environments, refer to step 5 in the [high-level process](#configure-federated-access-across-your-tenant-environments). |

1. Sign on to the Advanced Identity Cloud admin console as a super administrator\[[1](#_footnotedef_1 "View footnote.")].

2. Go to Tenant settings, then click the Federation tab.

3. In the Enforcement section, click Edit.

4. On the Edit Tenant Federation Enforcement page, select one of the following items:

   * Optional for All Admins: Allow all administrators to use either their Advanced Identity Cloud credentials or federated access to sign on.

   * Required for All Admins Except Super Admins: Require all administrators that are not super administrators to use federated access to sign on. Super administrators can use their Advanced Identity Cloud credentials or federated access to sign on.

   * Required for All Admins: Require all administrators to use federated access to sign on. If you choose this option, then subsequently need to switch to a lower enforcement level, you must create a support case in the [Ping Identity Support Portal](https://support.pingidentity.com).

5. Click Update. It can take about 10 minutes for the changes to take effect.

6. On the Change Federation Enforcement? modal:

   * To confirm your changes, click Confirm.

   * To cancel your changes, click Cancel.

### Deactivate a federation IdP

You can deactivate a federation IdP and reactivate it later. For example, you might want to deactivate a federation IdP if the provider is experiencing technical issues. If you deactivate all federation IdPs for a tenant, tenant administrators can no longer use federation to sign on to the tenant.

You can only deactivate a federation IdP if one of the following is true:

* `Optional for All Admins` is selected as the federation enforcement level (learn more in [Configure federation sign-on requirements](#configure-federation-sign-on-requirements)).

* More than one federation IdP is enabled in the Advanced Identity Cloud tenant.

To deactivate a federation IdP:

1. Sign on to the Advanced Identity Cloud admin console of your development environment as a super administrator\[[1](#_footnotedef_1 "View footnote.")].

2. Go to Tenant settings, then click Federation.

3. Perform one of the following actions:

   * To deactivate a federation IdP, click the ellipsis icon ([icon: ellipsis-h, set=fa]) to the right of an active federation IdP, then click Deactivate.

   * To activate a federation IdP, click the ellipsis icon ([icon: ellipsis-h, set=fa]) to the right of a deactivated federation IdP, then click Activate.

4. Run a series of promotions to move the updated configuration to your UAT\[[7](#_footnotedef_7 "View footnote.")], staging, and production environments.

### Rotate a federation IdP client secret

Most IdPs force you to rotate the client secrets they generate by setting an expiry on the secret. To ensure that federated access continues uninterrupted,you must create and configure a new client secret before the old one expires. If the client secret is stored in an ESV, you can rotate it by creating a new [secret version](../tenants/esvs.html#secret-versions).

For your development, UAT\[[7](#_footnotedef_7 "View footnote.")], staging, or production environment:

1. In the IdP's UI:

   1. Locate the client configured for the Advanced Identity Cloud environment.

   2. Create a new secret and make a note of it:

      * For Azure AD, add a new client secret to the application.

      * For AD FS, reset the client secret for the application group.

      * For OIDC, refer to your IdP vendor's documentation on creating a new client secret.

2. In Advanced Identity Cloud admin console:

   1. Add a new [secret version](../tenants/esvs.html#secret-versions) to the ESV secret using the value of the new federation IdP secret from the previous step. Learn more in [Update an ESV referenced by a configuration placeholder](../tenants/configuration-placeholders.html#update_an_esv_referenced_by_a_configuration_placeholder).

   2. [Restart Advanced Identity Cloud services](../tenants/configuration-placeholders.html#restart-identity-cloud-services).

***

[1](#_footnoteref_1). A super administrator is a tenant administrator with elevated permissions for configuring tenant administrators and federated tenant access. Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).[2](#_footnoteref_2). Microsoft Entra ID was previously Microsoft Azure AD. Learn more in [New name for Azure Active Directory](https://learn.microsoft.com/en-us/entra/fundamentals/new-name).[3](#_footnoteref_3). The user info endpoint isn't needed if you configure groups.[4](#_footnoteref_4). A [sandbox environment](../tenants/environments-sandbox.html) is an [add-on capability](../product-information/add-on-capabilities.html).[5](#_footnoteref_5). A tenant auditor is a tenant administrator with read-only permissions. Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).[6](#_footnoteref_6). A brand administrator is a tenant administrator with permissions to only manage hosted pages settings. Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).[7](#_footnoteref_7). A [user acceptance testing (UAT) environment](../tenants/environments-uat.html) is an [add-on capability](../product-information/add-on-capabilities.html).

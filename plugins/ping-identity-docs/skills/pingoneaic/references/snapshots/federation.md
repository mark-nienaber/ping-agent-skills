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

---

---
title: Set up an OIDC-compliant IdP as a federation IdP
description: Set up an OIDC-compliant identity provider as a federation IdP for Advanced Identity Cloud by configuring an OIDC client and group membership
component: pingoneaic
page_id: pingoneaic:federation:set-up-federation-idp-oidc
canonical_url: https://docs.pingidentity.com/pingoneaic/federation/set-up-federation-idp-oidc.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Federation", "Authentication", "Setup &amp; Configuration"]
page_aliases: ["federation:set-up-federation-provider-oidc.adoc"]
section_ids:
  configure-oidc-as-a-federation-idp: "Task 1: Configure OIDC-compliant IdP as a federation IdP"
  use-group-membership-to-enable-federation-in-oidc: "Task 2: Use group membership to enable federation in an OIDC-compliant IdP"
---

# Set up an OIDC-compliant IdP as a federation IdP

To use an OIDC-compliant IdP as a federation IdP for a PingOne Advanced Identity Cloud tenant environment, you need to create a new OIDC client.

## Task 1: Configure OIDC-compliant IdP as a federation IdP

1. Read your IdP vendor's documentation on configuring an OIDC client.

2. Configure an OIDC client profile:

   1. Choose a client ID or note the automatically generated client ID. Some OIDC IdPs let you choose the client ID while others autogenerate it for you.

      |   |                                                                                |
      | - | ------------------------------------------------------------------------------ |
      |   | In Advanced Identity Cloud, use this in an application's Application ID field. |

   2. Choose a client secret or note the automatically generated client secret. Some OIDC IdPs let you choose the client secret while others autogenerate it for you.

      |   |                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------- |
      |   | In Advanced Identity Cloud, enter this value in an application's Application Secret field (or set in an ESV mapped to that field). |

   3. Configure the allowed scopes. Recommended scopes: `openid`, `profile`, and `email`.

   4. Configure the client authentication method. Supported authentication methods: `client_secret_post`, `client_secret_basic`, or `none`.

3. Obtain the well-known URL from the OIDC-compliant IdP. You will enter this URL when you enable the IdP in Advanced Identity Cloud.

   |   |                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------- |
   |   | In Advanced Identity Cloud, enter this value in an application's Well-known Endpoint field (or set in an ESV mapped to that field). |

## Task 2: Use group membership to enable federation in an OIDC-compliant IdP

Groups let you add and remove sets of administrators based on their group membership in your IdP. You can also specify the level of administrator access (super administrator\[[1](#_footnotedef_1 "View footnote.")] or tenant administrator) for groups of users.

1. Read your IdP vendor's documentation on configuring groups in your OIDC client.

2. Obtain the name of the `groups` claim from the OIDC-compliant IdP.

   |   |                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------- |
   |   | In Advanced Identity Cloud, enter this value in an application's Group Claim Name field (or set in an ESV mapped to that field). |

3. (Optional) Set up super administrator\[[1](#_footnotedef_1 "View footnote.")] groups:

   1. Set up one or more groups for users that need to be super administrators\[[1](#_footnotedef_1 "View footnote.")] when they access the tenant using your IdP.

   2. Note the group ID (or group IDs).

      |   |                                                                                                                                                                                  |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In Advanced Identity Cloud, enter the group ID (or group IDs) in an application's Group Identifiers field to the left of `Super Admins` (or set in an ESV mapped to that field). |

4. (Optional) Set up tenant administrator groups:

   1. Set up one or more groups for users that need to be tenant administrators when they access the tenant using your IdP.

   2. Note the group ID (or group IDs).

      |   |                                                                                                                                                                                   |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In Advanced Identity Cloud, enter the group ID (or group IDs) in an application's Group Identifiers field to the left of `Tenant Admins` (or set in an ESV mapped to that field). |

5. (Optional) Set up tenant auditor\[[2](#_footnotedef_2 "View footnote.")] groups:

   1. Set up one or more groups for users that need to be tenant auditors when they access the tenant using your IdP.

   2. Note the group ID (or group IDs).

      |   |                                                                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In Advanced Identity Cloud, enter the group ID (or group IDs) in an application's Group Identifiers field to the left of `Tenant Auditor` (or set in an ESV mapped to that field). |

6. (Optional) Set up brand administrator\[[3](#_footnotedef_3 "View footnote.")] groups:

   1. Set up one or more groups for users that need to be brand administrators when they access the tenant using your IdP.

   2. Note the group ID (or group IDs).

      |   |                                                                                                                                                                                 |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In Advanced Identity Cloud, enter the group ID (or group IDs) in an application's Group Identifiers field to the left of `Brand Admin` (or set in an ESV mapped to that field). |

***

[1](#_footnoteref_1). A super administrator is a tenant administrator with elevated permissions for configuring tenant administrators and federated tenant access. Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).[2](#_footnoteref_2). A tenant auditor is a tenant administrator with read-only permissions. Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).[3](#_footnoteref_3). A brand administrator is a tenant administrator with permissions to only manage hosted pages settings. Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).

---

---
title: Set up Microsoft Active Directory Federation Services as a federation IdP
description: Set up Microsoft AD FS as a federation IdP for Advanced Identity Cloud by creating a relying party trust and application group
component: pingoneaic
page_id: pingoneaic:federation:set-up-federation-idp-microsoft-ad-fs
canonical_url: https://docs.pingidentity.com/pingoneaic/federation/set-up-federation-idp-microsoft-ad-fs.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Federation", "Authentication", "Setup &amp; Configuration"]
page_aliases: ["federation:set-up-federation-provider-microsoft-ad-fs.adoc"]
section_ids:
  create-a-relying-party-trust: "Task 1: Create a relying party trust"
  create-an-application-group: "Task 2: Create an application group"
  include-additional-identity-claims-in-tokens: "Task 3: Include additional identity claims in tokens"
  obtain-the-well-known-endpoint-for-the-ad-fs-open-id-connect-service: "Task 4: Obtain the well-known endpoint for the AD FS OpenID Connect service"
  use-group-membership-to-enable-federation-in-ad-fs: "Task 5: Use group membership to enable federation in AD FS"
  create-groups-containing-identity-cloud-tenant-administrators-ad-fs: Create groups containing Advanced Identity Cloud tenant administrators
  include-additional-claims-in-the-tokens-for-identity-cloud-ad-fs: Include additional claims in the tokens for Advanced Identity Cloud
---

# Set up Microsoft Active Directory Federation Services as a federation IdP

To use Microsoft Active Directory Federation Services (AD FS) as a federation IdP for a PingOne Advanced Identity Cloud tenant environment, you must create a relying party trust. The trust is a set of identifiers, names, and rules that identify the partner or web-application to the federation service.

Afterward, you must create an application group that uses single sign-on (SSO) to access applications that are outside the corporate firewall.

|   |                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The instructions in this document assume that you have a self-hosted instance of AD FS version 4.0, running on Windows Server 2016 or higher. |

## Task 1: Create a relying party trust

In this step, you create a relying party trust. The trust is a set of identifiers, names, and rules that identify the partner or web-application to the federation service.

1. Open the Server Manager console by clicking Server Manager on the Start screen or clicking Server Manager in the taskbar on the desktop.

2. In AD FS Management, select Tools > AD FS.

3. On the AD FS dialog, in the left panel, click Relying Party Trusts.

4. In the Actions pane, select Add Relying Party Trust.

5. On the Welcome page of the Add Relying Party Trust wizard, select Claims aware.

6. On the Select Data Source page, select Enter data about the relying party manually.

7. On the Specify Display Name page, enter a display name.

8. Complete the steps in the wizard until you reach the Configure Identifiers page.

9. On the Configure Identifiers page, add a relying party trust identifier for each of your tenant environments using the following URL format:

   https\://\<tenant-env-fqdn>/am

   For example, if your [tenant environment FQDN](../tenants/environments.html#tenant-environment-fqdns) is `openam-mycompany-ew2.id.forgerock.io`, use `https://openam-mycompany-ew2.id.forgerock.io/am`.

10. On the Choose Access Control Policy page, select the appropriate settings according to your corporate policy.

11. Complete the steps in the wizard until you reach the Finish page.

## Task 2: Create an application group

In this step, you create an application group that uses single sign-on (SSO) to access applications.

1. In the AD FS editor, select Application Groups.

2. In the Actions pane, select Add Application Group.

3. Complete the Add Application Groups wizard as follows:

   1. On the Welcome page of the Add Application Groups wizard, provide a name and a description and select the Server application accessing a web API template.

   2. On the Server application page:

      * Accept the proposed `Name`.

      * Note the `Client Identifier`.

        |   |                                                                                                                                |
        | - | ------------------------------------------------------------------------------------------------------------------------------ |
        |   | In Advanced Identity Cloud, enter this value in an application's Application ID field (or set in an ESV mapped to that field). |

      * Add tenant Redirect URIs for each of your tenant environments using the following URL format:

        https\://\<tenant-env-fqdn>/login/admin

        For example, if your [tenant environment FQDN](../tenants/environments.html#tenant-environment-fqdns) is `openam-mycompany-ew2.id.forgerock.io`, use `https://openam-mycompany-ew2.id.forgerock.io/login/admin`.

   3. Click Register to create the application.

   4. On the Configure Application Credentials page:

      1. Select Generate a shared secret. The secret acts as a password for the application.

      2. Use the Copy to clipboard button to copy the secret.

         |   |                                                                                                                                    |
         | - | ---------------------------------------------------------------------------------------------------------------------------------- |
         |   | In Advanced Identity Cloud, enter this value in an application's Application Secret field (or set in an ESV mapped to that field). |

   5. Click Next.

   6. On the Configure Web API page, add the `client identifier` you noted earlier.

   7. Click Next.

   8. On the Choose Access Control Policy page, select the appropriate settings according to your corporate policy.

   9. Click Next.

   10. On the Configure Application Permissions page, check the following permitted scopes:

       * allatclaims: Lets the application request the claims in the access token that is added to the ID token.

       * email: Lets the application request an email claim for the signed-in user.

       * openid: Lets the application request use of the OpenID Connect authentication protocol.

       * profile: Lets the application request profile-related claims for the signed-in user.

   11. Click Next.

   12. On the Summary page, review your selections.

   13. Click Next.

   14. On the Complete page, click Close.

## Task 3: Include additional identity claims in tokens

In this step, you configure AD FS to include additional claims in the identity tokens it issues. This is necessary because AD FS does not support the `/userinfo` endpoint.

1. In the AD FS editor, select Application Groups.

2. In the Actions pane, select Add Application Group.

3. Double-click your application group.

4. In the Applications section, in the Web API area, select your application, and click Edit.

5. Click the Issuance Transform Rules tab, and click Add Rule.

6. To include active directory attributes of the users that are accessing Advanced Identity Cloud, in the Claim rule template drop-down field, select Send LDAP Attributes as Claims.

7. In the Claim rule name field, enter a name for the claim rule. For example, Profile Attributes.

8. In the Attribute store drop-down field, select Active Directory.

9. To map LDAP attributes to name spaces in Advanced Identity Cloud, complete the Mapping of LDAP attributes to outgoing claim types table:

   ![Mapping of LDAP attributes to outgoing claim types in the claim rule](_images/federation-map-ldap-attributes.png)

   | LDAP Attribute (Select or type to add more) | Outgoing Claim Type (Select or type to add more) |
   | ------------------------------------------- | ------------------------------------------------ |
   | E-Mail Addresses                            | mail                                             |
   | Given-Name                                  | givenName                                        |
   | Surname                                     | sn                                               |

10. Click Finish.

11. On the Issuance Transform Rules tab, click Apply.

12. Click OK twice.

## Task 4: Obtain the well-known endpoint for the AD FS OpenID Connect service

In this step, you identify the well-known URI that the AD FS OpenID Connect service uses.

1. In the AD FS editor, select Service > Endpoints.

2. In the middle pane, scroll down to the OpenID Connect section.

3. In the OpenID Connect section, note the URL path. The well-known end point URL is the concatenation of the host name of the machine running AD FS and the URL path you just noted.

   |   |                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------- |
   |   | In Advanced Identity Cloud, enter this value in an application's Well-known Endpoint field (or set in an ESV mapped to that field). |

## Task 5: Use group membership to enable federation in AD FS

Groups let you add and remove sets of administrators based on their group membership in your IdP. You can also specify the level of administrator access (super administrator\[[1](#_footnotedef_1 "View footnote.")] or tenant administrator) for groups of users.

### Create groups containing Advanced Identity Cloud tenant administrators

In AD FS, create one or more groups of administrators that correspond to these [tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups) in Advanced Identity Cloud:

* Super administrators\[[1](#_footnotedef_1 "View footnote.")]

* Tenant administrators

* Tenant auditors\[[2](#_footnotedef_2 "View footnote.")]

* Brand administrators\[[3](#_footnotedef_3 "View footnote.")]

When naming each group, use a prefix that identifies the group as relevant for Advanced Identity Cloud; this allows the AD FS claim scripts to only include relevant groups. Make sure to include the tenant name as part of the group name to help you identify the tenant the group is for.

Example: group name template

`<prefix>-<tenant identifier>-<admin group>`.

Example: group name

`aic-dev-superadmin`

Example: All group names for a standard promotion group of tenants and a sandbox tenant.

* `aic-dev-superadmin`

* `aic-dev-tenantadmin`

* `aic-dev-tenantauditor`

* `aic-dev-brandadmin`

* `aic-staging-superadmin`

* `aic-staging-tenantadmin`

* `aic-staging-tenantauditor`

* `aic-staging-brandadmin`

* `aic-prod-superadmin`

* `aic-prod-tenantadmin`

* `aic-prod-tenantauditor`

* `aic-prod-brandadmin`

* `aic-sandbox-superadmin`

* `aic-sandbox-tenantadmin`

* `aic-sandbox-tenantauditor`

* `aic-sandbox-brandadmin`

### Include additional claims in the tokens for Advanced Identity Cloud

To use group membership to enable federation, you must add *issuance transform* rules to enable AD FS to add additional group claims.

You must add the following two rules in AD FS:

* **Store Groups rule**: A rule that collects all the user groups and stores them in a claim with the indicated name. The script produces a potentially large claim.

* **Issue Groups rule**: A rule that takes the long list of groups that the Store Groups script creates and only selects the groups with the Group Name Prefix that is relevant for the claim.

  1. In the AD FS editor, select Application Groups.

  2. In the Actions pane, select the group you previously created.

  3. Right-click the group and select Properties.

  4. In the Applications section, in the Web API area, select your application, and click Edit.

  5. Click the Issuance Transform Rules tab.

  6. Click Add Rule.

  7. To include active directory attributes of the users that are accessing Advanced Identity Cloud, in the Claim rule template drop-down field, select Send Claims Using a Custom Rule.

  8. In the Custom rule field, enter the rule definition for the Store Groups rule.

     * Store Groups rule template:

       `c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"] ⇒ add(store = "Active Directory", types = ("<Groups Claim Name>"), query = ";tokenGroups;{0}", param = c.Value);`

     * Store Groups rule example:

       `c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"] ⇒ add(store = "Active Directory", types = ("groups"), query = ";tokenGroups;{0}", param = c.Value);`

       * "groups" is the name of the resulting claim that you enter into the Groups Claim Name field on the Identity Provider Details page in the Advanced Identity Cloud.

  9. Click Finish.

  10. Click Add Rule.

  11. To include active directory attributes of the users that are accessing Advanced Identity Cloud, in the Claim rule template drop-down field, select Send Claims Using a Custom Rule.

  12. In the Custom rule field, enter the rule definition for the Issue Groups rule.

      * Issue Groups rule template:

        `c:[Type == "<Groups Claim Name>", Value =~ "^<Group Name Prefix>-.+"] ⇒ issue(claim = c);`

      * Issue Groups rule example:

        `c:[Type == "groups", Value =~ "^aic-.+"] ⇒ issue(claim = c);`

        * "groups" is the name of the resulting claim that you enter into the Groups Claim Name field on the Identity Provider Details page in the Advanced Identity Cloud.

        * "aic" is the prefix you chose for the group names.

  13. Click Finish.

***

[1](#_footnoteref_1). A super administrator is a tenant administrator with elevated permissions for configuring tenant administrators and federated tenant access. Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).[2](#_footnoteref_2). A tenant auditor is a tenant administrator with read-only permissions. Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).[3](#_footnoteref_3). A brand administrator is a tenant administrator with permissions to only manage hosted pages settings. Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).

---

---
title: Set up Microsoft Entra ID as a federation IdP
description: Set up Microsoft Entra ID as a federation IdP for Advanced Identity Cloud by registering an application and configuring group membership
component: pingoneaic
page_id: pingoneaic:federation:set-up-federation-idp-microsoft-entra-id
canonical_url: https://docs.pingidentity.com/pingoneaic/federation/set-up-federation-idp-microsoft-entra-id.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Federation", "Authentication", "Setup &amp; Configuration"]
page_aliases: ["federation:set-up-federation-provider-microsoft-azure-ad.adoc"]
section_ids:
  configure-entra-id-as-a-federation-idp: "Task 1: Configure Entra ID as a federation IdP"
  use-group-membership-to-enable-federation-in-entra-id: "Task 2: Use group membership to enable federation in Entra ID"
---

# Set up Microsoft Entra ID as a federation IdP

To use Microsoft Entra ID (Entra ID) as a federation IdP for a PingOne Advanced Identity Cloud tenant environment, you need to create a new app registration.

|   |                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Microsoft Entra ID used to be known by the name Microsoft Azure AD. Learn more in [New name for Azure Active Directory](https://learn.microsoft.com/en-us/entra/fundamentals/new-name). |

## Task 1: Configure Entra ID as a federation IdP

1. In a browser, navigate to the [Microsoft Entra admin center](https://entra.microsoft.com/#home).

2. Create a new application:

   1. Click Applications, then click App registrations.

   2. In the top toolbar, click [icon: add, set=material, size=inline] New registration.

   3. On the Register an application page:

      1. Enter the application Name. For example, "Advanced Identity Cloud administrators".

      2. Select Accounts in this organizational directory only (Me only - Single tenant) from the Supported account types list.

      3. In the Redirect URI (optional) section:

         1. In the left-hand field, select Web.

         2. In the right-hand field, enter the redirect URI for an Advanced Identity Cloud environment using the following URL format:

            https\://\<tenant-env-fqdn>/login/admin

            For example, if your [tenant environment FQDN](../tenants/environments.html#tenant-environment-fqdns) is `openam-mycompany-ew2.id.forgerock.io`, use `https://openam-mycompany-ew2.id.forgerock.io/login/admin`.

      4. Click Register to create the application.

3. Find the application ID:

   1. In the application menu, click Overview.

   2. Note the Application (client) ID of the application. For example, `6b05a314-c721-4aa6-baad-7f533cbd25b0`.

      |   |                                                                                                                                |
      | - | ------------------------------------------------------------------------------------------------------------------------------ |
      |   | In Advanced Identity Cloud, enter this value in an application's Application ID field (or set in an ESV mapped to that field). |

4. Find the application's well-known endpoint:

   1. In the top toolbar, click Endpoints.

   2. Note the OpenID Connect metadata document endpoint of the application. For example, `https://login.microsoftonline.com/0e076864-135f-4914-9b72-80efaa4c3dcf/v2.0/.well-known/openid-configuration`.

      |   |                                                                                                                                     |
      | - | ----------------------------------------------------------------------------------------------------------------------------------- |
      |   | In Advanced Identity Cloud, enter this value in an application's Well-known Endpoint field (or set in an ESV mapped to that field). |

5. Add the `email` claim to the application's token configuration:

   1. In the application menu, click Token configuration.

   2. Click [icon: add, set=material, size=inline] Add optional claim.

   3. In the Add optional claim modal:

      1. Select the ID token type.

      2. Select the email claim checkbox.

      3. Click Add.

      4. The first time you add the `email` claim, the UI displays an Add optional claim dialog box to let you grant the appropriate API permissions:

         ![Add optional claim dialog box with Turn on the Microsoft Graph profile permission checkbox selected.](_images/entra-id-add-optional-claim-email.png)

         1. Select the Turn on the Microsoft Graph profile permission checkbox.

         2. Click Add.

6. Add an application secret:

   1. In the application menu, click Certificates & secrets.

   2. Click [icon: add, set=material, size=inline] New client secret.

   3. In the Add a client secret modal:

      1. (Optional) Enter a Description.

      2. Select an option from the Expires list (or accept the default selection of 180 days).

      3. Click Add to create the secret.

   4. Note the Value of the new secret. Do this immediately, as it can only be viewed for a short time after creation.

      |   |                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------- |
      |   | In Advanced Identity Cloud, enter this value in an application's Application Secret field (or set in an ESV mapped to that field). |

## Task 2: Use group membership to enable federation in Entra ID

Groups let you add and remove sets of administrators based on their group membership in your IdP. You can also specify the level of administrator access (super administrator\[[1](#_footnotedef_1 "View footnote.")] or tenant administrator) for groups of users.

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | If you modify group membership in Entra ID, it can take a few minutes for those changes to take effect in Advanced Identity Cloud. |

1. In a browser, navigate to the [Microsoft Entra admin center](https://entra.microsoft.com/#home).

2. Create one or more groups:

   1. (Optional) Create a group for super administrators\[[1](#_footnotedef_1 "View footnote.")]:

      1. Click Groups, then click All groups.

      2. In the top toolbar, click New group.

      3. In the New Group page:

         1. Select Microsoft 365 from the Group type list.

         2. Enter the super administrator Group name. For example, `Super administrators`.

         3. Click Create.

      4. In the All groups page, in the top toolbar, click Refresh.

      5. Click the new group you just created.

      6. Note the Object ID of the group. For example, `8c578f67-cac4-49eb-8f28-8e4f2c22945e`.

         |   |                                                                                                                                   |
         | - | --------------------------------------------------------------------------------------------------------------------------------- |
         |   | In Advanced Identity Cloud, enter this value in an application's Group Identifiers field (or set in an ESV mapped to that field). |

   2. (Optional) Repeat step 2a to create a group for tenant administrators.

      |   |                                                                                                                                                                                   |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In Advanced Identity Cloud, enter the group ID (or group IDs) in an application's Group Identifiers field to the left of `Tenant Admins` (or set in an ESV mapped to that field). |

   3. (Optional) Repeat step 2a to create a group for tenant auditors\[[2](#_footnotedef_2 "View footnote.")].

      |   |                                                                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In Advanced Identity Cloud, enter the group ID (or group IDs) in an application's Group Identifiers field to the left of `Tenant Auditor` (or set in an ESV mapped to that field). |

   4. (Optional) Repeat step 2a to create a group for brand administrators\[[3](#_footnotedef_3 "View footnote.")].

      |   |                                                                                                                                                                                 |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In Advanced Identity Cloud, enter the group ID (or group IDs) in an application's Group Identifiers field to the left of `Brand Admin` (or set in an ESV mapped to that field). |

3. Set up the application to acquire claims from the identity token instead of the user info endpoint:

   1. Click Applications, then click App registrations.

   2. Click All applications, then click your application.

   3. In the application menu, click Token configuration.

   4. Click [icon: add, set=material, size=inline] Add optional claim.

   5. In the Add optional claim modal:

      1. Select the ID token type.

      2. Select the email, family\_name, and given\_name claim checkboxes.

      3. Click Add.

      4. The first time you add these new claims, the UI displays an Add optional claim dialog box to let you grant the appropriate API permissions:

         ![Add optional claim dialog box with Turn on the Microsoft Graph profile permission checkbox selected.](_images/entra-id-add-optional-claim-additional.png)

         1. Select the Turn on the Microsoft Graph profile permission checkbox.

         2. Click Add.

   6. Click [icon: add, set=material, size=inline] Add groups claim.

   7. In the Edit groups claim modal:

      1. Select Groups assigned to the application.

      2. Click Add.

   8. Confirm the name of the groups claim you added is `groups`.

      |   |                                                                                                                                  |
      | - | -------------------------------------------------------------------------------------------------------------------------------- |
      |   | In Advanced Identity Cloud, enter this value in an application's Group Claim Name field (or set in an ESV mapped to that field). |

***

[1](#_footnoteref_1). A super administrator is a tenant administrator with elevated permissions for configuring tenant administrators and federated tenant access. Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).[2](#_footnoteref_2). A tenant auditor is a tenant administrator with read-only permissions. Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).[3](#_footnoteref_3). A brand administrator is a tenant administrator with permissions to only manage hosted pages settings. Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).
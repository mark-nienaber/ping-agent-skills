---
title: Authenticating Azure AD tenants who don&#8217;t have their own Azure account
description: Create a PingFederate workflow to authenticate users from different Microsoft tenants.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_authn_azure_ad_tenants
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_authn_azure_ad_tenants.html
revdate: April 13, 2025
page_aliases: ["workforce_use_cases:htg_authn_azure_ad_tenants_oidc_app_for_authn.adoc", "workforce_use_cases:htg_authn_azure_ad_tenants_view_update_app.adoc", "workforce_use_cases:htg_authn_azure_ad_tenants_oidc_idp_pf.adoc"]
section_ids:
  component: Component
  creating-an-oidc-v2-app-for-authn: Creating an OIDC V2 app for AuthN
  steps: Steps
  result: Result:
  viewing-and-updating-the-app-in-add-dashboard: Viewing and updating the app in ADD dashboard
  steps-2: Steps
  result-2: Result:
  creating-an-openid-connect-idp-connection-in-pingfederate: Creating an OpenID Connect IdP connection in PingFederate
  steps-3: Steps
  result-3: Result:
  troubleshooting: Troubleshooting:
  result-4: Result
---

# Authenticating Azure AD tenants who don't have their own Azure account

Create a PingFederate workflow to authenticate users from different Microsoft tenants.

If you use Microsoft Azure AD as an identity provider (IdP), a standard IdP connection won't authenticate users from other Azure tenants or from other Microsoft account types, such as outlook.com, live.com, or hotmail.com.

If you have users from these other tenants, you can authenticate them through the Azure Application Registration Portal and V2 endpoints.

## Component

PingFederate 10.0

## Creating an OIDC V2 app for AuthN

Register a new OpenID Connect (OIDC) application in the Azure App registration service.

### Steps

1. In the [Azure portal](https://portal.azure.com/), go to **App registrations > New registration**.

2. Enter an application name and click **Create**.

   |   |                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Give your application a name that identifies it and differentiates it from applications created through Azure AD, such as `PingAuthentication-V2`. |

3. Under **Supported account types**, click **Accounts in any organizational directory and personal Microsoft accounts**.

4. Click **Register**.

   #### Result:

   The **Overview** tab provides the **Application (client) ID**. This is the **Client ID** for your PingFederate OIDC IdP connection.

5. Click **API permissions**.

6. Click **Add a permission > Microsoft Graph > Delegated permissions > Directory** and select the **Directory.Read.All** checkbox.

7. Click **Add permissions**.

8. (Optional) Click the **Branding** tab to customize the following:

   * Brand logo

   * Home page URL

   * Terms of Service URL

   * Privacy Statement URL

9. At the top of the page, click **Save**.

## Viewing and updating the app in ADD dashboard

Verify and update the permissions in your v2 Azure application.

### Steps

1. In the [Azure portal](https://portal.azure.com/), go to **App registrations**.

2. Click the V2 application that you created to open the **Overview** tab.

3. Click **Authentication**.

   #### Result:

   Under the **Supported account types** heading, you see `Accounts in any organizational directory (Any Azure AD directory - Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)`.

4. At the top of the page, click **Save**.

## Creating an OpenID Connect IdP connection in PingFederate

### Steps

1. In PingFederate, go to **Authentication > Integration > IdP Connections** and click **Create Connection**.

2. On the **Connection Type** tab, select **Browser SSO**.

3. In the **Protocol** list, select **OpenID Connect**.

4. Click **Next**.

5. On the **Connection Options** tab, click **Next**.

6. On the **General Info** tab, enter the following values:

   1. In the **Issuer** field, enter `https://login.microsoftonline.com/common` and click **Load Metadata**.

      #### Result:

      When you click **Load Metadata**, the **Issuer** field is updated with a metadata URL.

   2. Replace the *\<tenant>* placeholder at the end of the URL with your Microsoft Tenant ID and add `/v2.0` to the end of the URL.

      |   |                                                                                                       |
      | - | ----------------------------------------------------------------------------------------------------- |
      |   | You can find your Tenant ID at **Azure Active Directory > Overview** in your Microsoft Azure account. |

   3. Select the **Enable Additional Issuers** checkbox.

   4. In the **Connection Name** field, enter a plain-language identifier for the connection, for example a company or department name.

      This name is displayed in the connection list in the administration console.

   5. In the **Client ID** field, enter the **Application (client) ID** value found in the **App registrations** menu in Azure AD.

   6. Click **Next**.

7. On the **Additional issuers** tab, select the **Accept All issuers (Not Recommended)** checkbox and click **Save**.

8. On the **Browser SSO** tab, click **Configure Browser SSO**.

   1. On the **User-Session Creation** tab, click **Configure User-Session Creation**

   2. Choose one of the **Identity Mapping** tab options:

      * Click **Account Mapping** if you plan to pass end-user claims to the target application through a service provider (SP) adapter instance or an authentication policy contract if your PingFederate server is a federation hub that bridges an OpenID provider to an SP.

      * Click **Account Linking** if your target application requires account linking.

      * Click **No Mapping** if you plan to pass end-user claims to the target application through an authentication policy contract in an SP authentication policy.

9. Delete the attributes that are unnecessary to your application in the **Attribute Contract** menu generated by the issuer metadata in step 5.

   #### Troubleshooting:

   You are likely to encounter attribute-related errors when testing your connection. If this occurs, review the `server.log` file to see what attributes or claims are sent to Azure and delete the unnecessary attributes from your attribute contract.

10. (Optional) On the **Target Session Mapping** menu, click **Map New Adapter Instance** to map end-user claims to the target application through an SP adapter instance or an authentication policy contract.

    Learn more in [Managing target session mappings](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-100.pdf#page=659) (page 659).

11. On the **Summary** tab, review the **User Session Creation** settings and click **Save**.

12. On the **Protocol Settings** tab, click **Configure Protocol Settings**.

13. On the **OpenID Provider Info** tab, enter the following values.

    | Field                      | Value                                                            |
    | -------------------------- | ---------------------------------------------------------------- |
    | **Authorization Endpoint** | `https://login.microsoftonline.com/common/oauth2/v2.0/authorize` |
    | **Token Endpoint**         | `https://login.microsoftonline.com/common/oauth2/v2.0/token`     |
    | **User Info Endpoint**     | `https://graph.microsoft.com/oidc/userinfo`                      |
    | **JWKS URL**               | `https://login.microsoftonline.com/common/discovery/v2.0/keys`   |

14. When you have finished configuring the identity provider (IdP) connection, copy the **Redirect URI** from the **Activation & Summary** tab and add it to your V2 application.

    1. In your Azure account, go to **App registrations**.

    2. Click the application you want to connect.

    3. Click **Authentication > Add a platform > Web**.

    4. Paste the redirect URI into the **Enter the redirect URI of the application** field.

    5. Select both the **Access Tokens** and **ID Tokens** checkboxes.

    6. Click **Configure**.

### Result

You can now authenticate users with non-Azure Microsoft accounts.

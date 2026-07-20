---
title: Authenticating Azure AD tenants who don&#8217;t have their own Azure account
description: Create a PingFederate workflow to authenticate users from different Microsoft tenants.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_authn_azure_ad_tenants
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_authn_azure_ad_tenants.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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

---

---
title: Configuring a SAML application
description: Configure a SAML application in PingFederate, PingOne, and PingOne for Enterprise.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_config_saml_app
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_config_saml_app.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["workforce_use_cases:htg_config_saml_app_pf.adoc", "workforce_use_cases:htg_config_saml_app_p1.adoc", "workforce_use_cases:htg_config_saml_app_p14e.adoc"]
section_ids:
  configuring-a-saml-application-in-pingfederate: Configuring a SAML application in PingFederate
  before-you-begin: Before you begin
  steps: Steps
  configuring-a-saml-application-in-pingone: Configuring a SAML application in PingOne
  about-this-task: About this task
  steps-2: Steps
  choose-from: Choose from:
  next-steps: Next steps
  configuring-a-saml-application-in-pingone-for-enterprise: Configuring a SAML application in PingOne for Enterprise
  before-you-begin-2: Before you begin
  steps-3: Steps
  result: Result
---

# Configuring a SAML application

Configure a SAML application in PingFederate, PingOne, and PingOne for Enterprise.

Read the following sections for instructions for each product.

## Configuring a SAML application in PingFederate

Configure a SAML application in PingFederate.

### Before you begin

**Component**

* PingFederate 10.1

Make sure you have the following:

* A datastore connection

* A configured password credential validator (PCV)

* A configured identity provider (IdP) adapter.

* An IdP digital signing certificate

### Steps

1. In the PingFederate administrative console, go to **Applications > Integration > SP Connections**.

2. Click **Create Connection**.

3. On the **Connection Template** tab, click **Do not use a template for this connection**. Click **Next**.

4. On the **Connection Type** tab, select the **Browser SSO Profiles** checkbox.

5. In the **Protocol** list, select **SAML 2.0**. Click **Next**.

6. On the **Connection Options** tab, leave the **Browser SSO** checkbox selected, and then click **Next**.

7. On the **Import Metadata** tab, import service provider (SP) metadata, pull from a URL, or enter the data manually. Click **Next**.

   In this example, we assume that SP metadata is provided.

8. On the **General Info** tab, provide a **Connection Name** if needed and review the information. Click **Next**.

   |   |                                                              |
   | - | ------------------------------------------------------------ |
   |   | **Entity ID** and **Base URL** should be provided by the SP. |

9. On the **Browser SSO** tab, click **Configure Browser SSO**.

10. On the **SAML Profiles** tab, select the **IdP-Intitiated SSO** and **SP-Initiated SSO** checkboxes. Click **Next**.

11. On the **Assertion Lifetime** tab, leave the default entries, and then click **Next**.

12. On the **Assertion Creation** tab, click **Configure Assertion Creation**.

13. On the **Identity Mapping** tab, click **Standard**. Click **Next**.

14. On the **Attribute Contract** tab, ensure that whatever attributes you need for the SP are defined here. Click **Next**.

15. On the **Authentication Source Mapping** tab, click **Map New Adapter Instance**.

16. On the **Adapter Instance** tab, from the **Adapter Instance** list, select your previously configured HTML form adapter. Click **Next**.

17. On the **Mapping Method** tab, leave the default selection, and then click **Next**.

18. On the **Attribute Contract Fulfillment** tab, from the **Source** list for **SAML\_SUBJECT**, select **Adapter**.

19. From the **Value** list, depending on what the SP is expecting, select **mail** or **uid**.

20. Define any other mappings as needed. Click **Next**.

    You can leverage hard-coded "Text" for sending values to the SP connection.

21. On the **Issuance Criteria** tab, click **Next**.

22. On the **Summary** tab, review your entries, and then click **Done**.

    ![Screen capture of the IdP Adapter Mapping Summary tab. The bottom of the screen capture shows a hyperlink option to Cancel and buttons for Save Draft, Previous, and Done.](_images/rde1600200768900.png)

23. On the **Authentication Source Mapping** tab, click **Next**.

24. On the **Summary** tab, review your entries, and then click **Done**.

25. On the **Assertion Creation** tab, click **Next**.

26. On the **Protocol Settings** tab, click **Configure Protocol Settings**.

27. On the **Assertion Consumer Service URL** tab, ensure you see an entry for your SP based on the metadata that you uploaded. Click **Next**.

28. On the **Allowable SAML Bindings** tab, **POST** should be selected. Click **Next**.

29. On the **Signature Policy** tab, click **Always Sign the SAML Assertion**. Click **Next**.

30. On the **Encryption Policy** tab, click **None**. Click **Next**.

31. On the **Summary** tab, review your entries, and then click **Done**.

    ![Screen capture of the Protocol Settings Summary tab. The bottom of the screen capture shows a hyperlink option to Cancel and buttons for Save Draft, Previous, and Done.](_images/kdm1600201023572.png)

32. On the **Protocol Settings** tab, click **Next**.

33. On the **Summary** tab, review your entries, and then click **Done**.

    ![Screen capture of the Browser SSO Summary tab. The bottom of the screen capture shows a hyperlink option to Cancel and buttons for Save Draft, Previous, and Done.](_images/xnt1600201249127.png)

34. On the **Browser SSO** tab, click **Next**.

35. On the **Credentials** tab, click **Configure Credentials**.

36. On the **Digital Signature Settings** tab, from the **Signing Certificate** list, select your organization's default signing certificate that you previously created.

37. Select the **Include the Certificate in the Signature \<KeyInfo> Element** check-box. Click **Next**.

38. On the **Summary** tab, review your entries, and then click **Done**.

    ![Screen capture of the Summary tab. The bottom of the screen capture shows a hyperlink option to Cancel and buttons for Save Draft, Previous, and Done.](_images/bax1600201729793.png)

39. On the **Credentials** tab, click **Next**.

40. On the **Activation & Summary** tab, click the toggle to enable the connection, and then scroll to the bottom and click **Save**.

    The connection status is enabled when the toggle is green. You must click **Save** or your work will be lost.

    ![Screen capture of the Activation and Summary window showing the connection status as enabled.](_images/ypw1601419641147.png)

\===Next steps

Click on the SP connection that you just created and copy the **SSO-URL** link. Start a private browsing session and test your connection using the **SSO-URL** link.

## Configuring a SAML application in PingOne

Configure a SAML application in PingOne.

### About this task

In the following configuration, values will vary depending on the identity provider (IdP) requirements.

|   |                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some application settings can only be configured after the application is created. Learn more in [Editing an application](https://docs.pingidentity.com/pingone/applications/p1_editing_applications.html). |

### Steps

1. Go to **Applications > Applications**.

2. Click the **[icon: plus, set=fa]**icon.

3. Create the application profile by entering the following:

   * **Application name**: A unique identifier for the application.

   * **Description** (optional): A brief characterization of the application.

   * **Icon** (optional): A graphic representation of the application. Use a file up to 1MB in JPG, JPEG, GIF, or PNG format.

4. For **Application Type**, select **SAML Application**.

5. Click **Configure** and specify the details of the connection between the application and PingOne.

   You can enter the values manually, or import them from a file or URL.

   #### Choose from:

   * Import the configuration details from an XML metadata file. Select **Import Metadata**. Click **Select a File** and then select an XML metadata file on your file system. Click **Open**.

     The configuration values are populated based on the information in the metadata file.

     |   |                                                                                                                 |
     | - | --------------------------------------------------------------------------------------------------------------- |
     |   | If the metadata file does not specify all the configuration values, you must enter the missing values manually. |

   * Import the configuration details from a metadata URL. Select **Import from URL**. Enter the URL and then click **Import**.

     |   |                                       |
     | - | ------------------------------------- |
     |   | The URL must be a valid absolute URL. |

     The configuration values are populated based on the information from the URL.

   * Enter the configuration details manually. In the **ACS URLs** field, enter the Assertion Consumer Service (ACS) URLs. You must specify at least one URL, and the first URL in the list is used as the default.

     In the **Entity ID** field, enter the service provider entity ID used to look up the application. The Entity ID is a required property and is unique within the environment.

6. Click **Save**.

### Next steps

After the application is created, you can edit the application settings, configure application policies, and control application access. Learn more in [Editing an application - SAML](https://docs.pingidentity.com/pingone/applications/p1_edit_application_saml.html), [Applying authentication policies to an application](https://docs.pingidentity.com/pingone/applications/p1_apply_auth_policy_to_applications.html), and [Application access control](https://docs.pingidentity.com/pingone/applications/p1_application_access_control.html).

## Configuring a SAML application in PingOne for Enterprise

Configure a SAML application in PingOne for Enterprise.

### Before you begin

If you do not have the service provider's (SP) single sign-on (SSO) URL for the application, generally a SAML application that already exists in your organization, you must configure the necessary SAML settings for the application to add it to PingOne for Enterprise.

### Steps

1. In the PingOne for Enterprise dashboard, go to **Applications > My Applications > SAML**.

2. Click **Add Applications > New SAML Application**.

3. In the **Application Details** section, complete the following required fields:

   * **Application Name**

   * **Application Description**

   * **Category**

     ![Screen capture of the Application Details section and the corresponding fields. Required fields are defined by a small red asterisk to the right of the field. In addition to the required fields of Application Name, Application Description, and Category, there is a field for Graphics. The bottom of the screen capture includes text that the next step is Application Configuration along with the Cancel and Continue to Next Step buttons.](_images/bcs1600199959633.png)

4. Click **Continue to Next Step**.

5. In the **Application Configuration** section, provide the SAML configuration details for the application.

   1. From the **Signing Certificate** list, select the signing certification you want to use.

   2. In the **SAML Metadata**field, click **Download** to retrieve the SAML metadata for PingOne for Enterprise.

      This supplies the PingOne for Enterprise connection information to the application.

   3. In the **Protocol Version** field, select the SAML protocol version appropriate for your application.

   4. In the **Upload Metadata** section, click **Choose File** to upload the application's metadata file.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The **ACS URL** and **Entity ID** will then be supplied for you. If you don't upload the application metadata, you'll need to enter this information manually. When manually assigning an entity ID, the value must be unique unless you are assigning the entity ID value for a private managed application, an application that is supplied and configured by a PingOne for Enterprise administrator, rather than an SP.When applications are supplied by an SP, entity ID values are required to be unique to ensure against possible identifier conflicts with the IdP ID for the application. |

   5. In the **Application URL** field, enter an appropriate URL.

      This is required by some applications as the target URL. It is used in IdP-initiated SSO for a deep-linking purpose. The application URL is passed in the RelayState parameter by the IdP.

   6. In the **Single Logout Endpoint** field, enter the URL to which the service will send the SAML single logout (SLO) request using the **Single Logout Binding Type** that you select.

   7. In the **Single Logout Response Endpoint** field, enter the URL to which your service sends the SLO response.

   8. In the **Single Logout Binding Type** field, select the binding type, **Redirect** or **POST**, to use for SLO.

   9. In the **Primary Verification Certificate** field, click **Choose File** to upload the primary public verification certificate to use for verifying the SP signatures on SLO requests and responses.

   10. In the **Secondary Verification Certificate** field, click **Choose File** to upload the secondary verification certificate if available.

       The secondary verification certificate is used if the primary verification certificate fails to validate a signature.

   11. Select the **Encryption Assertion** checkbox.

       If selected, the assertions PingOne for Enterprise sent to the SP for a multiplexed application are encrypted. You can also use this option for your managed applications. Available for SAML 2.0 applications only.

       Selecting this option displays the information needed to encrypt the assertion:

       * **Encryption Certificate**: Upload the certificate to use to encrypt the assertions.

       * **Encryption Algorithm**: Choose the algorithm to use for encrypting the assertions. We recommend **AES\_256** (the default), but you can select **AES\_128** instead.

       * **Transport Algorithm**: The algorithm used for securely transporting the encryption key. Currently, **RSA-OAEP** is the only transport algorithm supported.

         |   |                                                                                                                                                                                                                                                           |
         | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
         |   |  If an encryption certificate is included in the metadata you upload, this option is automatically enabled. The entry for **Encryption Certificate** shows the name of the certificate and the entry for **Encryption Algorithm **is set to **AES\_256**. |

   12. In the **Signing** field, select either to sign the SAML assertion or to sign the SAML response.

       If the **Encryption Assertion** checkbox has been selected, choose to sign the response. This provides a significant increase in security.

   13. In the **Signing Algorithm** list, select the desired algorithm or use the default value.

   14. Select the **Force Re-authentication** checkbox.

       If selected, users having a current, active SSO session will be re-authenticated by the identity bridge to establish a connection to this application.

   15. Select the **Force MFA** checkbox.

       If selected, users are required to use multi-factor authentication (MFA) as defined by your authentication policy each policy each time they access the application. You'll need to have an authentication policy in place to use this setting. Learn more in [Create or update an authentication policy](https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_create_update_authentication_policy.html).

       ![Screen capture of the Application Configuration section and the corresponding fields.](_images/arx1600200202338.png)

6. Depending on your requirements, complete the remaining entry fields. Click **Continue to Next Step**.

   The remaining entry fields are optional, depending on your requirements.

7. In the **SSO Attribute Mapping** section, modify or add any attribute mappings as necessary for the application.

   In most cases, the default attribute mappings are sufficient. These mappings assign your identity repository attributes to the attributes provided by the SP for the application. For each application attribute, you can:

   * Click the **Required** checkbox to designate an attribute or attributes as required by the application.

   * In the **Application Attribute** field, enter an identity repository attribute.

   * In the **Identity Bridge Attribute or Literal Value** field, select an identity repository attribute from the list.

   * Select the **As Literal** checkbox, and then enter a literal value to assign.

   * Click **Advanced**, and then enter any additional attributes required by the application. You then have all of the choices above when configuring the attribute.

8. When finished modifying or adding any additional attributes, click **Continue to Next Step**.

9. In the **Group Access** section, make the new application available to your users by assigning the groups authorized to use the application.

   1. Click **Add** for each group you want to authorize to use the application.

      All members of the selected group or groups will be able to use the application. When the application supports user provisioning, user provisioning to this application is also enabled for members of the assigned groups.

10. Click **Continue to Next Step**.

11. In the **Review Setup** section, review the application connection information.

    Some of this information might be needed by the SP to complete the SSO configuration for the application. In particular, you can download the PingOne for Enterprise signing certificate or the PingOne for Enterprise SAML metadata, which has the certificate embedded.

12. **Optional:** To change any of the configuration settings, click **Edit**.

13. Click **Finish**.

### Result

The new SAML application is added to your **My Applications** list. Go to **Users → User Groups** to see the application you've added is now authorized for use by the selected group or groups.

---

---
title: Configuring adaptive authentication in PingFederate
description: This document explains the conceptual information behind network-based adaptive authentication. It also provides instructions for creating a new selector and configuring an authentication policy to enable adaptive authentication.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_config_adaptive_authn_pf
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_config_adaptive_authn_pf.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["workforce_use_cases:htg_config_adaptive_authn_pf_new_selector.adoc"]
section_ids:
  component: Component
  creating-a-new-selector: Creating a new selector
  before-you-begin: Before you begin
  steps: Steps
  configuring-the-authentication-policy: Configuring the authentication policy
  steps-2: Steps
  result: Result:
  next-steps: Next steps
---

# Configuring adaptive authentication in PingFederate

This document explains the conceptual information behind network-based adaptive authentication. It also provides instructions for creating a new selector and configuring an authentication policy to enable adaptive authentication.

Network-based adaptive authentication is useful when PingFederate must authenticate users differently based on their network location. A typical application of this use case is when users must authenticate differently, depending on whether they are accessing a service from the organization's internal network or from the internet. For example, an organization might want to use Kerberos to authenticate internal users to provide a seamless single sign-on (SSO) experience while presenting a sign-on page for external users.

Network-based adaptive authentication is achievable on all supported versions of PingFederate. The examples shown make use of PingFederate 10.1. All capabilities are offered out-of-the-box and no additional or custom components are required to implement this solution.

## Component

PingFederate 10.1

## Creating a new selector

Selectors and authentication sources can be conditionally chained together in paths to form policies.

### Before you begin

* PingFederate must determine if a user is inside your internal network. You must know CIDR network ranges that identify your internal network.

* Upon identifying the network location of your user, you must know how you intend to authenticate your user in each case.

  * Configure authentication adapters, such as the Kerberos adapter and the HTML form adapter, along with their dependencies (Kerberos Realms and password credential validators (PCVs), respectively).

* Define an authentication policy contract to allow the outcome of the authentication process to be mapped into your SAML connections or OAuth environment.

### Steps

1. In the PingFederate administrative console, go to **Authentication > Policies > Selectors**.

2. To create a new selector, click **Create New Instance**.

3. Configure the **Type** window.

   1. In the **Instance Name** field, enter an instance name.

   2. In the **Instance ID** field, enter the instance ID.

   3. In the **Type** list, select **CIDR Authentication Selector**.

   4. Click **Next**.

      ![Screen capture illustrating the Selector Type fields of Instance Name, Instance ID, and Type](_images/pae1601586970183.png)

4. Configure the **Authentication Selector** window.

   1. Click **Add a new row to 'Networks'**.

   2. In the **Network Range (CIDR notation)** field, enter the CIDR ranges that identify your internal network address ranges.

      ![Screen capture illustrating the Network Range fields on the Authentication Selector tab. After the Network Range fields is a hyperlink option to Add a new row to Networks, which allows you to add additional network address ranges.](_images/lfg1601587281892.png)

   3. To save your network, click **Update**.

   4. **Optional:** In the **Result Attribute Name** field, enter an attribute name.

   5. Click **Next**.

5. On the **Summary** window, click **Done**.

6. Click **Save**.

## Configuring the authentication policy

Authentication policies define how PingFederate authenticates users.

### Steps

1. In the PingFederate administrative console, go to **Authentication > Policies > Policies**.

2. To create a new policy, click **Add Policy**.

3. Configure the **Policy** window.

   ![Screen capture illustrating the Name, Description, and Policy fields on the Policy window in .](_images/wgx1601587629835.png)

   1. In the **Name** field, enter a name.

   2. In the **Description** field, enter a description.

   3. From the **Policy** list, go to **Selectors** and choose your previously created selector.

      #### Result:

      After choosing your selector, additional fields display that require you to identify which authentication adapters to use for internal and external users.

4. From the additional lists that display, configure the authentication adapters to be used for internal and external users.

   ![Screen capture illustrating the internal and external authentication adapter lists in .](_images/peo1601587892714.png)

5. Click **Done**.

6. Click **Save**.

7. To enable the network-based adaptive authentication policy, go to **Authentication > Policies > Policies** and select the **IDP Authentication Policies** checkbox.

   ![Screen capture illustrating the IDP Authentication Policies checkbox selected on the Authentication Policies window in .](_images/bvd1601587996122.png)

## Next steps

* Map the policy contract you used after completing the adaptive authentication within your SAML connections, OAuth persistent grants, or both.

* You can hierarchically organize the policy to appear earlier or later in the **Policy** list.

  |   |                                                                                                                                                                   |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To configure PingFederate with multiple authentication policies or specify the order in which they are presented, go to **Authentication > Policies > Policies**. |

---

---
title: Configuring an Active Directory datastore for PingFederate
description: In PingFederate, establish an Active Directory datastore connection for retrieving user attributes for outbound connections.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_config_ad_datastore_pf
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_config_ad_datastore_pf.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["workforce_use_cases:htg_config_ad_datastore_pf_config_ad_datastore.adoc"]
section_ids:
  component: Component
  processing-steps: Processing steps
  configuring-an-active-directory-datastore: Configuring an Active Directory datastore
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
---

# Configuring an Active Directory datastore for PingFederate

In PingFederate, establish an Active Directory datastore connection for retrieving user attributes for outbound connections.

## Component

PingFederate 10.1

## Processing steps

Almost every customer using PingFederate as an identity provider (IdP) has at least one connection to a datastore. A datastore connection allows PingFederate to retrieve user attributes for outbound connections. Active Directory is the most common data source used to connect to PingFederate.

![An illustration of a 3-step user-initiated single sign-on (SSO) when is the identity provider and has a datastore connection.](_images/lfl1606863776896.jpg)

1. The user initiates single sign-on (SSO) and activates PingFederate.

2. The user enters credentials in the htmlForm page. PingFederate query's the connected datastore for authentication.

3. A SAML assertion is sent to the service provider containing the select attributes for SSO.

## Configuring an Active Directory datastore

In PingFederate, configure a datastore connection to allow PingFederate, the identity provider (IdP), to retrieve user attributes for outbound connections.

### Before you begin

Your administrator account associated with Active Directory must be configured in the directory and have read permissions to the organizational unit where user attribute searches are done.

### About this task

This topic details specific tasks for configuring an Active Directory datastore connection. Learn more in [Datastores](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-100.pdf#page=125) (page 125) in the PingFederate Server documentation.

### Steps

1. From the PingFederate admin console, go to **System > Data Stores**. Click **Add a New Data Store**.

   #### Result:

   The **Data Store** window configuration opens.

2. On the **Data Store Type** tab:

   1. In the **Name** field, enter a name.

   2. From the **Type** list, select **Directory (LDAP)**.

   3. Click **Next**.

3. On the **LDAP Configuration** tab:

   1. In the **Hostname(s)** field, enter the hostname for the configuration. Click **Add**.

      This is the hostname of the domain controller.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The **Hostname(s)** field entry can rely on network naming to route to the closest domain controller. For example, `pingdemo.com` resolves to `dc1.pingdemo.com`.Alternatively, you can define domain controllers explicitly, separated by a space. For example, `dc1.pingdemo.com dc2.pingdemo.com`. This creates a failover to each domain controller. If it does not find the user in the first directory, it then queries the second and so on. |

   2. In the **User DN** field, enter the distinguished name (DN).

      This is used as the domain name of the service account used to query the directory.

   3. In the **Password** field, enter a password.

      This is the password of the service account.

   4. Select the **Use DNS SRV Record** checkbox.

      SRV records are not required for this configuration, but you can use them.

   5. Choose whether to enable the **Use LDAPS** checkbox.

      * Select the **Use LDAPS** checkbox.

        The configuration assumes port 636 if the LDAPS option is selected.

      * Clear the **Use LDAPS** checkbox.

        The configuration assumes port 389 if the LDAPS option is cleared.

        |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
        | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | If you are running your directory on another port, you must state this in the **Hostname(s)** field as shown in the image below, and have the Active Directory public certificate uploaded in your trusted keystore. In following image, notice port 1389 is specified in the **Hostname(s)** field.![A screen capture of the Data Store window and LDAP Configuration tab in . The LDAP Configuration tab contains multiple configuration fields for the user to edit. The following fields and their entries are displayed: Hostname(s) with cjmuir-r:1389 and selected as the default, another row of Hostname(s) with Email address, a cleared Use LDAPS checkbox, a cleared Use DNS SRV Record checkbox, the Load Type list with the option selected, a cleared Bind Anonymously checkbox, the User DN field with cn=Directory Manager entered, the Password field with a hidden entry, and cjmuir-r:1389 selected from the connection list, and the Test Connection button displayed.](_images/phy1606865459207.png) |

   6. Click **Next**.

   7. On the **Summary** tab, click **Save**.

      #### Result:

      The **Data Store** configuration window closes. You are directed back to the **Data Stores** window where you can manage all your datastore connections.

---

---
title: Connecting PingFederate to a Microsoft SQL JDBC datastore with Windows authentication
description: Create a Microsoft SQL server Java Database Connectivity (JDBC)-connected datastore in PingFederate and configure it for Windows authentication.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_connect_pf_to_ms_sql_jdbc_datastore
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_connect_pf_to_ms_sql_jdbc_datastore.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["workforce_use_cases:htg_connect_pf_to_ms_sql_jdbc_datastore_add_user.adoc", "workforce_use_cases:htg_connect_pf_to_ms_sql_jdbc_datastore_assign_logon_policy.adoc", "workforce_use_cases:htg_connect_pf_to_ms_sql_jdbc_datastore_edit_signon_tab.adoc", "workforce_use_cases:htg_connect_pf_to_ms_sql_jdbc_datastore_deploy_jdbc.adoc", "workforce_use_cases:htg_connect_pf_to_ms_sql_jdbc_datastore_connect_jdbc.adoc workforce_use_cases:htg_connect_pf_to_ms_sql_jdbc_datastore_testing.ado"]
section_ids:
  component: Component
  before-you-begin: Before you begin
  adding-a-new-user: Adding a new user
  about-this-task: About this task
  steps: Steps
  assigning-the-log-on-as-a-service-policy-to-the-new-user: Assigning the log on as a service policy to the new user
  about-this-task-2: About this task
  steps-2: Steps
  editing-the-sign-on-tab-for-the-pingfederate-service: Editing the sign-on tab for the PingFederate service
  about-this-task-3: About this task
  steps-3: Steps
  deploying-the-required-jdbc-driver-files-and-dlls: Deploying the required JDBC driver files and DLLs
  about-this-task-4: About this task
  steps-4: Steps
  creating-the-jdbc-datastore-connection-in-pingfederate: Creating the JDBC datastore connection in PingFederate
  steps-5: Steps
  testing-the-newly-created-external-datastore: Testing the newly created external datastore
  steps-6: Steps
  result: Result:
---

# Connecting PingFederate to a Microsoft SQL JDBC datastore with Windows authentication

Create a Microsoft SQL server Java Database Connectivity (JDBC)-connected datastore in PingFederate and configure it for Windows authentication.

If your organization primarily uses a Microsoft Windows platform, you can have your PingFederate nodes on Windows servers, and you can use Microsoft SQL Server for your databases. One example use case for this type of datastore is storing OAuth grants in a clustered environment.

High availability requirements for this database should follow your organization's procedures and are outside the scope of this document. Any database maintenance tasks are also not addressed in this document.

## Component

PingFederate 9.3 or later

## Before you begin

You must have:

* An SQL server on the network, accessible from the PingFederate nodes on its assigned port

  |   |                                                                                                                                    |
  | - | ---------------------------------------------------------------------------------------------------------------------------------- |
  |   | Port 1433 is the default port for SQL server. You can test connectivity to the `server:port` with the telnet command line utility. |

* Access to a database on the server with the correct tables

  Work with the database administrator to determine an appropriate name for your database, such as "PingFederate".

  |   |                                                                                                                                                                                                                      |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | For storing OAuth grants, you can find the table creation scripts (access-grant-sqlserver.sql and access-grant-attribute-sqlserver.sql) in `<pf_install>/pingfederate/server/default/conf/access-grant/sql-scripts`. |

* A user account in the Active Directory (AD) domain you can use as a service account

  It does not need any special domain privileges, but it receives local permissions on your PingFederate nodes.

  Work with your database administrators to ensure the user account in the AD has permissions to access and write to the database.

## Adding a new user

### About this task

Perform these steps on each PingFederate node.

### Steps

1. On your Windows machine, open the folder where PingFederate is installed.

   ![Screen capture illustrating the version folder on a Windows machine.](_images/xyo1609355945861.png)

2. Right-click the folder and select **Properties**.

3. Click the **Security** tab.

4. To add a user, click **Edit** and **Add**.

5. Add the user account and click **OK**.

   ![Screen capture illustrating the window to add a user account. There are three fields: Select this object type, From this location, and Enter the object names to select.](_images/xgz1609356052419.png)

6. From the user account **Permissions** section, select the **Modify** checkbox.

   ![Screen capture illustrating the Modify checkbox being selected on the permissions window.](_images/sjy1609356126122.png)

7. To save your changes, click **Apply**.

## Assigning the log on as a service policy to the new user

### About this task

Perform these steps on each PingFederate node.

### Steps

1. On your Windows machine, open the **Local Security Policy** menu. You can search for "local security policy" from the Windows Start menu.

2. From the **Local Security Policy** window, go to **Local Policies > User Rights Assignment > Log on as a service**.

   ![Screen capture illustrating the Local Security Policy window with the Log on as a service policy highlighted.](_images/bwc1609356340621.png)

3. In the **Log on as a service Properties** window, click **Add User or Group…​**.

   ![Screen capture illustrating the Log on as a service Properties window.](_images/cwy1609356491274.png)

4. Add the user information as needed.

5. Click **Apply**, and then click **OK**.

## Editing the sign-on tab for the PingFederate service

### About this task

Perform these steps on each PingFederate node.

### Steps

1. On your Windows machine, open the **Services** menu.

2. Right-click the PingFederate service that is running on your machine and select **Properties**.

   ![Screen capture illustrating the Services window showing the right-click menu.](_images/nri1609356752728.png)

3. On the **Log On** tab, click **This account**.

   ![Screen capture illustrating the engine properties window open to the Log On tab.](_images/rul1609356859559.png)

4. In the **This account** field, enter the entire UPN name of the account, such as `svc.pingfed@<your-domain>`.

5. Enter a password for the account.

6. To save your changes, click **Apply**, and then click **OK**.

7. To restart the service, right-click the PingFederate service and select **Restart**.

   ![Screen capture illustrating the right-click menu for a local engine on the Windows Services menu.](_images/yug1609356938896.png)

## Deploying the required JDBC driver files and DLLs

### About this task

Perform these steps on each PingFederate node.

### Steps

1. Go to .microsoft.com/en-us/sql/connect/jdbc/release-notes-for-the-jdbc-driver?view=sql-server-ver15//\[Microsoft release notes] and download the correct `.zip` file for your Java version.

   Package 6.4 is known to work properly.

2. Extract the files and find the `.jar` file that corresponds to your Java version.

3. Place the `.jar` file in `<pf_install>/pingfederate/server/default/lib`

4. In the `auth` folder of your JDBC driver download folder, find the appropriate folder for your Java virtual machine (JVM) version (x32 or x64-based), and copy the DLL file to your `/windows/system32` folder.

5. Restart the PingFederate service.

## Creating the JDBC datastore connection in PingFederate

### Steps

1. From the PingFederate administrative console, go to **System > Data Stores** and click **Add New Data Store**.

2. On the **Data Store Type** tab, in the **Name** field, enter a name.

3. In the **Type** list, select **Database (JDBC)**. Click **Next**.

4. On the **Database Config** tab, in the **JDBC URL** field enter `jdbc:sqlserver://<databaseservername>;<databaseName=databasename>;integratedSecurity=true`.

5. Click **Add**.

   |   |                                                                                                                                                                                                                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Use the fully qualified domain name for your server. Port `1433` is the default port for SQL server. If you are using port `1433`, then you can omit it from the JDBC URL. For any non-standard ports, specify them in the URL.`integratedSecurity=true` makes the connection use Windows authentication. Without that, it attempts SQL authentication. |

6. In the **Driver Class** field, enter `com.microsoft.sqlserver.jdbc.SQLServerDriver`.

7. Complete the **Username** and **Password** fields with the same service account credentials from step 1.

8. In the **Validate Connection SQL** field, enter `SELECT getdate()`.

   |   |                                                                                         |
   | - | --------------------------------------------------------------------------------------- |
   |   | `SELECT getdate()` is used to re-establish the JDBC connection if it gets disconnected. |

9. Click **Next**, and then click **Save**.

10. Replicate the cluster configuration.

## Testing the newly created external datastore

### Steps

1. Follow the steps in [Configure external databases for grant storage](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_external_database_for_grant_storage.html).

2. Issue a grant in PingFederate.

   |   |                                                                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you do not have an OAuth client application readily available, you can use the OAuth Playground authorization code flow to obtain a code and exchange it for an access and refresh token. |

3. Work with the database administrator (if necessary) to view the tables in the database that were created by the script.

   #### Result:

   You should see an entry for the newly issued grant.

---

---
title: Connecting PingFederate with Yahoo through OIDC
description: Learn how to connect PingFederate with your Yahoo developer account using OpenID Connect (OIDC).
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_connect_pf_with_yahoo_through_oidc
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_connect_pf_with_yahoo_through_oidc.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["workforce_use_cases:htg_connect_pf_with_yahoo_through_oidc_oidc_app_yahoo.adoc", "workforce_use_cases:htg_connect_pf_with_yahoo_through_oidc_oidc_idp_connection.adoc", "workforce_use_cases:htg_connect_pf_with_yahoo_through_oidc_local_identity_profile.adoc", "workforce_use_cases:htg_connect_pf_with_yahoo_through_oidc_html_idp_adapter.adoc", "workforce_use_cases:htg_connect_pf_with_yahoo_through_oidc_policy_contract_lip.adoc", "workforce_use_cases:htg_connect_pf_with_yahoo_through_oidc_testing.adoc"]
section_ids:
  component: Component
  creating-an-oidc-app-in-your-yahoo-developer-account: Creating an OIDC app in your Yahoo developer account
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  creating-an-oidc-type-idp-connection: Creating an OIDC type IdP connection
  steps-2: Steps
  creating-a-local-identity-profile: Creating a local identity profile
  steps-3: Steps
  creating-an-html-form-idp-adapter: Creating an HTML form IdP adapter
  about-this-task-2: About this task
  steps-4: Steps
  creating-a-policy-to-fulfill-the-policy-contract-chosen-in-the-lip: Creating a policy to fulfill the policy contract chosen in the LIP
  steps-5: Steps
  testing-the-configuration: Testing the configuration
  steps-6: Steps
  result: Result:
  result-2: Result
---

# Connecting PingFederate with Yahoo through OIDC

Learn how to connect PingFederate with your Yahoo developer account using OpenID Connect (OIDC).

|   |                                                        |
| - | ------------------------------------------------------ |
|   | Yahoo no longer supports OpenID2 and migrated to OIDC. |

## Component

PingFederate 10.3

## Creating an OIDC app in your Yahoo developer account

### Before you begin

* Go to [developer.yahoo.com](https://developer.yahoo.com/) and create a developer account.

### About this task

In your Yahoo developer account, create an OIDC app and obtain the **Client ID** and **Client Secret**.

### Steps

1. Sign on to your Yahoo developer account and go to **Apps > Create an App**.

2. [Create an application with OpenID Connect permissions](https://developer.yahoo.com/oauth2/guide/openid_connect/getting_started.html).

3. Copy the **Client ID** and **Client Secret**.

   ![Screen capture of the Yahoo developer My Apps window showing the Client ID and Client Secret.](_images/qcw1620233205439.png)

## Creating an OIDC type IdP connection

### Steps

1. Sign on to PingFederate and go to **Authentication > Authorization > IdP Connections**. Click **Create Connection**.

2. On the **Connection Type** tab, select the **Browser SSO** checkbox, and in the **Protocol** list, select **SAML 2.0**. Click **Next**.

   ![Screen capture of the Connection Type tab with the Browser SSO Profiles checkbox selected and the SAML 2.0 option checked from the Protocol list.](_images/trs1624388770282.png)

3. On the **Connection Options** tab, select the **Browser SSO** checkbox. Click **Next**.

4. On the **General Info** tab, in the **Issuer** field, enter `https://api.login.yahoo.com`.

5. In the **Client ID** and **Client Secret** fields, enter the values copied earlier from your Yahoo OIDC app.

6. Click **Load Metadata**. Click **Next**.

   ![Screen capture of the General Info tab, showing the completed Issuer, Client ID, and Client Secret fields.](_images/khd1624388963952.png)

7. On the **Extended Properties** tab, click **Next**.

8. On the **Browser SSO** tab, click **Configure Browser SSO**.

9. On the **User Session Creation** tab, click **Configure User-Session Creation**.

10. On the **Identity Mapping** tab, select **Account Mapping**. Click **Next**.

11. On the **Attribute Contract** tab, leave the default values selected. Click **Next**.

    ![Screen capture of the Attribute Contract tab, showing the default values listed.](_images/zhm1624389361302.png)

12. On the **Target Session Mapping** tab, click **Map New Adapter Instance**.

13. On the **Adapter Instance** tab, in the **Adapter Instance** list, select **Open Token** adapter. Click **Next**.

    ![Screen capture of the Adapter Instance tab, showing the Adapter Instance list expanded.](_images/jad1624389568099.png)

14. On the **Attribute Data Store** tab, leave the default values selected. Click **Next**.

    ![Screen capture of the Adapter Data Store tab showing the default values listed.](_images/qkw1624389700267.png)

15. On the **Adapter Contract Fulfillment** tab, map the values as follows. Click **Next**.

    | Attribute     | Source              | Value            |
    | ------------- | ------------------- | ---------------- |
    | **givenName** | **Provider Claims** | **given\_name**  |
    | **mail**      | **Provider Claims** | **email**        |
    | **sn**        | **Provider Claims** | **family\_name** |
    | **subject**   | **Provider Claims** | **sub**          |

    ![Screen capture of the Adapter Contract Fulfillment tab showing the specified settings.](_images/bwa1624389840839.png)

16. On the **Issuance Criteria** tab, click **Next**.

17. On the **Summary** tab, review your entries and click **Done**.

18. On the **User Session Creation** tab, click **Next**.

19. On the **Protocol Settings** tab, click **Configure Protocol Settings**.

20. On the **OpenID Provider Info** tab, review the information and click **Next**.

    ![Screen capture of the OpenID Provider Info tab.](_images/kgu1624390089670.png)

21. On the **Overrides** tab, enter a **Default Target URL**. Click **Next**.

22. On the **Summary** tab, review your entries and click **Done**.

23. On the **Protocol Settings** tab, click **Next**.

24. On the **Summary** tab, review your entries and click **Done**.

25. On the **Activation and Summary** tab, click the toggle to activate the connection. Click **Save**.

## Creating a local identity profile

### Steps

1. Go to **Authentication > Policies > Local Identity Profiles** and click **Create New Profile**.

2. On the **Profile Info** tab, choose an existing policy contract or create a new one. Click **Next**.

   ![Screen capture of the Profile Info tab.](_images/msl1624390397788.png)

3. On the **Authentication Sources** tab, in the empty field next to the **Add** button, enter`Yahoo`. Click **Add**.

   ![Screen capture of the Authentication Sources tab showing Yahoo added as a source.](_images/zdn1624390527419.png)

4. Click **Save**.

## Creating an HTML form IdP adapter

### About this task

Create an HTML form IdP adapter to include the newly created LIP.

### Steps

1. Go to **Authentication > Integration > IdP Adapters** and click **Create New Instance**.

2. On the **Type** tab, enter a **Instance Name** and **Instance ID**, and in the **Type** list, select **HTML From IdP Adapter**. Click **Next**.

   ![Screen capture of the Type ta showing the completed Instance Name, instance ID, Type, Class Name and Parent Instance fields.](_images/yuh1624390674673.png)

3. On the **IdP Adapter** tab, select the **Local Identity Profile** checkbox and select the newly-created LIP in the list. Click **Next**.

   ![Screen capture of the IdP Adapter tab showing the Local Identity Profile checkbox selected and the LIP selected from the list.](_images/bsx1624390843981.png)

4. On the **Extended Contract** tab, add all desired attributes. Click **Next**.

   1. To add an attribute, enter the name in the empty field and click **Add**.

      ![Screen capture of the Extended Contract tab showing attributes listed.](_images/tme1624391014636.png)

5. On the **Adapter Attributes tab**, in the **username** row, select the **Pseudonym** checkbox. Click **Next**.

   ![Screen capture of the Adapter Attributes tab showing the username Pseudonym checkbox selected.](_images/lgd1624391164859.png)

6. On the **Adapter Contract Fulfillment** tab, configure the contract as follows. Click **Next**.

   | Attribute             | Value                                                                                                                                                                                  |
   | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **IsPhoneAvailable**  | `#this.get("telephoneNumber")== null? false:#this.get("telephoneNumber").toString().equalsIgnoreCase("")?false:true`                                                                   |
   | **telephoneNumber**   | `telephoneNumber`                                                                                                                                                                      |
   | **mail**              | `mail`                                                                                                                                                                                 |
   | **policy.action**     | `policy.action`                                                                                                                                                                        |
   | **givenName**         | `givenName`                                                                                                                                                                            |
   | **objectGUID**        | `objectGUID`                                                                                                                                                                           |
   | **memberOf**          | `memberOf`                                                                                                                                                                             |
   | **pi.template**       | `{ "name": "strong_authentication"."variables": { "logourl"."https//www.logosurfer.com/wp-content/uploads/2018/03/kohls-log_0.png"."currency": "USD"."recipient": "Charlie Parker" }}` |
   | **sn**                | `sn`                                                                                                                                                                                   |
   | **userPrincipalName** | `userPrincipalName`                                                                                                                                                                    |
   | **subjectDN**         | `subjectDN`                                                                                                                                                                            |
   | **username**          | `username`                                                                                                                                                                             |

7. On the **Summary** tab, review your entries. Click **Save**.

## Creating a policy to fulfill the policy contract chosen in the LIP

### Steps

1. Select the HTML form adapter that you created earlier and click **Rules**.

2. Add **Yahoo** as a rule:

   1. From the **Attribute Name** list, select **policy.action**.

   2. From the **Condition** list, select **equal to**.

   3. In the **Value** field, enter `Yahoo`.

   4. In the **Result** field, enter `Yahoo`.

   5. Click **Done**.

      The rest of the values are optional.

3. Under the **Yahoo** branch, in the **Policy** list, select the IdP connection that you created earlier.

4. In the **Success** list, select the policy contract that you used in the LIP. Click **Contract Mapping**.

   ![Screen capture of the Yahoo branch.](_images/mej1624391659649.png)

5. On the **Contact Fulfillment** tab, configure the following attributes.

   | Attribute            | Value         |
   | -------------------- | ------------- |
   | **UPN**              | `name`        |
   | **Email**            | `email`       |
   | **Group Membership** | `grp`         |
   | **Object GUID**      | `objectguid`  |
   | **subject**          | `sub`         |
   | **First Name**       | `given_name`  |
   | **DN**               | `dn`          |
   | **Last Name**        | `family_name` |

6. On the **Summary** tab, click **Done**.

## Testing the configuration

### Steps

1. Launch an application that satisfies the newly-created policy.

   #### Result:

   A sign-on window opens.

   ![Screen capture of the Sign on window.](_images/ybn1624392025856.png)

2. In the **Sign On With** section, click **Yahoo** to go to the Yahoo sign-on page.

   ![Screen capture of the Yahoo sign on page](_images/kjq1624392175053.png)

3. Enter your password and click **Next**.

### Result

After signing on, you are taken to the end application.

---

---
title: Delegating all authentication to an external IdP
description: PingOne provides an authentication policy step that allows you to make an external identity provider (IdP) part of a PingOne authentication policy or delegate all authentication to that external IdP.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_delegate_authn_to_external_idp
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_delegate_authn_to_external_idp.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["workforce_use_cases:htg_delegate_authn_to_external_idp_config_idp.adoc", "workforce_use_cases:htg_delegate_authn_to_external_idp_create_authn_policy.adoc"]
section_ids:
  before-you-begin: Before you begin
  configuring-an-external-idp: Configuring an external IdP
  before-you-begin-2: Before you begin
  steps: Steps
  choose-from: Choose from:
  creating-an-external-idp-authentication-policy: Creating an external IdP authentication policy
  steps-2: Steps
  next-steps: Next steps
---

# Delegating all authentication to an external IdP

PingOne provides an authentication policy step that allows you to make an external identity provider (IdP) part of a PingOne authentication policy or delegate all authentication to that external IdP.

## Before you begin

You must have:

* An external IdP defined in your PingOne tenant

* An authentication policy that specifies that external IdP as the only step

## Configuring an external IdP

### Before you begin

* If you want to use OpenID Connect (OIDC), you must configure an OIDC client in PingFederate.

* If you want to use SAML, you must configure a SAML service provider (SP) in PingFederate.

### Steps

1. In your PingOne tenant, go to **Integrations > External IdPs** and click **Add Provider**.

2. Go to **Add a Social or Custom Identity Provider > Select an Identity Provider from the Options Below > Custom** and click either:

   #### Choose from:

   * **OpenID Connect**

   * **SAML**

     ![Screen capture of the Add a Social or Custom Identity Provider window showing OpenID Connect and SAML options near the bottom.](_images/xld1621366507424.png)

3. If you clicked **OpenID Connect**:

   1. In the **Create Profile**window, in the **Name** field, specify a name for the IdP (used only in the PingOne console) and click **Continue**.

      ![igv1621366618264](_images/igv1621366618264.png)

   2. In the **Connection Details** section, in the **Client ID** and **Client Secret** fields, enter the client ID and client secret from the external IdP.

      |   |                                   |
      | - | --------------------------------- |
      |   | This must be an auth-code client. |

      ![Screen capture of the Configure OpenID Connect Connection window showing the required Client ID and Client Secret fields.](_images/aqn1621366697208.png)

   3. In the **Discovery Details** section, you can provide the OpenID well-known endpoint in the **Discovery Document** section to pre-populate all values.

      If the OpenID well-known endpoint isn't available, you must manually enter all the required values.

      ![Screen capture of the Discovery Details sections showing the required Authorization Endpoint, Token Endpoint, JWKS Endpoint and Issuer fields.](_images/gob1621366774192.png)

   4. Click **Save and Continue**.

   5. In the **Map Attributes** window, map incoming values as needed, and then click **Save and Finish**.

      ![Screen capture of the Map Attributes window showing the PingOne User Profile Attribute, OIDC Attribute and Update Condition fields.](_images/lqh1621366872979.png)

4. If you clicked **SAML**:

   1. In the **Create Profile** window, in the **Name** field, specify a name for the IdP (used only in the PingFederate console) and click **Continue**.

   2. In the **Configure PingOne Connection** section, choose the signing certificate for SP-initiated SAML authentication requests and click **Continue**.

      ![Screen capture of the Configure PingOne Connection window.](_images/tuz1621366926726.png)

   3. In the **Configure IDP Connection** window, import data or provide the values, and then click**Save and Continue**.

   4. In the **Map Attributes** window, map incoming values as needed, and then click **Save and Finish**.

      ![Screen capture of the Map Attributes window showing the PingOne User Profile Attribute, OIDC Attribute and Update Condition fields.](_images/grz1621367035594.png)

5. **Optional:** To support just-in-time (JIT) creation, edit the newly created external IdP:

   If a user who doesn't exist in PingOne is redirected from the external IdP, PingOne can perform a JIT creation of an account for that user in PingOne.

   1. Click **Registration**.

   2. In the **Population** list, select the population into which new users should be JIT provisioned.

   3. Click **Save**.

6. Enable the external IdP you created.

## Creating an external IdP authentication policy

### Steps

1. In your PingOne tenant, go to **Authentication > Authentication** and click **Add Policy**.

   ![Screen capture of the Policies window with the Add Policy option in the upper right corner.](_images/bkh1621367287358.png)

2. In the **Policy Name** field, enter a unique policy name.

3. In the **Step Type** list, select **External Identity Provider**.

   ![Screen capture of the expanded Step Type list showing External Identity Provider highlighted.](_images/rnt1621367352829.png)

4. In the **External Identity Provider** list, select the external IdP you want to delegate to.

   |   |                                                                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Disabled external IdPs are marked as such.![Screen capture of the expanded External Identity Provider list showing PF and PFIDP (Disabled) as options.](_images/bfs1621367395681.png) |

5. **Optional:** In the **Required Authentication Level** field, specify an authentication context to request from the IdP.

   For example, if you were using PingFederate you could use a selector on the incoming context to determine authentication policy flows.

   ![Screen capture of the Identity Provider Settings section showing the optional Required Authentication Level field.](_images/mug1621367434316.png)

6. Click **Save and Continue**.

### Next steps

Depending on how you want to use it, you can configure this policy as the default or assign it to specific applications. After calling an app that has this policy assigned, users are automatically sent to the external IdP for authentication.

After a successful return from the external IdP:

* If the user doesn't exist in PingOne, the user is created.

* If user does exist in PingOne, the user is prompted for linking and then passed to their respective application.

---

---
title: Enabling SLO for a PingAccess-protected application using PingFederate
description: Learn how to require a sign off of a PingAccess-protected application with PingFederate acting as a token provider.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_enable_slo_for_pa_protected_app_using_pf
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_enable_slo_for_pa_protected_app_using_pf.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["workforce_use_cases:htg_enable_slo_for_pa_protected_app_using_pf_pa_logout_endpoint.adoc", "workforce_use_cases:htg_enable_slo_for_pa_protected_app_using_pf_pa_partial_logout.adoc", "workforce_use_cases:htg_enable_slo_for_pa_protected_app_using_pf_global_slo.adoc", "workforce_use_cases:htg_enable_slo_for_pa_protected_app_using_pf_pf_pa_logout.adoc"]
section_ids:
  components: Components
  pingaccess-logout-endpoint: PingAccess Logout endpoint
  configuring-pingaccess-partial-logout: Configuring PingAccess partial logout
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  configuring-global-single-logout: Configuring global single logout
  before-you-begin-2: Before you begin
  about-this-task: About this task
  steps-2: Steps
  result-2: Result
  configuring-pingfederate-for-pingaccess-single-logout: Configuring PingFederate for PingAccess single logout
  about-this-task-2: About this task
  steps-3: Steps
  result-3: Result:
  result-4: Result
---

# Enabling SLO for a PingAccess-protected application using PingFederate

Learn how to require a sign off of a PingAccess-protected application with PingFederate acting as a token provider.

There are multiple scenarios for signing off a user. As an administrator, you might require one or more sign-off flows because requirements for each application can differ.

This guide provides information for the following use cases:

* Global single logout (SLO)

* Per application or partial logout

Each PingAccess sign-off flow is user-initiated, not system-initiated. PingAccess checks if a session is revoked and, if the existing session is found to be revoked, redirects to the web. PingAccess doesn't revoke sessions. It checks the revocation status by sending a GET request to that endpoint.

Learn more in [Authorization endpoint](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=1069) (page 1,069) and [Session Revocation API endpoint](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=1156) (page 1,156).

## Components

* PingAccess 6.3

* PingFederate 10.3

## PingAccess Logout endpoint

PingAccess responds differently depending on whether the sign off is successful or unsuccessful.

* For successful sign offs:

  1. PingAccess responds to the `/pa/oidc/logout.png` request with `Set-Cookie: PA.ACE_ws=;`.

  2. The `/pa/oidc/logout.png` endpoint clears the ID token from the browser containing the PingAccess cookie.

     Unless you select **Use single-logout** (SLO) for the token provider, the `/pa/oidc/logout.png` endpoint clears the cookie only from the requested host/domain, and the cookie might still exist in requests bound for other hosts/domains.

     |   |                                                                                                                                                                                                            |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you select the **Use Single-Logout** option when configuring the token provider, the `/pa/oidc/logout.png` endpoint also sends a logout request to the token provider, which completes a full SLO flow. |

* For unsuccessful sign offs:

  1. PingAccess responds to the same `/pa/oidc/logout.png` request without clearing the `PA.ACE_ws;` cookie.

  2. The user is directed back to the PingAccess-protected application page.

  3. If the application reads and finds the `PA.ACE_ws;` cookie present, it doesn't redirect to PingFederate for authentication.

PingAccess can only clear the sessions for which the corresponding cookie was sent in the request to the `/pa/oidc/logout` resource. If PingFederate or the authentication authority can maintain different sessions for each set of apps, you can use SLO to sign off of all sessions in each set. To initiate the end sessions sign off in specific domains, call the `/pa/oidc/logout.png` endpoint used by SLO.

Learn more in [Server-side session management configuration](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=112) (page 112) in the PingAccess solutions documentation.

## Configuring PingAccess partial logout

Learn how to require termination of a user's session per application or by a partial logout protected in the PingAccess administrative console.

### Before you begin

You must:

* Execute the identity provider (IdP) adapter's logout endpoint. Learn more in [HTML Form Adapter Logout Configuration](https://support.pingidentity.com/s/article/Html-Form-Adapter-Logout-Configuration).

* Have experience with PingFederate and PingAccess.

### Steps

1. In the PingAccess administrative console:

   1. Go to **Settings > Token Provider > Runtime > Show Advanced Settings**.

   2. Clear the **Use Single-Logout** checkbox.

      ![Screen capture of the PingAccess Administrative console. System is selected from the Settings menu. There are Advanced settings for Back Channel Servers, Back Channel Secure, Back Channel Base Path, Skip Hostname Verification, Expected Hostname, Use Proxy, Use Single-Logout. The Use Single Logout checkbox is cleared.](_images/mbq1628025151820.jpg)

   3. Click **Save**.

2. In the PingFederate administrative console:

   1. Go to **Authentication > Integration > IdP Adapters > Manage Adapter Instances** and then select the relevant IdP adapter instance.

      #### Result:

      The **Create Adapter Instance** page opens.

   2. To show the logout related fields, go to the **IdP Adapter > Show Advanced Fields**.

   3. In the **Logout Path** field, enter the path with the PingAccess endpoint.

      You can enter any valid path string.

      |   |                                                                                                                                                                                                                                |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | This value must start with a "/" character. For example, if you enter `/mylogoutpath`, then the logout path is `/ext/mylogoutpath`. Don't use a path already used by another adapter, such as `/ext/pickup` or `/ext/dropoff`. |

      |   |                                                                                          |
      | - | ---------------------------------------------------------------------------------------- |
      |   | Use an alphanumeric string to minimize the risk of using an invalid value in this field. |

   4. In the **Logout Redirect** field, enter the URL that PingFederate uses to redirect the user after sign off.

      The default **Logout Redirect** value is `https://<pingaccessServer>:3000/pa/oidc/logout`.

   5. For PingFederate to display a page using a template, in the **Logout Template** field, enter the name of the template file.

   6. In the **Logout Path** field, enter a path with the PingAccess endpoint.

      The default **Logout Path** value is `<pf_install>/server/default/conf/template/idp.logout.success.page.template.html`.

      ![Screen capture of the administrative console in the Create Adapter Instance configuration page. In the middle of the list, the Logout Path and Logout Redirect fields are highlighted in green with values of /logout and https://pa.pinglab.com:3000/pa/oidc/logout, respectively.](_images/fog1628025687784.jpg)

   7. Click **Done**.

## Configuring global single logout

Learn how to revoke global sessions with single logout (SLO) in the PingFederate administrative console.

### Before you begin

Make sure the identity provider (IdP) adapters have their **Session State** set to **Globally** in PingFederate.

### About this task

To revoke global sessions with SLO:

### Steps

1. In the PingFederate administrative console, go to **Applications > Integrations > Default URLs > SP Default URLs**.

2. To allow `TargetResource` as a redirect URI in PingFederate, enter and edit the URL in the **Provide The Default URL You Would Like to Send The User to When Single Logout (SLO) Has Succeeded** field.

   The `TargetResource` is the landing page PingFederate directs the user to after logout, for example, `http://pf01.pinglab.com:9331/idp/startSLO.ping?TargetResource=://pa01.pinglab.com:3000/PingAccessQuickstart/`.

   |   |                                                                       |
   | - | --------------------------------------------------------------------- |
   |   | The `TargetResource` must be an allowed redirect URI in PingFederate. |

3. Click **Save**.

### Result

PingFederate automatically redirects to the PingAccess logout endpoint `pa/oidc/logout`.

## Configuring PingFederate for PingAccess single logout

Learn how to configure PingFederate for user-initiated PingAccess single logout (SLO) so that PingFederate knows to add the Subresource Integrities (SRIs) to the revocation list if SLO is initiated.

### About this task

There are two ways to implement Server-Side Session Management:

* PingAccess can reject a PingAccess cookie associated with a PingFederate session that has been invalidated as a result of an end-user-driven logout.

* The end-user can initiate a logout from all PingAccess issued web sessions using a centralized sign off.

PingAccess can only clear the sessions for which the corresponding cookie is sent in the request to the `/pa/oidc/logout` resource. If PingFederate, as the authentication authority, can maintain different sessions for each set of apps, you can use SLO to sign off of all sessions in each set. Call the `/pa/oidc/logout.png` endpoint used by SLO to initiate the end sessions sign off in specific domains.

SLO is done by redirecting to the standard SLO location, which is configured in the `run.props` file. PingAccess does not revoke the user's session. The user is directed to the `pa.oidc.logout.redirectURI` URI when they sign off using OpenID Connect and the PingFederate SLO endpoint.

Learn more in [Configuration file reference](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=171) (page 171) and [OpenID Connect endpoints](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=158) (page 158).

### Steps

1. In the PingFederate administrative console, go to **Applications > OAuth > Clients > Client Management**, and select the relevant client.

   #### Result:

   The **Client** page opens.

2. To enable PingFederate to add the SRIs to the revocation list if SLO is initiated, in the **OpenID Connect** section, select the **PingAccess Logout Capable** checkbox.

3. Click **Save**.

### Result

PingFederate uses the `logout.png` endpoint `/pa/oidc/logout.png` to initiate a sign off from PingAccess in conjunction with the SLO functionality. This endpoint terminates the PingAccess tokens across domains.

Learn more in [Configuring PingFederate for user-initiated single logout](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=113) (page 113).

---

---
title: Integrating Pulse Connect Secure with PingFederate
description: Learn how to integrate Pulse Connect Secure with PingFederate for single sign-on (SSO).
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_integrate_pulse_connect_secure_with_pf
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_integrate_pulse_connect_secure_with_pf.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["workforce_use_cases:htg_integrate_pulse_connect_secure_with_pf_metadata.adoc", "workforce_use_cases:htg_integrate_pulse_connect_secure_with_pf_signing_cert.adoc", "workforce_use_cases:htg_integrate_pulse_connect_secure_with_pf_saml_pf.adoc", "workforce_use_cases:htg_integrate_pulse_connect_secure_with_pf_saml_pcs.adoc"]
section_ids:
  component: Component
  before-you-begin: Before you begin
  exporting-saml-metadata-from-pingfederate: Exporting SAML metadata from PingFederate
  steps: Steps
  exporting-signing-cert-from-pingfed: Exporting the signing certificate from PingFederate
  steps-2: Steps
  configuring-saml-integration-with-pingfederate-in-pulse-connect-secure: Configuring SAML integration with PingFederate in Pulse Connect Secure
  steps-3: Steps
  configuring-saml-integration-with-pulse-connect-secure-in-pingfederate: Configuring SAML integration with Pulse Connect Secure in PingFederate
  steps-4: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  result-4: Result:
  result-5: Result:
  result-6: Result:
  result-7: Result:
  result-8: Result:
  result-9: Result:
  result-10: Result:
---

# Integrating Pulse Connect Secure with PingFederate

Learn how to integrate Pulse Connect Secure with PingFederate for single sign-on (SSO).

## Component

PingFederate 10.3

## Before you begin

* Configure a PingFederate data store. Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_datastores.html).

* Configure a PingFederate [Password Credential Validator](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_passwordcredentialvalidatortasklet_passwordcredentialvalidatormgmtstate.html).

* Configure a PingFederate [HTML Form Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_html_form_adapt.html).

* Configure a Pulse Connect Secure authentication realm for your users.

* Configure a Pulse Connect Secure sign-on policy for your users.

## Exporting SAML metadata from PingFederate

### Steps

1. Sign on to the PingFederate administrative console and go to **System → Protocol Metadata → Metadata Export**.

2. On the **Metadata Role** tab, select **I am the Identity Provider (IdP)**, and then click **Next**.

   ![A screen capture of the Metadata Role tab in the administrative console.](../_images/zbi1593474042547.png)

3. On the **Metadata Mode** tab, select **Select Information to Include in Metadata Manually**, and then click **Next**.

   ![A screen capture of the Metadata Mode tab in the administrative console.](../_images/pvo1593474233350.png)

4. On the **Protocol** tab, click **Next** until you reach the **Signing Key** tab, accepting the default values.

5. On the **Signing Key** tab, select an available signing key from the **Digital Signature Keys/Certs** list, and then click **Next**. If none are available, click **Manage Certificates** to create a signing key, and then follow the on-screen instructions.

   |   |                                                                                         |
   | - | --------------------------------------------------------------------------------------- |
   |   | Although you can use a self-signed certificate, a CA-signed certificate is recommended. |

   ![A screen capture of Signing Key tab in the administrative console.](../_images/sga1593474593063.png)

6. Click **Next** until you reach the **Export & Summary** tab, accepting the default values on the **Metadata Signing** and **XML Encryption Certificate** tabs.

7. On the **Export & Summary** tab, click **Export** and save the `metadata.xml` file. You will upload this file to Palo Alto Networks NGFW in the next step.

   ![A screen capture of the Export & Summary tab in the administrative console.](../_images/lfe1593474764679.png)

## Exporting the signing certificate from PingFederate

### Steps

1. Sign on to the PingFederate administrative console.

2. Go to **Security > Signing & Decryption Keys & Certificates**.

3. In the row of the certificate that you want to use to sign SAML assertions to Pulse Connect Secure, in the **Select Action** list, select **Export**.

4. On the **Export Certificate** tab, click **Certificate Only**. Click **Next**.

5. On the **Export & Summary** tab, click **Export** and save the file.

6. Click **Done**.

## Configuring SAML integration with PingFederate in Pulse Connect Secure

### Steps

1. In the Pulse Connect Secure administrative interface, go to **System > Configuration > SAML**.

   ![Screen capture of the Pulse Secure administrative console with the System tab selected.](_images/urf1624994919729.png)

2. Click **New Metadata Provider**.

3. Configure the new metadata provider:

   1. In the **Name** field, enter a name.

   2. In the **Location** field, select **Local**.

   3. In the **Upload Metadata File** field, click **Browse** and import the metadata file you saved in [Configuring SSO for GlobalProtect VPN with PingFederate](../single_sign-on_use_cases/htg_config_sso_globalprotect_vpn_pf.html)

   4. In the **Signing Certificate** field, click **Browse** and select the certificate file you saved in the previous topic [Exporting the signing certificate from PingFederate](#exporting-signing-cert-from-pingfed).

   5. In the **Roles** field, select the **Identity Provider** checkbox.

   6. Click **Save Changes**.

      ![Screen capture of the Pulse Secure administrative console with the New Metadata Provider configuration fields displaying.](_images/dif1624995640138.png)

4. In the Pulse Connect Secure administrative interface, go to **Authentication > Auth Servers**.

   ![Screen capture of the Pulse Secure administrative console with the Authentication > Auth Servers screen displaying.](_images/wjw1624995770764.png)

5. In the list, select **SAML Server** and then click **New Server**.

   ![Screen capture of the Server Type list with the SAML Server highlighted in blue.](_images/irt1624995943394.png)

6. Configure the new server:

   1. Enter a **Server Name**.

   2. For **SAML Version**, click **2.0**.

   3. For **Configuration Mode**, click **Metadata**.

   4. In the **Identity Provider Entity ID** list, select the identity provider (IdP) that you created in the previous steps.

   5. In the **Identity Provider Single Sign On Service URL** list, select the appropriate SSO URL.

      ![Screen capture of the Pulse Secure administrative console with the New Server configuration page showing the Settings section.](_images/uyg1624998296188.png)

   6. In the **SSO Method** section, click **POST**.

   7. In the **Select Certificate** list, select the signing certificate you created previously.

   8. In the **Metadata Validity** field, enter any non-zero value.

      |   |                                                                                 |
      | - | ------------------------------------------------------------------------------- |
      |   | You must populate the **Metadata Validity** field even though it won't be used. |

   9. Select the **Do Not Publish Connect Secure Metadata** checkbox.

   10. Click **Save Changes**.

       ![Screen capture of the Pulse Secure administrative console with the New Server configuration page showing the SSO Method, Service Provider Metadata Settings, and User Record Synchronization sections.](_images/pnw1624998406067.png)

   11. Click **Download Metadata** and save the file.

   12. In the Pulse Connect Secure administrative interface, go to **Users > User Realms**.

       ![Screen capture of the Pulse Secure interface with the User Realms page displaying.](_images/ljq1624998579805.png)

   13. Select the authentication realm for your user population.

       ![Screen capture of the User Authentication Realms page of Pulse Secure.](_images/tri1625595774165.png)

   14. In the **Authentication** list, select the IdP that you configured.

       ![Screen capture of the General tab of the User Realms section of the Pulse Secure console.](_images/hqx1625595929818.png)

   15. Click **Save Changes**.

## Configuring SAML integration with Pulse Connect Secure in PingFederate

### Steps

1. In the PingFederate administrative console, go to **Applications > Integration > SP Connections**.

2. Click **Create Connection**.

   ![Screen capture of the administrative console on the SP Connection page displaying the Create Connection and Import Connection buttons.](_images/nxq1625679939156.png)

3. On the **Connection Template** tab, click **Do not use a template for this connection**. Click **Next**.

4. On the **Connection Type** tab, select the **Browser SSO Profiles** checkbox.

5. In the **Protocol** list, select **SAML 2.0** and click **Next**.

6. On the **Connection Options** tab, click **Next**.

7. On the **Import Metadata** tab, click **File** and then choose the metadata file that you downloaded previously. Click **Next**.

   ![Screen capture of the administrative console on the Import Metadata tab for creating an SP connection.](_images/pfn1625680046607.png)

8. On the **Metadata Summary** tab, review the **EntityID** field and click **Next**.

9. On the **General Info** tab, review the imported **Base URL** field, then click **Next**.

   ![Screen capture of the administrative console on the General Info tab for creating an SP connection.](_images/olp1625680129605.png)

10. On the**Browser SSO** tab, click **Configure Browser SSO**.

    ![Screen capture of the administrative console on the Browser SSO tab for configuring a browser SSO.](_images/nnx1625680222533.png)

    #### Result:

    The tabs for the **Browser SSO** section display.

11. Configure the browser SSO:

    1. On the **SAML Profiles** tab, select the **SP-Initiated SSO** checkbox. Click **Next**.

       ![Screen capture of the administrative console on the SAML Profiles tab for configuring a browser SSO.](_images/vlv1625680312534.png)

    2. On the **Assertion Lifetime** tab, accept the default values and click **Next**.

    3. On the **Assertion Creation** tab, click **Configure Assertion Creation**.

       ![Screen capture of the administrative console on the Assertion Creation tab for configuring a browser SSO with the Configure Assertion Creation button available.](_images/elq1625680405984.png)

       #### Result:

       The tabs for the **Assertion Creation** section display.

12. Configure the assertion creation:

    1. On the **Identity Mapping** tab, click **Next**.

    2. On the **Attribute Contract** tab, click **Next**.

    3. On the **Authentication Source Mapping** tab, click **Map New Adapter Instance**.

       ![Screen capture of the administrative console on the Authentication Source Mapping tab for configuring an assertion creation.](_images/tym1625680498617.png)

       #### Result:

       The tabs for the **IdP Adapter Mapping** section display.

13. Configure the IdP adapter mapping:

    1. On the **Adapter Instance** tab, select the HTML form adapter that you created. Click **Next**.

       ![Screen capture of the PingFederate administrative console on the Adapter Instance tab.](_images/fzr1625680599721.png)

    2. On the **Mapping Method** tab, click **Next**.

    3. On the **Attribute Contract Fulfillment** tab, in the **Source** list select **Adapter** and in the **Value** list select **username**. Click **Next**.

       ![Screen capture of the administrative console on the Attribute Contract Fulfillment tab.](_images/wvl1625680681986.png)

    4. On the **Issuance Criteria** tab, click **Next**.

    5. On the **Summary** tab, click **Done**.

       #### Result:

       You return to the **Assertion Creation** section.

14. On the **Authentication Source Mapping** tab, click **Next**.

15. On the **Summary** tab, click **Done**.

    #### Result:

    You return to the **Browser SSO** section.

16. On the **Assertion Creation** tab, click **Next**.

17. On the **Protocol Settings** tab, click **Configure Protocol Settings**.

    #### Result:

    The tabs for the **Protocol Settings** section display.

18. Configure the protocol settings:

    1. On the **Assertion Consumer Service URL** tab, review the **Endpoint URL** value. Click **Next**.

       ![Screen capture of the administrative console on the Assertion Consumer Service URL tab showing the Endpoint URL for a POST binding.](_images/efp1625680766332.png)

    2. On the **Allowable SAML Bindings** tab, ensure that **POST** and **REDIRECT** are the only values checked. Click **Next**.

    3. On the **Signature Policy** tab, click **Next**.

    4. On the **Encryption Policy** tab, click **Next**.

    5. On the **Summary** tab, click **Done**.

       #### Result:

       You return to the **Browser SSO** section.

19. On the **Protocol Settings** tab, click **Next**.

20. On the **Summary** tab, click **Done**.

    #### Result:

    You return to the **SP Connection** section.

21. On the **Browser SSO** tab, click **Next**.

22. On the **Credentials** tab, click **Configure Credentials**.

    ![Screen capture of the administrative console on the Credentials tab showing the Configure Credentials button.](_images/fpr1625680880187.png)

    #### Result:

    The tabs for the **Credentials** section display.

23. Configure the credentials:

    1. On the **Digital Signature Settings** tab, select the **Signing Certificate** that you chose in [Exporting the signing certificate from PingFederate](#exporting-signing-cert-from-pingfed). Click **Next**.

       ![Screen capture of the administrative console on the Digital Signature Settings tab with the Manage Certificates button available.](_images/oeq1625680981801.png)

    2. On the **Summary** tab, click **Done**.

       #### Result:

       You return to the **SP Connection** section.

24. On the **Credentials** tab, click **Next**.

25. On the **Activation & Summary** tab, click **Save**.

    ![Screen capture of the administrative console on the Activation & Summary tab of the SP Connection section.](_images/amf1625599569132.png)

---

---
title: Protecting a web application with PingAccess using PingFederate as the token provider
description: Configure a proof of concept to protect a web application from unwanted access using PingAccess with PingFederate as the token provider.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_protect_web_app_with_pa_using_pf_as_token_provider
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_protect_web_app_with_pa_using_pf_as_token_provider.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["workforce_use_cases:htg_protect_web_app_with_pa_using_pf_as_token_provider_pf101.adoc", "workforce_use_cases:htg_protect_web_app_with_pa_using_pf_as_token_provider_pa61.adoc", "workforce_use_cases:htg_protect_web_app_with_pa_using_pf_as_token_provider_prep_pf.adoc", "workforce_use_cases:htg_protect_web_app_with_pa_using_pf_as_token_provider_connect_pf_pa.adoc", "workforce_use_cases:htg_protect_web_app_with_pa_using_pf_as_token_provider_protect_web_app.adoc"]
section_ids:
  components: Components
  setting-up-pingfed-101: Setting up PingFederate 10.1
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  setting-up-pingaccess-6-1: Setting up PingAccess 6.1
  before-you-begin-2: Before you begin
  about-this-task-2: About this task
  steps-2: Steps
  choose-from-3: Choose from:
  result: Result:
  preparing-pingfederate-for-pingaccess-connectivity: Preparing PingFederate for PingAccess connectivity
  about-this-task-3: About this task
  steps-3: Steps
  result-2: Result:
  result-3: Result:
  result-4: Result
  connecting-pingfederate-and-pingaccess: Connecting PingFederate and PingAccess
  about-this-task-4: About this task
  steps-4: Steps
  result-5: Result
  protect-web-app-with-pingaccess: Protecting a web application with PingAccess
  about-this-task-5: About this task
  steps-5: Steps
  result-6: Result:
  result-7: Result:
  result-8: Result:
---

# Protecting a web application with PingAccess using PingFederate as the token provider

Configure a proof of concept to protect a web application from unwanted access using PingAccess with PingFederate as the token provider.

There are several ways to set up PingAccess to protect a web application. This use case covers the setup and configuration of PingFederate and PingAccess so PingFederate can act as the token provider. This is intended to be a basic configuration to get PingAccess and PingFederate up and running for a proof of concept. To learn more about other configuration options, see the [Protecting a web application with PingAccess](#protect-web-app-with-pingaccess).

## Components

* PingFederate 10.1

* PingAccess 6.1

## Setting up PingFederate 10.1

Combine PingFederate 10.1 with PingAccess 6.1 in a basic configuration to perform a proof of concept for protecting web applications. To get started, set up PingFederate.

### Before you begin

* [PingFederate system requirements](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=110) (page 110).

  Ensure you have the appropriate version of Java.

* [PingFederate port requirements](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=116) (page 116).

### About this task

To set up PingFederate:

### Steps

1. Install PingFederate on your operating system.

   #### Choose from:

   * [Installing PingFederate on Windows](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=121) (page 121).

   * [Installing PingFederate on Linux](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=122) (page 122).

2. Start the PingFederate server.

   #### Choose from:

   * [Starting and stopping PingFederate on Windows](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=155) (page 155).

   * [Starting and stopping PingFederate on Linux](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=155) (page 155).

3. Open the PingFederate administrative console.

   1. Open a browser and enter `https://Your Server Domain:9999/pingfederate/app`.

      |   |                                                                                                                                                                                                     |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | *Your Server Domain* is your fully qualified domain name (FQDN).If you do not have a DNS set up for an FQDN, you can also use an IP address, but the use of an FQDN long-term is the best practice. |

   2. To sign on, in the username field, enter `Administrator`, and in the password field, enter `2Federate`.

   3. To proceed, review the license agreement. Click **Accept**.

4. Click **No, Set Up Without PingOne for Enterprise**, and then click **Next**.

5. To import a valid PingFederate license, click **Choose File** and locate your license file.

   |   |                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Learn more in [Reviewing or importing your license](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=157) (page 157). |

6. Click **Next**.

7. On the **Basic Information** tab, enter the basic information.

   1. In the **Base URL** field, verify your base URL. Update as needed.

      The domain portion of the base URL should match the domain name of your organization because it is part of the address where your applications, users, and partners communicate with your PingFederate environment.

      |   |                                                                                                                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can add multiple virtual host names at a later time. Learn more in [Virtual host names](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=855) (page 855). |

   2. In the **Entity ID** field, enter your Entity ID if prompted. Click **Next**.

      |   |                                                                                                                                                        |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | This is the unique identifier of your organization. It is how your partners identify you when communicating with you based on SAML 2.0 specifications. |

8. On the **Connection** tab, in the **Directory Type** list, select your directory type and provide the required information.

   |   |                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Learn more about each field in [Connecting to a directory](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=158) (page 158). |

9. Click **Next** until you reach the **Summary** tab. Click **Done**.

   |   |                                                                                              |
   | - | -------------------------------------------------------------------------------------------- |
   |   | If you are connecting to Active Directory (AD), bypass Kerberos authentication at this time. |

10. On the **Administrator Account** tab, create an administrative account.

    1. To replace the default value in the **Username** field, enter a new value.

    2. In the **Password** and **Confirm Password** fields, enter a password.

    3. Click **Next**.

11. On the **Confirmation** tab, review your configuration.

12. To apply the configuration to PingFederate, click **Next**, and then click **Done**.

## Setting up PingAccess 6.1

Combine PingFederate 10.1 with PingAccess 6.1 in a basic configuration to perform a proof of concept for protecting web applications. To get started, set up PingAccess.

### Before you begin

Review and ensure you meet the [PingAccess installation requirements](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=33) (page 33), including the port requirements and required Java version.

### About this task

To set up PingAccess:

### Steps

1. Install PingAccess on your operating system.

   #### Choose from:

   * [Linux](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=38) (page 38)

   * [Windows using the installer](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=39) (page 39).

   * [Windows from the command line](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=40) (page 40).

2. [Start PingAccess](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=41) (page 41).

   |   |                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can also [run PingAccess as a service](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=44) (page 44). |

3. [Go to the administrative console](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=42) (page 42) and follow the setup wizard.

   #### Result:

   The PingAccess administrative console landing page opens.

## Preparing PingFederate for PingAccess connectivity

Combine PingFederate 10.1 with PingAccess 6.1 in a basic configuration to perform a proof of concept for protecting web applications. To set up this proof of concept, configure PingFederate for PingAccess connectivity.

### About this task

To configure PingFederate for PingAccess connectivity, use the PingFederate console.

### Steps

1. To verify PingFederate roles and protocols, go to **System → Server → Protocol Settings**, and then proceed to [Enabling PingFederate roles and protocols](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=437).

   |   |                                                                                     |
   | - | ----------------------------------------------------------------------------------- |
   |   | In PingFederate 10.1.x, all necessary roles and protocols are turned on by default. |

2. To verify the password credential validator (PCV) created during the setup process in [Setting up PingFederate 10.1](#setting-up-pingfed-101), go to **System → Data & Credential Stores → Password Credential Validators**.

   #### Result:

   You see a PCV that corresponds with the directory that you set up.

   |   |                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If there is no PCV displayed, see [Creating a password credential validator](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=438). |

3. To verify the IdP adapter created in the setup process, go to **Authentication → Integration → IdP Adapters**.

   #### Result:

   You see an HTML form adapter associated with the PCV in step 2.

   |   |                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If no IdP adapter is displayed, see [Configuring an IdP adapter](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=439). |

4. To define the default scope, go to **System → OAuth Settings → Scope Management**. Proceed to [Defining the default scope](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=439).

5. To create an access token manager, go to **Applications → OAuth → Access Token Management**.

   From **Token Management**, proceed to [Creating an access token manager](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=440).

6. Define an authentication policy contract.

   1. Go to **Authentication → Policies → Policy Contracts**.

   2. Click **Create New Contract**.

   3. In the **Contract Name** field, enter a name for your contract.

   4. Click **Next** until you reach the **Summary** section. Click **Save**.

      |   |                                                                                                                                         |
      | - | --------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Configuring a policy contract instead of configuring an IdP adapter mapping enables more advanced and flexible authentication policies. |

7. Configure a policy contract grant mapping.

   1. Go to **Security → Authentication → OAuth → Policy Contract Grant Mapping**.

   2. From the **Policy Contract** list, select the policy you just created. Click **Add Mapping**.

   3. Click **Next** until you reach the **Contract Fulfillment** section.

   4. From the **Source** list, select **Authentication Policy Contract** for both **User\_Key** and **User\_Name** contracts.

   5. From the **Value** list, select **Subject** for both **User\_Key** and **User\_Name** contracts.

   6. Click **Next** until you reach the **Summary** section. Click **Save**.

8. To configure an access token mapping, go to **Applications → OAuth → Access Token Mapping**. Proceed to [Configuring an access token mapping](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=441).

9. To create an OpenID Connect policy, go to **Applications → OAuth → OpenID Connect Policy Management**. Proceed to [Creating an OpenID Connect policy](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=441).

10. To create a resource server client, go to **Applications → OAuth → Clients**. Proceed to [Creating a resource server client](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=442).

11. To create a web session client, go to **Applications → OAuth → Clients**. Proceed to [Creating a web session client ](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=442).

12. Create and export a certificate from PingFederate to PingAccess.

    1. Go to **Security → Certificate & Key Management → SSL Server Certificates**.

    2. Click **Create New**.

    3. In the **Common Name** field, enter the PingFederate server address.

       |   |                                                                                                                       |
       | - | --------------------------------------------------------------------------------------------------------------------- |
       |   | This should match the *Your Domain Name* entry in step 3a in [Setting up PingFederate 10.1](#setting-up-pingfed-101). |

    4. In the **Organization** field, enter your organization's name.

    5. In the **Country** field, enter the two-letter abbreviation for your country.

    6. Complete the remaining fields as required.

    7. Click **Next**.

    8. Click **Save**.

    9. In the **Action** section, click **Activate Default for Runtime Server**.

    10. In the **Action** section, click **Activate Default for Admin Console**.

    11. In the **Action** section, click **Export**.

    12. Click **Certificate Only**. Click **Next**.

    13. Click **Export**, and then save the exported certificate.

    14. Click **Done**.

        |   |                                                                                                                                                                                             |
        | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | To avoid confusion, you can delete the default **localhost** certificate that appears in the certificate list. In the **Action** section, select **Deactivate**, and then click **Delete**. |

### Result

You are ready to connect PingAccess to PingFederate.

## Connecting PingFederate and PingAccess

Combine PingFederate 10.1 with PingAccess 6.1 in a basic configuration to perform a proof of concept for protecting web applications. After PingFederate has been installed and prepared for PingAccess connectivity, connect PingAccess and PingFederate.

### About this task

To connect PingFederate to PingAccess, use the PingAccess administrative console.

### Steps

1. [Importing certificates and creating a trusted certificate group](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=444).

2. Configure the token provider.

   1. Click **Settings**, and then go to **System → Token Provider → PingFederate → Runtime**.

   2. In the **Issuer** field, enter the PingFederate issuer name.

   3. From the **Trusted Certificate Group** list, select the **PingFed** certificate group.

   4. **Optional:** Click **Show Advanced Settings** and select the **Skip Hostname Verification** checkbox.

   5. Click **Save**.

   6. Click **Settings**, and then go to **System → Token Provider → PingFederate → Administration**.

   7. In the **Host** field, enter the host name or IP address for the PingFederate Runtime.

      For example, `mypingfedserver`.

   8. In the **Port** field, enter the port number for PingFederate Runtime.

      For example, `9031`.

   9. In the **Admin Username** field, enter the username.

      This username only requires auditor, read-only, permissions in PingFederate.

   10. In the **Admin Password** field, enter the password.

   11. From the **Secure** list, select **Secure**.

   12. From the **Trusted Certificate Group** list, select the **PingFed** certificate group.

   13. Click **Save**.

   14. Click **Settings**, and then go to **System → Token Provider → PingFederate → OAuth Resource Server**.

   15. In the **Client ID** field, enter the OAuth Client ID you defined when creating the PingAccess OAuth client in PingFederate.

       For example, `pa_rs`.

   16. In the **Client Credentials Type** section, select **Secret**, then enter the **Client Secret** assigned when you created the PingAccess OAuth client in PingFederate.

   17. In the **Subject Attribute Name** field, enter the attribute you want to use from the OAuth access token as the subject for auditing purposes.

       For example, `username`.

   18. **Optional:** Select the **Send Audience** checkbox.

   19. Click **Save**.

### Result

PingAccess can be configured to protect a web application.

## Protecting a web application with PingAccess

Use this use case to combine PingFederate 10.1 with PingAccess 6.1 in a basic configuration to perform a proof of concept for protecting web applications.

### About this task

To configure PingAccess to protect a web application for a proof of concept, use the PingAccess administrative console.

### Steps

1. To configure PingAccess to listen on port 443, adjust the engine listeners.

   1. Go to **Settings → Networking → Engine Listeners** and click **Add Engine Listener**.

   2. Complete the fields.

   3. Click **Save**.

      |   |                                                                                                                                                                                                                                                                                                                                                                    |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | Port 443 is commonly restricted to root-level access on certain operating systems. Availability to bind to this port might require root access. Consult your system administrator with any questions about port access.Listening on port 443 is not a requirement for using PingAccess, but rather a recommendation for this specific, proof of concept, use case. |

2. Configure a virtual host.

   1. Click **Applications**, and then go to **Applications → Virtual Hosts**.

   2. Click **[icon: plus, set=fa]Add Virtual Host**.

   3. In the **Host** field, enter the name for the virtual host.

      This is the host name used by end users to reach the site. For example, myHost.com. You can use a wildcard (`*`) for part or all of the host name. For example, `*.example.com` matches all host names ending in .example.com, and `*` matches all host names.

      For this example, add `*:443` and `localhost:443`.

3. Configure a site.

   For this proof of concept we are using <https://www.httpbin.org>.

   |   |                                                                                                                                                                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The site www\.httpbin.org is not affiliated with Ping Identity, but is a good example to use when presenting a proof of concept due to its ability to quickly expose the browser's communication with the protected site. You can choose to protect a different website, substituting instances of `www.httpbin.org` with your site. |

   1. Click **Applications**, and then go to **Sites → Sites**.

   2. Click **[icon: plus, set=fa]Add Site**.

   3. In the **Site Name** field, enter `HTTP Bin`.

   4. In the **Targets** field, enter `www.httpbin.org:443`.

   5. Select the **Secure** checkbox.

   6. From the **Trusted Certificate Group** list, select **Trust Any**.

      ![A screen capture of the admin console Add Site screen. The fields contain the information outlined in the substeps for HTTP bin. Name: HTTP bin, Targets: www.httpbin.org:443, Secure is marked No, and Trusted Certificate Group has Trust Any selected.](_images/ear1608575102956.png)

4. Configure a web session.

   1. Click **Access**, and then go to **Web Sessions → Web Sessions**.

   2. Click **[icon: plus, set=fa]Add Web Session**.

   3. In the **Name** field, enter `Web Session`.

   4. From the **Cookie Type** list, select **Encrypted JWT**.

   5. In the **Audience** field, enter `WebSession`.

   6. From the **OpenID Connect Login Type** list, select **Code**.

      |   |                                                                                                                                                                                                                                                                                      |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | For maximum security and standards interoperability, use the **Code** login type. However, other options are available. For information on the available profiles, see [Creating web sessions](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-61.pdf#page=254). |

   7. In the **Client ID** field, enter `pa_wam`.

   8. From the **Client Credentials Type** menu, select **Secret**.

   9. Enter the client secret for the OAuth client.

   10. In the **Idle Timeout** field, specify the amount of time, in minutes, that the PingAccess token remains active when no activity is detected by the user.

       The default is `60` minutes.

       |   |                                                                                                                                                                                            |
       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
       |   | If there is an existing valid PingFederate session for the user, an idle timeout of the PingAccess session might result in its re-establishment without forcing the user to sign on again. |

   11. In the **Max Timeout** field, specify the amount of time, in minutes, that the PingAccess token remains active before expiring.

       The default is `240` minutes.

   12. Click **Save**.

5. Configure an identity mapping.

   For this proof of concept use case, you do not need to configure rules.

   1. Click **Access**, and then go to **Identity Mappings → Identity Mappings**.

   2. Click **[icon: plus, set=fa]Add Identity Mapping**.

   3. In the **Name** field, enter `General Identity Mapping`.

   4. From the **Type** list, select **Header Identity Mapping**.

   5. In the **Attribute to Header Mapping** section, click **Subject**.

   6. From the **Attribute Name** list, select **sub** and in the **Header Name** field, enter `X-SUB`.

   7. In the **Certificate to Header Mapping** section, in the **Header Name** field, enter `X-CERT`.

      ![A screen capture of the admin console General Identity Mapping screen. The fields contain the information outlined in the substeps. Name: General Identity Mapping, Type: Header Identity Mapping is selected, Attribute to Header Mapping: sub is selected for Attribute Name and X-SUB is entered in Header Name, Certificate to Header Mapping: X-CERT is in the Header Name field.](_images/qin1608586061365.png)

6. Add a new redirection URI in PingFederate.

   For this proof of concept, we are using `www.protected.com`.

   |   |                                                                                                                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The redirection URI is what your end users enter when they are accessing the protected site. In this proof of concept, we are entering https\://www\.protected.com into the browser, but we are accessing https\://www\.httpbin.org through this configuration with PingAccess. To understand the relationship between the protected site and the redirection URI, see the following diagram. |

   ![A flow diagram showing a browser request to the virtual host 'protected.com' that generates a web session with . A session cookie is set in the browser that later uses instead of re-authenticating the user. processes and forwards the request to the target site, httpbin.org. Identity mapping and security policies verify the user should have access to the target site, providing user-centric data in the request. presents the protected site's response to the browser.](_images/rvp1609775442223.png)

   1. From the PingFederate administrative console, go to **Applications → OAuth → Clients → pa\_wam**.

   2. Click **Add**.

   3. In the **URI** field, enter `https://www.protected.com/pa/oidc/cb`.

      |   |                                                                                                     |
      | - | --------------------------------------------------------------------------------------------------- |
      |   | If you choose to use a different URI, format your entry as https\://*Your Site Address*/pa/oidc/cb. |

7. Configure an application in PingAccess.

   1. From the PingAccess administrative console, click **Applications** and then go to **Applications → Applications**.

   2. Click **[icon: plus, set=fa]Add Application**.

   3. In the **Name** field, enter `HTTP Bin`.

   4. In the **Context Root** field, enter `/`.

   5. From the **Virtual Host** list, select **www\.protected.com:443**.

   6. In the **Application Type** section, select **Web**.

   7. Verify that the **SPA Support** checkbox is unselected.

   8. From the **Web Session** list, select **None**.

   9. In the **Destination** section, select **Site**, then select **HTTP Bin**.

   10. Verify that the **Require HTTPS** checkbox is selected.

   11. Select the **Enabled** checkbox.

   12. Click **Save**.

8. Add a new authentication policy in PingFederate.

   1. From the PingFederate administrative console, go to **Authentication → Policies**.

   2. Select the **IDP Authentication Policies** checkbox.

   3. Click **Add Policy**.

   4. In the **Name** field, enter a name for your policy.

   5. From the **Policy** list, select **IdP Adapters** and then select **HTML Form Adapter**.

   6. In the **Fail** section, click **Done**.

   7. In the **Success** section, from the **Success** list, select **Policy Contracts** and then select **Default Policy Contract**.

   8. In the **Success** section, click **Contract Mapping**.

   9. Click **Next** until you reach the **Contract Fulfillment** tab.

   10. From the **Source** list, select **Adapter (HTMLFormAdapter)**.

   11. From the **Value** list, select **username**.

   12. Click **Next** until you reach the **Summary** tab. Click **Done**.

   13. Click **Done**, and then click **Save**.

       #### Result:

       Your policy is saved and enabled.

9. **Optional:** Demonstrate the configuration so far.

   1. Open a new browser window in private browsing or incognito mode and enter `https://www.httpbin.org/anything`.

   2. Note the following information:

      * The URL that the browser talks to is listed as https\://www\.httpbin.org/anything.

      * No cookies, typically found under the `headers` section, are set.

        ![A screen capture of a browser window displaying httpbin.org/anything with the url field highlighted with a red box. The field text reads 'https://httpbin.org/anything'.](_images/cjt1609776216785.png)

   3. Open a new browser window in private browsing or incognito mode and enter `https://www.protected.com/anything`.

   4. Note the following information:

      * The site displays the information from https\://www\.httpbin.org/anything.

      * The URL that the browser talks to is listed as https\://www\.protected.com/anything.

      * A PingAccess cookie, `PA.WebSession`, is set.

        ![A screen capture of a browser window displaying \protected.com/anything with the url and cookie fields highlighted with a red box. The url field text reads 'https://protected.com/anything', and the cookie field shows an identifier for a cookie.](_images/gaw1609776603645.png)

10. Set authentication requirements for the protected site.

    1. In the PingAccess administrative console, go to **Applications → HTTP Bin** and click the **Pencil** ([icon: pencil, set=fa]) icon to edit.

    2. From the **Web Session** list, select **Web Session**.

    3. Click **Save**.

    4. **Optional:** Refresh the browser window where you are accessing https\://www\.protected.com/anything.

       |   |                                                                                                                                                                                                                                                         |
       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | PingFederate now asks for credentials to access the site.If you enter valid credentials from your datastore to access the page, the same information from https\://www\.httpbin.org/anything is displayed through https\://www\.protected.com/anything. |

       #### Result:

       PingAccess evaluates the browser's requests through the authentication requirements you defined.

11. Configure PingAccess to pass data to the application.

    1. In the PingAccess administrative console, go to **Applications → HTTP Bin**.

    2. From the **Web Identity Mapping** list, select **General Identity Mapping**.

    3. Click **Save**.

    4. **Optional:** Refresh the browser window where you are accessing https\://www\.protected.com/anything.

       #### Result:

       There are two new fields following `User-Agent`: `X-Cert` and `X-Sub`.

---

---
title: Protecting your VPN with PingID MFA
description: To improve network security posture and provide a true MFA experience to network resources, add PingID multi-factor authentication (MFA) to your VPN authentication ceremony.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_protect_vpn_with_pid_mfa
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_protect_vpn_with_pid_mfa.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  next-steps: Next steps
---

# Protecting your VPN with PingID MFA

To improve network security posture and provide a true MFA experience to network resources, add PingID multi-factor authentication (MFA) to your VPN authentication ceremony.

## Before you begin

**Component**

* PingFederate 10.1

Do the following:

* Install and configure PingFederate.

* Install and configure PingID.

* Enable RADIUS network connectivity between your VPN client and PingFederate.

* Connect and configure an existing user datastore as a password credential validator (PCV), such as PingDirectory or Active Directory.

### About this task

By using the RADIUS protocol, PingFederate works as an on-premise agent to enable MFA into your VPN use cases. The following steps are required to set up and configure a PingID MFA for your VPN.

### Steps

1. In the PingOne for Enterprise administrative console, go to **Setup > PingID > Client Integration > Integration with PingFederate and Other Clients**.

   ![Screen capture illustrating the navigation to Setup Client Integration Integration with and Other Clients in the admin console.](_images/llt1601575026054.png)

2. To receive your `pingid.properties` file, click **Download**.

   |   |                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------- |
   |   | If there are no property files available and you need to generate one, click the **Generate** button and then click **Download**. |

3. In the PingFederate administrative console, go to **System > Data & Credential Stores > Password Credential Validators**.

   ![Screen capture illustrating the navigation to System Data & Credential Stores Password Credential Validators in the administrative console. Existing instances are displayed.](_images/bhd1601578462217.png)

4. Click **Create New Instance**.

5. On the **Type** tab, configure the fields:

   1. In the **Instance Name** field, enter an instance name.

   2. In the **Instance ID** field, enter an instance ID.

   3. From the **Type** list, select **PingID PCV (with integrated RADIUS server)**.

   4. Click **Next**.

      ![Screen capture illustrating the configurable Type fields for a new PCV in .](_images/hwu1601580627905.png)

6. On the **Instance Configuration** tab, click **Add a new row to 'RADIUS Clients'**.

   1. In the **Client IP** field, enter a client IP address to match your RADIUS client.

   2. In the **Client Shared Secret** field, enter a shared secret to match your RADIUS client.

   3. To complete the client configuration, click **Update**.

      Repeat step 6 for any additional RADIUS clients.

7. Click **Add a new row to 'Delegate PCV's'**.

   1. From the **Delegate PCV** list, select the primary user datastore you want RADIUS clients to authenticate against.

   2. To complete the configuration, click **Update**.

      Repeat step 7 for any additional PCVs.

8. In the **PingID Properties File** field, paste the `pingid.properties` file you downloaded from PingID in step 2.

   ![Screen capture illustrating a completed Properties File field in .](_images/dzn1601582257289.png)

9. In the **Authentication During Errors** field, select the appropriate authentication behavior when PingID services are unavailable.

   #### Choose from:

   * **Bypass User**

   * **Block User**

   * **Passive Offline Authentication**

   * **Enforce Offline Authentication**

10. In the **Users Without a Paired Device** field, select whether to bypass or block the user when PingID services are unavailable.

11. Complete any remaining fields. Click **Next**.

12. Click **Next** and **Done**.

13. Click **Save**.

### Next steps

Perform the RADIUS client test to verify and ensure the authentication ceremony works properly.

---

---
title: Setting up a login form that validates credentials against AD in PingFederate
description: Configure a login form in PingFederate that validates credentials against Active Directory (AD).
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_set_up_login_form_validating_creds_with_ad_pf
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_set_up_login_form_validating_creds_with_ad_pf.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2025
page_aliases: ["workforce_use_cases:htg_set_up_login_form_validating_creds_with_ad_pf_datastore.adoc", "workforce_use_cases:htg_set_up_login_form_validating_creds_with_ad_pf_pcv.adoc", "workforce_use_cases:htg_set_up_login_form_validating_creds_with_ad_pf_adapter.adoc"]
section_ids:
  component: Component
  configure-login-form-validate-the-datastore: Configuring the datastore
  before-you-begin: Before you begin
  steps: Steps
  configure-the-password-cred-validator: Configuring the password credential validator
  before-you-begin-2: Before you begin
  steps-2: Steps
  choose-from: Choose from:
  configuring-the-idp-adapter: Configuring the IdP adapter
  before-you-begin-3: Before you begin
  about-this-task: About this task
  steps-3: Steps
  result: Result
  next-steps: Next steps
---

# Setting up a login form that validates credentials against AD in PingFederate

Configure a login form in PingFederate that validates credentials against Active Directory (AD).

After completing these steps, the HTML form adapter is ready to use in either an [Authentication Policy](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=242) (page 242) or an [SP connection](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-101.pdf#page=398) (page 398).

## Component

PingFederate 10.1

## Configuring the datastore

Configure a datastore in PingFederate.

### Before you begin

* Install and run PingFederate.

* Install Active Directory (AD).

* Ensure the AD service account has permissions in all domains in that forest to read and access user data in all domains to which the agent connects.

### Steps

1. In the PingFederate administrative console, go to **System > Data & Credential Stores > Data Stores**.

2. Click **Add new Data Store**.

3. On the **Data Store Type** tab, in the **Name** field, enter a name.

4. In the **Type** list, select **Directory (LDAP)**. Click **Next**.

   ![Screen capture of the Data Store Type tab showing Active Directory Data Store in the Name field, and Directory (LDAP) selected from the Type list.](_images/vto1602268313849.png)

5. On the **LDAP Configuration** tab, in the **Hostname(s)** field, enter a name.

6. From the **LDAP Type** list, select **Active Directory**.

7. In the **User DN** and **Password** fields, enter the desired user distinguished name (DN) and password.

8. Select the **Use LDAPS** checkbox.

   Ping recommends that all LDAP connections be secured using LDAPS.

   |   |                                                                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | To enable the password changes, password reset, or account unlock features in the HTML form adapter against Microsoft AD, you must secure the connection to your directory server using LDAPS. AD requires this level of security to allow password changes. |

9. Complete any other fields that can help configure the datastore connection according to your current architect posture.

10. To test the connection, click **Test Connection**.

    ![Screen capture of the LDAP Configuration tab and corresponding fields.](_images/kym1602268501749.png)

11. Click **Next**.

12. On the **Summary** tab, review your entries, and then click **Save**.

## Configuring the password credential validator

Configure a password credential validator (PCV) in PingFederate.

### Before you begin

* Install and run PingFederate.

* Install Active Directory (AD).

* [Configure the data store](#configure-login-form-validate-the-datastore).

* Ensure the AD service account has permissions in all domains in that forest to read and access user data in all domains to which the agent connects.

### Steps

1. In the PingFederate administrative console, go to **System → Data & Credential Stores → Password Credential Validators**.

2. Click **Create New Instance**.

3. On the **Type** tab, in the **Instance Name** and **Instance ID** fields, enter a name and ID.

4. From the **Type** list, select **LDAP Username Password Credential Validator**.

   ![Screen capture of the Type tab showing the completed Instance Name and Instance ID fields. LDAP Username Password Credential Validator is selected from the Type list.](_images/oux1602268888684.png)

5. Click **Next**.

6. On the **Instance Configuration** tab, from the **LDAP Datastore Field Value** list, select **Active Directory Data Store**.

7. In the **Search Base Field Value** field, enter the location in the directory from which the LDAP search begins.

8. In the **Search Filter Field Value** field, enter an LDAP filter.

   You can use ${username} as part of the query. For example, for AD, sAMAccountName=${username}.

9. In the **Scope of Search** section, choose from:

   #### Choose from:

   * **One Level**

   * **Subtree**

     Choose **One Level** to search just the base distinguished name (DN), or choose **Subtree** to search organizational units nested under the base DN.![Screen capture of the Instance Configuration tab.](_images/slw1602268941097.png)

10. Click **Next**.

11. On the **Extended Contract** tab, confirm the default values and add additional attributes as needed.

    |   |                                                                              |
    | - | ---------------------------------------------------------------------------- |
    |   | On this tab, you can also extend the attribute contract of the PCV instance. |

    ![Screen capture of the Extended Contract tab showing the default values.](_images/kda1602269015267.png)

12. Click **Next**.

13. On the **Summary** tab, confirm your entries, and then click **Save**.

## Configuring the IdP adapter

Configure an identity provider (IdP) in PingFederate.

### Before you begin

* Install and run PingFederate.

* Install Active Directory (AD).

* [Configure the data store](#configure-login-form-validate-the-datastore).

* [Configure the password credential validator (PCV)](#configure-the-password-cred-validator).

* Ensure the AD service account has permissions in all domains in that forest to read and access user data in all domains to which the agent connects.

### About this task

The following steps are the minimum to set up an HTML adapter to validate against AD.

### Steps

1. In the PingFederate administrative console, go to **Authentication → Integration → IdP Adapters**.

2. Click **Create New Instance**.

3. On the **Type** tab, in the **Instance Name** and **Instance ID** fields, enter a name and ID.

4. From the **Type** list, select **HTML Form IdP Adapter**.

   ![Screen capture of the Type tab showing the completed Instance Name and Instance ID fields and HTML Form IdP Adapter selected from the Type list.](_images/anv1602269303714.png)

5. Click **Next**.

6. On the **Idp Adapter** tab, in the **Password Credential Validator Instance** section, click **Add a new row to 'Credential Validators'**.

7. From the **Password Credential Validator Instance** list, select the appropriate PCV, and then click **Update**.

   ![Screen capture of the IdP Adapter tab showing the corresponding fields.](_images/gjx1602269573655.png)

8. Review and modify any other fields as needed, and then click **Next**.

   Many fields have default values. Make adjustments as needed.

9. On the **Extended Contract** tab, confirm the default values and add additional attributes as needed.

10. Click **Next**.

11. On the **Adapter Attributes** tab, select the attributes to receive a pseudonym to uniquely identify a user and any attributes that must be masked in the log files.

    ![Screen capture of the Adapter Attributes tab showing the checkboxes to select to give attributes pseudonyms or mask log values.](_images/dxq1602269917079.png)

12. Click **Next**.

13. On the **Adapter Contract Mapping** tab, click **Configure Adapter Contract**.

14. On the **Attribute Sources & User Lookup** tab, fulfill the adapter contract with the adapter's default values, or use these values plus additional attributes retrieved from local data stores.

15. Click **Next**.

16. On the **Adapter Contract Fulfillment** tab, fulfill your adapter contract with values from the authentication adapter or with dynamic text values.

    By default, **Adapter** is selected from the **Source** lists.

17. Click **Next**.

18. On the **Issuance Criteria** tab, optionally create criteria for PingFederate to evaluate to determine whether users are authorized to access SP resources. Click **Next**.

19. On the **Summary** tab, confirm your entries, and then click **Done**.

    ![Screen capture of the Summary tab showing the selected entries.](_images/lqa1602270433807.png)

20. On the **Adapter Contract Mapping** tab, click **Next**.

21. On the **Summary** tab, review the IdP adapter instance settings, and then click **Save**.

### Result

After completing these steps, the HTML form adapter is ready to use in either an [Authentication Policy](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) or an [SP connection](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html).

### Next steps

Enter AD credentials (username and password) to test the configured adapter.

---

---
title: Setting up an authentication flow that includes MFA (PingFederate and PingID)
description: This configuration creates a service provider (SP) connection with a multi-factor authentication (MFA) flow using PingFederate and PingID.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_set_up_authn_flow_mfa_pf_pid
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_set_up_authn_flow_mfa_pf_pid.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2025
page_aliases: ["workforce_use_cases:htg_set_up_authn_flow_mfa_pf_pid_pcv_pf.adoc", "workforce_use_cases:htg_set_up_authn_flow_mfa_pf_pid_html_adapter_pcv.adoc", "workforce_use_cases:htg_set_up_authn_flow_mfa_pf_pid_download_props.adoc", "workforce_use_cases:htg_set_up_authn_flow_mfa_pf_pid_adapter.adoc", "workforce_use_cases:htg_set_up_authn_flow_mfa_pf_pid_authn_policy_contract.adoc", "workforce_use_cases:htg_set_up_authn_flow_mfa_pf_pid_sp_connection.adoc", "workforce_use_cases:htg_set_up_authn_flow_mfa_pf_pid_authn_selector.adoc", "workforce_use_cases:htg_set_up_authn_pid_pf_create_policy.adoc", "workforce_use_cases:htg_set_up_authn_flow_mfa_pf_pid_testing.adoc"]
section_ids:
  components: Components
  creating-a-password-credential-validator-in-pingfederate: Creating a password credential validator in PingFederate
  steps: Steps
  creating-an-html-adapter-that-uses-the-pcv: Creating an HTML adapter that uses the PCV
  steps-2: Steps
  downloading-the-pingid-properties-file-in-pingone-for-enterprise: Downloading the pingid.properties file in PingOne for Enterprise
  steps-3: Steps
  creating-a-pingid-adapter-in-pingfederate: Creating a PingID adapter in PingFederate
  steps-4: Steps
  creating-an-authentication-policy-contract: Creating an authentication policy contract
  steps-5: Steps
  creating-an-sp-connection: Creating an SP connection
  steps-6: Steps
  creating-an-authentication-selector: Creating an authentication selector
  steps-7: Steps
  creating-an-authentication-policy: Creating an authentication policy
  steps-8: Steps
  testing-your-connection: Testing your connection
  steps-9: Steps
  result: Result:
---

# Setting up an authentication flow that includes MFA (PingFederate and PingID)

This configuration creates a service provider (SP) connection with a multi-factor authentication (MFA) flow using PingFederate and PingID.

## Components

* PingFederate 10.1

* PingID

## Creating a password credential validator in PingFederate

### Steps

1. In the PingFederate administrative console, go to **System > Data & Credential Stores > Password Credential Validators**, and click **Create New Instance**.

2. On the **Type** tab, in the **Type** list, select **Simple Username Password Credential Validator**. Complete the remaining required fields, and then click **Next**.

3. On the **Instance Configuration** tab, click **Add a New Row to 'Users'**. Complete the **Username**, **Password**, and **Confirm Password** fields, and then click **Update**.

4. Click **Next**, and then on the **Summary** tab, click **Done**.

5. In the **Password Credential Validators** window, click **Save**.

## Creating an HTML adapter that uses the PCV

### Steps

1. Go to **Authentication > Integration > IdP Adapters** and click **Create New Instance**.

2. On the **Type** tab, in the **Type** list, select **HTML Form IdP Adapter**. Complete the remaining required fields, and then click **Next**.

3. On the **IdP Adapter** tab, in the **Password Credential Validator** list, select the PCV you previously created. Click **Update**.

4. Click **Next** until you reach the **Adapter Attributes** tab.

5. On the **Adapter Attributes** tab, select the **Pseudonym** checkbox for the `username` entry. Click **Next** until you reach the **Summary** tab.

6. On the **Summary** tab, click **Done**.

7. In the **Manage IdP Adapter Instances** window, click **Save**.

## Downloading the pingid.properties file in PingOne for Enterprise

### Steps

1. In the PingOne for Enterprise admin portal, go to **Setup > PingID > Client Integration**.

2. In the **Integrate with PingFederate and Other Clients** section, click **Download**.

## Creating a PingID adapter in PingFederate

### Steps

1. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters** and click **Create New Instance**.

2. On the **Type** tab, in the **Type** list, select **PingID Adapter 2.6**. Complete the remaining required fields, and then click **Next**.

3. On the **IdP Adapter** tab, click **Choose File**. Select the `pingid.properties` file, and then click **Next**.

4. Click **Next** until you reach the **Adapter Attributes** tab.

5. On the **Adapter Attributes** tab, select the **Pseudonym** checkbox for the `subject` entry. Click **Next**.

6. Click **Next** until you reach the **Summary** tab, and then click **Done**.

7. In the **Manage IdP Adapter Instances** window, click **Save**.

## Creating an authentication policy contract

### Steps

1. Go to **Authentication > Policies > Policy Contracts** and click **Create New Contract**.

2. On the **Contract Info** tab, in the **Contract Name** field, enter a name.

3. Click **Next** until you reach the **Summary** tab, and then click **Done**.

4. In the **Authentication Policy Contracts** window, click **Save**.

## Creating an SP connection

### Steps

1. Go to **Applications > Integration > SP Connections** and click **Create Connection**.

2. Click **Next** until you reach the **Connection Type** tab.

3. On the **Connection Type** tab, select the **Browser SSO Profiles** checkbox. Click **Next** until you reach the **General Info** tab.

4. On the **General Info** tab, in the **Partner's Entity ID** field, enter a dummy entity ID. In the **Connection Name** field, enter a name, and then click **Next**.

5. On the **Browser SSO** tab, click **Configure Browser SSO**.

6. On the **SAML Profiles** tab, select the **IdP-Initiated SSO** checkbox only. Click **Next** until you reach the **Assertion Creation** tab.

7. On the **Assertion Creation** tab, click **Configure Assertion Creation**. Click **Next** until you reach the **Authentication Source Mapping** tab.

8. On the **Authentication Source Mapping** tab, click **Map New Authentication Policy**.

9. On the **Authentication Policy Contract** tab, in the **Authentication Policy Contract** list, select your policy contract. Click **Next** until you reach the **Attribute Contract Fulfillment** tab.

10. On the **Attribute Contract Fulfillment** tab, in the **Source** list for the `SAML_SUBJECT` entry, select **Authentication Policy Contract**. From the **Value** list, select **subject**.

11. Click **Next** and **Done** until you reach the **Protocol Settings** tab. Click **Configure Protocol Settings**.

12. On the **Assertion Consumer Service URL** tab, enter a number in the **Index** field. From the **Binding** list, select **POST**. In the **Endpoint URL** field, enter a dummy URL, then click **Add**.

13. Click **Next** and **Done** until you reach the **Credentials** tab. Click **Configure Credentials**.

14. On the **Digital Signature Settings** tab, from the **Signing Certificate** list, select a signing certificate.

15. Click **Next** and **Done** until you reach the **Activation & Summary** tab. Click **Save**.

16. In the **SP Connections** window, click **Save**.

## Creating an authentication selector

### Steps

1. Go to **Authentication > Policies > Selectors** and click **Create New Instance**.

2. On the **Type** tab, in the **Type** list, select **Connection Set Authentication Selector**. Complete the remaining required fields, and then click **Next**.

3. On the **Authentication Selector** tab, click **Add a New Row to 'Connections'**. From the **Connection** list, select your SP connection. Click **Update** and then **Next**.

4. On the **Summary** tab, click **Done**. In the **Manage Authentication Selector Instances** window, click **Save**.

## Creating an authentication policy

### Steps

1. Go to **Authentication > Policies > Policies** and click **Add Policy**.

2. In the **Name** field, enter a name for the policy.

3. In the **Policy** list, from the list, select **Selectors**.

4. In the **ID** column, select the selector from step 7.

5. Beneath the **No** list, click **Continue**.

6. In the **Yes** list, select the HTML adapter from step 2.

7. Beneath the **Fail** list, click **Done**.

8. From the **Success** list, select the PingID Adapter from step 4.

9. Beneath your PingID Adapter instance, click **Options**.

10. In the **Incoming User ID** window, from the **Source** list, select the HTML adapter from step 2. From the **Attribute** list, select **username**.

11. Beneath the **Fail** list, click **Done**.

12. From the **Success** list, select the policy contract from step 5.

    ![A screen capture of the Policy section with a completed configuration as described in the preceding steps.](_images/etw1603144361293.png)

13. Click **Contract Mapping**.

14. On the **Contract Fulfillment** tab, from the **Source** list, select your HTML adapter. From the **Value** list, select **username**.

15. Click **Next** until you reach the **Summary** tab, and then click **Done**.

16. Click **Done** and then in the **Authentication Policies** window, click **Save**.

## Testing your connection

### Steps

1. In PingFederate, go to **Applications > Integration > SP Connections**, and click your SP connection.

2. On the **Activation & Summary** tab, verify that the green toggle switch is selected. Click the **SSO Application Endpoint** link.

3. Sign on as a user with the credentials created in step 1c.

   #### Result:

   When a user signs on for the first time, they are prompted to install PingID and register their device. If the user is registered, they are prompted to authenticate using PingID.

---

---
title: Setting up an authentication flow that includes MFA (PingOne for Enterprise and PingID)
description: You can create an authentication flow that uses multi-factor authentication (MFA) with PingOne for Enterprise and PingID.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_set_up_authn_flow_mfa_p14e_pid
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_set_up_authn_flow_mfa_p14e_pid.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2025
section_ids:
  steps: Steps
---

# Setting up an authentication flow that includes MFA (PingOne for Enterprise and PingID)

You can create an authentication flow that uses multi-factor authentication (MFA) with PingOne for Enterprise and PingID.

## Steps

1. In PingOne for Enterprise, create an MFA policy.

   Learn more in [Create or update an authentication policy](https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_create_update_authentication_policy.html).

2. To refine your secondary authentication, configure PingID policies.

   Learn more in [Web authentication policy configuration](https://docs.pingidentity.com/pingid/pingid_service_management/pid_web_authentication_policy_configuration.html).

3. Apply MFA to the PingOne for Enterprise admin portal.

   Learn more in [Configure SSO to the PingOne for Enterprise admin portal with multi-factor authentication](https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_configure_sso_admin_portal.html).

---

---
title: Setting up and testing a custom authentication policy
description: Authentication policies are used in PingFederate to implement complex authentication requirements. This document explains how to create a new custom authentication policy in PingFederate, and then test the policy.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_set_up_test_custom_authn_policy
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_set_up_test_custom_authn_policy.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2025
page_aliases: ["workforce_use_cases:htg_set_up_test_custom_authn_policy_create_pf_policy.adoc", "workforce_use_cases:htg_set_up_test_custom_authn_policy_test_pf_policy.adoc"]
section_ids:
  component: Component
  creating-a-custom-authentication-policy-in-pingfederate: Creating a custom authentication policy in PingFederate
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  result: Result:
  testing-a-custom-authentication-policy-in-pingfederate-html-form-with-pingid-mfa: Testing a custom authentication policy in PingFederate (HTML Form with PingID MFA)
  before-you-begin-2: Before you begin
  about-this-task-2: About this task
  steps-2: Steps
  result-2: Result:
---

# Setting up and testing a custom authentication policy

Authentication policies are used in PingFederate to implement complex authentication requirements. This document explains how to create a new custom authentication policy in PingFederate, and then test the policy.

## Component

PingFederate 10.0 or later

## Creating a custom authentication policy in PingFederate

Build and deploy a simple example of a custom authentication policy in PingFederate when there are multiple user types that need different authentication flows.

### Before you begin

Make sure you have the following:

* PingFederate 10 or later with administrator access to web console

* PingID for multi-factor authentication (MFA)

* HTML Form identity provider (IdP) adapter

* Simple password credential validator (PCV)

* A second SimpleForm (HTML Form adapter) instead of PingID

* IdP connection

* Selector

### About this task

Authentication policies are an optional configuration in PingFederate and help administrators implement complex authentication requirements.

A simple example of a custom authentication policy is having PingID act as a second-factor authentication event that triggers after a username and password form.

|   |                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Consider a custom policy when there are multiple user types that need different authentication flows, or if you want to chain together two types of authenticators, such as username and password with MFA. |

### Steps

1. In the PingFederate administrative console, go to **Authentication > Policies > Policies**.

2. In the **Authentication Policies** window, click **Add Policy**.

3. In the **Name** field, enter a policy name.

4. In the **Description** field, enter a description.

5. In the **Policy** list, select a previously created configuration:

   #### Choose from:

   * **IdP Adapter**

   * **IdP Connection**

   * **Selector**

6. In the **Fail** field, click **Done**.

   This means if the user fails authenticating the SimpleForm, their single sign-on (SSO) session ends.

7. From the **Success** list, select the **PingID Adapter**. Additional Fail/Success lists will appear.

   ![Screen capture illustrating the Policy configuration for a authentication policy. The Policy type shows SimpleForm. After this field are the Fail field set to Done and the Success field set to - Adapter. There are two hyperlinks below the Success field: Options and Rules.](_images/ppm1600454406019.png)

   1. Click **Options**.

8. In the **Incoming User ID** window, from the **Source** list, select **Adapter (SimpleForm)** and from the **Attribute** list, select **username**.

   ![Screen capture illustrating the Incoming User ID window in . There are two lists: Source and Attribute. The Source list shows Adapter (SimpleForm) and the Attribute list shows username. Next to the list selection fields is the Clear hyperlink option. At the bottom of the window are the option for Cancel and the Done button.](_images/qpr1600454522166.png)

   1. Click **Done**.

9. After the **Success** list, set the **Fail** and **Success** lists to **Done**.

   ![Screen capture illustrating the configured Policy fields for a custom authentication policy in . The Policy type shows SimpleForm. After this field are the Fail field set to Done and the Success field set to - Adapter. There are two hyperlinks below the Success field: Options and Rules. After the Success field are another pair of Fail and Success fields, both set to Done.](_images/nyz1600454165402.png)

   1. Click **Done**.

      #### Result:

      The custom policy appears in the **Policies** window in the **Policy** list.

10. To save and enable the new policy, click **Save**.

    ![Screen capture of the Policies window on the Policies tab in with a configured and enabled policy in the Policy list. A green toggle to the right of the policy information indicates the policy is enabled. At the bottom of the image is a hyperlink option to Cancel and the Next and Save buttons.](_images/aip1600454717333.png)

## Testing a custom authentication policy in PingFederate (HTML Form with PingID MFA)

Test the custom authentication policy you created in PingFederate.

### Before you begin

Set up a service provider (SP) connection.

### About this task

This requires an SP connection. This example uses the website HTTP\_BIN as a sample application that PingFederate sends the user to after the custom authentication policy has completed successfully.

### Steps

1. Locate an SP Connection that you configured previously to leverage the custom authentication policy.

   1. Go to **Applications > SP Connections > SP Connection > Activation & Summary**.

2. Click the **SSO Application Endpoint**.

   ![Screen capture illustrating the SSO Application Endpoint URL on the SP Connection Actiation & Summary tab in .](_images/jny1600455071838.png)

   #### Result:

   The **Sign On** window appears.

3. Enter a valid **Username** and **Password** based on your SimpleForm and SimplePCV settings.

   1. Click **Sign On**.

      ![Screen capture illustrating the Sign On window redirect from the SSO Application Endpoint.](_images/rav1600455279388.png)

4. Approve the sign-on request using multi-factor authentication (MFA), such as your mobile push.

   ![Screen capture illustrating the MFA push notification.](_images/zec1600455392649.png)

   |   |                                                                                                                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | * If you entered a username and password combination that doesn't authenticate, an error message will display.

   * If you entered a recognized user in the form, but the user has not yet enrolled in PingID, a registration window will display. |

---

---
title: Setting up Kerberos authentication in PingFederate
description: Set up a Kerberos authentication adapter in PingFederate for a seamless user authentication experience from a Windows machine to your applications.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_set_up_kerberos_authn_pf
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_set_up_kerberos_authn_pf.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 15, 2022
page_aliases: ["workforce_use_cases:htg_set_up_kerberos_authn_pf_config_realm.adoc", "workforce_use_cases:htg_set_up_kerberos_authn_pf_config_idp_adapter.adoc"]
section_ids:
  component: Component
  configure-ad-domain-kerberos-realm: Configuring the Active Directory domain/Kerberos realm
  steps: Steps
  configuring-the-idp-adapter: Configuring the IdP adapter
  before-you-begin: Before you begin
  steps-2: Steps
---

# Setting up Kerberos authentication in PingFederate

Set up a Kerberos authentication adapter in PingFederate for a seamless user authentication experience from a Windows machine to your applications.

This allows your user to access connected applications in PingFederate seamlessly from a domain-joined Windows machine without being prompted for additional authentication credentials. Learn more on PingFederate in [Introduction to PingFederate](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_intro_to_pf.html).

## Component

PingFederate 10.1

## Configuring the Active Directory domain/Kerberos realm

Configure an Active Directory (AD) domain/Kerberos realm in PingFederate.

### Steps

1. In the PingFederate administrative console, go to **System > Data & Credential Stores > Active Directory Domains/Kerberos Realms**.

2. Click **Add Domain/Realm**.

3. In the **Domain/Realm Name**, **Domain/Realm Username**, and **Domain/Realm Password** fields, enter the appropriate information.

   ![Screen capture of the Active Directory Domains/Kerberos Realms Manage Domain/Realm window showing the required Domain/Realm Name, Domain/Realm Username, and Domain/Realm Password fields.](_images/dyz1612380988895.jpg)

4. Click **Test Domain/Realm Connectivity** to ensure you can establish a connection, and then click **Done**.

5. On the **Manage Domain/Realms** tab, click **Next**.

   ![Screen capture of the Manage Domains/Realms tab.](_images/nau1612381176846.jpg)

## Configuring the IdP adapter

Configure a new Kerberos adapter instance in PingFederate.

### Before you begin

* Ensure you have an [AD domain configured](#configure-ad-domain-kerberos-realm) as a datastore in PingFederate that can be used to validate Kerberos tickets.

* Create a user in Active Directory (AD) who can read from the directory.

### Steps

1. In the PingFederate administrative console, go to **Authentication > IdP Adapters**.

   ![Screen capture of the Authentication window showing the IdP Adapters option as the second option in the first row.](_images/agg1605286135183.png)

2. Click **Create New Instance**.

3. On the **Type** tab, in the **Instance Name** and **Instance ID** fields, enter a name and ID.

4. In the **Type** list, select **Kerberos Adapter**, and then click **Next**.

   ![Screen capture of the Type tab showing the Instance Name, Instance ID, type and Parent Instance fields.](_images/rho1605286348542.png)

5. On the **IdP Adapter** tab, select the **Domain/Realm Name** you used when adding AD as a datastore.

6. Click **Manage Active Directory Domains/Kerberos Realms**

   ![Screen capture of the IdP Adapter tab showing the Domain/Realm Name and Error URL redirect fields.](_images/jrz1605286615664.png)

7. In the **Manage Domain/Realm** window, in the **Domain/Realm Name**, **Domain/Realm Username**, and **Domain/Realm Password** fields, enter the information from your AD environment.

   ![Screen capture of the Manage Domain/Realm window showing the domain/Realm Name, Domain/Realm Username, Domain/Realm Password fields. Below those are the options for Domain Controller/Key Distributions Center Host Names.](_images/ucb1605286702687.png)

8. Click **Test Domain/Realm Connectivity** to test your connection, then click **Done**.

9. On the **IdP Adapter** tab, click **Next**.

10. On the **Extended Contract** tab, click **Next**.

11. On the **Adapter Attributes** tab, select the **Username Pseudonym** checkbox. Click **Next**.

    ![Screen capture of the Adapter Attributes tab showing checkboxes for the option to use Pseudonyms or Mask Log Values for each attribute.](_images/dbk1605287007023.png)

12. On the **Adapter Contact Mapping** tab, click **Next**.

13. On the **Summary** tab, review your entries. Click **Save**.

---

---
title: Setting up password recovery in PingFederate
description: Learn how to set up PingFederate for self-service password reset and account recovery through an HTML Form Adapter.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_pf_password_recovery_setup
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_pf_password_recovery_setup.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2024
page_aliases: ["workforce_use_cases:htg_pf_password_recovery_setup_ldap.adoc", "workforce_use_cases:htg_pf_password_recovery_setup_ldap_pcv.adoc", "workforce_use_cases:htg_pf_password_recovery_setup_html_form_adapter.adoc"]
section_ids:
  component: Component
  create-ldap-datastore-pf: Creating an LDAP datastore in PingFederate
  about-this-task: About this task
  steps: Steps
  creating-an-ldap-pcv-in-pingfederate: Creating an LDAP PCV in PingFederate
  about-this-task-2: About this task
  steps-2: Steps
  example: Example:
  configuring-an-html-form-adapter-instance-in-pingfederate-for-account-recovery-and-password-change: Configuring an HTML Form Adapter instance in PingFederate for account recovery and password change
  about-this-task-3: About this task
  steps-3: Steps
---

# Setting up password recovery in PingFederate

Learn how to set up PingFederate for self-service password reset and account recovery through an HTML Form Adapter.

## Component

PingFederate 10.2

## Creating an LDAP datastore in PingFederate

### About this task

|   |                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These steps provide specific field configurations. You can find comprehensive instructions for configuring an LDAP datastore in [Configuring an LDAP connection](https://cdn-docs.pingidentity.com/archive/pdf/pingfederatebridge/pingfederatebridge-102.pdf#page=124) (page 124). |

To create an LDAP datastore in PingFederate:

### Steps

1. Go to **System > Data & Credential Stores > Data Stores**.

2. Click **Add New Data Store** to open the **Data Store** configuration window.

3. On the **Data Store Type** tab, in the **Type** list, select **Directory (LDAP)**.

4. Complete the remaining LDAP datastore configuration settings.

5. On the **Summary** tab, click **Save**.

## Creating an LDAP PCV in PingFederate

### About this task

|   |                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | These steps include specific field configurations. You can find comprehensive instructions for configuring an LDAP PCV instance in [Configuring the LDAP Username Password Credential Validator](https://cdn-docs.pingidentity.com/archive/pdf/pingfederatebridge/pingfederatebridge-102.pdf#page=136) (page 136). |

To create an LDAP password credential validator (PCV) in PingFederate:

### Steps

1. Go to **System > Data & Credential Stores > Password Credential Validators**.

2. On the **Type** tab, in the **Instance Name** list, select the LDAP datastore you created in [Creating an LDAP datastore in PingFederate](#create-ldap-datastore-pf).

3. In the **Type** list, select **LDAP Username Password Credential Validator**. Click **Next**.

4. On the **Instance Configuration** tab:

   1. Configure the **Search Base** field.

   2. Configure the **Search Filter** field.

      #### Example:

      For example, `sAMAccountName=${username}` for Active Directory and `uid=${username}` for Oracle Directory Server (ODS) and PingDirectory.

   3. Click **Show Advanced Fields**.

   4. Configure the **Display Name Attribute**, **Mail Attribute**, **SMS Attribute**, **PingID Username Attribute**, and **Mail Verified Attribute** fields.

   5. Configure the **Mail Search Filter**, **Username Attribute**, and **Mail Verified Attribute** fields for username recovery.

   6. For detailed password requirements, select the **Enable PingDirectory Detailed Password Policy Requirement Messaging** checkbox.

      |   |                                                                                                                                                                                                                          |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | Learn more about each field in step 3 of [Configuring the LDAP Username Password Credential Validator](https://cdn-docs.pingidentity.com/archive/pdf/pingfederatebridge/pingfederatebridge-102.pdf#page=136) (page 136). |

5. Click **Next**.

6. On the **Summary** tab, click **Save**.

## Configuring an HTML Form Adapter instance in PingFederate for account recovery and password change

### About this task

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These steps include specific field configurations. For comprehensive instructions for configuring this adapter instance, learn more in [Configuring an HTML Form Adapter instance](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-102.pdf#page=286) (page 286).When connecting to an Active Directory server, you must secure the datastore connection using LDAPS because Active Directory requires this level of security to allow password changes. |

To configure an HTML Form Adapter instance to enable account recovery and password change:

### Steps

1. Go to **Authentication > Integration > IdP Adapters > Create New Instance** and click the **IdP Adapter** tab.

2. Select the **Allow Password Changes** checkbox.

   |   |                                                       |
   | - | ----------------------------------------------------- |
   |   | An LDAP service account is used for password changes. |

3. To allow a password expiring message, select the **Show Password Expiring Warning** checkbox.

4. In the **Password Reset Type** field, click a method to use for self-service password reset.

   |   |                                                                                        |
   | - | -------------------------------------------------------------------------------------- |
   |   | To enable account recovery, you must select a password reset type other than **None**. |

   **Table 1. Password reset type and configuration requirements**

   | Self-service password reset option                     | Configuration requirements                                                                                                                                                                                                                                                                                                                                                                                          |
   | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Authentication Policy**                              | To enable this option, in the **Password Reset Policy Contract** list, select a policy.                                                                                                                                                                                                                                                                                                                             |
   | **Email One-Time Link** or **Email One-Time Password** | 1. In the **Notification Publisher** list, select an option or, to configure a new notification publisher, click **Manage Notification Publishers**

   2. In your LDAP password credential validator instance, on the **Instance Configuration** tab, enter values for the **Display Name Attribute** and **Mail Attribute** fields.                                                                                  |
   | **PingID**                                             | 1) Upload the PingID properties file for the PingID reset option.

   2) Configure the **PingID Username Attribute** field in the LDAP password credential validator.                                                                                                                                                                                                                                                  |
   | **Text Message**                                       | 1. Click **Manage SMS Provider Settings** to add an SMS Provider and enter values for the**Account SID**,**Auth Token**, and **From Number** fields. Click **Save**.

      &#xA;&#xA;Create a Twilio trial account to get an Account SID, Auth Token, and From Number.

   2. In your LDAP password credential validator instance, on the **Instance Configuration** tab, enter a value for the **SMS Attribute** field. |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When connecting to PingDirectory or Oracle Directory Server, administrators should configure proxied authorization for the service account on the directory server for account recovery. This allows PingFederate to request self-service password reset operations under the identity as the user. Otherwise, the service account's identity is used instead if a user's password is expired. |

5. To allow users with a locked account to unlock the account using the self-service password reset type, select the **Account Unlock** checkbox.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Access to the access control instruction (ACI) is required for PingDirectory account unlock.To enable self-service account unlock for an HTML Form Adapter instance that uses a PingDirectory datastore, administrators must configure the account usability control or ACI for the service account on the directory server when connecting PingFederate to PingDirectory.Learn more in [Configuring the account usability control ACI](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-100.pdf#page=182) (page 182) and [Managing Access Control](https://cdn-docs.pingidentity.com/archive/pdf/pingdirectory/pingdirectory-81.pdf#page=782) (page 782). |

6. To allow users to recover their username when using the HTML Form Adapter instance as they initiate single sign-on (SSO) requests and are prompted to enter their username and password, select the **Enable Username Recovery** checkbox.

   |   |                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This setting requires:- A notification publisher instance

   - Configured **mail search filter** and **username attribute** fields in the LDAP password credential validator |

7. Complete the remaining configuration tab settings, and then click **Next**.

8. On the **Summary** tab, click **Save**.

---

---
title: Setting up passwordless authentication in PingOne
description: Learn how to set up passwordless authentication and eliminate the need for your users to enter a password. Passwordless authentication is a quick and easy configuration where end users sign on with a paired multi-factor authentication (MFA) device.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_p1_passwordless_authn_setup
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_p1_passwordless_authn_setup.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2025
page_aliases: ["workforce_use_cases:htg_p1_passwordless_authn_setup_policy_p1.adoc", "workforce_use_cases:htg_p1_passwordless_authn_setup_no_paired_device.adoc", "workforce_use_cases:htg_p1_passwordless_authn_setup_add_policies_app.adoc", "workforce_use_cases:htg_p1_passwordless_authn_setup_testing.adoc"]
section_ids:
  creating-a-passwordless-authentication-policy-in-pingone: Creating a passwordless authentication policy in PingOne
  before-you-begin: Before you begin
  steps: Steps
  creating-an-authentication-policy-for-users-without-a-paired-mfa-device: Creating an authentication policy for users without a paired MFA device
  steps-2: Steps
  adding-the-authentication-policies-to-an-application: Adding the authentication policies to an application
  steps-3: Steps
  testing-the-configuration: Testing the configuration
---

# Setting up passwordless authentication in PingOne

Learn how to set up passwordless authentication and eliminate the need for your users to enter a password. Passwordless authentication is a quick and easy configuration where end users sign on with a paired multi-factor authentication (MFA) device.

In this configuration, a user without a paired MFA device can still authenticate with their credentials.

## Creating a passwordless authentication policy in PingOne

### Before you begin

Configure the application in PingOne that will use passwordless authentication.

### Steps

1. Go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add Policy**.

3. In the **Policy Name** field, enter a name for your policy.

4. In the **Step Type** list, select **Multi-factor Authentication**.

5. In the **Available Methods** section, select the allowed MFA methods for end users.

   The following image shows the available MFA methods.

   ![A screen capture of the admin console showing all of the MFA checkboxes. Every checkbox in the Available Methods section is selected.](_images/dzn1619047089030.png)

   |   |                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------ |
   |   | To enable **Mobile Applications**, go to **Applications > p1-nav-connected-applications}** and configure a native application. |

6. In the **None Or Incompatible Methods** section, select **Bypass**.

   |   |                                                                            |
   | - | -------------------------------------------------------------------------- |
   |   | If **Block** is selected, users without a paired MFA device can't sign on. |

7. In the **Required When** section, select when re-authentication will be required, such as when a user is accessing the application from an out-of-range IP address.

8. Click **Save**.

## Creating an authentication policy for users without a paired MFA device

### Steps

1. On the **Authentication Policies** page, click **[icon: plus, set=fa]Add Policy**.

2. In the **Policy Name** field, enter a name for your policy.

3. From the **Step Type** list, select **Login**.

4. **Optional:** Select any additional options.

5. Click **Save**.

## Adding the authentication policies to an application

### Steps

1. Go to **Applications > Applications** and expand the application that you want to add passwordless authentication to.

2. On the **Policies** tab, in the **All Policies** list, click the **Plus** ([icon: plus, set=fa]) icon for your backup policy, and then click the **Plus** ([icon: plus, set=fa]) icon for your passwordless policy to add them to the **Applied Policies** list.

   |   |                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Because the most recently added policy is added as the primary policy, verify that the passwordless policy is listed first in the **Applied Polices** list. |

   ![A screen capture of the console showing the Policies tab when editing an application.](_images/egi1619052769676.png)

3. Click **Save**.

## Testing the configuration

To test the configuration:

* Initiate an authorization request if your application uses OpenID Connect (OIDC).

* Initiate a single sign-on (SSO) request if your application uses SAML.

PingOne prompts for a username.

* If the user has a paired device, PingOne prompts them to complete MFA depending on the allowed methods. After they authenticate, they're redirected to the target application.

* If the user doesn't have a paired device, PingOne prompts them to sign on with a username and password and then prompts them to pair an MFA device.

---

---
title: Setting up PingFederate as a FedHub
description: Configuring PingFederate as an identity bridge or FedHub (SAML Chaining) allows you to manage external identities and facilitate access to applications across the enterprise community.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_set_up_pf_as_fedhub
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_set_up_pf_as_fedhub.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2025
page_aliases: ["workforce_use_cases:htg_set_up_pf_as_fedhub_flow.adoc", "workforce_use_cases:htg_set_up_pf_as_fedhub_contract.adoc", "workforce_use_cases:htg_set_up_pf_as_fedhub_sp_connection.adoc", "workforce_use_cases:htg_set_up_pf_as_fedhub_ip_connection.adoc", "workforce_use_cases:htg_set_up_pf_as_fedhub_authn_policy.adoc"]
section_ids:
  component: Component
  creating-a-service-provider-connection: Creating a service provider connection
  about-this-task: About this task
  steps: Steps
  creating-an-identity-provider-connection: Creating an identity provider connection
  about-this-task-2: About this task
  steps-2: Steps
  creating-an-authentication-policy-in-pingfederate: Creating an authentication policy in PingFederate
  before-you-begin: Before you begin
  about-this-task-3: About this task
  steps-3: Steps
  result: Result
---

# Setting up PingFederate as a FedHub

Configuring PingFederate as an identity bridge or FedHub (SAML Chaining) allows you to manage external identities and facilitate access to applications across the enterprise community.

## Component

PingFederate 10.3

## Creating a service provider connection

### About this task

Create an SP connection in PingFederate using the policy contract created in the previous task.

### Steps

1. Go to **Applications > Integration > SP Connections** and then click **Create Connection**.

2. On the **Connection Template** tab, select whether to use a template for this connection, and then click **Next**.

3. On the **Connection Type** tab, select the **Browser SSO Profiles** checkbox, and in the **Protocol** list, select **SAML 2.0**. Click **Next**.

4. On the **Connection Options** tab, select the option that applies to the connection. Click **Next**.

5. On the **Import Metadata** tab, import metadata from a file or URL if desired. Click **Next**.

6. On the **General Info** tab, complete the **Partner's Entity ID** and **Connection Name** fields. Click **Next**.

7. On the **Browser SSO** tab, click **Configure Browser SSO**, and then select the applicable SSO profiles. Click **Next**.

8. On the **Assertion Lifetime** tab, configure the assertion lifetime. Click **Next**.

9. On the **Assertion Creation** tab, click **Configure Assertion Creation**.

10. On the **Identity Mapping** tab, select the type of name identifier that you will send to the SP, and then click **Next**.

11. On the **Attribute Contract** tab, extend the contract if desired. Click **Next**.

12. On the **Authentication Source Mapping** tab, click **Map New Authentication Policy**.

13. From the **Authentication Policy Contract** list, select the policy contract you created in step 1. Click **Next**.

14. On the **Mapping Method** tab, choose to retrieve additional values from your data stores if desired. Click **Next**.

15. On the **Attribute Contract Fulfillment** tab, from the **Source** list, select **Authentication Policy Contract**.

16. From the **Value** list, select a value from the authentication policy contract and then click **Next**.

17. On the **Issuance Criteria** tab, configure conditional authorization if desired, and then click **Next**.

18. On the **Summary** tab, click **Done**.

19. Click **Next** and **Done** until you reach the **Protocol Settings** tab. Click **Configure Protocol Settings**.

20. On the **Assertion Consumer Service URL** tab, from the **Binding** list, select a binding, and in the **Endpoint URL** field, enter the endpoint URL. Click **Add** and then click **Next**.

21. Click **Next** until you reach the **Credentials** tab, configuring the desired settings.

22. On the **Credentials** tab, click **Configure Credentials**.

23. On the **Digital Signature Settings** tab, from the **Signing Certificate** list, select a signing certificate. Click **Next** and **Done** until you reach the **Activation & Summary** tab.

24. Click **Save**.

## Creating an identity provider connection

### About this task

Create an IdP connection in PingFederate using the policy contract created in step 1.

Learn more in [Managing IdP connections](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=678) (page 678).

|   |                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | In this connection, PingFederate will act as the SP, and Company B's single sign-on (SSO) provider will act as the IdP. You must have the IdP metadata or metadata information from Company B's SSO administrator. |

### Steps

1. Go to **Authentication > Integration > IdP Connections** and then click **Create Connection**.

2. On the **Connection Type** tab, select the **Browser SSO Profiles** checkbox, and in the **Protocol** list, select **SAML 2.0**. Click **Next**.

3. On the **Connection Options** tab, select the option that apply to the connection. Click **Next**.

4. On the **Import Metadata** tab, import metadata from a file or URL if desired. Click **Next**.

5. On the **General Info** tab, complete the **Partner's Entity ID** and **Connection Name** fields. Click **Next**.

6. On the **Browser SSO** tab, click **Configure Browser SSO**, and then select the applicable SSO profiles. Click **Next**.

7. On the **User-Session Creation** tab, click **Configure User-Session Creation**, and then select **No Mapping**. Click **Next**.

8. On the **Attribute Contract** tab, extend the contract if desired. Click **Next**.

9. On the **Target Session Mapping** tab, click **Map New Authentication Policy**, and from the **Authentication Policy Contract** list, select the policy contract you created in step 1. Click **Next**.

10. On the **Attribute Retrieval** tab, select the type of attribute retrieval, and then click **Next**.

11. On the **Contract Fulfillment** tab, from the **Source** list, select a source to fulfill the policy contract, and from the **Value** list, select a value from the source. Click **Next**.

12. On the **Issuance Criteria** tab, you can configure conditional authorization if desired. Click **Next**, and then on the **Summary** tab, click **Done**.

13. Click **Next** and **Done** until you reach the **Protocol Settings** tab. Click **Configure Protocol Settings**.

14. On the **SSO Service URLs** tab, from the **Binding** list, select a binding.

15. In the **Endpoint URL** field, enter the endpoint URL. Click **Add** and then click **Next**.

16. On the **Allowable SAML Bindings** tab, select which SAML bindings will receive messages from the IdP. Click **Next**.

17. On the **Artifact Resolver Locations** tab, in the **URL** field, enter the remote party URL that you will use to translate the artifact and get the protocol message. Click **Add** and then **Next**.

    |   |                            |
    | - | -------------------------- |
    |   | You can add multiple URLs. |

18. On the **Overrides** tab, specify a default target URL and an authentication context if desired. Click **Next**.

19. On the **Encryption Policy** tab, specify additional XML encryption for SAML messages if desired. Click **Next**.

20. On the **Signature Policy** tab, specify additional signature requirements if desired. Click **Next**.

21. Click **Next** and **Done** until you reach the **Credentials** tab. Click **Configure Credentials**.

22. On the **Back-Channel Authentication** tab, ensure that security settings are properly configured for your selected bindings, and then click **Next**.

23. On the **Signature Verification Settings** tab, click **Manage Signature Verification Settings** and follow the on-screen instructions. When you are returned to this tab, click **Next** and then **Done**.

24. Click **Next** and **Done** when you reach the **Activation & Summary** tab.

## Creating an authentication policy in PingFederate

### Before you begin

**Component**

* PingFederate 10.3

Before creating the policy, you must have an Identifier First Adapter instance and an HTML Form Adapter configured. Learn more in [Configuring an Identifier First Adapter instance](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=312) and [Configuring an HTML Form Adapter instance](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=291).

### About this task

Learn more on authentication policies in [Defining authentication policies](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=219).

### Steps

1. Go to **Authentication > Policies > Policies**, and then click **Add Policy**.

2. In the **Policy** list, select **IdP Adapters** and then select your Identifier First Adapter instance.

3. Click **Rules** and configure the sign-on flow for users according to the following example.

   This determines which IdP the user authenticates against.

   ![A screen capture of the Rules modal showing four columns: Attribute Name, Condition, Value, and Result.](_images/tww1600460722222.png)

4. Configure the authentication policy according to the following example.

   ![A screen capture of the Policy window. Company A and Company B have different authentication flows, defined by the respective Fail and Success lists. Company A users will sign on with credentials against Company A's data store. Company B users will be redirected to their IdP sign-on page.](_images/wyi1604452822015.png)

5. Click **Done**.

### Result

When users from Company B sign-on using their IdP, the IdP sends the assertion to the PingFederate SP endpoint. PingFederate provides the necessary attributes to the IdP endpoints, which are then used to generate an authentication response to Company A's application.

---

---
title: Setting up your PingOne Dock
description: The PingOne Dock gives your users one-click, single sign-on (SSO) access to the applications and other service providers (SPs) you authorize them to use.
component: solution-guides
page_id: solution-guides:workforce_use_cases:htg_p1_dock_setup
canonical_url: https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_p1_dock_setup.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2025
page_aliases: ["workforce_use_cases:htg_p1_dock_setup_access_directory.adoc", "workforce_use_cases:htg_p1_dock_setup_config_third_party_ip.adoc", "workforce_use_cases:htg_p1_dock_setup_config_dock.adoc", "workforce_use_cases:htg_p1_dock_setup_branding.adoc"]
section_ids:
  configure-user-ac-pingone-dir: Configuring user access control for PingOne Directory
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  choose-from: Choose from:
  result-2: Result:
  troubleshooting: Troubleshooting:
  configure-user-ac-third-party-ip: Configuring user access control for a third-party identity provider
  before-you-begin-2: Before you begin
  about-this-task-2: About this task
  steps-2: Steps
  result-3: Result:
  configuring-the-pingone-dock: Configuring the PingOne Dock
  about-this-task-3: About this task
  steps-3: Steps
  adding-your-branding-to-the-pingone-dock: Adding your branding to the PingOne Dock
  about-this-task-4: About this task
  steps-4: Steps
  choose-from-2: Choose from:
  next-steps: Next steps
---

# Setting up your PingOne Dock

The PingOne Dock gives your users one-click, single sign-on (SSO) access to the applications and other service providers (SPs) you authorize them to use.

To get started with the PingOne Dock, you assign user groups, configure dock settings, and personalize branding.

## Configuring user access control for PingOne Directory

### Before you begin

To set up your PingOne Dock, you must have the following:

* A PingOne account

  If you don't have a PingOne account, register at <https://admin.pingone.com/web-portal/register>.

* A connection between PingOne and an identity provider (IdP)

  Learn more about IdPs and connecting to them in [Connecting to an identity repository](https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_connecting_idp.html).

### About this task

|   |                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | These steps only apply if you are using the PingOne Directory. For all other identity providers, learn more in [Configuring user access control for a third-party identity provider](#configure-user-ac-third-party-ip). |

PingOne uses user groups to control user access to applications. As an administrator, you create user groups, manage the group's application permissions, and add or remove users to grant or limit their access to those applications.

To display application icons in a user's dock, map at least one application to a group.

### Steps

1. In PingOne, go to **Users > User Directory > Groups**.

2. Click **Add Group**.

   #### Result:

   The **New Group** form opens.

3. In the **Name** field, enter a name for this group.

4. On the **Directly Applied Role** line, grant user directory access to this group.

   #### Choose from:

   * To prevent users in this group from viewing or modifying the user directory, click **No Access**.

   * To allow users in this group to view user and group directory information, click **User Reader**.

   * To allow users in this group to create and modify user directory information, and to view group directory information, click **User Manager**.

   * To allow users in this group to create and modify user directory information, create and modify groups, and change group membership, click **Group and Entitlement Manager**.

5. Click **Save**.

   #### Result:

   The new user group appears in the **Groups** list.

6. Go to **Users > User Directory > Users**.

7. For each user that you want to add:

   1. Click **Edit**.

   2. Under **Memberships**, click **Add**.

   3. In the **Add Group Membership** form, select the checkbox for each group to add the user to.

8. Go to **Applications > My Applications**.

9. For each application you want to grant group access to:

   1. Click the name of the application to expand it.

   2. Click **Edit**.

   3. Click **Continue to Next Step** on each tab until you reach the **Group Access** tab.

   4. To grant group access to this application, click **Add**.

      #### Troubleshooting:

      Empty groups do not appear in the **Group Access** list. If your group does not appear in the list, go to step 7 to add users.

10. Click **Continue to Next Step**.

11. Click **Finish**.

## Configuring user access control for a third-party identity provider

### Before you begin

To set up your PingOne Dock, you must have the following:

* A PingOne account

  If you don't have a PingOne account, register at <https://admin.pingone.com/web-portal/register>.

* A connection between PingOne and an identity provider (IdP)

  Learn more about IdPs and connecting to them in [Connecting to an identity repository](https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_connecting_idp.html).

### About this task

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These steps apply only to third-party identity providers. If you are using PingOne Directory, learn more in [Configuring user access control for PingOne Directory](#configure-user-ac-pingone-dir). |

PingOne user groups control user access to applications. As an administrator, you create user groups, manage the group's application permissions, and add or remove users to grant or limit their access to those applications.

To display application icons in a user's dock, map at least one application to a group.

### Steps

1. Go to **Users > User Groups**.

2. Click **Add New Group**.

3. In the **New Group Name** field, enter a name for the group.

4. For each application to allow this group to access, select the corresponding checkbox.

5. Click **Save**.

   #### Result:

   The subsequent **User Groups** tab displays only the group you just created.

   |   |                                                                            |
   | - | -------------------------------------------------------------------------- |
   |   | To view all of your user groups, click the **User Groups** tab to refresh. |

## Configuring the PingOne Dock

### About this task

You can change the default settings of the PingOne Dock to customize your users' experience or comply with your security requirements.

The following settings are optional.

### Steps

1. Go to **Setup > Dock**.

2. In the **Company ID** field, enter a company ID.

   The entry in this field becomes part of your PingOne Dock URL, which is displayed in the **PingOne Dock URL** field.

3. From the **Maximum Session Lifetime** list, select the session duration before PingOne signs a user out.

4. From the **Session Idle Timeout** list, select the amount of time before PingOne signs off an idle user.

   The default value of **- -** disables this feature.

5. Select the **Enable Basic SSO** box to enable users to vault passwords using the PingOne browser extension.

6. In the **User Support Message** field, enter a message to diplay when a user clicks the **Need Help?** link on the left navigation pane of the PingOne Dock.

7. For each attribute you want to map, select the attribute to map it to from the list.

   Your IdP automatically maps some attributes that can't be changed afterward. The pre-mapped attributes vary depending on your IdP.

   Learn more about advanced attribute mapping in [Assign advanced attribute mappings](https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_assign_advanced_attribute_mappings.html).

8. Click **Save**.

## Adding your branding to the PingOne Dock

### About this task

You can customize the colors, logos, and images of the PingOne Dock to match your organization's branding.

Learn more about each part of the dock in [Introducing the PingOne Dock](https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_introducing_p14e_dock.html)

### Steps

1. Go to **Setup > Branding > Dock**.

2. On the **Logo for Dock** line, select the image you want to use for the upper left corner of the dock.

   #### Choose from:

   * To use your existing logo image, click **Use Corporate Logo**.

     |   |                                                                 |
     | - | --------------------------------------------------------------- |
     |   | To upload a corporate logo image, go to **Account > Branding**. |

   * To upload a new image, click **Custom** and then click the **Image** icon.

3. In the **Main Area** section, customize the image and font for the main area of your dock.

   1. Under **Background**:

      * To apply the default white background, click **None**.

      * To upload a background image, click **Image**.

      * To enter or select a solid background color, click **Color**.

   2. Click the **Font Color** color picker and enter or select a color for the text in the main area.

   3. Under the **Drop Shadow** line, click **Yes** to apply a drop shadow to the text in the main area.

4. In the **Left Navigation Colors** section, enter or select the colors for the left navigation pane of your dock.

5. In the **Search Color** section, enter or select the colors for the search bar at the top of your dock.

6. In the **Sign Off** section, customize the screen that displays to users when they sign off from your dock.

   1. Under **Main Background**:

      * To apply the default white background, click **None**.

      * To upload a background image, click **Image**.

      * To enter or select a solid background color, click **Color**.

   2. From the **Form Color** picker, enter or select the color for the sign off page form.

   3. From the **Font Color** picker, enter or select the color for the text in the sign off page form.

   4. From the **Link Color** picker, enter or select the color for the link back to the sign on page.

   5. In the **Page Text** field, enter the text that appears in the sign off page form.

7. Click **Save**.

### Next steps

To view your applied changes, go to **Setup > Dock** and click the **PingOne Dock URL** to sign in as a user.
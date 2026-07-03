---
title: Configuring SAML SSO with Atlassian Cloud and PingFederate
description: The following table details the required and optional attributes to be configured in the assertion attribute contract.
component: configuration_guides
page_id: configuration_guides:atlassian_cloud:config_saml_atlassiancloud_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/atlassian_cloud/config_saml_atlassiancloud_pf.html
revdate: May 15, 2024
section_ids:
  about-this-task: About this task
  create-a-pingfederate-sp-connection-for-atlassian-cloud: Create a PingFederate SP connection for Atlassian Cloud
  configure-the-pingfederate-idp-connection-for-atlassian-cloud: Configure the PingFederate IdP connection for Atlassian Cloud
---

# Configuring SAML SSO with Atlassian Cloud and PingFederate

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name                                                    | Description    | Required / Optional |
| ----------------------------------------------------------------- | -------------- | ------------------- |
| `SAML_SUBJECT`                                                    | Email Address  | Required            |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname` | First Name     | Required            |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`   | Surname        | Required            |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name`      | ID (not email) | Required            |

The following table details the references that are used within this guide that are environment specific. Replace these with the suitable value for your environment.

| Reference     | Description                                                                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *TenantSSOID* | Tenant single sign-on (SSO) ID, retrieved from Atlassian Cloud SAML Single Sign-on configuration as part of EntityID and Assertion Consumer Service (ACS) URL. |

## Create a PingFederate SP connection for Atlassian Cloud

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested, and is provided as an example. Additional steps might be required. |

1. In Atlassian Cloud, go to **Security → SAML Single Sign-on** and sign on to Atlassian Cloud as an administrator.

2. Make a note of the **Entity ID** and **ACS URL** values.

   You will need these later.

3. Sign on to the PingFederate administrative console.

4. Using the details retrieved from the application UI:

   * Configure using **Browser SSO** profile **SAML 2.0**.

   * Enable the **IDP-Initiated SSO** SAML profile.

   * Enable the **SP Initiated SSO** SAML profile.

   * In **Assertion Creation → Attribute Contract**, set the **Subject Name Format** to `urn:oasis:names:tc:SAML:2.0:attrname-format:emailAddress`.

   * Add the following attributes as type `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`:

     * `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`

     * `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`

     * `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name`

   * In **Assertion Creation → Attribute Contract Fulfilment**:

     * Map attribute **SAML\_SUBJECT** to the attribute **mail**.

     * Map attribute **givenname** to the attribute **givenName**.

     * Map attribute **surname** to the attribute **sn**.

     * Map attribute **name** to the non-email unique identifier, such as **uid**.

   * In **Protocol Settings**:

     * For **Assertion Consumer Service URL**, enter the consumer service URL retrieved from Atlassian and configure as index 0.

     * For **Allowable SAML Bindings**, enable **Redirect** and **POST**.

5. Export the signing certificate public key.

   ![SP Connections page](_images/xss1619229348270.png)

## Configure the PingFederate IdP connection for Atlassian Cloud

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

1. Sign in to Atlassian Cloud as an administrator.

2. Go to **Security → SAML Single Sign-on**.

3. Click **Add SAML Configuration**.

4. Enter the following details:

   * In the **Identity Provider Entity ID** field, enter the **Issuer** value for your PingFederate environment configuration.

   * In the **Identity Provider SSO URL** field, enter the SSO URL for your PingFederate environment configuration.

   * In a text editor, open the certificate you downloaded during the PingFederate and paste the contents of the certificate into the **Public x509 Certificate** field.

5. Click **Save Configuration**.

---

---
title: Configuring SAML SSO with Atlassian Cloud and PingOne for Enterprise
description: The following table details the required and optional attributes to be configured in the assertion attribute contract.
component: configuration_guides
page_id: configuration_guides:atlassian_cloud:config_saml_atlassiancloud_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/atlassian_cloud/config_saml_atlassiancloud_p1.html
revdate: May 20, 2024
section_ids:
  about-this-task: About this task
  create-a-pingone-for-enterprise-application-for-atlassian-cloud: Create a PingOne for Enterprise Application for Atlassian Cloud
  result: Result:
  configure-the-pingone-for-enterprise-idp-connection-for-atlassian-cloud: Configure the PingOne for Enterprise IdP connection for Atlassian Cloud
---

# Configuring SAML SSO with Atlassian Cloud and PingOne for Enterprise

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name                                                    | Description    | Required / Optional |
| ----------------------------------------------------------------- | -------------- | ------------------- |
| `SAML_SUBJECT`                                                    | Email Address  | Required            |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname` | First Name     | Required            |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`   | Surname        | Required            |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name`      | ID (not email) | Required            |

The following table details the references that are used within this guide that are environment specific. Replace these with the suitable value for your environment.

| Reference     | Description                                                                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *TenantSSOID* | Tenant single sign-on (SSO) ID, retrieved from Atlassian Cloud SAML Single Sign-on configuration as part of EntityID and Assertion Consumer Service (ACS) URL. |

## Create a PingOne for Enterprise Application for Atlassian Cloud

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested, and is provided as an example. Additional steps might be required. |

1. In Atlassian Cloud, go to **Security → SAML Single Sign-on** and sign on to Atlassian Cloud as an administrator.

2. Make a note of the **Entity ID** and **ACS URL** values.

3. Sign on to PingOne for Enterprise and go to **Applications → Application Catalog**.

4. On the **SAML** tab, in the **Add Application** list, select **Search Application Catalog**.

   ![Screen capture of the admin page My Applications page open to the SAML tab showing the Add Applications list.](_images/iji1619228760221.png)

5. Search for `Atlassian` and then click the **Atlassian Cloud** row.

   ![Screen capture of the admin page Application Catalog tab.](_images/xcb1619228839778.png)

6. Click **Setup**.

7. In the **Signing Certificate** list, select the appropriate signing certificate.

8. Review the steps, and make a note of the **PingOne SaaS ID**, **IdP ID**, **Single Sign-On URL**, and **Issuer** values shown.

   ![Screen capture of the admin page showing the SSO Instructions fields for the Application Catalog.](_images/ssj1619228884932.png)

9. Click **Continue to Next Step**.

10. Enter the following.

    | Attribute     | Directions                        | URL                                                                      |
    | ------------- | --------------------------------- | ------------------------------------------------------------------------ |
    | **ACS URL**   | Enter the ACS URL from step 1b.   | https\://auth.atlassian.com/login/callback?connection=saml-*tenantSSOID* |
    | **Entity ID** | Enter the Entity ID from step 1b. | https\://auth.atlassian.com/saml/*tenantSSOID*                           |

    ![Screen capture of the admin page showing the Connection Configuration steps for the Application Catalog. The ACS URL and Entity ID fields are highlighted in red.](_images/iak1619228914755.png)

11. Click **Continue to Next Step**.

12. Configure the **Attribute Mapping** section.

    | Application Attribute | Identity Bridge Attribute or Literal Value                                                                  |
    | --------------------- | ----------------------------------------------------------------------------------------------------------- |
    | **SAML\_SUBJECT**     | Select a suitable attribute containing the email address.                                                   |
    | **givenname**         | Select a suitable attribute containing the user's first name.                                               |
    | **surname**           | Select a suitable attribute containing the user's last name.                                                |
    | **name**              | Select a suitable attribute containing the user's unique ID.&#xA;&#xA;This should not be the email address. |

    ![Screen capture of the admin page showing the Attribute Mapping fields on the Application Catalog. The Identity Bridge: Attribute or Literal Value column fields are highlighted in red.](_images/ord1619228958620.png)

13. Click **Continue to Next Step**.

14. Update the **Name**, **Description**, and **Category** fields as required.

    ![Screen capture of the admin page showing the App Customization - Atlassian Cloud fields.](_images/isq1619228994607.png)

15. Click **Continue to Next Step**.

16. Add the user groups for the application.

    ![Screen capture of the admin page showing the Group Access fields for the Application Catalog.](_images/lja1619229041156.png)

17. Click **Continue to Next Step**.

18. Review the settings.

19. Copy the **Single Sign-On (SSO) URL** value to a temporary location.

    This is the IdP-initiated SSO URL that you can use for testing.

20. Make a note of the **PingOne Issuer** and **PingOne idpid** values.

    You will use these in the Atlassian Cloud configuration.

    ![Screen capture of the admin page showing the Review Setup fields for the Application Catalog. The idpid and Issuer fields are highlighted in red.](_images/nqh1619229086862.png)

21. On the **Signing Certificate** line, click **Download**. Click **Finish**.

    ![Screen capture of the admin page showing the Review Setup fields for the Application Catalog. The Signing Certificate Download button and the Finish buttons are highlighted.](_images/otl1619229125882.png)

    You will use this in the Atlassian Cloud configuration.

### Result:

![Screen capture of the admin page showing all of the available applications added to an account for My Applications.](_images/zvf1619229148141.png)

## Configure the PingOne for Enterprise IdP connection for Atlassian Cloud

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

1. In Atlassian Cloud, go to **Security → SAML Single Sign-on** and sign on to Atlassian Cloud as an administrator.

2. Click **Add SAML Configuration**.

3. Enter the following:

   * In the **Identity Provider Entity ID** field, enter the **Issuer** value from the PingOne for Enterprise configuration.

   * In the **Identity Provider SSO URL** field, enter `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=idpid`, replacing *idpid* with the one from the PingOne for Enterprise configuration.

   * In a text editor, open the certificate you downloaded during the PingOne for Enterprise configuration, and paste the contents of the certificate into the **Public x509 Certificate** field.

4. Click **Save Configuration**.
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

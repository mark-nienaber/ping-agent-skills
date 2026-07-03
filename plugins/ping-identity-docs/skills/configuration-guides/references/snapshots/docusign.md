---
title: Configuring SAML SSO using DocuSign and PingFederate
description: Learn how to enable DocuSign sign on from a PingFederate URL (IdP-initiated sign-on) and direct DocuSign sign on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:docusign:config_saml_docusign_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/docusign/config_saml_docusign_pf.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-docusign: Create a PingFederate SP Connection for DocuSign
  add-the-pingfederate-connection-to-docusign: Add the PingFederate connection to DocuSign
  update-the-entityid-and-acs-url-values-in-pingfederate: Update the EntityID and ACS URL values in PingFederate
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO using DocuSign and PingFederate

Learn how to enable DocuSign sign on from a PingFederate URL (IdP-initiated sign-on) and direct DocuSign sign on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Make sure DocuSign has a valid domain, an organisation created, and is populated with at least one user to test access.

* You must have administrative access to PingFederate and DocuSign.

## Create a PingFederate SP Connection for DocuSign

1. Sign on to PingFederate administration console.

2. Create an SP connection for DocuSign in PingFederate:

   * Configure using **Browser SSO** profile **SAML 2.0**.

   * Set **Partner's Entity ID** to `Placeholder`.

     You will update this value later.

   * Enable the following **SAML Profiles**:

     * **IdP-Initiated SSO**

     * **SP-Initiated SSO**

   * In **Assertion Creation: Attribute Contract**, extend the contract to add attributes named `SAML_NAME_FORMAT`, `surname`, `givenname` and `emailaddress`.

   * In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map **SAML\_SUBJECT**, **surname**, **givenname** and **emailaddress** and map **SAML\_NAME\_FORMAT** to `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`.

   * In **Protocol Settings: Assertion Consumer Service URL**, set **binding** to **POST**, and set **Endpoint URL** to `http://placeholder`.

     You will update the placeholder value later.

   * In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   * In **Credentials: Digital Signature Settings**, select the PingFederate signing certificate.

3. Save the configuration.

4. Export the signing certificate.

5. Export and then open the metadata file, and copy the value of these properties:

   * `entityID`

   * `Location entry` (`https://your value/idp/SSO.saml2`)

## Add the PingFederate connection to DocuSign

1. Sign on to your DocuSign domain as an administrator.

2. In the left navigation pane, select **Identity Providers**, and then click **Add Identity Provider**.

   ![Screen capture of the Docusign Admin portal open to the Identity Providers window with the Add Identity Provider button highlighted in red.](_images/njv1621287978925.png)

3. Configure the following fields.

   | Field                             | Value                                                                               |
   | --------------------------------- | ----------------------------------------------------------------------------------- |
   | **Name**                          | A name for the identity provider.                                                   |
   | **Identity Provider Issuer**      | Enter the **Issue** value from PingID.                                              |
   | **Identity Provider Login URL**   | `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=PingOne IdP ID value` |
   | **Send AuthN Request by**         | Click **POST**.                                                                     |
   | **Select Send Logout Request by** | Click **POST**.                                                                     |

   ![Screen capture of the Add Identity Provider fields for SSO Protocol: SAML 2.0. The Name, Identity Provider Issuer, and Identity Provider Login URL fields are required.](_images/psh1621288267240.png)

4. In the **Custom Attribute Mapping** section, click **Add New Mapping**, and then:

   * In the **Field** list, select **surname**, then enter `surname` in the **Attribute** field.

   * In the **Field** list, select **givenname**, then enter `givenname` in the **Attribute** field.

   * In the **Field** list, select **emailaddress**, then enter `emailaddress` in the **Attribute** field.

5. Click **Save**.

6. Click **Add New Certificate**.

   ![Screen capture of the PingOne identity provider with no current valid certificate. The Add New Certificate button is highlighted in red.](_images/ruf1621288498690.png)

7. Click **Add Certificate**.

   ![Screen capture of the Identity Provider Certificates field with the Add Certificate button highlighted in red.](_images/ogj1621288643739.png)

8. Select the signing certificate that downloaded from PingFederate. Click **Save**.

9. In the **Actions** list for the identity provider that you created, select **Endpoints**.

   ![Screen capture of the Identity Providers list with the PingOne identity provider Actions menu expanded. The Endpoints option is highlighted in red.](_images/pkv1621288741728.png)

10. Copy the **Service Provider Issuer URL** and **Service Provider Assertion Consumer Service URL** values.

    ![Screen capture of the Service Provider Issuer URL and Service Provider Assertion Consumer Service URL fields highlighted in red.](_images/cmz1621288870338.png)

    The DocuSign connection configuration is complete.

    |   |                                                                                                           |
    | - | --------------------------------------------------------------------------------------------------------- |
    |   | After testing, you can set the domain to require IP authentication to remove the DocuSign sign-on screen. |

## Update the EntityID and ACS URL values in PingFederate

1. Sign on to the PingFederate administrative console.

2. Edit the SP connection for DocuSign.

3. Set **Partner's Entity ID** to the DocuSign **Service Provider Issuer URL** value.

4. Set **Assertion Consumer Service URL Endpoint URL** to the **DocuSign Service Provider Assertion Consumer Service URL** value.

5. Save the changes.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO application endpoint for the DocuSign SP connection.

2. Complete PingFederate authentication.

   You're redirected to your DocuSign domain.

   ![Screen capture of the DocuSign domain.](_images/arw1621290347104.png)

## Test the PingFederate SP-initiated SSO integration

1. Go to <https://account.docusign.com>.

2. Enter your email address.

3. Click **Use Company Login**.

4. After you're redirected to PingFederate, enter your PingFederate username and password.

   After successful authentication, you're redirected back to DocuSign.

   ![Screen capture of the DocuSign domain.](_images/arw1621290347104.png)

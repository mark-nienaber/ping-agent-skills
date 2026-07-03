---
title: Configuring SAML SSO with Coupa and PingFederate
description: Learn how to enable Coupa sign-on from a PingFederate URL (IdP-initiated sign-on) and direct Coupa sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:coupa:config_saml_coupa_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/coupa/config_saml_coupa_pf.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  download-the-coupa-metadata: Download the Coupa metadata
  create-a-pingfederate-sp-connection-for-coupa: Create a PingFederate SP connection for Coupa
  add-the-pingfederate-idp-connection-to-coupa: Add the PingFederate IdP Connection to Coupa
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration:
---

# Configuring SAML SSO with Coupa and PingFederate

Learn how to enable Coupa sign-on from a PingFederate URL (IdP-initiated sign-on) and direct Coupa sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate Coupa with at least one user to test access.

* You must have administrative access to PingFederate and Coupa.

## Download the Coupa metadata

1. Sign on to your Coupa Admin organization as an administrator.

2. Go to `https://your_site.coupahost.com/administration/security`.

3. Select the **Sign in using SAML** check box.

4. Click the **Download and import SP metadata** link.

5. Save the Coupa metadata.

## Create a PingFederate SP connection for Coupa

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for Coupa in PingFederate using the Coupa metadata:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

      * Enable the following **SAML Profiles**:

        * **IdP-Initiated SSO**

        * **SP-Initiated SSO**

      * In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map **SAML\_SUBJECT** to the attribute containing a user's email address.

      * In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

      * In **Credentials: Digital Signature Settings** select the PingFederate signing certificate.

3. Save the configuration.

4. Export the signing certificate.

5. Export the metadata file.

## Add the PingFederate IdP Connection to Coupa

1. Sign on to your Coupa Admin organization as an administrator.

2. Go to `https://your_site.coupahost.com/administration/security`.

3. Make sure that the **Sign in using SAML** check box is selected.

4. In the **Upload IdP metadata** section, click **Choose File**.

5. Select the PingFederate metadata file and import it.

6. In the **Certificate** field, upload the PingFederate signing certificate.

7. Click **Save**.

8. Click the **Users** tab and edit the users who will use SAML authentication.

9. Set **Single Sign-On ID** to the value users will use to sign on, for example, their email address.

10. Set **Authentication method** to **SAML**.

11. Click **Save**.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO application endpoint for the Coupa SP connection.

2. Complete PingFederate authentication.

   You're redirected to your Coupa domain.

## Test the PingFederate SP-initiated SSO integration:

1. Go to your Coupa URL.

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to Coupa.

---

---
title: Configuring SAML SSO with Coupa and PingOne for Enterprise
description: Learn how to enable Coupa sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct Coupa sign-on using PingOne for Enterprise (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:coupa:config_saml_coupa_p14e
canonical_url: https://docs.pingidentity.com/configuration_guides/coupa/config_saml_coupa_p14e.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  download-the-coupa-metadata: Download the Coupa metadata
  set-up-the-coupa-application-in-pingone-for-enterprise-and-extract-the-metadata: Set up the Coupa application in PingOne for Enterprise and extract the metadata
  add-the-pingone-for-enterprise-idp-connection-to-coupa: Add the PingOne for Enterprise IdP connection to Coupa
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration:
  test-the-pingone-for-enterprise-sp-initiated-sso-integration: Test the PingOne for Enterprise SP-initiated SSO integration
---

# Configuring SAML SSO with Coupa and PingOne for Enterprise

Learn how to enable Coupa sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct Coupa sign-on using PingOne for Enterprise (SP-initiated sign-on).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Populate Coupa with at least one user to test access.

* You must have administrative access to PingOne for Enterprise and Coupa.

## Download the Coupa metadata

1. Sign on to your Coupa Admin organization as an administrator.

2. Go to `https://your_site.coupahost.com/administration/security`.

3. Select the **Sign in using SAML** check box.

4. Click the **Download and import SP metadata** link.

5. Save the Coupa metadata.

## Set up the Coupa application in PingOne for Enterprise and extract the metadata

1. Sign on to PingOne for Enterprise for Enterprise and go to **Applications → Application Catalog**.

2. Search for `Coupa`.

3. Expand the Coupa entry and click the **Setup** icon.

   ![Screen capture of PingOne for Enterprise Application Catalog with Coupa listed as the Application Name and the expansion arrow highlighted in red.](_images/nec1622059160332.png)

4. Copy the **IdP ID** value.

   ![Screen capture of PingOne for Enterprise IdP ID field highlighted in red.](_images/evh1622062440950.png)

5. Click **Continue to Next Step**.

6. Click **Select File** and upload the Coupa metadata file.

   ![Screen capture of PingOne for Enterprise Connection Configuration section with the Select File button for Upload Metadata highlighted in red as well as the field for the ACS URL.](_images/hos1622062666185.png)

7. Edit the ACS URL to add a relay state parameter to enable IdP initiated sign-on.

   `https://your-environment.coupahost.com/sp/ACS.saml2?RelayState=https://your-environment.coupahost.com/sessions/saml_post`

8. Click **Continue to Next Step**.

9. Ensure **SAML\_SUBJECT** is mapped to the field containing a user's email address.

   ![Screen capture of PingOne for Enterprise Attribute Mapping section. In the SAML\_SUBJECT\* row and Identity Bridge Attribute or Literal Value column, the Email (Work) field is highlighted in red.](_images/xzq1622063623154.png)

10. Click **Continue to Next Step** twice.

11. Click **Add** for all user groups that should have access to Coupa.

    ![Screen capture of PingOne for Enterprise Group Access page with Users@directory and Domain Administrators@directory listed under the Group Name column.](_images/xkc1622063848786.png)

12. Click **Continue to Next Step**.

13. Download the PingOne for Enterprise SAML metadata and signing certificate.

    ![Screen capture of PingOne for Enterprise Signing Certificate and SAML Metadata download hyperlinks highlighted in red.](_images/baz1622064155477.png)

14. Click **Finish**.

## Add the PingOne for Enterprise IdP connection to Coupa

1. Sign on to your Coupa Admin organization as an administrator.

2. Go to `https://your_site.coupahost.com/administration/security`.

3. Ensure the **Sign in using SAML** check box is selected.

4. In the **Upload IdP metadata** section, click **Choose File**, select the PingOne for Enterprise metadata, and import the file.

5. Confirm that the **Login Page URL** field has the **IdP ID** value from PingOne for Enterprise.

   `https://your site.coupahost.com/sp/startSSO.ping?PartnerIdpId=PingOne for Enterprise IdP ID value&TARGET=https://your site.coupahost.com/sessions/saml_post`

6. In the **Certificate** field, upload the PingOne for Enterprise signing certificate.

7. Click **Save**.

8. Click the **Users** tab and edit the users who will use SAML authentication.

9. Set **Single Sign-On ID** to the value users will use to sign on, for example, their email address.

10. Set **Authentication method** to SAML.

11. Click **Save**.

## Test the PingOne for Enterprise IdP-initiated SSO integration:

1. Go to your Ping desktop as a user with Coupa access.

   |   |                                                                                               |
   | - | --------------------------------------------------------------------------------------------- |
   |   | To find the Ping desktop URL in the Admin console, go to **Setup → Dock → PingOne Dock URL**. |

2. Complete PingOne for Enterprise authentication.

   You're redirected to your Coupa domain.

   ![Screen capture of PingOne for Enterprise login screen.](_images/ipm1622065041059.png)

## Test the PingOne for Enterprise SP-initiated SSO integration

1. Go to your Coupa URL.

2. After you're redirected to PingOne, enter your PingOne for Enterprise username and password.

   ![Screen capture of PingOne for Enterprise login screen.](_images/ttz1622065205294.png)

   You're redirected back to Coupa.
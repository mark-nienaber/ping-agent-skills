---
title: Configuring SAML SSO with Evernote and PingFederate
description: Learn how to enable Evernote sign on from a PingFederate URL (IdP-initiated sign-on) and direct Evernote sign on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:evernote:config_saml_evernote_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/evernote/config_saml_evernote_pf.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-evernote: Create a PingFederate SP connection for Evernote
  add-the-pingfederate-connection-to-evernote: Add the PingFederate connection to Evernote
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Evernote and PingFederate

Learn how to enable Evernote sign on from a PingFederate URL (IdP-initiated sign-on) and direct Evernote sign on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate Evernote with at least one user to test access.

* You must have administrative access to PingFederate and Evernote.

## Create a PingFederate SP connection for Evernote

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for Evernote in PingFederate:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to `https://www.evernote.com/saml2`.

   3. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation → Authentication Source Mapping → Attribute Contract Fulfillment**, map **SAML\_SUBJECT**.

   5. In **Protocol Settings → Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://www.evernote.com/SamlConsumer.action`.

   6. In **Protocol Settings → Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials → Digital Signature Settings**, select the **PingFederate Signing Certificate**.

3. Save the configuration.

4. Export the signing certificate.

5. Export the metadata, open the metadata file in a text editor, and copy the value of the Location entry (`https://your-value/idp/SSO.saml2`).

## Add the PingFederate connection to Evernote

1. Sign on to your Evernote Admin organization as an administrator and go to the Evernote Business Admin Console.

2. Go to **Security → Single Sign-On**.

3. Set **SAML HTTP Request URL** to the Location value from the metadata file that you downloaded previously (`https://your-value/idp/SSO.saml2`).

4. In a text editor, open your PingFederate signing certificate file, copy the contents, and paste your signing certificate contents into the **X.509 Certificate** field.

5. Click **Save & Enable**.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate **SSO Application Endpoint** for the Evernote SP connection.

2. Complete the PingFederate authentication.

   You're redirected to your Evernote domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to your Evernote URL.

2. Select the PingFederate sign-on option.

3. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to Evernote.

---

---
title: Configuring SAML SSO with Evernote and PingOne for Enterprise
description: Learn how to enable Evernote sign on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct Evernote sign on using PingOne for Enterprise (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:evernote:config_saml_evernote_p14e
canonical_url: https://docs.pingidentity.com/configuration_guides/evernote/config_saml_evernote_p14e.html
revdate: December 7, 2021
section_ids:
  before-you-begin: Before you begin
  update-the-evernote-application-in-pingone-for-enterprise: Update the Evernote application in PingOne for Enterprise
  add-the-pingone-for-enterprise-idp-connection-to-evernote: Add the PingOne for Enterprise IdP connection to Evernote
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration
  test-the-pingone-for-enterprise-sp-initiated-sso-integration: Test the PingOne for Enterprise SP-initiated SSO integration
---

# Configuring SAML SSO with Evernote and PingOne for Enterprise

Learn how to enable Evernote sign on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct Evernote sign on using PingOne for Enterprise (SP-initiated sign-on).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Populate Evernote with at least one user to test access.

* You must have administrative access to PingOne for Enterprise and Evernote.

## Update the Evernote application in PingOne for Enterprise

1. Sign on to PingOne for Enterprise and go to **Applications → Application Catalog**.

2. Search for `Evernote`.

   ![Screen capture of PingOne for Enterprise Application Catalog with Evernote displayed as a search result and the expansion arrow highlighted in red.](_images/xeh1625239040385.png)

3. Expand the Evernote entry and click the **Setup** icon.

4. Copy the **IdP ID** value.

   You will need this wherever you see `IdP-ID-value` in the next procedure.

5. Download the signing certificate.

   ![Screen captue of PingOne for Enterprise SSO Instructions with the Signing Certificate Download hyperlink, IdP ID field, and Issuer values all highlighted in red.](_images/yje1625240804439.png)

6. Click **Continue to Next Step** twice.

7. In the **Attribute Mapping** section, map **SAML\_SUBJECT** to the attribute containing the user's email address.

   ![Screen capture of PingOne for Enterprise Attribute Mapping section with the Email Identity Bridge Attribute or Literal Value field highlighted in red, as well as the Advanced button below it.](_images/tdv1625240910374.png)

8. Click **Advanced**.

9. In the **Name ID format to send to SP** field, enter `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`.

   ![Screen capture of PingOne for Enterprise Advanced Attribute Options for SAML\_SUBJECT with the Name ID Format to send to SP highlighted in red.](_images/coj1625241014206.png)

10. Click **Save**, then click **Continue to Next Step** twice.

11. Click **Add** for all user groups that should have access to Evernote.

    ![Screen capture of PingOne for Enterprise Group Access section.](_images/bql1625241133346.png)

12. Click **Continue to Next Step**.

13. Click **Finish**.

## Add the PingOne for Enterprise IdP connection to Evernote

1. Sign on to your Evernote Admin organization as an administrator and go to the Evernote Business Admin Console.

2. Go to **Security → Single Sign-On**.

3. Set **SAML HTTP Request URL** to `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=IdP-ID-value`.

4. In a text editor, open your PingOne for Enterprise signing certificate.

5. Copy and paste your signing certificate contents into the **X.509 Certificate** field.

6. Click **Save & Enable**.

## Test the PingOne for Enterprise IdP-initiated SSO integration

1. Go to your Ping desktop as a user with Evernote access.

   |   |                                                                                       |
   | - | ------------------------------------------------------------------------------------- |
   |   | To find the Ping desktop URL in the Admin console, go to **Setup → Dock → Dock URL**. |

2. Complete the PingOne for Enterprise authentication.

   ![Screen capture of PingOne for Enterprise sign on screen.](_images/kfg1625241418593.png)

   You're redirected to your Evernote domain.

## Test the PingOne for Enterprise SP-initiated SSO integration

1. Go to your Evernote URL.

2. Select the PingOne for Enterprise sign on option.

3. After you're redirected to PingOne for Enterprise, enter your PingOne for Enterprise username and password.

   ![Screen capture of PingOne for Enterprise sign on screen.](_images/kfg1625241418593.png)

   You're redirected back to Evernote.
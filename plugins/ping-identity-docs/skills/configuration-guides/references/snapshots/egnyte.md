---
title: Configuring SAML SSO with Egnyte and PingFederate
description: Learn how to enable Egnyte sign-on from a PingFederate URL (IdP-initiated sign-on) and direct Egnyte sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:egnyte:config_saml_egnyte_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/egnyte/config_saml_egnyte_pf.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  create-an-sp-connection-for-egnyte: Create an SP connection for Egnyte
  add-the-pingfederate-connection-to-egnyte: Add the PingFederate connection to Egnyte
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-Initiated SSO integration
---

# Configuring SAML SSO with Egnyte and PingFederate

Learn how to enable Egnyte sign-on from a PingFederate URL (IdP-initiated sign-on) and direct Egnyte sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate Egnyte with at least one user to test access.

* You must have administrative access to PingFederate and Egnyte.

## Create an SP connection for Egnyte

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for Egnyte in PingFederate.

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to `https://saml-auth.egnyte.com`.

   3. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation → Authentication Source Mapping → Attribute Contract Fulfillment**, map the **SAML\_SUBJECT** to the attribute containing the user's email address.

   5. In **Protocol Settings → Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://your-Egnyte-domain.egnyte.com/samlconsumer/PingFederate`.

   6. In **Protocol Settings → Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials → Digital Signature Settings**, select the **PingFederate Signing Certificate**.

3. Save the configuration.

4. Export the signing certificate.

5. Export and then open the metadata file and copy the value of the entityID and the Location entry (`https://your-value/idp/SSO.saml2`).

## Add the PingFederate connection to Egnyte

1. Sign on to your Egnyte Admin organization as an administrator.

2. Click the menu icon and then click **Settings**.

   ![Screen capture of Egnyte Settings highlighted in red from the expand menu icon, also highlighted in red.](_images/cgr1625159604516.png)

3. Click the **Security and Authentication** tab.

   ![Screen capture of Egnyte Configuration Settings with Security & Authentication highlighted in red.](_images/yyg1625159676037.png)

4. In the **Single sign-on authentication** list, select **SAML 2.0**.

5. In the **Identity provider** list, select **Ping Identity**.

6. Set the following values:

   | Field                             | Value                                                                                                             |
   | --------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
   | **Identity provider login URL**   | The Location value from the metadata that you exported.                                                           |
   | **Identity provider entity ID**   | The entityID value from the metadata that you exported.                                                           |
   | **Identity provider certificate** | In a text editor, open the signing certificate that you downloaded in a text editor. Copy and paste the contents. |
   | **Default user mapping**          | Email address                                                                                                     |

7. Click **Save**.

8. Go to **Settings → Users and Groups**.

9. Select the appropriate users and set their **AuthType** to **SSO**.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate **SSO Application Endpoint** for the Egnyte SP connection.

2. Complete the PingFederate authentication.

   You're redirected to your Egnyte domain.

## Test the PingFederate SP-Initiated SSO integration

1. Go to `https://your-Egnyte-domain.Egnyte.com`.

2. Select the PingFederate sign-on option.

3. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to Egnyte.

---

---
title: Configuring SAML SSO with Egnyte and PingOne for Enterprise
description: Learn how to enable Egnyte sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct Egnyte sign-on using PingOne for Enterprise (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:egnyte:config_saml_egnyte_p14e
canonical_url: https://docs.pingidentity.com/configuration_guides/egnyte/config_saml_egnyte_p14e.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  update-the-supplied-egnyte-application-in-pingone-for-enterprise: Update the supplied Egnyte application in PingOne for Enterprise
  add-the-pingone-for-enterprise-idp-connection-to-egnyte: Add the PingOne for Enterprise IdP connection to Egnyte
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration
  test-the-pingone-for-enterprise-sp-initiated-sso-integration: Test the PingOne for Enterprise SP-initiated SSO integration
---

# Configuring SAML SSO with Egnyte and PingOne for Enterprise

Learn how to enable Egnyte sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct Egnyte sign-on using PingOne for Enterprise (SP-initiated sign-on).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Populate Egnyte with at least one user to test access.

* You must have administrative access to PingOne for Enterprise and Egnyte.

## Update the supplied Egnyte application in PingOne for Enterprise

1. Sign on to PingOne for Enterprise and go to **Applications → Application Catalog**.

2. Search for `Egnyte`.

   ![Screen capture of PingOne for Enterprise Application Catalog with Egnyte displayed as the search result and the expansion arrow in the table highlighted in red.](_images/phw1625163597973.png)

3. Expand the Egnyte entry and click the **Setup** icon.

4. Copy the **Issuer** and **IdP ID** values.

5. Download the signing certificate.

   ![Screen capture of PingOne for Enterprise SSO instructions with the Download signing certificate, IdP ID, and Issuer values redacted and highlighted in red.](_images/zkk1625163701234.png)

6. Click **Continue to Next Step**.

7. Set **ACS URL** to `https://Your-Egnyte-domain.egnyte.com/samlconsumer/PingIdentity`.

8. Click **Continue to Next Step** twice.

9. In the **Attribute Mapping** section, map **SAML\_SUBJECT** to the attribute containing the user's email address.

10. Click **Continue to Next Step** twice.

11. Click **Add** for all user groups that should have access to Egnyte.

    ![Screen capture of PingOne for Enterprise Application GroupAccess section.](_images/pbj1625163838608.png)

12. Click **Continue to Next Step**.

13. Click **Finish**.

## Add the PingOne for Enterprise IdP connection to Egnyte

1. Sign on to your Egnyte Admin organization as an administrator.

2. Click the menu icon and then click **Settings.**

   ![Screen capture of Egnyte menu icon and Settings highlighted in red.](_images/cyt1625163922388.png)

3. Click the **Security and Authentication** tab.

   ![Screen capture of Egnyte Configuration Settings with Security & Authentication highlighted in red.](_images/eqa1625163988277.png)

4. In the **Single sign-on authentication** list, select **SAML 2.0**.

5. In the **Identity provider** list, select **Ping Identity**.

6. Set the following values:

   | Field                             | Value                                                                                            |
   | --------------------------------- | ------------------------------------------------------------------------------------------------ |
   | **Identity provider login URL**   | `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=IdP-ID-value`                      |
   | **Identity provider entity ID**   | The **Issuer** value from above.                                                                 |
   | **Identity provider certificate** | In a text editor, open the signing certificate that you downloaded. Copy and paste the contents. |
   | **Default user mapping**          | Email address                                                                                    |

7. Click **Save**.

8. Go to **Settings → Users and Groups**.

9. Select the appropriate users and set their **AuthType** to **SSO**.

## Test the PingOne for Enterprise IdP-initiated SSO integration

1. Go to our Ping desktop as a user with Egnyte access.

   |   |                                                                                       |
   | - | ------------------------------------------------------------------------------------- |
   |   | To find the Ping desktop URL in the Admin console, go to **Setup → Dock → Dock URL**. |

2. Complete the PingOne for Enterprise authentication.

   You're redirected to your Egnyte domain.

   ![Screen capture of PingOne for Enterprise sign on screen.](_images/mfe1625237764050.png)

## Test the PingOne for Enterprise SP-initiated SSO integration

1. Go to `https://Your-Egnyte-domain.Egnyte.com`.

2. Select the PingOne for Enterprise sign-on option.

3. After you're redirected to PingOne for Enterprise, enter your PingOne for Enterprise username and password.

   ![Screen capture of PingOne for Enterprise sign on screen.](_images/mfe1625237764050.png)

   You're redirected back to Egnyte.
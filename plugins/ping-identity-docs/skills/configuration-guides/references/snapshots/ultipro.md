---
title: Configuring SAML SSO with UltiPro and PingFederate
description: Learn how to enable UltiPro sign-on from the PingFederate console (IdP-initiated sign-on) and direct UltiPro sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:ultipro:config_saml_ultipro_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/ultipro/config_saml_ultipro_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-ultipro: Create a PingFederate SP connection for UltiPro
  add-the-pingfederate-connection-to-ultipro: Add the PingFederate connection to UltiPro
  update-the-acs-url-values-in-pingfederate: Update the ACS URL values in PingFederate
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with UltiPro and PingFederate

Learn how to enable UltiPro sign-on from the PingFederate console (IdP-initiated sign-on) and direct UltiPro sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate UltiPro with at least one user to test access.

* You must have administrative access to PingFederate.

## Create a PingFederate SP connection for UltiPro

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for UltiPro in Ping Federate:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to `placeholder`.

      You'll change this later.

   3. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP Initiated SSO**

   4. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment,** map the **SAML\_SUBJECT**.

   5. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST**, and set **Endpoint URL** to `https://placeholder`.

      You'll change the **Endpoint URL** later.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST.**

   7. In **Credentials: Digital Signature Settings**, select the PingFederate signing certificate.

3. Export the metadata for the newly created UltiPro SP connection.

4. Export the signing certificate.

## Add the PingFederate connection to UltiPro

1. Contact UltiPro Customer Support and request that SAML 2 be enabled for your organization.

2. Provide them with the downloaded PingFederate signing certificate and metadata.

3. Request their ACS URL and EntityID values.

## Update the ACS URL values in PingFederate

1. Sign on to the PingFederate administrative console.

2. Edit the SP connection for UltiPro.

3. Set **Partner's Entity ID** to the UltiPro **Entity ID** value.

4. In **Protocol Settings: Assertion Consumer Service URL**, set **Endpoint URL** to the UltiPro **Assertion Consumer Service URL** value.

5. Save the changes.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO application endpoint for the UltiPro SP connection.

2. Complete the PingFederate authentication.

   You're redirected to your UltiPro domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to your UltiPro application.

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to UltiPro.

---

---
title: Configuring SAML SSO with UltiPro and PingOne for Enterprise
description: Learn how to enable UltiPro sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct UltiPro sign-on using PingOne for Enterprise (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:ultipro:config_saml_ultipro_p14e
canonical_url: https://docs.pingidentity.com/configuration_guides/ultipro/config_saml_ultipro_p14e.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  add-the-ultipro-application-to-pingone-for-enterprise: Add the UltiPro application to PingOne for Enterprise
  add-the-pingone-for-enterprise-connection-to-ultipro: Add the PingOne for Enterprise connection to UltiPro
  complete-the-ultipro-pingone-for-enterprise-setup-in-ultipro: Complete the UltiPro PingOne for Enterprise setup in UltiPro
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration
  test-the-pingone-for-enterprise-sp-initiated-sso-integration: Test the PingOne for Enterprise SP-initiated SSO integration
---

# Configuring SAML SSO with UltiPro and PingOne for Enterprise

Learn how to enable UltiPro sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct UltiPro sign-on using PingOne for Enterprise (SP-initiated sign-on).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Populate UltiPro with at least one user to test access.

* You must have administrative access to PingOne for Enterprise.

## Add the UltiPro application to PingOne for Enterprise

1. Sign on to PingOne for Enterprise and go to **Applications → My Applications**.

2. On the **SAML** tab, click **Add Application**.

   ![Screen capture of PingOne for Enterprise My Applications page on the SAML tab, with the Add Application dropdown menu opened and New SAML Application selected.](_images/lbq1622073242894.png)

3. Enter `UltiPro` as the application name.

4. Enter a suitable description.

5. For the category, select **Human Resources**.

6. Click **Continue to Next Step**.

7. Set **Assertion Consumer Service (ACS)** to `https://placeholder` and set **Entity ID** to `placeholder`.

   You'll update these values later.

8. Click **Continue to Next Step**.

9. Click **Add new attribute**.

   ![Screen capture of PingOne for Enterprise SSO Attribute Mapping section with the Add new attribute button highlighted in red.](_images/fhw1622073479541.png)

10. Add the **SAML\_SUBJECT** attribute and map it to the value required by UltiPro.

    ![Screen capture of PingOne for Enterprise Application Attribute table with SAML\_SUBJECT highlighted in red in both the Application Attribute and Identity Bridge Attribute or Literal Value columns.](_images/hyw1622073590392.png)

11. Click **Continue to Next Step**.

12. Click **Add** for all user groups that should have access to UltiPro.

    ![Screen capture of PingOne for Enterprise Group Access page with Users@directory and Domain Administrators@directory listed in the Group Name column.](_images/dcz1622073699900.png)

13. Click **Continue to Next Step**.

14. Download the PingOne for Enterprise signing certificate and metadata.

    ![Screen capture of PingOne for Enterprise Signing Certificate and SAML Metadata Download hyperlinks highlighted in red.](_images/azy1622073821102.png)

15. Click **Finish**.

## Add the PingOne for Enterprise connection to UltiPro

1. Contact UltiPro Customer Support and request that SAML 2 be enabled for your organization.

2. Provide them with the downloaded PingOne for Enterprise signing certificate and metadata.

3. Request their ACS URL and EntityID values.

## Complete the UltiPro PingOne for Enterprise setup in UltiPro

1. Continue editing the UltiPro entry in PingOne for Enterprise for Enterprise.

   |   |                                                                                              |
   | - | -------------------------------------------------------------------------------------------- |
   |   | If the session has timed out, complete the initial steps to the point of clicking **Setup**. |

2. Click **Continue to Next Step**.

3. Set the **ACS URL** to the UltiPro **ACS URL** value.

4. Set the **Entity ID** to the UltiPro **Entity ID** value.

5. Click **Continue to Next Step** until you reach the final page, then click **Finish**.

## Test the PingOne for Enterprise IdP-initiated SSO integration

1. Go to your Ping desktop as a user with UltiPro access.

   |   |                                                                                               |
   | - | --------------------------------------------------------------------------------------------- |
   |   | To find the Ping desktop URL in the Admin console, go to **Setup → Dock → PingOne Dock URL**. |

2. Complete the PingOne for Enterprise authentication.

   You're redirected to your UltiPro application.

   ![Screen capture of PingOne for Enterprise login screen.](_images/fiz1622074168673.png)

## Test the PingOne for Enterprise SP-initiated SSO integration

1. Go to your UltiPro application.

2. After you're redirected to PingOne for Enterprise, enter your PingOne for Enterprise username and password.

   ![Screen capture of PingOne for Enterprise login screen.](_images/jko1622074218118.png)

   You're redirected back to UltiPro.
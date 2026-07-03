---
title: Configuring SAML SSO with Jamf Pro and PingFederate
description: Enable Jamf Pro sign-on from the PingFederate console (IdP-initiated sign-on) and direct Jamf Pro sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:jamf:config_saml_jamfpro_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/jamf/config_saml_jamfpro_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-jamf-pro: Create a PingFederate SP connection for Jamf Pro
  add-the-pingfederate-connection-to-jamf-pro: Add the PingFederate connection to Jamf Pro
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Jamf Pro and PingFederate

Enable Jamf Pro sign-on from the PingFederate console (IdP-initiated sign-on) and direct Jamf Pro sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate Jamf Pro with at least one user to test access.

* You must have administrative access to PingFederate.

## Create a PingFederate SP connection for Jamf Pro

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for Jamf Pro in PingFederate:

   * Configure using **Browser SSO** profile **SAML 2.0**.

   * Set **Partner's Entity ID** to `https://your-instance.jamfcloud.com/saml/metadata`.

   * Enable the **IdP-Initiated SSO** and **SP Initiated SSO** SAML profiles.

     * In **Assertion Creation → Authentication Source Mapping → Attribute Contract Fulfillment**, map the **SAML\_SUBJECT** to your `email` attribute.

     * In **Protocol Settings → Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://your-instance.jamfcloud.com/saml/SSO`.

     * In **Protocol Settings → Allowable SAML Bindings**, enable **POST**.

     * In **Credentials → Digital Signature Settings**, select the **PingFederate Signing Certificate**.

3. Export the metadata for the newly-created Jamf Pro SP connection.

4. Export the signing certificate.

## Add the PingFederate connection to Jamf Pro

1. Sign on to the Jamf Pro console as an administrator.

2. Click the **Gear** icon ([icon: gear, set=fa]]).

3. Go to **System Settings → Single Sign-On**.

   ![Screen capture of the Jamf Pro console with the System Settings and Single Sign-On sections highlighted in red.](_images/jlu1619216147468.png)

4. Click the **Edit** icon.

5. Select the **Enable Single Sign-On Authentication** check box.

   ![Screen capture of the Jamf Pro console with the Enable Single Sign-On Authentication check box highlighted in red.](_images/svc1619216215368.png)

6. In the **Identity Provider** list, select **Ping Identity**.

7. Confirm that the **Entity ID** value matches the value you set previously in PingFederate.

8. In the **Upload Metadata File** field, upload the PingFederate metadata file.

   ![Screen capture of the Single Sign-On System Settings in Jamf Pro console with the Identity provider list, the Entity ID field, and the Upload Metadata File fields highlighted in red.](_images/ndj1619216236431.png)

9. In the **Jamf Pro User Mapping** section, click **Email**.

   ![Screen capture of the Jamf Pro User Mapping section with the Email button highlighted in red.](_images/gcb1619216266706.png)

10. In the **Single Sign-On Options for Jamf Pro** section, select the **Allow users to bypass the Single Sign-On authentication** check box.

    ![Screen capture of the Jamf Pro Single Sign-On Options section with the Allow users to bypass the Single Sign-On authentication check box highlighted in red.](_images/snk1619216291025.png)

11. Click **Save**.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO application endpoint for the Jamf Pro SP connection.

2. Complete the PingFederate authentication.

   You're redirected to your Jamf Pro domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to your Jamf Pro application.

2. After you are redirected to PingFederate, enter your PingFederate username and password.

   After successful authentication, you're redirected back to Jamf Pro.

---

---
title: Configuring SAML SSO with Jamf Pro and PingOne for Enterprise
description: Enable Jamf Pro sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct JAMF Pro sign-on using PingOne for Enterprise (SP-initiated sign-on) with single logout (SLO).
component: configuration_guides
page_id: configuration_guides:jamf:config_saml_jamfpro_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/jamf/config_saml_jamfpro_p1.html
revdate: May 20, 2024
section_ids:
  before-you-begin: Before you begin
  add-the-jamf-pro-application-to-pingone-for-enterprise: Add the Jamf Pro application to PingOne for Enterprise
  add-the-pingone-for-enterprise-connection-to-jamf-pro: Add the PingOne for Enterprise connection to JAMF Pro
  test-the-pingone-for-enterprise-identity-provider-idp: Test the PingOne for Enterprise identity provider (IdP)
  test-the-pingone-for-enterprise-service-provider-sp: Test the PingOne for Enterprise service provider (SP)
---

# Configuring SAML SSO with Jamf Pro and PingOne for Enterprise

Enable Jamf Pro sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct JAMF Pro sign-on using PingOne for Enterprise (SP-initiated sign-on) with single logout (SLO).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Populate Jamf Pro with at least one user to test access.

* You must have administrative access to PingOne for Enterprise.

## Add the Jamf Pro application to PingOne for Enterprise

1. Sign on to PingOne for Enterprise and go to **Applications → My Applications**.

2. On the **SAML** tab, click **Add Application**.

   ![The PingOne for Enterprise My Applications page with the SAML tab selected. The Add Application list is open with New SAML Application selected.](_images/obo1619215162224.png)

3. Enter `Jamf Pro` as the application name.

4. Enter a suitable description.

5. Choose a suitable category.

6. Click **Continue to Next Step**.

7. Enter the following values:

   | Field                                | Value                                                   |
   | ------------------------------------ | ------------------------------------------------------- |
   | **Assertion Consumer Service (ACS)** | `https://your-instance.jamfcloud.com/saml/SSO`          |
   | **Entity ID**                        | `https://your-instance.jamfcloud.com/saml/metadata`     |
   | **Single Logout (SLO) Endpoint**     | `https://your-instance.jamfcloud.com/saml/SingleLogout` |
   | **Single Logout Binding Type**       | `POST`                                                  |

   ![Screen capture of the SAML metadata fields in PingOne for Enterprise with the SAML Metadata, Assertion Consumer Service, Entity ID, and Single Logout Endpoint fields highlighted in red.](_images/pwh1619215340080.png)

8. On the **SAML Metadata** line, click **Download**.

9. Click **Continue to Next Step**.

10. Click **Add new attribute**.

    ![Screen capture of the SSO Attribute Mapping section with the Add new attribute button highlighted in red.](_images/spq1619215373741.png)

11. Add the **SAML\_SUBJECT** attribute and map it to your email attribute.

    ![Screen capture of the SSO Attribute Mapping section with the Application Attribute and the Identity Bridge Attribute or Literal Value fields highlighted in red.](_images/swd1619215407551.png)

12. Click **Continue to Next Step**.

13. Click **Add** for each user groups that should have access to JAMF Pro.

    ![Screen capture of the PingOne for Enterprise Group Access section with two Group Name search field and the Group Name results field.](_images/zwe1619215443365.png)

14. Click **Continue to Next Step**.

15. Click **Finish**.

## Add the PingOne for Enterprise connection to JAMF Pro

1. Sign on to the Jamf Pro console as an administrator.

2. Click the **Gear** icon ([icon: gear, set=fa]]).

3. Go to **System Settings → Single Sign-On**.

   ![Screen capture of the Jamf Pro console with the System Settings and Single Sign-On sections highlighted in red.](_images/iju1619215515955.png)

4. Click the **Edit** icon.

   ![Screen capture of the Edit icon highlighted in red.](_images/ylm1619215540895.png)

5. Select the **Enable Single Sign-On Authentication** check box.

   ![Screen capture of the Jamf Pro console with the Enable Single Sign-On Authentication check box highlighted in red.](_images/agf1619215564248.png)

6. In the **Identity Provider** list, select **Ping Identity**.

7. Confirm that the **Entity ID** value matches the value you set previously in PingOne for Enterprise.

8. In the **Upload Metadata File** section, upload the PingOne for Enterprise metadata file.

   ![Screen capture of the Single Sign-On System Settings in Jamf Pro console with the Identity provider list, the Entity ID field, and the Upload Metadata File fields highlighted in red.](_images/agd1619215604302.png)

9. In the **Jamf Pro User Mapping** section, click **Email**.

   ![Screen capture of the Jamf Pro User Mapping section with the Email button highlighted in red.](_images/dzi1619215633101.png)

10. In the **Single Sign-On Options for Jamf Pro** section, select the **Allow users to bypass the Single Sign-On authentication** check box.

    ![Screen capture of the Jamf Pro Single Sign-On Options section with the Allow users to bypass the Single Sign-On authentication check box highlighted in red.](_images/cig1619215656986.png)

11. Click **Save**.

## Test the PingOne for Enterprise identity provider (IdP)

1. Go to your Ping desktop as a user with Jamf Pro access.

   |   |                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------ |
   |   | To find the Ping desktop URL, in the PingOne admin console, go to **Setup → Dock → PingOne Dock URL**. |

2. Complete the PingOne authentication.

   ![Screen capture of the Jam Pro application home page.](_images/ito1619215732180.png)

   You're redirected to your Jamf Pro application.

## Test the PingOne for Enterprise service provider (SP)

1. If you are using PingOne for Enterprise as the standard authentication method for Jamf Pro access, sign on to the Jamf Pro console as an administrator after you've completed PingOne for Enterprise IdP testing.

2. Go to **Settings → System Settings → Single Sign-On** and click **Edit**.

   ![Screen capture of the Edit icon highlighted in red.](_images/vuz1619215767621.png)

3. Clear the **Allow users to bypass the Single Sign-On authentication** check box.

   ![Screen capture of the Single Sign-On Options for Jamf Pro section with the Allow users to bypass the Single Sign-On authentication check box highlighted in red.](_images/wvh1619215811370.png)

4. Click **Save**.

5. Go to your Jamf Pro application.

   ![Screen capture of the Jamf Pro application home page.](_images/ito1619215732180.png)

   You're redirected to PingOne for Enterprise.

6. Enter your PingOne for Enterprise username and password.

   After successful authentication, you're redirected back to Jamf Pro.
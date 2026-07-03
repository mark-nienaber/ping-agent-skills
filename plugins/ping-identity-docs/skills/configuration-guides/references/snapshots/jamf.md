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

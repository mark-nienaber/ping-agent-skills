---
title: Configuring SAML SSO with Slack and PingFederate
description: Enable Slack sign-on from a PingFederate URL (IdP-initiated sign-on) and direct Slack sign-on using PingFederate (SP-initiated sign-on) with JIT provisioning.
component: configuration_guides
page_id: configuration_guides:slack:config_saml_slack_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/slack/config_saml_slack_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-slack: Create a PingFederate SP connection for Slack
  add-the-pingfederate-connection-to-slack: Add the PingFederate connection to Slack
  choose-from: Choose from:
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Slack and PingFederate

Enable Slack sign-on from a PingFederate URL (IdP-initiated sign-on) and direct Slack sign-on using PingFederate (SP-initiated sign-on) with JIT provisioning.

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users that require application access.

* You must have administrative access to PingFederate and Slack.

## Create a PingFederate SP connection for Slack

1. Sign on to the PingFederate administration console.

2. Create a service provider (SP) connection for Slack in PingFederate:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to `https://slack.com`.

   3. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation > Attribute Contract**, extend the contract with the following attributes:

      * `SAML_NAME_FORMAT`

      * `User.Email`

      * `User.Username`

      * `first_name`

      * `last_name`

      Use the following attribute name format:

      `urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified`

   5. In **Assertion Creation → Authentication Source Mapping → Attribute Contract Fulfillment**:

      1. Map **SAML\_SUBJECT**, **User.Email**, **User.Username**, **first\_name**, and **last\_name**.

      2. Map **SAML\_NAME\_FORMAT** to a text value of `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`.

   6. In **Protocol Settings → Assertion Consumer Service URL**, set the following properties:

      * Set **Binding** to **POST**.

      * Set **Endpoint URL** to `https://your-slack-domain.slack.com/sso/saml`.

   7. In **Protocol Settings → Allowable SAML Bindings**, enable **POST** and **REDIRECT**.

   8. In **Protocol Settings → Signature Policy**, select **Always Sign Assertion**.

   9. In **Credentials → Digital Signature Settings**, select the **PingFederate Signing Certificate**.

3. Save the configuration.

4. Export the signing certificate.

5. Export the metadata file, open it in a text editor, and copy:

   * The entityID

   * The Location entry, `https://your-value/idp/SSO.saml2`

## Add the PingFederate connection to Slack

### Choose from:

* For Slack Standard or Plus, do the following

  1. Sign on to your Slack Workspace as an administrator.

  2. Go to **Settings & Administration → Workspace Settings**.

     ![Screen capture showing how to select Workspace settings in the Settings and administration menu.](_images/kgz1618953230690.jpg)

  3. Click the **Authentication** tab.

  4. In the **Configure an authentication method** section, on the **SAML authentication** line, click **Configure**.

     ![Screen capture of the Authentication tab, in the Configure an authentication method section. There are options for Google Apps authentication and SAML authentication. Each authentication option has a Configure button.](_images/olx1618953369144.jpg)

  5. If prompted, enter your password to continue.

  6. In the **SAML 2.0 Endpoint (HTTP)** field, enter the PingFederate **Location** value.

  7. In the **Identity Provider Issuer** field, enter the PingFederate **entityID** value.

  8. In the **Public Certificate** field, paste in the contents of the PingFederate signing certificate.

     ![Screen capture showing the SAML configuration with the Identity Provider Issuer, PingFederate signing certificate, and Public Certificate fields where you paste the contents as described in the steps.](_images/jnf1619133776298.jpg)

  9. Expand the **Advanced Options** section, and clear the **Assertions Signed** check box.

     ![Screen capture of the expanded Advanced Options section. There are fields for AuthnContextClassRef anf Service Provider Issuer. There are a Responses Signed checkbox, which is Selected, and a Assertions Signed checkbox which is cleared.](_images/vhi1619133848297.jpg)

  10. In the **Settings** section, select the **It's optional** radio button for the authentication setting.

      |   |                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------- |
      |   | You can change the authentication setting to your desired value after you have completed testing. |

      ![Screen capture of the authentication settings section. The It's optional radio button is clicked and highlighted.](_images/idk1618953623813.jpg)

  11. Click **Save Configuration**.

      ![Screen capture of the Customize section. The Sign in Button Label and Button Preview are here to custmomize. The Save Configuration button is highlighted.](_images/rwz1619133915132.jpg)

  12. When you're redirected to PingFederate, authenticate with PingFederate.

      Your selection is confirmed against PingFederate and saved if successful.

* For Slack Enterprise Grid, do the following

  1. Sign on to your Slack Organization (not Workspace) as an administrator.

  2. Go to **Manage Organization → Security → SSO Settings → Configure SSO**.

     ![A screen recording that shows the Slack dashboard. The user clicks Manage Organization, and then clicks Security.](_images/fvm1617230085096.gif)

  3. In the **SAML 2.0 Endpoint (HTTP)** field, enter the PingFederate **Location** value from the metadata file.

  4. In the **Service Provider Issuer URL**, use the default value of **https\://slack.com**.

  5. In the **Public (X.509) Certificate** field, enter the contents of your PingFederate signing certificate.

  6. Enable authentication request signing.

     1. Select the **Sign the AuthnRequest** check box.

     2. Copy the certificate text.

     3. Create a new `.crt` file on your computer and paste the certificate text.

     4. In PingFederate, import the `.crt` file as a trusted certificate authority. You can find help in [Manage Trusted Certificate Authorities](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_trustedcas_certmanagementstate.html) in the PingFederate documentation.

  7. Clear the **Sign the Assertion** check box.

     ![A screenshot that shows the SAML Response Signing section with the correct settings.](_images/bdv1617989116378.jpg)

  8. Click **Test Configuration**.

  9. Sign out of Slack and then sign back on using SSO.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO application endpoint for the Slack SP connection.

2. Complete the PingFederate authentication.

   ![Screen capture of the new Slack domain and the user's profile.](_images/nib1618954174193.jpg)

   You're redirected to your Slack domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to your Slack domain, `https://your-domain.slack.com`.

2. Click **Sign in with Ping**.

   ![Screen capture of the Customize section. The Sign in Button Label and Button Preview are here to customize. The Save Configuration button is highlighted.](_images/rwz1619133915132.jpg)

3. After you're redirected, enter your PingFederate username and password.

   After successful authentication, you're redirected back to Slack.

   |   |                                                                                 |
   | - | ------------------------------------------------------------------------------- |
   |   | If the user doesn't exist in Slack, you are prompted to accept the Slack terms. |

   ![Screen capture of the new Slack domain and the user's profile.](_images/nib1618954174193.jpg)

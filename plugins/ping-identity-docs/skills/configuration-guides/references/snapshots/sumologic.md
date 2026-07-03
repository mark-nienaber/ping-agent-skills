---
title: Configuring SAML SSO with SumoLogic and PingFederate
description: Learn how to enable SumoLogic sign-on from a PingFederate URL (IdP-initiated sign-on) and direct SumoLogic sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:sumologic:config_saml_sumologic_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/sumologic/config_saml_sumologic_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-service-provider-sp-connection-for-sumologic: Create a PingFederate service provider (SP) connection for SumoLogic
  add-the-pingfederate-idp-connection-to-sumologic: Add the PingFederate IdP Connection to SumoLogic
  update-the-acs-url-values-in-pingfederate: Update the ACS URL values in PingFederate
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with SumoLogic and PingFederate

Learn how to enable SumoLogic sign-on from a PingFederate URL (IdP-initiated sign-on) and direct SumoLogic sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* PingFederate's X.509 certificate should be exchanged to verify the signature in SAML assertions.

* An email attribute is required in the assertion, either the SAML Subject or another SAML attribute per the SAML configuration. The value of the email attribute must be a valid email address. It is used to uniquely identify the user in the organization.

* Populate SumoLogic with at least one user to test access.

## Create a PingFederate service provider (SP) connection for SumoLogic

1. Sign on to the PingFederate admin console.

2. Configure using **Browser SSO** profile **SAML 2.0**.

3. Set **Partner's Entity ID** to `https://service.eu.sumologic.com/`.

4. Enable the following SAML Profiles:

   * **IdP-Initiated SSO**

   * **SP-Initiated SSO**

5. In **Assertion Creation: Attribute Contract**, select **urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified**.

6. In **Assertion Creation: Authentication Source Mapping: Authentication Source Mapping**, map a new **Adapter Instance → HTML Form**.

7. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfilment**, map `SAML_SUBJECT`.

8. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://service.eu.sumologic.com/sumo/saml/consume/596910108`. This value is received and updated from SumoLogic.

9. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

10. In **Credentials: Digital Signature Settings**, select the **PingFederate Signing Certificate**.

11. Save the configuration.

12. Export the signing certificate.

13. Export and then open the metadata file and copy the value of:

    * The **entityID**

    * The **Location** entry (`https://your-value/idp/SSO.saml2`)

## Add the PingFederate IdP Connection to SumoLogic

1. Sign on to the SumoLogic application.

   |   |                                                                     |
   | - | ------------------------------------------------------------------- |
   |   | In this example, we have registered and logged in using trial mode. |

   ![Screen capture of SumoLogic dashboard.](_images/tqh1638476606797.png)

2. Go to **Administration → Security → SAML**.

   ![Screen capture of the SumoLogic Configuration List.](_images/ewh1638476674038.png)

3. Click **Add Configuration**.

   ![Screen capture of SumoLogic Add Configuration page.](_images/tjb1638476698113.png)

4. Add the following values:

   * **Configuration Name** : `pingfed`

   * Select the **Debug Mode** check box

   * **Issuer**: The PingFederate Issuer value

   * **X.509 Certificate**: Copy PingFederate's X.509 certificate here for verifying the signature

   * **Attribute Mapping**: Select **Use SAML Subject**

   * **Optional Settings**: Leave the default settings

   * Click **Add**

   * Enable **Require SAML Sign In**.

   ![Screen capture of the SumoLogic Configuration List with pingfed added as a configuration.](_images/kdv1638476727757.png)

5. Select the **pingfed** configuration you have just created and copy the **Assertion Consumer Service URL**.

   ![Screen capture of the SumoLogic Configuration List page with pingfed selected.](_images/dki1638476762195.png)

6. To enable SP-initiated SSO, select the **pingfed** configuration and click the **Pencil** icon above the **ACS URL**.

7. Select the **SP Initiated Login Configuration** check box and enter the following values:

   * **Login Path**: enter a unique identifier for your organization. You can specify any alphanumeric string (with no embedded spaces), provided that it is unique to your organization. (You can't configure a **Login Path** that another Sumo customer has already configured).

   * **Authn Request URL**: enter the URL that the IdP has assigned for SumoLogic to submit SAML authentication requests to the IdP. For example, `https://idp-server-hostname:9031/sso/idp/SSO.saml2`

   * Select **Binding Type: Post**.

   ![Screen capture of SumoLogic pingfed editing section.](_images/ohp1638476785868.png)

8. Click **Save**.

9. Click the saved **pingfed** configuration again and make a note of the **Authentication Request** and **EntityID** URLs.

   ![Screen capture of SumoLogic Configuration List page with the pingfed URL values on the right side of the page.](_images/zre1638476812388.png)

   The SumoLogic connection configuration is now complete.

## Update the ACS URL values in PingFederate

1. Sign on to the PingFederate administrative console.

2. Edit the SP connection for SumoLogic.

3. Set the **Partner's Entity ID (Connection ID)** value to SumoLogic's **Entity ID** that you copied previously.

4. Set **Assertion Consumer Service URL : Endpoint URL** to SumoLogic's **Assertion Consumer Service URL** value.

5. Click **Save**.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the **PingFederate SSO Application Endpoint** for the SumoLogic SP connection.

2. Authenticate with PingFederate.

   You're redirected to your SumoLogic domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to your SumoLogic **Authentication Request URL**.

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   After successful authentication, you're redirected back to SumoLogic.
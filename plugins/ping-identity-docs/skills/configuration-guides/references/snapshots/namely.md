---
title: Configuring SAML SSO with Namely and PingFederate
description: Learn how to enable Namely sign-on from the PingFederate console (IdP-initiated sign-on) and direct Namely sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:namely:config_saml_namely_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/namely/config_saml_namely_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-the-namely-metadata: Create the Namely metadata
  add-the-pingfederate-connection-to-namely: Add the PingFederate connection to Namely
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Namely and PingFederate

Learn how to enable Namely sign-on from the PingFederate console (IdP-initiated sign-on) and direct Namely sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* PingFederate should be configured to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* Populate Namely with at least one user to test access.

* You must have administrative access to PingFederate.

## Create the Namely metadata

1. In PingFederate, create a service provider (SP) connection for Namely:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to `https://your-subdomain.namely.com/saml/metadata`.

   3. Enable the following SAML profiles:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfilment,** map the **SAML\_SUBJECT** to your email attribute.

   5. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://your-subdomain.namely.com/saml/consume`.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials: Digital Signature Settings**, select the **PingFederate Signing Certificate**.

   8. Note the metadata URL for the newly-created Namely SP connection.

## Add the PingFederate connection to Namely

1. Sign on to the Namely console as an administrator.

2. Select **Company** on the top navigation bar.

3. Click the **Settings** tab.

4. In the left navigation pane, click **Login Page**.

5. In the **Login Methods** section, click **SAML**.

6. Enter the **Identity Provider SSO URL** from PingFederate.

7. Copy and paste the IdP Provider Certificate value into the **Identity provider certificate**.

8. Enter the **SAML Metadata URL** from PingFederate.

   ![Screen capture of Namely Company page with Settings, Login Page, SAMML, SAML Settings ceritficate, and SAML Metadata highlighted.](_images/kky1640218027409.png)

9. Click **Save**.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO Application Endpoint for the Namely SP connection.

2. Authenticate with PingFederate.

   You're redirected to your Namely domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to `https://your-subdomain.namely.com/users/login`.

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to Namely.

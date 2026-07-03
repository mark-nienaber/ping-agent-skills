---
title: Configuring SAML SSO with Mimecast and PingFederate
description: Learn how to enable Mimecast sign-on from PingFederate (IdP-initiated sign-on) and direct Mimecast sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:mimecast:config_saml_mimecast_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/mimecast/config_saml_mimecast_pf.html
revdate: May 20, 2024
section_ids:
  before-you-begin: Before you begin
  create-the-mimecast-metadata: Create the Mimecast metadata
  add-the-pingfederate-connection-to-mimecast: Add the PingFederate connection to Mimecast
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Mimecast and PingFederate

Learn how to enable Mimecast sign-on from PingFederate (IdP-initiated sign-on) and direct Mimecast sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* Populate Mimecast with at least one user to test access.

* You must have administrative access to PingFederate.

## Create the Mimecast metadata

1. In PingFederate, create a service provider (SP) connection for Mimecast:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set Partner's Entity ID to `your-Mimecast-account-hosting-location-api.mimecast.com.accountcode`.

   3. Enable the following SAML profiles:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfilment**, map the **SAML\_SUBJECT** to your email attribute.

   5. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://your-Mimecast-account-hosting-location-api.mimecast.com/sign on/saml`.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials: Digital Signature Settings**, select the **PingFederate Signing Certificate**.

      |   |                                                                     |
      | - | ------------------------------------------------------------------- |
      |   | Note the metadata URL for the newly-created Mimecast SP connection. |

## Add the PingFederate connection to Mimecast

1. Sign on to the Mimecast console as an administrator.

2. Select **Administration** on the lefthand pane.

3. Click the **Services** tab.

4. Select **Application Settings**.

5. Select **Authentication Profiles**.

   ![Screen capture of Mimecast administration console with Authentication Profiles highlighted.](_images/hwo1640212753197.png)

6. Click **New Authentication Profile**.

7. Select the **Enforce SAML Authentication for Administration Console** option.

   The page expands to reveal the **SAML Settings**.

8. Under **Provider**, select **Other**.

9. Enter the **Metadata URL** for the Mimecast SP Connector in PingFederate.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO Application Endpoint for the Mimecast SP connection.

2. Authenticate with PingFederate.

   You're redirected to your Mimecast domain.

## Test the PingFederate SP-initiated SSO integration

1. Sign on to [Mimecast](https://login.mimecast.com/u/login/?gta=apps&_ga=2.197221231.1597895005.1652085427-1344334576.1645445521#/login).

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   After successful authentication, you're redirected back to Mimecast.

---
title: Configuring SAML SSO with Marketo and PingFederate
description: Learn how to enable Marketo sign-on from PingFederate (IdP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:marketo:config_saml_marketo_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/marketo/config_saml_marketo_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  obtain-your-munchkin-account-id: Obtain your Munchkin Account ID
  create-an-sp-connection-for-marketo-in-pingfederate: Create an SP connection for Marketo in PingFederate
  enable-saml-sso-in-marketo: Enable SAML SSO in Marketo
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO Integration
---

# Configuring SAML SSO with Marketo and PingFederate

Learn how to enable Marketo sign-on from PingFederate (IdP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* Populate Marketo with at least one user to test access.

* You must have administrative access to PingFederate.

## Obtain your Munchkin Account ID

1. Sign on to the Marketo console as an administrator.

2. Select **Admin** in the toolbar.

3. Select **Intergration** in the left-hand pane.

4. **Copy** and **Save** your Munchkin Account ID.

## Create an SP connection for Marketo in PingFederate

1. Sign on to PingFederate.

2. Configure using **Browser SSO** profile **SAML 2.0**.

3. Set **Partner's Entity ID** to `https://www.marketo.com/SAML/your-Munchkin-account-ID`.

4. Enable the **IDP-initiated SSO** **SAML Profile**.

   |   |                                                      |
   | - | ---------------------------------------------------- |
   |   | Marketo does not currently support SP-initiated SSO. |

5. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map the **SAML\_SUBJECT** to your email attribute.

6. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://login.marketo.com/saml/assertion/your-Munchkin-account-ID`.

7. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

8. In **Credentials: Digital Signature Settings**, select the PingFederate Signing Certificate and download it.

## Enable SAML SSO in Marketo

1. Sign on to the Marketo console as an administrator.

2. Select **Admin** in the toolbar.

3. Select **Other Stuff** in the left navigation pane.

4. Select **Single Sign-On**.

   |   |                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------- |
   |   | If you don't see **Single Sign-On**, contact <support@marketo.com> to enable SAML for your account. |

5. Next to **SAML Settings**, select **Edit**.

6. For the **Issuer ID**, enter the value you entered for the **IdP Entity ID** in PingFederate.

7. For the **Entity ID**, enter the value you entered for the **IdP Entity ID** in PingFederate.

8. For the **User ID** Location, click the **In Name identifier** element of **Subject**.

9. Click **Browse** next to **Identity Provider Certificate** and upload your public certificate.

10. Click **Save**.

## Test the PingFederate IdP-initiated SSO Integration

1. Go to the PingFederate SSO Application Endpoint for the Marketo SP connection.

2. Authenticate with PingFederate.

   You're redirected to your Marketo domain.

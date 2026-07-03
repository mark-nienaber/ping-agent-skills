---
title: Configuring SAML SSO with Workato and PingFederate
description: Learn how to enable Workato sign-on from the PingFederate console (IdP-initiated sign-on) and direct Workato sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:workato:config_saml_workato_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/workato/config_saml_workato_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-the-workato-metadata: Create the Workato metadata
  add-the-pingfederate-connection-to-workato: Add the PingFederate connection to Workato
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Workato and PingFederate

Learn how to enable Workato sign-on from the PingFederate console (IdP-initiated sign-on) and direct Workato sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* Populate Workato with at least one user to test access.

* You must have administrative access to PingFederate.

## Create the Workato metadata

1. In PingFederate, create a service provider (SP) connection for Workato:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set Partner's Entity ID to `https://www.workato.com/saml/metadata?id=Workato ID`.

      |   |                                                                           |
      | - | ------------------------------------------------------------------------- |
      |   | This value is provided by Workato on the **Tools → Team → Settings** tab. |

   3. Enable the following SAML profiles.

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfilment,** map the **SAML\_SUBJECT** to your email attribute.

   5. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://www.workato.com/saml/consume/`.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials: Digital Signature Settings**, select the **PingFederate Signing Certificate**.

      |   |                                                                    |
      | - | ------------------------------------------------------------------ |
      |   | Note the metadata URL for the newly-created Workato SP connection. |

## Add the PingFederate connection to Workato

1. Sign on to the Workato console as an administrator.

2. Select **Tools** in the left navigation pane.

3. Click the **Members** tab.

4. Select **Team**.

5. Select the **Settings** tab.

   ![Screen capture of the Workato Team page on the Settings tab.](_images/hol1640210179539.png)

6. Enter a **Team name** for the team or company.

7. In the **Authentication method** list, select **SAML based SSO**.

8. In the **SAML\_provider** list, select **Other**.

9. Enter the **Metadata URL** value for the Workato SP connector in PingFederate.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO Application Endpoint for the Workato SP connection.

2. Authenticate with PingFederate.

   You're redirected to your Workato domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to <https://app.workato.com/users/sign_in>.

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to Workato.

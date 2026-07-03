---
title: Configuring SAML SSO with GitHub Cloud and PingFederate
description: Learn how to enable GitHub sign-on from a PingFederate URL (IdP-initiated sign-on) and direct GitHub sign on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:github:config_saml_githubcloud_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/github/config_saml_githubcloud_pf.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-github: Create a PingFederate SP connection for GitHub
  add-the-pingfederate-idp-connection-to-github: Add the PingFederate IdP connection to GitHub
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with GitHub Cloud and PingFederate

Learn how to enable GitHub sign-on from a PingFederate URL (IdP-initiated sign-on) and direct GitHub sign on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate GitHub with at least one user to test access.

* You must have administrative access to PingFederate and GitHub.

## Create a PingFederate SP connection for GitHub

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for GitHub in Ping Federate UI:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to `https://github.com/orgs/your-tenant`.

   3. Enable the following SAML Profiles:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map **SAML\_SUBJECT** to an attribute containing the user's email address.

   5. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://github.com/orgs/your-tenant/saml/consume`.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials: Digital Signature Settings**, select the **PingFederate Signing Certificate**.

3. Save the configuration.

4. Export the signing certificate.

5. Export and then open the metadata file.

   Copy the value of the entityID and the Location entry (`https://your-value/idp/SSO.saml2`).

## Add the PingFederate IdP connection to GitHub

1. Sign on to GitHub as an administrator.

2. Select your GitHub organization.

3. Click **Organization settings**, then click **Security**.

4. Under **SAML single sign-on**, select **Enable SAML authentication**.

   |   |                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The assertion consumer service URL displayed on this screen should match the value that you entered into the PingFederate **Endpoint URL** field. |

   ![Screen capture of GitHub settings with the Enable checkbox, assertion consumer service URL, Sign on URL, Issuer URL, and Public certificate fields highlighted in red.](_images/rin1625253520648.png)

5. Set the following values.

   | Field                  | Value                                                                |
   | ---------------------- | -------------------------------------------------------------------- |
   | **Sign on URL**        | The PingFederate Location value (`https://your-value/idp/SSO.saml2`) |
   | **Issuer**             | The PingFederate entityID value.                                     |
   | **Public certificate** | Paste in the contents of the PingFederate signing certificate.       |

6. Click **Save**.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate **SSO Application Endpoint** for the GitHub SP connection.

2. Complete the PingFederate authentication.

   You're redirected to your GitHub domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to `https://github.com/orgs/your-tenant/sso`

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to GitHub.

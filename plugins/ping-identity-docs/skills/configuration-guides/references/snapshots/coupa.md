---
title: Configuring SAML SSO with Coupa and PingFederate
description: Learn how to enable Coupa sign-on from a PingFederate URL (IdP-initiated sign-on) and direct Coupa sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:coupa:config_saml_coupa_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/coupa/config_saml_coupa_pf.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  download-the-coupa-metadata: Download the Coupa metadata
  create-a-pingfederate-sp-connection-for-coupa: Create a PingFederate SP connection for Coupa
  add-the-pingfederate-idp-connection-to-coupa: Add the PingFederate IdP Connection to Coupa
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration:
---

# Configuring SAML SSO with Coupa and PingFederate

Learn how to enable Coupa sign-on from a PingFederate URL (IdP-initiated sign-on) and direct Coupa sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate Coupa with at least one user to test access.

* You must have administrative access to PingFederate and Coupa.

## Download the Coupa metadata

1. Sign on to your Coupa Admin organization as an administrator.

2. Go to `https://your_site.coupahost.com/administration/security`.

3. Select the **Sign in using SAML** check box.

4. Click the **Download and import SP metadata** link.

5. Save the Coupa metadata.

## Create a PingFederate SP connection for Coupa

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for Coupa in PingFederate using the Coupa metadata:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

      * Enable the following **SAML Profiles**:

        * **IdP-Initiated SSO**

        * **SP-Initiated SSO**

      * In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map **SAML\_SUBJECT** to the attribute containing a user's email address.

      * In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

      * In **Credentials: Digital Signature Settings** select the PingFederate signing certificate.

3. Save the configuration.

4. Export the signing certificate.

5. Export the metadata file.

## Add the PingFederate IdP Connection to Coupa

1. Sign on to your Coupa Admin organization as an administrator.

2. Go to `https://your_site.coupahost.com/administration/security`.

3. Make sure that the **Sign in using SAML** check box is selected.

4. In the **Upload IdP metadata** section, click **Choose File**.

5. Select the PingFederate metadata file and import it.

6. In the **Certificate** field, upload the PingFederate signing certificate.

7. Click **Save**.

8. Click the **Users** tab and edit the users who will use SAML authentication.

9. Set **Single Sign-On ID** to the value users will use to sign on, for example, their email address.

10. Set **Authentication method** to **SAML**.

11. Click **Save**.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO application endpoint for the Coupa SP connection.

2. Complete PingFederate authentication.

   You're redirected to your Coupa domain.

## Test the PingFederate SP-initiated SSO integration:

1. Go to your Coupa URL.

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to Coupa.

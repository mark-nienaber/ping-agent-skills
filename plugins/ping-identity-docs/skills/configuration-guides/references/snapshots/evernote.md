---
title: Configuring SAML SSO with Evernote and PingFederate
description: Learn how to enable Evernote sign on from a PingFederate URL (IdP-initiated sign-on) and direct Evernote sign on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:evernote:config_saml_evernote_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/evernote/config_saml_evernote_pf.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-evernote: Create a PingFederate SP connection for Evernote
  add-the-pingfederate-connection-to-evernote: Add the PingFederate connection to Evernote
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Evernote and PingFederate

Learn how to enable Evernote sign on from a PingFederate URL (IdP-initiated sign-on) and direct Evernote sign on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate Evernote with at least one user to test access.

* You must have administrative access to PingFederate and Evernote.

## Create a PingFederate SP connection for Evernote

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for Evernote in PingFederate:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to `https://www.evernote.com/saml2`.

   3. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation → Authentication Source Mapping → Attribute Contract Fulfillment**, map **SAML\_SUBJECT**.

   5. In **Protocol Settings → Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://www.evernote.com/SamlConsumer.action`.

   6. In **Protocol Settings → Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials → Digital Signature Settings**, select the **PingFederate Signing Certificate**.

3. Save the configuration.

4. Export the signing certificate.

5. Export the metadata, open the metadata file in a text editor, and copy the value of the Location entry (`https://your-value/idp/SSO.saml2`).

## Add the PingFederate connection to Evernote

1. Sign on to your Evernote Admin organization as an administrator and go to the Evernote Business Admin Console.

2. Go to **Security → Single Sign-On**.

3. Set **SAML HTTP Request URL** to the Location value from the metadata file that you downloaded previously (`https://your-value/idp/SSO.saml2`).

4. In a text editor, open your PingFederate signing certificate file, copy the contents, and paste your signing certificate contents into the **X.509 Certificate** field.

5. Click **Save & Enable**.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate **SSO Application Endpoint** for the Evernote SP connection.

2. Complete the PingFederate authentication.

   You're redirected to your Evernote domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to your Evernote URL.

2. Select the PingFederate sign-on option.

3. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to Evernote.

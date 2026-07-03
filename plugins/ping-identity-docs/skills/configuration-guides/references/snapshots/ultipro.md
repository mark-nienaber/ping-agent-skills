---
title: Configuring SAML SSO with UltiPro and PingFederate
description: Learn how to enable UltiPro sign-on from the PingFederate console (IdP-initiated sign-on) and direct UltiPro sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:ultipro:config_saml_ultipro_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/ultipro/config_saml_ultipro_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-ultipro: Create a PingFederate SP connection for UltiPro
  add-the-pingfederate-connection-to-ultipro: Add the PingFederate connection to UltiPro
  update-the-acs-url-values-in-pingfederate: Update the ACS URL values in PingFederate
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with UltiPro and PingFederate

Learn how to enable UltiPro sign-on from the PingFederate console (IdP-initiated sign-on) and direct UltiPro sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate UltiPro with at least one user to test access.

* You must have administrative access to PingFederate.

## Create a PingFederate SP connection for UltiPro

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for UltiPro in Ping Federate:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to `placeholder`.

      You'll change this later.

   3. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP Initiated SSO**

   4. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment,** map the **SAML\_SUBJECT**.

   5. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST**, and set **Endpoint URL** to `https://placeholder`.

      You'll change the **Endpoint URL** later.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST.**

   7. In **Credentials: Digital Signature Settings**, select the PingFederate signing certificate.

3. Export the metadata for the newly created UltiPro SP connection.

4. Export the signing certificate.

## Add the PingFederate connection to UltiPro

1. Contact UltiPro Customer Support and request that SAML 2 be enabled for your organization.

2. Provide them with the downloaded PingFederate signing certificate and metadata.

3. Request their ACS URL and EntityID values.

## Update the ACS URL values in PingFederate

1. Sign on to the PingFederate administrative console.

2. Edit the SP connection for UltiPro.

3. Set **Partner's Entity ID** to the UltiPro **Entity ID** value.

4. In **Protocol Settings: Assertion Consumer Service URL**, set **Endpoint URL** to the UltiPro **Assertion Consumer Service URL** value.

5. Save the changes.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO application endpoint for the UltiPro SP connection.

2. Complete the PingFederate authentication.

   You're redirected to your UltiPro domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to your UltiPro application.

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to UltiPro.

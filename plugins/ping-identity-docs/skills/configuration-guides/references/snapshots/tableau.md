---
title: Configuring SAML SSO with Tableau and PingFederate
description: Learn how to enable Tableau SSO in PingFederate (IdP and SP-initiated).
component: configuration_guides
page_id: configuration_guides:tableau:config_saml_tableau_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/tableau/config_saml_tableau_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  export-the-metadata-from-tableau: Export the metadata from Tableau
  create-a-tableau-sp-connection: Create a Tableau SP Connection
  import-the-metadata-in-tableau: Import the metadata in Tableau
  test-the-idp-initiated-sso-integration: Test the IdP-initiated SSO integration
  test-the-sp-initiated-sso-integration: Test the SP-initiated SSO integration
---

# Configuring SAML SSO with Tableau and PingFederate

Learn how to enable Tableau SSO in PingFederate (IdP and SP-initiated).

## Before you begin

* Configure PingFederate to authenticate against an identity repository containing the users requiring application access.

* An Email Attribute is required in the assertion, either the SAML Subject or another SAML attribute per the SAML configuration. The value of the Email Attribute must be a valid email address. This attribute is used to uniquely identify the user in the organization.

## Export the metadata from Tableau

1. Sign on to Tableau with an administration account.

2. Go to **Settings → Authentication**.

3. Select the **Enable an additional authentication method** check box.

4. Select the SAML authentication method.

5. Expand the **Edit Connection** section.

6. Click **Export Metadata**.

   ![Screen capture of Tableau Authentication types page.](_images/lrk1640220985403.png)

## Create a Tableau SP Connection

1. In PingFederate, create a service provider (SP) connection for Tableau.

2. Configure using **Browser SSO** profile **SAML 2.0**.

3. Upload the metadata file from Tableau.

4. Enable the following SAML profiles.

   * **IdP-Initiated SSO**

   * **SP-Initiated SSO**

5. Configure the assertion:

   * Select the source mappings.

   * Define the contract fulfillment.

     ![Screen capture of PingFederate mapping mathod and attribute contract fulfillment sections.](_images/ank1640221175322.png)

6. In **protocol settings: Allowable SAML Bindings**, enable **POST**.

7. Go to `https://PingFederate-url/pf/federation_metadata.ping?PartnerSpId=Tableau-EntityId` and download the metadata file from PingFederate.

## Import the metadata in Tableau

1. Upload the PingFederate metadata file and click **Apply**.

2. Confirm that the IdP entityID and SSO service URL are correct.

3. Test the connection.

4. Match the Tableau attributes to the assertion attributes and click **Apply**.

   ![Screen capture of Tableau Online Attribute page with Email and Display Name attributes shown.](_images/eej1640221622163.png)

## Test the IdP-initiated SSO integration

1. Go to the PingFederate SSO application endpoint for Tableau, `https://PingFederate-url/idp/startSSO.ping?PartnerSpId=Tableau-EntityId`.

   `https://127.0.0.1:9031/idp/startSSO.ping?PartnerSpId=https://sso.online.tableau.com/public/sp/metadata/5c142f94-8889-491a-816c-e61ae6dc84cb`

2. Authenticate with PingFederate.

   You're redirected to Tableau.

## Test the SP-initiated SSO integration

1. Go to the Tableau sign on page.

2. Enter the email address that will redirect to PingFederate.

3. Authenticate with PingFederate.

   You're redirected back to Tableau.

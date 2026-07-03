---
title: Configuring SAML SSO with Adobe Creative Cloud and PingFederate
description: Learn how to enable Adobe Creative Cloud sign-on from the PingFederate console (IdP-initiated sign-on) and direct Adobe Creative Cloud sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:adobe_creative_suite:config_saml_adobecreativecould_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/adobe_creative_suite/config_saml_adobecreativecould_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-directory-within-the-adobe-admin-portal: Create a directory within the Adobe admin portal
  create-a-pingfederate-service-provider-sp-connection-for-adobe-creative-cloud: Create a PingFederate service provider (SP) connection for Adobe Creative Cloud
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Adobe Creative Cloud and PingFederate

Learn how to enable Adobe Creative Cloud sign-on from the PingFederate console (IdP-initiated sign-on) and direct Adobe Creative Cloud sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* You must have access to the Adobe Creative Cloud Admin Portal. For this, you must have an Enterprise/Business Plan.

* Populate Adobe Creative Cloud with at least one user to test access.

* You must have administrative access in PingFederate.

## Create a directory within the Adobe admin portal

1. Sign on to the Adobe admin portal.

2. Click the **Settings** tab.

3. Select **Identity** and click **Create Directory**.

   ![Screen capture of Adobe admin portal with Create Directory highlighted in red.](_images/scs1638476915407.png)

4. Enter a name for the **Directory** and select **Federated ID**.

5. Click **Next**.

6. Select **Other SAML Providers**.

   ![Screen capture of Adobe administration console with Other SAML Providers selected as the identity provider.](_images/yxd1638476954054.png)

7. Click **Next**.

8. Download the **Copy** and note the **Entity ID** and **ACS URL** values.

## Create a PingFederate service provider (SP) connection for Adobe Creative Cloud

1. Sign on to the PingFederate administrative console.

2. Configure using **Browser SSO** profile **SAML 2.0**.

3. Set **Partner's Entity ID** to the entity ID value that you copied previously.

4. Enable the following **SAML Profiles**:

   * **IdP-Initiated SSO**

   * **SP-Initiated SSO**

5. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map the **SAML\_SUBJECT** to your email attribute, map the **FirstName** to your first name attribute, and map the **LastName** to your last name attribute.

6. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to the ACS URL value that you copied previously.

7. In **Protocol Settings: Allowable SAML Bindings**, enable **POST.**

8. In **Credentials: Digital Signature Settings**, select the **PingFederate Signing Certificate**.

9. Export the metadata file and certificate from PingFederate to upload to the Adobe Admin Console.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the **PingFederate SSO Application Endpoint** for the Adobe Creative Cloud connection.

2. Authenticate with PingFederate.

   You're redirected to your Adobe Creative Cloud.

## Test the PingFederate SP-initiated SSO integration

1. Go to your Adobe Creative Cloud.

2. When you're redirected to PingFederate, enter your PingFederate username and password.

   After successful authentication, you're redirected back to Adobe Creative Cloud.
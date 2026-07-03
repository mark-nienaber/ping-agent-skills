---
title: Configuring SAML SSO with Cloudflare and PingFederate
description: Learn how to direct Cloudflare sign on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:cloudflare:config_saml_cloudflare_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/cloudflare/config_saml_cloudflare_pf.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-service-provider-sp-connection-for-cloudflare: Create a PingFederate service provider (SP) connection for Cloudflare:
  add-the-pingfederate-idp-connection-to-cloudflare: Add the PingFederate IdP connection to Cloudflare
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Cloudflare and PingFederate

Learn how to direct Cloudflare sign on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* PingFederate's X.509 certificate should be exchanged to verify the signature in SAML assertions.

* An **Email Attribute** is required in the assertion, either the **SAML Subject** or another SAML attribute per the SAML configuration. The value of the **Email Attribute** must be a valid email address. It is used to uniquely identify the user in the organization.

* Populate Cloudflare with at least one user to test access.

## Create a PingFederate service provider (SP) connection for Cloudflare:

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for Cloudflare in PingFederate:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to `https://team name.cloudflareaccess.com/cdn-cgi/access/callback`.

   3. Enable the **IDP-Initiated SSO** and **SP-Initiated SSO** SAML profiles.

   4. In **Assertion Creation: Attribute Contract**, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress** for **SAML\_SUBJECT**.

   5. In **Assertion Creation: Authentication Source Mapping: Authentication Source Mapping**, map a new **Adapter Instance** to **HTML Form**.

   6. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map **SAML\_SUBJECT**.

   7. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `/cdn-cgi/access/callback`.

      |   |                                                     |
      | - | --------------------------------------------------- |
      |   | This value is received and updated from Cloudflare. |

   8. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   9. In **Signature Policy**, disable **Always Sign Assertion** and leave **Sign Response As Required** enabled.

   10. In **Credentials: Digital Signature Settings**, select the **PingFederate Signing Certificate**, the **Include the Certificate in the Signature *KEY INFO* Element**, and the **Include the Raw Key in the Signature *KEY INFO* Element** check boxes.

3. Save the configuration.

4. Export the signing certificate.

5. Export and then open the metadata file, and copy the value of:

   * The **entityID**

   * The **Location** entry (`https://your value/idp/SSO.saml2`)

## Add the PingFederate IdP connection to Cloudflare

1. Sign on to the Cloudflare application and click **pingfed.com** at the top of the page.

   ![Screen capture of Cloudflare application with pingfed.com as a search result.](_images/bxn1638477250767.png)

2. Go to **Access → Access App Launch → Setup Access App Launch**.

   ![Screen capture of Setup Access App Launch page in Cloudflare.](_images/jxe1638477276884.png)

3. Click **Save**.

4. Go to **Access → Login Methods → Add → SAML**.

   ![Screen capture of Cloudflare Add a SAML identity provider section.](_images/lpg1638477303049.png)

5. Click **Drop or select IdP metadata file to upload** to upload the IdP metadata file and enter the **Provider Name** value.

   ![Screen capture of Cloudflare Add a SAML identity provider section with metadata uploaded.](_images/njq1638477329500.png)

6. Click **Save** and close the **Login Method** page.

7. On the **Teams** dashboard, go to **Settings → Authentication**.

8. In the **Login methods** section, select **SAML + Pingfed**.

   ![Screen capture of Cloudflare for Teams Authentication page.](_images/anq1638477350149.png)

   The Cloudflare connection configuration is now complete.

9. Click **Test**.

10. After the Cloudflare application redirects to PingFederate, enter the credentials.

    ![Screen capture of PingFederate sign on page.](_images/twg1638477372299.png)![Screen capture of Cloudflare Access successful connection page.](_images/fkj1638477394555.png)

## Test the PingFederate SP-initiated SSO integration

1. Go to your **Cloudflare Authentication Request URL** (for example, https\://pingfed.cloudflareaccess.com/) and click **Login**.

   ![Screen capture of Cloudflare login page.](_images/qff1638477421198.png)

2. Click **SAML– PingFed**.

   ![Screen capture of Cloudflare Access with an App Launcher prompt to sign in with SAML - PingFed.](_images/kux1638477448102.png)

3. After you're redirected to PingFederate, enter your PingFederate username and password.

   After successful authentication, you're redirected back to Cloudflare.

---
title: Configuring SAML SSO with RingCentral and PingFederate
description: Learn how to enable RingCentral sign-on for the PingFederate console (IdP-initiated sign-on) and direct RingCentral sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:ringcentral:config_saml_ringcentral_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/ringcentral/config_saml_ringcentral_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  export-the-pingfederate-metadata: Export the PingFederate metadata
  configure-ringcentral-for-sso: Configure RingCentral for SSO
  create-a-pingfederate-sp-connection-for-ringcentral: Create a PingFederate SP connection for RingCentral
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with RingCentral and PingFederate

Learn how to enable RingCentral sign-on for the PingFederate console (IdP-initiated sign-on) and direct RingCentral sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users that need application access.

* Populate RingCentral with at least one user for testing access.

* You must have administrative access to PingFederate and RingCentral.

## Export the PingFederate metadata

1. In the PingFederate administrative console, go to **System → Protocol Metadata → Metadata Export**.

2. Select **I am the identity provider** then click **Next**.

3. On the **Metadata Mode** tab, select **Select information to include in metadata manually**. Click **Next**.

4. On the **Protocol** tab, click **Next**.

5. On the **Attribute Contract** tab, click **Next**.

6. On the **Signing Key** tab, select a signing certificate. Click **Next**.

7. **Optional:** On the **Metadata Signing** tab, select a certificate to sign the metadata XML file. Click Next.

8. On the **XML Encryption Certificate** tab, click **Next**.

9. On the **Export & Summary** tab, click **Export**.

10. Save the `metadata.xml` file.

11. Click **Done**.

## Configure RingCentral for SSO

1. In the RingCentral administrative console, go to **More → Security and Compliance → Single Sign-on**.

2. Select **Set up SSO by yourself**.

3. Upload the PingFederate metadata that you downloaded previously.

4. Select the email attributes to map.

5. In the **Certificate Management** section, upload the certificate and set it as the primary.

6. Download the RingCentral SP metadata file.

7. Toggle **Enable SSO** and click **Save**.

## Create a PingFederate SP connection for RingCentral

1. In the PingFederate administrative console, go to **Applications → SP Connections → Create Connection**.

2. Configure using **Browser SSO** profile **SAML 2.0**.

3. Import the RingCentral metadata file that you downloaded previously.

4. Enable the following SAML profiles:

   * **IdP-Initiated SSO**

   * **SP-Initiated SSO**

5. In **Assertion Creation: Attribute Contract**, next to **SAML\_SUBJECT**, map the **Subject Name Format** to **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

6. In **Assertion Creation: Authentication Policy Mapping: Attribute Contract Fulfillment**, map **SAML\_SUBJECT** to your email attribute.

7. In **Protocol Settings: Allowable SAML Bindings**, enable **POST** and **REDIRECT**.

8. In **Credentials: Digital Signature Settings**, in the **Signing Certificate** list, select your signing certificate.

9. Note the **SSO Application Endpoint** for your newly-created SP connection.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate **SSO Application Endpoint** for the RingCentral SP connection.

2. Authenticate with PingFederate.

   You're redirected to RingCentral.

## Test the PingFederate SP-initiated SSO integration

1. Go to <https://service.ringcentral.com/login/startupSSOLogin.html>.

2. Enter your email address and click **Submit**.

3. After you're redirected to PingFederate, enter your PingFederate username and password. s+ You're redirected to RingCentral.
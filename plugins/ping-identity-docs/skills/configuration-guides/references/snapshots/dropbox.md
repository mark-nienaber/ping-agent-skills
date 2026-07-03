---
title: Configuring SAML SSO with Dropbox and PingFederate
description: Learn how to configure SAML SSO with Dropbox and PingFederate.
component: configuration_guides
page_id: configuration_guides:dropbox:config_saml_dropbox_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/dropbox/config_saml_dropbox_pf.html
revdate: May 16, 2024
section_ids:
  create-a-pingfederate-sp-connection-for-dropbox: Create a PingFederate SP connection for Dropbox
  configure-the-pingfederate-idp-connection-for-dropbox: Configure the PingFederate IdP connection for Dropbox
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Dropbox and PingFederate

Learn how to configure SAML SSO with Dropbox and PingFederate.

## Create a PingFederate SP connection for Dropbox

1. Sign on to the PingFederate administrative console.

2. Create an SP connection in Ping Federate:

   1. Set **Partner's Entity ID** to **Dropbox**.

   2. Configure using **Browser SSO profile SAML 2.0**.

   3. Enable the following **SAML Profiles**:

      * **IDP-Initiated SSO**

      * **SP-Initiated SSO**

      * **IDP-Initiated SLO**

      * **SP-Initiated SLO**

   4. In **Assertion Creation: Attribute Contract**, set the **Subject Name Format** to `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`.

   5. In **Assertion Creation: Attribute Contract Fulfilment**, map attribute `SAML_SUBJECT` to the attribute `mail`.

   6. In **Protocol Settings**, set **Assertion Consumer Service URL:** to `https://www.dropbox.com/saml_login` and in **Allowable SAML Bindings**, enable **Redirect**.

3. Export the metadata for the newly-created SP connection.

4. Export the signing certificate public key.

   ![Screen capture of PingFederate SP Connections page.](_images/itz1625157960374.png)

## Configure the PingFederate IdP connection for Dropbox

1. Sign on to the Dropbox Admin Console as an administrator.

   ![Screen capture of Dropbox home page with Admin console on the lefthand side bar highlighted in red.](_images/spw1625156403370.png)

2. Click **Settings**.

3. Click the **Single sign-on** section.

   ![Screen capture of Dropbox Settings page with Single sign-on highlighted in red.](_images/zkb1625156484158.png)

4. For **Single sign-on**, select **Required**.

   ![Screen capture of Dropbox SSO settings with the Required button highlighted in red.](_images/tue1625158146404.png)

5. In the **Identity provider sign-in URL** field, enter the **URL Location for SingleSignOnService Location** value that you retrieved from the PingFederate SP metadata that you downloaded.

   ![Screen capture of Dropbox SSO settings with the IdP sign-in URL, X.509 certificate, and Save button all highlighted in red.](_images/vmx1625158428139.png)

   For example, `https://PingFederate-Hostname:PingFederate-Port/idp/SSO.saml2`.

6. Upload the PingFederate signing certificate that you downloaded.

7. Click **Save**.

## Test the PingFederate IdP-initiated SSO integration

Go to the **SSO Application Endpoint** value displayed in the PingFederate application configuration for the Dropbox configuration.

For example: `https://PingFederate-Hostname:PingFederate-Port/idp/startSSO.ping?PartnerSpId=Dropbox`

![Screen capture of PingFederate sign on screen.](_images/rbt1625158624275.png)![Screen capture of the Dropbox home page.](_images/vxq1625156836713.png)

## Test the PingFederate SP-initiated SSO integration

1. Go to `https://www.dropbox.com/login`.

2. Enter your email address.

   Dropbox will automatically detect that single sign-on is enabled based on the email used.

3. Click **Continue**.

   You're redirected to PingFederate for authentication.

   ![Screen capture of Dropbox sign on page.](_images/meu1625156993308.png)![Screen capture of PingFederate sign on page.](../_images/hvn1619115892208.jpg)![Screen capture of Dropbox home page.](_images/vxq1625156836713.png)

---
title: Configuring SAML SSO with Zendesk and PingFederate
description: Learn how to configure SAML SSO with Zendesk and PingFederate.
component: configuration_guides
page_id: configuration_guides:zendesk:config_saml_zendesk_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/zendesk/config_saml_zendesk_pf.html
revdate: May 16, 2024
section_ids:
  about-this-task: About this task
  create-the-pingfederate-service-provider-sp-connection-for-zendesk: Create the PingFederate service provider (SP) connection for Zendesk
  configure-the-pingfederate-idp-connection-for-zendesk: Configure the PingFederate IdP connection for Zendesk
  test-the-integration: Test the integration
---

# Configuring SAML SSO with Zendesk and PingFederate

Learn how to configure SAML SSO with Zendesk and PingFederate.

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name | Description   | Required / Optional |
| -------------- | ------------- | ------------------- |
| `SAML-SUBJECT` | Email Address | Required            |

The following table details the references that are used within this guide that are environment specific. Replace these with the suitable value for your environment.

| Reference | Description         |
| --------- | ------------------- |
| *tenant*  | Zendesk Tenant name |

## Create the PingFederate service provider (SP) connection for Zendesk

1. Sign on to the PingFederate administrative console.

2. Using the following information, create an SP connection in PingFederate:

   1. Set **Partner's Entity ID** to `https://tenant.zendesk.com`.

   2. Configure using **Browser SSO** profile **SAML 2.0**.

   3. Enable the following **SAML Profiles**.

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation → Attribute Contract Fulfillment**, set the **Subject Name Format** to `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`.

   5. In **Assertion Creation → Attribute Contract Fulfillment**, map the attribute **SAML\_SUBJECT** to the attribute `mail`.

   6. In **Protocol Settings → Assertion Consumer Service URL**, enter `https://tenant.zendesk.com/access/saml`.

   7. In **Protocol Settings → Allowable SAML Bindings**, enable **Redirect**.

   8. In **Credentials**, choose a suitable signing certificate and make sure the **Include the certificate in the signature \<KEYINFO> element** check box is selected.

3. Export the metadata for the newly-created SP connection.

4. Export the signing certificate public key.

   ![The PingFederate administrative console on the Applications > Integration > SP Connections page. The SP Connections page includes a successfully created and enabled Zendesk SP connection. A search bar with Search and Clear buttons, and a Narrow By filter. Below this is a list of the existing SP connections. The resuls are listed by Connection Name, Connection ID, Virtual ID, Protocol, Enabled which is a toggle switch set to the on position, and Action. There are Create Connection and Import Connection buttons.](_images/klx1619116894260.jpg)

## Configure the PingFederate IdP connection for Zendesk

1. Sign on to Zendesk as an administrator.

2. Click on the **Products** icon.

3. Click **Admin Centre**.

   ![A screen capture of the Zendesk Administrator home page. The Get Started page view option is clicked. On the top right of the page is a search bar, a message icon, a bell icon, the products icon, and a user icon. The products icon is clicked and displays the menu options of Support, Guides, Gather, Chat, Talk, Explore, Sell, and Admin Centre. The Admin Centre option has a light blue background when the mouse hovers over it and is highlighted.](_images/llp1618607510292.jpg)

4. Click the **Security** icon.

5. Click **Single sign-on**.

   ![A screen capture of the Admin Centre page. On the left side is a navigation pane with the icons for menu options. The Security icon which is a shield with a checkmark in the center is clicked. The Security sub-menu options has Staff Members, End users, Single sign-on, which is clicked and highlighted, and Advanced. The Single sign-on section is displayed. There are SAML and JSON Web Token configuration options with Configure buttons for each option. The SAML Configure button is highlighted.](_images/lbi1619117272068.jpg)

6. In the **SAML SSO URL** field, enter the SSO URL for your PingFederate environment configuration.

   For example:

   `https://pinghostname/idp/SSO.saml2`

7. Open the **Signing** certificate you downloaded in the PingFederate SP configuration and copy the thumbprint to the **Certificate** fingerprint.

   ![A screen capture of the Certificate dialog with the Details tab open. In the Show list, \<All> is selected. The list is organized by Field and Value. The Thumbprint line entry is selected and has a light grey background. At the bottom of the dialog is the Edit Properties button, whcich is blurred, and the Copy to File…​ button. Below these buttons is the OK button, which is highlighted with a blue outline.](_images/ghp1619117383411.jpg)

8. Select the **Enabled** check box.

   ![The SAML configuration page. The introduction sentence is SAML is an industry standard SSO framework typically used by large enterprises for communicating identities across the internet. There are fields for Enabled, which is a selected check box, SAML SSO URL, Certificate fingerprint\*, and the Remote logout URL.](_images/rvt1619117483271.jpg)

9. Click **Save**.

10. Enable external authentication for **Staff members** or **End users** as required.

    |   |                                                              |
    | - | ------------------------------------------------------------ |
    |   | The following example enables it for **Staff members** only. |

    * Click the **Security** icon.

    * Click **Staff members**.

    * Select the **External Authentication** check box.

    * Click **Single sign-on**.

    * Click **Save**.

    ![A screen capture of the Admin Centre > Security > Staff members configuration page. There are fields for External authentication, which is a checkbox that is selected, Google and Microsoft radio buttons, which aren't clicked, and a Single sign-on radio button which is clicked. At the bottom of the page is the Cancel and Save buttons.](_images/hjf1619117551464.jpg)

## Test the integration

* For PingFederate IdP-initiated SSO

  Go to the **SSO Application Endpoint** from the PingFederate application configuration to perform IdP-initiated SSO.

  For example, `https://PingFederateHostname:PingFederatePort/idp/startSSO.ping?PartnerSpId=Zendesk`.

  ![A screen capture of a SSO page. There are fields for Username and Password and a Sign On button.](../_images/hvn1619115892208.jpg)

   

* For PingOne SP-initiated SSO

  1. Go to the URL for your Zendesk tenant. For example, `https://tenant.zendesk.com`.

     |   |                                                                       |
     | - | --------------------------------------------------------------------- |
     |   | Because SSO is only enabled for Staff, you should see a sign on form. |

  2. Click **I am an Agent** to initiate SSO.

     ![A screen capture of the Zendesk sign on page. There are fields for Email and Password, a Sign in button, an I am an Agent link, which is highlighted, the Forgot my password link, and the Privacy Policy link.](_images/jwx1618609178567.jpg)![A screen capture of a SSO page. There are fields for Username and Password and a Sign On button.](_images/kjt1619119696576.jpg)

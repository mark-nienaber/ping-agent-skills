---
title: Configuring SAML SSO with HubSpot and PingFederate
description: Learn how to enable HubSpot sign-on from a PingFederate URL (IdP-initiated sign-on) and direct HubSpot sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:hubspot:config_saml_hubspot_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/hubspot/config_saml_hubspot_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-hubspot: Create a PingFederate SP connection for HubSpot
  add-the-pingfederate-connection-to-hubspot: Add the PingFederate connection to HubSpot
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with HubSpot and PingFederate

Learn how to enable HubSpot sign-on from a PingFederate URL (IdP-initiated sign-on) and direct HubSpot sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Populate HubSpot with at least one user to test access.

* You must have administrative access to PingFederate and HubSpot.

## Create a PingFederate SP connection for HubSpot

1. Obtain the HubSpot SSO details.

   1. Sign on to HubSpot, click the **Gear** icon ([icon: gear, set=fa]), and select **Account Details** from the **Settings** menu.

   2. In the **Single Sign-on** section, click **Set up**.

      ![Screen capture of HubSpot Security Settings with the Set up for Single Sign-on highlighted in red.](_images/ufh1621031728589.png)

   3. Copy the **Audience URI** and **Sign on URL, ACS, Recipient, or Redirect** values.

      ![Screen capture of HubSpot Audience URI (Service Provider Entity ID) and Sign on URL, ACS, Recipient, or Redirect fields with option to copy.](_images/gxe1621031857231.png)

2. Sign on to the PingFederate administrative console.

3. Create an SP connection for HubSpot in PingFederate.

   1. Configure using Browser SSO profile SAML 2.0.

   2. Set **Partner's Entity ID** to the HubSpot **Audience URI** value.

   3. Enable **IdP-Initiated SSO** and **SP Initiated SSO.**

   4. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map the SAML\_SUBJECT to the email attribute.

   5. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to the HubSpot **Sign on URL, ACS, Recipient, or Redirect** value.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials: Digital Signature Settings**, select the PingFederate signing certificate.

4. Export the metadata for the newly-created HubSpot SP connection.

5. Export the signing certificate.

6. Open the metadata file and copy the values of the entityID and the Location entry (`https://your-value/idp/SSO.saml2`).

## Add the PingFederate connection to HubSpot

1. Sign on to HubSpot, click the **Gear** icon ([icon: gear, set=fa]), select **Account Details**, and access the **Single Sign-on** settings.

2. Paste the entityID value that you copied previously to the **Identity Provider Identifier or Issuer URL** field.

3. Paste the Location value you copied previously to the **Identity Provider Single Sign-on URL** field.

4. Paste the PingFederate certificate into the **X.509 Certificate** field.

   ![Screen capture of HubSpot identity provider setup page with fields for inputting Identity Provider Identifier or Issuer URL, Identity Provider Single Sign-on URL, and X.509 Certificate.](_images/jkz1621032358508.png)

5. Click **Verify**.

6. In the left sidebar menu, click **Account Defaults**.

7. In the **Single Sign-on (SSO)** section, select the **Require Single Sign-on to log in** check box.

   ![Screen capture of HubSpot Security Single Sign-on (SSO) section with Require Single Sign-on to log in checked and highlighted in red.](_images/nlz1621032505904.png)

   |   |                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------- |
   |   | The user setting this up is automatically excluded to ensure their access is not lost in case of setup issues. |

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO Application Endpoint for the HubSpot SP connection.

2. Complete PingFederate authentication.

   You're redirected to your HubSpot domain.

   ![Screen capture of HubSpot Contacts page.](_images/ztx1621032651820.png)

## Test the PingFederate SP-initiated SSO integration

1. Go to <https://app.hubspot.com/login/sso>.

2. When you are redirected to PingFederate, enter your PingFederate username and password.

   After successful authentication, you're redirected back to HubSpot.

   ![Screen capture of HubSpot Contacts page.](_images/hhh1621032908474.png)

---

---
title: Configuring SAML SSO with HubSpot and PingOne for Enterprise
description: Learn how to enable HubSpot sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct HubSpot sign-on using PingOne for Enterprise (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:hubspot:config_saml_hubspot_p14e
canonical_url: https://docs.pingidentity.com/configuration_guides/hubspot/config_saml_hubspot_p14e.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  obtain-the-hubspot-sso-details: Obtain the HubSpot SSO details
  add-the-hubspot-application-to-pingone-for-enterprise: Add the HubSpot application to PingOne for Enterprise
  add-the-pingone-for-enterprise-connection-to-hubspot: Add the PingOne for Enterprise connection to HubSpot
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration
  test-the-pingone-for-enterprise-sp-initiated-sso-integration: Test the PingOne for Enterprise SP-initiated SSO integration
---

# Configuring SAML SSO with HubSpot and PingOne for Enterprise

Learn how to enable HubSpot sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct HubSpot sign-on using PingOne for Enterprise (SP-initiated sign-on).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Populate HubSpot with at least one user to test access.

* You must have administrative access to PingOne for Enterprise and HubSpot.

## Obtain the HubSpot SSO details

1. Sign on to HubSpot, click the **Gear** icon ([icon: gear, set=fa]), and select **Account Details** in the **Settings** menu.

2. In the **Single Sign-on** section, click **Set up**.

   ![The HubSpot Settings page with the Single Sign-on Set up button highlighted in red.](_images/pwn1620758047041.png)

3. Copy the **Audience URI** and **Sign on URL, ACS, Recipient, or Redirect** values.

## Add the HubSpot application to PingOne for Enterprise

1. Sign on to PingOne for Enterprise and go to **Applications → My Applications**.

2. On the **SAML** tab, click **Add Application**.

   ![Screen capture of the PingOne for Enterprise My Applications page, the SAML tab is selected and New SAML Application is selected in the Add Application list.](_images/bkh1620758762664.png)

3. For the application name, enter `HubSpot`.

4. Enter a suitable description.

5. For the category, select **CRM**.

6. Click **Continue to Next Step**.

7. Set **Assertion Consumer Service (ACS)** to the HubSpot **Sign on URL, ACS, Recipient, or Redirect** value and **Entity ID** to the **HubSpot Audience URI** value.

8. Click **Continue to Next Step**.

9. HubSpot needs the email passed in.

   * If you use an email address to sign on using PingOne for Enterprise, click **Continue to Next Step**.

   * If you sign on with a username, enter your email attribute in the **SAML\_SUBJECT** mapping, then click **Continue to Next Step**.

     ![Screen capture of the PingOne for Enterprise Attribute Mapping table. In the Identity Bridge Attribute or Literal Value column of the SAML\_Subject row, the Email attribute has been entered and is highlighted in red.](_images/jhl1620759185188.png)

10. Click **Add** for all user groups that should have access to HubSpot.

    ![Screen capture of PingOne for Enterprise Group Access section showing a list of group names with Add and Remove buttons next to them.](_images/aln1620759449599.png)

11. Click **Continue to Next Step**.

12. Copy and save the **Issuer** and **Initiate Single Sign-On (SSO) URL** values.

    ![Screen capture of PingOne for Enterprise individual identifiers, with the Issuer and Initiate Single Sign-On (SSO) URL fields highlighted in red.](_images/wqg1620761992743.png)

13. Download the PingOne for Enterprise signing certificate.

    ![Screen capture of PingOne for Enterprise Signing Certificate Download link highlighted in red.](_images/zvr1620762229725.png)

14. Click **Finish**.

## Add the PingOne for Enterprise connection to HubSpot

1. Sign on to HubSpot, click the **Gear** icon ([icon: gear, set=fa]), select **Account Details** from the **Settings** menu, and open the **Single Sign-on** settings.

2. In the **Identity Provider Identifier or Issuer URL** field, enter the PingOne for Enterprise **Issuer** value.

3. In the **Identity Provider Single Sign-on URL** field, enter the PingOne for Enterprise **Initiate Single Sign-On (SSO) URL** value.

4. Paste the PingOne for Enterprise signing certificate into the **X.509 Certificate** field.

   ![Screen capture of PingOne for Enterprise Identity Provider Identifier or Issuer URL, Identity Provider Single Sign-on URL, and X.509 Certificate fields.](_images/ibl1620762830720.png)

5. Click **Verify**.

6. In the sidebar menu, click **Account Defaults**.

7. In the **Single Sign-on (SSO)** section, select the **Require Single Sign-on to log in** check box.

   ![Screen capture of Security page, with Require Single Sign-on to log in check box checked and highlighted in red.](_images/eyj1620762997005.png)

   |   |                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------- |
   |   | The user setting this up is automatically excluded to ensure that their access is not lost in case of setup issues. |

## Test the PingOne for Enterprise IdP-initiated SSO integration

1. Go to your PingOne for Enterprise desktop as a user with HubSpot access.

   |   |                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------- |
   |   | To find the PingOne for Enterprise desktop URL in the Admin console, go to **Setup → Dock → PingOne Dock URL**. |

2. Complete PingOne for Enterprise authentication.

   You're redirected to your HubSpot domain.

   ![Screencapture of PingOne for Enterprise Sign One page.](_images/eox1620764150131.png)![Screen capture of HubSpot Contacts page.](_images/pwz1620764246852.png)

## Test the PingOne for Enterprise SP-initiated SSO integration

1. Go to <https://app.hubspot.com/login/sso>.

   You're redirected to PingOne for Enterprise.

2. Enter your PingOne for Enterprise username and password.

   ![Screen capture of PingOne for Enterprise Sign On page.](../_images/yrq1620763776078.png)

   After successful authentication, you're redirected back to HubSpot.

   ![Screen capture of HubSpot Contacts page.](_images/hmk1620764426975.png)
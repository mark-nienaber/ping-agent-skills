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

---

---
title: Configuring SAML SSO with Dropbox and PingOne for Enterprise
description: Learn how to configure SAML SSO with Dropbox and PingOne for Enterprise.
component: configuration_guides
page_id: configuration_guides:dropbox:config_saml_dropbox_p14e
canonical_url: https://docs.pingidentity.com/configuration_guides/dropbox/config_saml_dropbox_p14e.html
revdate: May 16, 2024
section_ids:
  create-a-pingone-for-enterprise-application-for-dropbox: Create a PingOne for Enterprise application for Dropbox
  configure-a-pingone-for-enterprise-idp-connection-for-dropbox: Configure a PingOne for Enterprise IdP connection for Dropbox
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration
  test-the-pingone-for-enterprise-sp-initiated-sso-integration-configuration: Test the PingOne for Enterprise SP-initiated SSO integration configuration
---

# Configuring SAML SSO with Dropbox and PingOne for Enterprise

Learn how to configure SAML SSO with Dropbox and PingOne for Enterprise.

## Create a PingOne for Enterprise application for Dropbox

1. Sign on to PingOne for Enterprise and click **Applications**.

2. On the **SAML** tab, click **Add Application**.

   ![Screen capture of PingOne for Enterprise My Applications tab in the SAML section with the Add Application drop down list displayed.](_images/nff1625154444996.png)

3. Click **Search Application Catalog** and search for `Dropbox`.

4. Click the **Dropbox** row.

   ![Screen capture of PingOne for Enterprise Application Catalog with the Dropbox SAML with Provisioning API displayed in the table.](_images/ucf1625154838404.png)

5. Click **Setup**.

6. Select the appropriate signing certificate.

7. Review the steps, and note the **PingOne for Enterprise SaaS ID**, **IdP ID**, **Initiate Single Sign-on (SSO) URL**, and **Issuer** values.

   ![Screen capture of PingOne for Enterprise Application SSO Instructions with the PingOne for Enterprise SaaS ID, IdP ID, Initiate Single Sign-on (SSO) URL, and Issuer values redacted.](_images/lya1625155514587.png)

8. Click **Continue to Next Step**.

9. Ensure **ACS URL**is set to `https://www.dropbox.com/saml_login` and **Entity ID** is set to `Dropbox`.

   ![Screen capture of PingOne for Enterprise Application Connection Configuration section with the ACS URL and Entity ID fields highlighted in red.](_images/swm1625155635402.png)

10. Click **Continue to Next Step**.

11. In the **Attribute Mapping** section, in the **Identity Bridge Attribute or Literal Value** column of the **SAML\_SUBJECT** row, select the attribute **SAML\_SUBJECT**.

    ![Screen capture of PingOne for Enterprise Application Attribute Mapping section with the Continue to Next Step button highlighted in red.](_images/vsg1625155761296.png)

12. Click **Continue to Next Step**.

13. Update the **Name**, **Description**, and **Category** fields as required.

    ![Screen capture of PingOne for Enterprise App Customization section with customizable fields for Dropbox icon, Name, Description, and Category.](_images/wki1625155864060.png)

14. Click **Continue to Next Step**.

15. Add suitable user groups for the application.

16. Click **Continue to Next Step**.

    ![Screen capture of PingOne for Enterprise Application Group Access section.](_images/zbi1625155975259.png)

17. Review the settings.

    ![Screen capture of PingOne for Enterprise Application Review Setup section with populated Icon, Name, Description, Category fields for the Dropbox application as well as redacted Connection ID, saasid, idpid, and Issuer values.](_images/ohl1625156026263.png)![Continuing from the previous screen capture, continued PingOne for Enterprise Setup Review for the Dropbox application with redacted fields and an Application Attribute table for SAML\_SUBJECT.](_images/ais1625156116343.png)

18. Copy the **Single Sign-On (SSO) URL** value to a temporary location.

    This is the IdP-initiated SSO URL that you can use for testing.

19. On the **Signing Certificate** row, click **Download** You will use this for the Dropbox configuration.

20. On the **SAML Metadata** row, click **Download**. You will use this for the Dropbox configuration.

21. Click **Finish**.

## Configure a PingOne for Enterprise IdP connection for Dropbox

1. Sign on to the Dropbox Admin Console as an administrator.

   ![Screen capture of Dropbox home page with Admin console highlighted in red on the lefthand side bar.](_images/spw1625156403370.png)

2. Click **Settings**.

3. Click the **Single sign-on** section.

   ![Screen capture of Dropbox Settings with the Single sign-on section highlighted in red.](_images/zkb1625156484158.png)

4. For **Single sign-on**, select **Required**.

   ![Screen capture of Dropbox Single sign-on settings with the Required dropdown button highlighted in red.](_images/nfw1625156554502.png)

5. In the **Identity provider sign-in URL** field, enter the **URL Location for SingleSignOnService Location** value that you retrieved from the PingOne for Enterprise SP metadata that you downloaded.

   For example, `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=idpid`

   ![Screen capture of Dropbox SSO settings with the IdP sign-in URL, X.509 certificate, and Save button highlighted in red.](_images/umm1625156664227.png)

6. Upload the PingOne for Enterprise signing certificate that you downloaded.

7. Click **Save**.

## Test the PingOne for Enterprise IdP-initiated SSO integration

1. Go to the **Single Sign-On (SSO) URL** in the PingOne for Enterprise Application configuration to perform IdP-initiated SSO.

   `https://sso.connect.pingidentity.com/sso/sp/initsso?saasid=saasid&idpid=idpid`

   ![Screen capture of PingOne for Enterprise sign on screen.](_images/qor1625156789599.png)![Screen capture of Dropbox home page.](_images/vxq1625156836713.png)

## Test the PingOne for Enterprise SP-initiated SSO integration configuration

1. Go to `https://www.dropbox.com/login`.

2. Enter your email address.

   Dropbox automatically detects that single sign-on is enabled based on the email used.

3. Click **Continue**.

   You're redirected to PingOne for Enterprise for authentication.

   ![Screen capture of Dropbox login screen.](_images/meu1625156993308.png)![Screen capture of PingOne for Enterprise sign on screen.](_images/dex1625157077622.png)![Screen capture of Dropbox home page.](_images/gwn1625157154257.png)
---
title: Configuring SAML SSO with BambooHR and PingFederate
description: The following table details the required and optional attributes to be configured in the assertion attribute contract.
component: configuration_guides
page_id: configuration_guides:bamboohr:config_saml_bamboohr_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/bamboohr/config_saml_bamboohr_pf.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result:
  choose-from: Choose from:
---

# Configuring SAML SSO with BambooHR and PingFederate

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name                                           | Description            | Required / Optional |
| -------------------------------------------------------- | ---------------------- | ------------------- |
| `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` | Email address for user | Required            |

The following table details the references that are used within this guide which are environment specific. Replace these with the suitable value for your environment.

| Reference | Description          |
| --------- | -------------------- |
| *tenant*  | BambooHR Tenant name |

## Steps

1. Create the PingFederate service provider (SP) connection for BambooHR.

   1. Sign on to the PingFederate administrative console.

   2. Using the metadata from `https://tenant.bamboohr.com/saml/sp_metadata.php`, create an SP connection in PingFederate:

      * Configure using **Browser SSO** profile **SAML 2.0**

      * Enable the **IdP-Initiated SSO** SAML profile.

      * Enable the **SP initiated SSO** SAML profile.

      * In **Assertion Creation → Attribute Contract**, set the **Subject Name Format** to **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

      * In **Assertion Creation → Attribute Contract Fulfillment**, map the attribute **SAML\_SUBJECT** to the attribute **mail**.

      * In **Protocol Settings → Allowable SAML Bindings**, enable **Redirect**.

   3. Export the metadata for the newly-created SP connection.

   4. Export the signing certificate public key.

      ![Screen capture illustrating the Applications > SP Connections page on the PingFederate administrative console.](_images/xlq1619029597861.png)

2. Configure the PingFederate identity provider (IdP) connection for BambooHR.

   1. Sign on to BambooHR as a Full Admin administrator user.

   2. On the **Settings** page, click **Apps**.

   3. On the **SAML Single Sign-On** application published by BambooHR line, click **Install**.

      ![Screen capture illustrating the SAML SSO application available for installation.](_images/clh1619029740667.png)

   4. In the **SSO Login URL** field, enter the URL Location for **SingleSignOnService Location** retrieved from the PingFederate SP metadata that you downloaded from the BambooHR configuration.

      ### Example:

      `https://PingFederateHostname:PingFederatePort/idp/SSO.saml2`

   5. In a text editor, open the signing certificate that you downloaded in from PingFederate and paste the contents into the **x.509 Certificate** field.

      ![Screen capture illustrating the SAML SSO Login URL and the x.509 Certificate metadata.](_images/gji1619029838840.png)

   6. Click **Install**.

      ### Result:

      Your configuration is complete.

      From this point BambooHR will redirect to the configured IdP for authentication for all new sessions. You should complete testing in a private or incognito browser session while keeping the original admin session active. This allows you to change settings or remove the configuration if the integration testing fails.

      ![Screen capture illustrating the SAML SSO application installed on the BambooHR website.](_images/nfy1619029926655.png)

3. Test the integration.

   ### Choose from:

   * PingFederate IdP-initiated SSO

     1. Go to the **SSO Application** in the PingFederate Application configuration to perform IdP-initiated SSO, such as https\://*PingFederateHostname*:*PingFederatePort*/idp/startSSO.ping?PartnerSpId=BambooHR-SAML.

        ![Screen capture illustrating the IdP SSO sign-on window.](_images/gof1619030025224.png)

     2. Go to the SSO Application Endpoint in the BambooHR configuration

        ![Screen capture illustrating the SSO Application endpoint in the BambooHr configuration.](_images/kre1619030073899.png)

   * PingFederate SP-initiated SSO

     Go to the URL for your BambooHR tenant: https\://*tenant*.bamboohr.com

     ![Screen capture illustrating the BambooHR tenant URL.](_images/pat1619030364471.png)

---

---
title: Configuring SAML SSO with BambooHR and PingOne for Enterprise
description: The following table details the required and optional attributes to configure in the assertion attribute contract.
component: configuration_guides
page_id: configuration_guides:bamboohr:config_saml_bamboohr_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/bamboohr/config_saml_bamboohr_p1.html
revdate: May 20, 2024
section_ids:
  about-this-task: About this task
  create-a-pingone-for-enterprise-application-for-bamboohr: Create a PingOne for Enterprise application for BambooHR.
  configure-the-pingone-for-enterprise-idp-connection-for-bamboohr: Configure the PingOne for Enterprise IdP connection for BambooHR
  example: Example:
  result: Result:
  test-the-integration: Test the integration
  choose-from: Choose from:
---

# Configuring SAML SSO with BambooHR and PingOne for Enterprise

## About this task

The following table details the required and optional attributes to configure in the assertion attribute contract.

| Attribute Name                                           | Description            | Required / Optional |
| -------------------------------------------------------- | ---------------------- | ------------------- |
| `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` | Email address for user | Required            |

The following table details the environment-specific references used in this guide. Replace these references with the suitable value for your environment.

| Reference | Description          |
| --------- | -------------------- |
| *tenant*  | BambooHR Tenant name |

## Create a PingOne for Enterprise application for BambooHR.

1. Download the BambooHR metadata from `https://tenant.bamboohr.com/saml/sp_metadata.php`.

2. Sign on to PingOne for Enterprise and go to **Applications → Application Catalog**.

3. On the **SAML** tab, in the **Add Application** list, select **Search Application Catalog**.

   ![Screen capture of the PingOne for Enterprise My Applications page on the SAML tab. The Add Application list is expanded showing the options to Search Application Catalog, New SAML Application, and Request Ping Identity add a new application to the application catalog buttons.](_images/xcr1618600994632.png)

4. Search for `BambooHR`.

5. Click the **BambooHR** row.

   ![Screen capture of the PingOne for Enterprise Application Catalog tab showing the search results for the BambooHR application.](_images/xgn1618601208139.png)

6. Click **Setup**.

7. In the **Signing Certificate** list, select the appropriate signing certificate.

   ![Screen capture of the PingOne for Enterprise SSO Instructions fields for the Application Catalog with the Signing Certificate list available for selection.](_images/jsw1618946929427.png)

8. Review the steps, and make a note of the PingOne for Enterprise **SaaS ID**, **IdP ID**, **Single Sign-On URL**, and **Issuer** values.

9. Click **Continue to Next Step**.

10. Click **Select File** and upload the BambooHR metadata you downloaded.

    |   |                                                                                                                              |
    | - | ---------------------------------------------------------------------------------------------------------------------------- |
    |   | If the upload fails, continue with the next steps and explicitly set the parameters based on the attributes in the metadata. |

11. Set the **ACS URL** to `https://tenant.bamboohr.com/saml/consume.php`.

12. Set the **Entity ID** to **BambooHR-SAML**.

    ![Screen capture of the Connection Configuration fields for the Application Catalog. The ACS URL and Entity ID fields are highlighted in red.](_images/lln1618947056171.png)

13. Click **Continue to Next Step**.

14. In the **Attribute Mapping** section, in the **Identity Bridge Attribute or Literal Value** column of the **SAML\_SUBJECT** row, select the attribute **SAML\_SUBJECT**.

    ![Screen capture of the PingOne for Enterprise Attribute Mapping fields for the Application Catalog. The Identity Bridge Attribute or Literal Value list for the SAML SUBJECT attribute is highlighted in red.](_images/ghb1618947147665.png)

15. Click **Continue to Next Step**.

16. Update the **Name**, **Description**, and **Category** fields as needed.

    ![Screen capture of the PingOne for Enterprise App Customization - BambooHR fields with the Icon, Name, Description, and Category fields displayed.](_images/nqp1618947222393.png)

17. Click **Continue to Next Step**.

18. Add the user groups for the application.

    ![Screen capture of the PingOne for Enterprise Group Name section displaying all of the available user groups.](_images/tms1618947309436.png)

19. Click **Continue to Next Step**.

20. Review your settings.

    ![Screen capture of the PingOne for Enterprise Review Setup fields for the Application Catalog displaying the configured fields for review on the BambooHR application.](_images/dkr1618947409051.png)

21. Copy the **Single Sign-On (SSO) URL** value to a temporary location.

    ![Screen capture of the PingOne for Enterprise SSO URL fields with the SSO URL value saved to a temporary location.](_images/ond1619019918822.png)

    This is the IdP-initiated SSO URL that you can use for testing.

22. On the **Signing Certificate** line, click **Download**.

    You use this in the BambooHR Cloud configuration.

23. On the **SAML Metadata** line, click **Download**.

    You use this in the BambooHR Cloud configuration.

24. Click **Finish**.

    ![Screen capture of the PingOne for Enterprise My Applications page on the SAML tab showing the available applications added to the user account.](_images/umh1619020020905.png)

## Configure the PingOne for Enterprise IdP connection for BambooHR

1. Sign on to BambooHR as a Full Admin administrator user.

2. On the **Settings** page, click **Apps**.

   ![Screen capture of the BambooHR Apps Settings page. There are no applications currently installed.](_images/oll1619020753726.png)

3. On the **SAML Single Sign-On** application published by BambooHR line, click **Install**.

   ![Screen capture of the SAML SSO application available to install on the BambooHR page.](_images/gga1619025870770.png)

4. In the **SSO Login URL** field, enter the URL Location for **SingleSignOnService Location** retrieved from the PingOne SP metadata that you downloaded from the BambooHR configuration.

   ### Example:

   `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=idpid`

   ![Screen capture of the SAML SSO Login URL and x.509 certificate metadata on the BambooHR page.](_images/now1619026060637.png)

5. In a text editor, open the signing certificate that you downloaded in the PingOne for Enterprise SP configuration and paste the contents into the **x.509 Certificate** field.

6. Click **Install**.

   ![Screen capture of the Apps Settings on BambooHR, showing the SAML Single Sign-On application installed.](_images/mrg1619026102968.png)

   ### Result:

   Your configuration is complete.

   |   |                                                                                                                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | From this point BambooHR will redirect to the configured IdP for authentication for all new sessions. You should complete testing in a private or incognito browser session while keeping the original admin session active. This allows you to change settings or remove the configuration if the integration testing fails. |

## Test the integration

### Choose from:

* PingOne for Enterprise IdP Initiated SSO

  Go to the **Single Sign-On (SSO) URL** in the PingOne Application configuration to perform IdP initiated SSO (`https://sso.connect.pingidentity.com/sso/sp/initsso?saasid=saasid&idpid=idpid`).

  ![Screen capture of the IdP initiated SSO PingOne for Enterprise Application sign-on window.](_images/eii1619026258707.png)

* PingOne SP Initiated SSO

  Go to the URL for your BambooHR tenant, https\://*tenant*.bamboohr.com

  ![Screen capture of the BambooHR Home page.](_images/gjn1619026302158.png)
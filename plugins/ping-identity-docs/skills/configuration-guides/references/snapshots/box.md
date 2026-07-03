---
title: Configuring SAML SSO with Box and PingFederate
description: Learn how to configure SAML SSO with Box and PingFederate.
component: configuration_guides
page_id: configuration_guides:box:config_saml_box_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/box/config_saml_box_pf.html
revdate: May 16, 2024
section_ids:
  about-this-task: About this task
  create-a-pingfederate-sp-connection-for-box: Create a PingFederate SP connection for Box
  configure-the-pingfederate-idp-connection-for-box: Configure the PingFederate IdP connection for Box
---

# Configuring SAML SSO with Box and PingFederate

Learn how to configure SAML SSO with Box and PingFederate.

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name | Description | Required / Optional |
| -------------- | ----------- | ------------------- |
| `SAML_SUBJECT` | Email       | Required            |
| `givenName`    | First Name  | Optional            |
| `sn`           | Last Name   | Optional            |
| `memberOf`     | Groups      | Optional            |

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

## Create a PingFederate SP connection for Box

1. Download the Box metadata from <https://cloud.app.box.com/s/9y0zm1sqgvkxe8ha2qa3dfhwoivpoyy4>.

2. Sign on to the PingFederate administrative console.

3. Using the metadata that you downloaded, create an SP connection in PingFederate:

   1. Configure using **Browser SSO profile SAML 2.0**.

   2. Enable the following **SAML Profiles**:

      * **IdP-Initiated SO**

      * **SP-Initiated SSO**

      * **IdP-Initiated SLO**

      * **SP-Initiated SLO**

   3. In **Assertion Creation: Attribute Contract**, set the **Subject Name Format** to **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

   4. Extend the contract with the following attributes:

      * **givenName**

      * **memberOf**

      * **Sn**

   5. In the **Assertion Creation: Attribute Contract Fulfillment** section:

      * Map the attribute **SAML\_SUBJECT** to the attribute **mail**.

      * Map the optional attribute **givenName** to the attribute for the user's first name.

      * Map the optional attribute **memberOf** to the attribute for the user's Box roles.

      * Map the optional attribute **Sn** to the attribute for the user's surname or family name.

   6. In **Protocol Settings**:

      * In **Assertion Consumer Service URL**, delete **Artifact** and **PAOS Bindings**.

      * In **SLO Service URLs**, delete **Artifact** and **SOAP** bindings.

      * In **Allowable SAML Bindings**, enable **Redirect** and **POST**.

4. Export the metadata for the newly-created SP connection.

5. Export the signing certificate public key.

   ![Screen capture of PingFederate SP Connections page.](_images/omb1625087491743.png)

## Configure the PingFederate IdP connection for Box

1. Sign on to the Box Admin Console as an administrator.

   ![Screen capture of the Box Admin Console with the Settings icon on the lefthand sidebar highlighted in red.](_images/tfw1625087801073.png)

2. Click **Enterprise Settings**.

3. Click the **User Settings** tab.

4. In the **Configure Single Sign On (SSO) for All Users** section, click **Configure**.

   ![Screen capture of the Box User Settings tab highlighted in red and the Configure button for Configure Single Sign On (SSO) for All Users highlighted in red.](_images/hpv1625087938902.png)

5. Click **'I don't see my provider, or don't have a metadata file.'**

6. Complete the **Box SSO Setup Support Form**:

   1. Review the request form and the **For faster service please read** section.

   2. Complete the required fields:

      * For **Who is your Identity Provider?**, select **Other with Metadata**.

      * For **What is the attribute for the user's email?**, select **SAML\_SUBJECT**.

      * For **What is the attribute for groups?**, select **memberOf**.

      * For **What is the attribute for the user's first name?**, select **givenName**.

      * For **What is the attribute for the user's last name?**, select **Sn**.

      * Attach the metadata that you downloaded from the PingFederate configuration.

7. Click **Submit**.

   ![Screen capture of the Box SSO Setup Support Form.](_images/kdp1625088309558.png)

8. After the Box support team completes the configuration, follow any provided instructions and test the integration.

---

---
title: Configuring SAML SSO with Box and PingOne for Enterprise
description: Learn how to configure SAML SSO with Box and PingOne for Enterprise.
component: configuration_guides
page_id: configuration_guides:box:config_saml_box_p14e
canonical_url: https://docs.pingidentity.com/configuration_guides/box/config_saml_box_p14e.html
revdate: May 16, 2024
section_ids:
  about-this-task: About this task
  create-a-pingone-for-enterprise-application-for-box: Create a PingOne for Enterprise application for Box
  configure-the-pingone-for-enterprise-idp-connection-for-box: Configure the PingOne for Enterprise IdP connection for Box
---

# Configuring SAML SSO with Box and PingOne for Enterprise

Learn how to configure SAML SSO with Box and PingOne for Enterprise.

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name | Description | Required / Optional |
| -------------- | ----------- | ------------------- |
| `SAML_SUBJECT` | Email       | Required            |
| `givenName`    | First Name  | Optional            |
| `sn`           | Last Name   | Optional            |
| `memberOf`     | Groups      | Optional            |

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

## Create a PingOne for Enterprise application for Box

1. Download the Box metadata from <https://cloud.app.box.com/s/9y0zm1sqgvkxe8ha2qa3dfhwoivpoyy4>.

2. Sign on to PingOne for Enterprise and click **Applications**.

3. On the **SAML** tab, click **Add Application**.

   ![Screen capture of the My Applications tab in PingOne for Enterprise with the drop down list from the Add Application button displaying the following options: Search Application Catalog, New SAML Application, and Request Ping Identity add a new application to the application catalog.](_images/qak1625080926253.png)

4. Click **Search Application Catalog** and search for `Box`.

5. Click the **Box** row.

   ![Screen capture of PingOne for Enterprise Application table. The Box row is expanded, detailing the icon, name, description, and category of the application with a Setup button in the bottom right corner.](_images/zyv1625083493626.png)

6. Click **Setup**.

7. Select the appropriate signing certificate.

8. Review the steps, and note the **PingOne for Enterprise SaaS ID**, **IdP ID**, **Initiate Single Sign-on (SSO) URL**, and **Issuer** values.

   ![Screen capture of PingOne for Enterprise SSO Instructions with the PingOne for Enterprise SaaS ID, IdP ID, Initiate Single Sign-on (SSO) URL, and Issuer values redacted.](_images/ogi1625083817453.png)

   1. Click **Continue to Next Step**.

   2. In the **Upload Metadata** section, click **Select File**, and upload the Box metadata file that you downloaded.

   3. Ensure that **ACS URL** is set to `https://sso.services.box.net/sp/ACS.saml2` and **Entity ID** is set to `box.net`.

   ![Screen capture of PingOne for Enterprise Connection Configuration section with a sample XML file uploaded in the Upload Metadata field and the ACS URL and Entity ID filled out in accordance with the above instructions.](_images/zan1625083902341.png)

9. Click **Continue to Next Step**.

10. In the Attribute Mapping section, in the **Identity Bridge Attribute or Literal Value**column of the **SAML\_SUBJECT**row, select the attribute **SAML\_SUBJECT**.

11. Complete the remaining attribute mappings for **givenName**, **sn**, **memberOf**, and **title**.

    ![Screen capture of PingOne for Enterprise Attribute Mapping section with the SAML\_SUBJECT, givenName, sn, memberOf, and title fields input to the Application Attribute table.](_images/iiy1625084340407.png)

12. Click **Continue to Next Step**.

13. Update the **Name**, **Description**, and **Category** fields as required.

    ![Screen capture of PingOne for Enterprise App Customization - Box section with the Name, Description, and Category fields filled out.](_images/wed1625084654775.png)

14. Click **Continue to Next Step**.

15. Add suitable user groups for the application.

    ![Screen capture of PingOne for Enterprise Group Access section with a search bar to search for applicable groups and add them to the table below it.](_images/jfq1625084778628.png)

16. Click **Continue to Next Step**.

17. Review the settings.

    ![Screen capture of PingOne for Enterprise Review Setup section with all the previously populated Box application information displayed for reference and verification.](_images/ywo1625084896788.png)![Continuing from the previous screen capture, this screen capture of PingOne for Enterprise Review Setup page displays the Application Attribute table with columns for Description and Identity Bridge Attribute or Literal Value.](_images/foz1625084972368.png)

18. Copy the **Single Sign-On (SSO) URL** value to a temporary location.

    This is the IdP-initiated SSO URL that you can use for testing.

19. On the **SAML Metadata** row, click **Download**. You will use this for the Box configuration.

20. Click **Finish**.

## Configure the PingOne for Enterprise IdP connection for Box

1. Sign on to the Box Admin Console as an administrator.

   ![Screen capture of Box Developer Plan homepage with the Settings icon on the left sidebar highlighted in red.](_images/adk1625085299452.png)

2. Click **Enterprise Settings**.

3. Click the **User Settings** tab.

4. In the **Configure Single sign-on (SSO) for All Users** section, click **Configure**.

   ![Screen capture of Box User Settings and the Configure button under Configure Single Sgn On (SSO) for All Users both highlighted in red.](_images/ddh1625085427780.png)

5. Click **I don't see my provider, or don't have a metadata file.**

6. Complete the **Box SSO Setup Support Form**:

   * Review the request form and the **For faster service please read** section.

   * Complete all the required fields.

     * For **Who is your Identity Provider**, select **Other with Metadata**.

     * For **What is the attribute for the user's email?**, select **SAML\_SUBJECT**.

     * For **What is the attribute for groups?**, select **memberOf**.

     * For **What is the attribute for the user's first name?**, select **givenName**.

     * For **What is the attribute for the user's last name?**, select **Sn**.

     * Attach the metadata that you downloaded from the PingOne for Enterprise configuration.

   * Click **Submit**.

     ![Screen capture of Box SSO Setup Support Form.](_images/tgi1625085837505.png)

7. After the Box support team completes the configuration, follow any provided instructions and test the integration.
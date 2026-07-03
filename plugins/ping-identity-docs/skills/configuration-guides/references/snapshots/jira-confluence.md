---
title: Configuring SAML SSO with Jira/Confluence and PingFederate
description: Learn how to configure SAML single sign-on with Jira/Confluence on premise and PingFederate.
component: configuration_guides
page_id: configuration_guides:jira_confluence:config_saml_jira_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/jira_confluence/config_saml_jira_pf.html
revdate: May 15, 2024
section_ids:
  about-this-task: About this task
  create-a-pingfederate-sp-connection-for-jiraconfluence: Create a PingFederate SP Connection for Jira/Confluence
  configure-the-pingfederate-idp-connection-for-jiraconfluence-on-premise: Configure the PingFederate IdP connection for Jira/Confluence on premise
---

# Configuring SAML SSO with Jira/Confluence and PingFederate

Learn how to configure SAML single sign-on with Jira/Confluence on premise and PingFederate.

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name    | Description | Required / Optional |
| ----------------- | ----------- | ------------------- |
| **SAML\_SUBJECT** | Username    | Required            |

## Create a PingFederate SP Connection for Jira/Confluence

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

1. Sign on to Atlassian application as an administrator and go to **Administration → System → SAML Authentication**.

2. Select **SAML Single Sign On**and note the **Audience URL (Entity ID)** and **Assertion Consumer Service URL** values.

3. Download the signing certificate.

4. Sign on to the PingFederate administrative console.

5. Using the details retrieved from the Atlassian application UI:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Enable **IdP-Initiated SSO** and **SP Initiated SSO**.

   3. In **Assertion Creation: Attribute Contract**, set the Subject Name Format to `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`.

   4. In the **Assertion Creation: Attribute Contract Fulfilment**, map the attribute **SAML\_SUBJECT** to the attribute **username**.

   5. In **Protocol Settings: Allowable SAML Bindings**, enable **Post** and **Redirect**.

6. Export the metadata for the newly-created SP connection.

7. Export the signing certificate public key.

## Configure the PingFederate IdP connection for Jira/Confluence on premise

1. Sign on to Atlassian application as an administrator and go to **Administration → System → SAML Authentication**.

2. Select **SAML Single Sign-On**.

3. Configure the following.

   | Setting                                  | Value                                                                                                                                                         |
   | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Single sign-on issuer**                | The issuer ID for your PingFederate instance. You can retrieve this from the metadata that you downloaded.                                                    |
   | **Identity provider single sign-on URL** | The PingFederate **SingleSignOnService** URL. You can retrieve this from the metadata that you downloaded. For example, `https://hostname:port/idp/SSO.saml2` |
   | **X509 Certificate**                     | Upload the PingFederate signing public certificate.                                                                                                           |
   | **Login Mode**                           | Choose whether SAML is primary or secondary authentication.                                                                                                   |

   Configuration is complete.

---

---
title: Configuring SAML SSO with Jira/Confluence and PingOne for Enterprise
description: Learn how to configure SAML single sign-on (SSO) with Jira/Confluence on premise and PingOne for Enterprise.
component: configuration_guides
page_id: configuration_guides:jira_confluence:config_saml_jira_p14e
canonical_url: https://docs.pingidentity.com/configuration_guides/jira_confluence/config_saml_jira_p14e.html
revdate: May 15, 2024
section_ids:
  about-this-task: About this task
  create-a-pingone-for-enterprise-application-for-jiraconfluence-on-premise: Create a PingOne for Enterprise application for Jira/Confluence on premise
  configure-the-pingone-for-enterprise-idp-connection-for-jiraconfluence-on-premise: Configure the PingOne for Enterprise IdP Connection for Jira/Confluence on-premise
---

# Configuring SAML SSO with Jira/Confluence and PingOne for Enterprise

Learn how to configure SAML single sign-on (SSO) with Jira/Confluence on premise and PingOne for Enterprise.

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name    | Description | Required / Optional |
| ----------------- | ----------- | ------------------- |
| **SAML\_SUBJECT** | Username    | Required            |

|   |                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A predefined application exists in the application catalog for use with Atlassian Cloud. It is recommended that this is used for Atlassian Cloud integrations. |

## Create a PingOne for Enterprise application for Jira/Confluence on premise

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

1. Sign on to the Atlassian application as an administrator and go to **Administration → System → SAML Authentication**.

2. Select **SAML Single Sign On** and note the **Audience URL (Entity ID)** and **Assertion Consumer Service URL** values.

3. Download the signing certificate.

4. Sign on to PingOne for Enterprise and click **Applications**.

5. On the **SAML** tab, click **Add Application**.

6. Click **New SAML Application**.

   ![Screen capture of PingOne for Enterprise SAML Application table. Below, the Add Application button drops down and the New SAML Application option is highlighted in red.](_images/soi1621019839814.png)

7. In the **Application Details** section, enter the following:

   * A suitable application name, such as Confluence.

   * A suitable description.

   * A suitable category, such as **Information Technology**.

   * (Optional) Upload an icon to be used in the PingOne for Enterprise dock.

   ![Screen capture of PingOne for Enterprise Application Details with the fields for Application Name, Application Description, and Category drop down list all asterisked and Graphics as an optional field.](_images/sui1621020048315.png)

8. Click **Continue to Next Step**.

9. Select **I have the SAML configuration**.

10. In the **Signing Certificate list**, select a suitable signing certificate.

11. For **Protocol Version**, click **SAML v.2.0**.

12. In the **Assertion Consumer Service (ACS)** field, enter the ACS value from the Atlassian single sign-on settings.

13. In the **Entity ID** field, enter the **Entity ID** value from the Atlassian single sign-on settings.

14. For **Primary Verification Certificate**, select the signing certificate that you downloaded.

    ![Screen capture of PingOne for Enterprise Signing Certificate section with PingOne for Enterprise Account Origination Certificate (2021) selected from the drop down list.](_images/wwd1621020417254.png)

15. Click **Continue to Next Step**.

16. In the **SSO Attribute Mapping** section, add the following mapping for the **SAML\_SUBJECT**:

    * For **Identity Bridge Attribute or Literal Value**, select the appropriate attribute. This should match the username for the user in the application.

    * Select the **Required** check box.

    ![Screen capture of PingOne for Enterprise SSO Attribute Mapping section with SAML\_SUBJECT input as the Application Attribute.](_images/bzy1621021573439.png)

17. Click **Continue to Next Step**.

18. Add the user groups for the application.

    ![Screenshot of the Group Access tab](_images/nsf1621021652829.png)

19. Click **Continue to Next Step**.

20. Review the settings.

    ![Screen capture of PingOne for Enterprise application connection test page.](_images/pbe1621021712614.png)

21. Copy the **Single Sign-On (SSO) URL** value to a temporary location.

    This is the IdP-initiated SSO URL that you can use for testing.

22. Note the **idpid** and **Issues** values.

23. On the **Signing Certificate** line, click **Download**.

    You'll use this for the application configuration.

24. On the **SAML Metadata** line, click **Download**.

    You'll use this for the application configuration.

25. Click **Finish**.

## Configure the PingOne for Enterprise IdP Connection for Jira/Confluence on-premise

1. Sign on to the Atlassian application as an administrator.

2. Go to **Administration → System → SAML Authentication**.

3. Select **SAML Single Sign On**.

4. Configure the following.

   | Setting                                  | Value                                                                                                                                                                                                                                                |
   | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Single sign-on issuer**                | The issuer from PingOne for Enterprise application details noted earlier.                                                                                                                                                                            |
   | **Identity provider single sign-on URL** | Enter the **Single Sign-On Service URL** in the following form, using the idpid previously noted. `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=idpid`Alternatively, you can retrieve the URL from the metadata that you downloaded. |
   | **X509 Certificate**                     | Upload the PingOne for Enterprise signing public certificate that you downloaded.                                                                                                                                                                    |
   | **Login Mode**                           | Choose whether SAML is your primary or secondary authentication.                                                                                                                                                                                     |

   Configuration is complete.
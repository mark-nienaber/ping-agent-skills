---
title: Configuring SAML SSO with ServiceNow and PingOne for Enterprise
description: Learn how to configure SAML SSO with ServiceNow and PingOne for Enterprise
component: configuration_guides
page_id: configuration_guides:servicenow:config_saml_servicenow_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/servicenow/config_saml_servicenow_p1.html
revdate: May 20, 2024
section_ids:
  about-this-task: About this task
  create-a-pingone-for-enterprise-application-for-servicenow: Create a PingOne for Enterprise application for ServiceNow
  configure-the-pingone-for-enterprise-idp-connection-for-servicenow: Configure the PingOne for Enterprise IdP connection for ServiceNow
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration
  test-the-pingone-for-enterprise-sp-initiated-sso-integration: Test the PingOne for Enterprise SP-initiated SSO integration
---

# Configuring SAML SSO with ServiceNow and PingOne for Enterprise

Learn how to configure SAML SSO with ServiceNow and PingOne for Enterprise

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name | Description                                                             | Required / Optional |
| -------------- | ----------------------------------------------------------------------- | ------------------- |
| NameID         | NameID and format is configurable in ServiceNow. This guide uses email. | Required            |

The following table details the references that are used within this guide that are environment specific. Replace these with the suitable value for your environment.

| Reference | Description                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------- |
| `tenant`  | The instance name for your ServiceNow tenant you want to integrate with PingOne for Enterprise. |

## Create a PingOne for Enterprise application for ServiceNow

1. Sign on to PingOne for Enterprise and go to **Applications → Application Catalog**.

2. Search for `ServiceNow` and then click the **ServiceNow** row.

   ![A screen capture of the PingOne Application Catalog tab. There is a search bar and button to browse applications that you want to add. The search entry contains servicenow. There is a list of the matching search results for ServiceNow, listed by an image of the application icon, Application Name, Type, and setup button, which looks like a black triangle pointing to the right, displayed in rows.](_images/cha1619137357749.jpg)

3. Click **Setup**.

4. Review the steps and make a note of the **PingOne SaaS ID**, **IdP ID**, **Single Sign-on URL**, and **Issuer** values.

   ![A screen capture of the 1. SSO Instructions section. There are fields for Signing Certificate and the Download option, Saas ID, IdP ID, Initiate Single Sign-On (SSO) URL, and Issuer.](_images/mmr1619137422179.jpg)

5. Click **Continue to Next Step**.

6. Verify the following:

   * **ACS URL** is set to `https://tenant.service-now.com/navpage.do`.

   * **Entity ID** is set to `https://tenant.service-now.com`.

   ![A screen capture of the 2. Connection Configuration section. The sentence introduction is Assign the attribute values for single sign-on (SSO) to the application. There are fields for Upload Metadata, ACS URL, Entity ID, Target Resource, Single Logout Endpoint, Single Logout Response Endpoint, Primary Verification Certificate with the Choose File button, Secondary Verification Certificate with the Choose File button, and a Force Re-authentication check box, which is cleared.](_images/huu1619137603531.jpg)

7. Click **Continue to Next Step**.

8. In the **Attribute Mapping** section, in the **Identity Bridge Attribute or Literal Value** column of the **SAML\_Subject** row, select a suitable attribute, such as **SAML\_SUBJECT**.

   ![A screen capture of the 3. Attribute Mapping section. The sentence introduction is Map your identity bridge to the attributes required by the application. The mapping attribute fields are Application Attribute, Description, and Identity Bridge Attribute or Literal Value. The fields have default entries for Application Attribute and Description. The Identity Bridge Attribute or Literal Value field requires an entry from the user and has a As Literal check box, which is cleared. There are Add new attribute, Cancel, Back, and Continue to Next Step buttons.](_images/hqs1619137732986.jpg)

   NameID is configurable in ServiceNow.

   |   |                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------ |
   |   | This guide assumes email is used and that **SAML\_SUBJECT** contains the email address for the user in PingOne for Enterprise. |

9. Click **Continue to Next Step**.

10. Update the **Name**, **Description**, and **Category** fields as required.

    ![A screen capture of the 4. PingOne App Customization – ServiceNow section. There are fields for Icon with a Select Image button, Name, Description, and Category. At the bottom of the section, on the left side is the text, NEXT: Group Access and on the right side is the Cancel, Back and Continue to Next Step buttons.](_images/jxp1619137809993.jpg)

11. Click **Continue to Next Step**.

12. Add suitable user groups for the application.

    ![A screen capture of the 5. Group Access section. The sentence introduction is Select all user groups that should have access to this application. Users that are members of the added groups will be able to SSO to this application and will see this application on their personal dock. There is a search bar and a Search button. There is a list showing results for Groups listed by Group Name. Each entry has the Group Name and a Remove button. At the bottom of the section, on the left is NEXT: Review Setup, and on the right is the Continue to Next Step button.](../_images/mxk1618606036124.jpg)

13. Click **Continue to Next Step**.

14. Review the settings.

    ![A screen capture of the 6. Review Setup section. The section introduction is Test your connection to the application. There are fields for Icon, Name, Description, Category, Connection ID, saasid, idpid, Issuer, Signing, Signing Algorithm, and Encrypt Assertion.](_images/jwd1619137927219.jpg)![A screen capture of the 6. Review Setup section. There are fields to review for Single Sign-On (SSO) Relay State, Single Logout Endpoint, Single Logout Response Endpoint, Force Re-authentication, Signing Certificate, SAML Metadata, SAML Metadata URL, and a list of the existing Mapped Application Attributes. There are Back and Finish buttons.](_images/hbb1619137982716.jpg)

15. Copy the **Single Sign-On (SSO) URL** value to a temporary location.

    This is the IdP-initiated SSO URL that you can use for testing.

    |   |                                                                                                                                                                    |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | Make a note of the following values. You'll use them later in the ServiceNow configuration:- PingOne for Enterprise **Issuer**

    - PingOne for Enterprise **idpid** |

16. On the **SAML Metadata** line, click **Download**.

    You will use this later for the ServiceNow configuration.

17. On the **Signing Certificate** line, click **Download**.

    You will use this later for the ServiceNow configuration.

18. Click **Finish**.

    ![A screen capture of the My Applications section. The section introduction is Applications you've added to your account are listed here. You can search by application name, description or entity ID. A bulleted list of 2 sentences follow: Active applications are enabled for single sign-on (SSO) and Details displays the application details. Below this is a list of all the added applications, listed by application icon, Application Name, Type, Status, Enabled, which is a toggle switch, and the Remove button with a setup icon, which is a black triangle turned to the right. At the bottom of the section, on the left side is the Add Application button, and on the right side is the Pause All SSO button.](_images/dbc1619138067274.jpg)

## Configure the PingOne for Enterprise IdP connection for ServiceNow

1. Sign on to ServiceNow as an administrator.

2. Activate SAML 2.0:

   1. Go to **System Applications**.

   2. Click **All Available Applications**.

   3. Click **All**.

   4. Locate the **Integration - Multiple Provider Single Sign-On Installer** plugin.

      |   |                                                                                    |
      | - | ---------------------------------------------------------------------------------- |
      |   | If you can't find the plugin, you can request it from ServiceNow customer support. |

      ![A screen capture of the Service Now admin console in the System Application section. In the navigation bar, System Applications, All Available Applications with the All option are highlighted. The All Applications search results are showing results for sign-on. The Integration – Multiple Provider Sign-on Installer section is highlighted. The section has an installed button, which indicates the plugin is installed.](_images/epp1619138156255.jpg)

   5. Check if the plugin is installed. If the plugin is not installed, click **Install**.

      ![A screen capture of the System Plugin section. There are fields for ID, Name, Version, Provider, Status, which is highlighted, Has demo data with a selected checkbox, Help, Requires, and Description.](_images/dne1619138232034.jpg)

3. Configure a new identity provider:

   1. In the left navigation pane, select **Multi-Provider SSO**.

      ![A screen capture of the Identity Providers section, In the left navigation pane, Multi-Provider SSO and Identity Providers are highlighted and selected. In the Identity Providers page, The New button, which is green, is selected and highlighted.](_images/loa1619138332405.jpg)

   2. Click **Identity Providers**.

   3. Click **New**.

   4. Click **SAML**.

      ![A screen capture of the Identity Providers section, where you add a new SSO Identity Provider. The section introduction is What kind of SSO are you trying to create? There are 3 options to choose from: Digest, SAML, and OpenID Connect. The SAML option is highlighted.](_images/vru1619138381492.jpg)

   5. Click **XML**.

   6. Paste the contents of the PingOne for Enterprise metadata file that you previously downloaded into the **Enter the XML** field.

      ![A screen capture of the Import Identity Provider Metadata dialog in the 3. Entering metadata manually by closing this popup section. There are two radio buttons, URL and XML. The XML radio button is clicked. The Enter the XML field contains pasted XML metadata. There are two buttons, Cancel and Import, which is green.](_images/zoo1619138487643.jpg)

   7. Update the **NameID Policy** to `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`.

   8. Click **Update**.

   9. Click **Test**.

      A browser window opens to validate the configuration. It prompts you to authenticate at the IdP and then sign out of the session. If successful, you can then activate the connection.

   10. Click **Activate**.

   If you receive an error stating that you must test the connection, something failed in the test. Validate the settings, and use the **Script Debugger → Debug** log to re-run the test to determine the cause of the failure.

   ![A screen capture of the Identity Provider create new section. There are fields for Name, Default, Active, and Auto Redirect IdP, which are all check boxes, Identity Provider URL, Identity Provider's AuthnRequest, Identity Provider's SingleLogoutRequest, ServiceNow Homepage, EntityID / Issuer, Audience URI, NameID Policy, and External logout redirect.](_images/upx1619138561635.jpg)

## Test the PingOne for Enterprise IdP-initiated SSO integration

1. Go to the **Single Sign-On (SSO) URL** from the PingOne for Enterprise application configuration to perform IdP-initiated SSO.

   For example, `https://sso.connect.pingidentity.com/sso/sp/initsso?saasid=saasid&idpid=idpid`

   ![A screen capture of the Ping Identity Sign On page. The page has the Username and Password fields, which are blank. Below these fields is the Remember Me check box, which is cleared, the Sign On button, and the Forgot Password link.](../_images/hzi1618945469130.png)![A screen capture System Administration dashboard. The dashboard has settings by icons for Guided Setup, System Security, Business Logic, Create and Deploy, Data Management, Diagnostics, Email, Homepages, and Integration.](_images/yqi1619138856840.jpg)

## Test the PingOne for Enterprise SP-initiated SSO integration

1. Go to your ServiceNow URL.

   For example, `https://your-environment.service-now.com`

   ![A screen capture of the PingOne Sign On page. The page has the Username and Password fields, which are blank. Below these fields is the Remember Me check box, which is cleared, the Sign On button, and the Forgot Password link.](../_images/hzi1618945469130.png)![A screen capture of the ServiceNow sign on page. There are the Username and Password fields, a Login button, and a Use external login link, which is highlighted.](_images/vcw1619138935426.jpg)

2. Click **Use external login**.

   ![A screen capture of the ServiceNow External login page. There is a User ID field, a Use local Login link, and a Submit button, which is highlighted.](_images/pkc1619138999446.jpg)

3. Click **Submit**.

4. Click **Continue**.

   You're redirected to PingOne for Enterprise for authentication.

5. After you're redirected to PingOne for Enterprise, enter your PingOne username and password.

   ![A screen capture of the PingOne Sign On page. The page has the Username and Password fields, which are blank. Below these fields is the Remember Me check box, which is cleared, the Sign On button, and the Forgot Password link.](../_images/hzi1618945469130.png)![A screen capture System Administration dashboard. The dashboard has settings by icons for Guided Setup, System Security, Business Logic, Create and Deploy, Data Management, Diagnostics, Email, Homepages, and Integration.](_images/yqi1619138856840.jpg)

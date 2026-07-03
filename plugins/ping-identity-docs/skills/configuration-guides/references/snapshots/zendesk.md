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

---

---
title: Configuring SAML SSO with Zendesk and PingOne
description: Learn how to configure SAML SSO with ZenDesk and PingOne.
component: configuration_guides
page_id: configuration_guides:zendesk:config_saml_zendesk_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/zendesk/config_saml_zendesk_p1.html
revdate: May 16, 2024
section_ids:
  about-this-task: About this task
  create-a-pingone-application-for-zendesk: Create a PingOne Application for Zendesk
  configure-the-pingone-idp-connection-for-zendesk: Configure the PingOne IdP connection for Zendesk
  test-the-integration: Test the integration
  choose-from: Choose from:
---

# Configuring SAML SSO with Zendesk and PingOne

Learn how to configure SAML SSO with ZenDesk and PingOne.

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name | Description   | Required / Optional |
| -------------- | ------------- | ------------------- |
| `SAML-SUBJECT` | Email Address | Required            |

The following table details the references that are used within this guide that are environment specific. Replace these with the suitable value for your environment.

| Reference | Description         |
| --------- | ------------------- |
| `tenant`  | Zendesk Tenant name |

## Create a PingOne Application for Zendesk

1. Sign on to PingOne for Enterprise and go to **Applications → Application Catalog**.

2. Search for `Zendesk`.

3. Click the **Zendesk** row.

   ![Screen capture of the PingOne Applications page with the Application Catalog tab clicked. There is a application catalog search bar and button. The search results show all the matching results for Zendesk, listed by the application icon, Application Name, and Type fields. In the same row, to the right of the Zendesk search results is a black arrowhead pointing right.](_images/mby1618603520982.jpg)

4. Click **Setup**.

5. In the **Signing Certificate** list, select the appropriate signing certificate.

   ![A screen capture of the 1. SSO Instructions section. There are fields for Signing Certificate and the Download option, Saas ID, IdP ID, Initiate Single Sign-On (SSO) URL, and Issuer.](_images/xsh1618603854792.jpg)

6. Review the steps, and make a note of the **PingOne SaaS ID**, **IdP ID**, **Single Sign-On URL**, and **Issuer** values shown.

7. Click **Continue to Next Step**.

8. Make sure that **ACS URL** is set to `https://tenant.zendesk.com/access/saml`.

9. Make sure that **Entity ID** is set to `https://tenant.zendesk.com`.

   ![A screen capture of the 2. Connection Configuration section. The introduction sentence is Assign the attribute values for single sign-on (SSO) to the application. There are fields for Upload Metadata with a Select File button and Or use URL option, ACS URL, Entity ID, Target Resource, Single Logout Endpoint, Single Logout Response Endpoint, Primary Verification Certificate, Secondary Verification Certificate, Force Re-authentication check box, Encrypt Assertion check box, Signing with two radio buttons, Sign Assertion, which is clicked, and Sign Response, which is not clicked.](_images/xjy1618604631386.jpg)

10. Click **Continue to Next Step**.

11. In the **Attribute Mapping** section, in the **Identity Bridge Attribute or Literal Value** column of the **SAML\_SUBJECT**row, enter `SAML_SUBJECT`.

    ![A screen capture of the 3. Attribute Mapping section. The sentence introduction is Map your identity bridge to the attributes required by the application. The are fields for Application Attribute, Description, and Identity Bridge Attribute or Literal Value. All the fields have default entries for Application Attribute and Description. The Identity Bridge Attribute or Literal Value field requires an entry from the user and has a cleared As Literal check box and Advanced button in all rows.](_images/vea1618605563887.jpg)

12. Enter the values for the other attributes as required.

13. Click **Continue to Next Step**.

14. Update the **Name**, **Description**, and **Category** fields as required.

    ![A screen capture of the 4. PingOne App Customization – Zendesk section. There are fields for Icon with a Select Image button, Name, Description, and Category. At the bottom of the section, on the left side is the text, "NEXT: Group Access" and on the right side is the Cancel, Back and Continue to Next Step buttons.](_images/ocg1618605861823.jpg)

15. Click **Continue to Next Step**.

16. Add the user groups for the application.

    ![A screen capture of the 5. Group Access section. The sentence introduction is Select all user groups that should have access to this application. Users that are members of the added groups will be able to SSO to this application and will see this application on their personal dock. There is a search bar with a Search button. The search results are listed by Group Name. Both entries have a Remove button. There is a Continue to Next Step button.](../_images/mxk1618606036124.jpg)

17. Click **Continue to Next Step**.

18. Review the settings.

    ![A screen capture of the 6. Review Setup section. The introduction sentence is Test your connection to the application. There are fields for Icon, Name, Description, Category, Connection ID, saasid, and idpid.](_images/caq1618606174261.jpg)

19. Copy the **Single Sign-On (SSO) URL** value to a temporary location.

    This is the IdP-initiated SSO URL that you can use for testing.

    1. On the **Signing Certificate** line, click **Download**.

       You'll use this in the Zendesk configuration.

20. On the **SAML Metadata** line, click **Download**.

    You'll use this in the Zendesk configuration.

21. Click **Finish**.

    ![A screen capture of the PingOne My Applications page with the SAML tab open. The introduction sentence is Applications you've added to your account are listed here. You can search by application name, description or entity ID. A bulleted list of 2 items follows, Active applications are enabled for single sign-on (SSO) and Details displays the application details. There is a search bar and button. The results show all the matching results for a ZenDesk search. The results are listed by icon, Application Name, Type, Status, Enabled toggle switch, Remove button, and the setup button, which is a black triangle turned to the right. At the bottom of the section, on the left side is the Add Application button, and on the right side is the Pause All SSO button.](_images/tbj1618606479711.jpg)

## Configure the PingOne IdP connection for Zendesk

1. Sign on to Zendesk as an administrator.

2. Click the **Products** icon.

3. Click **Admin Centre**.

   ![A screen capture of the Zendesk Administrator home page. The Get Started page view option is clicked. On the top right of the page is a search bar, a message icon, a bell icon, the products icon, and a user icon. The products icon is clicked and displays the menu options of Support, Guides, Gather, Chat, Talk, Explore, Sell, and Admin Centre. The Admin Centre option has a light blue background when the mouse hovers over it and is highlighted.](_images/llp1618607510292.jpg)

4. Click the **Security** icon.

   ![A screen capture of the Admin Centre page. On the left side is a navigation pane with the icons for menu options. The Security icon which is a shield with a checkmark in the center is clicked. The Security sub-menu options has Staff Members, End users, Single sign-on, which is clicked and highlighted, and Advanced. The Single sign-on section is displayed. There are SAML and JSON Web Token configuration options with Configure buttons for each option. The SAML Configure button is highlighted.](_images/lbi1619117272068.jpg)

5. Click **Single sign-on**.

6. In the **SSO Login URL** field, enter the URL Location for the **SingleSignOnService Location** from the PingOne SP metadata that you downloaded from the Zendesk configuration.

   For example:

   `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=idpid`

7. Open the signing certificate that you downloaded in the PingOne SP configuration and paste the thumbprint into the **Certificate fingerprint** section.

   ![A screen capture of the Certificate dialog with the Details tab open. In the Show list, \<All> is selected. The list is organized by Field and Value. The Thumbprint line entry is selected and has a light grey background. At the bottom of the dialog is the Edit Properties button, which is blurred, and the Copy to File…​ button. Below these buttons is the OK button, which is highlighted with a blue outline.](_images/ghp1619117383411.jpg)

8. Click **Enabled**.

   ![The SAML configuration page. The introduction sentence is SAML is an industry standard SSO framework typically used by large enterprises for communicating identities across the internet. There are fields for Enabled, which is a selected checkbox, SAML SSO URL, Certificate fingerprint\*, and the Remote logout URL.](_images/rvt1619117483271.jpg)

9. Click **Save**.

10. Enable external authentication for **Staff members** or **End users** as required.

    |   |                                                              |
    | - | ------------------------------------------------------------ |
    |   | The following example enables it for **Staff members** only. |

    * Click the **Security** icon.

    * Click **Staff members**.

    * Select the **External Authentication** check box.

    * Click **Single sign-on**. + Click **Save**.

    ![A screen capture of the Staff members configuration page. There are fields for External authentication, which is a check box that is selected, Google and Microsoft radio buttons, which aren't clicked, and a Single sign-on radio button which is clicked. At the bottom of the page is the Cancel and Save buttons.](_images/ekk1618608153644.jpg)

## Test the integration

### Choose from:

* For PingFederate IdP-Initiated SSO

  Go to the **Single Sign-On (SSO) URL** in the PingOne Application configuration to perform IdP initiated SSO.

  For example, `https://PingFederateHostname:PingFederatePort__/idp/startSSO.ping?PartnerSpId=Zendesk`.

  ![The PingOne Sign On page. There are fields for Username and Password fields. There is a Remember Me checkbox, which is cleared, the Sign On button, and the Forgot Password link.](_images/isa1618608306341.jpg)![A screen capture of the Zendesk agent dashboard page. The page displays the Open Tickets (current) and Ticket Statistics (this week). Open tickets (current) contains the number of open tickets for You and Groups. The Ticket Statistics (this week) contains the number of tickets categorized by Good, Bad, and Solved. Below this is the section, Tickets requiring your attention (1), with a What is this? Link, and a Play button to the right. A ticket list showing all ticket results with the fields of a check box, the ID, Subject, Requester, Requester updated, Group, and Assignee.](_images/fng1618609488659.jpg)

   

* For PingOne SP Initiated SSO

  1. Go to the URL for your Zendesk tenant. For example, `https://tenant.zendesk.com`.

     |   |                                                                       |
     | - | --------------------------------------------------------------------- |
     |   | Because SSO is only enabled for Staff, you should see a sign on form. |

  2. Click **I am an Agent** to initiate SSO.

     ![A screen capture of the Zendesk sign on page. There are fields for Email and Password, a Sign in button, an I am an Agent link, which is highlighted, the Forgot my password link, and the Privacy Policy link.](_images/jwx1618609178567.jpg)
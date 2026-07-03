---
title: Configuring SAML SSO with Workday and PingFederate
description: Enable Workday sign-on from a PingFederate URL (IdP-initiated sign-on) and direct Workday sign-on using PingFederate (SP-initiated sign-on), with single logout (SLO).
component: configuration_guides
page_id: configuration_guides:workday:config_saml_workday_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/workday/config_saml_workday_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-service-provider-sp-connection-for-workday: Create a PingFederate service provider (SP) connection for Workday
  add-the-pingfederate-idp-connection-to-workday: Add the PingFederate IdP Connection to Workday
  update-the-pingfederate-workday-idp-for-slo: Update the PingFederate Workday IdP for SLO
  test-the-pingfederate-idp-initiated-sso: Test the PingFederate IdP-initiated SSO
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Workday and PingFederate

Enable Workday sign-on from a PingFederate URL (IdP-initiated sign-on) and direct Workday sign-on using PingFederate (SP-initiated sign-on), with single logout (SLO).

## Before you begin

* Configure PingFederate to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* Populate Workday with at least one user to test access.

* You must have administrative access to PingFederate and Workday.

## Create a PingFederate service provider (SP) connection for Workday

1. Sign on to the PingFederate administrative console.

2. Create an SP connection for Workday in PingFederate.

3. Set **Partner's Entity ID** to `http://www.workday.com`.

4. Enable the **IdP-Initiated SSO** and **SP Initiated SSO** SAML profiles.

5. In **Assertion Creation → Authentication Source Mapping → Attribute Contract Fulfillment**, map **SAML\_SUBJECT**.

6. In **Protocol Settings → Assertion Consumer Service URL**:

   1. Set **Binding** to **POST**.

   2. In the **Endpoint URL** field, enter`https://your-environment.workday.com/your-tenant-name/login-saml.flex`

   3. In **Protocol Settings → Allowable SAML Bindings**, enable **POST**.

   4. In **Credentials → Digital Signature Settings**, select the **PingFederate Signing Certificate**.

7. Click **Save**.

8. Export the signing certificate.

9. Export the metadata file, open it in a text editor, and copy:

   * The entityID

   * The SSO Location entry `https://your value/idp/SSO.saml2`

   * The SLO Location entry `https://your value/idp/SLO.saml2`

## Add the PingFederate IdP Connection to Workday

1. Sign on to Workday as an administrator and click **Account Administration**.

   ![A screen capture of the Workday administrator home page/dashboard. The intro section sentence is Welcome, Ping and to the right has a gear icon. The page is split into two halves, the Inbox and Applications sections. The left or Inbox section contains a mail icon and the Inbox items. At the bottom center of this section is a Go to Inbox link. In the Applications or right section, is a puzzle icon. 7 icons and their corresponding application names are pictured. The Account Administration application of a person from the shoulders up with a gear icon is highlighted.](_images/aiq1618943478017.jpg)

2. Click **Edit Tenant Setup – Security**.

   ![A screen capture of the Account Administration application configuration with 3 separate sections of Audit, View, and Actions. Audit and View sections are sitting side-by-side, splitting the page in half, and the Actions section is below them filling the whole page. The Actions section has the options Edit Tenant Setup – Security, which is highlighted, Disable Workday Accounts, Enable/Disable Account Data Masking, and Create Workday Account for Supplier Contact.](_images/oit1618943538244.jpg)

3. In the **Single Sign On** section, click the **[icon: plus, set=fa]**icon under **Redirection URLs**.

4. Configure the redirection URLs:

   | Redirect Type                         | Single URL                                                                              |
   | ------------------------------------- | --------------------------------------------------------------------------------------- |
   | **Login Redirect URL**                | `https://your-environment.workday.com/your-tenant-name/login-saml2.flex`                |
   | **Logout Redirect URL**               | Single logout (SLO) location from previous procedure `https://your value/idp/SLO.saml2` |
   | **Mobile App Login Redirect URL**     | `https://your-environment.workday.com/your-tenant-name/login-saml2.flex`                |
   | **Mobile Browser Login Redirect URL** | `https://your-environment.workday.com/your-tenant-name/login-saml2.flex`                |
   | **Environment**                       | Select environment                                                                      |

5. In the **SAML Setup** section, select the **Enable SAML Authentication** check box.

   ![A screen capture of the SAML Setup section. The section contains two checkboxes: Enable SAML Authentication, which is selected and highlighted and a Enable Native Multi-Factor Authentication cleared checkbox.](_images/fkz1618943588290.jpg)

6. Click the **[icon: plus, set=fa]**icon.

   ![A screen capture of the SAML Identity Providers section. The row entry has a plus icon, which is highlighted, Identity Provider, Disabled, Identity Provider Name, Issuer, and x509 Certificate.](_images/cxz1618943826277.jpg)

7. Set the **Identity Provider Name** to PingFederate, and in the **Issuer** field, enter the entity ID value that you copied from PingFederate.

8. For SLO, in the **x509 certificate** section, click **Create x509 Public Key**.

   ![A screen capture of the expanded x509 Certificate field. In the menu list, the Create x509 Public Key option is highlighted.](_images/ztd1618944114635.jpg)

9. In the **Name** field, enter a name for your PingFederate signing certificate, such as `PingFederateCert`.

10. Open the PingFederate signing certificate in a text editor, copy the contents, and paste them into the **Certificate** field.

    ![A screen capture of the Create x509 Public Key configuration section. There are fields for Name, which is highlighted, Valid From, Valid To, and Certificate, which is highlighted.](_images/kis1618943870200.jpg)

11. Click **OK**.

12. Use the following configuration.

    | Enable IdP Initiated Logout                            | Selected                                                                                                   |
    | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
    | **Logout Response URL**                                | Enter the SLO location that you copied from PingFederate. For example, `https://your value/idp/SLO.saml2`. |
    | **Enable Workday Initiated Logout**                    | Selected                                                                                                   |
    | **Logout Request URL**                                 | Enter the SLO location that you copied from PingFederate. For example, `https://your value/idp/SLO.saml2.` |
    | **Service Provider ID**                                | Enter `http://www.workday.com`.                                                                            |
    | **SP Initiated**                                       | Selected                                                                                                   |
    | **Do Not Deflate SP-initiated Authentication Request** | Selected                                                                                                   |
    | **IdP SSO Service URL**                                | Enter the SLO location you copied from PingFederate. For example, `https://your-value/idp/SLO.saml2`.      |

13. Click **OK**.

14. For SLO, in the **x509 Private Key Pair** menu, select **Create x509 Private Key Pair**.

    ![A screen capture of the expanded \*x509 Private Key Pair field. The menu icon is highlighted. In the menu list, Create x509 Private Key is highlighted.](_images/fxl1618944205074.jpg)

15. In the **Name** field, enter a name for the key pair.

    ![A screen capture of the Create x509 Private Key configuration section. There are fields for Name which is highlighted, Description, and a Do Not Allow Regeneration checbox box.](_images/djo1618944290330.jpg)

16. Click **OK**.

17. Hover next to the key pair name and click the **…​** icon.

    ![A screen capture of the Create x509 Private Key configuration section. The x509 Private key pair name has the entry of workday with a menu icon. The menu icon is highlighted.](_images/qko1618944531583.jpg)

18. In **x509 Private Key Pair**, select **View Key Pair**.

    ![A screen capture of the expanded menu for the x509 Private key pair field. In the menu list, there are options for View Key Pair, which is highlighted, Edit Key Pair, and Regenerate Key Pair.](_images/wzw1618944587507.jpg)

19. Copy the contents of the public key and save them in a text editor.

    ![A screen capture of the Create x509 Private Key configuration section. There are fields for Description, Valid From, Valid To, and Public Key, which has the PingOne signing certificate details and is highlighted.](_images/hvi1618944628842.jpg)

20. Set the **Authentication Request Signature Method** to **SHA-256**.

    |   |                                                   |
    | - | ------------------------------------------------- |
    |   | Leave all the other values in this section blank. |

21. Click **Done**.

## Update the PingFederate Workday IdP for SLO

1. Sign on to the PingFederate administrative console.

2. Edit the SP connection for Workday and add the following extra SAML profiles:

   * **IDP-Initiated SLO**

   * **SP Initiated SLO**

3. In **Protocol Settings → SLO Service URL**:

   1. Set **Binding** to **POST**

   2. Set **Endpoint URL** to `https://your-environment.workday.com/your-tenant-name/logout-saml.htmld`.

   3. Set **Response URL** to `https://your-environment.workday.com/your-tenant-name/logout-saml.htmld`.

4. In **Credentials → Signature Verification Settings**, select the saved Workday public key.

## Test the PingFederate IdP-initiated SSO

1. Go to the PingFederate SSO Application Endpoint for the Workday SP connection.

2. Complete the PingFederate authentication.

   ![A screen capture of the Ping Identity Sign On page. The page has Username and Password fields, a Remember Me checkbox, a Sign On button, and the Forgot Password link.](../_images/hzi1618945469130.png)

   You are redirected to your Workday domain.

   ![A screen capture of the Workday administrator home page/dashboard. The intro section sentence is Welcome, Ping and to the right has a gear icon. The page is split into two halves, the Inbox and Applications sections. The left or Inbox section contains a mail icon and the Inbox items. At the bottom center of this section is a Go to Inbox link. In the Applications or right section, is a puzzle icon and a list of all Applications by their name and a icon.](_images/sop1618946033177.jpg)

3. Click **Sign Out**.

   ![A screen capture of the expanded cloud icon or the administrator account profile menu. The Ping View Profile menu is highlighted. The Sign Out button, which is the last of the menu options, is highlighted.](_images/lbp1618945789055.jpg)

## Test the PingFederate SP-initiated SSO integration

1. Go to your Workday URL.

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   After successful authentication, you are redirected back to Workday.

   ![A screen capture of the Workday administrator home page/dashboard. The intro section sentence is Welcome, Ping and to the right has a gear icon. The page is split into two halves, the Inbox and Applications sections. The left or Inbox section contains a mail icon and the Inbox items. At the bottom center of this section is a Go to Inbox link. In the Applications or right section, is a puzzle icon and a list of all Applications by their name and a icon.](_images/sop1618946033177.jpg)

3. Click **Sign Out**.

   ![A screen capture of the expanded cloud icons or the administrator account profile menu. The Ping View Profile at the top of the menu is highlighted. The Sign Out button, which is the last of the menu options, is highlighted.](_images/lbp1618945789055.jpg)

   You are signed out.

---

---
title: Configuring SAML SSO with Workday and PingOne for Enterprise
description: Enable Workday sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct WorkDay sign-on using PingOne for Enterprise (SP-initiated sign-on), with single logout (SLO).
component: configuration_guides
page_id: configuration_guides:workday:config_saml_workday_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/workday/config_saml_workday_p1.html
revdate: May 20, 2024
section_ids:
  before-you-begin: Before you begin
  setup-the-workday-application-in-pingone-for-enterprise: Setup the Workday application in PingOne for Enterprise
  add-the-pingone-for-enterprise-identity-provider-idp-connection-to-workday: Add the PingOne for Enterprise identity provider (IdP) connection to Workday
  complete-the-workday-slo-setup-in-pingone: Complete the Workday SLO setup in PingOne
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-initiated SSO integration
  test-the-pingone-for-enterprise-sp-initiated-sso-integration: Test the PingOne for Enterprise SP-initiated SSO integration
---

# Configuring SAML SSO with Workday and PingOne for Enterprise

Enable Workday sign-on from the PingOne for Enterprise console (IdP-initiated sign-on) and direct WorkDay sign-on using PingOne for Enterprise (SP-initiated sign-on), with single logout (SLO).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Populate Workday with at least one user to test access.

* You must have administrative access to PingOne for Enterprise and Workday.

## Setup the Workday application in PingOne for Enterprise

1. Sign on to PingOne for Enterprise and go to **Applications → Application Catalog**.

2. In the **Application Catalog**, search for `Workday`.

   ![A screen capture of the Application Catalog search section. There is a search bar and button with Workday entered. The Application search results are showing the results for Workday. The results are listed by the application icon, Application Name, Type, and the setup icon, which is a black triangle turned to the right.](_images/giy1618959860496.jpg)

3. Expand the Workday entry and click **Setup**.

4. Copy the **Issuer** and **IdP ID** values.

5. Download the signing certificate.

   ![A screen capture of the 1. SSO Instructions section. zthere are fields for Signing Certificate with a Download link, Saas ID, IdP ID, Initiate Single Sign-On (SSO) URL, and Issuer.](_images/wkf1618959918759.jpg)

6. Click **Continue to Next Step**.

7. Enter the following values.

   | Field                               | Entry                                                                     |
   | ----------------------------------- | ------------------------------------------------------------------------- |
   | **ACS URL**                         | `https://your-environment.workday.com/your-tenant-name/login-saml.flex`   |
   | **Entity ID**                       | `http://www.workday.com`                                                  |
   | **Target Resource**                 | `https://your-tenant-name/fx/home.flex`                                   |
   | **Single Logout Endpoint**          | `https://your-environment.workday.com/your-tenant-name/logout-saml.htmld` |
   | **Single Logout Response Endpoint** | `https://your-environment.workday.com/your-tenant-name/logout-saml.htmld` |

8. Click **Continue to Next Step**.

9. Map the **SAML\_SUBJECT** attribute.

   ![A screen capture of the 3. Attribute Mapping section. The sentence introduction is Map your identity bridge to the attributes required by the application. The mapping attribute fields are Application Attribute, Description, and Identity Bridge Attribute or Literal Value. The fields have default entries for Application Attribute and Description. The Identity Bridge Attribute or Literal Value field requires an entry from the user and has a As Literal checkbox, which is cleared.](_images/okg1618959965705.jpg)

10. Click **Continue to Next Step** twice.

11. Click **Add** for each user group that should have access to Workday.

    ![A screen capture of the 5. Group Access section. The sentence introduction is Select all user groups that should have access to this application. Users that are members of the added groups will be able to SSO to this application and will see this application on their personal dock. There is a search bar with a Search button. The search results are listed by Group Name. One entry has a Add button and the other entry has a Remove button.](_images/tnp1618960026988.jpg)

12. Click **Continue to Next Step**.

13. Click **Finish**.

## Add the PingOne for Enterprise identity provider (IdP) connection to Workday

1. Sign on to Workday as an administrator and click **Account Administration**.

   ![A screen capture of the Workday administrator home page/dashboard. The intro section sentence is Welcome, Ping and to the right has a gear icon. The page is split into two halves, the Inbox and Applications sections. The left or Inbox section contains a mail icon and the Inbox items. At the bottom center of this section is a Go to Inbox link. In the Applications or right section, is a puzzle icon. 7 icons and their corresponding application names are pictured. The Account Administration application of a person from the shoulders up with a gear icon is highlighted.](_images/aiq1618943478017.jpg)

2. Click **Edit Tenant Setup – Security**.

   ![A screen capture of the Account Administration application configuration with 3 separate sections of Audit, View, and Actions. Audit and View sections are sitting side-by-side, splitting the page in half, and the Actions section is below them filling the whole page. The Actions section has the options Edit Tenant Setup – Security, which is highlighted, Disable Workday Accounts, Enable/Disable Account Data Masking, and Create Workday Account for Supplier Contact.](_images/oit1618943538244.jpg)

3. In the **Single Sign On** section, click the **[icon: plus, set=fa]**icon under **Redirection URLs**.

4. Set the following properties:

   | Field                                 | Entry                                                                                              |
   | ------------------------------------- | -------------------------------------------------------------------------------------------------- |
   | **\*Redirect Type**                   | **Single URL**                                                                                     |
   | **Login Redirect URL**                | `https://your-environment.workday.com/your-tenant-name/login-saml2.flex`                           |
   | **Logout Redirect URL**               | `https://sso.connect.pingidentity.com/sso/SLO.saml2.workday.com/your-tenant-name/login-saml2.flex` |
   | **Mobile App Login Redirect URL**     | `https://your-environment.workday.com/your-tenant-name/logout-saml.htmld`                          |
   | **Mobile Browser Login Redirect URL** | `https://your-environment.workday.com/your-tenant-name/logout-saml.htmld`                          |
   | **Environment**                       | Select your environment.                                                                           |

5. In the **SAML Setup** section, select the **Enable SAML Authentication** check box.

   ![A screen capture of the SAML Setup section. The section contains two checkboxes: Enable SAML Authentication, which is selected and highlighted and a Enable Native Multi-Factor Authentication cleared checkbox.](_images/fkz1618943588290.jpg)

6. Click the **[icon: plus, set=fa]**icon.

   ![A screen capture of the SAML Identity Providers section. The row entry has a plus icon, which is highlighted, Identity Provider, Disabled, Identity Provider Name, Issuer, and x509 Certificate.](_images/cxz1618943826277.jpg)

7. Set the **Identity Provider Name** to **PingOne** and enter the **Issuer** value you copied previously.

8. In the **x509 Certificate** section, click **Create x509 Public Key**.

   ![A screen capture of the expanded \*x509 Certificate field. In the menu list, the Create x509 Public Key option is highlighted.](_images/ztd1618944114635.jpg)

9. Enter a name for your PingOne for Enterprise signing certificate, such as `PingOneCert`.

10. Open the PingOne for Enterprise signing certificate in a text editor and paste the contents of the certificate into the **Certificate** field.

    ![A screen capture of the Create x509 Public Key configuration section. There are fields for Name, which is highlighted, Valid From, Valid To, and Certificate, which is highlighted.](_images/kis1618943870200.jpg)

11. Click **OK**.

12. Set the following properties.

    | Property                                               | Value                                                                                    |
    | ------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
    | **Enable IdP Initiated Logout**                        | Selected                                                                                 |
    | **Logout Response URL**                                | `https://sso.connect.pingidentity.com/sso/SLO.saml2`                                     |
    | **Enable Workday Initiated Logout**                    | Selected                                                                                 |
    | **Logout Request URL**                                 | `https://sso.connect.pingidentity.com/sso/SLO.saml2`                                     |
    | **Service Provider ID**                                | `http://www.workday.com`                                                                 |
    | **SP Initiated**                                       | Selected                                                                                 |
    | **Do Not Deflate SP-initiated Authentication Request** | Selected                                                                                 |
    | **IdP SSO Service URL**                                | `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=IdP-ID-value-from-PingOne` |

13. Click **OK**.

14. For SLO, in the **x509 Private Key Pair** menu, select **Create x509 Private Key Pair**.

    ![A screen capture of the expanded \*x509 Private Key Pair field. The menu icon is highlighted. In the menu list, Create x509 Private Key is highlighted.](_images/fxl1618944205074.jpg)

15. Enter a name for the key pair.

    ![A screen capture of the Create x509 Private Key configuration section. There are fields for Name which is highlighted, Description, and a Do Not Allow Regeneration checbox box.](_images/djo1618944290330.jpg)

16. Click **OK**.

17. Hover next to the key pair name and click the **Menu** icon.

    ![A screen capture of the Create x509 Private Key configuration section. The x509 Private key pair name has the entry of workday with a menu icon. The menu icon is highlighted.](_images/qko1618944531583.jpg)

18. Click **View Key Pair**.

    ![A screen capture of the expanded menu for the x509 Private key pair field. In the menu list, there are options for View Key Pair, which is highlighted, Edit Key Pair, and Regenerate Key Pair.](_images/wzw1618944587507.jpg)

19. Copy the contents of the public key and save them in a text editor.

    ![A screen capture of the Create x509 Private Key configuration section. There are fields for Description, Valid From, Valid To, and Public Key, which has the PingOne signing certificate details and is highlighted.](_images/hvi1618944628842.jpg)

20. Set **Authentication Request Signature Method** to **SHA-256**.

    |   |                                               |
    | - | --------------------------------------------- |
    |   | Leave all other values in this section blank. |

21. Click **Done**.

## Complete the Workday SLO setup in PingOne

1. Go to PingOne for Enterprise and continue editing the Workday entry.

   |   |                                                                                              |
   | - | -------------------------------------------------------------------------------------------- |
   |   | If the session has timed out, complete the initial steps to the point of clicking **Setup**. |

2. Click **Continue to Next Step**.

3. Click **Choose File**, and select the saved Workday public key file.

   ![A screen capture of the Workday SLO setup, in the Certificate Verification upload section. Ther are fields for Primary Verification Certificate with a Choose File button that is highlighted, and Secondary Verification Certificate. Both fields have a Choose File button.](_images/wxu1618960489589.jpg)

4. Click **Continue to Next Step** until the final screen. Click **Finish**.

## Test the PingOne for Enterprise IdP-initiated SSO integration

1. Go to your Ping desktop as a user with Workday access.

   |   |                                                                                               |
   | - | --------------------------------------------------------------------------------------------- |
   |   | To find the Ping desktop URL in the admin console, go to **Setup → Dock → PingOne Dock URL**. |

2. Complete the PingOne authentication.

   ![A screen capture of the PingIdentity Sign On page. The page has Username and Password fields, a Remember Me checkbox, a Sign On button, and the Forgot Password link.](../_images/hzi1618945469130.png)

   You are redirected to your Workday environment.

   ![A screen capture of the Workday administrator home page/dashboard. The intro section sentence is Welcome, Ping and to the right has a gear icon. The page is split into two halves, the Inbox and Applications sections. The left or Inbox section contains a mail icon and the Inbox items. At the bottom center of this section is a Go to Inbox link. In the Applications or right section, is a puzzle icon and a list of all Applications by their name and a icon.](_images/sop1618946033177.jpg)

3. Click **Sign Out**.

   You are signed out.

   ![A screen capture of the expanded cloud icons or the administrator account profile menu. The Ping View Profile at the top of the menu is highlighted. The Sign Out button,which is the last of the menu options, is highlighted.](_images/lbp1618945789055.jpg)

## Test the PingOne for Enterprise SP-initiated SSO integration

1. Go to your Workday URL.

   For example:

   `https://your-environment.workday.com/Your tenant/login-saml2.flex`

2. After you're redirected to PingOne for Enterprise, enter your PingOne for Enterprise username and password.

   ![A screen capture of the Ping Identity Sign On page. The page has Username and Password fields, a Remember Me checkbox, a Sign On button, and the Forgot Password link.](../_images/hzi1618945469130.png)

   After successful authentication, you are redirected back to Workday.

   ![A screen capture of the Workday administrator home page/dashboard. The intro section sentence is Welcome, Ping and to the right has a gear icon. The page is split into two halves, the Inbox and Applications sections. The left or Inbox section contains a mail icon and the Inbox items. At the bottom center of this section is a Go to Inbox link. In the Applications or right section, is a puzzle icon and a list of all Applications by their name and a icon.](_images/sop1618946033177.jpg)

3. Click **Sign Out**.

   ![A screen capture of the expanded cloud icon or the administrator account profile menu. The Ping View Profile menu is highlighted. The Sign Out button, which is the last of the menu options, is highlighted.](_images/lbp1618945789055.jpg)

   You are signed out.

   ![A screen capture of the Sign Off Complete page. The page has the text, "Single sign-off is complete."](_images/ijw1619127119215.jpg)
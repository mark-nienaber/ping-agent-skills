---
title: Configuring SAML SSO with Namely and PingFederate
description: Learn how to enable Namely sign-on from the PingFederate console (IdP-initiated sign-on) and direct Namely sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:namely:config_saml_namely_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/namely/config_saml_namely_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-the-namely-metadata: Create the Namely metadata
  add-the-pingfederate-connection-to-namely: Add the PingFederate connection to Namely
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Namely and PingFederate

Learn how to enable Namely sign-on from the PingFederate console (IdP-initiated sign-on) and direct Namely sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* PingFederate should be configured to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* Populate Namely with at least one user to test access.

* You must have administrative access to PingFederate.

## Create the Namely metadata

1. In PingFederate, create a service provider (SP) connection for Namely:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set **Partner's Entity ID** to `https://your-subdomain.namely.com/saml/metadata`.

   3. Enable the following SAML profiles:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfilment,** map the **SAML\_SUBJECT** to your email attribute.

   5. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://your-subdomain.namely.com/saml/consume`.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials: Digital Signature Settings**, select the **PingFederate Signing Certificate**.

   8. Note the metadata URL for the newly-created Namely SP connection.

## Add the PingFederate connection to Namely

1. Sign on to the Namely console as an administrator.

2. Select **Company** on the top navigation bar.

3. Click the **Settings** tab.

4. In the left navigation pane, click **Login Page**.

5. In the **Login Methods** section, click **SAML**.

6. Enter the **Identity Provider SSO URL** from PingFederate.

7. Copy and paste the IdP Provider Certificate value into the **Identity provider certificate**.

8. Enter the **SAML Metadata URL** from PingFederate.

   ![Screen capture of Namely Company page with Settings, Login Page, SAMML, SAML Settings ceritficate, and SAML Metadata highlighted.](_images/kky1640218027409.png)

9. Click **Save**.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO Application Endpoint for the Namely SP connection.

2. Authenticate with PingFederate.

   You're redirected to your Namely domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to `https://your-subdomain.namely.com/users/login`.

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to Namely.

---

---
title: Configuring SAML SSO with Namely and PingOne
description: Learn how to enable Namely sign-on from the PingOne console (IdP-initiated sign-on) and direct Namely sign-on using PingOne (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:namely:config_saml_namely_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/namely/config_saml_namely_p1.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  add-the-namely-application-to-pingone: Add the Namely application to PingOne
  enable-saml-sso-in-namely: Enable SAML SSO in Namely
  test-the-pingone-idp-integration: Test the PingOne IdP integration
  test-the-pingone-sp-integration: Test the PingOne SP integration
---

# Configuring SAML SSO with Namely and PingOne

Learn how to enable Namely sign-on from the PingOne console (IdP-initiated sign-on) and direct Namely sign-on using PingOne (SP-initiated sign-on).

## Before you begin

* Link PingOne to an identity repository containing the users requiring application access.

* Populate Namely with at least one user to test access.

* You must have administrative access to PingOne and an Admin account on Namely.

## Add the Namely application to PingOne

1. In PingOne, go to **Connections → Applications** and click the + icon.

   ![Screen capture of PingOne Applications page.](../_images/vxx1638477533848.png)

2. When you're prompted to select an application type, select **WEB APP** and then click **Configure** next to **SAML** for the chosen connection type.

3. Enter `Namely` as the application name.

4. Enter a suitable description.

5. **Optional:** Upload an icon.

6. Click **Next**.

7. For **Provide App Metadata**, select **Enter Manually**.

8. In the **ACS URLS** field, enter `https://your-subdomain.namely.com/saml/consume`.

9. In the **Entity ID** field, enter `https://your-subdomain.namely.com/saml/consume`.

10. Select the **Signing Key** to use and then click **Download Signing Certificate** to download as X509 PEM (.crt).

11. Leave **SLO Endpoint** and **SLO Response Endpoint** blank.

12. In the **Subject NameID Format** list, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

13. Enter a suitable value for **Assertion Validity Duration (in seconds)**. A value of 300 seconds is typical.

14. Click **Save and Continue**.

15. Namely expects an email address to identify a user in the SSO security assertion:

    * If you use an email address to sign on through PingOne, click **Save and Close**.

    * If you sign on with a username, in the **PingOne User Attribute** list, select **Email Address** to map that to the **SAML\_SUBJECT**, then click **Save and Close**.

16. Click the toggle to enable the application.

17. On the **Configuration** tab of the newly-created Namely application, copy and save the **IDP Metadata URL** value.

    You'll need this when configuring SAML on Namely.

    ![Screen capture of PingOne Connection Details section.](../_images/cid1640211566357.png)

## Enable SAML SSO in Namely

1. Sign on to the Namely console as an administrator.

2. Select **Company** on the top navigation bar.

3. Click the **Settings** tab.

4. In the left navigation pane, click **Login Page**.

5. In the **Login Methods** section, click **SAML**.

6. In the **Identity Provider SSO URL** field, enter the **Initiate Single Sign-On URL** value from PingOne.

7. Copy and paste the **IdP Provider Certificate** value into the **Identity provider certificate** field.

8. In the **SAML Metadata** field, enter the **IdP Metadata URL** value from PingOne.

   ![Screen capture of Namely Company page detailing SAML settings.](_images/kky1640218027409.png)

9. Click **Save**.

## Test the PingOne IdP integration

1. Go to the PingOne Application Portal and sign on with a user account.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | In the Admin console, go to **Dashboard → Environment Properties** to find the **PingOne Application Portal URL**. |

2. Click the Namely icon.

   You're redirected to the Namely website and logged in with SSO.

## Test the PingOne SP integration

1. Go to `https://your-subdomain.namely.com/users/login` and enter your email address only.

2. In the PingOne sign-on prompt, enter your PingOne username and password.

   ![Screen capture of PingOne sign-on page.](../_images/yrq1620763776078.png)

   You're redirected back to Namely and signed on.
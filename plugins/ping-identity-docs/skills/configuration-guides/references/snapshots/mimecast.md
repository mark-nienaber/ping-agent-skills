---
title: Configuring SAML SSO with Mimecast and PingFederate
description: Learn how to enable Mimecast sign-on from PingFederate (IdP-initiated sign-on) and direct Mimecast sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:mimecast:config_saml_mimecast_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/mimecast/config_saml_mimecast_pf.html
revdate: May 20, 2024
section_ids:
  before-you-begin: Before you begin
  create-the-mimecast-metadata: Create the Mimecast metadata
  add-the-pingfederate-connection-to-mimecast: Add the PingFederate connection to Mimecast
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Mimecast and PingFederate

Learn how to enable Mimecast sign-on from PingFederate (IdP-initiated sign-on) and direct Mimecast sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* Populate Mimecast with at least one user to test access.

* You must have administrative access to PingFederate.

## Create the Mimecast metadata

1. In PingFederate, create a service provider (SP) connection for Mimecast:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set Partner's Entity ID to `your-Mimecast-account-hosting-location-api.mimecast.com.accountcode`.

   3. Enable the following SAML profiles:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfilment**, map the **SAML\_SUBJECT** to your email attribute.

   5. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://your-Mimecast-account-hosting-location-api.mimecast.com/sign on/saml`.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials: Digital Signature Settings**, select the **PingFederate Signing Certificate**.

      |   |                                                                     |
      | - | ------------------------------------------------------------------- |
      |   | Note the metadata URL for the newly-created Mimecast SP connection. |

## Add the PingFederate connection to Mimecast

1. Sign on to the Mimecast console as an administrator.

2. Select **Administration** on the lefthand pane.

3. Click the **Services** tab.

4. Select **Application Settings**.

5. Select **Authentication Profiles**.

   ![Screen capture of Mimecast administration console with Authentication Profiles highlighted.](_images/hwo1640212753197.png)

6. Click **New Authentication Profile**.

7. Select the **Enforce SAML Authentication for Administration Console** option.

   The page expands to reveal the **SAML Settings**.

8. Under **Provider**, select **Other**.

9. Enter the **Metadata URL** for the Mimecast SP Connector in PingFederate.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO Application Endpoint for the Mimecast SP connection.

2. Authenticate with PingFederate.

   You're redirected to your Mimecast domain.

## Test the PingFederate SP-initiated SSO integration

1. Sign on to [Mimecast](https://login.mimecast.com/u/login/?gta=apps&_ga=2.197221231.1597895005.1652085427-1344334576.1645445521#/login).

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   After successful authentication, you're redirected back to Mimecast.

---

---
title: Configuring SAML SSO with Mimecast and PingOne
description: Learn how to enable Mimecast sign-on from the PingOne console (IdP-initiated sign-on) and direct Mimecast sign-on using PingOne (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:mimecast:config_saml_mimecast_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/mimecast/config_saml_mimecast_p1.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  add-the-mimecast-application-to-pingone: Add the Mimecast application to PingOne
  add-pingone-as-identity-provider-idp-in-mimecast: Add PingOne as identity provider (IdP) in Mimecast
  test-the-pingone-idp-integration: Test the PingOne IdP integration
  test-the-pingone-sp-integration: Test the PingOne SP integration
---

# Configuring SAML SSO with Mimecast and PingOne

Learn how to enable Mimecast sign-on from the PingOne console (IdP-initiated sign-on) and direct Mimecast sign-on using PingOne (SP-initiated sign-on).

## Before you begin

* Link PingOne to an identity repository containing the users requiring application access.

* Populate Mimecast with at least one user to test access.

* You must have administrative access to PingOne and a Super Admin account for an Enterprise Organization on Mimecast.

## Add the Mimecast application to PingOne

1. In PingOne, go to **Connections → Applications** and click the + icon.

   ![Screen capture of PingOne Applications page.](../_images/vxx1638477533848.png)

2. When you're prompted to select an application type, select **WEB APP** and then click **Configure** next to **SAML** for the chosen connection type.

3. Enter `Mimecast` as the application name.

4. Enter a suitable description.

5. **Optional:** Upload an icon.

6. Click **Next**.

7. For **Provide App Metadata**, select **Enter Manually**.

8. In the **ACS URL** field, enter `https://account-hosting-location-api.mimecast.com/login/saml`.

9. Select the **Signing Key** to use and then click **Download Signing Certificate** to download as X509 PEM (.crt).

10. For **Entity ID**, enter `https://account-hosting-location-api.mimecast.com.accountcode`.

11. Leave **SLO Endpoint** and **SLO Response Endpoint** blank.

12. In the **Subject NameID Format** list, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

13. Enter a suitable value for **Assertion Validity Duration (in seconds)**. A value of 300 seconds is typical.

14. Click **Save and Continue**.

15. Mimecast expects an email address to identify a user in the SSO security assertion:

    * If you use an email address to sign on through PingOne, click **Save and Close**.

    * If you sign on with a username, in the **PingOne User Attribute** list, select **Email Address** to map that to the **SAML\_SUBJECT**, then click **Save and Close**.

16. Click the toggle to enable the application.

17. On the **Configuration** tab of the newly-created Mimecast application, copy and save the **IDP Metadata URL** value.

    You'll need this metadata when configuring SAML on Mimecast.

    ![Screen capture of PingOne Connection Details section.](../_images/cid1640211566357.png)

## Add PingOne as identity provider (IdP) in Mimecast

1. Sign on to Mimecast with an Admin account for your Enterprise Organization.

2. Go to **Administration → Services → Applications**.

3. Select **Authentication Profiles**.

4. Select **New Authentication Profile**.

5. Enter a **Description** for the new profiled.

6. Select **Enforce SAML Authentication for Administration Console**.

7. For **Provider**, select **Other**.

8. In the **Metadata URL** field, enter the URL value that you copied previously.

9. Go to **Administration → Services → Applications**.

10. Click **Lookup** to find the authentication profile that you created.

11. Click **Save and Exit**.

## Test the PingOne IdP integration

1. Go to the PingOne Application Portal and sign on with a user account.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | In the Admin console, go to **Dashboard → Environment Properties** to find the **PingOne Application Portal URL**. |

2. Click the Mimecast icon.

   You're redirected to the Mimecast website and logged in with SSO.

## Test the PingOne SP integration

1. Go to [login.mimecast.com](https://login.mimecast.com/u/login/?gta=apps&_ga=2.197221231.1597895005.1652085427-1344334576.1645445521#/login), and choose the option to sign on with SSO. Enter your email address only.

2. In the PingOne sign-on prompt, enter your PingOne username and password.

   ![Screen capture of PingOne sign-on page.](../_images/yrq1620763776078.png)

   You're redirected back to Mimecast and signed on.
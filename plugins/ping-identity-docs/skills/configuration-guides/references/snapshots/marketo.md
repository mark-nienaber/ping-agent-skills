---
title: Configuring SAML SSO with Marketo and PingFederate
description: Learn how to enable Marketo sign-on from PingFederate (IdP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:marketo:config_saml_marketo_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/marketo/config_saml_marketo_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  obtain-your-munchkin-account-id: Obtain your Munchkin Account ID
  create-an-sp-connection-for-marketo-in-pingfederate: Create an SP connection for Marketo in PingFederate
  enable-saml-sso-in-marketo: Enable SAML SSO in Marketo
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO Integration
---

# Configuring SAML SSO with Marketo and PingFederate

Learn how to enable Marketo sign-on from PingFederate (IdP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* Populate Marketo with at least one user to test access.

* You must have administrative access to PingFederate.

## Obtain your Munchkin Account ID

1. Sign on to the Marketo console as an administrator.

2. Select **Admin** in the toolbar.

3. Select **Intergration** in the left-hand pane.

4. **Copy** and **Save** your Munchkin Account ID.

## Create an SP connection for Marketo in PingFederate

1. Sign on to PingFederate.

2. Configure using **Browser SSO** profile **SAML 2.0**.

3. Set **Partner's Entity ID** to `https://www.marketo.com/SAML/your-Munchkin-account-ID`.

4. Enable the **IDP-initiated SSO** **SAML Profile**.

   |   |                                                      |
   | - | ---------------------------------------------------- |
   |   | Marketo does not currently support SP-initiated SSO. |

5. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment**, map the **SAML\_SUBJECT** to your email attribute.

6. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://login.marketo.com/saml/assertion/your-Munchkin-account-ID`.

7. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

8. In **Credentials: Digital Signature Settings**, select the PingFederate Signing Certificate and download it.

## Enable SAML SSO in Marketo

1. Sign on to the Marketo console as an administrator.

2. Select **Admin** in the toolbar.

3. Select **Other Stuff** in the left navigation pane.

4. Select **Single Sign-On**.

   |   |                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------- |
   |   | If you don't see **Single Sign-On**, contact <support@marketo.com> to enable SAML for your account. |

5. Next to **SAML Settings**, select **Edit**.

6. For the **Issuer ID**, enter the value you entered for the **IdP Entity ID** in PingFederate.

7. For the **Entity ID**, enter the value you entered for the **IdP Entity ID** in PingFederate.

8. For the **User ID** Location, click the **In Name identifier** element of **Subject**.

9. Click **Browse** next to **Identity Provider Certificate** and upload your public certificate.

10. Click **Save**.

## Test the PingFederate IdP-initiated SSO Integration

1. Go to the PingFederate SSO Application Endpoint for the Marketo SP connection.

2. Authenticate with PingFederate.

   You're redirected to your Marketo domain.

---

---
title: Configuring SAML SSO with Marketo and PingOne
description: Learn how to enable Marketo sign-on from PingOne (IdP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:marketo:config_saml_marketo_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/marketo/config_saml_marketo_p1.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  add-the-marketo-application-to-pingone: Add the Marketo Application to PingOne
  enable-saml-sso-with-marketo: Enable SAML SSO with Marketo
  test-the-pingone-idp-integration: Test the PingOne IdP integration
---

# Configuring SAML SSO with Marketo and PingOne

Learn how to enable Marketo sign-on from PingOne (IdP-initiated sign-on).

## Before you begin

* Link PingOne to an identity repository containing the users requiring application access.

* Populate Marketo with at least one user to test access.

* Gather your Munchkin Account ID.

* You must have administrative access to PingOne and an admin account on Marketo.

## Add the Marketo Application to PingOne

1. In PingOne, go to **Connections → Applications** and click the + icon.

   ![Screen capture of PingOne Applications page.](_images/fue1640201291588.png)

2. When you're prompted to select an application type, select **WEB APP** and then click **Configure** next to **SAML** for the chosen connection type.

3. Enter `Marketo` as the application name.

4. Enter a suitable description.

5. **Optional:** Upload an icon.

6. Click **Next**.

7. For **Provide App Metadata**, select **Enter Manually**.

8. For **ACS URLS**, enter `https://login.marketo.com/saml/assertion/your-Munchkin-account-ID`.

9. For **EntityID** enter `https://login.marketo.com/saml/your-Munchkin-account-ID`.

10. Choose the **Signing Key** to use and then click **Download Signing Certificate** to download as X509 PEM (.crt).

11. Leave **SLO Endpoint** and **SLO Response Endpoint** blank.

12. In the **Subject NameID Format** list, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

13. Enter a suitable value for **Assertion Validity Duration (in seconds)**. A value of 300 seconds is typical.

14. Click **Save and Continue**.

15. Marketo expects an email address to identify a user in the SSO security assertion:

    * If you use an email address to sign on through PingOne, click **Save and Close**.

    * If you sign on with a username, in the **PingOne User Attribute** list, select **Email Address** to map that to the **SAML\_SUBJECT**, then click **Save and Close**.

16. Click the toggle to enable the application.

17. On the Configuration tab of the newly-created Marketo application, copy and save the **IDP Metadata URL** value.

    You'll need this when configuring SAML on Marketo.

    ![Screen capture of PingOne Connection Details section.](_images/wfq1640202167911.png)

## Enable SAML SSO with Marketo

1. Sign on to the Marketo console as an administrator.

2. Select **Admin** in the toolbar.

3. Select **Other Stuff** in the left navigation pane.

4. Select **Single Sign-On**.

   |   |                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------- |
   |   | If you don't see **Single Sign-On**, contact <support@marketo.com> to enable SAML for your account. |

5. Select **Edit** next to **SAML Settings**.

6. For the **Issuer ID**, enter the value you entered for the **IdP Entity ID** in PingOne.

7. For the **Entity ID**, enter the value you entered for the **IdP Entity ID** in PingOne.

8. For the **User ID** Location, click the **In Name identifier** element of **Subject**.

9. Click **Browse** next to **Identity Provider Certificate** and upload your public certificate.

10. Click **Save**.

## Test the PingOne IdP integration

1. Go to the PingOne Application Portal and sign on with a user account.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | In the Admin console, go to **Dashboard → Environment Properties** to find the **PingOne Application Portal URL**. |

2. Click the Marketo icon.

   You're redirected to the Marketo website and signed on with SSO.
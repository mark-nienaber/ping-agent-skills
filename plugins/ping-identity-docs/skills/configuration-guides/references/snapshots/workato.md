---
title: Configuring SAML SSO with Workato and PingFederate
description: Learn how to enable Workato sign-on from the PingFederate console (IdP-initiated sign-on) and direct Workato sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:workato:config_saml_workato_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/workato/config_saml_workato_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-the-workato-metadata: Create the Workato metadata
  add-the-pingfederate-connection-to-workato: Add the PingFederate connection to Workato
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Workato and PingFederate

Learn how to enable Workato sign-on from the PingFederate console (IdP-initiated sign-on) and direct Workato sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an identity provider (IdP) or datastore containing the users requiring application access.

* Populate Workato with at least one user to test access.

* You must have administrative access to PingFederate.

## Create the Workato metadata

1. In PingFederate, create a service provider (SP) connection for Workato:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Set Partner's Entity ID to `https://www.workato.com/saml/metadata?id=Workato ID`.

      |   |                                                                           |
      | - | ------------------------------------------------------------------------- |
      |   | This value is provided by Workato on the **Tools → Team → Settings** tab. |

   3. Enable the following SAML profiles.

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   4. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfilment,** map the **SAML\_SUBJECT** to your email attribute.

   5. In **Protocol Settings: Assertion Consumer Service URL**, set **Binding** to **POST** and set **Endpoint URL** to `https://www.workato.com/saml/consume/`.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**.

   7. In **Credentials: Digital Signature Settings**, select the **PingFederate Signing Certificate**.

      |   |                                                                    |
      | - | ------------------------------------------------------------------ |
      |   | Note the metadata URL for the newly-created Workato SP connection. |

## Add the PingFederate connection to Workato

1. Sign on to the Workato console as an administrator.

2. Select **Tools** in the left navigation pane.

3. Click the **Members** tab.

4. Select **Team**.

5. Select the **Settings** tab.

   ![Screen capture of the Workato Team page on the Settings tab.](_images/hol1640210179539.png)

6. Enter a **Team name** for the team or company.

7. In the **Authentication method** list, select **SAML based SSO**.

8. In the **SAML\_provider** list, select **Other**.

9. Enter the **Metadata URL** value for the Workato SP connector in PingFederate.

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO Application Endpoint for the Workato SP connection.

2. Authenticate with PingFederate.

   You're redirected to your Workato domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to <https://app.workato.com/users/sign_in>.

2. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to Workato.

---

---
title: Configuring SAML SSO with Workato and PingOne
description: Learn how to enable Workato sign-on from the PingOne console (IdP-initiated sign-on) and direct Workato sign-on using PingOne (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:workato:config_saml_workato_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/workato/config_saml_workato_p1.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  add-the-workato-application-to-pingone: Add the Workato application to PingOne
  add-pingone-as-an-identity-provider-idp-to-workato: Add PingOne as an identity provider (IdP) to Workato
  test-the-pingone-idp-integration: Test the PingOne IdP integration
  test-the-pingone-sp-integration: Test the PingOne SP integration
---

# Configuring SAML SSO with Workato and PingOne

Learn how to enable Workato sign-on from the PingOne console (IdP-initiated sign-on) and direct Workato sign-on using PingOne (SP-initiated sign-on).

## Before you begin

* Link PingOne to an identity repository containing the users requiring application access.

* Populate Workato with at least one user to test access.

* You must have administrative access to PingOne and an Admin account on Workato.

## Add the Workato application to PingOne

1. In PingOne, go to **Connections → Applications** and click the + icon.

   ![Screen capture of PingOne Applications page.](../_images/vxx1638477533848.png)

2. When you're prompted to select an application type, select **WEB APP** and then click **Configure** next to **SAML** for the chosen connection type.

3. Enter **Workato** as the application name.

4. Enter a suitable description.

5. **Optional:** Upload an icon.

6. For **Provide App Metadata**, select **Enter from URL**.

7. In the **Import URL** field, enter `https://www.workato.com/saml/metadata?id=your-Workato-ID`.

   |   |                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------- |
   |   | *your-Workato-ID* is a unique value to your Workato account and can be found in the Workato Portal. |

8. In the **ACS URLS** field, enter `https://www.workato.com/saml/consume`.

9. Select the **Signing Key** to use and then click **Download Signing Certificate** to download as X509 PEM (.crt).

10. Leave **SLO Endpoint** and **SLO Response Endpoint** blank.

11. In the **Subject NameID Format** list, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

12. Enter a suitable value for **Assertion Validity Duration (in seconds)**. A value of 300 seconds is typical.

13. Click **Save and Continue**.

14. Workato expects an email address to identify a user in the SSO security assertion:

    * If you use an email address to sign on through PingOne, click **Save and Close**.

    * If you sign on with a username, in the **PingOne User Attribute** list, select **Email Address** to map that to the **SAML\_SUBJECT**, then click **Save and Close**.

15. Click the toggle to enable the application.

16. On the **Configuration** tab of the newly-created Workato application, copy and save the **IDP Metadata URL** value.

    You'll need this when configuring SAML on Workato.

    ![Screen capture of PingOne Connection Details section.](../_images/cid1640211566357.png)

## Add PingOne as an identity provider (IdP) to Workato

1. Sign on to the Workato console as an administrator.

2. In the left navigation pane, click **Tools**.

3. Click the **Members** tab.

4. Select **Team**.

5. Click the **Settings** tab.

   ![Screen capture of Workato Team page with Settings tab open.](_images/ufp1640211723424.png)

6. Enter a **Team name** for the team or company.

7. In the **Authentication method** list, select **SAML based SSO**.

8. In the **SAML\_provider** list, select **Other**.

9. Enter the **Metadata URL** for the Workato SP Connector in PingOne.

## Test the PingOne IdP integration

1. Go to the PingOne Application Portal and sign on with a user account.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | In the Admin console, go to **Dashboard → Environment Properties** to find the **PingOne Application Portal URL**. |

2. Click the Workato icon.

   You're redirected to Workato and signed on with SSO.

## Test the PingOne SP integration

1. Go to <https://app.workato.com/users/sign_in> and enter your email address only.

2. In the PingOne sign-on prompt, enter your PingOne username and password.

   ![Screen capture of PingOne sign-on page.](../_images/yrq1620763776078.png)

   You're redirected back to Workato and signed on.
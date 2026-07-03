---
title: Configuring SAML SSO with Asana and PingOne
description: Learn how to enable Asana sign-on from the PingOne console (IdP-initiated sign-on) and direct Asana sign-on using PingOne (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:asana:umy1635871123376
canonical_url: https://docs.pingidentity.com/configuration_guides/asana/umy1635871123376.html
revdate: May 6, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
---

# Configuring SAML SSO with Asana and PingOne

Learn how to enable Asana sign-on from the PingOne console (IdP-initiated sign-on) and direct Asana sign-on using PingOne (SP-initiated sign-on).

## Before you begin

* Link PingOne to an identity repository containing the users requiring application access.

* Populate Asana with at least one user to test access.

* You must have administrative access to PingOne and a Super Admin account for an Enterprise Organization on Asana.

## Steps

1. Add the Asana application to PingOne:

   1. Sign on to PingOne and go to **Connections → Applications**.

   2. To add a new application, click the + icon next to the **Applications** heading.

      ![Screen capture of PingOne Applications section.](../_images/vxx1638477533848.png)

   3. When prompted to select an application type, select **WEB APP**, then click **Configure** next to **SAML** for the chosen connection type.

   4. Enter `Asana` as the application name.

   5. Enter a suitable description.

   6. Upload an icon if desired.

   7. Click **Next**.

   8. For **Provide App Metadata**, select **Manually Enter**.

   9. In the **ACS URLS** field, enter `https://app/asana.com/-/saml/consume`.

   10. Select the **Signing Key** to use and then click **Download Signing Certificate** to download the certificate as X509 PEM (`.crt`).

   11. In the **Entity ID** field, enter `https://app.asana.com`.

   12. Leave **SLO Endpoint** and **SLO Response Endpoint** blank. Asana does not support single logout (SLO).

   13. Enter a suitable value for **Assertion Validity Duration (in seconds)**. A value of 300 seconds is typical.

   14. Click **Save and Continue**.

   15. Because Asana expects an email address to identify a user in the SSO security assertion:

       Choose from:

       * If you use email address to sign on through PingOne, click **Save and Close**.

       * If you sign on with a username, select **Email Address** in the **PingOne User Attribute** list to map that to the **SAML\_SUBJECT**, then click **Save and Close**.

   16. Enable user access to this new application by moving the toggle to the right.

   17. On the **Configuration** tab of the newly-created Asana application, copy and save the **Issuer ID** and **Initiate Single Sign-On URL**.

       You will need these when configuring SAML on Asana.

       ![Screen capture of PingOne SAML Connection Details section with Issuer ID and Initiate SSO URL highlighted in yellow.](_images/voj1638477570423.png)

2. Add PingOne as an identity provider (IdP) to Asana:

   1. Sign on to Asana with a Super Admin account for your Enterprise Organization.

   2. Click your profile photo and select **Admin Console** in the menu.

   3. Go to the **Security** tab.

   4. Go to the **SAML authentication** tab.

   5. In **SAML options**, click **Optional**.

      |   |                                                                                                                             |
      | - | --------------------------------------------------------------------------------------------------------------------------- |
      |   | This is the recommended value when testing. You can change it later to **Required for all members, except guest accounts**. |

   6. Paste the **Initiate Single Sign-On URL** value that you saved earlier into the **Sign-in page URL** field.

   7. Open the `.crt` file that you downloaded in a text editor and copy and paste the entire contents into the **X.509 certificate** field.

   8. Click **Save configuration**.

3. Test the PingOne IdP integration:

   1. Go to your PingOne Application Portal and sign on with a user account.

      |   |                                                                                                                 |
      | - | --------------------------------------------------------------------------------------------------------------- |
      |   | You can find the PingOne Application Portal URL in the admin console at **Dashboard → Environment Properties**. |

   2. Click the **Asana** icon.

      ### Result:

      You're redirected to the Asana website and signed on with SSO.

4. Test the PingOne service provider (SP) integration:

   1. Go to <https://app.asana.com/>, choose the option to sign on with SSO, and enter your email address only.

      ### Result:

      You're redirected and presented with a PingOne sign on prompt.

   2. Enter your PingOne username and password.

      ![Screen capture of PingOne sign on page.](../_images/jji1620936920163.png)

      ### Result:

      After successful authentication, you're redirected back to Asana and signed on.

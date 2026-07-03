---
title: Configuring SAML SSO with Osano and PingOne
description: Learn how to enable Osano sign-on from the PingOne console (IdP-initiated sign-on) and direct Osano sign-on using PingOne (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:osano:config_saml_osano_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/osano/config_saml_osano_p1.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  add-the-osano-application-to-pingone: Add the Osano application to PingOne
  add-pingone-as-the-identity-provider-idp-to-osano: Add PingOne as the identity provider (IdP) to Osano
  test-the-pingone-idp-integration: Test the PingOne IdP integration
  test-the-pingone-sp-connection: Test the PingOne SP connection
---

# Configuring SAML SSO with Osano and PingOne

Learn how to enable Osano sign-on from the PingOne console (IdP-initiated sign-on) and direct Osano sign-on using PingOne (SP-initiated sign-on).

## Before you begin

* Link PingOne to an identity repository containing the users requiring application access.

* Populate Osano with at least one user to test access.

* You must have administrative access to PingOne and an Admin account for an Enterprise Organization on Osano.

## Add the Osano application to PingOne

1. In PingOne, in the left menu, click **Connections**, then **Applications**.

2. To add a new application, click the + icon next to the **Applications** heading.

   ![Screen capture of PingOne Applications page with an arrow pointing to the plus icon next to Applications.](_images/rgq1635440596008.png)

3. Select **Web App** when prompted to select an application type and click **Configure** next to **SAML** for the chosen connection type.

4. Enter `Osano` as the application name.

5. Enter a suitable description.

6. Upload an icon if desired.

7. Click **Next**.

8. For **Provide App Metadata**, select **Manually Enter**.

9. For ACS URL, enter the value: `https://auth.osano.com/saml2/idpresponse`.

10. Select the **Signing Key** to use and click **Download Signing Certificate** to download as X509 PEM (`.crt`).

11. For **Entity ID**, enter the value: `urn:amazon:cognito:sp:us-east-1_7GtagkRKw`.

    |   |                                                                                                         |
    | - | ------------------------------------------------------------------------------------------------------- |
    |   | Leave **SLO Endpoint** and **SLO Response Endpoint** blank. Osano does not support single logout (SLO). |

12. In the **Subject** NameID Format list, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

13. Set a suitable value for **Assertion Validity Duration (in seconds)**. A value of 300 seconds is typical.

14. Click **Save and Continue**.

15. Change the **saml\_subject** attribute to **Email Address**.

    |   |                                                                                  |
    | - | -------------------------------------------------------------------------------- |
    |   | Osano expects an email address to identify a user in the SSO security assertion. |

16. Select **Add Attribute** and **Ping One Attribute** and enter `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` as the **Application Attribute**.

    Map this to the PingOne **User Attribute** for **Email Address**.

17. Select **Add Attribute** and **Ping One Attribute** and enter `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name` as the **Application Attribute**.

    Map this to the **PingOne User Attribute** for **Name**.

18. Click **Save and Close**.

19. Enable user access to this new application by moving the toggle to the right.

20. On the **Configuration** tab of the newly created Osano application, download the metadata.

    ![Screen capture of PingOne metadata connection details with the Download Metadata button highlighted in yellow.](_images/ume1638477061706.png)

## Add PingOne as the identity provider (IdP) to Osano

1. Open a Support request with your Osano Support Representative and supply the Metadata File exported in the previous procedure. This file should contain the following:

   * **Identity Provider Issuer**

   * **Identity Provider Single Sign-On URL**

   * X.509 Certificate

   Osano configures these settings for your account, and the connection is established.

## Test the PingOne IdP integration

1. Go to the PingOne SSO Application Endpoint for the Osano SP connection.

2. Complete the PingOne authentication.

   You're redirected to your Osano domain.

## Test the PingOne SP connection

1. Go to <https://my.osano.com>, select the option to sign on with SSO, and enter your email address only.

   You're redirected and presented with a PingOne sign on prompt.

2. Enter your PingOne username and password.

   ![Screen capture of PingOne sign on page.](../_images/jji1620936920163.png)

   After successful authentication, you're redirected back to Osano and signed on.
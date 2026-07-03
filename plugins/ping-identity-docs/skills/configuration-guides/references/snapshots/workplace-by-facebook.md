---
title: Configuring SAML SSO with Workplace by Facebook and PingOne for Enterprise
description: Learn how to enable Workplace by Facebook sign-on from the PingOne for Enterprise console (IdP initiated sign-on) and direct Workplace by Facebook sign-on using PingOne for Enterprise (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:workplace_by_facebook:config_saml_workplacebyfacebook_p14e
canonical_url: https://docs.pingidentity.com/configuration_guides/workplace_by_facebook/config_saml_workplacebyfacebook_p14e.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  setup-workplace-app: Set up the supplied Workplace by Facebook Application in PingOne for Enterprise
  add-the-pingone-for-enterprise-idp-connection-to-workplace-by-facebook: Add the PingOne for Enterprise IdP connection to Workplace by Facebook
  test-the-pingone-for-enterprise-idp-initiated-sso-integration: Test the PingOne for Enterprise IdP-Initiated SSO integration
  test-the-pingone-for-enterprise-sp-initiated-sso-integration: Test the PingOne for Enterprise SP-initiated SSO integration
---

# Configuring SAML SSO with Workplace by Facebook and PingOne for Enterprise

Learn how to enable Workplace by Facebook sign-on from the PingOne for Enterprise console (IdP initiated sign-on) and direct Workplace by Facebook sign-on using PingOne for Enterprise (SP-initiated sign-on).

## Before you begin

* Link PingOne for Enterprise to an identity repository containing the users requiring application access.

* Populate Workplace by Facebook with at least one user to test access.

* You must have administrative access to PingOne for Enterprise and Workplace by Facebook.

## Set up the supplied Workplace by Facebook Application in PingOne for Enterprise

1. Make a note of your Workplace by Facebook Organization ID and subdomain, for example, `https://my-org.workplace.com`.

2. Sign on to PingOne for Enterprise and go to **Applications → Application Catalog**.

3. Search for `Workplace by Facebook`.

4. Expand the Workplace by Facebook entry and click the **Setup** icon.

   ![Screen capture of PingOne for Enterprise Application Catalog. The table lists the Application Name as Workplace by Facebook, the Type as SAML, and the expand right arrow icon is highlighted in red.](_images/idr1620934501570.png)

5. Copy the **Issuer** and **IdP ID** values.

6. Download the signing certificate.

   ![Screen capture of PingOne for Enterprise SSO Instructions with the Signing Certificate Download hyperlink, IdP ID field, and Initiate Single Sign-On (SSO) URL field all highlighted in red.](_images/aob1620934881156.png)

7. Click **Continue to Next Step**.

8. Set **ACS URL** to `https://your-subdomain.facebook.com/work/saml.php`.

   Set **EntityID** to `https://www.facebook.com/company/your-organization-ID`.

   ![Screen capture of PingOne for Enterprise SSO attribute values with the URLs for the ACS URL field and Entity ID field highlighted in red.](_images/emc1620935090957.png)

9. Click **Continue to Next Step**.

10. Map **SAML\_SUBJECT** to the attribute containing the Facebook username value (an email address).

    ![Screen capture of PingOne for Enterprise Attribute Mapping table. In the SAML\_SUBJECT row and Identity Bridge Attribute or Literal Value column, the Email (Work) field is highlighted in red, as well as the Advanced button below it.](_images/tjx1620935313716.png)

11. Click **Advanced**.

12. Set **Name ID Format** to **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

    ![Screen capture of PingOne for Enterprise Advanced Attribute options with the Name ID Format to send to SP field highlighted in red.](_images/bvz1620935527108.png)

13. Click **Save**.

14. Click **Continue to Next Step** twice.

15. Click **Add** for all user groups that should have access to Workplace by Facebook.

    ![Screen capture of PingOne for Enterprise Group Access page with search bar for finding distinct groups.](_images/epz1620935705081.png)

16. Click **Continue to Next Step**.

17. Download the signing certificate.

    ![Screen capture of PingOne for Enterprise Signing Certificate and SAML Metadata Download options, with the Signing Certificate Download hyperlink highlighted in red.](_images/otg1620935860703.png)

18. Click **Finish**.

## Add the PingOne for Enterprise IdP connection to Workplace by Facebook

1. Sign on to your Workplace by Facebook console as an administrator.

2. Go to **Admin Panel → Security**.

3. Click the **Authentication** tab.

4. For **Log in**, select **Single Sign-On (SSO)**.

5. Click **Add New SSO Provider**.

6. Set the following field values:

   | Field                        | Setting                                                                                                                                                                                    |
   | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **Allow users to login via** | **SSO only**                                                                                                                                                                               |
   | **SAML URL**                 | `https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=IdP-ID-value` (from [Set up the supplied Workplace by Facebook Application in PingOne for Enterprise](#setup-workplace-app)) |
   | **SAML Issuer URL**          | `Issuer-value` (from [Set up the supplied Workplace by Facebook Application in PingOne for Enterprise](#setup-workplace-app))                                                              |
   | **SAML Certificate**         | Paste in the contents of the signing certificate that you downloaded.                                                                                                                      |

   ![Screen capture of PingOne for Enterprise SSO settings with the SSO only SAML Authentication drop down menu, SAML URL field, SAML Issuer URI field, and SAML certificate field all highlighted in red.](_images/ssm1620936461589.png)

7. Click **Test SSO**.

8. After a successful test, save the changes.

9. Go to **Admin panel → People** and search for the user to use SSO.

10. Edit the user and select **SSO** for **Log in with**.

    |   |                                                                      |
    | - | -------------------------------------------------------------------- |
    |   | See Workplace documentation for setting this value on users in bulk. |

## Test the PingOne for Enterprise IdP-Initiated SSO integration

1. Go to your Ping desktop as a user with Workplace by Facebook access.

   |   |                                                                                               |
   | - | --------------------------------------------------------------------------------------------- |
   |   | To find the Ping desktop URL in the Admin console, go to **Setup → Dock → PingOne Dock URL**. |

2. Complete PingOne for Enterprise authentication.

   You are redirected to your Workplace by Facebook domain.

   ![Screen capture of PingOne for Enterprise Sign On page.](../_images/jji1620936920163.png)

## Test the PingOne for Enterprise SP-initiated SSO integration

1. Go to https\://*your subdomain*.workplace.com.

2. Enter your email address.

3. When you are redirected to PingOne for Enterprise, enter your PingOne for Enterprise username and password.

   ![Screen capture of PingOne for Enterprise Sign On page.](_images/riu1620937056440.png)

   After successful authentication, you're redirected back to Workplace by Facebook.

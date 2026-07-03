---
title: Configuring SAML SSO with Terraform and PingOne
description: Learn how to enable Terraform sign-on from the PingOne SSO console (IdP-initiated sign-on) and direct Terraform login using PingOne SSO (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:terraform:config_saml_terraform_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/terraform/config_saml_terraform_p1.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  add-the-terraform-application-to-pingone: Add the Terraform application to PingOne
  add-pingone-as-an-identity-provider-idp-to-terraform: Add PingOne as an identity provider (IdP) to Terraform
  test-the-pingone-idp-integration: Test the PingOne IdP integration
---

# Configuring SAML SSO with Terraform and PingOne

Learn how to enable Terraform sign-on from the PingOne SSO console (IdP-initiated sign-on) and direct Terraform login using PingOne SSO (SP-initiated sign-on).

## Before you begin

* Link PingOne to an identity repository containing the users requiring application access.

* Populate Terraform with at least one user to test access.

* You must have administrative access to PingOne and an administrative account with site-admin permission on Terraform.

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | Whenever *TFE-HOSTNAME* is specified throughout this document, replace it with the actual value of your Terraform instance hostname. |

## Add the Terraform application to PingOne

1. In PingOne, go to **Connections → Applications** and click + to add a new application.

   ![Screen capture of PingOne Applications page with the plus icon highlighted with an arrow.](_images/dso1635890566045.png)

2. In **Select an Application Type**, click **Web App**.

3. In **Choose Connection Type**, click **Configure** next to **SAML.**

   ![Screen capture of PingOne WebApp New Application option.](_images/vah1638476375929.png)

4. Enter Terraform as the application name.

5. **Optional:** Enter a suitable description.

6. **Optional:** Upload an icon.

7. Click **Next**.

8. For **Provide App Metadata**, select **Manually Enter**.

9. For **ACS URLs**, enter `https://TFE-HOSTNAME/users/saml/auth`

10. Choose the **Signing Key** to use and then click **Download Signing Certificate** to download it as X509 PEM (`.crt`).

11. For **Entity ID,** enter `https://TFE-HOSTNAME/users/saml/metadata`

12. Leave **SLO Endpoint** and **SLO Response Endpoint** blank. Terraform does not support single logout (SLO).

13. In the **Subject NameID Format** list, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

14. Set a suitable value for **Assertion Validity Duration (in seconds)**. A value of 300 seconds is typical.

15. Click **Save and Continue**.

    |   |                                                                                                                                            |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | By default, Terraform generates a **Username** when an account is first created upon initial SSO. This is based on the user email address. |

16. **Optional:** If you want to dictate the **Username** created for a user, you can include the **Username** attribute in the security assertion.

    You can include the **MemberOF** attribute to automatically add users to specific **Teams** in the Terraform platform. Configure which **PingOne User Attribute** to map to each of these Terraform attributes.

    ![Screen capture of Terraform Attribute Mapping section.](_images/okr1638476415149.png)

17. Click **Save and Close**.

18. Enable user access to this new application by moving the toggle to the right.

19. On the **Configuration** tab of the newly created Terraform application, copy and save the **Issuer ID** and **Initiate Single Sign-On URL** values. You will use these for configuring SAML on Terraform.

    ![Screen capture of PingOne metadata about the newly added Terraform application.](_images/hxz1638476449991.png)

## Add PingOne as an identity provider (IdP) to Terraform

1. Go to `https://TFE-HOSTNAME/app/admin/saml` and sign on with an administrator account that has site-admin permissions.

2. Paste the **Initiate Single Sign-On URL** value that you saved previously into the **Single Sign-On URL** field.

3. Open the `.crt` file that downloaded previously in a text editor and copy and paste the entire contents into the **IDP Certificate** field.

4. Click **Save SAML settings**.

## Test the PingOne IdP integration

1. Go to the PingOne application portal and sign on with a user account.

   |   |                                                                                            |
   | - | ------------------------------------------------------------------------------------------ |
   |   | You can find the PingOne Application Portal URL in **Dashboard → Environment Properties**. |

2. Click the Terraform icon.

   You're redirected and presented with a PingOne sign on prompt.

3. Enter your PingOne username and password.

   ![Screen capture of PingOne sign on page.](../_images/jji1620936920163.png)

   After successful authentication, you're redirected back to Terraform as a signed-on user.

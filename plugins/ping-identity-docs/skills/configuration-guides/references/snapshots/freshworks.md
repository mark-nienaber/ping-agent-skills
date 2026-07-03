---
title: Configuring SAML SSO with Freshworks and PingOne
description: Learn how to configure SAML single sign-on (SSO) with Freshworks and PingOne.
component: configuration_guides
page_id: configuration_guides:freshworks:config_saml_freshworks_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/freshworks/config_saml_freshworks_p1.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  configure-sso-in-freshworks: Configure SSO in Freshworks
  configure-sso-in-pingone: Configure SSO in PingOne
  integrate-saml-sso-with-freshworks-and-pingone: Integrate SAML SSO with Freshworks and PingOne
  create-and-assign-identities-in-pingone: Create and assign identities in PingOne
  test-integration: Test the integration
---

# Configuring SAML SSO with Freshworks and PingOne

Learn how to configure SAML single sign-on (SSO) with Freshworks and PingOne.

## Before you begin

You must have a Business level or higher plan in Freshworks. Learn more at <https://support.freshworks.com/support/solutions/articles/237923>.

## Configure SSO in Freshworks

1. Sign on to your Freshworks Admin account homepage and go to the **Security** tab.

   ![Screen capture of Freshworks Admin Center with Security highlighted in red on the lefthand panel.](_images/nme1636412336160.jpg)

2. On the **Security Settings** page, in the **Default Login Methods** section, click the right arrow.

   ![Screen capture of Freshworks Security Settings with an expansion arrow highlighted in red.](_images/old1638472082048.jpg)

3. On the corresponding **Login Methods** page, click the **SSO Login** toggle.

   ![Screen capture of Freshworks Default Login Method page with the SSO Login toggle highlighted in red.](_images/ebj1638472321195.jpg)

   The **Configure SSO** panel opens.

4. On the **Configure SSO** panel, in the **IdP of your choice** section, click **SAML**.

   ![Screen capture of Configure SSO panel with SAML highlighted in red.](_images/bkz1638472376428.jpg)

5. On the **Set up SSO with SAML** page, in the **Map information in IdP** section, make a note of the **Assertion Consumer Services (ACS) URL** and **Service Provider (SP) Entity ID** values. You will need them later.

   Click **Download Metadata**.

   ![Screen capture of Freshworks Configure SSO panel with Download Metadata highlighted in red.](_images/dbn1638472424702.jpg)

## Configure SSO in PingOne

1. In PingOne, go to **Connections → Applications**.

2. Click the + icon next to **Applications**.

   ![Screen capture of Applications tab with the Connections icon and plus icon highlighted in red.](_images/wom1638472472457.jpg)

   |   |                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------- |
   |   | You will use the settings displayed in Step 5 of the previous procedure to begin configuring Freshworks within PingOne. |

3. On the **New Application** page, click **Advanced Configuration**.

4. In the **Choose Connection Type** list, on the **SAML** line, click **Configure**.

   ![Screen capture of New Application page with Advanced Configuration and Configure highlighted in red.](../_images/vkx1638472509882.jpg)

5. In **Create App Profile**, enter the values for:

   * **Application Name** (Required)

   * **Description** (Optional)

   * **Icon** (Optional)

   ![Screen capture of Create App Profile section.](_images/phg1638472574169.jpg)

6. On the **Configure SAML Connection** page, in the **Provide App Metadata** section, click **Import Metadata**.

   Upload the metadata downloaded previously and click **Import**.

   ![Screen capture of Configure SAML Connection section in with Import Metadata and Choose File highlighted in red.](_images/uqb1638472613398.jpg)

   After import, all necessary fields are populated automatically, except for the **Assertion Validity Duration**.

7. In the **Assertion Validity Duration** field, enter a valid duration value (in seconds), such as 3600.

8. In the **Signing Key** section, select **Download Signing Certificate** and download in the **X509 PEM (.crt)** format.

   Make sure that **Sign Assertion & Response** is selected, then click **Save and Continue**.

   ![Screen capture of SSO Signing Key section with Download Signing Certificate and X509 PEM (.crt) highlighted in red.](_images/siu1638472647955.jpg)

9. On the **Attribute Mapping** page, enter the values for the following attributes:

   * **Email Address** = saml\_subject

   * **givenName**

   * **LastName**

   * **mobile**

   * **phone**

   ![Screen capture of SAML Attributes section.](_images/pzl1638472858967.jpg)

10. Click **Save and Close** to finalize the creation of the application.

11. After you create the application, click the toggle next to the application to enable it.

    ![Screen capture of applications with the slider next to Freshworks highlighted.](_images/jhe1637011472230.jpg)

12. Select **Configuration** and copy the following values for later use.

    * **Issuer ID**

    * **Single Logout Service** (Optional)

    * **Single SignOn Service**

    ![Screen capture of Freshworks Configuration with the fields for Issuer ID, Single Logout Service, and Single Sign-on Service highlighted in red.](_images/ecb1637011556822.jpg)

## Integrate SAML SSO with Freshworks and PingOne

1. In Freshworks, go to **Set up SSO with SAML** and paste the information from the previous step into the below locations:

   * **Entity ID provided by the IdP** = the **Issuer ID** value from PingOne

   * **SAML SSO URL** = the **Single SignOn Service** value from PingOne

   * **Logout URL** = the **Single Logout Service** value from PingOne (Optional)

     ![Screen capture of Freshworks Map information from IdP section.](_images/fsz1638473039699.jpg)

2. Upload the X509 certificate that you downloaded previously. Open the downloaded file with a text editor and copy and paste the certificate into the **Security certificate** field, then select **Configure SSO**.

   |   |                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------ |
   |   | You must include the `BEGIN CERTIFICATE` and `END CERTIFICATE` text as part of the certificate upload. |

   ![Screen capture of Security certificate section with Configure SSO highlighted in red.](_images/ieb1638473188273.jpg)

3. Sign out of your Freshworks account, then click the **Sign in with SSO** to sign on.

   You're proxied into your account, finalizing the configuration.

   ![Screen capture of Freshworks login.](_images/pzn1636412465072.jpg)

## Create and assign identities in PingOne

Before you can test the integration, create and assign identities in PingOne. If you've already assigned identities and groups in PingOne, move on to [Test the integration](#test-integration).

1. In PingOne, go to **Identities → Groups** and click the + icon next to **Groups**.

   ![Screen capture of Groups section with the Group icon and plus icon highlighted in red.](_images/mik1638473245369.jpg)

2. On the **Create New Group** page, enter values for the following:

   * **Group Name** (Required)

   * **Description** (Optional)

   * **Population** (Optional)

3. Click **Finish & Save**.

   ![Screen capture of Create New Group section.](_images/aqy1638473302638.jpg)

4. To add identities to the group, on the **Identities** tab, go to **Users → + Add User**.

   ![Screen capture of Users section with + Add User highlighted in red.](_images/snp1638473665760.jpg)

5. On the **Add User** page, enter all the necessary information for a user.

   |   |                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------- |
   |   | Verify that the first name, last name, and email address are correct, as these are values passed in the SAML assertion. |

6. Click **Save**.

7. Assign the user that you created to the group that you created previously.

   Locate the user you created and do the following:

   1. Expand the section for the user.

   2. Select the **Groups** tab.

   3. Click **[icon: plus, set=fa]Add**.

      ![Screen capture of user settings with + Add and Groups highlighted in red.](../_images/agi1638473854046.jpg)

8. In the **Available Groups** section, select the group that you created and click the **[icon: plus, set=fa]**icon to add it to the user's group memberships. Click **Save**.

   ![Screen capture of Admin groups plus icon highlighted in red.](../_images/cjm1638473992117.jpg)

9. On the **Connections** tab for the Freshworks application do the following:

   1. Click the **Access** tab.

   2. Click the **Pencil** icon to edit the configuration.

      ![Screen capture of Freshworks settins in with the Access tab and pencil icon highlighted in red.](_images/fgw1638474050556.jpg)

10. Select the group that you created and add it to the **Applied Groups** section. Click **Save**.

    ![Screen capture of Freshworks application in with the plus icon next to the Admin group highighted in red.](_images/vef1638474131142.jpg)

## Test the integration

You're now ready to test the integration.

1. In the PingOne admin console, go to **Dashboard → Environment Properties**.

2. Right-click on the **Application Portal URL** and open it in a private browser session.

   ![Screen capture of Environment Properties with the Application Portal URL highlighted in red, as well as Open Link in Incognito Window.](../_images/bqo1636413815335.jpg)

3. Sign on as the test user that you created and click the Freshworks tile.

   You're signed on to the user's Freshworks account using SSO and testing is complete.

   ![Screen capture of dock with Freshworks application highlighted in red.](_images/iwm1638474176538.jpg)
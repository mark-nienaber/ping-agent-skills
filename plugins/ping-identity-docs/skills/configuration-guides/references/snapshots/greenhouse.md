---
title: Configuring SAML SSO with Greenhouse and PingOne
description: Learn how to configure SAML single sign-on (SSO) with Greenhouse and PingOne.
component: configuration_guides
page_id: configuration_guides:greenhouse:config_saml_greenhouse_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/greenhouse/config_saml_greenhouse_p1.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  configure-sso-in-greenhouse: Configure SSO in Greenhouse
  configure-greenhouse-in-pingone: Configure Greenhouse in PingOne
  create-and-assign-identities: Create and assign identities
  test-integration: Test the integration
---

# Configuring SAML SSO with Greenhouse and PingOne

Learn how to configure SAML single sign-on (SSO) with Greenhouse and PingOne.

## Before you begin

You must have an Advanced or Expert subscription tier to configure SAML. Learn more in see <https://support.greenhouse.io/hc/en-us/articles/210259723-Single-Sign-On-overview>.

|   |                               |
| - | ----------------------------- |
|   | This is a tested integration. |

## Configure SSO in Greenhouse

1. Sign on to your Greenhouse portal and select the **Gear** icon ([icon: gear, set=fa]) in the upper right hand corner.

2. In the left navigation pane, go to **Dev Center → Single Sign-On** to begin configuring SSO.

   ![Screen capture of Greenhouse Configure section with Dev Center and Single Sign-On highlighted in red.](_images/ofp1638475487482.jpg)

   |   |                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------- |
   |   | If you don't see **Single Sign-On**, you'll need to contact Greenhouse customer support to update your permissions. |

3. On the following page, click **Begin Configuration**.

   The configuration page opens.

4. In the **Add Greenhouse to your Single Sign-on provider** section, note the **SSO Assertion Consumer URL**. You'll need this later.

   ![Screen capture of Greenhouse SSO Assertion Consumer URL.](_images/uco1638475513472.jpg)

## Configure Greenhouse in PingOne

1. On a new tab, sign on to your PingOne SSO admin account.

   You'll use the settings from the previous procedure to start configuring Greenhouse in PingOne.

2. Go to **Connections → Applications** and click the + icon.

   ![Screen capture of PingOne Applications section with the plus icon highlighted in red.](../_images/wos1637005186329.jpg)

3. On the **New Application** page, click **Advanced Configuration**, and on the **SAML** line, click **Configure**.

   ![Screen capture of PingOne New Application section with Advanced Configuration and Configure highlighted in red.](../_images/vkx1638472509882.jpg)

4. On the **Create App Profile** page, enter:

   * **Application Name** (Required)

   * **Description** (Optional)

   * **Icon** (Optional)

   ![Screen capture of PingOne Create App Profile with Greenhouse information populated.](_images/hpo1638475595689.jpg)

5. Click **Save and Continue**.

6. On the **Configure SAML Connection** page, in the **Provide App Metadata** section, click **Manually Enter**.

   ![Screen capture of PingOne App Metadata section with the Manually Enter radio button selected.](_images/tut1638475626984.jpg)

7. Input the service provider (SP) data:

   * In the **ACS URLS** field, paste in the **SSO Assertion Consumer URL** that you copied from Greenhouse in the previous procedure.

     ![Screen capture of PingOne Application Metadata section with the ACS URLS field highlighted in red.](_images/ovw1637005671503.jpg)

   * In the **Entity ID** field, enter `greenhouse.io`.

     ![Screen capture of PingOne entity ID field with greenhouse.io input and highlighted in red.](_images/ved1638475706520.jpg)

   * In the **Assertion Validity Duration (In Seconds)**, enter a value, for example, `3600`.

     ![Screen capture of PingOne Assertion Validity Duration field with 3600 input and highlighted in red.](_images/cth1638475733682.jpg)

8. Click **Save and Continue**.

9. On the **Attribute Mapping** page, add the following attributes, selecting the **Required** check box for each attribute.

   * **saml\_subject** = **Email Address**

     |   |                                                                         |
     | - | ----------------------------------------------------------------------- |
     |   | This is automatically assigned to User ID, but will need to be updated. |

   * **User.FirstName** = **Given Name**

   * **User.LastName** = **Family Name**

   ![Screen capture of PingOne SAML Attribute Mappings.](_images/ixn1638475774564.jpg)

10. Click **Save and Close**.

11. On the **Applications** page, enable the connection by toggling the slider:

    ![Screen capture of Greenhouse application in PingOne with the toggled slider highlighted in red.](_images/dsy1638475855555.jpg)

12. Click on the newly created application to open it.

13. On the **Configuration** tab, in the **Connection Details** section, click **Download** to download the IdP metadata.

    You'll need this to complete the next step.

    ![Screen capture of PingOne application section with Greenhouse metadata and the Configuration tab and Download button highlighted in red.](_images/rio1637006995582.jpg)

14. Return to Greenhouse and, in the **Upload your Single Sign-On Provider** section, click **Choose File** and upload the IdP metadata that you downloaded in the previous step.

    ![Screen capture of Greenhouse SSO metadata XML file section with Choose File highlighted in red.](_images/mlf1638475942709.jpg)

    All required fields will be populated automatically, except for the **Name Identifier Format**.

15. Update the **Name Identifier Format** to `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`.

    Click **Save**.

    ![Screen capture of Greenhouse SSO Metadata section with the Name Identifier Format list and Save button highlighted in red.](_images/caj1637007463372.jpg)

## Create and assign identities

Before you can test the integration, you must create and assign identities in PingOne. If you've already assigned identities and groups in PingOne, move on to [Test the integration](#test-integration).

1. In PingOne, go to **Identities** **Groups** and click the + icon next to **Groups.**

2. On the **Create New Group** page, enter values for the following:

   * **Group Name** (Required)

   * **Description** (Optional)

   * **Population** (Optional)

3. Click **Finish & Save**.

   ![Screen capture of PingOne Groups section.](../_images/kvs1637007913530.jpg)

4. To add identities to the group, on the **Identities** tab, go to **Users → + Add User**.

   ![Screen capture of PingOne Users page with + Add User highlighted in red.](../_images/aas1637008099896.jpg)

5. On the **Add User** page, enter all the necessary information for a user.

   |   |                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------- |
   |   | Verify that the first name, last name, and email address are correct, as these are values passed in the SAML assertion. |

6. Click **Save**.

   ![Screen capture of PingOne Add User section with Save highlighted in red.](../_images/kzl1638474889926.jpg)

7. Assign the user that you created to the group that you created previously. Locate the user you created and do the following:

   * Expand their section.

   * Select the **Groups** tab.

   * Click **[icon: plus, set=fa]Add**.

     ![Screen capture of PingOne user section with the Groups tab and + Add button highlighted in red.](../_images/agi1638473854046.jpg)

8. In the **Available Groups** section, select the group that you created and click the **[icon: plus, set=fa]**icon to add it to the user's group memberships. Click **Save**.

   ![Screen capture of PingOne user settings in the Available Groups section with the plus icon next to Admin highlighted in red.](../_images/cjm1638473992117.jpg)

9. On the **Connections** tab, for the Greenhouse application, do the following:

   * Click the **Access** tab.

   * Click the **Pencil** icon to edit the configuration.

   ![Screen capture of PingOne application section with the Greenhouse Access tab and pencil icon highlighted in red.](_images/pvy1637009264980.jpg)

10. Select the group that you created and add it to the **Applied Groups** section. Click **Save**.

    ![Screen capture of Greenhouse Edit Access section with the plus icon next to Admin group highlighted in red.](_images/ayy1638476133533.jpg)

## Test the integration

1. In the PingOne admin console, go to **Dashboard → Environment Properties**.

2. Right-click on the **Application Portal URL** and open it in a private browser session.

   ![Screen capture of PingOne Environment Properties with the Application Portal URL selected and Open Link in Incognito Window highlighted in red.](_images/nal1637010202252.jpg)

3. Sign on as the test user that you created and click the Greenhouse tile.

   ![Screen capture of PingOne dock with Greenhouse tile highlighted in red.](_images/aid1638476186562.jpg)

   You're signed on to the user's Greenhouse account.

4. On the SSO configuration page in Greenhouse, click **Finalize Configuration**.

   ![Screen capture of Greenhouse SSO Configuration settings with Finalize Configuration highlighted in red.](_images/zjw1637010413258.jpg)

5. When prompted, enter `Configure`. Click **Finalize** to complete the connection.

   ![Screen capture of Greenhouse SSO Configuration settings with Configure and Finalize highlighted in red.](_images/ejn1638476226737.jpg)
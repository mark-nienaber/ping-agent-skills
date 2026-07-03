---
title: Configuring SAML SSO with Aha! Ideas and PingOne
description: Learn how to configure SAML SSO using Aha! Ideas and PingOne.
component: configuration_guides
page_id: configuration_guides:aha!_ideas:config_saml_ahalabs_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/aha!_ideas/config_saml_ahalabs_p1.html
revdate: May 15, 2024
section_ids:
  about-this-task: About this task
  obtain-your-saml-configuration-from-aha-ideas: Obtain your SAML configuration from Aha! Ideas
  configure-aha-ideas-in-pingone: Configure Aha! Ideas in PingOne
  create-and-assign-identities: Create and assign identities
  test-integration: Test the integration
---

# Configuring SAML SSO with Aha! Ideas and PingOne

Learn how to configure SAML SSO using Aha! Ideas and PingOne.

## About this task

Learn more about Aha! and SAML SSO in [Aha! Roadmaps | Account SSO | SAML 2.0](https://www.aha.io/support/roadmaps/account/single-sign-on/configure-sso-saml-2-point-0) on the Aha! support site.

## Obtain your SAML configuration from Aha! Ideas

1. Sign on to your Aha! Ideas admin account.

2. On the **Account settings** page, go to **Account → Security and single sign-on**.

   ![Screen capture of Aha! Ideas account settings sidebar with Account and Security and single sign-on highlighted in red.](_images/mtv1638821476223.jpg)

3. In the **Single sign-on** section, in the **Identity provider** list, select **SAML 2.0**.

   ![Screen capture of Aha! Ideas Single sign-on settings with SAML 2.0 selected as the Identity provider.](_images/vaq1638821646925.jpg)

   The **SAML 2.0 Configuration** page opens.

   Keep this tab open as you will need these settings in the next procedure.

## Configure Aha! Ideas in PingOne

1. In a new tab, sign on to your PingOne SSO admin account.

   You'll use the settings from the previous procedure to configure Aha! Ideas in PingOne.

2. Go to **Connections → Applications** and click the + icon.

   ![Screen capture of PingOne Applications page with the plus icon highlighted in red.](_images/whg1639074540980.jpg)

3. On the **New Applications** page, click **Advanced Configuration** and on the **SAML** line, click **Configure**.

   ![Screen capture of PingOne new application section with advanced configuration highlighted in red.](../_images/vkx1638472509882.jpg)

4. On the **Create App Profile** page, enter:

   * **Application Name** (Required)

   * **Description** (Optional)

   * **Icon** (Optional)

   ![Screen capture of PingOne Create App Profile section with fields filled out for Aha! Ideas.](_images/qbg1639074606881.jpg)

5. On the **Configure SAML Connection** page, in the **Provide App Metadata** section, click **Manually Enter**.

   ![Screen capture of PingOne Configure SAML Connection section with the Manually Enter radio button selected.](../_images/gdx1638480003458.jpg)

6. On your Aha! Ideas tab, copy the **SAML consumer URL** and **SAML Entity ID** values to a text editor.

   |   |                                                                      |
   | - | -------------------------------------------------------------------- |
   |   | The URLs are hard-coded and grayed-out, but you can still copy them. |

   ![Screen capture of Aha! Ideas SAML 2.0 Configuration settings with the SAML consumer ID and SAML entity ID highlighted in red.](_images/pzf1638822506345.jpg)

7. In your PingOne SSO account, paste the **SAML consumer URL**value into the **ACS URLS** section and the **SAML entity ID** value into the **Entity ID** section.

   ![Screen capture of PingOne metadata fields with the Aha! Ideas URLs pasted from the previous step.](_images/tct1638822693765.jpg)

8. Enter a value in the **Assertion Validity Duration** field, such as 3600, and then click **Save and Continue**.

   ![Screen capture of PingOne Assertion Validity Duration field highlighted in red, as well as the Save and Continue.](_images/zgu1638825395180.jpg)

9. On the **Attribute Mapping** page, add the following **PingOne Attributes**:

   | User Attribute    | Application Attribute |
   | ----------------- | --------------------- |
   | **Email Address** | **EmailAddress**      |
   | **Family Name**   | **LastName**          |
   | **Given Name**    | **FirstName**         |

   |   |                                          |
   | - | ---------------------------------------- |
   |   | Leave the default **User ID** attribute. |

   ![Screen capture of PingOne SAML Attribute mapping section.](_images/qek1638825666617.jpg)

10. Click **Save and Close**.

    The **Applications** page opens.

11. In the **Applications** page:

    1. Click the toggle to enable the configuration by selecting the slider.

    2. On the **Configuration** tab, in the **Download Metadata** section, click **Download**.

       You'll upload this in Aha! Ideas in the next step.

       ![Screen capture of Aha! Ideas connection details in PingOne.](_images/fyq1639074680384.jpg)

12. On your Aha! Ideas tab, in the **Configure using** section, click **Metadata file** and click **Choose File** to upload the file that you downloaded in the previous step.

    ![Screen capture of Aha! Ideas metadata file section.](_images/cro1638826362590.jpg)

13. Enter a **Name** for the connection, such as Ping Identity, and click **Enable** to turn on the configuration.

    ![Screen capture of Aha SAML 2.0 Configuration section with the Name and Enable button highlighted in red.](_images/rve1638826713905.jpg)

## Create and assign identities

If you've already assigned identities and groups in PingOne, move on to [Test the integration](#test-integration).

1. In PingOne, go to **Identities → Groups** and click the + icon next to **Groups**.

2. On the **Create New Group** page, enter values for the following:

   * **Group Name** (Required)

   * **Description** (Optional)

   * **Population** (Optional)

3. Click **Finish & Save**.

   ![Screen capture of PingOne Groups section.](../_images/kvs1637007913530.jpg)

4. To add identities to the group, on the **Identities** tab, go to **Users → + Add User**.

   ![Screen capture of PingOne Users section with + Add User highlighted in red.](../_images/aas1637008099896.jpg)

5. On the **Add User** page, enter in all the necessary information for a user.

   |   |                                                                                              |
   | - | -------------------------------------------------------------------------------------------- |
   |   | Verify that the email address is correct, as this is the value passed in the SAML assertion. |

6. Click **Save**.

   ![Screen capture of PingOne Add User section with the Save button highlighted in red.](../_images/kzl1638474889926.jpg)

7. To assign the user that you created to the group that you created previously, locate the user you created and:

   1. Expand their section.

   2. Select the **Groups** tab.

   3. Click **[icon: plus, set=fa]Add**.

      ![Screen capture of PingOne user section with Groups and + Add highlighted in red.](../_images/agi1638473854046.jpg)

8. In the **Available Groups** section, select the group that you created and click the [icon: circle-plus, set=fa]icon to add it to the user's group memberships. Click **Save**.

   ![Screen capture of PingOne user with the + icon next to Admin highlighted in red.](../_images/cjm1638473992117.jpg)

9. On the **Connections** tab, for the Aha! Ideas application:

   1. Click the **Access** tab.

   2. Click the **Pencil** icon to edit the configuration.

      ![Screen capture of Aha! Ideas access settings in PingOne.](_images/kcn1639074750268.jpg)

10. Select the group that you created and add it to the **Applied Groups** section. Click **Save**.

    ![Screen capture of Aha Ideas admin access in PingOne.](_images/mlo1639074794513.jpg)

## Test the integration

1. In the PingOne admin console, go to **Dashboard → Environment Properties**.

2. Right-click on the **Application Portal URL** and open it in a private browser session.

   ![Screen capture of PingOne Environment section with the Application Portal URL selected and Open Link in Incognito Window highlighted in red.](../_images/bqo1636413815335.jpg)

3. In your private browser window, sign on as the test user that you created and click the Aha! Ideas tile.

   ![Screen capture of Aha! Ideas as a tile in PingOne.](_images/rdq1639074898435.jpg)

   You're now signed on to the user's Aha! Ideas account.

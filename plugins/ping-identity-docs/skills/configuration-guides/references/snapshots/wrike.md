---
title: Configuring SAML SSO with Wrike and PingOne
description: Learn how to configure SAML SSO with Wrike and PingOne.
component: configuration_guides
page_id: configuration_guides:wrike:config_saml_wrike_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/wrike/config_saml_wrike_p1.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  download-the-wrike-metadata: Download the Wrike metadata
  choose-from: Choose from:
  import-the-metadata-into-pingone: Import the metadata into PingOne
  choose-from-2: Choose from:
  create-and-assign-identities-in-pingone: Create and assign identities in PingOne
  test-integration: Test the integration
---

# Configuring SAML SSO with Wrike and PingOne

Learn how to configure SAML SSO with Wrike and PingOne.

## Before you begin

You must have Business Level permissions to configure SAML.

## About this task

Learn more about Wrike and SSO in the [SAML SSO: Implementation Guide](https://help.wrike.com/hc/en-us/articles/209605769-SAML-SSO-Implementation-Guide/) in the Wrike documentation.

|   |                              |
| - | ---------------------------- |
|   | This is a tested integration |

## Download the Wrike metadata

1. Sign on to your Wrike admin account and in the upper right-hand corner, select your name and then **Settings**.

2. Go to **Security → Setup SAML SSO**.

3. In the **Set up your identity provider** list, select **Other**.

4. Download the service provider (SP) metadata:

   ### Choose from:

   * Click **Download XML file**.

   * Copy the metadata link.

5. Click **Next**.

## Import the metadata into PingOne

1. In a new tab, sign on to your PingOne SSO admin account and go to **Connections → Applications** and click the **[icon: plus, set=fa]**icon.

2. On the **New Application** page, click **Advanced Configuration**, and on the **SAML** line, click **Configure**.

3. On the **Create App Profile** page, enter the following information:

   * **Application Name**

   * Optional: **Description**

   * Optional: **Icon**

4. Click **Save and Continue**.

5. The **Configure SAML Connection** page allows for a few options to configure the SP metadata in PingOne. Only one of the following is required to import the metadata:

   ### Choose from:

   * Click **Import Metadata** to import the metadata file that you downloaded in the previous procedure.

   * Click **Import from URL** to upload the copied link from the previous procedure.

   * If you know the Wrike SP metadata details, manually enter the required information.

   |   |                                                                                                                                                                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | All required information is filled out if you choose **Import Metadata** or **Import From URL** except for the **SUBJECT NAMEID FORMAT**.You must update the SUBJECT NAMEID FORMAT to `urn:oasis:nams:tc:SAML:1.1:nameid-format:emailAddress`. If you set this to something else, you'll get a connection error. |

6. Click **Save and Continue**.

7. On the **Attribute** mapping page, add the following attributes and mark all as **Required**.

   * **firstName**

   * **lastName**

   * **NameID**

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | The PingOne **User Attribute** for the **saml\_subject** must be updated to **Email Address** and not **User ID**. |

8. Click **Save and Close**.

9. On the **Applications** page, click the **Configuration** tab and copy the URL on the **IDP METADATA URL** line.

10. On your Wrike tab, paste the URL that you copied in the previous step into the **Use URL to provide XML** field and click **Next**.

11. Click **Enable SAML settings** to finalize the configuration of the SAML connection.

    You'll receive a verification email providing you with a 6-digit code.

12. Copy and paste the 6-digit code into the confirmation box to verify the connection and then click **Confirm** to finalize set up.

    A page with information on testing opens.

    |   |                                                                                                                                                             |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Although this page provides you with information on testing the SAML SSO set up, follow [Test the integration](#test-integration) to test your integration. |

13. Click **Save**.

## Create and assign identities in PingOne

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | If you've already assigned identities and groups in PingOne, go to [Test the integration](#test-integration). |

1. In PingOne, go to **Identities → Groups** and click the **[icon: plus, set=fa]**icon next to **Groups.**

2. On the **Create New Group** page, enter values for the following:

   * **Group Name** (Required)

   * **Description** (Optional)

   * **Population** (Optional)

3. Click **Finish & Save**.

4. To add identities to the group, on the **Identities** tab, go to **Users → + Add User**.

5. On the **Add User** page, enter the necessary information for a user.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | Verify the first name, last name, and email address are correct, as these are values passed in the SAML assertion. |

6. Click **Save**.

7. Assign the user that you created to the group that you created previously.

   Locate the user you created and:

   1. Expand the section for the user.

   2. Select the **Groups** tab.

   3. Click **[icon: plus, set=fa]Add**.

8. In the **Available Groups** section, select the group that you created and click the **[icon: plus, set=fa]**icon to add it to the user's group memberships. Click **Save**.

9. On the **Connections** tab, for the Wrike application:

   * Click the **Access** tab

   * Click the **Pencil** icon to edit the configuration

10. Select the group that you created and add it to the **Applied Groups** section. Click **Save**.

    You're now ready to test the integration.

## Test the integration

1. In the PingOne admin console, go to **Dashboard → Environment Properties**.

2. Right-click on the **Application Portal URL** and open it in a private browser session.

3. Sign on as the test user that you created and click the Wrike tile.

   You're signed on to the user's Wrike account using SSO and testing is complete.

---
title: Configuring SAML SSO with Datadog and PingOne
description: Learn how to enable SAML SSO with Datadog and PingOne
component: configuration_guides
page_id: configuration_guides:datadog:config_saml_datadog_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/datadog/config_saml_datadog_p1.html
revdate: May 16, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  set-up-the-integration: Set up the integration
  create-and-assign-identities: Create and assign identities
  test-integration: Test the integration
---

# Configuring SAML SSO with Datadog and PingOne

Learn how to enable SAML SSO with Datadog and PingOne

## Before you begin

To enable SSO within Datadog, you must have an administrator account.

## About this task

|   |                               |
| - | ----------------------------- |
|   | This is a tested integration. |

## Set up the integration

1. Sign on to your PingOne SSO admin account and go to **Connections → Applications** and click the plus icon (+).

2. On the **New Application** page, click **Advanced Configuration**, and on the **SAML** line, click **Configure**.

3. On the **Create App Profile** page, enter the following:

   1. **Application Name**

   2. **Optional:** **Description**

   3. **Optional:** **Icon**

4. Click **Next**.

5. On the corresponding **Configure SAML Connection** page, click **Manually Enter** to begin configuring Datadog with PingOne.

6. In a new tab, sign on to your Datadog admin account. In the lower left hand corner, click on your account name and then **Configure SAML**, which will contain information for the next step.

7. In PingOne, enter the following information for the required fields:

   1. The **ACS URL(s)** of the application.

      You can find this on the Datadog admin console under **Assertion Consumer Service URL**.

   2. The **Entity ID** of the application. from the previous step.

      You can find this on the Datadog admin console under **Service Provider Entity ID**.

   3. Update the **SUBJECT NAMEID FORMAT** to `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`.

   4. Enter the **Assertion Validity Duration (in seconds)**, for example, `3600`.

   5. Configure the remaining options as needed.

   6. Click **Save and Continue**.

8. On the **Attribute Mapping** page, enter the following attributes:

   1. Outgoing value: **User ID** = Application Attribute: **saml\_subject** (required).

   2. Outgoing value: **Family Name** = Application Attribute: **sn**

   3. Outgoing value: **Given Name** = Application Attribute: **givenName**

   4. Outgoing value: **Username** = Application Attribute: **eduPersonPrincipalName**

   5. Click **Save and Close**.

      |   |                                                                                                         |
      | - | ------------------------------------------------------------------------------------------------------- |
      |   | You can add additional attributes to control roles. See the Datadog documentation for more information. |

9. On the newly-created application, click the **Configuration** tab and click **Download Metadata**.

10. In your Datadog account, click **Choose File**, upload the IdP metadata that you downloaded in the previous step, and click **Upload File**.

11. After uploading the IdP metadata and configuring your IdP, click **Enable** to enable SAML and finalize the configuration.

12. If you're leveraging this integration for an IdP-initiated sign-on, in the **Additional Features** section of Datadog, make sure to select the **Identity Provider (IdP) Initiated Login** check box.

    The set up is now complete.

## Create and assign identities

Before you test the integration, you must create and assign identities in PingOne.

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | If you've already assigned identities and groups in PingOne, you can [test the integration](#test-integration). |

1. In PingOne, go to **Identities → Groups** and click the **[icon: plus, set=fa]**icon next to **Groups.**

2. On the **Create New Group** page, enter values for the following:

   * **Group Name** (Required)

   * **Description** (Optional)

   * **Population** (Optional)

3. Click **Finish & Save**.

4. To add identities to the group, on the **Identities** tab, go to **Users → + Add User**.

5. On the **Add User**page, enter in all the necessary information for a user.

   |   |                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------- |
   |   | Verify the first name, last name, USER ID, and USERNAME are correct, as these are values passed in the SAML assertion. |

6. Click **Save**.

7. Assign the user that you created to the group that you created previously.

   Locate the user you created and do the following:

   1. Expand the section for the user.

   2. Select the **Groups** tab.

   3. Click **[icon: plus, set=fa]Add**.

8. In the **Available Groups** section, select the group that you created and click the **[icon: plus, set=fa]**icon to add it to the user's group memberships. Click **Save**.

9. On the **Connections** tab, for the Datadog application:

   * Click the **Access** tab

   * Click the **Pencil** icon to edit the configuration

10. Select the group that you created and add it to the **Applied Groups** section. Click **Save**.

## Test the integration

1. In the PingOne admin console, go to **Dashboard → Environment Properties**.

2. Right-click on the **Application Portal URL** and open it in a private browser session.

3. Sign on as the test user that you created and click the Datadog tile.

   You're signed on to the user's Datadog account using SSO and testing is complete.
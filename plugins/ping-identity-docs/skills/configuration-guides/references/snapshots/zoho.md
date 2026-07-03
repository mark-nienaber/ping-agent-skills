---
title: Configuring SAML SSO with Zoho and PingOne
description: Learn how to configure SAML SSO using Zoho and PingOne.
component: configuration_guides
page_id: configuration_guides:zoho:config_saml_zoho_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/zoho/config_saml_zoho_p1.html
revdate: May 15, 2024
section_ids:
  configue-saml-in-pingone: Configue SAML in PingOne
  set-up-saml-in-zoho: Set up SAML in Zoho
  input-the-service-provider-sp-data: Input the service provider (SP) data
  configure-zoho-for-sso: Configure Zoho for SSO
  create-and-assign-identities-in-pingone: Create and assign identities in PingOne
  test-integration: Test the integration
---

# Configuring SAML SSO with Zoho and PingOne

Learn how to configure SAML SSO using Zoho and PingOne.

## Configue SAML in PingOne

1. In PingOne, go to **Connections → Applications** and click the + icon.

   ![Screen capture of PingOne application list.](_images/ylg1638479232778.jpg)

2. On the **New Application** page, click **Advanced Configuration**.

3. On the **SAML** line, click **Configure**.

   ![Screen capture of PingOne new application advanced configuration.](../_images/vkx1638472509882.jpg)

4. On the **Create App Profile** page, enter the following details:

   * **Application Name** (Required)

   * **Description** (Optional)

   * **Icon** (Optional)

   ![Screen capture of PingOne Create App Profile section with Zoho information filled in.](_images/fca1638479854338.jpg)

5. Click **Save and Continue**.

6. On the **Configure SAML Connection** page, in the **Provide App Metadata** section, select **Manually Enter**.

   ![Screen capture of PingOne SAML connection configuration section with the Manually Enter radio button selected and highlighted in red.](../_images/gdx1638480003458.jpg)

## Set up SAML in Zoho

1. In a separate browser tab, sign on to your Zoho Directory admin account (directory.zoho.com).

2. Go to **Security → Custom Authentication**, select **Setup Now**, and note the **ACS URL** value.

   ![Screen capture of Zoho security settings with the ACS URL highlighted in red.](_images/crx1638480121641.jpg)

3. Copy the **ACS URL** value from the previous step.

4. Go to your PingOne SSO browser tab and paste this value into the **ACS URLS** field.

   ![Screen capture of PingOne configure SAML connection page with the Zoho ACS URLS field highlighted in red.](_images/xuj1638480206096.jpg)

## Input the service provider (SP) data

1. Enter the **ENTITY ID** in PingOne.

   |   |                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This configuration example uses `https://directory.zoho.com`. Refer to the following table for instructions on which Entity ID to use, based on your location. |

   | Zoho Directory account DC | Identifier (Entity ID) | Relay state                    |
   | ------------------------- | ---------------------- | ------------------------------ |
   | US                        | zoho.com               | https\://directory.zoho.com    |
   | EU                        | zoho.eu                | https\://directory.zoho.eu     |
   | IN                        | zoho.in                | https\://directory.zoho.in     |
   | AU                        | zoho.com.au            | https\://directory.zoho.com.au |
   | CN                        | zoho.com.cn            | https\://directory.zoho.com.cn |

2. Update the **SUBJECT NAMEID FORMAT** to **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

3. In the **Assertion Validity Duration (In Seconds)** field, enter a value, for example `3600`.

   ![Screen capture of PingOne SP data with values for Zoho entity ID, subject nameID format, and assertion validity highlighted in red.](_images/lzc1638480491085.jpg)

4. In the **Signing Key**, click **Download Signing Certificate** and select **X509 PEM (.crt)**for the format.

   You'll need the signing certificate later.

   ![Screen capture of PingOne signing certificate download button and C509 PEM (.crt) highlighted in red.](../_images/jao1638474529759.jpg)

5. On the **Attribute Mapping** tab, in the **SAML Attributes** section, map the **Outgoing Value** for **saml\_subject** to **Email Address**.

   |   |                                                                  |
   | - | ---------------------------------------------------------------- |
   |   | This is the only required attribute for a successful connection. |

   ![Screen capture of PingOne Attribute Mapping section with the Email Address outgoing value highlighted in red.](_images/cox1638480821760.jpg)

6. Click **Save and Close**.

7. On the **Applications** page, next to **Zoho Directory**, click the toggle to enable the connection.

   ![Screen capture of Zoho Directory added to PingOne with the toggle highlighted in red.](_images/idt1638481090968.jpg)

8. On the **Configuration** tab, in the **Configuration Details** section, note the **Single Logout Service** and **Single SignOn Service** values.

   You'll need these to complete the next procedure.

   ![Screen capture of Zoho Directory in PingOne with the single logout service and single signon service URLs highlighted in red.](_images/cvk1638481197759.jpg)

## Configure Zoho for SSO

1. In Zoho, on the **Custom Authentication** page, paste the **Single SignOn Service** value from PingOne into the **Sign-in URL**.

2. **Optional:** Paste the **Single Logout Service** value from PingOne into the **Sign-out URL** field.

   ![Screen capture of Zoho Sign-in URL and Sign-out URL highlighted in red.](_images/foj1638481316025.jpg)

3. **Optional:** If required, enter your site's password change URL in the **Change Password URL** field.

4. In the **Verification Certificate** section, click **Browse** and upload the X509 certificate that you downloaded previously.

   ![Screen capture of Zoho verification certificate.](_images/rum1638481428944.jpg)

5. Click **Save** to save the connection and complete the setup.

## Create and assign identities in PingOne

If you've already assigned identities and groups in PingOne, move on to [Test the integration](#test-integration).

1. In PingOne, go to **Identities Groups** and click the **[icon: plus, set=fa]**icon next to **Groups**.

2. On the **Create New Group** page, enter values for the following:

   * **Group Name** (Required)

   * **Description** (Optional)

   * **Population** (Optional)

3. Click **Finish & Save**.

   ![Screen capture of PingOne Groups section.](../_images/kvs1637007913530.jpg)

4. To add identities to the group, on the **Identities** tab, go to **Users → + Add User**.

   ![Screen capture of PingOne Users section with + Add User highlighted in red.](_images/thw1638481695367.jpg)

5. On the **Add User** page, enter the required information for a user.

   |   |                                                                                              |
   | - | -------------------------------------------------------------------------------------------- |
   |   | Verify that the email address is correct, as this is the value passed in the SAML assertion. |

6. Click **Save**.

   ![Screen capture of PingOne add user section with Save highlighted in red.](../_images/kzl1638474889926.jpg)

7. Assign the user that you created to the group that you created previously. Locate the user and do the following:

   1. Expand their section.

   2. Select the **Groups** tab.

   3. Click **[icon: plus, set=fa]Add**.

   ![Screen capture of PingOne user with Groups and + Add highlighted in red.](../_images/agi1638473854046.jpg)

8. In the **Available Groups** section, select the group you created and click the **[icon: plus, set=fa]**icon to add it to the user's group memberships. Click **Save**.

   ![Screen capture of PingOne User under Groups tab with the + icon next to Admin highlighted in red.](../_images/cjm1638473992117.jpg)

9. On the **Connections** tab, for the Zoho Directory application, do the following:

   1. Click the **Access** tab.

   2. Click the **Pencil** icon to edit the configuration.

      ![Screen capture of Zoho Directory acces tab with the pencil edit icon highlighted in red.](_images/hsn1638482184485.jpg)

   3. Select the group that you created and add it to the **Applied Groups** section. Click **Save**.

      ![Screen capture of Zoho Directory edit access section with the plus icon next to Admin highlighted in red.](_images/lsm1638482265599.jpg)

## Test the integration

1. In the PingOne admin console, go to **Dashboard → Environment Properties**.

2. Right-click on the **Application Portal URL** and open it in a private browser session.

   ![Screen capture of PingOne environment settings with the application portal URL highlighted with open link in incognito window.](_images/zqa1638482562700.jpg)

3. Sign on as the test user that you created and click the **Zoho Directory** tile.

   ![Screen capture of PingOne dock with Zoho Directory added as a tile.](_images/nnd1638482640807.jpg)

   You're signed on to the user's Zoho Directory account.
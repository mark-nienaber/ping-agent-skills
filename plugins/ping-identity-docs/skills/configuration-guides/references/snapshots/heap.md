---
title: Configuring SAML SSO with Heap and PingOne
description: Learn how to configure SAML single sign-on (SSO) with Heap and PingOne.
component: configuration_guides
page_id: configuration_guides:heap:config_saml_heap_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/heap/config_saml_heap_p1.html
revdate: May 15, 2024
section_ids:
  configure-sso-with-heap: Configure SSO with Heap
  create-and-assign-identities: Create and assign identities
  test-integration: Test your integration
---

# Configuring SAML SSO with Heap and PingOne

Learn how to configure SAML single sign-on (SSO) with Heap and PingOne.

## Configure SSO with Heap

1. Sign on to your Heap admin portal and make sure that you're in the **Development** section.

2. In the left hand pane, go to **Account → Manage → General Settings**.

3. In the **Single Sign-On** section, copy the **Metadata URL**. You'll need this later.

   ![Screen capture of Heap SSO Configuration general settings with Main, General Settings, Account, Manage, SSO, and the Metadata URL highlighted in red.](_images/vgw1638474339686.jpg)

4. In a new tab, sign on to your PingOne admin account and go to **Connections → Applications**.

5. Click the + icon next to **Applications**.

   ![Screen capture of admin console Applications section with the plus icon highlighted in red.](_images/qdi1638474384807.jpg)

6. On the **New Application** page, click **Advanced Configuration**.

7. In the **Choose Connection Type** list, on the **SAML** line, click **Configure**.

   ![Screen capture of New Application Advanced Configuration highlighted in red.](_images/vuu1638474423553.jpg)

8. On the **Create App Profile** page, enter the values for:

   * **Application Name** (Required)

   * **Description** (Optional)

   * **Icon** (Optional)

   ![Screen capture of Create App Profile panel with Heap details entered.](_images/kfd1638474450253.jpg)

9. On the **Configure SAML Connection** page, in the **Provide App Metadata** section, click **Import From URL**.

   Paste in the URL that you copied previously and click **Import**.

   ![Screen capture of Configure SAML Connection page with the Import from URL radio button and Import URL highlighted in red.](_images/njw1638474484427.jpg)

   After import, all necessary fields are auto-populated except for the **Assertion Validity Duration**.

10. In the **Assertion Validity Duration** field, enter a valid duration value (in seconds), such as 3600.

11. Update the **SUBJECT NAMEID FORMAT** section to `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`.

    |   |                                                                                                                                                                                   |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you don't update this section, you'll get an error for the integration. **SUBJECT NAMEID FORMAT** does not automatically update when you upload the service provider metadata. |

12. In the **Signing Key** section, select **Download Signing Certificate** and download in the **X509 PEM (.crt)** format. Click **Save and Continue**.

    ![Screen capture of Signing Key section with Download Signing Certificate and X509 PEM (.crt) highlighted in red.](../_images/jao1638474529759.jpg)

13. On the **Attribute Mapping** page, update the **Outgoing Value** to **Email Address** for the **saml\_subject** application attribute.

    |   |                                   |
    | - | --------------------------------- |
    |   | No other attributes are required. |

14. Click **Save and Close** to finalize the creation of the application.

    ![Screen capture of SAML Attribute mapping section with Email Address and Save and Close highlighted in red.](_images/xbj1638474566030.jpg)

15. After you create the application, click the toggle next to the application to enable it.

    ![Screen capture of Heap application added to with the toggle bar highlighted in red.](_images/vfz1638474659283.jpg)

16. Select **Configuration** and copy the following values. You'll need these later.

    * **Single Logout Service**

    * **Single SignOn Service**

    ![Screen capture of application with the slider next to Heap highlighted in red.](_images/ujs1637011171895.jpg)

17. In your Heap account, go to the **Your SAML Identity Provider certificate** section and paste in the Ping X509 certificate that you downloaded previously.

    |   |                                                                                                        |
    | - | ------------------------------------------------------------------------------------------------------ |
    |   | You must include the `BEGIN CERTIFICATE` and `END CERTIFICATE` text as part of the certificate upload. |

    ![Screen capture of application with Heap selected and Configuration, Single Logout Service, and Single Signon Service fields highlighted in red.](_images/myz1637011243290.jpg)

18. Paste the URLs that you copied previously into the corresponding fields:

    * **Single SignOn Service**= **Remote login URL**

    * **Single Logout Service**= **Logout landing URL** (optional)

19. Click **Save Configuration**.

    ![Screen capture of Heap SAML Identity Provider details highlighted in red, as well as Save Configuration.](_images/cmp1636482442616.jpg)

    After saving the configuration, a **Test Configuration** button appears.

20. Click **Test Configuration**.

    You're signed out and then prompted to sign on with your username and password.

    ![Screen capture of Heap SSO section with Test Configuration highlighted in red.](_images/umo1636489689692.jpg)

21. After signing on to your Heap account, go to the **Single Sign-On** settings section and select **Enable Configuration** to finalize the SSO connection.

    ![Screen capture of Heap SSO section with Enable Configuration highlighted in red.](_images/cqh1636490534335.jpg)

## Create and assign identities

Before testing your integration, you must create and assign identities in PingOne. If you've already assigned identities and groups in PingOne, move on to [Test your integration](#test-integration).

1. In PingOne, go to **Identities → Groups** and click the + icon next to **Groups.**

   ![Screen capture of Groups page with the plus icon highlighted in red.](_images/kmq1638474774529.jpg)

2. On the **Create New Group** page, enter values for the following:

   * **Group Name** (Required)

   * **Description** (Optional)

   * **Population** (Optional)

3. Click **Finish & Save**.

   ![Screen capture of Groups fields for .](_images/mxc1638474810835.jpg)

4. To add identities to the group, on the **Identities** tab, go to **Users → + Add User**.

   ![Screen capture of Users page with + Add User highlighted in red.](../_images/aas1637008099896.jpg)

5. On the **Add User** page, enter in all the necessary information for a user.

   |   |                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------- |
   |   | Verify that the first name, last name, and email address are correct, as these are values passed in the SAML assertion. |

6. Click **Save**.

   ![Screen capture of Add User popup with the Save button highlighted in red.](../_images/kzl1638474889926.jpg)

7. Assign the user that you created to the group that you created previously. Locate the user you created and do the following:

   1. Expand the section for the user.

   2. Select the **Groups** tab.

   3. Click **[icon: plus, set=fa]Add**.

   ![Screen capture of expanded user profile with Groups and + Add highlighted in red.](../_images/agi1638473854046.jpg)

8. In the **Available Groups** section, select the group that you created and click the **[icon: plus, set=fa]**icon to add it to the user's group memberships. Click **Save**.

   ![Screen capture of Admin group with the plus icon highlighted in red.](../_images/cjm1638473992117.jpg)

9. On the **Connections** tab, for the Heap application:

   * Click the **Access** tab

   * Click the **Pencil** icon to edit the configuration

   ![Screen capture of applications with Heap Access and Pencil edit button highlighted in red.](_images/nra1638475028506.jpg)

10. Select the group that you created and add it to the **Applied Groups** section. Click **Save**.

    ![Screen capture of application list with Heap Apps listed and the plus icon highlighted in red.](_images/bzm1638475097331.jpg)

## Test your integration

1. In the PingOne admin console, go to **Dashboard → Environment Properties**.

2. Right-click on the **Application Portal URL** and open it in a private browser session.

   ![Screen capture of Properties Environment section with the Application Portal URL highlighted in red.](_images/ygn1636566242655.jpg)

3. Sign on as the test user that you created and click the Heap tile.

   You're signed on to the user's Heap account using SSO and testing is complete.

   ![Screen capture of dock with Heap added as an application.](_images/eyc1638475142523.jpg)

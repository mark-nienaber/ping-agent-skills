---
title: AD Connect final setup
description: Complete the setup or manual update of AD Connect, verify the AD Connect installation, and configure additional settings in PingOne for Enterprise.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_adc_final_setup
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_adc_final_setup.html
revdate: January 9, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# AD Connect final setup

Complete the setup or manual update of AD Connect, verify the AD Connect installation, and configure additional settings in PingOne for Enterprise.

## About this task

## Steps

1. On the PingOne for Enterprise admin portal page for AD Connect, click **Verify Installation**.

   |   |                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're using AD Connect in a clustered, high availability configuration, you will verify the installation in the PingOne for Enterprise admin portal only for the initial AD Connect installation. |

2. **Optional:** Choose whether to enable Integrated Windows Authentication (IWA).

   When enabled, IWA is applied when the user is on your organization's network. When the user comes from outside your network, NTLM is used. A user is prompted for their credentials only once per browser session.

   1. If you enable IWA, the **Intranet IP Ranges** entry box is displayed. Your entries here apply IWA to all users whose IP addresses are specified or contained within a block of IP addresses. The addresses need to be IPv4 addresses in dot-decimal format (123.123.123.123), or an IPv4 address block in CIDR format (123.123.123.0/24).

3. In **AD Connect Configuration**, the following settings are available:

   * **Authentication Account Lookup Method**

     Assigns the Active Directory attribute to use when looking up the account information for the user during delegated authentication. This can be:

     * **Mail**. The email address assigned to the user.

     * **sAMAccountName**. The legacy Windows logon name for the user.

     * **Filter**. An LDAP filter to use when looking up the account information for the user.

       Include `{0}` in your filter where you want the user's input to be substituted. For example, if you want to look up users by `sAMAccountName`, you would enter `sAMAccountName={0}`.

     * **userPrincipalName**. We recommend you use `userPrincipalName` if you select the **Enable Global Catalog** option.

   * **Subject Attribute**

     Choose the value to use for `SAML_SUBJECT`. The possible values are `sAMAccountName` or `userPrincipalName`.

     |   |                                                                                                                                                                                                             |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If your user population comes from multiple domains, choose `userPrincipalName` as the subject attribute to avoid the potential of different users in different domains signing in using the same username. |

   * **Enable Delegated Windows Authentication**

     Select to enable a URL automatically created by PingOne for Enterprise that is unique to your account. We use this URL to verify the credentials used for sign-on requests received when a Salesforce user attempts to sign on using either the Salesforce UI or API.

     To ensure security, PingOne for Enterprise also generates a random key that is associated with this URL. If the existing key is compromised, click **Renew** to generate a new random key for the URL.

   * **Enable Password Change**

     Select to enable users to change their corporate passwords through AD Connect. When enabled, a Change My Password option is displayed on the AD Connect sign on screen. Users selecting this option are prompted for their existing password and the new password to use. Their password is then changed in Active Directory.

   * **Enable Group Hierarchy**

     Select to enable support for group hierarchies in Active Directory. When enabled, Active Directory groups that are nested will inherit the SSO permissions of their parent group or groups. When disabled (the default), an Active Directory group uses only the SSO permissions that are assigned to it, with no inheritance.

   * **Enable Global Catalog**

     Select to use the Active Directory Global Catalog for user lookup. When enabled, we recommend you use `userPrincipalName` as the **Authentication Account Lookup Method**.

4. Assign the Active Directory-to-PingOne for Enterprise attribute mapping.

   This assignment maps Active Directory attributes to the default PingOne for Enterprise attributes. This attribute mapping is not used by applications that you add to PingOne for Enterprise. You will configure those attribute mappings for each application.

   1. For any of the attribute mappings, you can choose to configure an advanced mapping. Learn more in [Creating advanced attribute mappings](p14e_creating_advaced_attribute_mappings.html).

5. Click **Finish**.

   When you return to the **Setup > Identity Repository**, a summary of the settings for your identity bridge is displayed.

## Next steps

If you're using AD Connect in a clustered, high availability configuration, repeat these steps on each AD Connect host.

---

---
title: AD Connect for IIS final setup
description: You're completing the setup or manual update of AD Connect for IIS and are ready to verify the AD Connect for IIS installation and configure additional settings in PingOne for Enterprise.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_adc_iis_final_setup
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_adc_iis_final_setup.html
revdate: June 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# AD Connect for IIS final setup

## About this task

You're completing the setup or manual update of AD Connect for IIS and are ready to verify the AD Connect for IIS installation and configure additional settings in PingOne for Enterprise.

## Steps

1. On the PingOne for Enterprise admin portal page for AD Connect, click **Verify Installation**. PingOne for Enterprise checks the connection to the AD Connect identity bridge.

   |   |                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're using AD Connect in a clustered, high availability configuration, you will verify the installation in the PingOne admin portal only for the initial AD Connect installation. |

2. For Authentication, the setting for `Account Lookup Method` is displayed.

   This setting assigns the Active Directory user attribute to use when looking up the account information for the user during authentication. This can be:

   * **Mail**. The email address assigned to the user.

   * **sAMAccountName**. The legacy Windows logon name for the user.

   * **Filter**. An LDAP filter to use when looking up the account information for the user.

     Include `{0}` in your filter where you want the user's input to be substituted. For example, if you want to look up users by `sAMAccountName`, you would enter `sAMAccountName={0}`.

3. For Delegated Authentication, the setting for `Account Lookup Method` is displayed.

   This setting assigns the Active Directory user attribute to use when looking up the account information for the user during delegated authentication. This can be:

   * **Mail**. The email address assigned to the user.

   * **sAMAccountName**. The legacy Windows logon name for the user.

   * **Filter**. An LDAP filter to use when looking up the account information for the user.

     Include `{0}` in your filter where you want the user's input to be substituted. For example, if you want to look up users by `sAMAccountName`, you would enter `sAMAccountName={0}`.

4. In the Identity Provider SSO URL section, check that a valid URL to your IIS host is displayed, and that the connection string for the SSO URL is correct. If needed, change either of these URLs.

5. The settings for `Entity ID`, `Assertion Lifetime` and `Authentication Type` are displayed.

   |   |                                                                                                                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `Entity ID` setting for your deployment is also displayed. This uniquely identifies the identity bridge to PingOne. This identifier is used in the Issuer element of the SAML assertion sent to us by the identity bridge. Do not change this setting unless we advise you to do so. |

   1. Check that the `Assertion Lifetime` setting is acceptable. Generally, you needn't change the default setting.

      This setting indicates how long the SAML assertion remains valid (in minutes).

   2. For Authentication, check that the `Authentication Type` setting is acceptable.

      This setting assigns the type of authentication the AD Connect identity bridge is to use. This can be:

      * **Integrated**. Integrated Windows Authentication (IWA) is used when the user is on your organization's network. A user is prompted for their credentials only once during the same browser session.

      * **Forms**. A Web-based authentication form is used. A user is prompted for their credentials at every authentication point during the same browser session.

      * **Hybrid**. A combination of Integrated Windows Authentication (IWA) and Form-based authentication is used. IWA is limited to intranet users who fall within a certain IP block range (specified in the `Intranet IP Block` attribute. Form-based authentication is used in all other cases (intended for those users authenticating from outside your organization's intranet).

   If you're using Integrated or Hybrid types, see [Configure IWA for AD Connect with IIS](p14e_configure_iwa_adc_iis.html).

6. Click **Finish**.

   When you return to the **Setup > Identity Repository** page, a summary of the settings for your identity bridge is displayed. You can click the Edit icon to modify the settings.

## Next steps

When you've completed your configuration:

* If you've upgraded:

  * You need to set the proper verification certificate. While logged in as an Administrator, browse to `https://localhost/adconnect/config.aspx`.

    In the bottom left of this page you will find the digital signature portion. Select the certificate that you'd assigned for the previous AD Connect installation, or want to assign for this installation. You can also choose to use the self-signed certificate.

    |   |                                                                                                                                                                                                                                                                                                                                                    |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If an error displays after you've selected the verification certificate stating that the certificate does not have the proper permissions, see the PingOne Knowledge Base article [Manually updating the AD Connect signing certificate](https://support.pingidentity.com/s/article/PingOne-Manually-updating-the-AD-Connect-signing-certificate). |

  * If you upgraded from version 1.x, in the PingOne admin portal, you will see that the group short names have been converted to their full DN. If you have multiple domains or child domains, check your application group mappings to ensure all of the correct groups have been selected for your application.

* If you're using AD Connect with IIS in a clustered, high availability configuration, repeat these steps on each AD Connect host.

---

---
title: AD Connect in a DMZ
description: When installing AD Connect on a host in a DMZ, you will need to open the following ports between the DMZ and your internal network:
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_adc_dmz
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_adc_dmz.html
revdate: March 30, 2023
---

# AD Connect in a DMZ

When installing AD Connect on a host in a DMZ, you will need to open the following ports between the DMZ and your internal network:

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | TCP and UDP are shown together below. Depending on the firewall network device, you may need to add the TCP and UDP rules separately. |

* TCP/UDP 389, 636, 3268, 3269

  These are the Lightweight Directory Access Protocol (LDAP) ports. AD Connect uses LDAP to access the Active Directory DC (when in-network or Windows Authentication is used). Also used for mobile authentication.

* UDP 138

  NetBIOS name resolution.

* TCP/UDP 445

  SAM/LSA.

* UDP 123

  NTP W32 Time.

* TCP/UDP 135, 49152-65535

  RPC Endpoint Mapper.

* UDP 137

  NetBios datagram.

* TCP/UDP 88

  This port belongs exclusively to Kerberos. AD Connect uses this port for off-network access when executing a single sign-on (SSO) event outside of the corporate network.

* TCP/UDP 464

  This server port is also used by Kerberos (to set or change the password).

* TCP/UDP 53

  The DNS service runs on this port. It's used to convert between URLs and IP Addresses.

---

---
title: AD Connect security best practices
description: Keep your AD Connect configuration and data secure with the following tips and tools.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_adc_security_hardening_guide
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_adc_security_hardening_guide.html
revdate: March 30, 2023
section_ids:
  encrypt-configuration-files: Encrypt configuration files
  enable-iwa: Enable IWA
  use-userprincipalname-as-the-subject-attribute: Use userPrincipalName as the subject attribute
---

# AD Connect security best practices

Keep your AD Connect configuration and data secure with the following tips and tools.

## Encrypt configuration files

AD Connect stores configuration data in the following files:

* `AuthenticationAgent.exe.config`

* `Provisioner.exe.config`

* `Softwareupdater.exe.config`

|   |                                                              |
| - | ------------------------------------------------------------ |
|   | These files contain sensitive data, such as the product key. |

You can encrypt these files using the Windows `Aspnet_config.exe` utility.

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because of a limitation of `Aspnet_config.exe`, you must:1) Rename the configuration files to `web.config`.

2) Run `Aspnet_config.exe` to encrypt the files.

3) Rename the files back to their original filenames. |

For more information, see [Encrypting and Decrypting Configuration Sections](https://docs.microsoft.com/en-us/previous-versions/zhhddkxy\(v=vs.140\)?redirectedfrom=MSDN) in the Microsoft documentation.

|   |                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ping Identity does not test AD Connect with encrypted configuration files. Encrypting these files could cause unforeseen complications, and you do so at your own risk.If encrypted configuration files do cause trouble, you can reinstall AD Connect. |

## Enable IWA

If you enable Integrated Windows Authentication (IWA), users within your organization's network will be authenticated through IWA. This improves security by reducing the need for user credentials to be communicated over the internet.

However, IWA has other limitations to consider. For example, your users will be unable to sign off of PingOne for Enterprise because IWA will automatically sign them back on.

For more information, see [Using IWA with browser clients](p14e_adc_using_iwa_browser_clients.html).

## Use `userPrincipalName` as the subject attribute

AD Connect has two options for which attribute to use as the subject attribute. While `sAMAccountName` is unique only within an Active Directory (AD) domain, `userPrincipalName` is unique across all AD domains.

If your user population contains multiple AD domains, select `userPrincipalName` as the subject attribute to avoid the potential of different users in different domains signing in using the same username.

For more information, see [AD Connect final setup](p14e_adc_final_setup.html).

---

---
title: Add a Basic SSO (password vaulting) application
description: To use Basic SSO, you first need to enable it on the Setup > Dock > Configurations page. See Configuring the dock when using an identity bridge or (if you're using PingOne directory as your identity repository) Configure the dock when using PingOne for Enterprise Directory for more information.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_basic_sso_application
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_basic_sso_application.html
revdate: March 28, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Add a Basic SSO (password vaulting) application

## About this task

To use Basic SSO, you first need to enable it on the **Setup > Dock > Configurations** page. See [Configuring the dock when using an identity bridge](p14e_configuring_dock_when_using_identity_bridge.html) or (if you're using PingOne directory as your identity repository) [Configure the dock when using PingOne for Enterprise Directory](p14e_configure_dock_when_using_p14e_directory.html) for more information.

You'll need to install the PingOne browser extension to add Basic SSO applications. If you've not already installed the browser extension, you will be prompted to do so when adding the app.

Basic SSO (password vaulting) uses the PingOne for Enterprise browser extension to relay credentials to the target cloud application. User credentials are encrypted (128 bit AES) with a user-specified privacy key and are stored in PingOne for Enterprise. The privacy key is stored in the local file system and is never sent to PingOne for Enterprise. PingOne for Enterprise uses stored encrypted credentials for single sign-on (SSO) to your cloud applications. The browser extension can access the encrypted credentials only after a user is authenticated to the identity repository.

## Steps

1. Click the **Applications** tab. The My Applications page is displayed.

2. Click **Add Application** and select **New Basic SSO Application**.

3. If you've not installed the PingOne browser extension for the current browser, you're prompted to install it. When the browser extension is installed, click **Begin** to launch the wizard for adding new Basic SSO applications. The wizard will guide you through training the browser extension for password vaulting into the application.

   When you're finished, the new Basic SSO application is added to your My Applications list.

4. Make the new application available to your users.

   See [Authorize group access to applications](p14e_authorize_group_access_applications.html) for instructions.

---

---
title: Add a Poll subscription
description: For Poll subscriptions, the audit events of the selected type are accumulated and made available to a client pulling those events. Accumulated audit events are kept for seven days and then discarded.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_poll_subscription
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_poll_subscription.html
revdate: February 8, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Add a Poll subscription

## About this task

For Poll subscriptions, the audit events of the selected type are accumulated and made available to a client pulling those events. Accumulated audit events are kept for seven days and then discarded.

You can assign an Audit & Report Administrator to manage subscriptions for audit events. For more information, see [Assign administrative roles](p14e_assign_administrative_roles.html) or [Assign administrators](../pingone_sso_for_saas_apps/p14saas_assign_administrators.html).

## Steps

1. From the Dashboard, click **Reporting > Subscriptions > Add Subscription**.

2. Enter the **Name** to assign to the subscription.

3. Enter the **Type** of audit event that will be polled for this subscription.

   See [PingOne for Enterprise report types](p14e_report_types.html) for the available types.

4. Select **Poll** to create a Poll subscription.

5. Select a **Batch Size** to indicate the maximum number of audit events to get for each call when polling for new audit events.

   The Poll subscription will retrieve the accumulated audit events, up to this batch size.

   |   |                                                                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The number of audit events accumulated and returned by the subscription can also be less or more than the batch size specified. If the number of audit events exceeds the batch size, the remaining audit events are retrieved by your next call to retrieve the audit events for this subscription. |

6. Click **Done**.

You will find the new subscription listed on the Subscriptions page.

---

---
title: Add an app to a category
description: The PingOne dock can contain many apps. Categorizing them can organize the dock and ease search and navigation for your users.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_app_category
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_app_category.html
revdate: December 13, 2021
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Add an app to a category

## About this task

The PingOne dock can contain many apps. Categorizing them can organize the dock and ease search and navigation for your users.

When you add an app to the applications list, select the appropriate category from the list provided. If the app is available to a user in their dock, the category is listed in their navigation pane, and the app appears under the selected category, as well as in the **All Applications** category.

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | The PingOne dock navigation pane lists only the categories having at least one associated app. |

## Steps

1. Click **Applications > My Applications**.

2. Select an application from the list and click **Edit**.

3. Continue through the app wizard until you reach the page containing the **PingOne App Customization** section. Here you can select the logo, icon, name and description for the app.

4. In the **Category** dropdown menu, select the category that you want to apply to this app and click **Save & Publish**.

   ### Result:

   The app is added to the selected category. When a user with access to the app signs on to PingOne dock, the app appears on the dock in the category that you selected and in the **All Applications** category.

---

---
title: Add an application from the Application Catalog
description: The Application Catalog contains applications that service providers have made available through PingOne. You can configure these applications to make them available to your users.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_application_application_catalog
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_application_application_catalog.html
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Add an application from the Application Catalog

The Application Catalog contains applications that service providers have made available through PingOne. You can configure these applications to make them available to your users.

## About this task

For more detailed directions to configure the most popular catalog applications, see [PingOne for Enterprise Application Catalog](../pingone_for_enterprise_app_catalog/p14eapps_landing_page.html).

## Steps

1. Go to **Applications > Application Catalog**.

2. **Optional:** In the **Search** field, search for your application by typing the name, entity ID, or description of the application you want to add.

3. When you find the application you want, click the line of the application to expand the description.

4. Click **Setup** to begin. The SSO Instructions page for the application is displayed.

5. Follow the instructions to configure SSO for the application. Click **Continue to Next Step**.

6. Configure your connection to the application per the application instructions. Click **Continue to Next Step**.

7. To add a new attribute, click **Add New Attribute**.

   In most cases, the default attribute mappings are sufficient. These mappings assign your identity repository attributes to the attributes provided by the Service Provider for the application.

   For each application attribute, you can:

   1. Enter a value in the **Application Attribute** field

   2. Click the **Required** checkbox to designate an attribute or attributes as required by the application.

   3. In the **Identity Bridge Attribute or Literal Value** field, choose between:

      * Select an attribute from the drop down list.

      * Select **As Literal** and enter a literal value to assign.

        1. Click **Advanced** and enter Advanced Attribute Mapping mode.

           For more information, see [Creating advanced attribute mappings](p14e_creating_advaced_attribute_mappings.html)

        2. Select the **Provisioning** checkbox to make this a provisioning attribute rather than an SSO attribute.

           Custom provisioning attributes are currently only available for Aquera and Salesforce applications.

8. When you've finished modifying or adding any additional attributes, click **Continue to Next Step**.

9. **Optional:** Customize how the application appears in your dock.

   * Click **Select Image** to upload a new application icon image.

   * In the **Name** field, enter a new name for the application.

   * In the **Description** field, enter a new description for the application.

   * From the **Category** list, select the category to assign the application to.

   * Click **Continue to Next Step**.

10. Make the new application available to your users by assigning the groups authorized to use the application.

    All members of the selected group or groups will be able to use the application. When the application supports user provisioning, user provisioning to this application is also enabled for members of the assigned groups.

    For more information about group access, see [Authorize group access to applications](p14e_authorize_group_access_applications.html).

    1. For each group you want to grant access to the application, click **Add**.

    2. Click **Continue to Next Step**

       ### Result:

       The summary information for the application configuration is then displayed on a new page.

11. Review your configuration and click **Finish** to add the application to the PingOne Dock.

---

---
title: Add directory attributes
description: You need to be either a Global Administrator or Identity Repository Administrator to add an attribute to the directory. For more information about changing administrative roles, see Editing administrative roles, permissions, and notifications.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_p1d_attributes
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_p1d_attributes.html
revdate: March 30, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
---

# Add directory attributes

## About this task

You need to be either a Global Administrator or Identity Repository Administrator to add an attribute to the directory. For more information about changing administrative roles, see [Editing administrative roles, permissions, and notifications](p14e_editing_administrative_roles_permissions_notifications.html).

The predefined attributes for the directory are SCIM version 1.1 core schema attributes. For more information, see [System for Cross-Domain Identity Management: Protocol 1.1](http://www.simplecloud.info/specs/draft-scim-api-01.html).

## Steps

1. Go to **Setup > Directory > Attributes**.

The attributes that are currently applied to the directory are displayed.

1. Click **Add Attribute** to add more predefined attributes.

   ### Result:

   The listing of available attributes from the SCIM core schema is displayed.

2. Select the attribute to add and click **Add**.

   ### Result:

   The attribute is added to the listing.

3. Click **Save Attribute** when you're finished.

---

---
title: Add directory groups and entitlements
description: You need to be either either a Global Administrator, an Identity Repository Administrator or Group and Entitlement Manager to add directory groups.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_p1d_groups_entitlements
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_p1d_groups_entitlements.html
revdate: March 2, 2022
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Add directory groups and entitlements

## Before you begin

You need to be either either a Global Administrator, an Identity Repository Administrator or Group and Entitlement Manager to add directory groups.

## About this task

By default, all new users are automatically assigned to the group `Users`, which has no directory entitlements (users aren't able to view directory information).

You can add a new group to the PingOne for Enterprise Directory, give the group a meaningful name, and (optionally) assign a directory role to the group. A user's directory entitlements are inherited from the entitlements from their group memberships. A group's entitlements derive from the role assigned to the group.

By default all members of all groups have access to all of the applications you add. The applications available to a user are displayed in the PingOne dock. If you've added applications to PingOne, when you're finished adding directory groups, see [Authorize group access to applications](p14e_authorize_group_access_applications.html) to control a group's access to applications.

By default, all PingOne for Enterprise administrative users are assigned to a group called `Domain Administrators`. This group is read-only and can't be directly modified. Learn how to change your administrators' permissions in [Assign administrative roles](p14e_assign_administrative_roles.html).

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | Regular reviews of group access privileges and memberships helps prevent unauthorized access to critical applications and sensitive data. |

## Steps

1. Go to **Users > User Directory > Groups**.

2. Click **Add Group**. The New Group page is displayed.

3. Enter a name to use for the new group and select the directory role to assign to the group.

   A group can be assigned only one role.

   * User Reader

     Groups assigned this role are entitled only to view user and group directory information.

   * User Manager

     Groups assigned this role have User Reader entitlements plus the ability to invite and create directory users and modify user attributes, though not group memberships.

   * Group and Entitlement Manager

     Groups assigned this role have User Manager entitlements plus the ability to create directory groups, assign entitlements to groups and change group membership.

   ### Result:

   For all of the roles, the PingOne admin portal application is added to the PingOne dock for each group member. In this case (for all roles), the PingOne admin portal displays only the **Users** and **Groups** tabs.

4. Click **Save** when you're finished.

5. Repeat these steps for any additional groups to add to the directory.

6. If you've added applications to PingOne, see [Authorize group access to applications](p14e_authorize_group_access_applications.html) to control a group's access to applications.

---

---
title: Add directory users
description: Add new users to the PingOne for Enterprise Directory.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_p1d_users
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_p1d_users.html
revdate: December 27, 2022
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Add directory users

Add new users to the PingOne for Enterprise Directory.

## Before you begin

You need to be either a Global Administrator, Identity Repository Administrator, or have at least User Manager entitlements to add a directory user.

## About this task

When you add new users to the PingOne for Enterprise Directory, you can pre-fill some or all of the user attribute values, or you can allow the new user to enter all of the necessary information.

By default, all new users are automatically assigned to the group `Users`, which has no directory entitlements (users aren't able to view directory information).

By default, all PingOne for Enterprise administrative users are assigned to a group called `Domain Administrators`. This group is read-only and can't be directly modified. Learn how to change your administrators' permissions in [Assign administrative roles](p14e_assign_administrative_roles.html).

## Steps

1. Go to **Users > User Directory > Users**.

2. Do one of the following:

   ### Choose from:

   * To create the user using attribute values you assign:

     1. Click **Add Users** to display the list of methods to add a user, and select **Create New User**.

     2. In the **Password** section, enter the initial password to assign to the user.

        The user will be required to reset their password the first time they sign on.

     3. Enter the attribute values you want to assign to the user.

        The **Username**, and **Email** values are required. All new users are automatically assigned to the `Users` group, so specifying group membership isn't required, though we recommend it.

     4. Click **Save** when you're done.

     5. Send the user's single sign-on (SSO) credentials to them. The new user can then SSO to PingOne for Enterprise.

   * To invite the user, having them enter all of the necessary user attributes:

     1. Click **Add Users** to display the list of methods to add a user, and select **Invite New User**. You're prompted for the email address to use.

        Use this method when you need to contact the user via an alternate email address (one not associated with an application dependent on their single sign-on to PingOne for Enterprise).

     2. If the user currently has access to the email address assigned to their PingOne for Enterprise account, use **Email Address** to send the invitation. The new user is added to the directory and an email invitation is sent to the email address you've entered.

        Optionally, if the user currently doesn't have access to the email address assigned to their PingOne for Enterprise account, you can use **Alternate Email** to send the invitation.

3. If you've chosen to invite the user, note the user's Invited status on the **Users** page. This status will change to Enabled when the new user activates their PingOne for Enterprise account.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The user invitation has a lifetime of 24 hours. If the user hasn't responded within that time you will need to resend the invitation.If a user clicks on an expired invitation link, they're redirected to the PingOne for Enterprise sign-on page, which displays an error message to request a new invitation from the administrator.You can change the destination of the redirect by using the `redirectLink` attribute in the PingOne for Enterprise Directory API. For more information, see .pingidentity.com/pingone/enterprise/v1/api///\[User Registration Notifications]. |

   While the user status is Invited, you can choose to do any of the following (from the list next to the **Details** button):

   * **Resend email** to resend an email invitation using the user's account email address.

   * **Resend email to alternate email address** to resend an email invitation to an email address for the user that's not used for the account email.

   * **Delete** to remove the user from the directory.

4. Repeat these steps for each new user to add to PingOne for Enterprise.

5. To add a user to an administrative role (including adding a user to the Domain Administrators group), see [Assign administrative roles](p14e_assign_administrative_roles.html).

---

---
title: Add or update an application using its SSO URL
description: If you have the SSO URL for an application that is not in the Application Catalog, you can connect to the application without using SAML. Typically, the application already exists in your organization, but it may be an application from a service provider (SP) if the SP supplies you the URL for the application.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_update_application_sso_url
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_update_application_sso_url.html
revdate: March 30, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Add or update an application using its SSO URL

## Before you begin

If you have the SSO URL for an application that is not in the Application Catalog, you can connect to the application without using SAML. Typically, the application already exists in your organization, but it may be an application from a service provider (SP) if the SP supplies you the URL for the application.

## About this task

You can then make the application available to your single sign-on (SSO) users.

|   |                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Applications you've made available using the SSO URL cannot be added to the authentication context in the PingOne authentication policy. However, if the SSO URL references an application configured for SSO in PingFederate, you can apply multi-factor authentication in PingFederate using a PingID advanced policy. |

## Steps

1. Go to **Applications > My Applications > SAML**.

2. Click **Add Application**.

3. On the Application Details page, enter the application details. **Application Name**, **Application Description** and **Category**are required fields. You can optionally assign an application icon. The icon file can be up to 5 Mb in size. The supported graphics formats are JPEG/JPG and PNG.

4. Click **Continue to Next Step**. The Application Configuration page is displayed.

5. On the Application Configuration page, click **I have the SSO URL** and enter the URL to use for SSO to the application.

   If the application is being supplied by an SP, the SP will need to supply the URL to you. We encode this URL, so do not encode it yourself (for example, by using `&amp;` rather than `&`).

   If you are using Google as your identity bridge and adding a Google application, enter the URL for the application using this format:

   ```
      https://<application>.google.com/a/<GoogleAppsDomainName>
   ```

   Where *application* is the name of one of the Google applications, and *GoogleAppsDomainName* is the domain name assigned to your Google account.

6. Confirm that the SSO URL is correct. You can use the Single Sign-On link to test the URL. The application connection is established, and available on your PingOne dock.

7. Click **Finish** to complete the application setup.

   The new application is added to your My Applications list for SAML. You can edit the application configuration as needed by clicking the right arrow icon then clicking **Edit**. Refer to this documentation when changing configuration values.

8. Make the new application available to your users.

   See [Authorize group access to applications](p14e_authorize_group_access_applications.html) for instructions.

---

---
title: Add trusted sites using Firefox settings
description: Requirements
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_trusted_sites_firefox_settings
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_trusted_sites_firefox_settings.html
revdate: December 9, 2021
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Add trusted sites using Firefox settings

## Before you begin

Requirements

* Your AD Connect configuration in PingOne must have an `Authentication Type` value of either "Hybrid" or "Integrated".

## About this task

For seamless SSO with AD Connect, use these instructions to assign the Windows Server IIS host to the Mozilla Firefox client's list of trusted sites.

## Steps

1. In Firefox, enter "about:config"" in the URL address bar.

2. In the Search bar, enter "network.negotiate".

3. Double-click the entry **network.negotiate-auth.trusted-uris**, and enter the URL of the IIS host for AD Connect (for example, https\://www\.my-adconnect-host.com).

   |   |                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're using NLB, or another clustering solution, you will add the virtual cluster IP rather than an individual IIS host IP. |

4. Click **OK**. The URL for the IIS host is displayed as the value of `network.negotiate-auth.trusted-uris`.

## Result

The IIS host(s) for AD Connect should now be accessible from your Firefox clients.

---

---
title: Add trusted sites using Group Policy
description: Requirements
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_trusted_sites_google_policy
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_trusted_sites_google_policy.html
revdate: December 9, 2021
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result
---

# Add trusted sites using Group Policy

## Before you begin

Requirements

* Administrative permissions on the AD Connect domain controller (DC) for the Windows Server IIS host (or cluster of IIS hosts) for AD Connect.

## About this task

For seamless SSO with AD Connect, use these instructions when you want to assign the IIS host to the Internet Explorer (IE) client's list of trusted sites, and you are using a Group Policy for IE to do this.

You will need to create a new Group Policy Object (GPO) on the DC and assign the trusted site for AD Connect to Internet Explorer clients.

|   |                                                          |
| - | -------------------------------------------------------- |
|   | These Group Policy settings should also work for Chrome. |

## Steps

1. From the DC, open Group Policy Management (in Administrative Tools).

2. Right-click the domain, select **Create a GPO in this domain, and Link it here**, and enter a name for the GPO you will use for the IE trusted sites policy.

3. Right-click on your new GPO and select **Edit**. The Computer Configuration and User Configuration nodes are displayed in the left pane.

4. Expand the User Configuration node to Preferences + Windows Settings.

5. Right-click **Registry** and select **New**, **Registry Item**.

6. From the Action dropdown list, select **Update**.

7. From the Hive dropdown list, select **HKEY\_CURRENT\_USER**, then click to browse for the Key Path value.

8. Expand the HKEY\_CURRENT\_USER node to **Preferences > Software > Microsoft > Windows > CurrentVersion > Internet Settings > ZoneMap**. Click **Domains > Select**.

9. In the Key Path field, go to the end of the entry and enter the domain in which the IIS host for AD Connect resides (for example, mydomain.com), and the IIS host name (for example, adConnect):

   ### Example:

   Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\mydomain.com\adConnect

   |   |                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you're using NLB, or another clustering solution, you will specify the virtual cluster IP rather than an individual IIS host name here. |

10. In the Value name field, enter the protocol. We recommend "https".

11. From the `Value type` dropdown list, select **REG\_DWORD**, and for `Value` data enter "1" as the number (1 - 4) indicating the security zone to assign to the URL.

    The security zone assignments are as follows:

    * 1 - Intranet

    * 2 - Trusted Sites

    * 3 - Internet

    * 4 - Restricted

12. Click **Apply > OK** and close Group Policy Management.

13. From the command line interface, run the command: `gpupdate /force`.

14. When the command finishes, close IE (if it is open) and run the `gpupdate /force` command again, this time from the Local Admin account.

15. Open IE and go to **Tools > Internet Options > Security > Local Intranet > Sites**. You should see the URL for the IIS host for AD Connect in the list of trusted sites.

## Result

This method of adding trusted sites using Group Policy applies to every IE client user in the domain, and doesn't conflict with any URLs added by the user. You can constrain this policy by applying the GPO to a specific OU within the domain, or changing the Security Group to which the GPO should apply (in the GPO's **Scope > Security Filtering** settings).

---

---
title: Add trusted sites using Internet Explorer settings
description: "Your AD Connect configuration in PingOne must have an Authentication Type value of either \"Hybrid\" or \"Integrated\". These authentication types use Integrated Windows Authentication (IWA)."
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_trusted_sites_ie_settings
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_trusted_sites_ie_settings.html
revdate: December 9, 2021
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Add trusted sites using Internet Explorer settings

## Before you begin

* Your AD Connect configuration in PingOne must have an `Authentication Type` value of either "Hybrid" or "Integrated". These authentication types use Integrated Windows Authentication (IWA).

## About this task

For seamless SSO with AD Connect, use these instructions when you want to assign the IIS host to the Internet Explorer(IE) client's list of trusted sites, and you will not be using a Group Policy for IE to do this.

## Steps

1. On the IE menu, select **Tools > Internet Options > Security > Local Intranet > Sites**.

2. Click **Advanced** and enter the full URL of the Windows Server IIS host for AD Connect (for example, https\://www\.my-adconnect-host.com). Click **Add** to add the host as a trusted site.

   |   |                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're using NLB, or another clustering solution, you will add the virtual cluster IP rather than an individual IIS host IP. |

3. Close this dialog box when you're finished and click **OK** to close the remaining open dialog boxes.

## Result

The IIS host(s) for AD Connect should now be accessible from your IE clients.

---

---
title: Adding a logo and banner message
description: "The logo you assign can be used for display on users' login and SSO pages as well as in the PingOne for Enterprise dock."
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_adding_logo_banner_message
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_adding_logo_banner_message.html
revdate: March 23, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding a logo and banner message

## About this task

The logo you assign can be used for display on users' login and SSO pages as well as in the PingOne for Enterprise dock.

## Steps

1. Go to **Account > Branding**.

2. In the **Corporate Logo** section, click the **Add** icon and browse for the logo that you want to assign.

   The standard maximum display dimensions on the PingOne for Enterprise dock are 72px high by 350px wide. The image dimension ratio is preserved. For the logo to render optimally on high-definition displays (such as Apple Retina displays), double the dimensions to 144px high by 700px wide.

3. To create a banner message, enter you message text into the **Banner Message** field.

   The banner is displayed at the top of the admin portal and is only visible to your administrative users.

4. Click **Save**.

---

---
title: Adding a Push subscription
description: Push subscriptions stream audit events of the selected type to the HTTPS URL you specify.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_push_subscription
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_push_subscription.html
revdate: September 8, 2023
section_ids:
  steps: Steps
  result: Result:
  result-2: Result
---

# Adding a Push subscription

Push subscriptions stream audit events of the selected type to the HTTPS URL you specify.

## Steps

1. Go to **Dashboard > Reporting > Subscriptions > Add Subscription**.

2. In the **Name** field, enter a name for this subscription.

3. In the **Type** list, select the type of audit event that will be pushed for this subscription.

   For more information, see [PingOne for Enterprise report types](p14e_report_types.html).

4. Select **Push** to create a Push subscription.

5. In the **Format** list, select the format for the audit events.

   For Push subscriptions, this can be either:

   * `Audit` (the PingOne for Enterprise default format).

   * `Splunk` (a format compatible with Splunk processing).

   Both formats are JSON.

6. In the **URL** field, enter the URL to stream audit events to.

   |   |                        |
   | - | ---------------------- |
   |   | The URL must be HTTPS. |

7. In the **Authorization Header** field, enter a request header that will be posted to the **URL** you specified.

   For example, `"Authorization: Basic 80F4FC1D78C0F15627C9B95C"`.

8. Click **Upload** to upload the public certificate registered to the **URL** you specified.

   |   |                                                                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For Splunk subscriptions, you need to upload the endpoint certificate, not the entire certificate chain. You can get your endpoint certificate by going to your Splunk endpoint in a browser and downloading it. |

9. Click **Done**.

   ### Result:

   You will find the new subscription listed on the **Subscriptions** page.

## Result

The audit events pushed to the URL you specified will look similar to these samples:

`Audit` format

```json
{
  "source": "ADMINISTRATOR_LOGIN",
  "id": "8fd3d92f-7af2-11e8-b80d-0ec0fbebxxxx",
  "recorded": "2018-28-06T16:44:44.849Z",
  "action": {
    "type": "Password"
  },
  "actors": [
    {
      "type": "user",
      "name": "pcasso@pingidentity.com"
    }
  ],
  "resources": [],
  "client": {
    "id": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "ipAddress": "192.168.10.1, 172.138.206.50"
  },
  "result": {
    "status": "SUCCESS",
    "message": "Password"
  }
}
```

`Splunk` format

```json
{
  "event": {
    "source": "ADMINISTRATOR_LOGIN",
    "id": "44990ce5-7af4-11e8-b80d-0ec0fbebxxxx",
    "recorded": "2018-28-06T16:56:57.627Z",
    "action": {
      "type": "Password"
    },
    "actors": [
      {
        "type": "user",
        "name": "pcasso@pingidentity.com"
      }
    ],
    "resources": [],
    "client": {
      "id": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
      "ipAddress": "24.222.35.218, 172.18.26.54"
    },
    "result": {
      "status": "SUCCESS",
      "message": "Password"
    }
  },
  "host": "pingidentity.com",
  "time": 1530205017627,
  "source": "ADMINISTRATOR_LOGIN"
}
```

---

---
title: Adding or updating a SAML application
description: If you don't have the service provider's (SP) single sign-on (SSO) URL for the application (generally a SAML application that already exists in your organization), you will need to configure the necessary SAML settings to add the application.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_update_saml_application
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_update_saml_application.html
revdate: September 22, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  result: Result:
  result-2: Result
---

# Adding or updating a SAML application

If you don't have the service provider's (SP) single sign-on (SSO) URL for the application (generally a SAML application that already exists in your organization), you will need to configure the necessary SAML settings to add the application.

## About this task

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are using the Google identity bridge, you cannot add Google applications using this method. See [Add or update an application using its SSO URL](p14e_add_update_application_sso_url.html) to add these applications. |

## Steps

1. Go to **Applications > My Applications > SAML**.

2. Click **Add Application > New SAML Application**.

3. On the **Application Details** tab, enter the application details. **Application Name**, **Application Description** and **Category** are required fields.

   You can optionally assign an application icon. The icon file can be up to 5 Mb in size. The supported graphics formats are JPEG/JPG and PNG.

4. Click **Continue to Next Step**.

5. On the **Application Configuration** page, provide the SAML configuration details for the application.

   1. **Signing Certificate**. In the list, select the signing certificate you want to use.

   2. **SAML Metadata**. Click **Download** to retrieve the SAML metadata for PingOne for Enterprise. This supplies the PingOne for Enterprise connection information to the application.

   3. **Protocol Version**. Select the SAML protocol version appropriate for your application.

   4. **Upload Metadata**. Click **Select File** to upload the application's metadata file, or click **Or use URL** to enter the URL of the metadata file. The **ACS URL** and **Entity ID** will then be supplied for you. If you don't upload the application metadata, you'll need to enter this information manually with values provided by the application.

      |   |                                                                                                                                                                          |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | The application's **Entity ID** must be unique within your account. You can't configure more than one application in PingOne for Enterprise using the same SP entity ID. |

   5. **Application URL**. This is required by some applications as the target URL. It's used in identity provider (IdP)-initiated SSO for a deep-linking purpose. The application URL is passed in the `RelayState` parameter by the IdP.

   6. **Single Logout Endpoint**. The URL to which our service will send the SAML Single Logout (SLO) request using the **Single Logout Binding Type** that you select).

   7. **Single Logout Response Endpoint**. The URL to which your service will send the SLO Response.

   8. **Single Logout Binding Type**. Select the binding type (**Redirect** or **POST**) to use for SLO.

   9. **Primary Verification Certificate**. Click **Choose File** to upload the primary public verification certificate to use for verifying the SP signatures on SLO requests and responses.

   10. **Secondary Verification Certificate**. Click **Choose File** and upload the secondary verification certificate if available. The secondary verification certificate is used if the primary verification certificate fails to validate a signature.

   11. **Optional:** **Encrypt Assertion**. If selected, the assertions PingOne sends to the SP for a multiplexed application will be encrypted. You can also use this option for your managed applications. Available for SAML 2.0 applications only.

       |   |                                                                                                                                                                                                                                                               |
       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | If an encryption certificate is included in the metadata you upload, this option is automatically enabled. The entry for **Encryption Certificate** will show the name of the certificate and the entry for **Encryption Algorithm** will be set to AES\_256. |

       Selecting this option displays the information needed to encrypt the assertion:

       * Encryption Certificate

         Upload the certificate to use to encrypt the assertions.

       * Encryption Algorithm

         Choose the algorithm to use for encrypting the assertions. We recommend **AES\_256** (the default), but you can select **AES\_128** instead.

       * Transport Algorithm

         The algorithm used for securely transporting the encryption key. Currently, **RSA-OAEP** is the only transport algorithm supported.

   12. **Signing**. Select either to sign the SAML assertion or to sign the SAML response.

       When you have selected **Encrypt Assertion**, we highly recommend that you choose to sign the response. This provides a significant increase in security.

   13. **Signing Algorithm**. Select an algorithm from the list.

   We strongly recommend using the default **RSA\_SHA256** algorithm or higher.

   1. **Force Re-authentication**. If selected, users having a current, active SSO session will be re-authenticated by the identity bridge to establish a connection to this application.

   2. **Force MFA**. If selected, users are required to use multi-factor authentication (MFA), as defined by the applied application policy, each time they access the application.

      You'll need to have an authentication policy in place to use this setting. See [Create or update an authentication policy](p14e_create_update_authentication_policy.html) for more information.

   3. **Use Custom URL**. Select and enter a custom URL in the text box to customize the URL to launch the application from the dock. This can be an SSO URL assigned by the SP or IdP. The default URL is generated by PingOne for Enterprise.

      The remaining entries are optional, depending on your requirements. Click **Continue to Next Step**. The SSO Attribute Mapping page is displayed.

6. Modify or add any attribute mappings as necessary for the application.

   In most cases, the default attribute mappings are sufficient. These mappings assign your identity repository attributes to the attributes provided by the SP for the application.

   |   |                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're adding SAML subject as an attribute, make sure to use the value `SAML_SUBJECT` for the **Application Attribute** field. If not defined, `SAML_SUBJECT` will be mapped to the subject sent by the IdP. |

   For each application attribute, you can:

   ### Choose from:

   * Click the **Required** checkbox to designate an attribute or attributes as required by the application.

   * Click in an entry box and select an identity repository attribute from a drop-down list.

   * Click in an entry box and enter an identity repository attribute.

   * Click the **As Literal** checkbox and in the entry box, enter a literal value to assign.

   * Click **Advanced** and enter Advanced Attribute Mapping mode. See [Creating advanced attribute mappings](p14e_creating_advaced_attribute_mappings.html) for instructions.

   * Click **Add new attribute** to enter any additional attributes required by the application. You can then enter custom text in the **Application Attribute** text box, in addition to all of the choices above when configuring the new attribute.

7. When you have finished modifying or adding any additional attributes, click **Continue to Next Step**.

   The **Add Groups** page is displayed.

8. Make the new application available to your users by assigning the groups authorized to use the application.

   All members of the selected group or groups will be able to use the application. When the application supports user provisioning, user provisioning to this application is also enabled for members of the assigned groups.

   1. Click **Add** for each group you want to authorize to use the application.

   2. Click **Continue to Next Step**

      ### Result:

      The summary information for the application configuration is then displayed on a new page.

9. Review the application connection information.

   Some of this information might be needed by the SP to complete the SSO configuration for the application. In particular, you can download the PingOne for Enterprise signing certificate or the PingOne for Enterprise **SAML metadata**, which has the certificate embedded. You can also copy the **SAML Metadata URL** and use it to keep your IdP configuration updated with PingOne for Enterprise metadata.

   The SSO URL for the application is displayed as the value of **Initiate Single Sign-On (SSO) URL**. You can use this to test SSO directly to the application without going through the PingOne for Enterprise dock.

10. Click **Edit** to change any of the configuration settings, or **Finish** to complete the application setup.

## Result

The new SAML application is added to your My Applications list.

You can go to **Users > User Groups** to see that the application you have added is now authorized for use by the selected group or groups.

---

---
title: Adding or updating an OIDC application
description: Create a new OpenID Connect (OIDC) application or modify an existing application in PingOne for Enterprise.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_add_update_oidc_application
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_update_oidc_application.html
revdate: June 5, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  result: Result
  next-steps: Next steps
---

# Adding or updating an OIDC application

Create a new OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* application or modify an existing application in PingOne for Enterprise.

## Before you begin

Before you add an OIDC application, you must configure the access token that your account will use for OIDC applications. These account-level settings are inherited at the application level when you add or update an application.

|   |                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Account-level OAuth settings apply only to your managed applications, not to applications supplied by a service provider (SP) *(tooltip: \<div class="paragraph">&#xA;\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>&#xA;\</div>)*. |

PingOne for Enterprise returns OIDC user attributes in different ways depending on the `response_type` parameter.

The contents of the ID token depend on whether or not the application also returns an access token:

* For flows that return both an access token and an ID token (such as authorization code flow, or implicit flows where the `response_type` includes `token`) the ID token contains the `sub` and, if requested, `email` scopes. The `userinfo` endpoint contains all of the attributes for the requested scopes and attributes configured on the **User Info** tab for the application, if the `openid` scope was requested.

* For flows that don't return an access token, the ID token contains all of the attributes for the requested scopes and any attributes configured on the **User Info** tab for the application, if the `openid` scope was requested. The `userinfo` endpoint is inaccessible in this case because no access token is issued.

The access token contains attributes configured at **Applications > OAuth Settings > Access Token**.

For more information, see [Configuring your OAuth settings](p14e_configure_oauth_settings.html).

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When you add an OIDC application, you must have access to the necessary configuration information for the application. For applications supplied by an SP, the SP will direct you to this information. |

## Steps

1. Go to **Applications > My Applications > OIDC**.

2. Add a new application or edit an existing application.

   ### Choose from:

   * To create a new application, click **Add Application**. See Step 3 for new application types.

   * To update an existing application, expand the application and click the **Pencil** icon. Skip to step 4.

3. Select the type of application that you want to add and click **Next**:

   ### Choose from:

   * To create an application that is accessed and used within a browser, click**Web App**.

   * To create an application that is stored locally and run on a desktop or device, click **Native App**.

   * To create an API-driven front-end application, such as applications using Node.js or Angular, click **Single Page App**.

   * If you want full control of all available configuration parameters, click **Advanced Configuration**.

4. In the **Application Name** field, enter an application name.

5. In the **Short Description** field, enter an application description.

6. In the **Category** list, select a category to assign the application to.

7. **Optional:** To add an icon for the application, click the **Image** icon and upload an icon image.

   The icon file can be up to 1 Mb in size. The supported graphics formats are JPEG/JPG, PNG and GIF.

8. Click **Next**.

9. **Optional:** To enable or disable a custom valid duration for the application access token, click the **Override Access Token Lifetime** toggle.

10. **Optional:** If you enabled the override, enter the number of minutes access token lifetime in the **Minutes** field.

    The valid range is 1 - 60 minutes. The default value is inherited from your account-level OAuth settings. For more information, see [Configuring your OAuth settings](p14e_configure_oauth_settings.html).

11. Select the allowed grant types for the application.

    Available grant types are determined by the application type. For more information, see [OIDC application grant types](p14e_oidc_app_grant_types.html).

12. **Optional:** If you selected **Refresh Token**, configure the token settings:

    1. Click the **Override Refresh Idle Lifetime** toggle to override the global OAuth setting for the application.

    2. In the **Refresh Token Idle Lifetime** field, enter the number of minutes that a refresh token can be idle before being used again.

    3. Click the **Override Refresh Token Max Lifetime** toggle to override the global OAuth setting for this application.

    4. In the **Refresh Token Max Lifetime** field, enter the maximum number of minutes that a refresh token can be valid.

13. **Optional:** For Web Apps and Advanced Configuration applications, click **Add Secret** to add a secret to pair with the application **Client ID**.

    If you want to change a client secret, you must generate a second secret before deleting the first.

    |   |                                                                                                                                                                                                                                           |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | For greater security with Web App applications, you can use PKCE in your authorization and token request. In this case, a client secret is not used. For more information, see [OAuth 2.0 RFC 7636](https://tools.ietf.org/html/rfc7636). |

14. Copy the **Discovery URL**, **Issuer**, and **IDPID** values to use later in integrating the application with PingOne for Enterprise.

    This information also displays on the summary page for the application after you've added the application to PingOne for Enterprise.

    For more information, see [Integrating an OIDC application](p14e_integrate_oidc_application.html).

15. Click **Next**.

16. In the **Start SSO URL** field, enter the URL to use for SSO to the application.

    This is the URL to which application users will redirect to initiate SSO to PingOne for Enterprise using OIDC.

17. In the **Redirect URIs** field, enter URIs forPingOne for Enterprise to send responses to for the application's authorization requests.

    |   |                                                     |
    | - | --------------------------------------------------- |
    |   | Click **Add URL** to define multiple redirect URIs. |

18. **Optional:** In the **Logout URI** field, enter the URI to which PingOne for Enterprise sends a user for single logout (SLO).

19. **Optional:** Select the authentication requirements.

    | Authentication Method                 | Description                                                                                                                                                                                                                                                                                                                                             |
    | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Force authentication**              | If selected, to establish a connection to this application, users having a current, active SSO session will be re-authenticated by the identity repository.                                                                                                                                                                                             |
    | **Force multi-factor authentication** | If selected, users are required to use multi-factor authentication (MFA) as defined by your authentication policy each time they access the application.You'll need to have an authentication policy in place to use this setting. See [Create or update an authentication policy](p14e_create_update_authentication_policy.html) for more information. |

20. Click **Next**.

21. To add attributes to the **Default User Profile Attribute Contract**, click **Add Attribute** and enter an attribute in the **Attribute Name** field.

    Select the **Required** checkbox to make the attribute required.

    The default user profile attribute contract is the user profile returned by the `userinfo` endpoint for this application when the `openid` scope is included in the authentication request.

    The (subject) `sub` attribute is required for all UserInfo requests.

    PingOne for Enterprise uses the `idpid` attribute to identify the identity provider (IdP) and is included in the attribute contract by default.

    If the application you're adding is a managed application, you can remove the `idpid` attribute from the contract. For managed applications,PingOne for Enterprise already has the `idpid` value for your account.

22. Click **Next**.

23. Click the \[.uicontrol]\*[icon: plus, set=fa]\*icon to add scopes to the allowed list, or click the **-** icon to remove them.

    These OAuth user scopes are the user resources to which the application will request access. The `openid` scope is expected to always be included in the authorization request.

24. Click **Next**.

1) Map identity repository attributes to claims made by the application.

   For each IdP attribute, enter or select the target attribute from the list.

   Click **Advanced** to display the advanced attribute mapping mode. For more information, see [Assign advanced attribute mappings](p14e_assign_advanced_attribute_mappings.html).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This is a mapping of your identity repository attributes to the OIDC scope claims available to the application. By default, the attribute mapping inherits the account-level attribute mapping that you specify when you [configure your OAuth settings](p14e_configure_oauth_settings.html).You can override the account-level attribute mappings for the application. If you update the attribute mappings, the inherited account-level mappings remain available as selections in the list.The OIDC claims listed here include all claims from the access token attribute contract, the `UserInfo` attribute contract for this application, and the claims for any scopes to which this application is permitted.The attributes listed are determined by the scopes that you added previously. The `sub` attribute is required for all applications. |

1. Click **Next**.

2. Make the new application available to your users by assigning the groups authorized to use the application.

   Click the **[icon: plus, set=fa]**icon for each group that you want to authorize.

   |   |                                                             |
   | - | ----------------------------------------------------------- |
   |   | All members of the selected groups can use the application. |

3. Click **Done**.

## Result

The new OIDC application is added to your **My Applications** list for OIDC. You can edit the application configuration by clicking the **Edit** icon.

## Next steps

[Integrate your OIDC application](p14e_integrate_oidc_application.html) with PingOne for Enterprise.

---

---
title: Adding trusted sites for Firefox
description: In Firefox, enter about:config in the URL address bar.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_adc_adding_trusted_sites_firefox
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_adc_adding_trusted_sites_firefox.html
revdate: November 22, 2023
section_ids:
  steps: Steps
  result: Result
---

# Adding trusted sites for Firefox

## Steps

1. In Firefox, enter `about:config` in the URL address bar.

2. Click **Accept the Risk and Continue**.

3. In the **Search** bar, enter `network.negotiate`.

4. Click the **Pencil** icon for **network.negotiate-auth.trusted-uris**.

5. In the field that opens, enter the host name of the AD Connect host.

6. Click the **Save** icon.

## Result

The name of the AD Connect host is displayed as the value of **network.negotiate-auth.trusted-uris**.
---
title: Additional logging
description: "The following logging options can be updated in log4j2.xml after the section AsyncLogger name=\"com.pingidentity.provisioner\". This will provide additional logging details in the provisioner.log for troubleshooting purposes."
component: box
page_id: box:troubleshooting:pf_box_connector_additional_logging
canonical_url: https://docs.pingidentity.com/integrations/box/troubleshooting/pf_box_connector_additional_logging.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Additional logging

The following logging options can be updated in `log4j2.xml` after the section `AsyncLogger name="com.pingidentity.provisioner"`. This will provide additional logging details in the `provisioner.log` for troubleshooting purposes.

Learn more about log4j2 in [Log4j 2 logging service and configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_log4j_2_loggin_service_and_config.html). You can also learn more from Ping Identity [Support & Community](https://support.pingidentity.com/s/).

```
<AsyncLogger name="com.pingidentity.integrations"
                     level="INFO" additivity="false" includeLocation="false">
            <appender-ref ref="ProvisionerLog" />
            <!--
                <appender-ref ref="CONSOLE-PROVISIONER" />
                <appender-ref ref="ProvisionerLogToOracleDB-FAILOVER"/>
                <appender-ref ref="ProvisionerLogToSQLServerDB-FAILOVER"/>
                <appender-ref ref="ProvisionerLogToMySQLDB-FAILOVER"/>
            -->
        </AsyncLogger>

<AsyncLogger name="com.pingidentity.saas"
                     level="INFO" additivity="false" includeLocation="false">
            <appender-ref ref="ProvisionerLog" />
            <!--
                <appender-ref ref="CONSOLE-PROVISIONER" />
                <appender-ref ref="ProvisionerLogToOracleDB-FAILOVER"/>
                <appender-ref ref="ProvisionerLogToSQLServerDB-FAILOVER"/>
                <appender-ref ref="ProvisionerLogToMySQLDB-FAILOVER"/>
            -->
</AsyncLogger>
```

---

---
title: Box Provisioner
description: The Box Provisioner allows PingFederate to integrate with Box for provisioning and single sign-on (SSO).
component: box
page_id: box::pf_box_connector
canonical_url: https://docs.pingidentity.com/integrations/box/pf_box_connector.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Box Provisioner

The Box Provisioner allows PingFederate to integrate with Box for provisioning and single sign-on (SSO).

## Features

* Manages users in Box based on changes in an external data store that is attached to PingFederate.

  * Creates, updates, disables, and deletes users.

  * Allows you to enable the create, update, disable, and delete capabilities independently.

  * Allows you to provision disabled users.

  * Allows you to choose whether to disable or delete users when deprovisioning.

* Manages groups in Box based on changes in an external data store that is attached to PingFederate.

  * Creates and deletes groups.

  * Updates group memberships.

* Enables browser-based SSO initiated by the service provider (SP) or identity provider (IdP).

* Pre-populates some connection settings with the included quick connection template.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following sections of the PingFederate documentation:

* [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

* [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

* [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

* [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

* [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

## System requirements

* PingFederate 7.3 or later.

* A Box administrator account.

* To allow PingFederate to make outbound connections to the Box API, you might need to allow the following domain in your firewall:

  * https\://account.box.com

  * https\://api.box.com

---

---
title: Changelog
description: Added option to create personal folders on user creates
component: box
page_id: box:release_notes:pf_box_connector_change_list_by_version
canonical_url: https://docs.pingidentity.com/integrations/box/release_notes/pf_box_connector_change_list_by_version.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  box-provisioner-2-5-april-2018-current-release: Box Provisioner 2.5 – April 2018 (current release)
  box-provisioner-2-4-1-october-2017: Box Provisioner 2.4.1 – October 2017
  box-provisioner-2-4-july-2017: Box Provisioner 2.4 – July 2017
  box-provisioner-2-3-july-2017: Box Provisioner 2.3 – July 2017
  box-provisioner-2-2-2-march-2017: Box Provisioner 2.2.2 – March 2017
  box-provisioner-2-2-1-january-2017: Box Provisioner 2.2.1 – January 2017
  box-provisioner-2-2-november-2016: Box Provisioner 2.2 – November 2016
  box-provisioner-2-1-may-2016: Box Provisioner 2.1 – May 2016
  box-provisioner-2-0-march-2016: Box Provisioner 2.0 – March 2016
  box-provisioner-1-0-june-2014: Box Provisioner 1.0 – June 2014
---

# Changelog

## Box Provisioner 2.5 – April 2018 (current release)

* Added option to create personal folders on user creates

* Added option to force delete users with managed content

## Box Provisioner 2.4.1 – October 2017

* Resolved issue when saving new tokens to the database (token renewal workflow)

* Improved logging for token renewal workflow

## Box Provisioner 2.4 – July 2017

* Added option to provision groups with common name or distinguished name

## Box Provisioner 2.3 – July 2017

* Added option to store Box credentials in a flatfile or in a database

  * Flatfile credential storage is limited to a single instance of PingFederate

  * Database credential storage has the ability to support multiple PingFederate instances (for example, failover use case)

* Added support for disabling or deleting users without updating any user attributes

* Added configuration control of provisioning disabled users

## Box Provisioner 2.2.2 – March 2017

* Fixed synchronization on update of users, that were previously created with "User Create Enabled" set to false in configurable options

## Box Provisioner 2.2.1 – January 2017

* Fixed OAuth token issues

* Fixed the provisioner handling channels with multiple threads

* Improved handling of different letter case logins and aliases

## Box Provisioner 2.2 – November 2016

* Added support for updating user emails

## Box Provisioner 2.1 – May 2016

* Added support for transferring box content to an admin account during deprovisioning (hard delete only)

## Box Provisioner 2.0 – March 2016

* Added support for additional user attributes

* Added support for group provisioning

* Added support for adding users to groups

* Added configuration options for CRUD capabilities

## Box Provisioner 1.0 – June 2014

* Initial release

* Added support for user provisioning

---

---
title: Configure Box for SSO
description: To configure Box for single sign-on (SSO), you will require metadata from your PingFederate Identity Provider (IdP) setup. Learn more in Exporting connection-specific SAML metadata
component: box
page_id: box:setup:pf_box_connector_configure_box_for_sso
canonical_url: https://docs.pingidentity.com/integrations/box/setup/pf_box_connector_configure_box_for_sso.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure Box for SSO

## About this task

To configure Box for single sign-on (SSO), you will require metadata from your PingFederate Identity Provider (IdP) setup. Learn more in [Exporting connection-specific SAML metadata](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_exportmetadatatasklet_exportconnectionstate.html)

To export your IdP metadata:

1. Go to **Server Configuration > Metadata Export**.

2. On the **Metadata Mode** screen, choose **Use a Connection for Metadata Generation** and click **Next**.

3. On the **Connection Metadata** screen, select the Box connection created in [Configure PingFederate for SSO](pf_box_connector_configure_pf_for_sso.html).

4. On the **Metadata Signing** screen, click **Next**.

5. On the **Export & Summary** screen, click **Export** to retrieve your metadata `.xml` file.

To configure Box for SSO:

## Steps

1. Submit a ticket through the Box [SSO Setup Support Form](https://support.box.com/hc/en-us/requests/new?ticket_form_id=360002612594) and upload your PingFederate metadata.

2. Click **Submit**.

---

---
title: Configure PingFederate for SSO
description: The following section describes the steps for configuring single sign-on (SSO) to Box. Configuring SAML SSO involves configuring both the PingFederate SP connection and Box.
component: box
page_id: box:setup:pf_box_connector_configure_pf_for_sso
canonical_url: https://docs.pingidentity.com/integrations/box/setup/pf_box_connector_configure_pf_for_sso.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure PingFederate for SSO

## About this task

The following section describes the steps for configuring single sign-on (SSO) to Box. Configuring SAML SSO involves configuring both the PingFederate SP connection and Box.

|   |                                                        |
| - | ------------------------------------------------------ |
|   | Configuring SSO is optional for outbound provisioning. |

## Steps

1. Create a new SP connection or select an existing SP connection from the **SP Configuration** menu.

2. On the **Connection Template** screen, select the **Use a template for this connection** option and choose **Box Connector** in the **Connection Template** list. You will be asked to provide the `boxmetadata.xml` file you obtained earlier in [Download Box SAML 2.0 metadata file](pf_box_connector_download_box_saml_20_metadata_file.html).

   ![An image of the Connection Template screen.](_images/igc1563995181315.png)

3. On the **Connection Type** screen, ensure that the **Browser SSO Profiles** check box is selected.

4. On the **General Info** screen, the default values are taken from the metadata file you selected in step 2. We recommend using the metadata default values.

   ![An image of the General Info screen.](_images/vev1563995186742.png)

5. Click **Next** to continue the Browser SSO configuration. Learn more in the following sections under [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html):

   * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

   * [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html)

   * [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html)

6. On the authentication adapter's **Attribute Contract Fulfillment** screen, map SAML\_SUBJECT to email address.

7. On the **Protocol Settings > Allowable SAML Bindings** screen, ensure that both **POST** and **SOAP** are selected.

8. On the **Credentials** screen, click **Configure Credentials**.

9. On the **Back-Channel Authentication** screen, click **Configure**.

10. On the **Inbound Authentication Type** screen, select **Digital Signature (Browser SSO profile only)** and click **Done**.

11. On the **Credentials > Digital Signature Settings** screen, select the signing certificate.

12. On the **Signature Verification Settings** screen, click **Manage Signature Verification Settings**.

13. On the **Trust Model** screen, ensure **Unanchored** is selected and click **Next**.

14. On the **Signature Verification Certificate** screen, select the Box certificate as the primary certificate and click **Next**.

    ![An image of the Box Signature Verification Certificate.](_images/ogf1563995187462.png)

15. On the **Activation & Summary** screen, set **Connection Status** to Active, then click **Save**.

---

---
title: Configure provisioning
description: To configure a connection for outbound provisioning to Box, follow the instructions in this section.
component: box
page_id: box:setup:pf_box_connector_configure_provisioning
canonical_url: https://docs.pingidentity.com/integrations/box/setup/pf_box_connector_configure_provisioning.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure provisioning

## About this task

To configure a connection for outbound provisioning to Box, follow the instructions in this section.

Outbound provisioning details are managed within a service provider (SP) connection. You can configure outbound provisioning with or without Browser SSO, WS-Trust STS, or both when you create a new SP connection. You can also add outbound provisioning to an existing SP connection.

## Steps

1. In the PingFederate administrator console, configure the data store that PingFederate will use as the source of user data. Learn more in [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html) in the PingFederate documentation.

   * When targeting users and groups for provisioning, exclude the user account that you will use to administer users in your connection to Box. This prevents the PingFederate provisioning engine from interfering with the account that provisions users and groups.

2. Create a new SP connection or select an existing SP connection from the **SP Configuration** menu.

3. On the **Connection Template** screen, select the **Use a template for this connection** option and choose **Box Connector** from the **Connection Template** drop-down list. You will be asked to provide the `boxmetadata.xml` file you obtained earlier in [Download Box SAML 2.0 metadata file](pf_box_connector_download_box_saml_20_metadata_file.html).

   ![An image of the Connection Template screen.](_images/igc1563995181315.png)

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | If this selection is not available, verify the connector installation and restart PingFederate. |

4. On the **Connection Type** screen, ensure the **Outbound Provisioning** check box is selected, and the **Browser SSO Profiles** check box is cleared (if appropriate).

5. On the **General Info** screen, the default values are taken from the metadata file you selected in step 2. We recommend using the metadata default values.

   ![An image of the General Info screen.](_images/dfn1563995181955.png)

6. Follow the connection wizard to configure the connection.

7. On the **Outbound Provisioning** screen, click **Configure Provisioning**.

8. On the **Target** screen, enter the values for each field as required by the Box Connector.

   ![An image of the Target screen.](_images/gqj1563995182647.png)

   | Field Name                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Client ID**                                                 | The client ID for the application created in Box.Learn more about obtaining a client ID in [Obtain client ID and secret from Box](pf_box_connector_obtain_client_id_and_secret_from_box.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | **Client Secret**                                             | The client secret generated during application creation for Box.Learn more about obtaining a client secret in [Obtain client ID and secret from Box](pf_box_connector_obtain_client_id_and_secret_from_box.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | **OAuth Access Token**                                        | The OAuth access token generated by the OAuth Configuration Service.Learn more about obtaining authorized OAuth tokens in [Generate OAuth access and refresh tokens](pf_box_connector_generate_oauth_access_and_refresh_tokens.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | **OAuth Refresh Token**                                       | The OAuth refresh token generated by the OAuth Configuration Service.Learn more about obtaining authorized OAuth tokens in [Generate OAuth access and refresh tokens](pf_box_connector_generate_oauth_access_and_refresh_tokens.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | **Token Management Datastore**                                | Select where tokens will be stored:- **Flatfile** (default)

     Tokens will be stored in a flatfile named `boxoauthtoken.conf` located at `<pf_install>/server/default/data/adapter-config`.

     &#xA;&#xA;The flatfile option is only available when running in Standalone mode, since the flatfile cannot be accessed by multiple nodes. The flatfile option cannot be used in a clustered environment even if only one node is used for provisioning.

   - **Database**

     Tokens can also be stored in a database. If you have set up databases in PingFederate, they will appear in the list as options. If you have a multinode PingFederate configuration for clustered or failover use cases, tokens must be stored in a database.

     The `saas_connection_fields` table must be first created in the database using the appropriate supplied script. The same database used for PingFederate provisioning can be used to create the `saas_connection_fields` table. This must be completed before configuring the Box Connector. During configuration, choose the database that contains the `saas_connection_fields` table.                                                                         |
   | **Group Provenance** (Optional)                               | Optional and for group provisioning only. This allows you to keep track of which external source this group is coming from (for example, "Active Directory", "Google Groups", "Facebook Groups"). This field should be a human-readable identifier up to 255 characters long. Setting this will also prevent Box users from editing this group directly through Box. This is desirable for one-way syncing of groups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | **Group Name Source**                                         | Possible values:- **Group Common Name** (default)

     When selected, groups will be provisioned in Box with the name equal to the common name of the group in Active Directory.

   - **Group Distinguished Name**

     When selected, groups will be provisioned in Box with the name equal to the distinguished name of the group in Active Directory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Provisioning Options**                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | **User Create**                                               | * **True** (default)

     Users will be created in Box.

   * **False**

     Users will not be created in Box.

     &#xA;&#xA;The provisioner.log will display a warning within the create user workflow that the user was not created in Box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | **User Update**                                               | - **True** (default)

     Users will be updated in Box.

   - **False**

     Users will not be updated in Box.

     &#xA;&#xA;The provisioner.log will display a warning within the update user workflow that the user was not updated in Box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | **User Disable/Delete**                                       | * **True** (default)

     Users will be disabled or deleted in Box.

     &#xA;&#xA;A disabled user can only be re-enabled if User Update is true.

   * **False**

     Users will not be disabled or deleted in Box.

     &#xA;&#xA;The provisioner.log will display a warning indicating that the user was not disabled or deleted in Box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | **Provision Disabled Users**                                  | This option is only relevant if **User Create** is true.* **True** (default)

     If a disabled user in the user store is targeted for provisioning, it will be created in a disabled state in Box.

   * **False**

     Box users will not be created in a disabled state. This is desirable for scenarios where there are disabled users in the data store, not intended for creation in Box during initial synchronization.

     &#xA;&#xA;The provisioner.log will display a warning within the create user workflow indicating that the user was not created in Box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | **Personal Folders**                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | **Create Personal Folders**                                   | - **False** (default)

     Personal folders will not be created.

   - **True**

     On the creation of a new user, a personal Box folder will be created for the user. The new folder will be created in a parent folder you must specify on this page (see **Parent Folder ID**), and its name will be the value of the user's **Personal Folder Name** attribute. You can find details in [Supported attributes reference](pf_box_connector_supported_attributes_reference.html).

     &#xA;&#xA;If an issue occurs during the creation of the personal folder, the server.log will display a warning indicating that the user's personal folder was not created in Box. If you have applied Additional logging changes, this will be shown in the provisioner.log.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | **Parent Folder ID**                                          | This option is required if **Create Personal Folders** is true.The ID of the parent folder in which new personal folders will be created. The administrator account used when obtaining the client ID and client secret must be the owner of this folder.You can easily find the ID of a folder by navigating to the desired parent folder in the Box web portal and copying the string of numbers at the end of the url. For example, the ID of the folder located at:- https\://myconnector.app.box.com/folder/12345678910would be `12345678910`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | **Personal Folder Permission Levels**                         | This option is only relevant if **Create Personal Folders** is true.- **Admin as Owner - User as Co-Owner** (default)

     When a new personal folder is created, the admin will be the owner of the folder, and the user will be a co-owner.

   - **Admin as Owner - User as Editor**

     When a new personal folder is created, the admin will be the owner of the folder, and the user will be an editor.

   - **User as Owner**

     When a new personal folder is created, the user will be the owner, and the admin will have no permissions on or visibility into that folder.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | **Deprovisioning**                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | **Remove User Action**                                        | Select a deprovision method (**Suspend** or **Delete**). Deprovisioning is triggered when previously provisioned users no longer meet the condition set in the **Source Location** screen, or when a user has been suspended or deleted from the data store. This option is only applicable if **User Disable/Delete** is set to true.- **Suspend** (default)

     When selected, if you delete a user from Active Directory, the user will be suspended in Box (also known as a soft delete).

   - **Delete**

     When selected, if you delete a user from Active Directory, the user will be deleted in Box (also known as a hard delete).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | **Box Account Email For Transferring Deleted User's Content** | Optional and only relevant when **User Disable/Delete** is true and **Remove User Action** is **Delete**.The email associated with a valid and active Box account. When this is specified, if a user is deleted, their content (for example, files) would be transferred to the specified Box account instead of being deleted with the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | **Force Delete Managed Content**                              | This option is only relevant if **User Disable/Delete** is true, **Remove User Action** is **Delete**, and the **Box Account Email For Transferring Deleted User's Content** is valid.- **False - Users with managed content will not be deleted** (default)

     Attempts to delete users who own files will fail unless the files can be transferred to another account. If a value has been provided for **Box Account Email For Transferring Deleted User's Content** field then the user will be deleted after the data is transferred. The `provisioner.log` will show an error and retry on the next provisioning cycle.

   - **True - CAUTION: Users and their managed content will be deleted**

     Attempts to delete users will proceed regardless of whether they own files. Any content owned by the user, including folders and files, will be permanently deleted from Box. If a value has been provided for the **Box Account Email For Transferring Deleted User's Content** field, then the transfer of files will be attempted prior to the user and content being deleted. Only select this option if revoking user access to content is of a higher priority than preserving the content. |

   |   |                                                                                                                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Once PingFederate is restarted, these and subsequent authorized OAuth tokens are stored in either the flatfile or the database, depending on the **Token Management Datastore** choice.If these values in your SP connection require updating at any time in the future, follow the steps in [Updating Box OAuth tokens](../troubleshooting/pf_box_connector_updating_box_oauth_tokens.html). |

9. Click **Next** to continue the provisioning configuration. Learn more in the following sections under [Outbound provisioning for IdPs](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_outboun_provis_for_idp.html) in the PingFederate documentation:

   * [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html)

   * [Specifying channel information](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasgeneralinfostate.html)

   * [Identifying the source datastore](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourceselectionstate.html)

   * [Modifying source settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcesettingsstate.html)

   * [Specifying a source location](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saassourcelocationstate.html)

   * [Mapping attributes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasattrmappingmgmtstate.html)

   * [Reviewing channel settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saaschanneltasklet_saasactivationstate.html)

     |   |                                                                                                                 |
     | - | --------------------------------------------------------------------------------------------------------------- |
     |   | Credentials will be verified when the channel and SP connection is set to Active and provisioning is initiated. |

     |   |                                                                                                                                                                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you are not ready to complete the provisioning configuration, you can click **Save** and return to the configuration page later. To return to the configuration page, select the connection from **Identity Provider > SP Connections > Manage All**. |

---

---
title: Configure SAML SSO
description: The following section describes the steps for configuring single sign-on (SSO) to Box.
component: box
page_id: box:setup:pf_box_connector_configure_saml_sso
canonical_url: https://docs.pingidentity.com/integrations/box/setup/pf_box_connector_configure_saml_sso.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Configure SAML SSO

The following section describes the steps for configuring single sign-on (SSO) to Box.

|   |                                                        |
| - | ------------------------------------------------------ |
|   | Configuring SSO is optional for outbound provisioning. |

* [Configure PingFederate for SSO](pf_box_connector_configure_pf_for_sso.html)

* [Configure Box for SSO](pf_box_connector_configure_box_for_sso.html)

---

---
title: Download Box SAML 2.0 metadata file
description: This connector's quick-connection template uses a metadata .xml file from Box to assist in configuring many settings in the SP connection. When asked during the SP connection configuration steps, import the boxmetadata.xml that you downloaded from Box.
component: box
page_id: box:setup:pf_box_connector_download_box_saml_20_metadata_file
canonical_url: https://docs.pingidentity.com/integrations/box/setup/pf_box_connector_download_box_saml_20_metadata_file.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Download Box SAML 2.0 metadata file

## About this task

This connector's quick-connection template uses a metadata `.xml` file from Box to assist in configuring many settings in the SP connection. When asked during the SP connection configuration steps, import the `boxmetadata.xml` that you downloaded from Box.

## Steps

1. Download the SAML 2.0 metadata from [Box](https://cloud.box.com/s/3isa8qvvqn).

2. Save the `.xml` file to a desired location.

---

---
title: Download manifest
description: The distribution .zip archive for the connector contains the following:
component: box
page_id: box:release_notes:pf_box_connector_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/box/release_notes/pf_box_connector_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 17, 2026
---

# Download manifest

The distribution `.zip` archive for the connector contains the following:

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `/legal`

  * `Legal.pdf`: Copyright and license information.

* `/dist`: Contains libraries needed for the connector:

  * `pf-box-quickconnection-<version>.jar`: The PingFederate Box Provisioner.

* `/scripts`

  * `saas_connection_fields-postgresql.sql`

  * `saas_connection_fields-oracle.sql`

  * `saas_connection_fields-mysql.sql`

  * `saas_connection_fields-mssql.sql`

---

---
title: Enable outbound provisioning
description: After enabling outbound provisioning in the <pf_install>/pingfederate/bin/run.properties file, you must also activate the outbound provisioning role in the administrative console.
component: box
page_id: box:setup:pf_box_connector_enable_outbound_provisioning
canonical_url: https://docs.pingidentity.com/integrations/box/setup/pf_box_connector_enable_outbound_provisioning.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enable outbound provisioning

## About this task

After enabling outbound provisioning in the `<pf_install>/pingfederate/bin/run.properties` file, you must also activate the outbound provisioning role in the administrative console.

## Steps

1. Go to the **Server Configuration > Server Settings > Roles & Protocols** screen.

2. Select the **Outbound Provisioning** check box.

   ![An image of the Roles & Protocols screen.](_images/fes1563995185697.png)

   |   |                                                                                                                                                                                                                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Enabling outbound provisioning adds the outbound provisioning screen, requiring the selection of a database to facilitate provisioning. Learn more in [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html) or click **Help** from the configuration screen. |

---

---
title: Generate OAuth access and refresh tokens
description: "Go to the Ping OAuth Configuration Service at the following URL: https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform"
component: box
page_id: box:setup:pf_box_connector_generate_oauth_access_and_refresh_tokens
canonical_url: https://docs.pingidentity.com/integrations/box/setup/pf_box_connector_generate_oauth_access_and_refresh_tokens.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Generate OAuth access and refresh tokens

## Steps

1. Go to the Ping OAuth Configuration Service at the following URL: <https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oasrequestform>

2. In the list, select **Box Connector**.

   ![A screen capture of the OAuth Configuration Service screen.](_images/mfz1563995179128.png)

3. Enter the **Client ID** value you previously obtained into the **ClientID** field.

4. Enter the **Client Secret** value you previously obtained into the **Client Secret** field.

5. Click the **Connect** button.

6. Sign on to Box as an administrative user for your organization.

   |   |                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you are already signed on to Box you will not be asked to sign on again. Make sure that the account you are signed in under is an administrative account. |

7. Click **Grant access to Box** to generate your access and refresh tokens.

8. You should be redirected to the OAuth Configuration Service and presented with an access token and refresh token.

   ![A screen capture of the OAuth Configuration Service response.](_images/qei1563995179770.png)

9. Copy the **Access Token** and **Refresh Token** to use when configuring the Box Connector.

---

---
title: Install the connector
description: This section describes the common steps required to install the PingFederate Box Connector.
component: box
page_id: box:setup:pf_box_connector_install_the_connector
canonical_url: https://docs.pingidentity.com/integrations/box/setup/pf_box_connector_install_the_connector.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Install the connector

## About this task

This section describes the common steps required to install the PingFederate Box Connector.

If you experience issues with deployment, installation or configuration, visit Ping Identity [Support & Community](https://support.pingidentity.com/s/).

## Steps

1. Download the Box Provisioner `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/box-single-signon-integration).

2. Stop the PingFederate server if it is running.

3. Extract the Box Connector distribution `.zip` archive.

4. Copy the contents of the `dist` directory into the `<pf_install>/pingfederate/server/default/deploy` directory.

5. (Optional) If you plan to use the connector for outbound provisioning, edit the `run.properties` file located in `<pf_install>/pingfederate/bin`, changing the property `pf.provisioner.mode` to `STANDALONE`. For example:

   `pf.provisioner.mode=STANDALONE`

   |   |                                                                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Learn more about using the FAILOVER setting for runtime deployment in [Deploying provisioning failover](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html). |

6. Start the PingFederate server.

---

---
title: Known issues and limitations
description: Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.
component: box
page_id: box:release_notes:pf_box_connector_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/box/release_notes/pf_box_connector_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  box-token-failover-support-limitations: Box token failover support limitations
  performance-limitations: Performance limitations
---

# Known issues and limitations

* Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.

* User attributes cannot be cleared once set.

* Version 2.2 and later enables updating a user's login. However, the user has to have logged in previously for the update to succeed.

* The provenance attribute is the only supported attribute for group provisioning.

* The provenance attribute cannot be cleared once set for a group.

* The Inactive Status Default user attribute will have no effect if the Box connector is configured to delete (hard delete) instead of disable (soft delete) for user deprovisioning. Additionally, deleting a user in LDAP will always set that user as inactive in Box.

* When an LDAP user is deleted in a targeted group distinguished name (DN), the provisioning connector does not propagate the deletion until a new user is added to the group. This limitation is compounded when the **User Create** provisioning option is disabled. For solutions, see [SaaS provisioner does not remove the user](https://support.pingidentity.com/s/article/After-deleting-an-AD-user-account-SaaS-provisioner-does-not-remove-the-user-in-the-next-provisioning-cycle-when-Group-DN-is-specified) in the Knowledge Base.

* A Box API limitation prevents logins of different letter case (but otherwise the same), from being updated by the provisioner. In scenarios where the letter case differs, the login will be omitted from the API operation. For example, `USER@TEST.COM` in Box, cannot be updated to `user@test.com`. In an update operation, the login would be omitted, but any other attributes that may have changed would be provisioned and updated.

* Due to Box API requirements, only primary, validated email addresses can be used to sync users.

## Box token failover support limitations

* Tokens entered during SP connection configuration will be invalidated and replaced with new tokens upon first use. Afterwards, they will be updated with new tokens once they expire.

* If a SP connection is re-configured to change the connection datasource from a database to a flatfile, or vice versa, any pre-existing entries in the new datasource for the given client ID must be deleted before the SP connection is updated.

## Performance limitations

* Enabling personal folder functionality will diminish initial synchronization provisioning performance.

---

---
title: Obtain client ID and secret from Box
description: The Box Connector's outbound provisioning functionality is built using Box's REST API, which requires an OAuth 2.0 access token for authentication. To obtain the access token, you will need to first obtain an app key and secret from Box.
component: box
page_id: box:setup:pf_box_connector_obtain_client_id_and_secret_from_box
canonical_url: https://docs.pingidentity.com/integrations/box/setup/pf_box_connector_obtain_client_id_and_secret_from_box.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtain client ID and secret from Box

## About this task

The Box Connector's outbound provisioning functionality is built using Box's REST API, which requires an OAuth 2.0 access token for authentication. To obtain the access token, you will need to first obtain an app key and secret from Box.

## Steps

1. Sign on to your Box account as an administrative user for your organization.

   <https://app.box.com/developers/console>

2. Go to **Dev Console**.

3. Go to **My Apps**.

4. Select **Create New App**.

5. Select **Enterprise Integration**.

6. On the **Authentication Method** screen, select **Standard OAuth 2.0 (User Authentication)**.

7. Give your application a name, such as 'PingFederate Provisioning'.

8. In the **OAuth 2.0 Credentials** section, copy the **Client ID** and **Client Secret** values for later use.

9. Update the **Redirect URI** field with the following URL:

   * https\://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oastempcredresponse/

10. Click **Save Changes**.

---

---
title: Sample OGNL expressions
description: PingFederate provides an advanced option allowing administrators to map user attributes by way of an expression language. The following are sample OGNL expressions for common use case requirements with the PingFederate Box Connector. Learn more about enabling expressions in PingFederate in Enabling and disabling expressions in the PingFederate documentation.
component: box
page_id: box:setup:pf_box_connector_sample_ognl_expressions
canonical_url: https://docs.pingidentity.com/integrations/box/setup/pf_box_connector_sample_ognl_expressions.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  example: Example
  lastname-firstname: Lastname, Firstname
  lastname-firstname-department: Lastname, Firstname (Department)
  remove-domain-from-email-address: Remove Domain from Email Address
---

# Sample OGNL expressions

PingFederate provides an advanced option allowing administrators to map user attributes by way of an expression language. The following are sample OGNL expressions for common use case requirements with the PingFederate Box Connector. Learn more about enabling expressions in PingFederate in [Enabling and disabling expressions](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enable_disable_express.html) in the PingFederate documentation.

The below sample expressions are intended for use with the **Personal Folder Name** attribute. This can be configured under **SP Connection > Configure Channels > Channel > Attribute Mapping** when **Create Personal Folders** is enabled. To configure the **Personal Folder Name** attribute, select **Edit**, add all necessary attributes for the evaluation of the expression, and configure the expression.

## Example

### Lastname, Firstname

The following expression would produce the format `Collins, Audrey` for the user Audrey Collins.

```
#lastname = #this.get("sn").toString(),
#firstname = #this.get("givenName").toString(),
#foldername = #lastname + ", " + #firstname
```

### Lastname, Firstname (Department)

The following expression would produce the format `Collins, Audrey (Sales)`, where the user Audrey Collins works in the Sales department.

```
#lastname = #this.get("sn").toString(),
#firstname = #this.get("givenName").toString(),
#department = #this.get("department").toString(),
#foldername = #lastname + ", " + #firstname + " (" + #department + ")"
```

### Remove Domain from Email Address

The following expression would produce the format `acollins`, where the user Audrey Collins has an email address `acollins@example.com`.

```
#this.get("mail").toString().split("@")[0]
```

---

---
title: Supported attributes reference
description: The following attributes can be mapped for user provisioning to Box.
component: box
page_id: box:setup:pf_box_connector_supported_attributes_reference
canonical_url: https://docs.pingidentity.com/integrations/box/setup/pf_box_connector_supported_attributes_reference.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Supported attributes reference

The following attributes can be mapped for user provisioning to Box.

| Attribute                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                              | The name of the user. This attribute is required.                                                                                                                                                                                                                                                                                                                                                                                      |
| Login                             | The email address the user uses to sign on. This attribute is required.&#xA;&#xA;This value must be in the format of an email. Box Connector version 2.2 and later enables updating a user's login. However, the user has to have signed on previously for the update to succeed.                                                                                                                                                      |
| Language                          | The user's language. Learn more in [Language Codes](https://developer.box.com/guides/api-calls/language-codes/) in the Box documentation.                                                                                                                                                                                                                                                                                              |
| Timezone                          | The user's timezone. Input format follows tz database timezones.                                                                                                                                                                                                                                                                                                                                                                       |
| Space Amount                      | The user's total available space amount in bytes. A value of -1 grants unlimited storage.                                                                                                                                                                                                                                                                                                                                              |
| Inactive Status Default           | The user's default inactive status. The three inactive defaults include:- inactive

- cannot\_delete\_edit

- cannot\_delete\_edit\_upload&#xA;&#xA;When a user is disabled, the user status will be the value you have specified here. If no value, the default is inactive. Deleting the user in LDAP will always default to inactive regardless of the attribute's value or the Target screen configuration for Remove User Action. |
| Job Title                         | The user's job title.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Phone                             | The user's phone number.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Address                           | The user's address.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Role                              | The user's enterprise role. Valid options include:- coadmin

- user                                                                                                                                                                                                                                                                                                                                                                    |
| Can See Managed Users             | Whether the user can see other enterprise users in their contact list. Valid options include:- true

- false                                                                                                                                                                                                                                                                                                                           |
| Is Sync Enabled                   | Whether or not the user can use Box Sync. Valid options include:- true

- false                                                                                                                                                                                                                                                                                                                                                        |
| Is Exempt from Device Limits      | Whether to exempt the user from Enterprise device limits. Valid options include:- true

- false                                                                                                                                                                                                                                                                                                                                        |
| Is Exempt from Login Verification | Whether or not this user must use two-factor authentication. Valid options include:- true

- false                                                                                                                                                                                                                                                                                                                                     |
| Is External Collab Restricted     | Whether this user is allowed to collaborate with users outside her enterprise. Valid options include:- true

- false                                                                                                                                                                                                                                                                                                                   |
| Personal Folder Name              | The name to be used for the personal folder which can optionally be created along with a new user. The personal folder name format can be configured using OGNL expressions. Learn more in [Sample OGNL expressions](pf_box_connector_sample_ognl_expressions.html).Learn more about personal folder fields in [Configure provisioning](pf_box_connector_configure_provisioning.html).                                                 |

---

---
title: Troubleshooting
description: The following table lists potential problems administrators might encounter during the setup or deployment of the Box Connector, along with possible solutions. Learn more in Common Errors in the Box documentation.
component: box
page_id: box:troubleshooting:pf_box_connector_troubleshooting
canonical_url: https://docs.pingidentity.com/integrations/box/troubleshooting/pf_box_connector_troubleshooting.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Troubleshooting

The following table lists potential problems administrators might encounter during the setup or deployment of the Box Connector, along with possible solutions. Learn more in [Common Errors](https://developer.box.com/guides/api-calls/permissions-and-errors/common-errors/) in the Box documentation.

| Problem                                                                                                                                                                                                                                                    | Possible Solution                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The exception {"error":"invalid\_grant", "error\_description":"Refresh token has expired"} appears in `server.log`.                                                                                                                                        | The error indicates that the refresh token has expired. A refresh token from Box has a lifespan of 60 days. Additionally, if a new refresh token has been requested, the old one will become expired. Learn more about configuring PingFederate with a new refresh token in [Updating Box OAuth tokens](pf_box_connector_updating_box_oauth_tokens.html). |
| The exception {"type":"error","status":403, "code":"access\_denied\_insufficient\_permissions", "help\_url":"http:\\/\\/developers.box.com\\/docs\\/#errors", "message":"Access denied - insufficient permission"} appears in `server.log`.                | Revert the email to the original and have the user sign on and set their password, then update the user's email.                                                                                                                                                                                                                                          |
| The exception {"errors":\[{"reason":"invalid\_parameter", "name":"email","message":"Invalid value '\<email value>. This email address already has a Box account. You can only add emails that do not have an account already."}]} appears in `server.log`. | Revert the email to the original and have the user log in and set their password, then update the user's email.                                                                                                                                                                                                                                           |
| The exception {"type":"error","status":500,"code":"internal\_server\_error", "help\_url":"http:\\/\\/developers.box.com\\/docs\\/#errors","message":"Internal Server Error","request\_id":"xxxxxxxx"} appears in `provisioner.log`.                        | If there is a value in the **Target** field **Box Account Email for Transferring Deleted User's Content**, ensure that it is a valid email belonging to a Box user in your instance, and that the user is active.                                                                                                                                         |

---

---
title: Updating Box OAuth tokens
description: Use the following procedure to manually update the Box OAuth tokens.
component: box
page_id: box:troubleshooting:pf_box_connector_updating_box_oauth_tokens
canonical_url: https://docs.pingidentity.com/integrations/box/troubleshooting/pf_box_connector_updating_box_oauth_tokens.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Updating Box OAuth tokens

## About this task

Use the following procedure to manually update the Box OAuth tokens.

## Steps

1. Obtain new Box OAuth tokens. Learn more in [Generate OAuth access and refresh tokens](../setup/pf_box_connector_generate_oauth_access_and_refresh_tokens.html).

2. If using the flatfile method for token storage, delete the `boxoauthtoken.conf` file located at `<pf_install>/server/default/data/adapter-config`. If using the database method for token storage, delete the row that contains the Box tokens from the `saas_connection_fields` table.

3. On the **Target** screen of the SP connection, update the following fields with the new OAuth token values:

   * `OAUTH_ACCESS_TOKEN`

   * `OAUTH_REFRESH_TOKEN`

4. Restart PingFederate. This will regenerate the flatfile or repopulate the database with the new credentials.

---

---
title: Upgrade an existing connector
description: Before stopping the PingFederate server to upgrade the Box Connector, access the Attribute Mapping screen for existing channel configurations and note the current configuration.
component: box
page_id: box:setup:pf_box_connector_upgrade_an_existing_connector
canonical_url: https://docs.pingidentity.com/integrations/box/setup/pf_box_connector_upgrade_an_existing_connector.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Upgrade an existing connector

## Steps

1. Before stopping the PingFederate server to upgrade the Box Connector, access the **Attribute Mapping** screen for existing channel configurations and note the current configuration.

   |   |                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The upgrade process removes existing mappings and defaults on the **Attribute Mapping** screen. These must be configured again before activating the channel configuration. |

2. Disable the existing service provider (SP) connection where the Box Connector is configured.

3. Delete the existing Box Connector SP connection and save.

4. Stop the PingFederate server if it is running.

5. Unzip the new Box Connector distribution `.zip` archive into a holding directory.

6. Remove any older versions of `pf-box-quickconnection-[version].jar` from: `<pf_install>/pingfederate/server/default/deploy`

7. From the `dist` directory of the new version of the connector, copy the `pf-box-quickconnection-[version].jar` file into the `<pf_install>/pingfederate/server/default/deploy` directory.

8. Start the PingFederate server.

9. Create a new SP connection, using **Box Connector** as the connection template.

10. Follow the instructions in [Configure provisioning](pf_box_connector_configure_provisioning.html) and [Updating Box OAuth tokens](../troubleshooting/pf_box_connector_updating_box_oauth_tokens.html) to configure the connection.

11. Access the **Attribute Mapping** screen for existing channel configurations and click **Refresh Fields**.

12. Ensure all new required fields (if any), are mapped appropriately or have a default value.

13. When you have completed the attribute configuration, click **Done**, **Done**, and **Save**.

14. Activate the SP connection to resume outbound provisioning.

---

---
title: User and group management
description: The Box Provisioner synchronizes users and groups from your datastore to Box. The following describes the behavior of each provisioning capability.
component: box
page_id: box::pf_box_connector_user_and_group_management
canonical_url: https://docs.pingidentity.com/integrations/box/pf_box_connector_user_and_group_management.html
llms_txt: https://docs.pingidentity.com/integrations/box/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning: User deprovisioning
  synchronizing-existing-groups: Synchronizing existing groups
  group-provisioning: Group provisioning
  group-name-updates: Group name updates
  group-membership-updates: Group membership updates
  group-deletion: Group deletion
---

# User and group management

The Box Provisioner synchronizes users and groups from your datastore to Box. The following describes the behavior of each provisioning capability.

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure the following capabilities and specify which users to provision when you get to the [Configure provisioning](setup/pf_box_connector_configure_provisioning.html) part of the setup process. |

## Synchronizing existing users

PingFederate synchronizes users based on the `mail` attribute in Box. If a user already exists in your datastore and Box, mapping this attribute correctly links the two records together.

For example:

* In Box, Janet's `mail` is `jsmith@example.com`.

* In your datastore, Janet's `mail` is `jsmith@example.com`.

* On the **Attribute Mapping** tab of your provisioning connection configuration, map the `mail` attribute to `mail`.

* When the provisioning connector runs, the datastore user is provisioned with a `mail` of `jsmith@example.com`. That matches Janet's existing `mail` in Box, so her information in the datastore is synchronized to her Box account.

## User provisioning

PingFederate provisions users when any of the following happens:

* A user is added to the datastore group or filter that is targeted by the provisioning connector.

* A user with `disabled` status is added to the datastore group or filter that is targeted by the provisioning connector, and the **Provision disabled users** provisioning option is enabled. This feature is not available in all provisioning connector versions.

You can define which users PingFederate targets for provisioning on the **Source Location** tab of your provisioning connection configuration.

## User updates

PingFederate updates users when a user attribute changes in your datastore.

You can define which attributes PingFederate monitors for changes on the **Attribute Mapping** tab of your provisioning connection configuration.

## User deprovisioning

PingFederate deprovisions users when any of the following happens:

* A user is deleted from the user store.

* A user is disabled in the user store.

* A user is removed from the datastore group or filter that is targeted by the provisioning connector.

The **Remove User Action** setting in the connection configuration determines whether the deprovisioning action disables or deletes the user.

## Synchronizing existing groups

PingFederate synchronizes groups from the datastore to the target service based on the group name.

For example:

* In Box, there is a group is named `Accounting`.

* In your datastore, there is a group with a `CN` of `Accounting`.

* When the provisioning connector runs, the two groups are synchronized.

## Group provisioning

PingFederate provisions groups when a group is added to the datastore filter that is targeted by the provisioning connector.

You can define which groups PingFederate targets for provisioning and monitors for changes on the **Source Location** tab in your provisioning connection configuration.

## Group name updates

PingFederate renames groups when they are renamed in the datastore.

## Group membership updates

PingFederate updates group memberships when memberships change in the datastore, whether the change is in the group's properties or a user's properties.

Group memberships in the datastore overwrite the group memberships in Box.

## Group deletion

PingFederate deletes groups when any of the following happens:

* The group is deleted in the datastore.

* The group is removed from the datastore group or filter that is targeted by the provisioning connector.

|   |                                                     |
| - | --------------------------------------------------- |
|   | Group deletions are permanent and cannot be undone. |
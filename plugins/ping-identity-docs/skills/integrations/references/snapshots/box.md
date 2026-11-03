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

| Attribute                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                              | The name of the user. This attribute is required.                                                                                                                                                                                                                                                                                                                                                                                 |
| Login                             | The email address the user uses to sign on. This attribute is required.&#xA;&#xA;This value must be in the format of an email. Box Connector version 2.2 and later enables updating a user's login. However, the user has to have signed on previously for the update to succeed.                                                                                                                                                 |
| Language                          | The user's language. Learn more in [Language Codes](https://developer.box.com/guides/api-calls/language-codes/) in the Box documentation.                                                                                                                                                                                                                                                                                         |
| Timezone                          | The user's timezone. Input format follows tz database timezones.                                                                                                                                                                                                                                                                                                                                                                  |
| Space Amount                      | The user's total available space amount in bytes. A value of -1 grants unlimited storage.                                                                                                                                                                                                                                                                                                                                         |
| Inactive Status Default           | The user's default inactive status. The three inactive defaults include:- inactive

- cannot_delete_edit

- cannot_delete_edit_upload&#xA;&#xA;When a user is disabled, the user status will be the value you have specified here. If no value, the default is inactive. Deleting the user in LDAP will always default to inactive regardless of the attribute's value or the Target screen configuration for Remove User Action. |
| Job Title                         | The user's job title.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Phone                             | The user's phone number.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Address                           | The user's address.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Role                              | The user's enterprise role. Valid options include:- coadmin

- user                                                                                                                                                                                                                                                                                                                                                               |
| Can See Managed Users             | Whether the user can see other enterprise users in their contact list. Valid options include:- true

- false                                                                                                                                                                                                                                                                                                                      |
| Is Sync Enabled                   | Whether or not the user can use Box Sync. Valid options include:- true

- false                                                                                                                                                                                                                                                                                                                                                   |
| Is Exempt from Device Limits      | Whether to exempt the user from Enterprise device limits. Valid options include:- true

- false                                                                                                                                                                                                                                                                                                                                   |
| Is Exempt from Login Verification | Whether or not this user must use two-factor authentication. Valid options include:- true

- false                                                                                                                                                                                                                                                                                                                                |
| Is External Collab Restricted     | Whether this user is allowed to collaborate with users outside her enterprise. Valid options include:- true

- false                                                                                                                                                                                                                                                                                                              |
| Personal Folder Name              | The name to be used for the personal folder which can optionally be created along with a new user. The personal folder name format can be configured using OGNL expressions. Learn more in [Sample OGNL expressions](pf_box_connector_sample_ognl_expressions.html).Learn more about personal folder fields in [Configure provisioning](pf_box_connector_configure_provisioning.html).                                            |

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

| Problem                                                                                                                                                                                                                                                   | Possible Solution                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The exception {"error":"invalid_grant", "error_description":"Refresh token has expired"} appears in `server.log`.                                                                                                                                         | The error indicates that the refresh token has expired. A refresh token from Box has a lifespan of 60 days. Additionally, if a new refresh token has been requested, the old one will become expired. Learn more about configuring PingFederate with a new refresh token in [Updating Box OAuth tokens](pf_box_connector_updating_box_oauth_tokens.html). |
| The exception {"type":"error","status":403, "code":"access_denied_insufficient_permissions", "help_url":"http:\\/\\/developers.box.com\\/docs\\/#errors", "message":"Access denied - insufficient permission"} appears in `server.log`.                   | Revert the email to the original and have the user sign on and set their password, then update the user's email.                                                                                                                                                                                                                                          |
| The exception {"errors":\[{"reason":"invalid_parameter", "name":"email","message":"Invalid value '\<email value>. This email address already has a Box account. You can only add emails that do not have an account already."}]} appears in `server.log`. | Revert the email to the original and have the user log in and set their password, then update the user's email.                                                                                                                                                                                                                                           |
| The exception {"type":"error","status":500,"code":"internal_server_error", "help_url":"http:\\/\\/developers.box.com\\/docs\\/#errors","message":"Internal Server Error","request_id":"xxxxxxxx"} appears in `provisioner.log`.                           | If there is a value in the **Target** field **Box Account Email for Transferring Deleted User's Content**, ensure that it is a valid email belonging to a Box user in your instance, and that the user is active.                                                                                                                                         |

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
---
title: About attribute mappings
description: Attribute mappings define how the values of a single destination attribute are determined.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_about_attr_mapping
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_about_attr_mapping.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 7, 2024
section_ids:
  json-attribute-mapping: JSON attribute mapping
  constructed-attribute-mapping: Constructed attribute mapping
  direct-attribute-mapping: Direct attribute mapping
  dn-attribute-mapping: DN attribute mapping
  reference-attribute-mapping: Reference attribute mapping
  workflow: Workflow
  example-mapping: Example mapping
  configuration: Configuration
  configuration-property-types: Configuration property types
  caching-properties: Caching properties
---

# About attribute mappings

Attribute mappings define how the values of a single destination attribute are determined.

The destination attribute in an attribute mapping can be derived from a direct mapping with a source attribute, constructed from a combination of hard-coded strings and elements of other attributes, or generated using custom Java class code. All attribute mapping types support the following properties:

| Property                        | Description                                                                                                                                                                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `to-attribute`                  | Specifies the name of the attribute whose values are constructed by the mapping.This property is required.                                                                                                                   |
| `description`                   | Describes the attribute mapping.This property is optional.                                                                                                                                                                   |
| `exclude-value`                 | Specifies a list of values to exclude from the destination attribute after applying the mapping.This property is optional.                                                                                                   |
| `also-depends-on-src-attribute` | Specifies the source attributes that trigger an update to the relevant destination attributes when changed, regardless of changes to attributes the mapping directly depends on.This property is optional.                   |
| `sync-on-every-update`          | Synchronizes the value of `to-attribute` on any detected change of any attribute.This property is optional.&#xA;&#xA;The attribute mapping of to-attribute is always evaluated during sync, even if the value didn't change. |

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | Use the `dsconfig list-attribute-mappings` command to view configured attribute mappings. |

The PingDataSync server supports the attribute mappings described in the following sections, unless otherwise specified.

## JSON attribute mapping

Use this mapping for a destination JSON attribute whose JSON field values are constructed by defining JSON attribute mapping field configuration objects. If any field value cannot be constructed, either because the required source attributes aren't present or the resulting value is invalid, that field is omitted from the constructed JSON attribute. The following example creates a JSON attribute mapping with the field `formatted` from the `cn` attribute:

```shell
$ bin/dsconfig create-attribute-map \
  --map-name PingDirectory_to_PingOne_User_Map
```

```shell
$ bin/dsconfig create-attribute-mapping \
  --map-name PingDirectory_to_PingOne_User_Map \
  --mapping-name name \
  --type json
```

```shell
$ bin/dsconfig create-json-attribute-mapping-field \
  --map-name PingDirectory_to_PingOne_User_Map \
  --mapping-name name \
  --field-name formatted \
  --set from-attribute:cn \
  --set json-type:string
```

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If any existing JSON fields of the destination attribute must be preserved, a JSON attribute configuration object must be created for the sync class. |

## Constructed attribute mapping

Use this mapping when a destination attribute's values are constructed from static text and multiple source attribute values. The source attribute values can be modified using regular expressions and replacement values. You can use a constructed attribute mapping to provide a fixed set of attribute values or to augment existing attribute values with additional fixed values. Constructed attribute mappings support the following properties:

| Property                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `value-pattern`             | Specifies a pattern for constructing the destination attribute value using fixed text and attribute values from the source entry.&#xA;&#xA;You can't have more than one multivalued attribute. If an attribute is multivalued, the destination value takes the same number of values minus duplicates.&#xA;&#xA;For example, a mapping of {givenName}{sn} produces values of 'Jim Smith', 'James Smith' if givenName has values of 'Jim', 'James' and sn has a value of 'Smith'.This property is optional.                                                                                                                                           |
| `conditional-value-pattern` | Specifies a pattern for conditionally constructing the destination attribute value using fixed text and attribute values from the source entry. The pattern constructs the destination attribute only if the specified LDAP filter matches the source entry. The value of this property has the form `LDAP-filter : pattern`.&#xA;&#xA;The LDAP filter is similar to what you can pass to the ldapsearch command. For example, if you want to select the admin-user-name attribute from the source only if the is-admin attribute has a value of true, you can use a value pattern of (is-admin=true) : {admin-user-name}.This property is optional. |

## Direct attribute mapping

Use this mapping when a destination attribute receives its values directly from a source attribute. To use a direct attribute mapping, the attribute values must not change in format from the source to the destination. Direct attribute mappings support the following properties:

| Property               | Description                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `from-attribute`       | Specifies the name of the source attribute whose values are used to provide the values of the destination attribute.This property is required. |
| `base64-encode-value`  | Encodes the source attribute with base-64 before synchronizing it to the destination.This property is optional.                                |
| `base-64-decode-value` | Decodes the source attribute from base-64 before synchronizing it to the destination.This property is optional.                                |

## DN attribute mapping

Use this mapping when a destination attribute receives its values directly from a source attribute whose distinguished name (DN) *(tooltip: \<div class="paragraph">
\<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
\</div>)* values require translation. This translation can be performed either by an existing DN map or a map configured within the attribute mapping itself. DN attribute mappings support the following properties:

| Property         | Description                                                                                                                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `from-attribute` | Specifies the name of the source attribute whose values are used to directly provide the values of the destination attribute.This property is required.                                                            |
| `dn-map`         | Constructs the destination DN value using components of the source DN and attributes from the source entry. If source DNs match different DN patterns, you can specify multiple DN maps.This property is optional. |

## Reference attribute mapping

Use this mapping when a destination attribute's values are derived from attributes of referenced entries. The source attribute contains a reference to another entry in the directory, and the destination attribute's values get constructed using information extracted from the destination referenced entry.

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This feature is provided as a **Preview**, which means that it isn't supported and should not be used in production environments. Learn more in [Feature statuses](../feature_status.html). |

When syncing entries with referential attributes to PingOne and other SCIM destinations, the destination attribute value frequently requires a JSON object construction, which contains multiple fields. These field values aren't available on the source, but can be retrieved on the destination by correlating the source reference entry to a destination reference entry and specifying an existing JSON attribute mapping. That makes reference attribute mapping an effective solution for this scenario. Learn more in [Synchronize with PingOne](pd_sync_with_p1.html) and [Configuring synchronization to a SCIM 2.0 server](pd_sync_config_synchronization_scim2_server.html).

### Workflow

The synchronization of a reference attribute follows a conceptual four-step path, moving from the source system to the destination system:

1. **Source entry**: For example, a group entry

2. **Source referenced entry**: For example, the user being referenced by the group on the source

3. **Destination referenced entry**: For example, the corresponding user on the destination

4. **Destination entry**: For example, the destination group where the reference value gets written

#### Example mapping

In the following example, you can combine the values of the `sn` and `givenName` attributes and correlate them to the entry with the matching `cn` attribute on the destination. After locating the destination referenced entry, you can extract the `uid` attribute value to use as the final destination reference value for constructing a DN.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For the purposes of this example, assume that you already created the following mappings:- `ref-cn-from-given-name-sn`, which produces a `cn` value for the source referenced entry

- `ref-dn-from-uid`, which builds the DN from the provided `uid` valueYou can also assume the following sample value for `member` on the source: `uid=user.1,ou=People,dc=example,dc=com`.We omitted the `source-referenced-entry-key` property because we used a `from-attribute` value of `dn` to pull in the DN value. |

```shell
bin/dsconfig create-attribute-mapping \
    --map-name "Attribute Map For Sync Class" \
    --mapping-name member \
    --type reference \
    --set source-entry-value:attribute:member \
    --set source-referenced-entry-value:mapping:"Attribute Map For Reference Attribute Mapping:ref-cn-from-given-name-sn" \
    --set destination-referenced-entry-key:attribute:cn \
    --set destination-referenced-entry-value:mapping:"Attribute Map For Reference Attribute Mapping:ref-dn-from-uid"
```

### Configuration

With reference attribute mapping, a value is extracted from the entry in the previous step and then used as a key to retrieve the corresponding entry in the next step. This path is defined by a set of key-value configuration properties, considered in a specific order, as follows:

| Configuration property               | Description                                                                                                   | Example                                                                                                                                                                               |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source-entry-value`                 | Extracts one or more values from the source entry.                                                            | If the source entry is a group, specifying `attribute:member` extracts the DN value of the group member.                                                                              |
| `source-referenced-entry-key`        | Uses the extracted value to retrieve the source referenced entry.                                             | Specifying `dn` enables the mapping to correlate the extracted DN `member` value to the user entry with a matching `dn` value.                                                        |
| `source-referenced-entry-value`      | Extracts a value from the source referenced entry.                                                            | Specifying `attribute:entryUUID` enables the mapping to extract the unique identifier of the matching user entry.                                                                     |
| `destination-referenced-entry-key`   | Uses the extracted value to retrieve the matching entry on the destination.                                   | Specifying `attribute:externalId` enables the mapping to correlate the extracted unique identifier to the user entry on the destination with a matching `externalId` value.           |
| `destination-referenced-entry-value` | Extracts the final value from the destination referenced entry to be used as the destination reference value. | Specifying `mapping:json-map:scim-user-reference` extracts a JSON object constructed by the `scim-user-reference` attribute mapping for use as the final destination attribute value. |

#### Configuration property types

You can use the following reference types for the reference attribute mapping configuration properties. The value returned depends on whether you use them with a value or key property.

|   |                                                           |
| - | --------------------------------------------------------- |
|   | You can't use mappings with a key configuration property. |

* `attribute:<attribute-name>`

  * For value configuration properties, this type returns the value of the attribute name specified.

  * For key configuration properties, this type returns the entry that contains an attribute of the specified name with a value that matches the value extracted from the previous entry in the workflow.

* `dn`

  * For value configuration properties, this type returns the DN of the entry.

  * For key configuration properties, this type returns the entry with the DN that matches the value extracted from the previous entry in the workflow.

* `mapping:<map-name>:<mapping-name>`

  For value configuration properties, this type returns only the specified attribute mapping in the specified attribute map.

  * The `to-attribute` isn't used for the specified attribute mapping.

  * For DN attribute mappings, you can specify a value of `dn` as the `from-attribute` to use the DN of the entry itself as input for the DN maps.

#### Caching properties

The following properties determine how long the server maintains a cached relationship between the extracted source entry values and the destination referenced entry values. If the limits are exceeded for either property, the cache expires.

* `maximum-reference-mappings-to-cache`

  The maximum number of mappings to cache. Setting this to a large value increases memory usage proportionally, but also reduces the amount of time required to process cached entries. The default value is 10,000.

* `reference-mapping-cache-duration`

  The maximum length of time (in seconds) that a cached mapping should be considered valid. Setting this to a long duration increases memory usage but also reduces the amount of time required to process cached entries. The default duration is 24 hours (86,400 seconds).

---

---
title: Access control filtering on the sync pipe
description: PingDataSync provides an advanced Sync Pipe configuration property, filter-changes-by-user, which performs access control filtering on a changelog entry for a specific user.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_access_ctrl_filter_sync_pipe
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_access_ctrl_filter_sync_pipe.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_sync_consids_access_ctrl_filter.adoc", "pd_sync_config_sync_pipe_filter_changes.adoc"]
section_ids:
  considerations-for-access-control-filtering: Considerations for access control filtering
  configure-the-sync-pipe-to-filter-changes-by-access-control-instructions: Configure the sync pipe to filter changes by access control instructions
  steps: Steps
---

# Access control filtering on the sync pipe

PingDataSync provides an advanced Sync Pipe configuration property, `filter-changes-by-user`, which performs access control filtering on a changelog entry for a specific user.

Since the changelog entry contains data from the target entry, the access controls filter out attributes that the user does not have the privileges to see before it is returned. For example, values in the changes, `ds-changelog-before-values`, `ds-changelog-after-values`, `ds-changelog-entry-key-attr-values`, and `deletedEntryAttrs` are filtered out through access control instructions.

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | This property is only available for notification mode and can be configured using the `create-sync-pipe-config` or `dsconfig` commands. |

The source server must be a PingDirectory server or a PingDirectoryProxy server that points to a PingDirectory server.

## Considerations for access control filtering

* The directory server will not return the changelog entry if the user is not allowed to see the target entry.

* The directory server strips out any attributes that the user is not allowed to see.

* If no changes are left in the entry, no changelog entry will be returned.

* If only some attributes are stripped out, the changelog entry will be returned.

* Access control filtering on a specific attribute value is not supported. Either all attribute values are returned or none.

* If a sensitive attribute policy is used to filter attributes when a client normally accesses the directory server, this policy will not be taken into consideration during notifications since the Sync User is always connecting using the same method. Configure access controls to filter out attributes, not based on the type of connection made to the server, but based on who is accessing the data. The `filter-changes-by-user` property will be able to evaluate if that person should have access to these attributes.

## Configure the sync pipe to filter changes by access control instructions

### Steps

1. Set the filter-changes-by-user property to filter changes based on access controls for a specific user.

   ```shell
   $ bin/dsconfig set-sync-pipe-prop \
     --pipe-name "Notifications Sync Pipe" \
     --set "filter-changes-by-user:uid=admin,dc=example,dc=com"
   ```

2. On the source directory server, set the `report-excluded-changelog-attributes` property to include the names of users that have been removed through access control filtering. This will allow PingDataSync to warn about attributes that were supposed to be synchronized but were filtered out. This step is recommended but not required.

   ```shell
   $ bin/dsconfig set-backend-prop \
     --backend-name "changelog" \
     --set "report-excluded-changelog-attributes:attribute-names"
   ```

   |   |                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingDataSync only uses the `attribute-names` setting for the PingDirectory server's `report-excluded-changelog-attributes` property. It does not use the `attribute-counts` setting for the property. |

---

---
title: Boolean SCIM 2.0 attribute mappings
description: Boolean System for Cross-domain Identity Management (SCIM) 2.0 attribute mappings can be used for cases in which the SCIM attribute has a value that is a single JavaScript Object Notation (JSON) Boolean value.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_boolean_scim2_attr_maps
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_boolean_scim2_attr_maps.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Boolean SCIM 2.0 attribute mappings

Boolean System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 attribute mappings can be used for cases in which the SCIM attribute has a value that is a single JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* Boolean value.

Additional configuration properties that are available for Boolean SCIM 2.0 attribute mappings include:

* `ldap-attribute-name`

  The name of the Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
  \<p>An open, cross platform protocol used for interacting with directory services.\</p>
  \</div>)* attribute (in the mapped representation of the source entry generated by the sync class) whose value will be used as the value of the SCIM 2.0 attribute. This is required, and the LDAP attribute must have a value of either `true` or `false`.

|   |                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This SCIM 2.0 attribute mapping type does not support multivalued attributes because it doesn't make sense for a Boolean attribute to have multiple values. |

You can use the following example configuration change to create a Boolean SCIM 2.0 attribute mapping:

```
dsconfig create-scim2-attribute-mapping \
     --mapping-name "Account Enabled" \
     --type boolean \
     --set scim-attribute-name:active \
     --set ldap-attribute-name:accountEnabled \
     --set attribute-usage:fetch \
     --set attribute-usage:create-during-realtime-sync \
     --set attribute-usage:create-during-resync \
     --set attribute-usage:update-during-realtime-sync \
     --set attribute-usage:update-during-resync \
     --set single-valued:true
```

---

---
title: Configure the external servers
description: Perform the following to configure an external server for each host in the deployment:
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_external_servers
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_external_servers.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure the external servers

## About this task

Perform the following to configure an external server for each host in the deployment:

## Steps

1. Configure a PingDirectory server as an external server, which will later be configured as a Sync Source. On PingDataSync, run the following `dsconfig` command:

   ```shell
   $ bin/dsconfig create-external-server \
     --server-name source-ds \
     --type ping-identity-ds \
     --set server-host-name:ds1.example.com \
     --set server-port:636 \
     --set "bind-dn:cn=Directory Manager" \
     --set password:secret \
     --set connection-security:ssl \
     --set key-manager-provider:Null \
     --set trust-manager-provider:JKS
   ```

2. Configure the System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
   \<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
   \</div>)* server as an external server, which will later be configured as a Sync Destination. The `scim-service-url` property specifies the complete URL used to access the SCIM service provider. The user-name property specifies the account used to connect to the SCIM service provider. By default, the value is `cn=Sync User,cn=Root DNs,cn=config`. Some SCIM service providers might not have the username in distinguished name (DN) *(tooltip: \<div class="paragraph">
   \<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
   \</div>)* format.

   ```shell
   $ bin/dsconfig create-external-server \
     --server-name scim \
     --type scim \
     --set scim-service-url:https://scim2.example.com:8443 \
     --set "user-name:cn=Sync User,cn=Root DNs,cn=config" \
     --set password:secret \
     --set connection-security:ssl \
     --set hostname-verification-method:strict \
     --set trust-manager-provider:JKS
   ```

---

---
title: Configure the Notification sync pipe
description: The following procedure configures a one-way Sync Pipe with a PingDirectory server as the Sync Source and a generic sync destination. The procedure uses the create-sync-pipe-config tool in interactive command-line mode and highlights the differences for configuring a Sync Pipe in notification mode.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_notif_sync_pipe
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_notif_sync_pipe.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_sync_consids_config_sync_classes.adoc", "pd_sync_create_the_sync_pipe.adoc", "pd_sync_config_sync_source_steps.adoc", "pd_sync_config_dest_endpoint_server.adoc"]
section_ids:
  considerations-for-configuring-sync-classes: Considerations for configuring sync classes
  create-the-sync-pipe: Create the sync pipe
  about-this-task: About this task
  steps: Steps
  configure-the-sync-source: Configure the sync source
  steps-2: Steps
  configure-the-destination-endpoint-server: Configure the destination endpoint server
  steps-3: Steps
  next-steps: Next steps
---

# Configure the Notification sync pipe

The following procedure configures a one-way Sync Pipe with a PingDirectory server as the Sync Source and a generic sync destination. The procedure uses the `create-sync-pipe-config` tool in interactive command-line mode and highlights the differences for configuring a Sync Pipe in notification mode.

## Considerations for configuring sync classes

When configuring a Sync Class for a Sync Pipe in notification mode, consider the following:

* Exclude any operational attributes from synchronizing to the destination so that its before and after values are not recorded in the change log. For example, the following attributes can be excluded: `creatorsName`, `createTimeStamp`, `ds-entry-unique-id`, `modifiersName`, and `modifyTimeStamp`. Filter the changes at the change log level instead of making the changes in the Sync Class to avoid extra configuration settings with the following:

  * Use the directory server's `changelog-exclude-attribute` property with `(+)` to exclude all operational attributes (`change-log-exclude-attribute:+`).

  * Configure a Sync Class that sets the `excluded-auto-mapped-source-attributes` property to each operational attribute to exclude from the synchronization process.

  * Use the directory server's `changelog-exclude-attribute` property to specify each operational attribute to exclude in the synchronization process. Set the configuration using the `dsconfig` tool on the directory server Change Log Backend menu. For example, `setchangelog-exclude-attribute:modifiersName`.

* Use the `destination-create-only-attribute` advanced property on the Sync Class. This property sets the attributes to include on CREATE operations only.

* Use the `replace-all-attr-values` advanced property on the Sync Class. This property specifies whether to use the ADD and DELETE modification types (reversible), or the REPLACE modification type (non-reversible) for modifications to destination entries. If set to `true`, REPLACE is used.

* If targeting specific attributes that require higher performance throughput, consider implementing change log indexing. See [Synchronize through PingDirectoryProxy servers](pd_sync_thru_pdproxy_server.html) for more information.

## Create the sync pipe

### About this task

The initial configuration steps show how to set up a single Sync Pipe from a directory server instance to a generic Sync Destination.

Before starting:

* Place any third-party libraries in the `<server-root>/lib/extensions` folder.

* Implement a server extension for any custom endpoints and place it in the appropriate directory.

### Steps

1. If necessary, start PingDataSync:

   ```shell
   $ bin/start-server
   ```

2. Run the `create-sync-pipe-config` tool.

   ```shell
   $ bin/create-sync-pipe-config
   ```

3. At the Initial Synchronization Configuration Tool prompt, press Enter to continue.

4. On the Synchronization Mode menu, select the option for notification mode.

5. On the Synchronization Directory menu, enter the option to create a one-way Sync Pipe in notification mode from the directory to a generic client application.

## Configure the sync source

### Steps

1. On the Source Endpoint Type menu, enter the option for the Sync Source type.

2. Choose a pre-existing Sync Source, or create a new sync source.

3. Enter a name for the Source Endpoint and a name for the Sync Source.

4. Enter the base distinguished name (DN) *(tooltip: \<div class="paragraph">
   \<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
   \</div>)* for the directory server used for Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
   \<p>An open, cross platform protocol used for interacting with directory services.\</p>
   \</div>)* searches, such as `dc=example,dc=com`, and press Enter to return to the menu. If entering more than one base DN, make sure they do not overlap.

5. On the Server Security menu, select the type of communication that PingDataSync will use with endpoint servers.

6. Enter the host and port of the first Source Endpoint server. The Sync Source can specify a single server or multiple servers in a replicated topology. PingDataSync contacts this first server if it is available, then contacts the next highest priority server if the first server is unavailable. The server tests the connection.

7. On the Sync User Account menu, enter the DN of the sync user account and password, or press Enter to accept the default, `cn=Sync User,cn=Root DNs,cn=config`. This account allows PingDataSync to access the source endpoint server.

## Configure the destination endpoint server

### Steps

1. On the Destination Endpoint Type menu, select the type of datastore on the endpoint server. In this example, select the option for Custom.

2. Enter a name for the Destination Endpoint and a name for the Sync Destination.

3. On the Notifications Setup menu, select the language (Java or Groovy) used to write the server extension.

4. Enter the fully qualified name of the Server SDK extension that implements the abstract class. A Java, extension should reside in the `/lib/extensions` directory. A Groovy script should reside in the `/lib/groovy-scripted-extensions` directory.

5. Configure any user-defined arguments needed by the server extension. Typically, these are connection arguments, which are defined by the extension itself. The values are then entered here and stored in the server configuration.

6. Configure the maximum number of before and after values for all changed attributes. Notification mode requires this. Set the cap to something well above the maximum number of values that any synchronized attribute will have. If this cap is exceeded, PingDataSync issues an alert. For this example, we accept the default value of 200.

   ```
   Enter a value for the max changelog before/after values,
   or -1 for no limit [200]:
   ```

7. Configure any key attributes in the change log that must be included in every notification. These attributes can be used to find the destination entry corresponding to the source entry, and are present regardless of whether the attributes changed. Later, any attributes used in a Sync Class include-filter must also be configured as key attributes in the Sync Class.

8. In both standard and notification modes, the Sync Pipe processes the changes concurrently with multiple threads. If changes must be applied strictly in order, the number of Sync Pipe worker threads will be reduced to 1. This will limit the maximum throughput of the Sync Pipe.

### Next steps

The rest of the configuration steps follow the same process as a standard synchronization mode Sync Pipe. For more information see [Sync user account](pd_sync_user_account.html).

---

---
title: Configure the PingDirectory server backend for synchronizing deletes
description: "The PingDirectory server's change log backend's changelog-deleted-entry-include-attribute property specifies which attributes should be recorded in the change log entry during a DELETE operation. Normally, PingDataSync cannot correlate a deleted entry to the entry on the destination. If a Sync Class is configured with a filter, such as \"include-filter: objectClass=person,\" the objectClass attribute must be recorded in the change log entry. Special correlation attributes (other than DN), will also need to be recorded on the change log entry to be properly synchronized at the endpoint server."
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_ds_backend_sync_deletes
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_ds_backend_sync_deletes.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure the PingDirectory server backend for synchronizing deletes

## About this task

The PingDirectory server's change log backend's `changelog-deleted-entry-include-attribute` property specifies which attributes should be recorded in the change log entry during a DELETE operation. Normally, PingDataSync cannot correlate a deleted entry to the entry on the destination. If a Sync Class is configured with a filter, such as "`include-filter: objectClass=person`," the `objectClass` attribute must be recorded in the change log entry. Special correlation attributes (other than DN), will also need to be recorded on the change log entry to be properly synchronized at the endpoint server.

On each PingDirectory server backend, use the `dsconfig` command to set the property.

```shell
$ bin/dsconfig set-backend-prop --backend-name changelog \
  --set changelog-deleted-entry-include-attribute:objectClass
```

If the destination endpoint is an Oracle/Sun DSEE (or Sun DS) server, the Sun DSEE server does not store the value of the user deleting the entry, specified in the modifiers name attribute. It only stores the value of the user who last modified the entry while it still existed.

To set up a Sun DSEE destination endpoint to record the user who deleted the entry, use the Ping Identity Server SDK to create a plugin, as follows:

## Steps

1. Update the Sun DSEE schema to include a `deleted-by-syncauxiliary` objectclass. It will only be used as a marker objectclass, and not require or allow additional attributes to be present on an entry.

2. Update the Sun DSEE Retro Change Log plugin to include the `deleted-by-sync auxiliary` objectclass as a value for the `deletedEntryAttrs` attribute.

3. Write an `LDAPSyncDestinationPlugin` script that in the `preDelete()` method modifies the entry that is being deleted to include the `deleted-by-sync` objectclass.

4. Update the Sync Class filter that is excluding changes by the Sync User to also include `(!(objectclass=deleted-by-sync))`.

---

---
title: Configure the PingDirectory server sync source
description: Configure the Sync source for the synchronization network. More than one external server can be configured to act as the Sync source for failover purposes. If the source is a PingDirectory server, also configure the following items:
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_pd_sync_source
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_pd_sync_source.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure the PingDirectory server sync source

## About this task

Configure the Sync source for the synchronization network. More than one external server can be configured to act as the Sync source for failover purposes. If the source is a PingDirectory server, also configure the following items:

* Enable the changelog password encryption plugin on any directory server that will receive password modifications. This plugin intercepts password modifications, encrypts the password, and adds an encrypted attribute to the change log entry.

* Configure the `changelog-deleted-entry-include-attribute` property on the changelog backend, so that PingDataSync can record which attributes were removed during a DELETE operation.

Perform the following steps to configure the Sync source:

## Steps

1. Run the `dsconfig` command to configure the external server as the Sync source. Based on the previous example where the PingDirectory server was configured as `source-ds`, run the following command:

   ```shell
   $ bin/dsconfig create-sync-source --source-name source \
     --type ping-identity \
     --set base-dn:dc=example,dc=com \
     --set server:source-ds \
     --set use-changelog-batch-request:true
   ```

2. Enable the change log password encryption plugin on any server that receives password modifications. The encryption key can be copied from the output, if displayed, or accessed from the `<server-root>/bin/sync-pipe-cfg.txt` file, if the `create-sync-pipe-config` tool was used to create the sync pipe.

   ```shell
   $ bin/dsconfig set-plugin-prop \
     --plugin-name "Changelog Password Encryption" \
     --set enabled:true \
     --set changelog-password-encryption-key:<key>
   ```

3. On PingDataSync, set the decryption key used to decrypt the user password value in the change log entries. The key allows the user password to be synchronized to other servers that do not use the same password storage scheme.

   ```shell
   $ bin/dsconfig set-global-sync-configuration-prop \
     --set changelog-password-decryption-key:ej5u9e39pq-68
   ```

4. Configure the `changelog-deleted-entry-include-attribute` property on the changelog backend.

   ```shell
   $ bin/dsconfig set-backend-prop --backend-name changelog \
     --set changelog-deleted-entry-include-attribute:objectClass
   ```

---

---
title: Configure the SCIM 2.0 external server
description: The System for Cross-domain Identity Management (SCIM) 2.0 external server configuration object provides the information that the PingDataSync server needs to connect and authenticate to the SCIM 2.0 service.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_scim2_external_server
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_scim2_external_server.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configure the SCIM 2.0 external server

The System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 external server configuration object provides the information that the PingDataSync server needs to connect and authenticate to the SCIM 2.0 service.

First, you must create an HTTP authentication method that allows the PingDataSync server to authenticate to the SCIM 2.0 server to authorize requests. In most cases, this authentication is an OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* 2.0 bearer token, and you will likely want to obtain that token using the client credentials grant type. This allows you to provide a client ID and client secret to the OAuth authorization server to obtain a bearer token.

In this case, the client secret is sensitive information, so the PingDataSync server uses a passphrase provider to access it, which allows it to be obtained from a variety of sources, like an optionally encrypted file, Amazon Secrets Manager, Azure Key Vault, a CyberArk Conjur instance, or a HashiCorp Vault instance. For example:

```
dsconfig create-passphrase-provider \
     --provider-name "SCIMv2 Client Secret" \
     --type file-based \
     --set enabled:true \
     --set password-file:config/scimv2-client-secret.txt

dsconfig create-http-authorization-method \
     --method-name "SCIMv2 Authorization Method" \
     --type client-credentials-bearer-token \
     --set enabled:true \
     --set oauth-server-token-endpoint-url:https://oauth.example.com/as/token \
     --set hostname-verification-method:strict \
     --set oauth-client-id:this-is-the-client-id \
     --set "oauth-client-secret-passphrase-provider:SCIMv2 Client Secret" \
     --set request-method:get \
     --set credentials-submission-method:basic-authorization \
     --set "maximum-token-lifetime:1 h"
```

The SCIM 2.0 external server configuration offers the following properties:

* `scim-service-url`

  The base URL to the SCIM 2.0 service to be used. This should not include any endpoint name because that will be appended through the endpoint mapping. This is required.

* `key-manager-provider`

  A key manager provider to use during SSL negotiation with the SCIM 2.0 server. This is optional, and it will likely only be used if the PingDataSync server needs to supply a client certificate to the SCIM 2.0 server.

* `ssl-cert-nickname`

  The nickname (alias) of the client certificate to present to the SCIM 2.0 server. This is only needed if a `key-manager-provider` is specified and only if the associated key store has multiple certificates that could be used.

* `trust-manager-provider`

  A trust manager provider to use to determine whether to trust the certificate chain presented by the SCIM 2.0 server during Secure Sockets Layer (SSL) *(tooltip: \<div class="paragraph">
  \<p>A protocol for authenticated and encrypted links between networked machines, typically over HTTPS. SSL was deprecated in 1999 in favor of Transport Layer Security (TLS).\</p>
  \</div>)* negotiation. This is optional, and if you don't specify it, then the PingDataSync server will rely primarily on the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
  \<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
  \</div>)*'s default set of trusted issuers. If the SCIM 2.0 server is using a certificate signed by one of those trusted issuers, then you can leave this property unset.

* `hostname-verification-method`

  Indicates whether the PingDataSync server should verify that the certificate presented by the SCIM 2.0 server is appropriate for the intended address. A value of `strict`, which is the default, indicates that the connection should only be established if the certificate has a subject alternative name extension with a value that matches the address provided in the `scim-service-url` property (or if the certificate does not have a subject alternative name extension, then it falls back to using the `CN` attribute of the certificate subject). A value of `allow-all` indicates that the PingDataSync server should not attempt to confirm that the certificate was issued for the intended server.

* `http-authorization-method`

  The HTTP authorization method that the PingDataSync server should use to authenticate to and authorize requests in the SCIM 2.0 server. This is required.

* `response-timeout`

  The maximum length of time that the PingDataSync server should wait for a response from the SCIM 2.0 server when issuing requests. If this is not specified, a default of 10 seconds is used.

* `client-reconnect-interval`

  The maximum length of time that a SCIM 2.0 client instance will be used before a new one is created, which might potentially include obtaining new credentials. If the client credentials grant HTTP authorization method is used and the OAuth authorization server specified an expiration time for the bearer token that it issued, then the actual reconnect interval is based on the lesser of the two values. If this is not specified, and if the HTTP authorization method does not indicate a maximum lifetime for its credentials, then the same SCIM 2.0 client instance is used indefinitely.

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The server will automatically try to refresh the credentials if the SCIM 2.0 service returns a 401 (unauthorized) error in response to any request. |

For example, you can use the following change to configure a SCIM 2.0 external server:

```
dsconfig create-external-server \
     --server-name "SCIMv2 Server" \
     --type scim2 \
     --set scim-service-url:https://scim2.example.com/scim/v2 \
     --set "http-authorization-method:SCIMv2 Authorization Method"
```

---

---
title: Configure the SCIM 2.0 sync destination
description: The System for Cross-domain Identity Management (SCIM) 2.0 sync destination associates a SCIM 2.0 external server with a set of one or more endpoint mappings and can also specify additional configuration properties.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_scimv2_sync_dest
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_scimv2_sync_dest.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configure the SCIM 2.0 sync destination

The System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 sync destination associates a SCIM 2.0 external server with a set of one or more endpoint mappings and can also specify additional configuration properties.

Available properties include:

* `server`

  The SCIM 2.0 external server to which changes will be synchronized. This is required.

* `endpoint-mapping`

  A set of one or more SCIM 2.0 endpoint mappings to use when synchronizing changes to the SCIM 2.0 server. This is required.

* `query-method`

  The HTTP request method that should be used when querying the SCIM 2.0 server to fetch existing entries. The value can be one of the following:

  * **`get`** – Use the HTTP GET method to submit the query. This is the default value that will be used if the property is not specified.

  * **`post`** – Use the HTTP POST method to submit the query.

* `update-method`

  The HTTP request method that should be used when applying changes to existing SCIM 2.0 entries. The value can be one of the following:

  * **`put`** – Use the HTTP PUT method to replace the entire entry. SCIM 2.0 servers must support this method, but it is less efficient and more risky than using the PATCH method because it has greater potential of losing changes to the entry made by other SCIM 2.0 clients.

  * **`patch`** – Use the HTTP PATCH method to specify which specific changes should be applied to the entry. This method is an optional part of the SCIM 2.0 specification, so it might not be available in all servers, but it is more efficient and safer than the PUT method, so this is the default that will be used if the property is not specified.

You can use the following example configuration change to create a SCIM 2.0 sync destination:

```
dsconfig create-sync-destination \
     --destination-name "SCIMv2 Destination" \
     --type scim2 \
     --set "server:SCIMv2 Server" \
     --set "endpoint-mapping:Users Endpoint"
```

---

---
title: Configure the SCIM sync destination
description: Configure the System for Cross-domain Identity Management (SCIM) sync destination to synchronize data with a SCIM service provider. Run the dsconfig command:
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_scim_sync_dest
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_scim_sync_dest.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configure the SCIM sync destination

Configure the System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* sync destination to synchronize data with a SCIM service provider. Run the `dsconfig` command:

```shell
$ bin/dsconfig create-sync-destination \
  --destination-name scim \
  --type scim \
  --set server:scim
```

---

---
title: Configure the source PingDirectory server
description: The following procedure configures a backend set of directory servers. The procedure is the same for the source servers and the destination servers in a synchronization topology. For directory server installation and configuration details, see the PingDirectory server administration guide.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_source_pd_server
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_source_pd_server.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure the source PingDirectory server

## About this task

The following procedure configures a backend set of directory servers. The procedure is the same for the source servers and the destination servers in a synchronization topology. For directory server installation and configuration details, see the [PingDirectory server administration guide](../pingdirectory_server_administration_guide/pd_ds_amin_guide.html).

## Steps

1. On each backend PingDirectory server that will participate in synchronization, enable the change log database, either from the command line or by using a `dsconfig` batch file.

   ```shell
   $ dsconfig --no-prompt set-backend-prop \
     --backend-name changelog \
     --set enabled:true
   ```

2. Stop the server if it is running, and import the dataset for the first backend set into the first server in the backend set before the import.

   ```shell
   $ bin/stop-server
   $ bin/import-ldif --backendID userRoot --ldifFile ../dataset.ldif
   $ bin/start-server
   ```

3. On the first server instance in the first backend set, configure replication between this server and the second server in the same backend set.

   ```shell
   $ bin/dsreplication enable --host1 ldap-west-01.example.com \
     --port1 389 \
     --bindDN1 "cn=Directory Manager" \
     --bindPassword1 password \
     --replicationPort1 8989 \
     --host2 ldap-west-02.example.com \
     --port2 389 \
     --bindDN2 "cn=Directory Manager" \
     --bindPassword2 password \
     --replicationPort2 9989 \
     --adminUID admin \
     --adminPassword admin \
     --baseDN dc=example,dc=com \
     --no-prompt
   ```

4. Initialize the second server in the backend set with data from the first server in the backend set. This command can be run from either instance.

   ```shell
   $ bin/dsreplication initialize \
     --hostSource ldap-west-01.example.com \
     --portSource 389 \
     --hostDestination ldap-west-02.example.com \
     --portDestination 389 \
     --baseDN "dc=example,dc=com" \
     --adminUID admin \
     --adminPassword admin \
     --no-prompt
   ```

5. Run the following command to check replica status.

   ```shell
   $ bin/dsreplication status \
     --hostname ldap-west-01.example.com \
     --port 389 \
     --adminPassword admin \
     --no-prompt
   ```

6. Repeat steps 2 through 5 (import, enable replication, initialize replication, check status) for the second backend set.

---

---
title: Configure the sync pipe, sync classes, and evaluation order
description: Configure a Sync Pipe for Lightweight Directory Access Protocol (LDAP) to System for Cross-domain Identity Management (SCIM) synchronization, create Sync classes for the Sync Pipe, and set the evaluation order index for the Sync classes.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_sync_pipe_classes_eval
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_sync_pipe_classes_eval.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure the sync pipe, sync classes, and evaluation order

## About this task

Configure a Sync Pipe for Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* to System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* synchronization, create Sync classes for the Sync Pipe, and set the evaluation order index for the Sync classes.

|   |                                                                                               |
| - | --------------------------------------------------------------------------------------------- |
|   | The synchronization mode must be set to standard. Notification mode cannot be used with SCIM. |

## Steps

1. After the source and destination endpoints have been configured, configure the Sync Pipe for LDAP to SCIM synchronization. Run `dsconfig` to configure an LDAP-to-SCIM Sync Pipe:

   ```shell
   $ bin/dsconfig create-sync-pipe \
     --pipe-name ldap-to-scim \
     --set sync-source:source \
     --set sync-destination:scim
   ```

2. The next set of steps define three Sync Classes. The first Sync Class is used to match user entries in the Sync Source. The second class is used to match group entries. The third class is a DEFAULT class that is used to match all other entries.

   Run `dsconfig` to create the first Sync Class and set the Sync Pipe Name and Sync Class name:

   ```shell
   $ bin/dsconfig create-sync-class \
     --pipe-name ldap-to-scim \
     --class-name user
   ```

3. Run `dsconfig` to set the base distinguished name (DN) *(tooltip: \<div class="paragraph">
   \<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
   \</div>)* and filter for this Sync class. The `include-base-dn` property specifies the base DN in the source, which is `ou=people,dc=example,dc=com` by default. This Sync Class is invoked only for changes at the `ou=people` level. The include-filter property specifies an LDAP filter that tells PingDataSync to include `inetOrgPerson` entries as user entries. The `destination-correlation-attributes` specifies LDAP attributes that allow PingDataSync to find the destination resource on the SCIM server. The value of this property will vary. See [Identify a SCIM resource at the destination](pd_sync_identify_scim_resource_dest.html) for details.

   ```shell
   $ bin/dsconfig set-sync-class-prop \
     --pipe-name ldap-to-scim \
     --class-name user \
     --add include-base-dn:ou=people,dc=example,dc=com \
     --add "include-filter:(objectClass=inetOrgPerson)" \
     --set destination-correlation-attributes:externalId
   ```

4. Create a second Sync class, which is used to match group entries:

   ```shell
   $ bin/dsconfig create-sync-class \
     --pipe-name ldap-to-scim \
     --class-name group
   ```

5. For the second Sync class, set the base DN and the filters to match the group entries.

   ```shell
   $ bin/dsconfig set-sync-class-prop \
     --pipe-name ldap-to-scim \
     --class-name group \
     --add include-base-dn:ou=groups,dc=example,dc=com \
     --add "include-filter:(|(objectClass=groupOfEntries)\
       (objectClass=groupOfNames)(objectClass=groupOfUniqueNames)\
       (objectClass=groupOfURLs))"
   ```

6. For the third Sync class, create a DEFAULT Sync class that is used to match all other entries. To synchronize changes from only user and group entries, set `synchronize-creates`, `synchronize-modifies`, and `synchronize-delete` to false.

   ```shell
   $ bin/dsconfig create-sync-class \
     --pipe-name ldap-to-scim \
     --class-name DEFAULT \
     --set evaluation-order-index:99999 \
     --set synchronize-creates:false \
     --set synchronize-modifies:false \
     --set synchronize-deletes:false
   ```

7. After all of the Sync classes needed by the Sync Pipe are configured, set the evaluation order index for each Sync class. Classes with a lower number are evaluated first. Run `dsconfig` to set the evaluation order index for the Sync class. The actual number depends on the deployment.

   ```shell
   $ bin/dsconfig set-sync-class-prop \
     --pipe-name ldap-to-scim \
     --class-name user \
     --set evaluation-order-index:100
   ```

---

---
title: Configure the sync source
description: The sync source describes the service from which entries and changes are read so that they can be synchronized to the sync destination.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_sync_source
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_sync_source.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configure the sync source

The sync source describes the service from which entries and changes are read so that they can be synchronized to the sync destination.

The process for configuring a sync source varies based on the type of service that you use, such as an LDAP server or a relational database, so you should consult the appropriate documentation for the specific type of sync source that you want to use.

Currently, the `create-sync-pipe-config` tool does not offer support for the System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 sync destination, so you might need to configure the sync source manually with a tool like `dsconfig` or the admin console. However, if you plan to synchronize from the desired source to another type of destination, and if that destination is one that is supported by the `create-sync-pipe-config` tool, then you can reuse the sync source created for that pipe.

If the sync source server is a PingDirectory server, then you can use the `prepare-endpoint-server` tool to make necessary changes to allow the PingDataSync server to interact with that directory server instance. This includes creating the account that the PingDataSync server uses to authenticate to the PingDirectory server and enabling the changelog to allow the PingDataSync server to retrieve information about changes processed in the PingDirectory server.

Running `prepare-endpoint-server --help` shows you the complete usage for the tool, but the following example demonstrates a sample usage:

```
bin/prepare-endpoint-server \
     --hostname ds-source.example.com \
     --port 636 \
     --useSSL \
     --trustStorePath config/truststore \
     --syncServerBindDN "cn=Sync User,cn=Root DNs,cn=config" \
     --syncServerBindPasswordFile sync-user-password.txt \
     --baseDN dc=example,dc=com \
     --isSource
```

In addition, if the source server is a PingDirectory server instance, then you should enable the Changelog Password Encryption plugin in that server to indicate that it should store an encrypted representation of clear-text passwords in the changelog along with their encoded form. See [Configuring password encryption](pd_sync_config_password_encryption.html).

Doing this allows the PingDataSync server to retrieve those clear-text passwords so that they can be synchronized to the SCIM 2.0 sync destination. You can do this with a change like the following:

```
dsconfig set-plugin-prop \
     --plugin-name "Changelog Password Encryption" \
     --set enabled:true \
     --set changelog-password-encryption-key:<this-is-the-key-you-want-to-use>
```

---

---
title: "Configure the synchronization environment with <code class=\"cmdname\"><strong>dsconfig</strong></code>"
description: The dsconfig tool can be used to configure any part of PingDataSync, but will likely be used for more fine-grained adjustments. If configuring a Sync Pipe for the first time, use the create-sync-pipe-config tool to guide through the necessary Sync Pipes creation steps.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_sync_env_dsconfig
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_sync_env_dsconfig.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_sync_config_server_groups_dsconfig_interactive.adoc", "pd_sync_start_global_sync_config_dsconfig.adoc"]
section_ids:
  configure-server-groups-with-dsconfig-interactive: Configure server groups with dsconfig interactive
  start-the-global-sync-configuration-with-dsconfig-interactive: Start the Global Sync configuration with dsconfig interactive
  about-this-task: About this task
  steps: Steps
---

# Configure the synchronization environment with `dsconfig`

The `dsconfig` tool can be used to configure any part of PingDataSync, but will likely be used for more fine-grained adjustments. If configuring a Sync Pipe for the first time, use the `create-sync-pipe-config` tool to guide through the necessary Sync Pipes creation steps.

## Configure server groups with `dsconfig` interactive

In a typical deployment, one PingDataSync server and one or more redundant failover servers are configured. Primary and secondary servers must have the same configuration settings to ensure proper operation. To enable this, assign all servers to a server group using the `dsconfig` tool. Any change to one server will automatically be applied to the other servers in the group.

Run the `dsconfig` command and set the global configuration property for server groups to `all-servers`. On the primary PingDataSync server, run the following command:

```shell
$ bin/dsconfig set-global-configuration-prop \
  --set configuration-server-group:all-servers
```

Updates to servers in the group are made using the `--applyChangeTo server-group` option of the `dsconfig` command. To apply the change to one server in the group, use the `--applyChangeTo single-server` option. If additional servers are added to the topology, the `setup` tool will copy the configuration from the primary server to the new servers.

## Start the Global Sync configuration with `dsconfig` interactive

### About this task

After the Synchronization topology is configured, perform the following steps to start the Global Sync configuration, which will use only those Sync Pipes that have been started:

### Steps

1. On the `dsconfig` main menu, type the number corresponding to the Global Sync Configuration.

2. On the Global Sync Configuration menu, type the number corresponding to view and edit the configuration.

3. On the GlobalSync Configuration Properties menu, type the number corresponding to setting the started property, and then follow the prompts to set the value to `TRUE`.

4. On the GlobalSync Configuration Properties menu, type `f` to save and apply the changes.

---

---
title: Configure traffic through a load balancer
description: If a PingDataSync server is sitting behind an intermediate HTTP server, such as a load balancer, a reverse proxy, or a cache, it will log incoming requests as originating with the intermediate HTTP server instead of the client that actually sent the request. If the actual client's IP address should be recorded to the trace log, enable X-Forwarded-* handling in both the intermediate HTTP server and the PingDataSync server. See the product documentation for the device type. For PingDataSync servers:
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_traffic_load_balancer
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_traffic_load_balancer.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configure traffic through a load balancer

If a PingDataSync server is sitting behind an intermediate HTTP server, such as a load balancer, a reverse proxy, or a cache, it will log incoming requests as originating with the intermediate HTTP server instead of the client that actually sent the request. If the actual client's IP address should be recorded to the trace log, enable `X-Forwarded-*` handling in both the intermediate HTTP server and the PingDataSync server. See the product documentation for the device type. For PingDataSync servers:

* Edit the appropriate Connection Handler object (HTTPS or HTTP) and set `use-forwarded-headers` to `true`.

* When `use-forwarded-headers` is set to `true`, the server will use the client IP address and port information in the `X-Forwarded-*` headers instead of the address and port of the entity that's actually sending the request, the load balancer. This client address information will show up in logs where one would normally expect it to show up, such as in the `from` field of the HTTP REQUEST and HTTP RESPONSE messages.

---

---
title: Configuring attribute mapping
description: The following procedure defines an attribute map from the email attribute in the source servers to a mail attribute in the target servers. Both attributes must be valid in the target servers and must be present in their respective schemas.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_attribute_mapping
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_attribute_mapping.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring attribute mapping

## About this task

The following procedure defines an attribute map from the `email` attribute in the source servers to a `mail` attribute in the target servers. Both attributes must be valid in the target servers and must be present in their respective schemas.

|   |                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following can also be done with `dsconfig` in interactive mode. The attribute mapping *(tooltip: \<div class="paragraph">&#xA;\<p>Matching corresponding attributes between an IdP and an SP to identify federated users or add supplemental user information.\</p>&#xA;\</div>)* options are available from the PingDataSync main menu. |

## Steps

1. On PingDataSync, run the `dsconfig` command to create an attribute map for the "SunDS>DS" Sync Class for the "Sun DS to Ping Identity DS" Sync Pipe, and then run the second `dsconfig` command to apply the new attribute map to the Sync Pipe and Sync Class.

   ```shell
   $ bin/dsconfig --no-prompt create-attribute-map \
     --map-name "SunDS>DS Attr Map" \
     --set "description:Attribute Map for SunDS>Ping Identity Sync Class" \
     --port 7389 \
     --bindDN "cn=admin,dc=example,dc=com" \
     --bindPassword secret
   ```

   ```shell
   $ bin/dsconfig --no-prompt set-sync-class-prop \
     --pipe-name "Sun DS to DS" \
     --class-name "SunDS>DS" \
     --set "attribute-map:SunDS>DS Attr Map" \
     --port 7389 \
     --bindDN "cn=admin,dc=example,dc=com" \
     --bindPassword secret
   ```

2. Create an attribute mapping (from `email` to `mail`) for the new attribute map.

   ```shell
   $ bin/dsconfig --no-prompt create-attribute-mapping \
     --map-name "SunDS>DS Attr Map" \
     --mapping-name mail --type direct \
     --set "description:Email>Mail Mapping" \
     --set from-attribute:email \
     --port 7389 \
     --bindDN "cn=admin,dc=example,dc=com" \
     --bindPassword secret
   ```

3. For a bidirectional deployment, repeat steps 1–2 to create an attribute map for the DS>SunDS Sync Class for the Ping Identity DS to Sun DS Sync Pipe, and create an attribute mapping that maps `mail` to `email`.

   ```shell
   $ bin/dsconfig --no-prompt create-attribute-map \
     --map-name "DS>SunDS Attr Map" \
     --set "description:Attribute Map for DS>SunDS Sync Class" \
     --port 7389 \
     --bindDN "cn=admin,dc=example,dc=com" \
     --bindPassword secret
   ```

   ```shell
   $ bin/dsconfig --no-prompt set-sync-class-prop \
     --pipe-name "Ping Identity DS to Sun DS" \
     --class-name "DS>SunDS" \
     --set "attribute-map:DS>SunDS Attr Map" \
     --port 7389 \
     --bindDN "cn=admin,dc=example,dc=com" \
     --bindPassword secret
   ```

   ```shell
   $ bin/dsconfig --no-prompt create-attribute-mapping \
     --map-name "DS>SunDS Attr Map" \
     --mapping-name email \
     --type direct \
     --set "description:Mail>Email Mapping" \
     --set from-attribute:mail \
     --port 7389 \
     --bindDN "cn=admin,dc=example,dc=com" \
     --bindPassword secret
   ```

---

---
title: Configuring log signing
description: PingDirectory servers support the ability to cryptographically sign a log to ensure that it has not been modified. For example, financial institutions require tamper-proof audit logs files to ensure that transactions can be properly validated and ensure that they have not been modified by a third-party entity or internally by an unauthorized person.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_log_signing
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_log_signing.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring log signing

## About this task

PingDirectory servers support the ability to cryptographically sign a log to ensure that it has not been modified. For example, financial institutions require tamper-proof audit logs files to ensure that transactions can be properly validated and ensure that they have not been modified by a third-party entity or internally by an unauthorized person.

When enabling signing for a logger that already exists, the first log file will not be completely verifiable because it still contains unsigned content from before signing was enabled. Only log files whose entire content was written with signing enabled will be considered completely valid. For the same reason, if a log file is still open for writing, then signature validation will not indicate that the log is completely valid because the log will not include the necessary "end signed content" indicator at the end of the file.

To validate log file signatures, use the `validate-file-signature` tool provided in the `bin` directory of the server (or the `bat` directory on Windows systems). After this property has been enabled, disable and then re-enable the log publisher for the changes to take effect.

Perform the following steps to configure log signing:

## Steps

1. Use `dsconfig` to enable log signing for a Log Publisher. In this example, set the `sign-log` property on the File-based Audit Log Publisher.

   ```shell
   $ bin/dsconfig set-log-publisher-prop \
     --publisher-name "File-Based Audit Logger" \
     --set sign-log:true
   ```

2. Disable and then re-enable the Log Publisher for the changes to take effect.

   ```shell
   $ bin/dsconfig set-log-publisher-prop \
     --publisher-name "File-Based Audit Logger" \
     --set enabled:false
   ```

   ```shell
   $ bin/dsconfig set-log-publisher-prop \
     --publisher-name "File-Based Audit Logger" \
     --set enabled:true
   ```

3. To validate a signed file, use the `validate-file-signature` tool to check if a signed file has been altered.

   ```shell
   $ bin/validate-file-signature --file logs/audit
   ```

   ```
   All signature information in file 'logs/audit' is valid
   ```

   If any validation errors occur, a message displays that is similar to this:

   ```
   One or more signature validation errors were encountered while validating
   the contents of file 'logs/audit':
   * The end of the input stream was encountered without encountering the end
   of an active signature block. The contents of this signed block cannot be
   trusted because the signature cannot be verified
   ```

---

---
title: Configuring one way synchronization from Active Directory to PingDirectory
description: Configure a one-way Sync Pipe with the Active Directory (AD) topology as the sync source and a PingDirectory server topology as the Sync Destination.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_configure_sync_pipe_ad
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_configure_sync_pipe_ad.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_sync_ad_with_pd.adoc"]
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  sync_ad_pd: Synchronizing Active Directory with PingDirectory
  modifies-as-creates: modifies-as-creates
---

# Configuring one way synchronization from Active Directory to PingDirectory

Configure a one-way Sync Pipe with the Active Directory (AD) *(tooltip: \<div class="paragraph">
\<p>A directory service for Windows domain networks, included in most Windows Server operation systems.\</p>
\</div>)* topology as the sync source and a PingDirectory server topology as the Sync Destination.

## About this task

Syncing from AD-LDS to PingDirectory is supported for all features except password syncing. For regular AD, password synchronization requires the [Password Sync Agent](pd_sync_password_sync_agent.html).

|   |                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are syncing the `lockoutTime`, `userAccountControl & (ACCOUNTDISABLE == 2)`, or `pwdLastSet` AD attributes, or the AD-LDS `ms-DS-User-Account-Disabled` attribute, see [Synchronizing Active Directory with PingDirectory](#sync_ad_pd). |

## Steps

1. From the `server-root` directory, start PingDataSync.

   ```shell
   $ <server-root>/bin/start-server
   ```

2. To set up the initial synchronization topology, run the `sync` tool.

   ```shell
   $ bin/create-sync-pipe-config
   ```

3. In the **Create Initial Synchronization Configuration** menu, press Enter to continue the configuration.

4. In the **Synchronization Mode** menu, press Enter to accept the default option `1` for `Standard mode`.

5. In the **Synchronization Direction** menu, press Enter to accept the default option `1` for `One way`.

6. In the **Source Endpoint Type** menu, enter option `7` for `Microsoft Active Directory`.

7. In the **Source Endpoint Name** menu, enter a name for the Microsoft AD source server, or press Enter to accept the default value of `Microsoft Active Directory Source`.

8. In the ***\<Source Server>* Server Security** menu, press Enter to accept the default option `1` for `SSL` security.

9. In the ***\<Source Server>* Servers** menu, enter the host name and listener port for Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
   \<p>An open, cross platform protocol used for interacting with directory services.\</p>
   \</div>)* communication with the source server in the format of `<host name>:<port number>` and press Enter.

   The Data Sync server attempts a connection to the AD source server. After adding the first server, you can add additional servers for the source endpoints that will be prioritized below the first server.

10. When you have finished adding servers, press Enter to continue to the next configuration step.

11. In the **Synchronization User Account for *\<Source Server>*** menu, enter a user account distinguished name (DN) *(tooltip: \<div class="paragraph">
    \<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
    \</div>)* for the source servers, or press Enter to accept the default value.

    The account is used exclusively by the Data Sync Server to communicate with the source external servers.

12. Enter a password for the synchronization user account and press Enter.

    |   |                                                                                          |
    | - | ---------------------------------------------------------------------------------------- |
    |   | The User Account DN password must meet the minimum password requirements for AD domains. |

13. In the **Destination Endpoint Type** menu, press Enter to select the default option `1` for `Ping Identity Directory Server`.

14. In the **Destination Endpoint Name** menu, enter a name for your destination endpoint, or press Enter to select the default value, `Ping Identity Directory Server Destination`.

15. In the **Base DNs for *\<Endpoint Server>*** menu, enter a base DN where synchronized entries can be found in your endpoint server, or press Enter to accept the default value.

    After your initial entry, you can add additional base DNs by following the prompts.

16. When you have finished entering base DNs for synchronized entries, press Enter to continue the configuration.

17. In the ***\<Endpoint Server>* Server Security** menu, enter the option for the type of security that the Sync Server will use in communication with the endpoint server and press Enter.

18. In the ***\<Endpoint Server>* Servers** menu, enter the host name and port for LDAP communication in the format of `<host name>:<port number>` and press Enter.

    The PingDataSync server attempts a connection to the destination PingDirectory server endpoint. After adding the first server, you can add additional servers for the destination endpoints that will be prioritized below the first server.

19. When you have finished adding servers, press Enter to continue to the next configuration step.

20. In the **Synchronization User Account for *\<Endpoint Server>*** menu, enter a DN for the synchronization user account that will be used in communication with external servers, or press Enter to accept the default value, `[cn=Sync User,cn=Root DNs,cn=config]`.

21. Enter a password for the synchronization user account and press Enter.

22. In the **Prepare Server *\<Source Server>*** menu, press Enter to accept the default option `1` for `Yes` to prepare the source server for synchronization.

23. In the **Prepare Server *\<Endpoint Server>*** menu, press Enter to accept the default option `1` for `Yes` to prepare the endpoint server for synchronization.

24. In the **Sync Pipe Name** menu, enter a name for the Sync Pipe from the source server (AD) to the endpoint server (PingDirectory server), or press Enter to select the default value, `Microsoft_Active_Directory_Source_to_Ping_Identity_Directory_Server_Destination`.

25. In the **Pre-configured Sync Class Configuration for Active Directory Sync Source** menu, follow the prompts to create the basic sync classes and attribute mappings needed to synchronize user accounts, user passwords, and groups to and from AD.

    1. To synchronize user `Create`, `Modify`, and `Delete` operations from AD, follow the prompts.

    2. Enter the object class for user entries at the endpoint, or press Enter to accept the default value, `inetOrgPerson`.

    3. To configure which password policy state attributes to synchronize, follow the prompts.

       For more information on the AD to PingDirectory password policy state attribute mappings, see [Synchronizing Active Directory with PingDirectory](#sync_ad_pd).

       |   |                                                                                                                                                                                         |
       | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | For the referenced password policy state attributes, AD is treated as the authoritative source, because synchronization from PingDirectory to AD is not supported for those attributes. |

       |   |                                                                                                                                                                               |
       | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | The password policy in PingDirectory must match the password in AD. For example, the `lockout-failure-count` in PingDirectory must match the account lockout threshold in AD. |

    4. To create a DN map for users in the sync pipe, enter `yes` and press Enter. To not create a DN map, press Enter to accept the default option, `no`.

    5. Review the list of basic mappings set up for synchronized user entries and follow the prompts to add any additional attribute mappings. Press Enter to continue.

    6. To synchronize group `Create`, `Modify`, and `Delete` operations from AD, follow the prompts.

26. In the **Sync Pipe Sync Class Definitions** menu, either press Enter to accept the `Microsoft Active Directory Source Users Sync Class`, or enter a value and press Enter to create a new sync class name.

27. Review the **Configuration Summary** and press Enter to write the configuration file as displayed.

    ### Result:

    The server writes the configuration file to a `dsconfig` batch file.

28. To apply the configuration changes to the local PingDataSync server, press Enter. (If you don't want to apply the changes, enter `no` and press Enter.)

## Synchronizing Active Directory with PingDirectory

When you use the `sync-pipe` tool to configure AD *(tooltip: \<div class="paragraph">
\<p>A directory service for Windows domain networks, included in most Windows Server operation systems.\</p>
\</div>)* or AD-LDS as a one-way sync with PingDirectory, three AD password policy state attributes require user input to map to a corresponding PingDirectory attribute.

The following table shows these three attributes, the intermediate attribute that is formed between PingDirectory and AD (or AD-LDS), and the extended operation type used by the PingDirectory server to apply the change.

| AD and AD-LDS attribute                                                                                                      | Intermediate attribute            | PingDirectory attribute   | PasswordPolicyStateOperation opType  |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------------------------- | ------------------------------------ |
| `lockoutTime`                                                                                                                | `pwdAccountLockedTimeFromAD`      | `pwdAccountLockedTime`    | `OP_TYPE_SET_AUTH_FAILURE_TIMES`     |
| `userAccountControl & (ACCOUNTDISABLE == 2)`&#xA;&#xA;In AD-LDS, the corresponding attribute is ms-DS-User-Account-Disabled. | `ds-pwp-account-disabled-from-ad` | `ds-pwp-account-disabled` | `OP_TYPE_SET_ACCOUNT_DISABLED_STATE` |
| `pwdLastSet`                                                                                                                 | `pwdChangedTimeFromAD`            | `pwdChangedTime`          | `OP_TYPE_SET_PW_CHANGED_TIME`        |

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Intermediate attributes only exist in memory on the PingDataSync server so that they can be consumed for attribute mappings. They don't exist on either the AD server or on the PingDirectory server. |

### `modifies-as-creates`

By default, the `modifies-as-creates` sync class property is set to `false`.

Active Directory attributes might not be synchronized as expected when the following is true:

* You are using the `realtime-sync` tool.

* The `modifies-as-creates` sync class property is set to `true`.

* A modification is detected on the source endpoint to a missing entry on the destination endpoint.

* The modification is to attributes other than the three AD password policy state attributes previously mentioned.

To avoid this known issue, you can run the `resync` tool instead of the `realtime-sync` tool. Using `resync` will correctly copy all attributes. For more information, see [The `resync` command](pd_sync_resync_tool.html).

---

---
title: Configuring password encryption
description: You must follow this procedure when synchronizing passwords from a PingDirectory server to Active Directory (AD), or when synchronizing clear text passwords.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_password_encryption
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_password_encryption.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 22, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Configuring password encryption

You must follow this procedure when synchronizing passwords from a PingDirectory server to Active Directory (AD), or when synchronizing clear text passwords.

## About this task

These steps aren't required for the following scenarios:

* Synchronizing from AD to a PingDirectory server

* Excluding password synchronization

## Steps

1. On the PingDirectory server that will receive the password modifications, enable the Change Log Password Encryption component. The component intercepts password modifications, encrypts the password and adds an encrypted attribute, `ds-changelog- encrypted-password`, to the change log entry. The encryption key can be copied from the output if displayed, or accessed from the `<serverroot>/bin/sync-pipe-cfg.txt` file.

   ```shell
   $ bin/dsconfig set-plugin-prop --plugin-name "Changelog Password
   Encryption" \
     --set enabled:true \
     --set changelog-password-encryption-key:<key>
   ```

2. On PingDataSync, set the decryption key used to decrypt the user password value in the change log entries. The key allows the user password to be synchronized to other servers that do not use the same password storage scheme.

   ```shell
   $ bin/dsconfig set-global-sync-configuration-prop \
     --set changelog-password-decryption-key:ej5u9e39pqo68
   ```

## Next steps

Test the configuration or populate data in the destination servers using the [bulk comparison capability of the resync tool](pd_sync_pds_operations.html#bulk_resync). Then, use the `realtime-sync` tool to start synchronizing the data.

|   |                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To synchronize passwords from PingDirectory to AD, you must use the `realtime-sync` tool. The `resync` tool isn't supported for this operation. |

---

---
title: Configuring server locations
description: PingDataSync supports endpoint failover, which is configurable using the location property on the external servers. By default, the server prefers to connect to, and failover to, endpoints in the same location as itself. If there are no location settings configured, PingDataSync will iterate through the configured list of external servers on the Sync Source and Sync Destination when failing over.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_server_locations
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_server_locations.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring server locations

## About this task

PingDataSync supports endpoint failover, which is configurable using the `location` property on the external servers. By default, the server prefers to connect to, and failover to, endpoints in the same location as itself. If there are no location settings configured, PingDataSync will iterate through the configured list of external servers on the Sync Source and Sync Destination when failing over.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | Location-based failover is only applicable for LDAP endpoint servers. |

## Steps

1. On PingDataSync, run the `dsconfig` command to set the location for each external server in the Sync Source and Sync Destination. For example, the following command sets the location for six servers in two data centers, `austin` and `dallas`.

   ```shell
   $ bin/dsconfig set-external-server-prop \
     --server-name example.com:1389 \
     --set location:austin
   ```

   ```shell
   $ bin/dsconfig set-external-server-prop \
     --server-name example.com:2389 \
     --set location:austin
   ```

   ```shell
   $ bin/dsconfig set-external-server-prop \
     --server-name example.com:3389 \
     --set location:austin
   ```

   ```shell
   $ bin/dsconfig set-external-server-prop \
     --server-name example.com:4389 \
     --set location:dallas
   ```

   ```shell
   $ bin/dsconfig set-external-server-prop \
     --server-name example.com:5389 \
     --set location:dallas
   ```

   ```shell
   $ bin/dsconfig set-external-server-prop \
     --server-name example.com:6389 \
     --set location:dallas
   ```

2. Run `dsconfig` to set the location on the Global Configuration. This is the location of PingDataSync itself. In this example, set the location to `austin`.

   ```shell
   $ bin/dsconfig set-global-configuration-prop \
     --set location:austin
   ```
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
title: Active Directory sync user account
description: The Sync User created for Active Directory (AD) is added to the cn=Administrators branch and is given most of a root user's permissions. If this account cannot be secured and there is a need to configure the permissions required by the Sync User, the following are required to perform synchronization tasks.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_active_dir_sync_user_acct
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_active_dir_sync_user_acct.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Active Directory sync user account

The Sync User created for Active Directory (AD) *(tooltip: \<div class="paragraph">
\<p>A directory service for Windows domain networks, included in most Windows Server operation systems.\</p>
\</div>)* is added to the `cn=Administrators` branch and is given most of a root user's permissions. If this account cannot be secured and there is a need to configure the permissions required by the Sync User, the following are required to perform synchronization tasks.

As a Sync Source, these permissions are needed:

* List contents

* Read all properties

* Read permissions

Deleted items are a special case. For the PingDataSync server to see deleted entries, the user account must have sufficient access to `cn=Deleted Objects,<domain name>`. Giving access to that distinguished name (DN) *(tooltip: \<div class="paragraph">
\<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
\</div>)* requires using the `dsacls` tool, such as:

```
# Take ownership may be required to make the needed changes.
dsacls "CN=Deleted Objects,DC=example,DC=com" /takeOwnership
```

```
# Give the Sync User generic read permission to the domain.
dsacls "CN=Deleted Objects,DC=example,DC=com" /G "example\SyncUser":GR
```

```
# List the permission for the domain.
dsacls "CN=Deleted Objects,DC=example,DC=com"
```

To revoke all permissions from the Sync User, run the following `dsacls` command:

```
dsacls "CN=Deleted Objects,DC=example,DC=com" /R "example\SyncUser"
```

If Active Directory is used as a destination for synchronization, the Sync User account should not be changed.

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
title: Change the synchronization state by a specific time duration
description: The following command will start synchronizing data at the state that occurred 2 hours and 30 minutes before the current time on External Server 1 for Sync Pipe 1. Any changes made before this time will not be synchronized. Specify days (d), hours (h), minutes (m), seconds (s), or milliseconds (ms).
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_change_sync_state_time_dur
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_change_sync_state_time_dur.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Change the synchronization state by a specific time duration

The following command will start synchronizing data at the state that occurred 2 hours and 30 minutes before the current time on External Server 1 for Sync Pipe 1. Any changes made before this time will not be synchronized. Specify days (d), hours (h), minutes (m), seconds (s), or milliseconds (ms).

Use `realtime-sync` with the `--startpoint-rewind` option to set the synchronization state and begin synchronizing at the specified time.

```shell
$ bin/realtime-sync set-startpoint \
  --startpoint-rewind 2h30m \
  --pipe-name "Sync Pipe 1" \
  --bindPassword secret \
  --no-prompt
```

---

---
title: Changelog synchronization considerations
description: If the Sync Source is configured with use-changelog-batch-request=true, PingDataSync will use the get changelog batch request to retrieve changes from the Lightweight Directory Access Protocol (LDAP) changelog. This extended request can contain an optional set of selection criteria, which specifies changelog entries for a specific set of attributes.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_changelog_sync_consids
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_changelog_sync_consids.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Changelog synchronization considerations

If the Sync Source is configured with `use-changelog-batch-request=true`, PingDataSync will use the get changelog batch request to retrieve changes from the Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* changelog. This extended request can contain an optional set of selection criteria, which specifies changelog entries for a specific set of attributes.

PingDataSync takes the union of the source attributes from PingDataSync distinguished name (DN) *(tooltip: \<div class="paragraph">
\<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
\</div>)* mappings, attribute mappings, and the `auto-mapped-source-attributes` property on the Sync Class to create the selection criteria. However, if it encounters the value "-all-" in the `auto-mapped-source-attributes` property, it cannot make use of selection criteria because the Sync Pipe is interested in all possible source attributes.

When the PingDirectory server receives a get changelog request that contains selection criteria, it returns changelog entries for one or more of the attributes that meet the criteria.

* For ADD and MODIFY changelog entries, the changes must include at least one attribute from the selection criteria.

* For MODDN changelog entries, one of the RDN attributes must match the selection criteria.

* For DELETE changelog entries, one of the `deletedEntryAttrs` much match the selection criteria.

If `auto-mapped` is not set to `all` source attributes, at least one should be configured to show up in the `deletedEntryAttrs` (with the `changelog-deleted-entry-include-attribute` property on the changelog backend).

Another way to do this is to set `use-reversible-form` to `true` on the changelog backend. This includes all attributes in the `deletedEntryAttrs`.

---

---
title: Changing the administrative password
description: Users that authenticate to the Configuration API or the admin console are stored in cn=RootDNs,cn=config. The setup tool automatically creates one administrative account when performing an installation. Accounts can be added or changed with the dsconfig tool.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_change_admin_password
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_change_admin_password.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Changing the administrative password

Users that authenticate to the Configuration API or the admin console are stored in `cn=RootDNs,cn=config`. The `setup` tool automatically creates one administrative account when performing an installation. Accounts can be added or changed with the `dsconfig` tool.

## About this task

Root users are governed by the Root Password Policy and by default, their passwords never expire. However, if a root user's password must be changed, use the `ldappasswordmodify` tool.

## Steps

1. Open a text editor and create a text file containing the new password. In this example, name the file rootuser.txt.

   ```shell
   $ echo password > rootuser.txt
   ```

2. Use `ldappasswordmodify` to change the root user's password.

   ```shell
   $ bin/ldappasswordmodify --port 1389 --bindDN "cn=Directory Manager" \
   --bindPassword secret --newPasswordFile rootuser.txt
   ```

3. Remove the text file.

   ```shell
   $ rm rootuser.txt
   ```

---

---
title: Composed complex SCIM 2.0 attribute mappings
description: Composed complex System for Cross-domain Identity Management (SCIM) 2.0 attribute mappings can be used to create a single-valued complex attribute in which the sub-attributes are created from other SCIM 2.0 attribute mappings.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_composed_complex_scim2_attr_map
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_composed_complex_scim2_attr_map.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Composed complex SCIM 2.0 attribute mappings

Composed complex System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 attribute mappings can be used to create a single-valued complex attribute in which the sub-attributes are created from other SCIM 2.0 attribute mappings.

For example, the `name` complex attribute described in [RFC 7643 section 8.7.1](https://datatracker.ietf.org/doc/html/rfc7643#section-8.7.1) can have sub-attributes, such as `formatted`, `familyName`, and `givenName`, that might correspond to the `cn`, `sn`, and `givenName` Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* attributes. If you had SCIM 2.0 attribute mappings defined for each of those attributes, then you could use a composed complex SCIM 2.0 attribute mapping that uses those mappings to construct an appropriate value for the name complex attribute.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because the order in which values are presented in multivalued LDAP attributes is not considered significant, you can only use composed complex SCIM 2.0 attribute mappings to generate single-valued complex attributes. If you need a multivalued complex attribute, use the JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">&#xA;\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>&#xA;\</div>)*-formatted complex SCIM 2.0 attribute mapping type. |

Additional configuration properties that are available for composed complex SCIM 2.0 attribute mappings include:

* `sub-attribute-mapping`

  A reference to one or more attribute mappings for the sub-attributes to include in the complex attribute. This is required.

You can use the following example configuration change to create a composed complex SCIM 2.0 attribute mapping:

```
dsconfig create-scim2-attribute-mapping \
     --mapping-name "name Complex Attribute" \
     --type composed-complex \
     --set scim-attribute-name:name\
     --set attribute-usage:fetch \
     --set attribute-usage:create-during-realtime-sync \
     --set attribute-usage:create-during-resync
     --set attribute-usage:update-during-realtime-sync \
     --set attribute-usage:update-during-resync \
     --set "sub-attribute-mapping:Formatted Name" \
     --set "sub-attribute-mapping:First Name" \
     --set "sub-attribute-mapping:Last Name"
```

---

---
title: Conditions that trigger immediate failover
description: Immediate failover occurs when PingDataSync receives one of the following error codes from an external server:
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_conditions_trigger_immed_failover
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_conditions_trigger_immed_failover.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Conditions that trigger immediate failover

Immediate failover occurs when PingDataSync receives one of the following error codes from an external server:

* BUSY (51)

* UNAVAILABLE (52)

* SERVER CONNECTION CLOSED (81)

* CONNECT ERROR (91)

If PingDataSync attempts a write operation to a target server that returns one of these error codes, PingDataSync will automatically fail over to the server instance with the next-highest priority in the target topology, issue an alert, and then reissue the retry attempt. If the operation is unsuccessful for any reason, the server logs an error.

---

---
title: Configuration checklist
description: Before any deployment, determine the configuration parameters necessary for the synchronization topology.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_checklist
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_checklist.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  external-servers: External servers
  sync-pipes: Sync Pipes
  sync-classes: Sync Classes
---

# Configuration checklist

Before any deployment, determine the configuration parameters necessary for the synchronization topology.

For a better configuration experience, gather the following information before you start your configuration.

## External servers

|   |                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | As a best practice, external server definitions should not point at load balancers. Instead, direct connections should be made to the required systems. |

* External server type

  Determine the type of external servers included in the synchronization topology. Supported servers include:

  * PingDirectory server

  * PingDirectoryProxy server

  * Sun Directory Server Enterprise Edition

  * Sun Directory Server

  * Oracle Unified Directory

  * OpenDJ

  * Microsoft Active Directory (AD) *(tooltip: \<div class="paragraph">
    \<p>A directory service for Windows domain networks, included in most Windows Server operation systems.\</p>
    \</div>)*

  * Generic LDAP directories

* LDAP connection settings

  Determine the following for each external server instance included in the synchronization topology:

  * Host

  * Port

  * Bind distinguished name (DN)

  * Bind password

* Security and authentication settings

  Determine the following:

  * The secure connection types for each external server, such as SSL or StartTLS

  * The authentication methods for external servers, such as simple authentication or external SASL mechanisms

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are synchronizing encoded passwords or clear-text passwords in particular, the connection should be secure. To synchronize to or from a Microsoft AD system, establish an SSL or StartTLS connection to PingDataSync. You should also enable password encryption for synchronization from AD or when synchronizing clear-text passwords. For more information, see [Configuring password encryption](pd_sync_config_password_encryption.html). |

## Sync Pipes

A `Sync Pipe` defines a single synchronization path between the source and destination targets. One `Sync Pipe` is needed for each point-to-point synchronization path defined for a topology.

* `Sync Source`

  Determine which external server is the `Sync Source` for the synchronization topology. You can define a prioritized list of external servers for failover purposes.

* `Sync Destination`

  Determine which external server is the `Sync Destination` for the synchronization topology. You can define a prioritized list of external servers for failover purposes.

## Sync Classes

A `Sync Class` defines how attributes and DNs are mapped and how source and destination entries are correlated. For each `Sync Pipe` defined, define one or more `Sync Classes` with the following information:

* Evaluation order

  If you are defining more than one `Sync Class`, the evaluation order of each `Sync Class` must be determined with the `evaluation-order-index` property. If there is an overlap between criteria used to identify a `Sync Class`, the `Sync Class` with the most specific criteria is used first.

* Base DNs

  Determine which base DNs contain entries needed in the `Sync Class`.

* Include filters

  Determine the filters to be used to search for entries in the `Sync Source`.

* Synchronized entry operations

  Determine which operations to synchronize:

  * `create`

  * `modify`

  * `delete`

* DNs

  Determine the differences between the DNs from the `Sync Source` topology to the `Sync Destination` topology. For example, if there are structural differences in each directory information tree (DIT).

* Destination correlation attributes

  Determine the correlation attributes used to associate a source entry to a destination entry during synchronization. During the configuration setup, one or more comma-separated lists of destination correlation attributes are defined and used to search for corresponding source entries. PingDataSync maps all attributes in a detected change from source to destination attributes using the attribute maps defined in the `Sync Class`.

The correlation attributes are flexible enough that several destination searches with different combinations of attributes can be performed until an entry matches. For LDAP server endpoints, use the DN to correlate entries.

For example, to correlate entries in LDAP deployments, specify the attribute lists `dn,uid`, `uid,employeeNumber` and `cn,employeeNumber`. PingDataSync searches for a corresponding entry that has the same `dn` and `uid` values. If the search fails, it then searches for `uid` and `employeeNumber`. If that search fails, it searches for `cn` and `employeeNumber`. If none of these searches are successful, the synchronization change is aborted and a message is logged.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To prevent incorrect matches, the most restrictive attribute lists (those that will never match the wrong entry) should be first in the list, followed by less restrictive attribute lists, which are used when the earlier lists fail. For LDAP-to-LDAP deployments, use the DN with a combination of other unique identifiers in the entry to guarantee correlation. For non-LDAP deployments, determine the attributes that can be synchronized across the network. |

* Attributes

  Determine the differences between the attributes from the `Sync Source` to the `Sync Destination`.

| Attribute consideration                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attribute mappings                     | Determine how attributes are mapped from the `Sync Source` to the `Sync Destination`.For example, if they're mapped directly, mapped based on attribute values, or mapped based on attributes that store DN values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Automatically mapped source attributes | Determine if there are attributes that can be automatically synchronized with the same name at the `Sync Source` to `Sync Destination`.For example, if you can set direct mappings for `cn`, `uid`, `telephoneNumber`, or for all attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Non-auto mapped source attributes      | Determine if there are attributes that shouldn't be automatically mapped.For example, the `Sync Source` might have an attribute, `employee`, while the `Sync Destination` has a corresponding attribute, `employeeNumber`. If an attribute isn't automatically mapped, you must provide a map to synchronize it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Conditional value mapping              | Determine if some mappings should only be applied some of the time as a function of the source attributes.&#xA;&#xA;You can use conditional value mappings with the conditional-value-pattern property, which conditionalizes the attribute mapping based on the subtype of the entry, or on the value of the attribute.For example, this might apply if the `adminName` attribute on the destination should be a copy of the `name` attribute on the source, but only if the `isAdmin` attribute on the source is set to `true`. Conditional mappings are multivalued. Each value is evaluated until one is matched (the condition is `true`). If none of the conditional mappings are matched, the ordinary mappings is used. If there isn't an ordinary mapping, the attribute is not created on the destination. |

---

---
title: Configuration components
description: PingDataSync supports the following configuration parameters that determine how synchronization takes place between directories or databases:
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_components
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_components.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configuration components

PingDataSync supports the following configuration parameters that determine how synchronization takes place between directories or databases:

* Sync pipe

  Defines a single synchronization path between the source and destination topologies. Every Sync Pipe has one or more Sync Classes that control how and what is synchronized. Multiple Sync Pipes can run in a single server instance.

* Sync source

  Defines the directory topology that is the source of the data to be synchronized. A Sync Source can reference one or more supported external servers.

* Sync destination

  Defines the topology of directory servers where changes detected at the Sync Source are applied. A Sync Destination can reference one or more external servers.

* External server

  Defines a single server in a topology of identical, replicated servers to be synchronized. A single external server configuration object can be referenced by multiple Sync Sources and Sync Destinations

* Sync class

  Defines the operation types and attributes that are synchronized, how attributes and DNs are mapped, and how source and destination entries are correlated. A source entry is in one Sync Class and is determined by a base DN and LDAP filters. A Sync Class can reference zero or more Attribute Maps and DN Maps, respectively. Within a Sync Pipe, a Sync Class is defined for each type of entry that needs to be treated differently, such as entries that define attribute mappings, or entries that should not be synchronized at all. A Sync Pipe must have at least one Sync Class but can refer to multiple Sync Class objects.

* DN map

  Defines mappings for use when destination DNs differ from source DNs. These mappings allow the use of wild cards for DN transformations. A single wild card ("\*") matches a single RDN component and can be used any number of times. The double wild card ("\*\*") matches zero or more RDN components and can be used only once. The wild card values can be used in the `to-dn-pattern` attribute using `{1}` and their original index position in the pattern, or `{attr}` to match an attribute value. For example:

  ```
  **,dc=myexample,dc=com->{1},o=example
  ```

  Regular expressions and attributes from the user entry can also be used. For example, the following mapping constructs a value for the `uid` attribute, which is the RDN, out of the initials (first letter of `givenname` and `sn`) and the employee ID (`eid` attribute).

  ```
  uid={givenname:/^(.)(.*)/$1/s}{sn:/^(.)(.*)/$1/s}{eid},{2},o=example
  ```

  The following figure illustrates how a nested DIT can be mapped to a flattened structure.

  A diagram illustrating the mapping of a nested DIT to a flattened structure.

* Attribute map and attribute mappings

  Defines a mapping for use when destination attributes differ from source attributes. A Sync Class can reference multiple attribute maps. Multiple Sync Classes can share the same attribute map. There are three types of attribute mappings:

  * Direct mapping: Attributes are directly mapped to another attribute: For example:

    ```
    employeenumber->employeeid
    ```

  * Constructed mapping: Destination attribute values are derived from source attribute values and static text. For example:

    ```json
    {givenname}.{sn}@example.com->mail
    ```

  * DN mapping: Attributes are mapped for DN attributes. The same DN mappings that map entry DNs can be referenced. For example:

    ```
    uid=jdoe,ou=People,dc=example,dc=com.
    ```

  * Reference attribute mapping: Allows you to synchronize attributes that reference other entries.

    1. The source attribute references another entry on the source.

    2. The source reference entry gets correlated to a reference entry on the destination.

    3. The final attribute value on the destination gets constructed using data from that referenced destination entry.

    You configure key-value properties to build these correlations and extract the necessary data from the relevant entries. Learn more in [About attribute mappings](pd_sync_about_attr_mapping.html).

    |   |                                                                                                                                                                                             |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | This feature is provided as a **Preview**, which means that it isn't supported and should not be used in production environments. Learn more in [Feature statuses](../feature_status.html). |

---

---
title: Configuration properties that control failover behavior
description: There are four important advanced properties to fine tune the failover mechanism:
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_props_ctrl_failover_behavior
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_props_ctrl_failover_behavior.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configuration properties that control failover behavior

There are four important advanced properties to fine tune the failover mechanism:

* `max-operation-attempts` (Sync Pipe)

* `response-timeout` (source and destination endpoints)

* `max-failover-error-code-frequency` (source and destination endpoints)

* `max-backtrack-replication-latency` (source endpoints only)

These properties apply to the following LDAP error codes:

**LDAP Error Codes**

| Error Code                                   | Description                                                                                                            |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ADMIN\_LIMIT\_EXCEEDED(11)                   | Indicates that processing on the requested operation could not continue, because an administrative limit was exceeded. |
| ALIAS\_DEREFERENCING\_PROBLEM(36)            | Indicates that a problem was encountered while attempting to dereference an alias for a search operation.              |
| CANCELED(118)                                | Indicates that a cancel request was successful, or that the specified operation was canceled.                          |
| CLIENT\_SIDE\_LOCAL\_ERROR(82)               | Indicates that a local (client-side) error occurred.                                                                   |
| CLIENT\_SIDE\_ENCODING\_ERROR(83)            | Indicates that an error occurred while encoding a request.                                                             |
| CLIENT\_SIDE\_DECODING\_ERROR(84)            | Indicates that an error occurred while decoding a request.                                                             |
| CLIENT\_SIDE\_TIMEOUT(85)                    | Indicates that a client-side timeout occurred.                                                                         |
| CLIENT\_SIDE\_USER\_CANCELLED(88)            | Indicates that a user canceled a client-side operation.                                                                |
| CLIENT\_SIDE\_NO\_MEMORY(90)                 | Indicates that the client could not obtain enough memory to perform the requested operation.                           |
| CLIENT\_SIDE\_CLIENT\_LOOP(96)               | Indicates that a referral loop was detected.                                                                           |
| CLIENT\_SIDE\_REFERRAL\_LIMIT\_EXCEEDED(97)  | Indicates that the referral hop limit was exceeded.                                                                    |
| DECODING\_ERROR(84)                          | Indicates that an error occurred while decoding a response.                                                            |
| ENCODING\_ERROR(83)                          | Indicates that an error occurred while encoding a response.                                                            |
| INTERACTIVE\_TRANSACTION\_ ABORTED(30221001) | Indicates that an interactive transaction was aborted.                                                                 |
| LOCAL\_ERROR(82)                             | Indicates that a local error occurred.                                                                                 |
| LOOP\_DETECT(54)                             | Indicates that a referral or chaining loop was detected while processing a request.                                    |
| NO\_MEMORY(90)                               | Indicates that not enough memory could be obtained to perform the requested operation.                                 |
| OPERATIONS\_ERROR(1)                         | Indicates that an internal error prevented the operation from being processed properly.                                |
| OTHER(80)                                    | Indicates that an error occurred that does not fall into any of the other categories.                                  |
| PROTOCOL\_ERROR(2)                           | Indicates that the client sent a malformed or illegal request to the server.                                           |
| TIME\_LIMIT\_EXCEEDED(3)                     | Indicates that a time limit was exceeded while attempting to process the request.                                      |
| TIMEOUT(85)                                  | Indicates that a timeout occurred.                                                                                     |
| UNWILLING\_TO\_PERFORM(53)                   | Indicates that the server is unwilling to perform the requested operation.                                             |

---

---
title: "Configuration with the <code class=\"cmdname\"><strong>dsconfig</strong></code> tool"
description: The Ping Identity servers provide several command-line tools for management and administration. The command-line tools are available in the bin directory for UNIX or Linux systems and in the bat directory for Microsoft Windows systems.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_with_dsconfig_tool
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_with_dsconfig_tool.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configuration with the `dsconfig` tool

The Ping Identity servers provide several command-line tools for management and administration. The command-line tools are available in the `bin` directory for UNIX or Linux systems and in the `bat` directory for Microsoft Windows systems.

The `dsconfig` tool is the text-based management tool used to configure the underlying server configuration. The tool has three operational modes:

* Interactive mode

* Non-interactive mode

* Batch mode

The `dsconfig` tool also offers an offline mode using the `--offline` option, in which the server does not have to be running to interact with the configuration. In most cases, the configuration should be accessed with the server running in order for the server to give the user feedback about the validity of the configuration.

Each command-line utility provides a description of the subcommands, arguments, and usage examples needed to run the tool. View detailed argument options and examples by typing `-- help` with the command.

```shell
$ bin/dsconfig --help
```

To list the subcommands for each command:

```shell
$ bin/dsconfig --help-subcommands
```

To list more detailed subcommand information:

```shell
$ bin/dsconfig list-log-publishers --help
```

---

---
title: Configure a directory-to-database sync pipe
description: The following topics contain procedures that let you configure a one-way Sync Pipe with a PingDirectory Server as the Sync Source and an RDBMS (Oracle) system as the Sync Destination with the create-sync-pipe-config tool. You can configure Sync Pipes later using the dsconfig command.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_dir_database_sync_pipe
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_dir_database_sync_pipe.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_sync_create_sync_pipe.adoc", "pd_sync_configure_sync_pipe_classes.adoc"]
section_ids:
  creating-the-sync-pipe: Creating the sync pipe
  configure-the-sync-source: Configure the sync source
  configure-the-destination-endpoint-server: Configure the destination endpoint server
  configuring-the-sync-pipe-and-sync-classes: Configuring the sync pipe and sync classes
  configure-the-accounts-sync-class: Configure the accounts Sync Class
  configure-the-groups-sync-class: Configure the groups Sync Class
---

# Configure a directory-to-database sync pipe

The following topics contain procedures that let you configure a one-way Sync Pipe with a PingDirectory Server as the Sync Source and an RDBMS (Oracle) system as the Sync Destination with the `create-sync-pipe-config` tool. You can configure Sync Pipes later using the `dsconfig` command.

## Creating the sync pipe

The following procedures configure the Sync Pipe, external servers, and Sync Classes. The examples are based on the Complex JDBC sample in the `config/jdbc/samples/oracle-db` directory. The `create-sync-pipe-config` tool can be run with the server offline and the configuration can later be imported.

1. Run the `create-sync-pipe-config` tool.

   `$ bin/create-sync-pipe-config`

2. At the `Initial Synchronization Configuration Tool` prompt, press Enter to continue.

3. On the **Synchronization Mode** menu, select **Standard Mode** or **Notification Mode**.

4. On the **Synchronization Directory** menu, choose one-way or bidirectional synchronization.

### Configure the sync source

1. On the **Source Endpoint Type** menu, enter the number for the sync source corresponding to the type of source external server.

2. Enter a name for the **Source Endpoint**.

3. Enter the base distinguished name (DN) *(tooltip: \<div class="paragraph">
   \<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
   \</div>)* for the directory server, which is used as the base for Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
   \<p>An open, cross platform protocol used for interacting with directory services.\</p>
   \</div>)* searches. For example, enter `dc=example,dc=com`, and then press Enter again to return to the menu. If entering more than one base DN, make sure the DNs do not overlap.

4. On the **Server Security** menu, select the type of communication that PingDataSync will use with the endpoint servers.

5. Enter the host and port of the source endpoint server. The Sync Source can specify a single server or multiple servers in a replicated topology. The server tests that a connection can be established.

6. Enter the DN of the Sync User account and create a password for this account. The Sync User account enables PingDataSync to access the source endpoint server. By default, the Sync User account is stored as `cn=SyncUser,cn=RootDNs,cn=config`.

### Configure the destination endpoint server

1. On the **Destination Endpoint Type** menu, select the type of datastore on the endpoint server. This example is configuring an Oracle Database.

2. Enter a name for the **Destination Endpoint**.

3. On the **JDBC Endpoint Connection Parameters** menu, enter the fully-qualified host name or IP address for the Oracle database server.

4. Enter the listener port for the database server, or press Enter to accept the default (1521).

5. Enter a database name such as `dbsync-test`.

6. The server attempts to locate the JDBC driver in the `lib` directory. If the file is found, a success message is shown.

   ```
   Successfully found and loaded JDBC driver for:
   jdbc:oracle:thin:@//dbsync-w2k8-vm-2:1521/dbsync-test
   ```

   If the server cannot find the JDBC driver, add it later, or quit the `create-sync-pipe-config` tool and add the file to the `lib` directory.

7. Add any additional Java database connectivity (JDBC) *(tooltip: \<div class="paragraph">
   \<p>A Java API that allows Java programs to interact with databases.\</p>
   \</div>)* connection properties for the database server, or press Enter to accept the default (no). Consult the JDBC driver's vendor documentation for supported properties.

8. Enter a name for the database user account with which PingDataSync will communicate, or press Enter to accept the default (SyncUser). Enter the password for the account.

9. On the Standard Setup menu, enter the number for the language (Java or Groovy) that was used to write the server extension.

10. Enter the fully qualified name of the Server SDK extension class that implements the `JDBCSyncDestination` API.

    ```
    Enter the fully qualified name of the Java class that will implement
    com.unboundid.directory.sdk.sync.api.JDBCSyncDestination:
    com.unboundid.examples.oracle.ComplexJDBCSyncDestination
    ```

11. Configure any user-defined arguments needed by the server extension. These are defined in the extension itself and the values are specified in the server configuration. If there are user-defined arguments, enter `yes`.

12. To prepare the Source Endpoint server, which tests the connection to the server with the Sync User account, press Enter to accept the default (yes). For the Sync User account, it will return "Denied" as the account has not been written yet to the PingDirectory server at this time.

    ```
    Testing connection to server1.example.com:1389	Done
    Testing 'cn=Sync User,cn=Root DNs,cn=config' access	Denied
    ```

13. To configure the Sync User account on the directory server, press Enter to accept the default (yes). Enter the bind DN (`cn=DirectoryManager`) and the bind DN password of the directory server so that you can configure the `cn=Sync User` account. PingDataSync creates the Sync User account, tests the base DN, and enables the change log.

    ```
    Created 'cn=Sync User,cn=Root DNs,cn=config'
    Verifying base DN 'dc=example,dc=com'	Done
    Enabling cn=changelog .....
    ```

14. Enter the maximum age of the change log entries, or press Enter to accept the default.

## Configuring the sync pipe and sync classes

The following procedures define a Sync Pipe and two Sync Classes. The first Sync Class is used to match the `accounts` objects. The second Sync Class matches the `group` objects.

1. Continuing from the previous session, enter a name for the Sync Pipe.

2. When prompted to define one or more Sync Classes, enter `yes`.

### Configure the accounts Sync Class

1. Enter a name for the Sync Class. For example, type `accounts_sync_class`.

2. If restricting entries to specific subtrees, enter one or more base DN *(tooltip: \<div class="paragraph">
   \<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
   \</div>)*s. If not, press Enter to accept the default (no).

3. To set an LDAP *(tooltip: \<div class="paragraph">
   \<p>An open, cross platform protocol used for interacting with directory services.\</p>
   \</div>)* search filter, type `yes` and enter the filter `"(accountid=*)"`. Press Enter again to continue. This property sets the LDAP filters and returns all entries that match the search criteria to be included in the Sync Class. In this example, specify that any entry with an `accountID` attribute be included in the Sync Class. If the entry does not contain any of these values, it will not be synchronized to the target server.

4. Choose to synchronize all attributes, specific attributes, or exclude specific attributes from synchronization, or press Enter to accept the default (all).

5. Specify the operations that will be synchronized for the Sync Class, or press Enter to accept the default.

### Configure the groups Sync Class

For this example, configure another Sync Class to handle the `groups` object class. The procedures are similar to that of the configuration steps for the `account_sync_class` Sync Class.

1. On the **Sync Class** menu, enter a name for a new sync class, such as `groups_sync_class`.

2. To restrict entries to specific subtrees, enter one or more base DNs.

3. Set an LDAP search filter. Type `yes` to set up a filter and enter the filter `"(objectClass=groupOfUniqueNames)"`. This property sets the LDAP filters and returns all entries that match the `groupOfUniqueNames` attribute to be included in the Sync Class. If the entry does not contain any of these values, it will not be synchronized to the target server.

4. Choose to synchronize all attributes, specific attributes, or exclude specific attributes from synchronization, or press Enter to accept the default (all).

5. Specify the operations that will be synchronized for the Sync Class, or press Enter to accept the default.

6. At the prompt to enter the name of another Sync Class, press Enter to continue.

7. On the **Default Sync Class Operations** menu, press Enter to accept the default. The Default Sync Class determines how all entries that do not match any other Sync Class are handled.

8. Review the configuration, and press Enter to write the configuration to the server.

Use the `dsconfig` command to make changes to this configuration. Refer to [Configuring PingDataSync](pd_sync_config_pds.html) for configuration options and details.

---

---
title: Configure a Kafka sync destination
description: Use the dsconfig command or the admin console to configure PingDataSync to synchronize changes to an Apache Kafka environment.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_kafka_sync_dest
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_kafka_sync_dest.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 11, 2024
page_aliases: ["pd_sync_kafka_obscure_sensitive_values.adoc", "pd_sync_ssl_config.adoc"]
section_ids:
  obscure_sensitive_producer_values: Obscuring sensitive producer property values
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result:
  example-2: Example:
  ssl_configuration: SSL configuration
---

# Configure a Kafka sync destination

Use the `dsconfig` command or the admin console to configure PingDataSync to synchronize changes to an Apache Kafka environment.

PingDataSync supports synchronization of single and multivalued attributes to Kafka. You can reuse existing PingDirectory sync sources that were created for other sync pipes.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To review an example configuration, refer to the file located at `<server-root>/config/sample-dsconfig-batch-files/reference-sync-pingdirectory-to-kafka.dsconfig`.To configure Kerberos authentication for a Kafka sync destination, supply the `producer-property` attribute with the appropriate values according to the [Apache Kafka documentation](https://kafkaide.com/learn/connect-to-kafka-using-kerberos-auth/). |

The following objects are required to configure a Kafka sync destination:

* **Kafka cluster external server**: Defines the procedure for connecting to a Kafka cluster. The Kafka cluster external server can be referenced from multiple Kafka sync destination and sync source configuration objects. The only required property is `bootstrap-server`, which identifies some of the Kafka brokers in the environment.

  When `use-ssl` is set to `true`, the following configuration changes are made:

  * A `trust-manager-provider` is configured to validate the Kafka broker's SSL certificate.

  * A `key-manager-provider` is configured to let the Kafka broker authenticate the PingDataSync Kafka producer.

* **Kafka sync destination**: References the Kafka cluster external server. The Kafka sync destination must specify the name of the topic to use for publishing messages.

  To adjust Kafka messages beyond the mapping, attribute filtering, and other configuration changes that PingDataSync makes, reference one or more of the `KafkaSyncDestinationPlugin` extension points that are implemented by using the Server SDK.

Run the `prepare-endpoint-server` command for the PingDirectory sync source.

## Obscuring sensitive producer property values

### About this task

When configuring a PingDataSync Kafka producer, you might add producer properties that contain sensitive values such as keys or passwords. To prevent storing these sensitive values in plain text, you can use the `sensitive-kafka-producer-property` configuration property.

You create a `sensitive-kafka-producer-property` using the following required arguments:

* `--property-name`

  Specifies the name of the sensitive Kafka producer property.

* `--set sensitive-producer-key:<key>`

  Specifies the name of the valid property key that contains a sensitive value.

* `--set sensitive-producer-value:<value>`

  Specifies the sensitive value associated with the producer key.

### Steps

* Create one or more sensitive Kafka producer properties using `dsconfig create-sensitive-kafka-producer-property`.

  #### Example:

  ```shell
  $ bin/dsconfig create-sensitive-kafka-producer-property \
    --property-name saslConfig \
    --set "sensitive-producer-key:sasl.jaas.config" \
    --set "sensitive-producer-value:org.apache.kafka.common.security.scram.ScramLoginModule" \
      required username="username" password="password";
  ```

  #### Result:

  Perform an `ldapsearch` for the sensitive property:

  ```
  ldapsearch --baseDN "cn=saslConfig,cn=Sensitive Kafka Producer Property,cn=config" "(objectclass=*)"
  ```

  The sensitive value is now obscured.

  ```
  dn: cn=saslConfig,cn=Sensitive Kafka Producer Property,cn=config
  objectClass: top
  objectClass: ds-cfg-sensitive-kafka-producer-property
  cn: saslConfig
  ds-cfg-sensitive-producer-key: sasl.jaas.config
  ds-cfg-sensitive-producer-value: AADu9yRP8DyrLndvqqDzeQEK9aqqLvDBZZhgHAZbh++KgovN+kUthhyn9+1o9+AqExDmigO14YQnwakqOpTAB4LnbsvwBJos6PZzYlWMNjFNXsDtOUeBsFhVi/nErPJT+cmQijC5P1EUsKWPvjDVauBe
  ```

  |   |                                                                                                                                    |
  | - | ---------------------------------------------------------------------------------------------------------------------------------- |
  |   | The `config-audit.log` file that contains the `dsconfig` change you made to create the sensitive property also obscures the value. |

* (Optional) Delete one or more sensitive Kafka producer properties using `dsconfig delete-sensitive-kafka-producer-property`.

  #### Example:

  ```shell
  $ bin/dsconfig delete-sensitive-kafka-producer-property \
  --property-name saslConfig
  ```

## SSL configuration

The following table identifies the `trust-manager-provider` and `key-manager-provider` properties of the Kafka cluster external server configuration object, as well as the Kafka configuration properties to which they map.

| Configuration object type         | Configuration property                                                                                           | Kafka configuration property |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| File-based trust manager provider | `trust-store-file`                                                                                               | `ssl.truststore.location`    |
| File-based trust manager provider | `trust-store-pin`, `trust-store-pin-property`, `trust-store-pin-environment-variable`, or `trust-store-pin-file` | `ssl.truststore.password`    |
| File-based key manager provider   | `key-store-file`                                                                                                 | `ssl.keystore.location`      |
| File-based key manager provider   | `key-store-pin`, `key-store-pin-property`, `key-store-pin-environment-variable`, or `key-store-pin-file`         | `ssl.keystore.password`      |
| File-based key manager provider   | `private-key-pin`, `private-key-pin-property`, `private-key-pin-environment-variable`, or `private-key-pin-file` | `ssl.key.password`           |

---

---
title: Configure a Kafka sync source
description: Configure a Kafka sync source to consume change events from a Kafka topic and apply them to a sync destination.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_kafka_sync_source
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_kafka_sync_source.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 22, 2026
section_ids:
  kafka-cluster-external-server: Kafka cluster external server
  steps: Steps
  example: Example:
  passing-consumer-properties: Passing consumer properties
  steps-2: Steps
  example-2: Example:
  example-3: Example:
  kafka-sync-source-properties: Kafka sync source properties
  message-format-semantics-for-sync-sources: Message format semantics for sync sources
  json-sync-operation-mapping: JSON sync operation mapping
  dead-letter-queue: Dead letter queue
  configuring-a-kafka-sync-source: Configuring a Kafka sync source
  steps-3: Steps
  example-4: Example:
  example-5: Example:
  example-6: Example:
  example-7: Example:
  example-8: Example:
---

# Configure a Kafka sync source

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This feature is provided as a **Preview**, which means that it isn't supported and should not be used in production environments. Learn more in [Feature statuses](../feature_status.html). |

A Kafka sync source reads change events from a Kafka topic and applies them to a sync destination. This lets you use Kafka as a change feed for propagating updates from an upstream system into PingDataSync. For example, an upstream application can publish change events to a Kafka topic, and PingDataSync can consume those events and apply the changes to a PingDirectory server or another sync destination.

The following objects are required to configure a Kafka sync source:

* **Kafka cluster external server**: Defines the connection parameters for the Kafka cluster. This is the same configuration object used by the Kafka sync destination, and can be shared between both.

* **Kafka sync source**: References the Kafka cluster external server and defines how PingDataSync consumes messages from the topic.

## Kafka cluster external server

The only required property is `bootstrap-server`, which identifies one or more Kafka brokers in the cluster.

When `use-ssl` is set to `true`, you must also configure a `trust-manager-provider` and a `key-manager-provider`. Learn more in [SSL configuration](pd_sync_config_kafka_sync_dest.html#ssl_configuration).

### Steps

* Create the Kafka cluster external server.

  #### Example:

  ```shell
  $ bin/dsconfig create-external-server \
    --server-name kafkaServerName \
    --type kafka-cluster \
    --set bootstrap-server:kafkaHost:9092 \
    --set use-ssl:true \
    --set trust-manager-provider:Kafka \
    --set key-manager-provider:Kafka \
    --applyChangeTo server-group
  ```

  |   |                                                                                                                                                     |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you already created a Kafka cluster external server for a Kafka sync destination, you can reference the same object from your Kafka sync source. |

### Passing consumer properties

Use the `consumer-property` configuration parameter to pass standard Kafka consumer configuration properties to PingDataSync. For sensitive values such as passwords or keys, use `sensitive-consumer-property` instead to prevent storing those values in plain text.

Create a `sensitive-consumer-property` using the following required arguments:

* `--property-name`

  Specifies the name of the sensitive Kafka consumer property.

* `--set sensitive-consumer-key:<key>`

  Specifies the name of the valid property key that contains a sensitive value.

* `--set sensitive-consumer-value:<value>`

  Specifies the sensitive value associated with the consumer key.

#### Steps

* Create one or more sensitive Kafka consumer properties using `dsconfig create-sensitive-kafka-consumer-property`.

  ##### Example:

  ```shell
  $ bin/dsconfig create-sensitive-kafka-consumer-property \
    --property-name saslConfig \
    --set "sensitive-consumer-key:sasl.jaas.config" \
    --set "sensitive-consumer-value:org.apache.kafka.common.security.scram.ScramLoginModule" \
      required username="username" password="password";
  ```

* (Optional) Delete one or more sensitive Kafka consumer properties using `dsconfig delete-sensitive-kafka-consumer-property`.

  ##### Example:

  ```shell
  $ bin/dsconfig delete-sensitive-kafka-consumer-property \
    --property-name saslConfig
  ```

## Kafka sync source properties

Use the following properties to configure the Kafka sync source object:

* `topic`

  The Kafka topic to read messages from.

* `cluster`

  The Kafka cluster external server that defines the connection to the Kafka cluster.

* `consumer-group-id`

  Identifies the consumer group this sync source belongs to. Kafka delivers each message once per consumer group. Multiple instances of the same sync source should share a consumer group so that a new instance can take over where a failed instance left off.

* `max-poll-records`

  The maximum number of records to return in a single poll request. Larger values can improve throughput but increase memory usage.

## Message format semantics for sync sources

The Kafka sync source uses the same JSON message format as the Kafka sync destination. Learn more in [Message format](pd_sync_message_format.html).

The following additional semantics apply when reading messages as a sync source:

* For modify operations, the `current` field can be a partial entry containing only the modified attributes. Attributes omitted from `current` are left unchanged on the destination entry.

* To delete an attribute value in a modify operation, set the attribute to `null` (single-valued) or an empty array (multivalued) in the `current` field.

* For add operations, the `current` field must be a complete entry.

### JSON sync operation mapping

If your Kafka messages use a different format, you can configure a JSON sync operation mapping object to map your message fields to the fields that PingDataSync requires.

The JSON sync operation mapping uses the existing constructed value syntax to assign values from the incoming JSON message to each required sync operation field.

The following properties are available:

> **Collapse: JSON sync operation mapping properties**
>
> * `dn-pattern`
>
>   (Required) A constructed value pattern that resolves to a DN identifying the entry. If the source doesn't use LDAP DNs, you can construct a synthetic DN such as `uid=<userId>,ou=people,dc=example,dc=com` and map it to a destination DN using the existing DN map configuration.
>
> * `change-id-pattern`
>
>   (Required) A constructed value pattern that resolves to a unique identifier for the change.
>
> * `source-entry-pattern`
>
>   (Required) A constructed value that resolves to a JSON object representing the entry. For modify operations, this can be a partial entry containing only the modified attributes.
>
> * `op-type-pattern`
>
>   (Required) A constructed value pattern that resolves to the operation type being performed.
>
> * `modified-attributes-pattern`
>
>   (Optional) A constructed value pattern that lists the attributes modified by the event. If unspecified, all attributes are assumed to be modified.
>
> * `create-op-type-value`
>
>   (Optional) The value in your message that represents a create operation. Defaults to `create`.
>
> * `delete-op-type-value`
>
>   (Optional) The value in your message that represents a delete operation. Defaults to `delete`.
>
> * `modify-op-type-value`
>
>   (Optional) The value in your message that represents a modify operation. Defaults to `modify`.

## Dead letter queue

When PingDataSync can't process a Kafka message (for example, due to a JSON parsing error or mapping failure) it logs an error and moves on to the next message. To preserve failed messages for later inspection or reprocessing, you can configure a dead letter queue (DLQ).

When the DLQ is enabled, failed messages are published to a separate Kafka topic. The original message data is preserved, and error metadata is added to the Kafka record headers.

The following properties configure the DLQ:

* `dlq-enabled`

  Disabled by default. Set to `true` to enable the DLQ. When the DLQ is enabled, you must also specify the `dlq-topic`.

* `dlq-topic`

  The name of the Kafka topic where failed messages are published. Kafka restricts topic names to alphanumeric characters, periods, underscores, and hyphens, with a maximum length of 249 characters.

## Configuring a Kafka sync source

The following steps create a basic Kafka sync source and connect it to a sync destination through a sync pipe.

### Steps

1. Create the [Kafka cluster external server](#kafka-cluster-external-server).

2. Create the Kafka sync source.

   #### Example:

   ```shell
   $ bin/dsconfig create-sync-source \
     --source-name kafkaSyncSource \
     --type kafka \
     --set topic:topicName \
     --set cluster:kafkaServerName \
     --set consumer-group-id:consumerGroupId \
     --applyChangeTo server-group
   ```

   The `consumer-group-id` should be consistent across all PingDataSync instances in a server group so that a standby instance resumes from the last committed offset if the primary fails.

3. Create the sync destination.

   #### Example:

   ```shell
   $ bin/dsconfig create-sync-destination \
     --destination-name syncDestinationName \
     --type ping-directory \
     --set server:destinationServer \
     --applyChangeTo server-group
   ```

   The sync destination can be any supported type, including PingDirectory.

4. Create the sync pipe.

   #### Example:

   ```shell
   $ bin/dsconfig create-sync-pipe \
     --pipe-name kafkaPipeName \
     --set num-worker-threads:10 \
     --set change-detection-polling-interval:"500 ms" \
     --set sync-source:kafkaSyncSource \
     --set sync-destination:syncDestinationName \
     --applyChangeTo server-group
   ```

5. Create the sync class.

   #### Example:

   ```shell
   $ bin/dsconfig create-sync-class \
     --pipe-name kafkaPipeName \
     --class-name kafkaSyncClass \
     --set auto-mapped-source-attribute:all \
     --applyChangeTo server-group
   ```

6. Start the sync pipe.

   #### Example:

   ```shell
   $ bin/dsconfig set-sync-pipe-prop \
     --pipe-name kafkaPipeName \
     --set started:true \
     --applyChangeTo server-group
   ```

---

---
title: Configure a proxy server
description: The following procedure configures a proxy server, including defining the external servers and configuring the client-connection policy. The procedure is the same for the source servers and the destination servers in a synchronization topology.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_proxy_server
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_proxy_server.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure a proxy server

## About this task

The following procedure configures a proxy server, including defining the external servers and configuring the client-connection policy. The procedure is the same for the source servers and the destination servers in a synchronization topology.

For additional changes, use the `dsconfig` command. For proxy installation and configuration details, see the [PingDirectoryProxy server administration guide](../pingdirectoryproxy_server_administration_guide/pd_proxy_admin_guide.html).

## Steps

1. From the PingDirectoryProxy server root directory, run the `prepare-external-server` command to set up the `cn=Proxy User` account for access to the backend directory servers. The server tests the connection and creates the `cn=Proxy User` account.

   ```shell
   $ bin/prepare-external-server --no-prompt \
     --hostname ldap-west-01.example.com \
     --port 389 --bindDN "cn=Directory Manager" \
     --bindPassword password \
     --proxyBindDN "cn=Proxy User,cn=Root DNs,cn=config" \
     --proxyBindPassword pass \
     --baseDN "dc=example,dc=com"
   ```

2. Repeat step 1 for any other directory server instances.

3. Run the `dsconfig` command to define the external servers and their types. For this example, round-robin load balancing algorithms are defined, which do not require health checks or locations to be specified.

   ```shell
   $ bin/dsconfig --no-prompt create-external-server \
     --server-name ldap-west-01 \
     --type "ping-identity-ds" \
     --set "server-host-name:ldap-west-01.example.com" \
     --set "server-port:389" \
     --set "bind-dn:cn=Proxy User" \
     --set "password:password" \
     --bindDN "cn=Directory Manager" \
     --bindPassword pxy-pwd
   ```

   ```shell
   $ bin/dsconfig --no-prompt create-external-server \
     --server-name ldap-west-02 \
     --type "ping-identity-ds" \
     --set "server-host-name:ldap-west-02.example.com" \
     --set "server-port:389" \
     --set "bind-dn:cn=Proxy User" \
     --set "password:password" \
     --bindDN "cn=Directory Manager" \
     --bindPassword pxy-pwd
   ```

   ```shell
   $ bin/dsconfig --no-prompt create-external-server \
     --server-name ldap-west-03 \
     --type "ping-identity-ds" \
     --set "server-host-name:ldap-west-03.example.com" \
     --set "server-port:389" \
     --set "bind-dn:cn=Proxy User" \
     --set "password:password" \
     --bindDN "cn=Directory Manager" \
     --bindPassword pxy-pwd
   ```

   ```shell
   $ bin/dsconfig --no-prompt create-external-server
     --server-name ldap-west-04 \
     --type "ping-identity-ds" \
     --set "server-host-name:ldap-west-04.example.com" \
     --set "server-port:389" \
     --set "bind-dn:cn=Proxy User" \
     --set "password:password" \
     --bindDN "cn=Directory Manager" \
     --bindPassword pxy-pwd
   ```

4. Create a load-balancing algorithm for each backend set.

   ```shell
   $ bin/dsconfig --no-prompt create-load-balancing-algorithm \
     --algorithm-name "test-lba-1" \
     --type "round-robin" --set "enabled:true" \
     --set "backend-server:ldap-west-01" \
     --set "backend-server:ldap-west-02" \
     --set "use-location:false" \
     --bindDN "cn=Directory Manager" \
     --bindPassword pxy-pwd
   ```

   ```shell
   $ bin/dsconfig --no-prompt create-load-balancing-algorithm \
     --algorithm-name "test-lba-2" \
     --type "round-robin" --set "enabled:true" \
     --set "backend-server:ldap-west-03"
     --set "backend-server:ldap-west-04"
     --set "use-location:false" \
     --bindDN "cn=Directory Manager" \
     --bindPassword pxy-pwd
   ```

5. Configure the proxying request processors, one for each load-balanced directory server set. A request processor provides the logic to either process the operation directly, forward the request to another server, or hand off the request to another request processor.

   ```shell
   $ bin/dsconfig --no-prompt create-request-processor \
     --processor-name "proxying-processor-1" --type "proxying" \
     --set "load-balancing-algorithm:test-lba-1" \
     --bindDN "cn=Directory Manager" \
     --bindPassword pxy-pwd
   ```

   ```shell
   $ bin/dsconfig --no-prompt create-request-processor \
     --processor-name "proxying-processor-2" --type "proxying" \
     --set "load-balancing-algorithm:test-lba-2" \
     --bindDN "cn=Directory Manager" \
     --bindPassword pxy-pwd
   ```

6. Define an entry-balancing request processor. This request processor is used to distribute entries under a common parent entry among multiple backend sets. A backend set is a collection of replicated directory servers that contain identical portions of the data. Multiple proxying request processors are used to process operations.

   Next, define the placement algorithm, which selects the server set to use for new add operations to create new entries. In this example, a round-robin placement algorithm forwards LDAP add requests to backend sets.

   ```shell
   $ bin/dsconfig --no-prompt create-placement-algorithm \
     --processor-name "entry-balancing-processor" \
     --algorithm-name "round-robin-placement" \
     --set "enabled:true" \
     --type "round-robin" \
     --bindDN "cn=Directory Manager" \
     --bindPassword pxy-pwd
   ```

7. Define the subtree view that specifies the base distinguished name (DN) *(tooltip: \<div class="paragraph">
   \<p>A name uniquely identifying an object within the hierarchy of a directory tree.\</p>
   \</div>)* for the entire deployment.

   ```shell
   $ bin/dsconfig --no-prompt create-subtree-view \
     --view-name "test-view" \
     --set "base-dn:dc=example,dc=com" \
     --set "request-processor: entry-balancing-processor" \
     --bindDN "cn=Directory Manager" \
     --bindPassword pxy-pwd
   ```

8. Finally, define a client connection policy that specifies how the client connects to the proxy server.

   ```shell
   $ bin/dsconfig --no-prompt set-client-connection-policy-prop \
     --policy-name "default" \
     --add "subtree-view:test-view" \
     --bindDN "cn=Directory Manager" \
     --bindPassword pxy-pwd
   ```

---

---
title: Configure a sync pipe
description: A sync pipe associates a sync source, from which changes will be read, with a sync destination, to which corresponding changes will be applied.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_sync_pipe
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_sync_pipe.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configure a sync pipe

A sync pipe associates a sync source, from which changes will be read, with a sync destination, to which corresponding changes will be applied.

Although there are many useful configuration properties associated with a sync pipe, including those used to control retry attempts, rate limiting, and the number of worker threads, most of those properties already have good default values. The only properties you need to specify are:

* `sync-source`

  The sync source from which the changes will be read. This is required.

* `sync-destination`

  The sync destination to which the corresponding changes will be applied. This is required.

You can use the following example configuration change to create a sync pipe:

```
dsconfig create-sync-pipe \
     --pipe-name "LDAP Source to SCIMv2 Destination" \
     --set "sync-source:LDAP Source" \
     --set "sync-destination:SCIMv2 Destination"
```

---

---
title: Configure an LDAPv3 Sync Source
description: Synchronization can be performed with an LDAP V3-compliant source, such as IBM SDS (Tivoli Directory Server), Oracle Unified Directory, DSEE, or OpenDJ, by configuring a Generic LDAP Sync Source. PingDataSync relies on the source server having a cn=changelog implementation. If the server does not have a cn=changelog implementation, a Server SDK Change Detector extension can be configured to define the change detection criteria that PingDataSync should use.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_ldapv3_sync_source
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_ldapv3_sync_source.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Configure an LDAPv3 Sync Source

Synchronization can be performed with an LDAP V3-compliant source, such as IBM SDS (Tivoli Directory Server), Oracle Unified Directory, DSEE, or OpenDJ, by configuring a Generic LDAP Sync Source. PingDataSync relies on the source server having a `cn=changelog` implementation. If the server does not have a `cn=changelog` implementation, a Server SDK Change Detector extension can be configured to define the change detection criteria that PingDataSync should use.

If multiple Generic LDAP Sync Source instances are defined, the order in which they are added is used as a priority order for failover. If server locations are defined, PingDataSync will always fail over to servers that are in the same location. If there are multiple Sync Sources in the same location as PingDataSync, then PingDataSync will fail over to the first local server in the list and proceed down the list.

During synchronization, when a change is detected by PingDataSync, the changed entry is fetched from the source. Initially, the DN of the entry is used to search for the entry. If that search fails, then a second search is performed using the `unique-id-attribute` if it is defined. This is typically an operational attribute that is automatically generated by the server, such as `entryUUID`.

---

---
title: Configure authentication with a SASL external certificate
description: By default, PingDataSync authenticates to the PingDirectory server using LDAP simple authentication (with a bind DN and a password). However, PingDataSync can be configured to use SASL EXTERNAL to authenticate to the PingDirectory server with a client certificate.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdatasync_server_administration_guide:pd_sync_config_authn_sasl_ext_cert
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdatasync_server_administration_guide/pd_sync_config_authn_sasl_ext_cert.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Configure authentication with a SASL external certificate

## About this task

By default, PingDataSync authenticates to the PingDirectory server using LDAP simple authentication (with a bind DN and a password). However, PingDataSync can be configured to use SASL EXTERNAL to authenticate to the PingDirectory server with a client certificate.

|   |                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure assumes that PingDataSync instances are installed and configured to communicate with the backend PingDirectory server instances using either SSL or StartTLS. |

After the servers are configured, perform the following steps to configure SASL EXTERNAL authentication:

## Steps

1. Create a JKS keystore that includes a public and private key pair for a certificate that the PingDataSync instance(s) will use to authenticate to the PingDirectory server instance(s). Run the following command in the instance root of one of the PingDataSync instances. When prompted for a keystore password, enter a strong password to protect the certificate. When prompted for the key password, press ENTER to use the keystore password to protect the private key:

   ```shell
   $ keytool -genkeypair \
     -keystore config/sync-user-keystore \
     -storetype JKS \
     -keyalg RSA \
     -keysize 2048 \
     -alias sync-user-cert \
     -dname "cn=Sync User,cn=Root DNs,cn=config" \
     -validity 7300
   ```

2. Create a `config/sync-user-keystore.pin` file that contains a single line that is the keystore password provided in the previous step.

3. If there are other PingDataSync instances in the topology, copy the `sync-user-keystore` and `sync-user-keystore.pin` files into the config directory for all instances.

4. Use the following command to export the public component of the user certificate to a text file:

   ```shell
   $ keytool -export \
     -keystore config/sync-user-keystore \
     -alias sync-user-cert \
     -file config/sync-user-cert.txt
   ```

5. Copy the `sync-user-cert.txt` file into the `config` directory of all PingDirectory server instances. Import that certificate into each server's primary trust store by running the following command from the server root. When prompted for the keystore password, enter the password contained in the `config/truststore.pin` file. When prompted to trust the certificate, enter `yes`.

   ```shell
   $ keytool -import \
     -keystore config/truststore \
     -alias sync-user-cert \
     -file config/sync-user-cert.txt
   ```

6. Update the configuration for each PingDataSync instance to create a new key manager provider that will obtain its certificate from the `config/sync-user-keystore` file. Run the following `dsconfig` command from the server root:

   ```shell
   $ dsconfig create-key-manager-provider \
     --provider-name "Sync User Certificate" \
     --type file-based \
     --set enabled:true \
     --set key-store-file:config/sync-user-keystore \
     --set key-store-type:JKS \
     --set key-store-pin-file:config/sync-user-keystore.pin
   ```

7. Update the configuration for each LDAP external server in each PingDataSync server instance to use the newly created key manager provider, and also to use SASL EXTERNAL authentication instead of LDAP simple authentication. Run the following `dsconfig` command:

   ```shell
   $ dsconfig set-external-server-prop \
     --server-name ds1.example.com:636 \
     --set authentication-method:external \
     --set "key-manager-provider:Sync User Certificate"
   ```

## Next steps

After these changes, PingDataSync should re-establish connections to the LDAP external server and authenticate with SASL EXTERNAL. Verify that PingDataSync is still able to communicate with all backend servers by running the `bin/status` command. All of the servers listed in the "--- LDAP External Servers ---" section should have a status of `Available`. Review the PingDirectory server access log to make sure that the BIND RESULT log messages used to authenticate the connections from PingDataSync include `authType="SASL", saslMechanism="EXTERNAL", resultCode=0`, and `authDN="cn=Sync User,cn=RootDNs,cn=config"`.
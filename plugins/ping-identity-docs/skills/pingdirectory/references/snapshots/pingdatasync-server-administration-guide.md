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

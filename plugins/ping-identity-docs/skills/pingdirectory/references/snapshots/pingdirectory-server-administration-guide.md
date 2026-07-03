---
title: About backing up and restoring data
description: Administrators should make a comprehensive backup strategy and schedule that consist of daily, weekly, and monthly backups. The plan should include:
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_about_backup_restore_data
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_about_backup_restore_data.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About backing up and restoring data

Administrators should make a comprehensive backup strategy and schedule that consist of daily, weekly, and monthly backups. The plan should include:

* Full backups of the PingDirectory server data, configuration, and backends

* A backup plan for the underlying file system

This dual purpose approach provides excellent coverage in the event that a server database must be restored for any reason.

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can use `dsconfig create-recurring-task` to configure backups as recurring tasks and schedule those tasks as part of a recurring task chain. |

If you back up more than one backend, the `backup` tool creates a subdirectory within a specified backup directory for each backend. If you back up only a single backend, then the backup files are placed in the specified directory. A single directory can only contain files from one backend, so you cannot have backup files from multiple different backends in the same backup directory.

When performing a backup, the server records information about the current state of the server and backend, including:

* The server product name

* The server version

* The backend ID

* The set of base distinguished names (DNs) for the backend

* The Java class used to implement the backend logic

The backup descriptor also includes information about the Berkeley DB Java edition version and information about the attribute and virtual list view (VLV) indexes that have been defined.

When restoring a backup, the server compares the descriptor obtained from the backup with the current state of the server and backend. If any problems are identified, the server generates warnings or errors.

You can choose to ignore warnings using the `ignoreCompatibilityWarnings` option to the `restore` tool. Errors always cause the restore operation to fail.

For example, restoring a newer backup into an older version of the server results in a warning. Restoring an older backup into a new version of the server does not result in a warning, but because the `config` and `schema` backends require special handling, the server generates an error if the server versions do not match exactly the major, minor, point, and patch version numbers.

Both the `backup` and `restore` tools provide encryption options that can be used to specify which key to use for encrypting the backup:

* `--promptForEncryptionPassphrase`

* `--encryptionPassphraseFile`

* `--encryptionSettingsDefinitionID`

For backups encrypted with an encryption settings definition or an internal topology key, the server automatically determines the correct key.

Alternately, you can use the `--doNotEncrypt` argument to force a backup to be unencrypted even if automatic encryption is enabled.

If necessary, you can use the `--maxMegabytesPerSecond` argument to impose a limit on the rate at which the backup can be written to disk.

---

---
title: About backing up and restoring the encryption settings definitions
description: The PingDirectory server provides two different mechanisms for backing up and restoring encryption settings definitions.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_backup_restore_encryption_settings_defs
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_backup_restore_encryption_settings_defs.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About backing up and restoring the encryption settings definitions

The PingDirectory server provides two different mechanisms for backing up and restoring encryption settings definitions.

To back up and restore encryption settings definitions, you can either:

* Export one or more encryption settings definitions using the `encryption-settings export` command. This command also generates a passphrase-protected file containing the encryption settings definitions in a portable format. This is the recommended approach.

* Back up and restore the entire encryption settings database using the `backup` and `restore` tools.

The `encryption-settings export` command is recommended for the following reasons:

* With the `backup` command, the resulting backup only contains the `encryption-settings-db` file. The backup does not automatically contain any metadata files needed by the configured cipher stream provider to access the encryption settings database. The output generated by the `backup` command indicates which additional files are needed to enable that access.

  |   |                                                                                         |
  | - | --------------------------------------------------------------------------------------- |
  |   | These metadata files must be present before restoring the encryption settings database. |

* With the `backup` command, the resulting backup depends on the cipher stream provider enabled when the encryption settings database was last written. This means that the cipher stream provider must already be configured and active in the server configuration before restoring the encryption settings database.

* Because the backup generated by the `backup` command depends on the existing configuration of the cipher stream provider, that cipher stream provider might not be useable if the system configuration changes. For example, if the Amazon Key Management Service cipher stream provider was used at the time the backup was generated with an encryption key that is no longer available, then it's not possible to restore the backup.

|   |                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The encryption settings definitions must be exported or backed up regularly, especially after creating a new definition, importing one or more definitions, or changing the preferred encryption settings definition.If an encryption settings definition is lost, then any data encrypted with that definition becomes inaccessible. In some cases, a lost definition renders the server inoperable. |

---

---
title: About encrypting and protecting sensitive data
description: The PingDirectory server provides an encryption settings database that holds encryption and decryption definitions to protect sensitive data. You can enable on-disk encryption for data:
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_encrypt_protect_sensitive_data
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_encrypt_protect_sensitive_data.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About encrypting and protecting sensitive data

The PingDirectory server provides an encryption settings database that holds encryption and decryption definitions to protect sensitive data. You can enable on-disk encryption for data:

* in backends

* in the changelog

* in the replication databases

You can protect sensitive attributes by limiting the ways that clients can interact with them.

---

---
title: About encrypting log files
description: The server lets you encrypt log files as they are written.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_encrypt_log_files
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_encrypt_log_files.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
page_aliases: ["pd_ds_config_log_signing.adoc", "pd_ds_validate_signed_file.adoc", "pd_ds_config_log_file_encryption.adoc"]
section_ids:
  configuring-log-signing: Configuring log signing
  steps: Steps
  example: Example:
  example-2: Example:
  validating-a-signed-file: Validating a signed file
  steps-2: Steps
  example-3: Example:
  result: Result:
  configuring-log-file-encryption: Configuring log file encryption
  steps-3: Steps
  example-4: Example:
  example-5: Example:
---

# About encrypting log files

The server lets you encrypt log files as they are written.

The `encrypt-log` configuration property controls whether encryption is enabled for the logger. Enabling encryption causes the log file to have an `.encrypted` extension. If both encryption and compression are enabled, the extension is `.gz.encrypted`. Any change that affects the name used for the log file could prevent older files from getting properly cleaned up.

Like compression, encryption can only be enabled when the logger is created. Encryption cannot be turned on or off after the logger is configured. For any log file that is encrypted, enabling compression is also recommended to reduce the amount of data that needs to be encrypted. This reduces the overall size of the log file. The `encrypt-file` tool or custom code, using the LDAP SDK's `com.unboundid.util.PassphraseEncryptedInputStream`, is used to access the encrypted data.

To enable encryption, at least one encryption settings definition must be defined in the server. Use the one created during setup, or create a new one with the `encryption-settings create` command. By default, the encryption is performed with the server's preferred encryption settings definition.

To explicitly specify which definition should be used for the encryption, set the `encryption-settings-definition-id` property with the ID of that definition. You should set the encryption settings definition to be created from a passphrase so that the file can be decrypted by providing that passphrase even if the original encryption settings definition is no longer available. You can also create a randomly generated encryption settings definition, but the log file can only be decrypted using a server instance that has that encryption settings definition.

When using encrypted logging, a small amount of data might remain in an in-memory buffer until the log file is closed. The encryption is performed using a block cipher, and it cannot write an incomplete block of data until the file is closed. This is not an issue for any log file that is not being actively written.

To examine the contents of a log file that is being actively written, use the `rotate-log` tool to force the file to be rotated before attempting to examine it.

## Configuring log signing

Configure log signing for a log publisher.

### Steps

1. To enable log signing for a log publisher, use `dsconfig`.

   #### Example:

   In this example, the `sign-log` property is set on the File-based Audit Log Publisher.

   ```shell
   $ bin/dsconfig set-log-publisher-prop --publisher-name "File-Based Audit Logger" \
     --set sign-log:true
   ```

2. Disable and then re-enable the log publisher for the change to take effect.

   #### Example:

   ```shell
   $ bin/dsconfig set-log-publisher-prop --publisher-name "File-Based Audit Logger" \
     --set enabled:false
   $ bin/dsconfig set-log-publisher-prop --publisher-name "File-Based Audit Logger" \
     --set enabled:true
   ```

## Validating a signed file

The server provides a tool, `validate-file-signature`, that checks if a file has not been tampered with in any way.

### Steps

* Run the `validate-file-signature` tool to check if a signed file has been tampered with.

  #### Example:

  For this example, assume that the `sign-log` property was enabled for the File-Based Audit Log Publisher.

  ```shell
  $ bin/validate-file-signature --file logs/audit
  ```

  #### Result:

  ```
  All signature information in file 'logs/audit' is valid
  ```

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                        |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If any validations errors occur, you will see a message similar to the one as follows.```
  One or more signature validation errors were encountered
  while validating the contents of file 'logs/audit':
  * The end of the input stream was encountered without
    encountering the end of an active signature block.
    The contents of this signed block cannot be trusted
    because the signature cannot be verified
  ``` |

## Configuring log file encryption

Configure log file encryption for a log publisher.

### Steps

1. To enable encryption for a log publisher, use `dsconfig`.

   #### Example:

   In this example, the File-based Access Log Publisher `"Encrypted Access"` is created, compression is set, and rotation and retention policies are set.

   ```shell
   $ bin/dsconfig create-log-publisher-prop --publisher-name "Encrypted Access" \
     --type file-based-access \
     --set enabled:true \
     --set compression-mechanism:gzip \
     --set encryption-settings-definition-id:332C846EF0DCD1D5187C1592E4C74CAD33FC1E5FC20B726CD301CDD2B3FFBC2B \
     --set encrypt-log:true \
     --set log-file:logs/encrypted-access \
     --set "rotation-policy:24 Hours Time Limit Rotation Policy" \
     --set "rotation-policy:Size Limit Rotation Policy" \
     --set "retention-policy:File Count Retention Policy" \
     --set "retention-policy:Free Disk Space Retention Policy" \
     --set "retention-policy:Size Limit Retention Policy"
   ```

2. Decrypt and decompress the file.

   #### Example:

   ```shell
   $ bin/encrypt-file --decrypt \
     --decompress-input \
     --input-file logs/encrypted-access.20180216040332Z.gz.encrypted \
     --output-file decrypted-access
   Initializing the server's encryption framework...Done
   Writing decrypted data to file '/ds/Data-Sync/decrypted-access' using a
   key generated from encryption settings definition '332c846ef0dcd1d5187c1592e4c74cad33fc1e5fc20b726cd301cdd2b3ffbc2b'
   Successfully wrote 123,456,789 bytes of decrypted data
   ```

---

---
title: About log compression
description: The server supports the ability to compress log files as they are written.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_log_compression
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_log_compression.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# About log compression

The server supports the ability to compress log files as they are written.

This feature can significantly increase the amount of data that can be stored in a given amount of space so that log information can be kept for a longer period of time.

Because of the inherent problems with mixing compressed and uncompressed data, compression can only be enabled at the time the logger is created. Compression cannot be turned on or off when the logger is configured. Because of problems in trying to append to an existing compressed file, if the server encounters an existing log file at startup, it rotates that file and begin a new one rather than attempting to append to the previous file.

Compression is performed using the standard gzip algorithm, so compressed log files can be accessed using readily available tools. The `summarize-access-log` tool can also work directly on compressed log files rather than requiring them to be uncompressed first.

However, because it can be useful to have a small amount of uncompressed log data available for troubleshooting purposes, administrators using compressed logging might want to have a second logger defined that does not use compression and has rotation and retention policies that minimizes the amount of space consumed by those logs while still making them useful for diagnostic purposes without the need to uncompress the files before examining them.

Configure compression by setting the `compression-mechanism` property to have the value of `gzip` when creating a new logger.

---

---
title: About log signing
description: The server supports the ability to cryptographically sign a log to ensure that it has not been modified in any way.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_log_signing
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_log_signing.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# About log signing

The server supports the ability to cryptographically sign a log to ensure that it has not been modified in any way.

For example, financial institutions require audit logs for all transactions to check for correctness. Tamper-proof files are needed to ensure that these transactions can be properly validated and ensure that they have not been modified by any third-party entity or internally by unscrupulous employees.

Use the `dsconfig` tool to enable the `sign-log` property on a log publisher to turn on cryptographic signing.

When enabling signing for a logger that already exists and was enabled without signing, the first log file is not completely verifiable because it still contains unsigned content from before signing was enabled. Only log files whose entire content was written with signing enabled are considered completely valid. For the same reason, if a log file is still open for writing, then signature validation does not indicate that the log is completely valid because the log doesn't include the necessary end signed content indicator at the end of the file.

To validate log file signatures, use the `validate-file-signature` tool provided in the `bin` directory of the server or the `bat` directory for Windows systems.

After you have enabled this property, you must disable and then re-enable the log publisher for the changes to take effect.

---

---
title: About managing attribute syntaxes
description: The attribute type definition has a SYNTAX element, or attribute syntax, that specifies how the data values for the attribute are represented.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_manage_attr_syntaxes
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_manage_attr_syntaxes.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About managing attribute syntaxes

The attribute type definition has a `SYNTAX` element, or attribute syntax, that specifies how the data values for the attribute are represented.

The syntax can be used to define a large range of data types necessary for client applications. An attribute syntax uses the Abstract Syntax Notation One (ASN.1) format for its definitions.

---

---
title: About managing attribute types
description: An attribute type determines the important properties related to an attribute, such as specifying the matching and syntax rules used in value comparisons. An attribute description consists of an attribute type and a set of zero or more options.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_manage_attribute_types
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_manage_attribute_types.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About managing attribute types

An attribute type determines the important properties related to an attribute, such as specifying the matching and syntax rules used in value comparisons. An attribute description consists of an attribute type and a set of zero or more options.

Options are short, case-insensitive text strings that differentiate between attribute descriptions. For example, the LDAPv3 specification defines only one type of option, the tagging option, that can be used to tag language options, such as `cn;lang-de;lang-sp` or binary data, such as `userCertificate;binary`. You can also extend the schema by adding your own attribute definitions.

Attributes have the following properties:

* Attributes can be user attributes that hold information for client applications, or operational attributes used for administrative or server-related purposes.

  |   |                                                                   |
  | - | ----------------------------------------------------------------- |
  |   | To specify the purpose of the attribute, use the `USAGE` element. |

* Attributes are multi-valued by default. Multi-valued means that attributes can contain more than one value within an entry.

  |   |                                                                                                        |
  | - | ------------------------------------------------------------------------------------------------------ |
  |   | If the attribute should contain at most one value within an entry, include the `SINGLE-VALUE` element. |

* Attributes can inherit properties from a parent attribute as long as they both have the same `USAGE`, and the child attribute has the same `SYNTAX`, or its `SYNTAX` allows values that are a subset of the values allowed by the `SYNTAX` of the parent attribute. For example, the surname (`sn`) attribute is a child of the name attribute.

---

---
title: About managing JSON attribute values
description: The PingDirectory server supports a JSON object attribute syntax that can be used for attribute types whose values are JSON objects. The syntax requires that each value of this type is a valid JSON object.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_manage_json_attr_values
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_manage_json_attr_values.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About managing JSON attribute values

The PingDirectory server supports a JSON object attribute syntax that can be used for attribute types whose values are JSON objects. The syntax requires that each value of this type is a valid JSON object.

The following is an example schema definition.

```
dn: cn=schema
objectClass: top
objectClass: ldapSubentry
objectClass: subschema
cn: schema
attributeTypes: ( jsonAttr1-OID NAME 'jsonAttr1' DESC 'test json attribute support' EQUALITY jsonObjectExactMatch SYNTAX 1.3.6.1.4.1.30221.2.3.4 USAGE userApplications )
objectClasses: ( jsonObjectClass-OID NAME 'jsonObjectClass' AUXILIARY MAY jsonAttr1 )
```

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You should always specify the `EQUALITY` matching rule as `jsonObjectExactMatch` in the schema definition. Using the `jsonObjectFilterExtensibleMatch` isn't valid in this case. |

The `jsonObjectExactMatch` and `jsonObjectFilterExtensibleMatch` matching rules are provided to filter equality matching rule JSON object syntax. The following three additional matching rules are used in conjunction with `jsonObjectExactMatch` and provide support for customizing the way that the server treats case sensitivity in JSON field names and in string values:

* `jsonObjectCaseSensitiveNamesCaseSensitiveValues`

* `jsonObjectCaseInsensitiveNamesCaseInsensitiveValues`

* `jsonObjectCaseInsensitiveNamesCaseSensitiveValues`

The `jsonObjectExactMatch` equality matching rule is used in evaluating equality filters in `search` operations, and for matching performed against JSON object attributes for `add`, `compare`, and `modify` operations. It determines whether two values are logically-equivalent JSON objects. The field names used in both objects must match exactly, although fields can appear in different orders. The values of each field must have the same data types. The order of elements in arrays is considered significant. Substring or approximate matching isn't supported.

The `jsonObjectFilterExtensibleMatch` matching rule can perform more powerful matching against JSON objects. The assertion values for these extensible matching filters should be JSON objects that express the constraints for the matching. These JSON object filters are described in detail in the Javadoc documentation for the LDAP SDK for Java. Although the LDAP SDK can facilitate searches with this matching rule, these searches can be issued through any LDAP client API that supports extensible matching.

The following are example searches using the `jsonObjectFilterExtensibleMatch` rule with available filter types:

* `"equals"` filter type

```shell
$ bin/ldapsearch -p 1389 -b dc=example,dc=com  -D "cn=Directory Manager" -w password '(jsonAttr1:jsonObjectFilterExtensibleMatch:={ "filterType" : "equals", "field" : ["stuff", "onetype", "name"], "value" : "John Doe" })'
```

* `"containsField"` filter type

```shell
$ bin/ldapsearch -p 1389 -b dc=example,dc=com  -D "cn=Directory Manager" -w password '(jsonAttr1:jsonObjectFilterExtensibleMatch:={ "filterType" : "containsField", "field" : "age", "expectedType" : "number" })'
```

* `"greaterThan"` filter type

```shell
$ bin/ldapsearch -p 1389 -b dc=example,dc=com  -D "cn=Directory Manager" -w password '(jsonAttr1:jsonObjectFilterExtensibleMatch:={ "filterType" : "greaterThan", "field" : "age", "value" : 26, "allowEquals" : true})'
```

---

---
title: About managing matching rules
description: Matching rules determine how clients and servers compare attribute values during LDAP requests or operations.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_manage_matching_rules
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_manage_matching_rules.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About managing matching rules

Matching rules determine how clients and servers compare attribute values during LDAP requests or operations.

Matching rules are also used in evaluating search filter elements, including distinguished names (DNs) and attributes. They are defined for each attribute based on the following properties:

* `EQUALITY`: Two attributes are equal based on case, exact match, and so forth.

* `SUBSTR`: The assertion value is a substring of an attribute.

* `ORDERING`: Specifies greater than or equal, less than or equal, and so forth.

|   |                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingDirectory server supports an `APPROXIMATE` matching rule that compares similar attributes based on fuzzy logic. Attributes that are similar or sound alike are matched. For example, `petersen` would match `peterson`. |

---

---
title: About minimizing disk access
description: Minimizing disk access is critical to the PingDirectory server's performance.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_minimize_disk_access
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_minimize_disk_access.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
---

# About minimizing disk access

Minimizing disk access is critical to the PingDirectory server's performance.

Defining a Java Virtual Machine (JVM) heap size that can contain the entire contents of the database cache in memory minimizes read operations from disk and achieves optimal performance. The database on-disk is comprised of transaction log files, which are only appended to. After an initial database import, the size on-disk will grow by a factor of at least 25% as inactive records accumulate in the transaction logs. During normal operation, the on-disk size of the database transaction logs does not represent the memory needed to cache the database.

Consider minimizing the size of the database based on the known characteristics of your data. Doing so reduces hard disk requirements and the memory requirements for the database cache. An example of this is the PingDirectory server automatically compacting common parent distinguished names (DN).

Finally, consider the write load on your server and its effect on the database. Write operations will always require an associated write-to-disk, but an environment that sustains a high load of write operations might consider tuning the background database cleaner to minimize the size of the database on disk.

---

---
title: About monitoring index entry limits
description: Index keys that have reached their limit require indexes to be rebuilt before they can use a new limit. To avoid a potentially costly rebuild, there are several ways to monitor index limits.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_monitor_index_entry_limits
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_monitor_index_entry_limits.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About monitoring index entry limits

Index keys that have reached their limit require indexes to be rebuilt before they can use a new limit. To avoid a potentially costly rebuild, there are several ways to monitor index limits.

In certain cases, it's acceptable for index keys to exceed the index entry limit. For example, the `objectClass` attribute type should be indexed for equality because the server needs to use it to find all group entries when bringing a backend online, and applications frequently need to find entries of a specific type. However, the top objectClass key doesn't need to be indexed because it appears in every entry in the server.

Select an index entry limit value that is high enough to ensure that all of the right keys are indexed, but keys that occur too frequently are not. The `--listKeysNearestIndexEntryLimit` argument of the `verify-index` tool lists a specified number of keys that are closest to the limit without having exceeded it. Make the index entry limit larger than the number of entries matching the largest key to remain indexed, with enough overhead to account for future growth. Use this command regularly to determine if you need to adjust the index entry limit needs to be adjusted.

The `--listKeysExceedingIndexEntryLimit` argument of the `verify-index` tool lists all keys for which the value has exceeded the index entry limit and the number of entries in which they appear. If there are keys for which the limit has been exceeded that need to be maintained, adjust the index entry limit to be higher than the number of entries that contain that key, with additional room for future growth. Then, run the `rebuild-index` tool or export to LDIF and re-import.

The server provides other methods for determining if index keys have exceeded or are close to exceeding the index entry limit, including:

* When performing an LDIF import, the tool includes an Index Summary Statistics section that provides usage information for each index, including:

  * The number of keys for which the index entry limit has been exceeded.

  * The number of keys for which the number of matching entries falls within several predefined buckets, such as 1–4 entries, 5–9 entries, 10–99 entries, and 100–999 entries.

* During a search operation, if the server accesses one or more index keys whose values have exceeded the index entry limit, the access log message for that operation includes an `indexesWithKeysAccessedExceedingEntryLimit` field containing a comma-delimited list of the appropriate indexes. The same access log field can appear in log messages for add, delete, modify, and modify DN operations in which the server wrote to, or tried to write to, at least one index key whose value exceeded the index entry limit.

* During a search operation, if the server accesses one or more index keys whose values have not yet exceeded the index entry limit but are greater than 80 percent of it, the access log message for that operation includes an `indexesWithKeysAccessedNearEntryLimit` field containing a comma-delimited list of the appropriate indexes. The same access log field can appear in log messages for add, delete, modify, and modify DN operations in which the server wrote to at least one index key whose value was within 80%of the index entry limit.

* If a search operation request includes either the `debugsearchindex` attribute or the matching entry count request control with debugging enabled, the debug information includes any indexes accessed that have exceeded the index entry limit or that are within 80% of the configured index entry limit.

* The monitor entry for each configured index includes attributes that provide information about the number of index keys that have been encountered since the backend was brought online, or since the index entry limit was changed in several different categories. These monitor attributes include:

  * `ds-index-exceeded-entry-limit-count-since-db-open`

    The number of index keys for which the number of matching entries has crossed the index entry limit because of a write operation.

  * `ds-index-unique-keys-near-entry-limit-accessed-by-search-since-db-open`

    The number of unique index keys that have been accessed by a search operation for which the number of matching entries is within 80% of the index entry limit.

  * `ds-index-unique-keys-exceeding-entry-limit-accessed-by-search-since-db-open`

    The number of unique index keys that have been accessed by a search operation for which the number of matching entries has exceeded the index entry limit at some point since the index was last built.

  * `ds-index-unique-keys-near-entry-limit-accessed-by-write-since-db-open`

    The number of unique index keys that have been accessed by a write operation for which the number of matching entries is within 80% of the index entry limit.

  * `ds-index-unique-keys-exceeding-entry-limit-accessed-by-write-since-db-open`

    The number of unique index keys that have been accessed by a write operation for which the number of matching entries has exceeded the index entry limit at some point since the index was last built.

---

---
title: About recurring tasks and task chains
description: You can use the admin console to create recurring tasks and task chains to perform regular maintenance tasks for the PingDirectory server. These tasks can perform regular backups, LDIF exports, enter and exit lockdown mode, or other static operations.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_recurring_task_chains
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_recurring_task_chains.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 4, 2024
---

# About recurring tasks and task chains

You can use the admin console to create recurring tasks and task chains to perform regular maintenance tasks for the PingDirectory server. These tasks can perform regular backups, LDIF exports, enter and exit lockdown mode, or other static operations.

Because this process is owned by the server, tasks do not require special privileges or credentials, and they can be run when the server is offline.

Create recurring tasks and add them to a recurring task chain for scheduling. The task chain ensures that invocations of a task or set of tasks run in a specified order and do not overlap.

A recurring task includes:

* The task-specific object classes to include in the task entry

* The task-specific attributes to include in the task entry, if any

* Whether to alert on task start, success, or failure

* Any addresses to email on task start, success, or failure

* Whether to cancel an instance of the task if it is dependent upon another task and that task does not complete successfully

After you create a task, add one or more tasks to a task chain and schedule the chain.

A recurring task chain includes:

* An ordered list of the tasks to invoke

* The months, days, times, and time zones in which each task can be scheduled to start

* The behavior to exhibit if any of the tasks are interrupted by a server shutdown

* The behavior to exhibit if the server is offline when the start time occurs

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Changing the schedule for an existing recurring task chain only takes effect the next time an instance of the chain needs to be scheduled. It does not affect any existing instances of the chain that are already scheduled. Existing scheduled instances still run at the originally scheduled time. When that run is complete, the server schedules the next iteration according to the then-current schedule logic.You cannot cancel the existing scheduled instance to make the next instance run earlier. When you cancel an instance of a recurring task chain, the server automatically schedules the next instance for the next time that matches the scheduling criteria. It never schedules a new instance for earlier than or the same time as one that you manually canceled. |

---

---
title: About recurring tasks and task chains
description: You can use the admin console to create recurring tasks and task chains to perform regular maintenance tasks for the PingDirectory server. These tasks can perform regular backups, LDIF exports, enter and exit lockdown mode, or other static operations.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_recurring_task_chains_2
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_recurring_task_chains_2.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# About recurring tasks and task chains

You can use the admin console to create recurring tasks and task chains to perform regular maintenance tasks for the PingDirectory server. These tasks can perform regular backups, LDIF exports, enter and exit lockdown mode, or other static operations.

Because this process is owned by the server, tasks do not require special privileges or credentials, and they can be run when the server is offline.

Create recurring tasks and add them to a recurring task chain for scheduling. The task chain ensures that invocations of a task or set of tasks run in a specified order and do not overlap.

A recurring task includes:

* The task-specific object classes to include in the task entry

* The task-specific attributes to include in the task entry, if any

* Whether to alert on task start, success, or failure

* Any addresses to email on task start, success, or failure

* Whether to cancel an instance of the task if it is dependent upon another task and that task does not complete successfully

After you create a task, add one or more tasks to a task chain and schedule the chain.

A recurring task chain includes:

* An ordered list of the tasks to invoke

* The months, days, times, and time zones in which each task can be scheduled to start

* The behavior to exhibit if any of the tasks are interrupted by a server shutdown

* The behavior to exhibit if the server is offline when the start time occurs

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Changing the schedule for an existing recurring task chain only takes effect the next time an instance of the chain needs to be scheduled. It does not affect any existing instances of the chain that are already scheduled. Existing scheduled instances still run at the originally scheduled time. When that run is complete, the server schedules the next iteration according to the then-current schedule logic.You cannot cancel the existing scheduled instance to make the next instance run earlier. When you cancel an instance of a recurring task chain, the server automatically schedules the next instance for the next time that matches the scheduling criteria. It never schedules a new instance for earlier than or the same time as one that you manually canceled. |

---

---
title: About soft deletes
description: Soft deletes preserve a deleted entry's attribute and uniqueness characteristics so it can be undeleted or permanently removed at a later date.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_soft_deletes
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_soft_deletes.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About soft deletes

Soft deletes preserve a deleted entry's attribute and uniqueness characteristics so it can be undeleted or permanently removed at a later date.

The standard implementation of an LDAP server allows adding, renaming, modifying, searching, comparing, and deleting one or more entries. By specification, the `delete` operation permanently removes an entry and its attributes in a Directory Information Tree (DIT) but records the changes in access, and optionally, audit and change logs. The `delete` operation severs any associations such as references and group memberships. Meta attributes, such as operational attributes, which can be unique to an entry like `entryUUID`, are lost or different if the same entry is re-added to the PingDirectory server.

There are cases where a company might want to preserve their deleted entries to allow for possible undeletion at a later date. For example, a company might want to retain account and subscriber entries for their users who leave but later rejoin. Artifacts that a user creates such as account histories, web pages, notes, can be tracked and recovered while a user is deleted or when the user returns as an active customer. Soft deletes facilitate this use-case.

A delete request can result in a soft delete either by the client explicitly requesting a soft delete or by the request matching criteria defined in an active soft delete policy. The soft-deleted entries are renamed by prefixing an `entryUUID` operational attribute to the DN and adding an auxiliary object class to the entry, `ds-soft-delete-entry`, which saves the entry in a hidden state. All active references and group memberships are then removed. While in this hidden state, clients cannot access soft-deleted entries under normal operating conditions. Only clients with the `soft-delete-read` privilege can interact with soft-deleted entries.

To allow soft deletes, the PingDirectory server's attribute uniqueness function has been relaxed to allow for the co-existence of a soft-deleted entry and an active entry with identical naming attributes, such as `uid`. For example, if a user John Smith was soft deleted, but a different John Smith was added to the user accounts system, both entries can reside in the DIT without conflict. One entry would exist in a soft-deleted state and the other in an active state. The PingDirectory server extends this capability by allowing multiple users with the same DN, who would normally conflict if active, to reside in the soft-deleted state.

Soft-deleted entries can be restored with an `undelete` operation. The same uniqueness constraints that apply when adding a new user to the PingDirectory server are enforced when a soft-deleted entry is undeleted. In the previous example, John Smith was soft-deleted, but a different John Smith with the same `uid` as the original John Smith was later added to the system. If the original John Smith was undeleted from its soft-deleted state, it would result in a conflict with the active John Smith entry. Administrators must modify the DN of the soft-deleted entry to avoid such conflicts.

Administrators can permanently remove a soft-deleted entry by performing a regular `delete` operation on it. This operation, called a hard delete, permanently removes a soft-deleted entry from the server. You can also permanently remove a regular non-soft-deleted entry using a hard delete. This is useful when the server is configured with a soft-delete policy that would otherwise turn a regular delete request into a soft delete.

The PingDirectory server provides tool arguments that can use the soft delete request control, the hard delete request control, and other controls necessary to process these operations. Procedures to show how to use these options are presented later in this section.

For replicated topologies, when a participating PingDirectory server soft deletes an entry, it notifies the other replicas in the topology to soft delete the same entry on its respective machine. The changelog backend also records these entries by annotating them using an attribute that indicates its soft-deleted state. Modification and hard deletes of soft-deleted entries are not recorded by default in the changelog but can be enabled in the server. For maximum compatibility, make sure all servers in the replication cluster support soft deletes and have identical soft delete configurations.

---

---
title: "About the <code class=\"cmdname\"><strong>manage-profile</strong></code> tool"
description: The manage-profile tool is provided with the server to work with server profiles. It includes subcommands for creating, applying, and replacing server profiles, all of which significantly reduce the effort required by an administrator to configure a server appropriately.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_manage_profile_tool
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_manage_profile_tool.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
page_aliases: ["pd_ds_manage_profile_generate_profile.adoc", "pd_ds_manage_profile_setup.adoc", "pd_ds_manage_profile_replace_profile.adoc", "pingdirectoryproxy_server_administration_guide:pd_proxy_manage_profile_tool.adoc", "pingdirectoryproxy_server_administration_guide:pd_proxy_manage_profile_gen_profile.adoc", "pingdirectoryproxy_server_administration_guide:pd_proxy_manage_profile_setup.adoc", "pingdirectoryproxy_server_administration_guide:pd_proxy_manage_profile_replace_profile.adoc", "pingdatasync_server_administration_guide:pd_sync_manage_profile_tool.adoc"]
section_ids:
  manage-profile-generate-profile: manage-profile generate-profile
  manage-profile-setup: manage-profile setup
  manage-profile-replace-profile: manage-profile replace-profile
---

# About the `manage-profile` tool

The `manage-profile` tool is provided with the server to work with server profiles. It includes subcommands for creating, applying, and replacing server profiles, all of which significantly reduce the effort required by an administrator to configure a server appropriately.

The following sections describe these subcommands in more detail. For more information about the `manage-profile` tool, run `manage-profile --help`. For more information about each individual subcommand and its options, run `manage-profile <subcommand> --help`.

## `manage-profile generate-profile`

To create a server profile from a configured server, use the `generate-profile` subcommand. The generated profile contains the following information, which provides a base for completing a profile:

* Command-line arguments that were used to set up the server

* `dsconfig` commands necessary to configure the server

* Installed server SDK extensions

* Files that are added to the server root

To produce a complete profile, some parts of the generated profile might require modifications, such as adding password files that `setup-arguments.txt` uses. The `--instanceName` and `--localHostName` arguments in `setup-arguments.txt` are made variables by `generate-profile`, and must be provided values when other `manage-profile` subcommands use the generated profile.

|   |                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------- |
|   | For the PingDirectory server, LDIF files must also be added manually to the generated server profile. |

The `--excludeSetupArguments` option generates a server profile without a setup-arguments.txt file. This is useful when generating server profiles for use with Docker images.

## `manage-profile setup`

To apply a server profile to an unconfigured server, use the `setup` subcommand, which replaces the normal setup tool when using a server profile. Run `manage-profile setup` to do the following:

1. Copy the `server-root/pre-setup` files to the server root.

2. For the PingDirectory server only, apply changes for any batch files contained in the `pre-setup-dsconfig` directory.

3. Run the setup tool.

4. Copy the `server-root/post-setup` files to the server root.

5. Install any Server SDK extensions.

6. Apply changes for any `dsconfig` batch files.

7. For the PingDirectory server only, import any LDIF files contained in the `ldif` directory structure.

8. Start the server.

`manage-profile setup` creates a copy of the profile in a temporary directory specified by the `--tempProfileDirectory` option. The tool leaves the server running upon completion unless you use the `--doNotStart` option.

## `manage-profile replace-profile`

Run the `replace-profile` subcommand on a server that was originally set up with a server profile to replace its configuration with a new profile. The tool applies a specified server profile to an existing server while preserving its data, topology configuration, and replication configuration.

|   |                                                                                                   |
| - | ------------------------------------------------------------------------------------------------- |
|   | For the PingDirectory server, new LDIF files from the replacement server profile aren't imported. |

While `manage-profile replace-profile` is running, the existing server is stopped and moved to a temporary directory that the `--tempServerDirectory` argument can specify. A fresh, new server is subsequently installed and set up with the new profile. The final server is left running if it was running before the command was started, and remains stopped if it was stopped.

Run `manage-profile replace-profile` from a second uncompressed server install package on the same host as the existing server, similar to the `update` tool. Use the `--serverRoot` argument to specify the root of the existing server that will have its profile replaced.

If files have been added or modified in the server root since the most recent `manage-profile setup` or `manage-profile replace-profile` was run, they're included in the final server with the replaced profile. Otherwise, files specifically added from the `server-root` directory of the previous server profile are absent from the final server with the replaced profile. If errors occur during the subcommand, such as the new profile having an invalid `setup-arguments.txt` file, the existing server returns to its original state from before `manage-profile replace-profile` was run.

The `--skipValidation` option skips the validation step when running on an offline server

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you run the `manage-profile replace-profile` tool with an SDK extension included in the new profile, the tool invokes the `setup` command.The `manage-profile replace-profile` tool can update the server version when needed, but will fail if you attempt to downgrade the server to an earlier version. It can also directly apply configuration changes when there are no other changes in the new profile. This is a shorter process when making small changes to `dsconfig`. |

---

---
title: About the client connection policy
description: Client connection policies are based on two factors.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_client_connection_policy
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_client_connection_policy.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# About the client connection policy

Client connection policies are based on two factors.

* Connection criteria

  The connection criteria are used in many areas within the server. They are used by the client connection policies, but they can be used in other instances when the server needs to perform matching based on connection-level properties, such as filtered logging. A single connection can match multiple connection criteria definitions.

* Evaluation order index

  If multiple client connection policies are defined in the server, then each of them must have a unique value for the `evaluation-order-index` property. The client connection policies are evaluated in order of ascending evaluation order index. If a client connection does not match the criteria for any defined client connection policy, then that connection will be terminated.

If the connection policy matches a connection, then the connection is assigned to that policy and no further evaluation occurs. If, after evaluating all of the defined client connection policies, no match is found, the connection is terminated.

---

---
title: About the configuration tools
description: You can access and modify the server configuration in two ways.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_config_tools
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_config_tools.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# About the configuration tools

You can access and modify the server configuration in two ways.

* Admin console

  The server provides an admin console for graphical server management and monitoring. The console functions are equivalent to the `dsconfig` tool for viewing or editing configurations.

  All configuration changes using the admin console are recorded in `logs/config-audit.log`, which also has the equivalent reversion commands if you need to undo a configuration.

* `dsconfig` Command-line tool

  The `dsconfig` tool is a text-based menu-driven interface to the underlying configuration. The tool runs the configuration using three operational modes:

  * Interactive command-line mode

  * Non-interactive command-line mode

  * Batch mode

  All configuration changes made using this tool are recorded in `logs/config-audit.log`.

|   |                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can [generate a summary of your server's configuration](pd_ds_generate_summary_config_components.html) to help you plan any modifications. |

---

---
title: About the dbtest Index Status table
description: The dbtest tool has a list-all --analyze option that generates the current status of all of the databases on your system, including all index databases.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_dbtest_index_status_table
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_dbtest_index_status_table.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About the dbtest Index Status table

The `dbtest` tool has a `list-all --analyze` option that generates the current status of all of the databases on your system, including all index databases.

The table shows the following information:

* Type

* Entry count (the number of records in the database)

* Index status

  * `TRUSTED` indicates the indexes are up-to-date.

  * `UNTRUSTED` indicates the index needs rebuilding.

* Each key's total data size

* Each key's average data size

* Each key's maximum data size

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
|   | Any indexes that are in exploded format are also listed in this table. |

![A screen capture of the dbtest index status table output, showing the Index Name, Index Type, JE Database Name, and Index Status columns.](_images/ymc1564011708192.png)dbtest output including index databases

---

---
title: About the dsconfig configuration tool
description: The dsconfig tool is the text-based management tool used to configure the underlying server configuration.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_dsconfig_config_tool
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_dsconfig_config_tool.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# About the dsconfig configuration tool

The `dsconfig` tool is the text-based management tool used to configure the underlying server configuration.

The `dsconfig` tool has three operational modes: interactive mode, non-interactive mode, and batch mode.

The `dsconfig` tool offers an offline mode using the `--offline` option, in which the server does not have to be running to interact with the configuration. In most cases, you should keep the server running when you access the configuration for the server to give the user feedback about the validity of the configuration.

To view the options for the dsconfig tool, change to the `PingDirectory/bin` directory, and enter `./dsconfig --help`. Example output is shown below.

```
./dsconfig --help

View and edit the Directory Server configuration.
This utility offers three primary modes of operation, the interactive mode, the non-interactive mode
and batch mode.  The interactive mode supports viewing and editing the configuration via an intuitive,
menu driven environment.  Running dsconfig in interactive command-line mode provides a user-friendly,
menu-driven interface for accessing and configuring the server. To start dsconfig in interactive
command-line mode, simply invoke the dsconfig shell script or batch file without any arguments.

The dsconfig non-interactive command-line mode provides a simple way to make arbitrary changes to the
Ping Identity Directory Server by invoking it on the command-line. If you want to use administrative
scripts to automate the configuration process, then run the dsconfig command in non-interactive mode.

The dsconfig tool provides a batching mechanism that reads multiple dsconfig invocations from a file
and executes them sequentially.  The batch file provides advantages over standard scripting in that it
minimizes LDAP connections and JVM invocations that normally occur with each dsconfig call.  You can
view the logs/config-audit.log file to review the configuration changes made to the Ping Identity
Directory Server and use them in the batch file.

Subcommands

  See the Usage section for instructions on viewing the list of supported subcommands.

Usage:  dsconfig  {options}
        where {options} include:

    --applyChangeTo [server-group|server-group-force|single-server]
        Controls whether changes apply to a single server or all servers in the configuration server group
    --offline
        Interact with the local configuration while the server is offline.  Not for use while the server
        is running
    -r, --reason {reason}
        A string describing the reason for the configuration change
    --help-classifications
        Display subcommands relating to connection and operation classification
    --help-core-server
        Display subcommands relating to core
    --help-database
        Display subcommands relating to backends, indexing, and caching
    --help-logging
        Display subcommands relating to logging, monitoring, and notifications
    --help-replication
        Display subcommands relating to replication
    --help-security
        Display subcommands relating to security and authorization
    --help-topology
        Display subcommands relating to topology
    --help-user-management
        Display subcommands relating to authentication and password management
    --help-web
        Display subcommands relating to web services and applications
    --help-subcommands
        Display all subcommands

  Configuration Options

    --advanced
        Allow the configuration of advanced components and properties

  LDAP Connection Options

    -Z, --useSSL
        Use SSL for secure communication with the server
    -q, --useStartTLS
        Use StartTLS to secure communication with the server
    --useNoSecurity
        Use no security when communicating with the server
    -h, --hostname {host}  [Default: localhost]
        Directory Server hostname or IP address
    -p, --port {port}  [Default: 389]
        Directory Server port number
    -D, --bindDN {bindDN}  [Default: cn=Directory Manager]
        DN used to bind to the server
    -w, --bindPassword {bindPassword}
        Password used to bind to the server
    -j, --bindPasswordFile {bindPasswordFile}
        Bind password file
    -o, --saslOption {name=value}
        SASL bind options (can be specified multiple times)
    -X, --trustAll
        Trust all server SSL certificates
    -P, --trustStorePath {truststorePath}  [Default: /Users/rowannabobo/Desktop/PingDirectory_9.2/config/truststore]
        Certificate truststore path
    -T, --trustStorePassword {truststorePassword}
        Certificate truststore PIN
    -U, --trustStorePasswordFile {path}
        Certificate truststore PIN file
    --trustStoreFormat {trustStoreFormat}
        Certificate truststore format
    -K, --keyStorePath {keystorePath}
        Certificate keystore path
    -W, --keyStorePassword {keystorePassword}
        Certificate keystore PIN
    -u, --keyStorePasswordFile {keystorePasswordFile}
        Certificate keystore PIN file
    --keyStoreFormat {keyStoreFormat}
        Certificate keystore format
    -N, --certNickname {nickname}
        Nickname of the certificate for SSL client authentication

  Utility Input/Output Options

    -v, --verbose
        Use verbose mode
    -Q, --quiet
        Use quiet mode
    -n, --no-prompt
        Use non-interactive mode.  If data in the command is missing, you will not be prompted and the
        tool will fail
    -F, --batch-file {batchFilePath}
        Path to a file containing a sequence of dsconfig commands to run
    --batch-continue-on-error
        Force the execution of all commands in the batch file on the server even if prevalidation fails.
        Execution will also continue even if one of the commands fails.
        Please note that commands affecting multiple servers can still fail to execute unless the
        --applyChangeTo argument is provided with the value server-group-force. Only applies if the batch
        file argument is also supplied.
    --dry-run
        Validate configuration changes but do not apply them. This option can only be used along with the
        -F/--batch-file option
    --propertiesFilePath {propertiesFilePath}
        Path to the file that contains default property values used for command-line arguments
    --noPropertiesFile
        Specify that no properties file will be used to get default command-line argument values
    --script-friendly
        Use script-friendly mode

  General Options

    -V, --version
        Display Directory Server version information
    -?, -H, --help
        Display general usage information
    --help-ldap
        Display help for using LDAP options
    --help-sasl
        Display help for using SASL options
    --help-debug
        Display help for using debug options

Examples

  Start dsconfig in interactive mode:

    dsconfig

  Use non-interactive mode to change the amount memory used for caching database contents and to specify
  common parent DNs that should be compacted in the underlying database:

    dsconfig --no-prompt --bindDN uid=admin,dc=example,dc=com \
         --bindPassword password set-backend-prop --backend-name userRoot \
         --set db-cache-percent:40 \
         --add compact-common-parent-dn:ou=accts,dc=example,dc=com \
         --add compact-common-parent-dn:ou=subs,dc=example,dc=com

  Use batch mode to read and execute a series of commands in a batch file:

    dsconfig --bindDN uid=admin,dc=example,dc=com --bindPassword password \
         --no-prompt --batch-file /path/to/config-batch.txt

  List information about all available configuration properties for all objects, including inherited properties:

    dsconfig list-properties --offline --inherited

  For examples and help with LDAP options see --help-ldap.  For help with SASL authentication, see --help-sasl
```
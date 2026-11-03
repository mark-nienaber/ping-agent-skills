---
title: Filter synchronization data
description: Filter synchronization data using scripts, conditions, and queries
component: pingoneaic
page_id: pingoneaic:idm-synchronization:chap-restricting-sync
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/chap-restricting-sync.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization"]
section_ids:
  filtering-source-and-target: Filter source and target objects with scripts
  recon-by-query: Restrict reconciliation by using queries
  restricting-recons-ui: Restrict reconciliation queries using the admin console
  recon-by-id: Restrict reconciliation to a specific ID
  restricting-implicit-sync: Restrict implicit synchronization to specific property changes
---

# Filter synchronization data

By default, Advanced Identity Cloud synchronizes all objects that match those defined in the connector configuration for the resource. Many connectors let you limit the scope of objects that the connector accesses. For example, the LDAP connector lets you specify base DNs and LDAP filters so that you do not need to access every entry in the directory.

The following sections describe other ways to filter out objects or attributes to restrict the synchronization load.

## Filter source and target objects with scripts

You can filter the source or target objects that are included in a synchronization operation using the `validSource`, `validTarget`, or `sourceCondition` properties in your mapping:

* `validSource`

  A script that determines if a source object is valid to be mapped.

  The script yields a boolean value: `true` indicates that the source object is valid; `false` can be used to defer mapping until some condition is met. In the root scope, the source object is provided in the `"source"` property. If the script is not specified, then all source objects are considered valid:

  ```json
  {
      "validSource": {
          "type": "text/javascript",
          "source": "source.ldapPassword != null"
      }
  }
  ```

* `validTarget`

  A script used during the second phase of reconciliation that determines if a target object is valid to be mapped.

  The script yields a boolean value: `true` indicates that the target object is valid; `false` indicates that the target object should not be included in reconciliation. In the root scope, the source object is provided in the `"target"` property. If a `validTarget` the script is not specified, then all target objects are considered valid for mapping:

  ```json
  {
      "validTarget": {
          "type": "text/javascript",
          "source": "target.employeeType == 'internal'"
      }
  }
  ```

* `sourceCondition`

  An additional filter that must be met for a source object to be included in a mapping.

  This condition works like a `validSource` script. Its value can be either a `queryFilter` string, or a script configuration. `sourceCondition` is used mainly to specify that a mapping applies only to a particular role or entitlement.

  The following `sourceCondition` restricts synchronization to those user objects whose account status is `active`:

  ```json
  {
      "mappings": [
          {
              "name": "managedUser_systemLdapAccounts",
              "source": "managed/realm-name_user",
              "sourceCondition": "/source/accountStatus eq \"active\"",
          ...
          }
      ]
  }
  ```

During synchronization, scripts and filters have access to a `source` object and a `target` object. Examples already shown in this section use `source.attributeName` to retrieve attributes from the source objects. Scripts can also write to target attributes using `target.attributeName` syntax, for example:

```json
{
    "onUpdate": {
        "type": "text/javascript",
        "source": "if (source.email != null) {target.mail = source.email;}"
    }
}
```

The `sourceCondition` filter also has the `linkQualifier` variable in its scope.

For more information about functions in identity-related scripts, refer to [scripting functions](../idm-scripting/scripting-func-engine.html).

## Restrict reconciliation by using queries

Every reconciliation operation performs a query on the source and on the target resource, to determine which records should be reconciled. The default source and target queries are `_queryFilter=true&_fields=_id`, which means that all records in both the source and the target are considered candidates for that reconciliation operation.

You can restrict reconciliation to specific entries by defining an explicit `sourceQuery` or `targetQuery` in the mapping configuration.

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | The `sourceQuery` filter is ignored during the target phase, and the `targetQuery` filter is ignored during the source phase. |

For example, to restrict reconciliation to those records whose `employeeType` on the source resource is `Permanent`, you might specify a source query as follows:

```json
"mappings" : [
     {
         "name" : "managedUser_systemLdapAccounts",
         "source" : "managed/realm-name_user",
         "target" : "system/ldap/account",
         "sourceQuery" : {
            "_queryFilter" : "employeeType eq \"Permanent\""
         },
...
```

The format of the query can be any query type that is supported by the resource, and can include additional parameters, if applicable. Use the `_queryFilter` parameter, in common filter notation.

The source and target queries send the query to the resource that is defined for that source or target, by default. You can override the resource the query is sent to by specifying a `resourceName` in the query. For example, to query a specific endpoint instead of the source resource, you might modify the preceding source query as follows:

```json
{
    "mappings" : [
        {
            "name" : "managedUser_systemLdapAccounts",
            "source" : "managed/realm-name_user",
            "target" : "system/ldap/account",
            "sourceQuery" : {
                "resourceName" : "endpoint/scriptedQuery"
                "_queryFilter" : "employeeType eq \"Permanent\""
            },
            ...
}
```

To override a source or target query that is defined in the mapping, you can specify the query when you call the reconciliation operation. For example, to reconcile all employee entries, and not just the permanent employees, you would run the reconciliation operation as follows:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{"sourceQuery": {"_queryFilter" : "true"}}' \
"https://<tenant-env-fqdn>/openidm/recon?_action=recon&mapping=managedUser_systemLdapAccounts"
```

By default, a reconciliation operation runs both the source and target phase. To avoid queries on the target resource, set `runTargetPhase` to `false` in the mapping configuration. To prevent the target resource from being queried during the reconciliation operation configured in the previous example, amend the mapping configuration as follows:

```json
{
    "mappings" : [
        {
            "name" : "systemLdapAccounts_managedUser",
            "source" : "system/ldap/account",
            "target" : "managed/realm-name_user",
            "sourceQuery" : {
                "_queryFilter" : "employeeType eq \"Permanent\""
            },
            "runTargetPhase" : false,
   ...
```

### Restrict reconciliation queries using the admin console

To restrict a mapping's reconciliation queries, use the [Advanced Sync](../identities/advanced-sync.html) editor's [advanced reconciliation settings](../identities/advanced-sync-advanced-reconciliation.html).

## Restrict reconciliation to a specific ID

You can restrict reconciliation to a specific record in much the same way as you restrict reconciliation by using queries.

To restrict reconciliation to a specific ID, use the `reconById` action, instead of the `recon` action when you call the reconciliation operation. Specify the ID with the `id` parameter.

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | Reconciling more than one ID with the `reconById` action is not supported. |

The following command reconciles only the user with ID `b3c2f414-e7b3-46aa-8ce6-f4ab1e89288c`, for the mapping `managedUser_systemLdapAccounts`. The command synchronizes this particular user account in LDAP with the data from the managed user repository. The example assumes that implicit synchronization has been disabled, and that a reconciliation operation is required to copy changes made in the repository to the LDAP system:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/recon?_action=reconById&mapping=managedUser_systemLdapAccounts&id=b3c2f414-e7b3-46aa-8ce6-f4ab1e89288c"
```

Reconciliation by ID takes the default reconciliation options that are specified in the mapping, so the source and target queries, and source and target phases apply equally to reconciliation by ID.

## Restrict implicit synchronization to specific property changes

For a mapping that has managed objects as the source, an implicit synchronization is triggered if *any* source property changes, regardless of whether the modified property is explicitly defined as a `source` property in the mapping.

This default behavior is helpful in situations where no source properties are explicitly defined—any property within the object is included as part of the mapping.

However, this behavior adds a processing overhead, because every mapping from the managed object is invoked when *any* managed object property changes. If several mappings are configured from the managed object, this default behavior can cause performance issues.

In these situations, you can restrict the properties that should trigger an implicit synchronization *per mapping*, using the `triggerSyncProperties` attribute. This attribute contains an array of JSON pointers to the properties that must change before an implicit synchronization to the target is triggered. If none of these properties changes, no synchronization is triggered, even if other properties in the object change.

In the following example, implicit synchronization is triggered *only* if the `mail`, `telephoneNumber`, or `userName` of an object changes:

```json
{
    "mappings" : [
        {
            "name" : "managedUser_systemLdapAccounts",
            "source" : "managed/realm-name_user",
            "target" : "system/ldap/account",
            "enableLinking" : false,
            "triggerSyncProperties" : [
                "/mail",
                "/telephoneNumber",
                "/userName"
            ],
            "properties" : [],
            "policies" : []
        }
    ]
}
```

If any other property changes on the managed object, no implicit synchronization is triggered.

---

---
title: How Advanced Identity Cloud assesses synchronization situations
description: Understand how Advanced Identity Cloud assesses synchronization situations
component: pingoneaic
page_id: pingoneaic:idm-synchronization:sync-situations
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/sync-situations.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization"]
---

# How Advanced Identity Cloud assesses synchronization situations

Advanced Identity Cloud performs reconciliation in two phases:

1. *Source reconciliation* accounts for source objects and associated links based on the configured mapping.

2. *Target reconciliation* iterates over the target objects that were not processed in the first phase.

   For example, if a source object was deleted, the *source reconciliation* phase will not identify the target object that was previously linked to that source object. Instead, this *orphaned* target object is detected during the second phase.

---

---
title: Import bulk data
description: Import bulk CSV data into managed objects with reconciliation and error handling
component: pingoneaic
page_id: pingoneaic:idm-synchronization:import-data
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/import-data.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization"]
---

# Import bulk data

The bulk import facility lets you import large numbers of external entries over REST. You import entries from a comma-separated values (CSV) file, to a specified managed object type in the Advanced Identity Cloud repository. Bulk import works as follows:

* Loads bulk CSV entries and stores them temporarily (in the Advanced Identity Cloud repository) as JSON objects

* Creates a temporary mapping between those entries and the managed object store in the repository

* Performs a reconciliation between the JSON objects and the objects in the repository

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The bulk import mechanism assumes that the CSV file is the *authoritative* data source. If you run an import more than once, the import overwrites all of the properties of the managed object (including timestamps) with the values in the CSV file. |

To import bulk CSV entries into the repository, using the REST API, follow these steps:

> **Collapse: Generate a CSV Template**
>
> The first time you upload entries, you must generate a CSV template. The template is essentially an empty CSV file with one header row that matches the managed object type to which you are importing. In most cases, you will be importing data that fits the `managed/realm-name_user` object model, but you can import any managed object type, such as roles and assignments.
>
> To generate the CSV template, send a GET request to the `openidm/csv/template` endpoint. The following request generates a CSV template for the managed user object type:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "https://<tenant-env-fqdn>/openidm/csv/template?resourceCollection=managed/realm-name_user&_fields=header&_mimeType='text/plain'"
> {
>   "_id": "template",
>   "header": "\"userName\",\"givenName\",\"sn\",\"mail\",\"description\",\"accountStatus\",\"telephoneNumber\",
>  \"postalAddress\",\"city\",\"postalCode\",\"country\",\"stateProvince\",\"preferences/updates\",
>  \"preferences/marketing\""
> }
> ```
>
> The template is generated based on the specified `resourceCollection`, and includes a single header row. The names of each header column are derived from the schema of the managed object type. The template includes only a subset of managed user properties that can be represented by CSV fields.
>
> Only the following managed object properties are included in the header row:
>
> * Properties of type `string`, `boolean`, and `number`
>
> * Properties that do *not* start with an underscore (such as `_id` or `_rev`)
>
>   If you are importing entries to `managed/realm-name_user`, the bulk import facility assumes that self-service password reset is enabled. This is because the import does not support upload of hashed passwords.
>
> * Properties whose `scope` is not `private`
>
> Set the parameters `_fields=header` and `_mimeType=text/csv` to download the template as a CSV file.
>
> When you have generated the template, export your external data to CSV format, using the headers in the generated template.

> **Collapse: Upload a CSV File**
>
> The default maximum file size for bulk import is 50MBytes. If you need to import a number of records that exceeds this size, divide the data into chunks and import each file separately.
>
> When you have a CSV file, with the structure of the template generated in the previous example, upload the file to the Advanced Identity Cloud repository with the following request:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --form upload=@/path/to/example-users.csv \
> --request POST \
> "http://<tenant-env-fqdn>/upload/csv/managed/realm-name_user?uniqueProperty=userName"
> {
>   "importUUIDs": [
>     "3ebd514f-bdd7-491f-928f-21b72f44e381"
>   ]
> }
> ```
>
> * `--form` (`-F`)
>
>   This option causes `curl` to POST data using the Content-Type `multipart/form-data`, which lets you upload binary files. To indicate that the form content is a file, prefix the file name with an `@` sign.
>
>   To import more than one file at once, specify multiple `--form` options, for example:
>
>   ```
>   --form upload=@/path/to/example-users-a-j.csv \
>   --form upload=@/path/to/example-users-k-z.csv \
>   ```
>
> * `uniqueProperty` (required)
>
>   This parameter lets you correlate existing entries, based on a unique value field. This is useful if you need to upload the same file a number of times (for example, if data in the file changes, or if some entries in the file contained errors). You can specify any unique value property here. You can also correlate on more than one property by specifying multiple, comma-delimited unique properties.
>
> A successful upload generates an array of `importUUID`s. You need these UUIDs to perform other operations on the import records.
>
> |   |                                                                                   |
> | - | --------------------------------------------------------------------------------- |
> |   | Note that the endpoint (`upload/csv`) is not an Advanced Identity Cloud endpoint. |

> **Collapse: Query Bulk Imports**
>
> A query on the `csv/metadata` endpoint returns the import ID, the data structure (header fields in the CSV file), a recon ID, and a number of fields indicating the status of the import:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "https://<tenant-env-fqdn>/openidm/csv/metadata/?_queryFilter=true"
> {
>   "result": [
>     {
>       "_id": "3ebd514f-bdd7-491f-928f-21b72f44e381",
>       "_rev": "000000003e8ef4f7",
>       "header": [
>         "userName",
>         "givenName",
>         "sn",
>         "mail",
>         "description",
>         "accountStatus",
>         "country"
>       ],
>       "reconId": "2e2cf41a-c4b8-4dda-9d92-6e0af65a15fe-6528",
>       "filename": "example-users.csv",
>       "resourcePath": "managed/realm-name_user",
>       "total": 1000,
>       "success": 1000,
>       "failure": 0,
>       "created": 1000,
>       "updated": 0,
>       "unchanged": 0,
>       "begin": "2020-04-17T16:31:02.955Z",
>       "end": "2020-04-17T16:31:09.861Z",
>       "cancelled": false,
>       "importDeleted": false,
>       "tempRecords": 0,
>       "purgedTempRecords": true,
>       "purgedErrorRecords": false,
>       "authId": "openidm-admin",
>       "authzComponent": "internal/user"
>     },
>     {
>       "_rev": "00000000d4392fc8"
>     }
>   ],
>   ...
> }
> ```

> **Collapse: Query Imports To a Specific Object Type**
>
> Use a query filter to restrict your query to imports to a specific managed object type. The following example queries uploads to the managed user object:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'https://<tenant-env-fqdn>/openidm/csv/metadata/?_queryFilter=/resourcePath+eq+"managed/realm-name_user"'
> {
>   "result": [
>     {
>       "_id": "82d9a643-8b03-4cec-86fc-3e09c4c2f01c",
>       "_rev": "000000009b3ff60b",
>       "header": [
>         "userName",
>         "givenName",
>         "sn",
>         "mail",
>         "description",
>         "accountStatus",
>         "country"
>       ],
>       "reconId": "417dae3b-c939-4191-acbf-6eb1b9e802af-53335",
>       "filename": "example-users.csv",
>       "resourcePath": "managed/realm-name_user",
>       "total": 1001,
>       "success": 1000,
>       "failure": 1,
>       "created": 0,
>       "updated": 0,
>       "unchanged": 1000,
>       "begin": "2020-04-20T13:12:03.028Z",
>       "end": "2020-04-20T13:12:05.222Z",
>       "cancelled": false,
>       "importDeleted": false,
>       "tempRecords": 0,
>       "purgedTempRecords": true,
>       "purgedErrorRecords": false,
>       "authId": "openidm-admin",
>       "authzComponent": "internal/user"
>     }
>   ],
>   ...
> }
> ```

> **Collapse: Handle Failed Import Records**
>
> The previous example showed the statistics that are returned when you query bulk imports. One of these fields is `"failure": 0,`. If the import was unsuccessful for any records, this `failure` field will have a positive value. You can then download the failed records, examine the failures and correct them in the CSV file, then run the import again.
>
> To download failed records, send a GET request to the endpoint `export/csvImportFailures/importUUID`:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --request GET \
> --header "Accept-API-Version: resource=1.0" \
> "http://<tenant-env-fqdn>/export/csvImportFailures/82d9a643-8b03-4cec-86fc-3e09c4c2f01c"
> userName,  givenName,  sn,      mail,     ...,  _importError
> emacheke,  Edward,     Macheke, emacheke, ...,  "{code=403, reason=Forbidden, message=Policy validation
>    failed, detail={result=false, failedPolicyRequirements=[{policyRequirements=[
>    {policyRequirement=VALID_EMAIL_ADDRESS_FORMAT}], property=mail}]}}"
> ```
>
> The output indicates the failed record or records, and the reason for the failure, in the `_importError` field. In this example, the import failed because of a policy validation error—the email address is not the correct format.
>
> |   |                                                                                                                                                                                                                                                                 |
> | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | Advanced Identity Cloud does not scan for possible [CSV injection](https://owasp.org/www-community/attacks/CSV_Injection) attacks on uploaded files. *Do not* edit the downloaded CSV file with Microsoft Excel, as this can expose your data to CSV injection. |

> **Collapse: Cancel an Import in Progress**
>
> Cancel an import that is in progress by sending a POST request to the `openidm/csv/metadata/importUUID` endpoint, with the `cancel` action. You may want to cancel an import if the import is taking too long, or if you have noticed problems with the import data, for example:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request POST \
> "https://<tenant-env-fqdn>/openidm/csv/metadata/92971c92-67bb-4ae7-b41b-96d249b0b2aa/?_action=cancel"
> {
>   "status": "OK"
> }
> ```

> **Collapse: HTTP Request Timeout**
>
> By default, the timeout for the bulk import servlets is 30 seconds (or `30000` milliseconds). This parameter is set in your `resolver/boot.properties` file, as follows:
>
> ```properties
> openidm.servlet.timeoutMillis=30000
> ```
>
> If you are importing a very large number of records, you might need to increase the HTTP request timeout to prevent requests timing out.
>
> In test environments, you can set this parameter to `0` to disable the request timeout. You should *not* disable the timeout in a production environment because no timeout can lead to DDoS attacks where thousands of slow HTTP connections are made.

For a list of all REST endpoints related to bulk import, refer to [Bulk import](../idm-rest-api/endpoints/rest-bulk-import.html).

---

---
title: Manage liveSync
description: Trigger, manage, and troubleshoot liveSync operations over REST
component: pingoneaic
page_id: pingoneaic:idm-synchronization:manage-livesync
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/manage-livesync.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization"]
section_ids:
  trigger-livesync-ui: Trigger liveSync using the admin console
  troubleshooting-livesync: Troubleshoot liveSync failures
---

# Manage liveSync

Because you can trigger liveSync operations using REST (or the resource API) you can use an external scheduler to trigger liveSync operations, rather than using the Advanced Identity Cloud scheduling mechanism.

There are two ways to trigger liveSync over REST:

* Use the `_action=liveSync` parameter directly on the resource. This is the recommended method. The following example calls liveSync on the user accounts in an external LDAP system:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --request POST \
  "https://<tenant-env-fqdn>/openidm/system/ldap/account?_action=liveSync"
  ```

* Target the `system` endpoint and supply a `source` parameter to identify the object that should be synchronized. This method matches the scheduler configuration and can therefore be used to test schedules before they are implemented.

  The following example calls the same liveSync operation as the previous example:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --request POST \
  "https://<tenant-env-fqdn>/openidm/system?_action=liveSync&source=system/ldap/account"
  ```

A successful liveSync operation returns the following response:

```json
{
     "_rev": "000000001ade755f",
     "_id": "SYSTEMLDAPACCOUNT",
     "connectorData": {
         "nativeType": "integer",
         "syncToken": 1
     }
}
```

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Do not run two identical liveSync operations simultaneously. Rather, ensure that the first operation has completed before launching a second, similar operation. |

## Trigger liveSync using the admin console

LiveSync operations are specific to a system object type (such as `system/ldap/account`).

You can trigger liveSync operations on-demand using REST as described in the previous section.

To schedule liveSync using the admin console, learn more in [Manage provisioner schedules](../app-management/standalone-provisioner-schedules.html).

## Troubleshoot liveSync failures

To troubleshoot a liveSync operation that has not succeeded, include the `detailedFailure` parameter to return additional information. For example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/system/ldap/account?_action=liveSync&detailedFailure=true"
```

The first time liveSync is called, it does not have a synchronization token in the database to establish which changes have already been processed. The default liveSync behavior is to locate the last existing entry in the change log, and to store that entry in the database as the current starting position from which changes should be applied. This behavior prevents liveSync from processing changes that might already have been processed during an initial data load. Subsequent liveSync operations will pick up and process any new changes.

Typically, in setting up liveSync on a new system, you would load the data initially (by using reconciliation, for example) and then enable liveSync, starting from that base point.

In the case of DS, the change log (`cn=changelog`) can be read only by `uid=admin` by default. If you are configuring liveSync with DS, the `principal` that is defined in the LDAP connector configuration must have access to the change log. For information about allowing a regular user to read the change log, refer to [Allow a User or Application to Read the Change Log](https://docs.pingidentity.com/pingds/8/config-guide/replication.html#read-ecl-as-regular-user).

If the following error message is present, you might have forgotten to set `changelog-read` access for a regular user:

```
Unable to locate the DS replication change log suffix. Please make
sure it's enabled, and changelog-read access is granted.
```

---

---
title: Manage reconciliation
description: Trigger, cancel, and monitor reconciliation operations with detailed statistics
component: pingoneaic
page_id: pingoneaic:idm-synchronization:manage-recon
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/manage-recon.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Reconciliation"]
section_ids:
  triggering-recons: Trigger a reconciliation
  cancel-recon: Cancel a reconciliation
  list-recons: List reconciliation history
  recon-run-props: Reconciliation properties
  recon-details: Reconciliation details
  recon-details-ui: View reconciliation details using the admin console
  recon-assoc: Reconciliation association details
  recon-delete: Purge reconciliation statistics
---

# Manage reconciliation

To trigger, cancel, and monitor reconciliation operations over REST, use the `openidm/recon` REST endpoint. You can perform most of these actions in the Advanced Identity Cloud admin console. Learn more in [Advanced synchronization reconciliation](../identities/advanced-sync-reconciliation.html).

## Trigger a reconciliation

The following example triggers a reconciliation operation over REST based on the `systemLdapAccounts_managedUser` mapping:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/recon?_action=recon&mapping=systemLdapAccounts_managedUser"
```

By default, a reconciliation run ID is returned immediately when the reconciliation operation is initiated. Clients can make subsequent calls to the reconciliation service, using this reconciliation run ID to query its state, and to call operations on it. For an example, refer to [Reconciliation Details](#recon-details).

The reconciliation run initiated previously would return something similar to the following:

```json
{
  "_id": "05f63bce-4aaa-492e-9e86-a702d5c9d6c0-1144",
  "state": "ACTIVE"
}
```

To complete the reconciliation operation before the reconciliation run ID is returned, set the `waitForCompletion` property to `true` when the reconciliation is initiated:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/recon?_action=recon&mapping=systemLdapAccounts_managedUser&waitForCompletion=true"
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To trigger this reconciliation in the Advanced Identity Cloud admin console, use the [Advanced Sync](../identities/advanced-sync.html) editor's reconciliation controls. Learn more in [Run a manual reconciliation](../identities/advanced-sync-reconciliation.html#advanced-sync-manual-recon).If you click Cancel Reconciliation before it completes, you must start the reconciliation again. |

## Cancel a reconciliation

To cancel an in progress reconciliation, specify the reconciliation run ID. The following REST call cancels the reconciliation run initiated in the previous section:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/recon/0890ad62-4738-4a3f-8b8e-f3c83bbf212e?_action=cancel"
```

The output for a reconciliation cancellation request is similar to the following:

```json
{
    "status":"INITIATED",
    "action":"cancel",
    "_id":"0890ad62-4738-4a3f-8b8e-f3c83bbf212e"
}
```

If the reconciliation run is waiting for completion before its ID is returned, obtain the reconciliation run ID from the list of active reconciliations, as described in the following section.

|   |                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To cancel a reconciliation run in progress in the Advanced Identity Cloud admin console, use the Advanced Sync editor's reconciliation controls. Learn more in [Advanced synchronization reconciliation](../identities/advanced-sync-reconciliation.html). |

## List reconciliation history

Display a list of reconciliation processes that have completed, and those that are in progress, by running a RESTful GET on `"https://<tenant-env-fqdn>/openidm/recon"`.

The following example displays all reconciliation runs:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/recon"
```

> **Collapse: Example Output**
>
> The output is similar to the following, with one item for each reconciliation run:
>
> ```json
> "reconciliations": [
>     {
>       "_id": "05f63bce-4aaa-492e-9e86-a702d5c9d6c0-1144",
>       "mapping": "systemLdapAccounts_managedUser",
>       "state": "SUCCESS",
>       "stage": "COMPLETED_SUCCESS",
>       "stageDescription": "reconciliation completed.",
>       "progress": {
>         "source": {
>           "existing": {
>             "processed": 2,
>             "total": "2"
>           }
>         },
>         "target": {
>           "existing": {
>             "processed": 0,
>             "total": "0"
>           },
>           "created": 2,
>           "unchanged": 0,
>           "updated": 0,
>           "deleted": 0
>         },
>         "links": {
>           "existing": {
>             "processed": 0,
>             "total": "0"
>           },
>           "created": 2
>         }
>       },
>       "situationSummary": {
>         "SOURCE_IGNORED": 0,
>         "FOUND_ALREADY_LINKED": 0,
>         "UNQUALIFIED": 0,
>         "ABSENT": 2,
>         "TARGET_IGNORED": 0,
>         "MISSING": 0,
>         "ALL_GONE": 0,
>         "UNASSIGNED": 0,
>         "AMBIGUOUS": 0,
>         "CONFIRMED": 0,
>         "LINK_ONLY": 0,
>         "SOURCE_MISSING": 0,
>         "FOUND": 0
>       },
>       "statusSummary": {
>         "SUCCESS": 2,
>         "FAILURE": 0
>       },
>       "durationSummary": {
>         "sourceQuery": {
>           "min": 42,
>           "max": 42,
>           "mean": 42,
>           "count": 1,
>           "sum": 42,
>           "stdDev": 0
>         },
>         "auditLog": {
>           "min": 0,
>           "max": 1,
>           "mean": 0,
>           "count": 24,
>           "sum": 15,
>           "stdDev": 0
>         },
>         "linkQuery": {
>           "min": 5,
>           "max": 5,
>           "mean": 5,
>           "count": 1,
>           "sum": 5,
>           "stdDev": 0
>         },
>         "targetQuery": {
>           "min": 3,
>           "max": 3,
>           "mean": 3,
>           "count": 1,
>           "sum": 3,
>           "stdDev": 0
>         },
>         "targetPhase": {
>           "min": 0,
>           "max": 0,
>           "mean": 0,
>           "count": 1,
>           "sum": 0,
>           "stdDev": 0
>         },
>         "sourceObjectQuery": {
>           "min": 6,
>           "max": 34,
>           "mean": 21,
>           "count": 22,
>           "sum": 474,
>           "stdDev": 9
>         },
>         "postMappingScript": {
>           "min": 0,
>           "max": 1,
>           "mean": 0,
>           "count": 22,
>           "sum": 17,
>           "stdDev": 0
>         },
>         "onMappingScript": {
>           "min": 0,
>           "max": 4,
>           "mean": 2,
>           "count": 22,
>           "sum": 48,
>           "stdDev": 2
>         },
>         "sourcePhase": {
>           "min": 490,
>           "max": 490,
>           "mean": 490,
>           "count": 1,
>           "sum": 490,
>           "stdDev": 0
>         }
>       },
>       "parameters": {
>         "sourceQuery": {
>           "resourceName": "system/ldap/account",
>           "queryFilter": "true",
>           "_fields": "_id"
>         },
>         "targetQuery": {
>           "resourceName": "managed/realm-name_user",
>           "queryFilter": "true",
>           "_fields": "_id"
>         }
>       },
>       "started": "2020-05-07T09:14:57.740Z",
>       "ended": "2020-05-07T09:14:58.325Z",
>       "duration": 585,
>       "sourceProcessedByNode": {}
>     }
>   ]
> ```

You can adjust the number of reconciliation runs that are stored in IDM by adding the `maxAnalysisRunsPerMapping` and `maxNonAnalysisRunsPerMapping` properties to your [mapping](mappings.html):

```json
"reconAssociation" : {
    "maxAnalysisRunsPerMapping" : 1,
    "maxNonAnalysisRunsPerMapping" : 3
}
```

In this context, *analysis* refers to reconciliation runs that are triggered with the `analyze=true` parameter. These runs don't perform any actions, but determine which actions *would* be performed in a real reconciliation. Non-analysis refers to a normal reconciliation.

In contrast, the admin console displays the results of only the most recent reconciliation. For more information, refer to [View reconciliation details using the admin console](#recon-details-ui).

### Reconciliation properties

Each reconciliation run includes the following properties:

* `_id`

  The ID of the reconciliation run.

* `mapping`

  The name of the [mapping](mappings.html).

* `state`

  The high-level state of the reconciliation run. Values can be as follows:

  * `ACTIVE`

    The reconciliation run is in progress.

  * `CANCELED`

    The reconciliation run was successfully canceled.

  * `FAILED`

    The reconciliation run was terminated because of failure.

  * `SUCCESS`

    The reconciliation run completed successfully.

* `stage`

  The current stage of the reconciliation run. Values can be as follows:

  * `ACTIVE_INITIALIZED`

    The initial stage, when a reconciliation run is first created.

  * `ACTIVE_QUERY_ENTRIES`

    Querying the source, target, and possibly link sets to reconcile.

  * `ACTIVE_RECONCILING_SOURCE`

    Reconciling the set of IDs retrieved from the mapping source.

  * `ACTIVE_RECONCILING_TARGET`

    Reconciling any remaining entries from the set of IDs retrieved from the mapping target, that were not matched or processed during the source phase.

  * `ACTIVE_LINK_CLEANUP`

    Checking whether any links are now unused and should be cleaned up.

  * `ACTIVE_PROCESSING_RESULTS`

    Post-processing of reconciliation results.

  * `ACTIVE_CANCELING`

    Attempting to abort a reconciliation run in progress.

  * `COMPLETED_SUCCESS`

    Successfully completed processing the reconciliation run.

  * `COMPLETED_CANCELED`

    Completed processing because the reconciliation run was aborted.

  * `COMPLETED_FAILED`

    Completed processing because of a failure.

* `stageDescription`

  A description of the stages described previously.

* `progress`

  The progress object has the following structure (annotated here with comments):

  ```json
  "progress":{
    "source":{             // Progress on set of existing entries in the mapping source
      "existing":{
        "processed":1001,
          "total":"1001"   // Total number of entries in source set, if known, "?" otherwise
      }
    },
    "target":{             // Progress on set of existing entries in the mapping target
      "existing":{
        "processed":1001,
          "total":"1001"     // Total number of entries in target set, if known, "?" otherwise
      },
      "created":0          // New entries that were created
    },
    "links":{              // Progress on set of existing links between source and target
      "existing":{
        "processed":1001,
          "total":"1001"     // Total number of existing links, if known, "?" otherwise
      },
    "created":0            // Denotes new links that were created
    }
  },
  ```

## Reconciliation details

To display the details of a specific reconciliation over REST, include the reconciliation run ID in the URL. The following call shows the details of the reconciliation run initiated in [Trigger a reconciliation](#triggering-recons).

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/recon/05f63bce-4aaa-492e-9e86-a702d5c9d6c0-1144"
```

> **Collapse: Example Output**
>
> ```json
> {
>   "_id": "05f63bce-4aaa-492e-9e86-a702d5c9d6c0-1144",
>   "mapping": "systemLdapAccounts_managedUser",
>   "state": "SUCCESS",
>   "stage": "COMPLETED_SUCCESS",
>   "stageDescription": "reconciliation completed.",
>   "progress": {
>     "source": {
>       "existing": {
>         "processed": 2,
>         "total": "2"
>       }
>     },
>     "target": {
>       "existing": {
>         "processed": 0,
>         "total": "0"
>       },
>       "created": 2,
>       "unchanged": 0,
>       "updated": 0,
>       "deleted": 0
>     },
>     "links": {
>       "existing": {
>         "processed": 0,
>         "total": "0"
>       },
>       "created": 2
>     }
>   },
>   "situationSummary": {
>     "SOURCE_IGNORED": 0,
>     "FOUND_ALREADY_LINKED": 0,
>     "UNQUALIFIED": 0,
>     "ABSENT": 2,
>     "TARGET_IGNORED": 0,
>     "MISSING": 0,
>     "ALL_GONE": 0,
>     "UNASSIGNED": 0,
>     "AMBIGUOUS": 0,
>     "CONFIRMED": 0,
>     "LINK_ONLY": 0,
>     "SOURCE_MISSING": 0,
>     "FOUND": 0
>   },
>   "statusSummary": {
>     "SUCCESS": 2,
>     "FAILURE": 0
>   },
>   "durationSummary": {
>     "sourceQuery": {
>       "min": 42,
>       "max": 42,
>       "mean": 42,
>       "count": 1,
>       "sum": 42,
>       "stdDev": 0
>     },
>     "auditLog": {
>       "min": 0,
>       "max": 1,
>       "mean": 0,
>       "count": 24,
>       "sum": 15,
>       "stdDev": 0
>     },
>     "linkQuery": {
>       "min": 5,
>       "max": 5,
>       "mean": 5,
>       "count": 1,
>       "sum": 5,
>       "stdDev": 0
>     },
>     "targetQuery": {
>       "min": 3,
>       "max": 3,
>       "mean": 3,
>       "count": 1,
>       "sum": 3,
>       "stdDev": 0
>     },
>     "targetPhase": {
>       "min": 0,
>       "max": 0,
>       "mean": 0,
>       "count": 1,
>       "sum": 0,
>       "stdDev": 0
>     },
>     "sourceObjectQuery": {
>       "min": 6,
>       "max": 34,
>       "mean": 21,
>       "count": 22,
>       "sum": 474,
>       "stdDev": 9
>     },
>     "postMappingScript": {
>       "min": 0,
>       "max": 1,
>       "mean": 0,
>       "count": 22,
>       "sum": 17,
>       "stdDev": 0
>     },
>     "onMappingScript": {
>       "min": 0,
>       "max": 4,
>       "mean": 2,
>       "count": 22,
>       "sum": 48,
>       "stdDev": 2
>     },
>     "sourcePhase": {
>       "min": 490,
>       "max": 490,
>       "mean": 490,
>       "count": 1,
>       "sum": 490,
>       "stdDev": 0
>     }
>   },
>   "parameters": {
>     "sourceQuery": {
>       "resourceName": "system/ldap/account",
>       "queryFilter": "true",
>       "_fields": "_id"
>     },
>     "targetQuery": {
>       "resourceName": "managed/realm-name_user",
>       "queryFilter": "true",
>       "_fields": "_id"
>     }
>   },
>   "started": "2020-05-07T09:14:57.740Z",
>   "ended": "2020-05-07T09:14:58.325Z",
>   "duration": 585,
>   "sourceProcessedByNode": {}
> }
> ```

### View reconciliation details using the admin console

You can display the details of the most recent reconciliation in the admin console. Use the [Advanced Sync](../identities/advanced-sync.html) editor's reconciliation controls.

Learn more in [Advanced synchronization reconciliation](../identities/advanced-sync-reconciliation.html).

### Reconciliation association details

When performing a reconciliation run, information is reconciled between the source object and the target object. This creates an association between the two objects, which can be recorded in IDM by including the `persistAssociations=true` parameter when triggering a reconciliation. This information can then be retrieved by querying the `recon/assoc` endpoint.

|   |                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `persistAssociations` parameter is `false` by default because setting it to `true` can cause performance issues when performing large reconciliations, and in extreme cases, can cause a system outage. Refer to [How do I troubleshoot and improve reconciliation performance in Identity Cloud?](https://backstage.pingidentity.com/knowledge/kb/article/a20158821) |

To get a list of currently stored recon associations, run the following query:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/recon/assoc?_queryFilter=true"
{
  "result": [
    {
      "_id": "da88b9a5-1fe5-4f8d-a6a8-7e0a2b4e136b-9230",
      "_rev": "1",
      "mapping": "managedUser_systemLdapAccounts",
      "sourceResourceCollection": "managed/realm-name_user",
      "targetResourceCollection": "system/ldap/account",
      "isAnalysis": "false",
      "finishTime": "2019-05-01T23:36:24.434153Z"
    },
    {
      "_id": "da88b9a5-1fe5-4f8d-a6a8-7e0a2b4e136b-99638",
      "_rev": "1",
      "mapping": "systemLdapAccounts_managedUser",
      "sourceResourceCollection": "system/ldap/account",
      "targetResourceCollection": "managed/realm-name_user",
      "isAnalysis": "true",
      "finishTime": "2019-05-06T21:31:42.140066Z"
    }
  ],
  "resultCount": 2,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

You can also get information for a specific reconciliation by querying the recon ID:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/recon/assoc/da88b9a5-1fe5-4f8d-a6a8-7e0a2b4e136b-9230"
{
  "_id": "da88b9a5-1fe5-4f8d-a6a8-7e0a2b4e136b-9230",
  "_rev": "1",
  "mapping": "managedUser_systemLdapAccounts",
  "sourceResourceCollection": "managed/realm-name_user",
  "targetResourceCollection": "system/ldap/account",
  "isAnalysis": "false",
  "finishTime": "2019-05-01T23:36:24.434153Z"
}
```

It is possible to also get the specific association details of each entry in the reconciliation run by appending `/entry` to your query:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/recon/assoc/da88b9a5-1fe5-4f8d-a6a8-7e0a2b4e136b-9230/entry?_queryFilter=true"
{
  "result": [
    {
      "_id": "400d40fd-da58-41f5-857b-71855eb97bd9",
      "_rev": "0",
      "mapping": "managedUser_systemLdapAccounts",
      "reconId": "da88b9a5-1fe5-4f8d-a6a8-7e0a2b4e136b-9230",
      "situation": "CONFIRMED",
      "action": "UPDATE",
      "linkQualifier": "default",
      "sourceObjectId": "07978ba5-b31d-4f8b-9f60-506c07f68495",
      "targetObjectId": "ca8abc7f-7b97-3e96-94fb-6b27b0ec5aed",
      "sourceResourceCollection": "managed/realm-name_user",
      "targetResourceCollection": "system/ldap/account",
      "status": "SUCCESS",
      "exception": null,
      "message": null,
      "messageDetail": "null",
      "ambiguousTargetObjectIds": null
    },
    ...
    {
      "_id": "08ec633c-744f-4092-b88d-fe253b1d8e52",
      "_rev": "0",
      "mapping": "managedUser_systemLdapAccounts",
      "reconId": "da88b9a5-1fe5-4f8d-a6a8-7e0a2b4e136b-9230",
      "situation": "CONFIRMED",
      "action": "UPDATE",
      "linkQualifier": "default",
      "sourceObjectId": "ee2449a8-01e6-4c0b-84d3-e65e25c3e38c",
      "targetObjectId": "67a6596e-ebfc-3542-a664-1ab1610e082a",
      "sourceResourceCollection": "managed/realm-name_user",
      "targetResourceCollection": "system/ldap/account",
      "status": "SUCCESS",
      "exception": null,
      "message": null,
      "messageDetail": "null",
      "ambiguousTargetObjectIds": null
    }
  ],
  ...
}
```

|   |                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For particularly large reconciliations, the results returned can be quite substantial, since it includes the details of every object reconciled. We encourage using query filters to tune your queries to only return the subset of results you're looking for. |

### Purge reconciliation statistics

When the number of completed reconciliation runs for a given mapping reaches the number specified by `maxAnalysisRunsPerMapping` or `maxNonAnalysisRunsPerMapping`, statistics are purged automatically. Statistics and reconciliation run information (such as recon associations) are purged chronologically by mapping, with the oldest reconciliation run for that mapping purged first.

You can also manually remove reconciliation statistics. To purge reconciliation statistics from the repository manually, run a DELETE command on the reconciliation run ID. For example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request DELETE \
"https://<tenant-env-fqdn>/openidm/recon/da88b9a5-1fe5-4f8d-a6a8-7e0a2b4e136b-9230"
```

---

---
title: Map a single source object to multiple target objects
description: Map single source object to multiple target objects using link qualifiers
component: pingoneaic
page_id: pingoneaic:idm-synchronization:linking-multiple-targets
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/linking-multiple-targets.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Mappings"]
section_ids:
  link-qualifiers-ui: Configure link qualifiers
---

# Map a single source object to multiple target objects

In certain cases, you might have a single object in a resource that maps to more than one object in another resource. For example, assume that managed user, bjensen, has two distinct accounts in an LDAP directory: an `employee` account (under `uid=bjensen,ou=employees,dc=example,dc=com`) and a `customer` account (under `uid=bjensen,ou=customers,dc=example,dc=com`). You want to map both of these LDAP accounts to the same managed user account.

Advanced Identity Cloud uses *link qualifiers* to manage this one-to-many scenario. A link qualifier is essentially a label that identifies the *type* of link (or relationship) between objects.

The following diagram shows two link qualifiers that let you link both of bjensen's LDAP accounts to her managed user object:

![link-qualifier](_images/link-qualifier.png)

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The previous diagram displays that the link qualifier is a property of the *link* between the source and target object, and not a property of the source or target object itself. |

Link qualifiers are defined as part of the mapping. Each link qualifier must be unique within the mapping. If no link qualifier is specified (when only one possible matching target object exists), Advanced Identity Cloud uses a default link qualifier with the value `default`.

Link qualifiers can be defined as a static list, or dynamically, using a script. The following excerpt of a sample mapping shows the two static link qualifiers, `employee` and `customer`, described at the top of this topic:

```json
{
    "mappings": [
        {
            "name": "managedUser_systemLdapAccounts",
            "source": "managed/realm-name_user",
            "target": "system/MyLDAP/account",
            "linkQualifiers" : [ "employee", "customer" ],
...
```

Advanced Identity Cloud evaluates the list of static link qualifiers for *every* source record. That is, every reconciliation processes all synchronization operations, for each link qualifier, in turn.

A dynamic link qualifier script returns a list of link qualifiers that can be applied to each source record. For example, suppose you have two *types* of managed users—employees and contractors. For employees, a single managed user (source) account can correlate with three different LDAP (target) accounts—employee, customer, and manager. For contractors, a single managed user account can correlate with only two separate LDAP accounts—contractor, and customer. The following diagram displays the possible linking situations for this scenario:

![link-qualifier-script](_images/link-qualifier-script.png)

In this scenario, you could write a script to generate a dynamic list of link qualifiers, based on the managed user type. For employees, the script would return `[employee, customer, manager]` in its list of possible link qualifiers. For contractors, the script would return `[contractor, customer]` in its list of possible link qualifiers. A reconciliation operation would then process only the list of link qualifiers applicable to each source object.

If your source resource includes many records, you should use a dynamic link qualifier script instead of a static list of link qualifiers. Generating the list of applicable link qualifiers dynamically avoids unnecessary additional processing for those qualifiers that will never apply to specific source records. Therefore, synchronization performance is improved for large source data sets.

You can include a dynamic link qualifier script inline (using the `source` property). The following link qualifier script sets up the dynamic link qualifier lists described in the previous example.

|   |                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In this example, the `source` property value has been formatted across multiple lines for clarity. In general, the script source must be formatted on a single line. |

```json
{
  "mappings": [
    {
      "name": "managedUser_systemLdapAccounts",
      "source": "managed/realm-name_user",
      "target": "system/MyLDAP/account",
      "linkQualifiers" : {
        "type" : "text/javascript",
        "globals" : { },
        "source" : "if (returnAll) {
                      ['contractor', 'employee', 'customer', 'manager']
                    } else {
                      if(object.type === 'employee') {
                        ['employee', 'customer', 'manager']
                      } else {
                        ['contractor', 'customer']
                      }
                    }"
      }
...
```

Dynamic link qualifier scripts must return all valid link qualifiers when the `returnAll` global variable is true. The `returnAll` variable is used during the target reconciliation phase to check whether there are any target records that are unassigned, for each known link qualifier.

If you configure dynamic link qualifiers through the UI, the complete list of dynamic link qualifiers displays in the Generated Link Qualifiers item below the script. This list represents the values returned by the script when the `returnAll` variable is passed as `true`. For a list of the variables available to a dynamic link qualifier script, see [Script Triggers Defined in Mappings](../idm-scripting/script-triggers-mappings.html).

Link qualifiers have no functionality on their own, but they can be referenced in reconciliation operations to manage situations where a single source object maps to multiple target objects. The following examples show how link qualifiers can be used in reconciliation operations:

* Use link qualifiers during object creation, to create multiple target objects per source object.

  The following mapping excerpt defines a transformation script that generates the value of the `dn` attribute on an LDAP system. If the link qualifier is `employee`, the value of the target `dn` is set to `"uid=userName,ou=employees,dc=example,dc=com"`. If the link qualifier is `customer`, the value of the target `dn` is set to `"uid=userName,ou=customers,dc=example,dc=com"`. The reconciliation operation iterates through the link qualifiers for each source record. In this case, two LDAP objects, where separate `dn`s are created for each managed user object:

  ```json
  {
      "target" : "dn",
      "transform" : {
          "type" : "text/javascript",
          "globals" : { },
          "source" : "if (linkQualifier === 'employee')
                { 'uid=' + source.userName + ',ou=employees,dc=example,dc=com'; }
              else
              if (linkQualifier === 'customer')
                { 'uid=' + source.userName + ',ou=customers,dc=example,dc=com'; }"
      },
      "source" : ""
  }
  ```

* Use link qualifiers with *correlation queries*. The correlation query assigns a link qualifier based on the values of an existing target object.

  During source synchronization, Advanced Identity Cloud queries the target system for every source record *and* link qualifier, to check if there are any matching target records. If a match is found, the sourceId, targetId, and linkQualifier are all saved as the *link*.

  The following excerpt of a sample mapping shows the two link qualifiers described previously (`employee` and `customer`). The correlation query first searches the target system for the `employee` link qualifier. If a target object matches the query, based on the value of its `dn` attribute, Advanced Identity Cloud creates a link between the source object and that target object, and assigns the `employee` link qualifier to that link. This process is repeated for all source records. Then, the correlation query searches the target system for the `customer` link qualifier. If a target object matches that query, Advanced Identity Cloud creates a link between the source object and that target object and assigns the `customer` link qualifier to that link:

  ```json
  "linkQualifiers" : ["employee", "customer"],
    "correlationQuery" : [
      {
        "linkQualifier" : "employee",
        "type" : "text/javascript",
        "source" : "var query = {'_queryFilter': 'dn co \"' + uid=source.userName + 'ou=employees\"'}; query;"
      },
      {
        "linkQualifier" : "customer",
        "type" : "text/javascript",
        "source" : "var query = {'_queryFilter': 'dn co \"' + uid=source.userName + 'ou=customers\"'}; query;"
      }
    ]
  ...
  ```

  For more information about correlation queries, see [Writing Correlation Queries](chap-correlation.html#correlation-queries-configuring).

* Use link qualifiers during policy validation to apply different policies based on the link type.

  The following excerpt of a sample mapping shows two link qualifiers, `user` and `test`. Depending on the link qualifier, different actions are taken when the target record is ABSENT:

  ```json
  {
      "mappings" : [
          {
              "name" : "systemLdapAccounts_managedUser",
              "source" : "system/ldap/account",
              "target" : "managed/realm-name_user",
              "linkQualifiers" : [
                  "user",
                  "test"
          ],
      "properties" : [
      ...
      "policies" : [
          {
              "situation" : "CONFIRMED",
              "action" : "IGNORE"
          },
          {
              "situation" : "FOUND",
              "action" : "UPDATE
          }
          {
              "condition" : "/linkQualifier eq \"user\"",
              "situation" : "ABSENT",
              "action" : "CREATE",
              "postAction" : {
                  "type" : "text/javascript",
                  "source" : "java.lang.System.out.println('Created user: \');"
              }
          },
          {
              "condition" : "/linkQualifier eq \"test\"",
              "situation" : "ABSENT",
              "action" : "IGNORE",
              "postAction" : {
                  "type" : "text/javascript",
                  "source" : "java.lang.System.out.println('Ignored user: ');"
              }
          },
          ...
  ```

  With this sample mapping, the synchronization operation creates an object in the target system only if the potential match is assigned a `user` link qualifier. If the match is assigned a `test` qualifier, no target object is created. In this way, the process avoids creating duplicate *test-related* accounts in the target system.

## Configure link qualifiers

Use the [Advanced Sync](../identities/advanced-sync.html) editor to configure [correlation](../identities/advanced-sync-correlation.html) queries and scripts.

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Link qualifier configuration is currently available only in the IDM native admin console, which is [deprecated](../product-information/migration-dependent-features/deprecated-identity-management-native-console-faq.html). |

---

---
title: Prevent the accidental deletion of a target system
description: Prevent accidental target deletion by requiring empty source set confirmation
component: pingoneaic
page_id: pingoneaic:idm-synchronization:prevent-accidental-deletion
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/prevent-accidental-deletion.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Mappings"]
section_ids:
  preventing-accidental-deletion-ui: Prevent accidental target deletion using the admin console
---

# Prevent the accidental deletion of a target system

If a source resource is empty, the default behavior is to exit without failure and to log a warning similar to the following:

```
[318] Feb 19, 2020 1:51:56.455 PM org.forgerock.openidm.sync.NonClusteredRecon dispatchRecon
WARNING: Cannot reconcile from an empty data source, unless allowEmptySourceSet is true.
```

The reconciliation summary is also logged in the reconciliation audit log.

This behavior prevents reconciliation operations from accidentally deleting everything in a target resource. In the event that a source system is unavailable but erroneously reports its status as up, the absence of source objects should not result in objects being removed on the target resource.

If you *do* want reconciliations of an empty source resource to proceed, override the default behavior by setting the `allowEmptySourceSet` property to `true` in the mapping. For example:

```json
{
    "mappings" : [
        {
        "name" : "systemCsvfileAccounts_managedUser",
        "source" : "system/csvfile/account",
        "allowEmptySourceSet" : true,
        ...
```

When an empty source is reconciled, the data in the target is wiped out.

## Prevent accidental target deletion using the admin console

To allow reconciliations from an empty source to delete all data in a target resource, select the Allow reconciliations from an Empty Source checkbox in the [Advanced Sync](../identities/advanced-sync.html) editor's advanced reconciliation settings.

Learn more in [Advanced reconciliation settings](../identities/advanced-sync-advanced-reconciliation.html).

---

---
title: Remove a mapping
description: Remove synchronization mappings and associated links from repository
component: pingoneaic
page_id: pingoneaic:idm-synchronization:remove-sync-mapping
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/remove-sync-mapping.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Resource", "Mappings"]
---

# Remove a mapping

* To remove a mapping, delete the corresponding section from your mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint.)*.

* To remove a mapping in the Advanced Identity Cloud admin console, use the [Advanced Sync](../identities/advanced-sync.html) editor. Learn more in [Edit or delete an advanced sync mapping](../identities/advanced-sync-mappings.html#edit-delete-advanced-sync-mapping).

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you delete the mapping in the admin console, the `delete-mapping-links` script removes all links related to that mapping from the repository. |

---

---
title: Resource mapping
description: Map attributes between source and target resources with pagination support
component: pingoneaic
page_id: pingoneaic:idm-synchronization:mappings
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/mappings.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Resource", "Mappings"]
section_ids:
  sync-mapping-paging: Paging synchronization mapping results
---

# Resource mapping

A synchronization mapping specifies a relationship between objects and their attributes in two data stores. The following example shows a typical attribute mapping, between objects in an external LDAP directory and an Advanced Identity Cloud managed user data store:

```
"source": "lastName",
"target": "sn"
```

In this case, the `lastName` source attribute is mapped to the `sn` (surname) attribute in the target LDAP directory.

The core synchronization configuration is defined in the mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint.)*.

For a list of *all* mappings, use the following request:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/sync/mappings?_queryFilter=true"
```

This call returns the mappings in the order in which they will be processed.

Mappings are always defined from a *source* resource to a *target* resource. To configure bidirectional synchronization, you must define two mappings. For example, to configure bidirectional synchronization between an LDAP server and an Advanced Identity Cloud repository, you would define the following two mappings:

* LDAP Server > Advanced Identity Cloud Repository

* Advanced Identity Cloud Repository > LDAP Server

Bidirectional mappings can include a `links` property that lets you reuse the links established between objects, for both mappings. For more information, see [Reuse Links Between Mappings](reusing-links.html).

You can update a mapping while the server is running. To avoid inconsistencies between data stores, do not update a mapping while a reconciliation is in progress *for that mapping*.

## Paging synchronization mapping results

With many synchronization mappings, use paging to retrieve the results in manageable chunks to avoid overwhelming the client. The `openidm/sync/mappings` endpoint supports paging with the `_pageSize` parameter and either cookies (`_pagedResultsCookie`) or offsets (`_pagedResultsOffset`).

Example: Cookie-based paging

In the following example, the source `source1` returns 3 results without a query filter (`mapping1`, `mapping4`, and `mapping7`).

1. To get the first page of results, with a page size of 2, send a request like this:

   ```
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://<tenant-env-fqdn>/openidm/sync/mappings?_queryFilter=/source+eq+'source1'&_pageSize=2"
   ```

   The response includes a `pagedResultsCookie` containing the ID of the next available result (`mapping7`) that you can use to retrieve the next page:

   ```json
   {
     "result": [
       {
         "_id": "mapping1",
         "source": "source1",
         "target": "target1",
         "name": "mapping1",
         "sourceRouteReady": false,
         "targetRouteReady": false
       },
       {
         "_id": "mapping4",
         "source": "source1",
         "target": "target0",
         "name": "mapping4",
         "sourceRouteReady": false,
         "targetRouteReady": false
       }
     ],
     "resultCount": 2,
     "pagedResultsCookie": "mapping7",
     "totalPagedResultsPolicy": "EXACT",
     "totalPagedResults": 2,
     "remainingPagedResults": -1
   }
   ```

2. To get the next page of results, use the `_pagedResultsCookie` query parameter with the ID (`mapping7`) from the previous response:

   ```
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://<tenant-env-fqdn>/openidm/sync/mappings?_queryFilter=/source+eq+'source1'&_pageSize=2&_pagedResultsCookie=mapping7"
   {
     "result": [
       {
         "_id": "mapping7",
         "source": "source1",
         "target": "target3",
         "name": "mapping7",
         "sourceRouteReady": false,
         "targetRouteReady": false
       }
     ],
     "resultCount": 1,
     "pagedResultsCookie": null,         (1)
     "totalPagedResultsPolicy": "EXACT",
     "totalPagedResults": 1,
     "remainingPagedResults": -1
   }
   ```

   |       |                                                                                           |
   | ----- | ----------------------------------------------------------------------------------------- |
   | **1** | The `pagedResultsCookie` has a `null` value, indicating no further results are available. |

Example: Offset-based paging

1. To get the first page of results, with a page size of 2 and an offset of 0:

   ```
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://<tenant-env-fqdn>/openidm/sync/mappings?_queryFilter=/source+eq+'source1'&_pageSize=2&_pagedResultsOffset=0"
   {
     "result": [
       {
         "_id": "mapping1",
         "source": "source1",
         "target": "target1",
         "name": "mapping1",
         "sourceRouteReady": false,
         "targetRouteReady": false
       },
       {
         "_id": "mapping4",
         "source": "source1",
         "target": "target0",
         "name": "mapping4",
         "sourceRouteReady": false,
         "targetRouteReady": false
       }
     ],
     "resultCount": 2,
     "pagedResultsCookie": "mapping7",
     "totalPagedResultsPolicy": "EXACT",
     "totalPagedResults": 2,
     "remainingPagedResults": -1
   }
   ```

2. To get the second page of results, set the `_pagedResultsOffset` to the number of results already retrieved (in this case, 2):

   ```
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://<tenant-env-fqdn>/openidm/sync/mappings?_queryFilter=/source+eq+'source1'&_pageSize=2&_pagedResultsOffset=2"
   {
     "result": [
       {
         "_id": "mapping7",
         "source": "source1",
         "target": "target3",
         "name": "mapping7",
         "sourceRouteReady": false,
         "targetRouteReady": false
       }
     ],
     "resultCount": 1,
     "pagedResultsCookie": null,
     "totalPagedResultsPolicy": "EXACT",
     "totalPagedResults": 1,
     "remainingPagedResults": -1
   }
   ```

---

---
title: Reuse links between mappings
description: Reuse links between bidirectional mappings to maintain single link per object pair
component: pingoneaic
page_id: pingoneaic:idm-synchronization:reusing-links
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/reusing-links.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Mappings"]
section_ids:
  reusing-mapping-links-ui: Reuse links between mappings using the admin console
---

# Reuse links between mappings

When two mappings synchronize the same objects bidirectionally, use the `links` property in one mapping to have Advanced Identity Cloud use the same link for both mappings. If you do not specify a `links` property, Advanced Identity Cloud maintains a separate link for each mapping.

The following excerpt shows two mappings, one from MyLDAP accounts to managed users, and another from managed users to MyLDAP accounts. In the second mapping, the `link` property indicates that Advanced Identity Cloud should reuse the links created in the first mapping, rather than create new links:

```json
{
    "mappings": [
        {
            "name": "systemMyLDAPAccounts_managedUser",
            "source": "system/MyLDAP/account",
            "target": "managed/realm-name_user"
        },
        {
            "name": "managedUser_systemMyLDAPAccounts",
            "source": "managed/realm-name_user",
            "target": "system/MyLDAP/account",
            "links": "systemMyLDAPAccounts_managedUser"
        }
    ]
}
```

## Reuse links between mappings using the admin console

To reuse the links from an existing mapping, select Link Mapping when you create the mapping in the [Advanced Sync](../identities/advanced-sync.html) editor.

Learn more in [Create an advanced sync mapping](../identities/advanced-sync-mappings.html#create-advanced-sync-mapping).

---

---
title: Schedule synchronization
description: Schedule synchronization operations like reconciliation and liveSync with Quartz triggers
component: pingoneaic
page_id: pingoneaic:idm-synchronization:chap-schedules
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/chap-schedules.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization"]
section_ids:
  configuring-sync-schedule: Configure scheduled synchronization
  livesync-ui: Schedule liveSync using the admin console
---

# Schedule synchronization

You can schedule synchronization operations, such as liveSync and reconciliation, using Quartz triggers. Advanced Identity Cloud supports [SimpleTriggers](https://www.quartz-scheduler.org/documentation/quartz-2.5.x/tutorials/tutorial-lesson-05.html) and [CronTriggers](https://www.quartz-scheduler.org/documentation/quartz-2.5.x/tutorials/crontrigger.html).

Use the trigger type that suits your scheduling requirements. Because simple triggers aren't bound to the local timezone, they're better suited to scenarios such as liveSync, where the requirement is to trigger the schedule at regular intervals, regardless of the local time.

This section describes scheduling specifically for reconciliation and liveSync, and shows simple triggers in all the examples. You can use the scheduler service to schedule any other event by supplying a script in which that event is defined. For information about scheduling other events, refer to [Schedule tasks and events](../idm-schedules/schedules.html).

## Configure scheduled synchronization

Each scheduled reconciliation and liveSync task requires a schedule configuration *(tooltip: You can create and change schedule configurations over REST at the openidm/scheduler/job endpoint.)*, with the following format:

```json
{
 "enabled"        : boolean, true/false
 "type"           : "string",
 "repeatInterval" : long integer,
 "repeatCount"    : integer,
 "persisted"      : boolean, true/false
 "startTime"      : "(optional) time",
 "endTime"        : "(optional) time",
 "schedule"       : "cron expression",
 "misfirePolicy"  : "optional, string",
 "invokeService"  : "service identifier",
 "invokeContext"  : "service specific context info"
}
```

These properties are specific to the scheduler service, and are explained in [Schedule tasks and events](../idm-schedules/schedules.html).

To schedule a reconciliation or liveSync task, set the `invokeService` property to either `sync` (for reconciliation) or `provisioner` for liveSync.

The value of the `invokeContext` property depends on the type of scheduled event. For reconciliation, the properties are set as follows:

```json
{
    "invokeService": "sync",
    "invokeContext": {
        "action": "reconcile",
        "mapping": "systemLdapAccount_managedUser"
    }
}
```

The `mapping` is referenced by its `name` in the mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint.)*.

For liveSync, the properties are set as follows:

```json
{
    "invokeService": "provisioner",
    "invokeContext": {
        "action": "liveSync",
        "source": "system/ldap/account"
    }
}
```

The `source` property follows the convention for a pointer to an external resource object, and takes the form `system/resource-name/object-type`.

|   |                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you schedule a reconciliation operation to run at regular intervals, do not set `"concurrentExecution" : true`. This parameter enables multiple scheduled operations to run concurrently. You cannot launch multiple reconciliation operations for a single mapping concurrently. |

## Schedule liveSync using the admin console

You can create a liveSync schedule for an external object type in the admin console.

Learn more in [Manage provisioner schedules](../app-management/standalone-provisioner-schedules.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The scheduler configuration assumes a `simple` trigger type by default, so the `Cron-like Trigger` field is disabled. You should use simple triggers for liveSync schedules to avoid problems related to daylight savings time. For more information, refer to [Schedules and daylight savings time](../idm-schedules/schedules-dst.html).For more information on the distinction between the scheduler service and the configuration service, refer to [Configure the scheduler service](../idm-schedules/scheduler-configuration-file.html). |

---

---
title: Scriptable conditions in a mapping
description: Create scriptable conditions and filters for conditional attribute mapping
component: pingoneaic
page_id: pingoneaic:idm-synchronization:mapping-conditions
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/mapping-conditions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Mappings", "Scripts"]
section_ids:
  mapping-conditions-ui: Configure mapping conditions using the admin console
---

# Scriptable conditions in a mapping

By default, Advanced Identity Cloud synchronizes all attributes in a mapping. For more complex relationships between source and target objects, you can define conditions under which Advanced Identity Cloud maps certain attributes. You can define two types of mapping conditions:

* *Scriptable conditions*, in which an attribute is mapped only if the defined script evaluates to `true`.

* *Condition filters*, a declarative filter that sets the conditions under which the attribute is mapped. Condition filters can include a *link qualifier* , that identifies the *type* of relationship between the source object and multiple target objects. For more information, reference [Map a Single Source Object to Multiple Target Objects](linking-multiple-targets.html).

  The following list shows examples of condition filters:

  * `"condition": "/object/country eq 'France'"`—Only map the attribute if the object's `country` attribute equals `France`.

  * `"condition": "/object/password pr"`—Only map the attribute if the object's `password` attribute is present.

  * `"condition": "/linkQualifier eq 'admin'"`—Only map the attribute if the link between this source and target object is of type `admin`.

## Configure mapping conditions using the admin console

To apply a conditional update to a mapping property, use the [Advanced Sync](../identities/advanced-sync.html) editor's conditional update editor.

Learn more in [Define and preview mapping rules](../identities/advanced-sync-mappings.html#define-preview-mapping-rules).

Scriptable conditions create mapping logic, based on the result of the condition script. If the script does not return `true`, Advanced Identity Cloud doesn't manipulate the target attribute during a synchronization operation.

In the following excerpt, the value of the target `mail` attribute is set to the value of the source `email` attribute *only if* the source attribute is not empty:

```json
{
    "target": "mail",
        "comment": "Set mail if non-empty.",
        "source": "email",
        "condition": {
            "type": "text/javascript",
            "source": "(object.email != null)"
        }
...
```

|   |                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can add comments to JSON files. This example includes a property named `comment`; however, you can use any unique property name, as long as it is not used elsewhere in the server. Advanced Identity Cloud ignores unknown property names in JSON configuration files. |

---

---
title: Scripts in mappings
description: Use script hooks to manipulate objects and attributes during synchronization operations
component: pingoneaic
page_id: pingoneaic:idm-synchronization:scripts-in-mappings
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/scripts-in-mappings.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Mappings", "Scripts"]
section_ids:
  construct-attributes: Construct and manipulate attributes
  actions-with-scripts: Perform other actions
  using-scripts-logs: Generate Log Messages
---

# Scripts in mappings

You can use a number of *script hooks* to manipulate objects and attributes during synchronization. Scripts can be triggered during various stages of the synchronization process, and are defined as part of the mapping.

You can trigger a script when a managed or system object is created (`onCreate`), updated (`onUpdate`), or deleted (`onDelete`). You can also trigger a script when a link is created (`onLink`) or removed (`onUnlink`).

In the default synchronization mapping, changes are always written to *target* objects, not to *source* objects. However, you can explicitly include a call to an action that should be taken on the source object within the script.

## Construct and manipulate attributes

The most common use of synchronization scripts is when a target object is created or updated.

The `onUpdate` script is *always* called for an UPDATE situation, even if the synchronization process determines that there is no difference between the source and target objects, and that the target object will not be updated.

If the `onUpdate` script has run and the synchronization process determines that the target value to set is the same as its existing value, the change is prevented from synchronizing to the target.

The following excerpt of a sample mapping derives a DN for an LDAP entry when the corresponding managed entry is created:

```json
{
    "onCreate": {
        "type": "text/javascript",
        "source":
            "target.dn = 'uid=' + source.uid + ',ou=people,dc=example,dc=com'"
    }
}
```

## Perform other actions

[Construct and manipulate attributes with scripts](#construct-attributes) shows how to manipulate attributes with scripts when objects are created and updated. You can also trigger scripts in response to other synchronization actions. For example, you might not want to delete a managed user directly when an external account is deleted, but instead unlink the objects and deactivate the user in another resource. Alternatively, you might delete the object in Advanced Identity Cloud and run a script to perform some subsequent action.

The following example shows a more advanced mapping configuration that exposes the script hooks available during synchronization:

```json
{
    "mappings": [
        {
            "name": "systemLdapAccount_managedUser",
            "source": "system/ldap/account",
            "target": "managed/realm-name_user",
            "validSource": {
                "type": "text/javascript",
                "file": "script/isValid.js"
            },
            "correlationQuery" : {
                "type" : "text/javascript",
                "source" : "var map = {'_queryFilter': 'uid eq \"'

                     source.userName + '\"'}; map;"
            },
            "properties": [
                {
                    "source": "uid",
                    "transform": {
                        "type": "text/javascript",
                        "source": "source.toLowerCase()"
                    },
                    "target": "userName"
                },
                {
                    "source": "",
                    "transform": {
                        "type": "text/javascript",
                        "source": "if (source.myGivenName)
                            {source.myGivenName;} else {source.givenName;}"
                    },
                    "target": "givenName"
                },
                {
                    "source": "",
                    "transform": {
                        "type": "text/javascript",
                        "source": "if (source.mySn)
                            {source.mySn;} else {source.sn;}"
                    },
                    "target": "familyName"
                },
                {
                    "source": "cn",
                    "target": "fullname"
                },
                {
                    "condition": {
                        "type": "text/javascript",
                        "source": "var clearObj = openidm.decrypt(object);
                            clearObj.password != null) &&                             (clearObj.ldapPassword != clearObj.password"
                    },
                    "transform": {
                        "type": "text/javascript",
                        "source": "source.password"
                    },
                    "target": "PASSWORD"
                }
            ],
            "onCreate": {
                "type": "text/javascript",
                "source": "target.ldapPassword = null;
                    target.adPassword = null;
                    target.password = null;
                    target.ldapStatus = 'New Account'"
            },
            "onUpdate": {
                "type": "text/javascript",
                "source": "target.ldapStatus = 'OLD'"
            },
            "onUnlink": {
                "type": "text/javascript",
                "file": "script/triggerAdDisable.js"
            },
            "policies": [
                {
                    "situation": "CONFIRMED",
                    "action": "UPDATE"
                },
                {
                    "situation": "FOUND",
                    "action": "UPDATE"
                },
                {
                    "situation": "ABSENT",
                    "action": "CREATE"
                },
                {
                    "situation": "AMBIGUOUS",
                    "action": "EXCEPTION"
                },
                {
                    "situation": "MISSING",
                    "action": "EXCEPTION"
                },
                {
                    "situation": "UNQUALIFIED",
                    "action": "UNLINK"
                },
                {
                    "situation": "UNASSIGNED",
                    "action": "EXCEPTION"
                }
            ]
        }
    ]
}
```

The following list shows the properties that you can use as hooks in mapping configurations to call scripts:

* Triggered by Situation

  onCreate, onUpdate, onDelete, onLink, onUnlink

* Object Filter

  validSource, validTarget

* Correlating Objects

  correlationQuery

* Triggered on Reconciliation

  result

* Scripts Inside Properties

  condition, transform

Scripts can obtain data from any connected system by using the `openidm.read(id)` function, where `id` is the identifier of the object to read.

The following example reads a managed user object from the repository:

```javascript
repoUser = openidm.read("managed/realm-name_user/9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb");
```

The following example reads an account from an external LDAP resource:

```javascript
externalAccount = openidm.read("system/ldap/account/uid=bjensen,ou=People,dc=example,dc=com");
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For illustration purposes, this query targets a DN rather than a UID as it did in the previous example. The attribute that is used for the `_id` is defined in the connector configuration and, in this example, is set to `"uidAttribute" : "dn"`. Although you *can* use a DN (or any unique attribute) for the `_id`, it is a best practice to use an attribute that is both unique and immutable, such as the `entryUUID`. |

## Generate Log Messages

Advanced Identity Cloud provides a `logger` object that you can use from scripts defined in your mapping. These scripts can log messages to the OSGi console and to log files, which are then ingested by the `monitoring/logs` endpoint. The `logger` object includes the following functions:

* `debug()`

* `error()`

* `info()`

* `trace()`

* `warn()`

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information on logs within identity-related scripts, refer to [log functions](../idm-scripting/scripting-func-logs.html#logger-functions). |

Consider the following mapping excerpt:

```json
{
    "mappings" : [
        {
            "name" : "systemCsvfileAccounts_managedUser",
            "source" : "system/csvfile/account",
            "target" : "managed/realm-name_user",
            "correlationQuery" : {
                "type" : "text/javascript",
                "source" : "var query = {'_queryId' : 'for-userName', 'uid' :  source.name};query;"
            },
            "onCreate" : {
                "type" : "text/javascript",
                "source" : "logger.warn('Case onCreate: the source object contains: = {} ', source); source;"
            },
            "onUpdate" : {
                "type" : "text/javascript",
                "source" : "logger.warn('Case onUpdate: the source object contains: = {} ', source); source;"
            },
            "result" : {
                "type" : "text/javascript",
                "source" : "logger.warn('Case result: the source object contains: = {} ', source); source;"
            },
            "properties" : [
                {
                    "transform" : {
                        "type" : "text/javascript",
                        "source" : "logger.warn('Case no Source: the source object contains: = {} ', source); source;"
                    },
                    "target" : "sourceTest1Nosource"
                },
                {
                    "source" : "",
                    "transform" : {
                        "type" : "text/javascript",
                        "source" : "logger.warn('Case emptySource: the source object contains: = {} ', source); source;"
                    },
                    "target" : "sourceTestEmptySource"
                },
                {
                    "source" : "description",
                    "transform" : {
                        "type" : "text/javascript",
                        "source" : "logger.warn('Case sourceDescription: the source object contains: = {} ', source); source"
                    },
                    "target" : "sourceTestDescription"
                },
                ...
            ]
        }
    ]
}
```

The scripts that are defined for `onCreate`, `onUpdate`, and `result` log a warning message to the console whenever an object is created or updated, or when a result is returned. The script result includes the full source object.

The scripts that are defined in the `properties` section of the mapping log a warning message if the property in the source object is missing or empty. The last script logs a warning message that includes the description of the source object.

During a reconciliation operation, these scripts would generate output in the OSGi console, similar to the following:

```none
2017-02... WARN Case no Source: the source object contains: = null  [9A00348661C6790E7881A7170F747F...]
2017-02... WARN Case emptySource: the source object contains: = {roles=openidm-..., lastname=Jensen...]
2017-02... WARN Case no Source: the source object contains: = null  [9A00348661C6790E7881A7170F747F...]
2017-02... WARN Case emptySource: the source object contains: = {roles=openidm..., lastname=Carter,...]
2017-02... WARN Case sourceDescription: the source object contains: = null  [EEE2FF4BCE9748927A1832...]
2017-02... WARN Case sourceDescription: the source object contains: = null  [EEE2FF4BCE9748927A1832...]
2017-02... WARN Case onCreate: the source object contains: = {roles=openidm-..., lastname=Carter,  ...]
2017-02... WARN Case onCreate: the source object contains: = {roles=openidm-..., lastname=Jensen,  ...]
2017-02... WARN Case result: the source object contains: = {SOURCE_IGNORED={count=0, ids=[]}, FOUND_ALL...]
```

---

---
title: Situations specific to implicit synchronization and liveSync
description: Synchronization situations specific to implicit sync and liveSync deletion events
component: pingoneaic
page_id: pingoneaic:idm-synchronization:autosync-and-livesync
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/autosync-and-livesync.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization"]
---

# Situations specific to implicit synchronization and liveSync

Certain situations occur only during implicit synchronization (when changes made in the repository are pushed out to external systems) and liveSync (when Advanced Identity Cloud polls external system change logs for changes and updates the repository).

The following table shows the situations that pertain only to implicit sync and liveSync, when records are *deleted* from the source or target resource.

**Situations detected during implicit sync or liveSync deletion events**

| Source Qualifies | Link Exists | Targets Found \[[1](#_footnotedef_1 "View footnote.")] | Targets Qualify | Situation      | Default Action        | Possible Actions                                   |
| ---------------- | ----------- | ------------------------------------------------------ | --------------- | -------------- | --------------------- | -------------------------------------------------- |
| n/a              | **YES**     | 0                                                      | n/a             | LINK_ONLY      | EXCEPTION             | IGNORE, REPORT, NOREPORT, ASYNC                    |
| n/a              | **YES**     | 1                                                      | 1               | SOURCE_MISSING | EXCEPTION             | DELETE, IGNORE, REPORT, NOREPORT, ASYNC            |
| n/a              | **YES**     | 1                                                      | 0               | TARGET_IGNORED | IGNORE                | DELETE, UNLINK, EXCEPTION, REPORT, NOREPORT, ASYNC |
| n/a              | **NO**      | 0                                                      | n/a             | ALL_GONE       | IGNORE                | EXCEPTION, REPORT, NOREPORT, ASYNC                 |
| **YES**          | **NO**      | 0                                                      | n/a             | ALL_GONE       | IGNORE                | EXCEPTION, REPORT, NOREPORT, ASYNC                 |
| **YES**          | **NO**      | 1                                                      | 1               | UNASSIGNED     | EXCEPTION             | REPORT, NOREPORT                                   |
| **YES**          | **NO**      | > 1                                                    | > 1             | AMBIGUOUS      | EXCEPTION             | IGNORE, REPORT, NOREPORT, ASYNC                    |
| **NO**           | **NO**      | 0                                                      | n/a             | ALL_GONE       | IGNORE                | EXCEPTION, REPORT, NOREPORT, ASYNC                 |
| **NO**           | **NO**      | 1                                                      | 1               | TARGET_IGNORED | IGNORE target object  | DELETE, UNLINK, EXCEPTION, REPORT, NOREPORT, ASYNC |
| **NO**           | **NO**      | > 1                                                    | > 1             | UNQUALIFIED    | DELETE target objects | EXCEPTION, IGNORE, REPORT, NOREPORT, ASYNC         |

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about how to configure situations and actions using [Advanced sync situation rules](../identities/advanced-sync-situation-rules.html). |

***

[1](#_footnoteref_1). If no link exists for the source object, Advanced Identity Cloud executes any included correlation logic. If a link exists, correlation does not apply.

---

---
title: Source reconciliation
description: Understand synchronization situations detected during source reconciliation phase
component: pingoneaic
page_id: pingoneaic:idm-synchronization:source-reconciliation
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/source-reconciliation.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Reconciliation"]
section_ids:
  sync-situations-source-target-conflict: The SOURCE_TARGET_CONFLICT situation
---

# Source reconciliation

During source reconciliation and liveSync, Advanced Identity Cloud iterates through the objects in the source resource. For reconciliation, the list of objects includes all objects that are available through the connector. For liveSync, the list contains only changed objects. Advanced Identity Cloud can filter objects from the list by using the following:

* Scripts specified in the `validSource` property

* A query specified in the `sourceCondition` property

* A query specified in the `sourceQuery` property

For each object in the list, Advanced Identity Cloud assesses the following conditions:

1. Is the source object valid?

   Valid source objects are categorized `qualifies=1`. Invalid source objects are categorized `qualifies=0`. Invalid objects include objects that were filtered out by a `validSource` script or `sourceCondition`. For more information, refer to [Filter source and target objects with scripts](chap-restricting-sync.html#filtering-source-and-target).

2. Does the source object have a record in the links table?

   Source objects that have a corresponding link in the repository's `links` table are categorized `link=1`. Source objects that do not have a corresponding link are categorized `link=0`.

3. Does the source object have a corresponding valid target object?

   Source objects that have a corresponding object in the target resource are categorized `target=1`. Source objects that do not have a corresponding object in the target resource are categorized `target=0`.

The following diagram illustrates the categorization of four sample objects during source reconciliation. In this example, the source is the managed user repository and the target is an LDAP directory:

![sync-situations](_images/sync-situations.png)Figure 1. Object Categorization During the Source Synchronization Phase

Based on the categorizations of source objects during the source reconciliation phase, the synchronization process assesses a *situation* for each source object, and executes the *action* that is configured for each situation.

Not all situations are detected during all synchronization types (reconciliation, implicit synchronization, and liveSync). The following table describes the set of synchronization situations detected during source reconciliation, the default action taken for each situation, and valid alternative actions that can be configured for each situation:

**Situations Detected During Reconciliation and Source Change Events**

| Source Qualifies | Link Exists | Target Objects Found | Situation                                                     | Default Action                                                       | Possible Actions                                        |
| ---------------- | ----------- | -------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------- |
| **NO**           | **NO**      | 0                    | SOURCE_IGNORED                                                | IGNORE source object                                                 | EXCEPTION, REPORT, NOREPORT, ASYNC                      |
| **NO**           | **NO**      | 1                    | UNQUALIFIED                                                   | DELETE target object                                                 | EXCEPTION, IGNORE, REPORT, NOREPORT, ASYNC              |
| **NO**           | **NO**      | > 1                  | UNQUALIFIED                                                   | DELETE target objects                                                | EXCEPTION, IGNORE, REPORT, NOREPORT, ASYNC              |
| **NO**           | **YES**     | 0                    | UNQUALIFIED                                                   | DELETE linked target object \[[1](#_footnotedef_1 "View footnote.")] | EXCEPTION, REPORT, NOREPORT, ASYNC                      |
| **NO**           | **YES**     | 1                    | UNQUALIFIED                                                   | DELETE linked target object                                          | EXCEPTION, REPORT, NOREPORT, ASYNC                      |
| **NO**           | **YES**     | > 1                  | UNQUALIFIED                                                   | DELETE linked target object                                          | EXCEPTION, REPORT, NOREPORT, ASYNC                      |
| **YES**          | **NO**      | 0                    | ABSENT                                                        | CREATE target object                                                 | EXCEPTION, IGNORE, REPORT, NOREPORT, ASYNC              |
| **YES**          | **NO**      | 1                    | FOUND                                                         | UPDATE target object                                                 | EXCEPTION, IGNORE, REPORT, NOREPORT, ASYNC              |
| **YES**          | **NO**      | 1                    | FOUND_ALREADY_LINKED \[[2](#_footnotedef_2 "View footnote.")] | EXCEPTION                                                            | IGNORE, REPORT, NOREPORT, ASYNC                         |
| **YES**          | **NO**      | > 1                  | AMBIGUOUS \[[3](#_footnotedef_3 "View footnote.")]            | EXCEPTION                                                            | REPORT, NOREPORT, ASYNC                                 |
| **YES**          | **YES**     | 0                    | MISSING \[[4](#_footnotedef_4 "View footnote.")]              | EXCEPTION                                                            | CREATE, UNLINK, DELETE, IGNORE, REPORT, NOREPORT, ASYNC |
| **YES**          | **YES**     | 1                    | CONFIRMED \[[5](#_footnotedef_5 "View footnote.")]            | UPDATE target object                                                 | IGNORE, REPORT, NOREPORT, ASYNC                         |

Based on this table, the following situations would be assigned to the previous diagram:

![sync-situations2](_images/sync-situations2.png)Figure 2. Situation Assignment During the Source Synchronization Phase

## The `SOURCE_TARGET_CONFLICT` situation

For mappings between applications and workforce identities, `CONFIRMED` has a conflict variant. Advanced Identity Cloud reports `SOURCE_TARGET_CONFLICT` when a source object qualifies for the mapping and is linked to a target object, and changes made directly to the linked objects can't be reconciled. This happens when both objects have changed since the last successful synchronization, or when the next outbound synchronization would overwrite changes made directly to the application account.

Application templates preconfigure the action to `ASYNC`. The `EXCEPTION`, `IGNORE`, `REPORT`, and `NOREPORT` actions are also valid alternatives. Learn more in [Synchronization actions](sync-actions.html).

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about how to configure situations and actions using [Advanced sync situation rules](../identities/advanced-sync-situation-rules.html). |

***

[1](#_footnoteref_1). In this case (and the two following cases), the DELETE action is applied to the linked target object and not necessarily to the target object(s) found by the correlation query. If the source is no longer valid and a link existed, the correlation logic is skipped.[2](#_footnoteref_2). The source object qualifies for a target object and is not linked to an existing target object. There is a single target object that correlates with this source object, according to the logic in the correlation, but that target object is already linked to a different source object.[3](#_footnoteref_3). The source object qualifies for a target object, is not linked to an existing target object, but there is more than one correlated target object (that is, more than one possible match on the target system).[4](#_footnoteref_4). If the action is CREATE for the situation MISSING, the orphaned link associated with the source object is updated to point to the new target object. When a target object is deleted, the link from the target to the corresponding source object is not deleted automatically. This lets Advanced Identity Cloud detect and report items that might have been removed without permission or might need review. If you need to remove the corresponding link when a target object is deleted, change the action to UNLINK to remove the link, or to DELETE to remove the target object and the link.[5](#_footnoteref_5). For application-to-workforce identity mappings, when conflicting changes are made directly to the linked objects, Advanced Identity Cloud reports `SOURCE_TARGET_CONFLICT` instead of `CONFIRMED`. Refer to [The `SOURCE_TARGET_CONFLICT` situation](#sync-situations-source-target-conflict).

---

---
title: Synchronization
description: Configure synchronization between Advanced Identity Cloud and other resources.
component: pingoneaic
page_id: pingoneaic:idm-synchronization:preface
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization"]
page_aliases: ["index.adoc"]
---

# Synchronization

> Configure synchronization between Advanced Identity Cloud and other resources.

Synchronizing identity data between resources is one of the core services of Advanced Identity Cloud. The following topics discuss the different types of synchronization and how to configure the flexible synchronization mechanism.

[icon: book, set=fas, size=3x]

#### [Synchronization overview](sync-overview.html)

Understand synchronization types and configuration.

[icon: map-signs, set=fas, size=3x]

#### [Mappings](mappings.html)

Map data between resources.

[icon: cubes, set=fas, size=3x]

#### [Situations and actions](chap-situations-actions.html)

Learn about synchronization situations and how to configure actions for each.

[icon: sort-amount-down, set=fas, size=3x]

#### [Filter synchronization data](chap-restricting-sync.html)

Use filtering mechanisms to limit the synchronized data.

[icon: sync-alt, set=fas, size=3x]

#### [Implicit sync and liveSync](chap-implicit-live-sync.html)

Configure automatic synchronization between resources.

[icon: cogs, set=fas, size=3x]

#### [Reconciliation performance](chap-performance.html)

Learn about ways to improve reconciliation performance.

---

---
title: Synchronization actions
description: Perform actions based on synchronization situations including create, update, delete
component: pingoneaic
page_id: pingoneaic:idm-synchronization:sync-actions
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/sync-actions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Scripts"]
section_ids:
  script-actions: Launch a script as an action
---

# Synchronization actions

When an object has been assigned a situation, the synchronization process takes the configured *action* on that object. If no action is configured, the default action for that situation applies.

The following actions can be taken:

* `CREATE`

  Create and link a target object.

* `UPDATE`

  Link and update a target object.

* `DELETE`

  Delete and unlink the target object.

* `LINK`

  Link the correlated target object.

* `UNLINK`

  Unlink the linked target object.

* `EXCEPTION`

  Flag the link situation as an exception.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Do *not* use this action for liveSync mappings.In the context of liveSync, the EXCEPTION action triggers the liveSync failure handler, and the operation is retried in accordance with the configured retry policy. This is not useful because the operation will never succeed. If the configured number of retries is high, these pointless retries can continue for a long period of time.If the maximum number of retries is exceeded, the liveSync operation terminates and does not continue processing the entry that follows the failed (EXCEPTION) entry. LiveSync is only resumed at the next liveSync polling interval.This behavior differs from reconciliation, where a failure to synchronize a single source-target association does not fail the entire reconciliation. |

* `IGNORE`

  Do not change the link or target object state.

* `REPORT`

  Do not perform any action but report what would happen if the default action were performed.

* `NOREPORT`

  Do not perform any action or generate any report.

* `ASYNC`

  An asynchronous process has been started, so do not perform any action or generate any report.

|   |                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information on how to configure the situations and actions in the Advanced Identity Cloud admin console, refer to [Configure situations and actions using the Advanced Identity Cloud admin console](chap-situations-actions.html#situations-and-actions-ui). |

## Launch a script as an action

In addition to the static synchronization actions described previously, you can provide a script to run in specific synchronization situations. You can specify the script inline (with the `"source"` property).

The following excerpt of a sample mapping specifies that an inline script should be invoked when a synchronization operation assesses an entry as `ABSENT` in the target system. The script checks whether the `employeeType` property of the corresponding source entry is `contractor`. If so, the source entry is ignored. Otherwise, the entry is created on the target system:

```json
{
    "situation" : "ABSENT",
    "action" : {
        "type" : "text/javascript",
        "globals" : { },
        "source" : "if (source.employeeType === 'contractor') {action='IGNORE'}
                   else {action='CREATE'};action;"
    },
}
```

The following variables are available to a script that is called as an action:

* `source`

* `target`

* `linkQualifier`

* `recon` (where `recon.actionParam` contains information about the current reconciliation operation)

For more information about the variables available to scripts, refer to [Script variables](../idm-scripting/script-vars.html).

The result obtained from evaluating this script must be a string whose value is one of the synchronization actions listed in [Synchronization actions](sync-actions.html). This resulting action is shown in the reconciliation log.

To launch a script as a synchronization action in the admin console, use the [Advanced Sync](../identities/advanced-sync.html) editor to [define situation rules](../identities/advanced-sync-situation-rules.html).

---

---
title: Synchronization configuration overview
description: High-level configuration overview for synchronization between resources
component: pingoneaic
page_id: pingoneaic:idm-synchronization:sync-config
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/sync-config.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Configuration"]
---

# Synchronization configuration overview

This section describes the high-level steps required to set up synchronization between two resources. A basic synchronization configuration involves the following steps:

1. Set up a connection between the source and target resource.

   A connector configuration *(tooltip: You can create and change connector configurations over REST at the /openidm/config/provisioner.openicf/\<connector-name> endpoint.)* references a specific connector type and indicates the connection details of the external resource. You must define a connector configuration for each external resource to which you are connecting.

   For more information, refer to [Connections between resources](sync-connections.html).

2. Map source objects to target objects.

   The mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint.)* of your project. Mappings are synchronized in the order in which they are created. Mappings can be created either over REST or using the [Advanced Sync](../identities/advanced-sync.html) editor.

   Learn more in [Configure advanced sync mappings](../identities/advanced-sync-mappings.html).

3. Configure any scripts that are required to check source and target objects, and to manipulate attributes.

4. In addition to these configuration elements, Advanced Identity Cloud stores a `links` table in its repository. The links table maintains a record of relationships established between source and target objects.

The following diagram illustrates the high-level synchronization configuration:

![sync-config](_images/sync-config.png)

---

---
title: Synchronization operations
description: Manage reconciliation and liveSync operations ensuring data consistency across stores
component: pingoneaic
page_id: pingoneaic:idm-synchronization:chap-sync-operations
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/chap-sync-operations.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Synchronization operations

There are various *synchronization* operations within Advanced Identity Cloud that ensure data consistency:

* *Reconciliation* is the process of ensuring that the objects in two different data stores are consistent. Reconciliation is very thorough and a heavy process.

* *LiveSync* captures the changes that occur on an external system, and pushes those changes to Advanced Identity Cloud.

The following subsections describe the various ways you can manage reconciliation and liveSync via REST and the Advanced Identity Cloud admin console.

---

---
title: Synchronization overview
description: Understand synchronization types and mechanisms for keeping data consistent
component: pingoneaic
page_id: pingoneaic:idm-synchronization:sync-overview
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/sync-overview.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Types"]
---

# Synchronization overview

*Synchronization* keeps data consistent across disparate resources. Within Advanced Identity Cloud, we refer to two resource types— *managed resources* (stored in the Advanced Identity Cloud repository) and *external resources*.

An external resource can be any system that holds identity data, such as DS, Active Directory, a CSV file, a JDBC database, and so on.

Advanced Identity Cloud connects to external resources through [*connectors*](https://docs.pingidentity.com/openicf/index.html). Synchronization across resources happens when managed resources change, or when Advanced Identity Cloud discovers a change on a system resource. There are various [synchronization mechanisms](sync-types.html) that ensure data consistency.
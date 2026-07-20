---
title: Audit logs
description: (Deprecated; use JSON audit event handler) REST endpoints for querying and writing PingIDM audit logs, covering reconciliation, sync, activity, access, and authentication topics
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-audit-logs
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-audit-logs.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "logs"]
---

# Audit logs

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Query and read operations on the `/audit` API endpoint are [deprecated](../../release-notes/deprecated-functionality.html#deprecation-read-query-audit-endpoint) and will be removed in a future release of IDM. Use the [JSON audit event handler](../../audit-guide/configuring-topic-handlers.html#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack). |

You can interact with the audit logs over REST, as shown in the following table. Queries on the audit endpoint must use `queryFilter` syntax.

| URI                                                                                   | HTTP Operation | Description                                                                       |
| ------------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------- |
| /openidm/audit/recon?\_queryFilter=true                                               | GET            | Displays the reconciliation audit log.                                            |
| /openidm/audit/recon/id                                                               | GET            | Reads a specific reconciliation audit log entry.                                  |
| /openidm/audit/recon/id                                                               | PUT            | Creates a reconciliation audit log entry.                                         |
| /openidm/audit/recon?\_queryFilter=/reconId+eq+"reconId"                              | GET            | Queries the audit log for a particular reconciliation operation.                  |
| /openidm/audit/recon?\_queryFilter=/reconId+eq+"reconId"+and+situation+eq+"situation" | GET            | Queries the reconciliation audit log for a specific reconciliation situation.     |
| /openidm/audit/sync?\_queryFilter=true                                                | GET            | Displays the synchronization audit log.                                           |
| /openidm/audit/sync/id                                                                | GET            | Reads a specific synchronization audit log entry.                                 |
| /openidm/audit/sync/id                                                                | PUT            | Creates a synchronization audit log entry.                                        |
| /openidm/audit/activity?\_queryFilter=true                                            | GET            | Displays the activity log.                                                        |
| /openidm/audit/activity/id                                                            | GET            | Returns activity information for a specific action.                               |
| /openidm/audit/activity/id                                                            | PUT            | Creates an activity audit log entry.                                              |
| /openidm/audit/activity?\_queryFilter=transactionId=id                                | GET            | Queries the activity log for all actions resulting from a specific transaction.   |
| /openidm/audit/access?\_queryFilter=true                                              | GET            | Displays the full list of auditable actions.                                      |
| /openidm/audit/access/id                                                              | GET            | Displays information on the specific audit item.                                  |
| /openidm/audit/access/id                                                              | PUT            | Creates an access audit log entry.                                                |
| /openidm/audit/authentication?\_queryFilter=true                                      | GET            | Displays a complete list of authentication attempts, successful and unsuccessful. |
| /openidm/audit/authentication?\_queryFilter=/principal+eq+"principal"                 | GET            | Displays the authentication attempts by a specified user.                         |
| /openidm/audit?\_action=availableHandlers                                             | POST           | Returns a list of audit event handlers.                                           |
| openidm/audit/config?\_queryFilter=true                                               | GET            | Lists changes made to the configuration.                                          |

---

---
title: Bulk import
description: REST endpoints for the PingIDM bulk import service to upload CSV files, track imports, and clean up records
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-bulk-import
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-bulk-import.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "upload files"]
---

# Bulk import

The bulk import service lets you import large numbers of entries from a CSV file into the IDM repository. You can import any managed object type, but you will generally use this service to import user entries. The following table shows the endpoints used by the bulk import service:

| URI                                                   | HTTP Operation | Description                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /openidm/csv/template?resourceCollection=managed/user | GET            | Generates a CSV header row that you can use as a template for the import. You can safely remove generated columns for properties that are not required. Set the query parameters `_fields=header` and `_mimeType=text/csv` to download the header file.                                                                                                                                                                                 |
| /upload/csv/resourceCollection                        | POST           | Uploads the file specified by the `--form` (`-F`) parameter to the specified resource collection. `?uniqueProperty=propertyName` is required. Generally, for `managed/user` objects, the `uniqueProperty` is `userName`. You can specify multiple comma-delimited values here to identify unique records; for example, `?uniqueProperty=firstName,lastName`. [Example](../../synchronization-guide/import-data.html#query-bulk-import). |
| /openidm/csv/metadata/?\_action=cleanupList           | POST           | Lists the import UUIDs that have error records or temporary records. These can be cleaned up to free up database space. If you clean up error records, you will no longer be able to download a CSV of failed import records.                                                                                                                                                                                                           |
| /openidm/csv/metadata/importUUID?\_action=cleanup     | POST           | Cleans up temporary import records for the specified import UUID. To also clean up error records, set the query parameter `?deleteErrorRecords=true`.                                                                                                                                                                                                                                                                                   |
| /openidm/csv/metadata/importUUID?\_action=cancel      | POST           | Cancels the specified in-progress import.                                                                                                                                                                                                                                                                                                                                                                                               |
| /openidm/csv/metadata/importUUID                      | DELETE         | Deletes the specified import record. This does not affect the data that was imported.                                                                                                                                                                                                                                                                                                                                                   |
| /openidm/csv/metadata?\_queryFilter                   | GET            | Queries bulk imports.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| /openidm/csv/metadata/importUUID                      | GET            | Reads the specified import record.                                                                                                                                                                                                                                                                                                                                                                                                      |
| /export/csvImportFailures/importUUID                  | GET            | Downloads a CSV file of failed import records. Returns 404 if there were no failures for the specified import UUID.                                                                                                                                                                                                                                                                                                                     |

---

---
title: Cluster activation
description: REST endpoint to read and set the cluster readiness state of a PingIDM node, enabling on-demand active and standby transitions
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-cluster-active
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-cluster-active.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API"]
section_ids:
  endpoint_summary: Endpoint summary
  read_the_cluster_readiness_state: Read the cluster readiness state
  set_the_cluster_readiness_state: Set the cluster readiness state
  request_body: Request body
  authentication: Authentication
---

# Cluster activation

The `openidm/cluster/active` endpoint lets you read and set the cluster readiness state of an IDM instance.

This endpoint is available only when both `org.forgerock.feature.cluster.active.passive` and `org.forgerock.feature.cluster.improved` are set to `true` in `resolver/boot.properties`.

Learn more in [Cluster standby mode](../../install-guide/cluster-standby.html).

## Endpoint summary

| HTTP Operation | Endpoint                  | Description                                    |
| -------------- | ------------------------- | ---------------------------------------------- |
| GET            | `/openidm/cluster/active` | Read the current readiness state of this node. |
| PUT            | `/openidm/cluster/active` | Set the readiness state of this node.          |

## Read the cluster readiness state

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/cluster/active'
```

Example response

```json
{
  "state": "STANDBY"
}
```

## Set the cluster readiness state

To activate a node:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request PUT \
--header "Accept-API-Version: resource=1.0" \
--header 'Content-Type: application/json' \
--header 'If-Match: *' \
--data '{"state":"ACTIVE"}' \
'http://localhost:8080/openidm/cluster/active'
```

Example response

```json
{
  "state": "ACTIVE"
}
```

To set a node to standby:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request PUT \
--header "Accept-API-Version: resource=1.0" \
--header 'Content-Type: application/json' \
--header 'If-Match: *' \
--data '{"state":"STANDBY"}' \
'http://localhost:8080/openidm/cluster/active'
```

Example response

```json
{
  "state": "STANDBY"
}
```

## Request body

| Property | Type   | Description                                             |
| -------- | ------ | ------------------------------------------------------- |
| `state`  | String | The readiness state. Valid values: `ACTIVE`, `STANDBY`. |

## Authentication

Access to this endpoint is authenticated using credentials configured through the purpose `idm.cluster.activation.credentials`.

Learn more in [Store username and password as a secret](../../security-guide/secret-stores.html#store-user-pass-as-secret).

---

---
title: Email
description: REST endpoints for sending email messages and managing email templates using the PingIDM outbound email service
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-email
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-email.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Email"]
---

# Email

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | To configure the email service, refer to [Outbound email service](../../external-services-guide/email.html). |

You can use the IDM outbound email service over REST at the `external/email` endpoint:

| URI                                           | HTTP Operation | Description              |
| --------------------------------------------- | -------------- | ------------------------ |
| /openidm/external/email?\_action=send         | POST           | Sends an email.          |
| /openidm/external/email?\_action=sendTemplate | POST           | Sends an email template. |

For complete examples, refer to [Send email using REST](../../external-services-guide/email-send.html).

---

---
title: File upload
description: REST endpoints for the PingIDM file upload service to upload, retrieve, and delete files in the repository or filesystem
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-file-upload
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-file-upload.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "upload files"]
---

# File upload

IDM supports a generic file upload service at the `file` endpoint. Files are uploaded either to the filesystem or to the repository. For information about configuring this service, and for command-line examples, refer to [Upload files to the server](../../objects-guide/file-upload-service.html).

IDM provides REST access to the file upload service, as listed in the following table:

| URI                                                                 | HTTP Operation | Description                                                                                                                                                                        |
| ------------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /openidm/file/handler/                                              | PUT            | Uploads a file to the specified file handler. The file handler is either the repository or the filesystem and the context path is configured in the `conf/file-handler.json` file. |
| /openidm/file/handler/filename                                      | GET            | Returns the file content in a base 64-encoded string within the returned JSON object.                                                                                              |
| /openidm/file/handler/filename?\_fields=content&\_mimeType=mimeType | GET            | Returns the file content with the specified MIME type.                                                                                                                             |
| /openidm/file/handler/filenamemimeType                              | DELETE         | Deletes an uploaded file.                                                                                                                                                          |

---

---
title: Internal objects
description: REST endpoints for listing, creating, and managing PingIDM internal users and their roles
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-internal
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-internal.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "internal users"]
---

# Internal objects

You can manage the following internal objects over REST:

| URI                                                     | HTTP Operation | Description                                                                     |
| ------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------- |
| /openidm/internal/role?\_queryFilter=true               | GET            | Lists all internal roles.                                                       |
| /openidm/internal/user?\_queryFilter=true               | GET            | Lists internal users.                                                           |
| /openidm/internal/user/username                         | PUT            | Adds a new internal user, or changes the password of an existing internal user. |
| /openidm/internal/user/username                         | PATCH          | Adds or removes roles of an internal user.                                      |
| /openidm/internal/role?\_queryFilter=true&\_fields=\_id | GET            | Lists internal roles.                                                           |
| /openidm/internal/role/role-id?\_fields=\*,authzMembers | GET            | Lists internal and managed users with the specified internal role.              |

---

---
title: Managed organizations
description: REST endpoints for creating, reading, updating, deleting, and querying PingIDM managed organizations
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-managed-organizations
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-managed-organizations.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Organizations"]
---

# Managed organizations

Organizations are exposed under the context path `/managed/organization`. The following table lists the REST commands associated with managed organizations.

| URI                                                            | HTTP Operation | Description                                                 |
| -------------------------------------------------------------- | -------------- | ----------------------------------------------------------- |
| /openidm/managed/organization?\_queryFilter=true&\_fields=\_id | GET            | Lists the IDs of all managed organizations.                 |
| /openidm/managed/organization?\_queryFilter=filter             | GET            | Queries managed organizations with the defined filter.      |
| /openidm/managed/organization/\_id                             | GET            | Returns the JSON representation of a specific organization. |
| /openidm/managed/organization/\_id                             | PUT            | Creates an organization with a user-defined ID.             |
| /openidm/managed/organization/\_id                             | PUT            | Updates an organization (replaces the entire object).       |
| /openidm/managed/organization?\_action=create                  | POST           | Creates a new organization with a system-generated ID.      |
| /openidm/managed/organization/\_id                             | DELETE         | Deletes an organization.                                    |

For a number of sample commands that show how to manage organizations over REST, refer to [Managed Organizations](../../objects-guide/managed-objects.html#managed-orgs).

---

---
title: Managed users
description: REST endpoints for creating, reading, updating, patching, deleting, and querying PingIDM managed users
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-managed-users
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-managed-users.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Users", "Identities"]
---

# Managed users

User objects are stored in the repository and are exposed under the context path `/managed/user`. Many examples of REST calls related to this context path exist throughout this document. The following table lists available functionality associated with the `/managed/user` context path.

| URI                                                                       | HTTP Operation | Description                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /openidm/managed/user?\_queryFilter=true&\_fields=\_id                    | GET            | Lists the IDs of all the managed users in the repository.                                                                                                                                                                                                                                      |
| /openidm/managed/user?\_queryFilter=true                                  | GET            | Lists all info for the managed users in the repository.                                                                                                                                                                                                                                        |
| /openidm/managed/user?\_queryFilter=filter                                | GET            | Queries the managed user object with the defined filter.                                                                                                                                                                                                                                       |
| /openidm/managed/user/\_id                                                | GET            | Returns the JSON representation of a specific user.                                                                                                                                                                                                                                            |
| /openidm/managed/user/\_id                                                | PUT            | Creates a new user.                                                                                                                                                                                                                                                                            |
| /openidm/managed/user/\_id                                                | PUT            | Updates a user entry (replaces the entire entry).                                                                                                                                                                                                                                              |
| /openidm/managed/user?\_action=create                                     | POST           | Creates a new user.                                                                                                                                                                                                                                                                            |
| /openidm/managed/user?\_action=patch&\_queryId=for-userName\&uid=userName | POST           | Updates a user (can be used to replace the value of one or more existing attributes).&#xA;&#xA;The access rule for this endpoint is:&#xA;&#xA;{&#xA;  "pattern" : "managed/user/\*",&#xA;  "roles" : "internal/role/openidm-authorized",&#xA;  "methods" : "patch",&#xA;  "actions" : ""&#xA;} |
| /openidm/managed/user/\_id                                                | PATCH          | Updates specified fields of a user entry.                                                                                                                                                                                                                                                      |
| /openidm/managed/user/\_id                                                | DELETE         | Deletes a user entry.                                                                                                                                                                                                                                                                          |

For a number of sample commands that show how to manage users over REST, refer to [Users](../../objects-guide/users.html).

---

---
title: Privileges
description: REST endpoints to list PingIDM privilege paths and resource-level privileges for the authenticated user
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-privileges
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-privileges.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Delegated Administration"]
---

# Privileges

Privileges are a part of internal roles, and can be created or modified using the REST calls specified in [Internal objects](rest-internal.html). Additionally, `openidm/privilege` can be used for getting information about privileges on a resource as they apply to the authenticated user.

| URI                                        | HTTP Operation | Description                                                                                                    |
| ------------------------------------------ | -------------- | -------------------------------------------------------------------------------------------------------------- |
| /openidm/privilege?\_action=listPrivileges | POST           | Lists an array of privilege paths for the authenticated user, with additional detail required by the admin UI. |
| /openidm/privilege/resource                | GET            | Lists the privileges for the logged in user associated with the given resource path.                           |
| /openidm/privilege/resource/guid           | GET            | Lists the privileges for the logged in user associated with the specified object.                              |

---

---
title: Reconciliation operations
description: REST endpoints for running, querying, canceling, and managing PingIDM reconciliation operations and association data
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-recon
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-recon.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Reconciliation"]
---

# Reconciliation operations

You can interact with the reconciliation engine over REST, as shown in the following table:

| URI                                | HTTP Method | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/openidm/recon`                   | GET         | Lists all reconciliation runs, including those in progress. Inspect the `state` property to see the reconciliation status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `/openidm/recon/id`                | GET         | Returns the JSON representation of a specific reconciliation run.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `/openidm/recon?_action=recon`     | POST        | Launches a reconciliation run with the specified mapping.A JSON body can be included in the POST request to override specific mapping configuration parameters for this run only. For example, `sourceQuery`, `targetQuery`, or `runTargetPhase` can be adjusted dynamically.**Parameters**- `&mapping=mapping-name` (Required)

  Specifies the mapping to use.

- `&waitForCompletion=true`

  If set, the REST call blocks until the reconciliation completes.

  This parameter isn't supported for clustered reconciliation environments and will result in an error if used.

- `&persistAssociations=true`

  Stores detailed association results for this run, queryable with `recon/assoc` endpoints. Learn more in [Reconciliation association details](../../synchronization-guide/manage-recon.html#recon-assoc). Performance impact should be considered for large reconciliations.

- `&analyze=true`

  Performs an analysis run, determining actions without executing them. Requires `persistAssociations=true` to store and query the analysis results effectively. Learn more in [Reconciliation association details](../../synchronization-guide/manage-recon.html#recon-assoc).                               |
| `/openidm/recon?_action=reconById` | POST        | Restricts the reconciliation run to the specified source object ID (`id`).**Parameters**- `&mapping=mapping-name` (Required)

  Specifies the mapping to use.

- `&id=source-id` (Required)

  The `_id` of the source object to reconcile.You can include a JSON body in the POST request to override specific mapping configuration properties for this run only.**Optional request body properties**- `sourceQuery`

  Overrides the source query.

- `targetQuery`

  Overrides the target query.

- `allowEmptySourceSet`

  Overrides whether reconciliation proceeds when the source object set is empty. Learn more in [Prevent the accidental deletion of a target system](../../synchronization-guide/prevent-accidental-deletion.html).

- `runTargetPhase`

  Set to `false` to skip the target phase for this run.

- `sourceQueryFullEntry`

  Overrides whether the source query returns full object data (`true`) or IDs only (`false`).

- `targetQueryFullEntry`

  Overrides whether the target query returns full object data (`true`) or IDs only (`false`).Learn more in [Override mapping configuration for reconById](../../synchronization-guide/chap-restricting-sync.html#recon-by-id-override-params). |
| `/openidm/recon/id?_action=cancel` | POST        | Cancels the specified reconciliation run.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `/openidm/recon/assoc`             | GET         | Lists stored reconciliation association summaries. Requires runs performed with `persistAssociations=true`. Supports standard query parameters like `_queryFilter`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `/openidm/recon/assoc/id`          | GET         | Returns the association summary for a specific reconciliation run.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `/openidm/recon/assoc/id/entry`    | GET         | Returns detailed entry-level association information for a specific reconciliation run. Results can be large. Supports standard query parameters like `_queryFilter`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `/openidm/recon/id`                | DELETE      | Purges the statistics and stored association data for a specific reconciliation run. Learn about configuring this to run automatically in [Purge reconciliation statistics](../../synchronization-guide/manage-recon.html#recon-delete).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

The following example runs a reconciliation for the [mapping](../../synchronization-guide/mappings.html) `systemHrdb_managedUser`:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/recon?_action=recon&mapping=systemHrdb_managedUser"
```

---

---
title: REST and IDM
description: Explains how PingIDM implements the Common REST API, including PATCH limitations, query filters, and _fields parameter behavior
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:rest-and-idm
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/rest-and-idm.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API"]
section_ids:
  crest-idm-specifics: Common REST and IDM
---

# REST and IDM

Representational State Transfer (REST) is a software architecture style for exposing resources, using the technologies and protocols of the World Wide Web. REST describes how distributed data objects, or resources, can be defined and addressed.

IDM provides a RESTful API for accessing managed objects, system objects, workflows, and the system configuration.

## Common REST and IDM

IDM implements the Common REST API as described in the previous section, with the exception of the following elements:

* IDM provides limited support for the [in expression clause](../objects-guide/queries.html#query-in). You can use this clause for queries on singleton string properties, not arrays. `in` query expressions are not supported through the admin UI.

* The PATCH `transform` action is supported only on the `config` endpoint. Note that this is an optional action and not implemented everywhere across the Ping Identity Platform.

* Common REST supports PATCH operations by list element index, as shown in the example in [Patch Operation: Remove](../crest/crest-patch.html#crest-patch-remove). IDM *does not support* PATCH by list element index. So, for PATCH operations, you cannot use an ordinal when adding or removing list items.

  You can add an item using the special hyphen index, which designates that the element should be added to the end of the list. To remove specific items from a list, you must specify the *value* to be removed, for example:

  ```json
  [
      {
          "operation" : "remove",
          "field" : "/phoneNumber/",
          "value" : "202-555-0185"
      }
  ]
  ```

  |   |                                                                                                                      |
  | - | -------------------------------------------------------------------------------------------------------------------- |
  |   | When you remove items in this way, if the list contains two or more items with the same value, they are all removed. |

* If `_fields` is left blank (null), the server returns all default values. In IDM, this excludes relationships and virtual fields. To include these fields in the output, add `"returnByDefault" : true` in the applicable schema.

  IDM also implements wild-card (`*`) handling with the `_fields` parameter. So, a value of `_fields=*_ref` will return all relationship fields associated with an object. A value of `_fields=*_ref/*` will return all the fields within each relationship.

* IDM does not implement the `ESTIMATE` total paged results policy. The `totalPagedResults` is either the exact total result count (`_totalPagedResultsPolicy=EXACT`) or result counting is disabled (`_totalPagedResultsPolicy=NONE`). For more information, refer to [Page Query Results](../objects-guide/queries.html#paging-query-results).

---

---
title: REST API Explorer
description: (Deprecated; download separately) Use the PingIDM API Explorer, an OpenAPI/Swagger implementation, to browse/test REST endpoints from the legacy admin UI
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:api-explorer
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/api-explorer.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Tools"]
section_ids:
  example: Example
  disable_the_api_explorer: Disable the API Explorer
---

# REST API Explorer

|   |                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Starting with IDM 8.1, the API Explorer is deprecated and is no longer bundled with IDM. It's available as a separate download from the [Backstage download site](https://backstage.forgerock.com/downloads).To continue using the API Explorer, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

The IDM API Explorer, an implementation of the [OpenAPI Initiative Specification](https://swagger.io/solutions/getting-started-with-oas/), also known as Swagger, covers many of the endpoints provided with a default IDM installation.

Each endpoint lists supported HTTP methods, such as POST and GET. When custom actions are available, the API Explorer lists them as:

```none
HTTP Method /path/to/endpoint?_action=something
```

## Example

To see the API Explorer in action, follow along with this procedure:

1. To access the API Explorer, log in to the admin UI, click the question mark button [icon: question-circle, set=fas]in the upper right corner, and select [icon: code, set=fas]API Explorer.

   |   |                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the API Explorer does not display, you might need to enable it in your `resolver/boot.properties` file by setting the `openidm.apidescriptor.enabled` property to `true`. |

2. Expand the User v1.0 endpoint node, and click GET /openidm/managed/user1.0\_query\_id\_query-all.

   ![API Explorer - User Node](_images/apiExpUserNode.png)

3. Click Try it out!, and then click Execute.

   The output includes:

   * The REST call, in the form of the `curl` command.

   * The request URL, which specifies the endpoint and associated parameters.

   * The response body, which contains the data that you requested.

   * The HTTP response code; if everything works, this should be `200`.

     |   |                                                                                                                                                    |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you refer to a `401 Access Denied` code in the response body, your session may have timed out, and you'll have to log in to the admin UI again. |

   * Response headers.

   > **Collapse: Example Output**
   >
   > ![apiExpOutput](_images/apiExpOutput.png)

For details on common REST parameters, refer to [Common REST](../crest/about-crest.html).

You'll refer to examples of REST calls throughout this documentation set. You can try these calls with the API Explorer.

You can also generate an OpenAPI-compliant descriptor of the REST API to provide API reference documentation specific to your deployment. The following command saves the API descriptor of the managed/user endpoint to a file named `my-openidm-api.json`:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
--output "my-openidm-api.json" \
"http://localhost:8080/openidm/managed/user?_api"
```

For information about publishing reference documentation using the API descriptor, refer to [Publish OpenAPI Documentation](../crest/about-crest.html#use-openapi-descriptors).

## Disable the API Explorer

If you've already installed and configured the legacy admin UI, but want to disable the API Explorer, delete the `api/` directory from your Nginx `html` webroot.

|   |                                                                                   |
| - | --------------------------------------------------------------------------------- |
|   | Learn more in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

---

---
title: REST API reference
description: PingIDM REST API reference covering request and response structure, API versioning, and available endpoints
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API"]
page_aliases: ["index.adoc"]
---

# REST API reference

> Guide to creating and managing objects in PingIDM.

This reference describes the Common REST API. Refer to [Common REST and IDM](rest-and-idm.html#crest-idm-specifics) for information specific to the IDM implementation of Common REST.

Quick Start

[icon: play-circle, set=fad, size=3x]

#### [Start Here](rest-and-idm.html)

Learn about the Common REST interface in the Ping Identity Platform and the specifics of REST in IDM.

[icon: cogs, set=fad, size=3x]

#### [REST API Structure](rest-structure.html)

Understand RESTful syntax with respect to the IDM REST API.

[icon: list, set=fad, size=3x]

#### [REST Endpoints](endpoints/rest-server-config.html)

Discover the REST endpoints IDM exposes.

---

---
title: REST API structure
description: "Reference for PingIDM REST API structure: URI schemes, object identifiers, content negotiation, and conditional operations"
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:rest-structure
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/rest-structure.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API"]
section_ids:
  rest-uri-scheme: URI scheme
  rest-object-identifier: Object identifiers
  rest-content-negotiation: Content negotiation
  rest-conditional-operations: Conditional operations
---

# REST API structure

## URI scheme

The URI scheme for accessing a managed object follows this convention, assuming the IDM web application was deployed at `/openidm`.

```
/openidm/managed/type/id
```

Similar schemes exist for URIs associated with all but system objects. For more information, refer to [Configure Access Control in access.json](../auth-guide/authorization-and-roles.html#access-json).

The URI scheme for accessing a system object follows this convention:

```
/openidm/system/resource-name/type/id
```

An example of a system object in an LDAP directory might be:

```
/openidm/system/ldap/account/07b46858-56eb-457c-b935-cfe6ddf769c7
```

|   |                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For LDAP resources, you should *not* map the LDAP `dn` to the IDM `uidAttribute` (`_id`). The attribute that is used for the `_id` should be immutable. You should therefore map the LDAP `entryUUID` operational attribute to the IDM `_id`, as shown in the following excerpt of the provisioner configuration file:```none
...
"uidAttribute" : "entryUUID",
...
``` |

## Object identifiers

Every managed and system object has an identifier (expressed as id in the URI scheme) that is used to address the object through the REST API. The REST API allows for client-generated and server-generated identifiers, through PUT and POST methods. The default server-generated identifier type is a UUID. If you create an object by using `POST`, a server-assigned ID is generated in the form of a UUID. If you create an object by using PUT, the client assigns the ID in whatever format you specify.

Most of the examples in this guide use client-assigned IDs, as it makes the examples easier to read.

## Content negotiation

The REST API fully supports negotiation of content representation through the `Accept` HTTP header. Currently, the supported content type is JSON. When you send a JSON payload, you must include the following header:

```
Accept: application/json
```

In a REST call (using the `curl` command, for example), you would include the following option to specify the noted header:

```
--header "Content-Type: application/json"
```

You can also specify the default UTF-8 character set as follows:

```
--header "Content-Type: application/json;charset=utf-8"
```

The `application/json` content type is not needed when the REST call does not send a JSON payload.

## Conditional operations

The REST API supports conditional operations through the use of the `ETag`, `If-Match` and `If-None-Match` HTTP headers. The use of HTTP conditional operations is the basis of IDM's optimistic concurrency control system. Clients should make requests conditional in order to prevent inadvertent modification of the wrong version of an object.

**REST API Conditional Operations**

| HTTP Header                                                              | Operation | Description                                                                            |
| ------------------------------------------------------------------------ | --------- | -------------------------------------------------------------------------------------- |
| `If-Match: <rev>`                                                        | PUT       | Update the object if the \<rev> matches the revision level of the object.              |
| `If-Match: *`                                                            | PUT       | Update the object regardless of revision level.                                        |
| `If-None-Match: <rev>`                                                   |           | Bad request.                                                                           |
| `If-None-Match: *`                                                       | PUT       | Create; fails if the object already exists.                                            |
| When the conditional operations `If-Match`, `If-None-Match` are not used | PUT       | Upsert; attempts a create, and then an update; if both attempts fail, return an error. |

---

---
title: REST API versioning
description: How to specify REST API versions in PingIDM requests using the Accept-API-Version header or scripts, and configure version-warning logging
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:rest-api-versioning
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/rest-api-versioning.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API"]
section_ids:
  api-version-over-rest: Specify the API version in REST calls
  api-version-in-scripts: Specify the API Version in Scripts
  api_version_header_warnings: API Version Header Warnings
  filter_resource_path_warnings: Filter Resource Path Warnings
---

# REST API versioning

Ping REST API features are assigned version numbers. Providing version numbers in the REST API helps ensure compatibility between releases. The version number of a feature increases when Ping introduces a change that is not backwards-compatible and affects clients who use the feature.

If there is more than one version of the API, you must select the version by setting a version header that specifies which version of the *resource* is requested. To ensure that your clients are always compatible with a newer IDM version, you should always include resource versions in your REST calls.

For more information about the supported resource versions, refer to [REST API Explorer](api-explorer.html).

## Specify the API version in REST calls

HTTP requests can optionally include the `Accept-API-Version` header with the value of the resource version, such as `resource=2.0`. If no `Accept-API-Version` header is included, the request defaults to API version `1.0`. The `consent`, `scheduler/job`, `scheduler/trigger`, and `schema` endpoints default to API version `2.0`.

The following call requests version `2.0` of the specified resource:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
--data '{
  "url":"https://www.forgerock.com/favicon.ico",
  "method":"GET"
}' \
"http://localhost:8080/openidm/external/rest?_action=call"
```

If `Accept-API-Version` contains an invalid version, IDM returns the following error:

```json
{
  "code": 404,
  "reason": "Not Found",
  "message": "Resource&#39;&#39; not found"
}
```

## Specify the API Version in Scripts

You can specify a resource version in scripts using the fourth (*additional parameters*) argument. If present, the `Accept-API-Version` parameter is applied to the actual REST request. Any other parameters are set as Additional Parameters on the request.

The following examples request specific resource versions:

REST with Inline Javascript

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "type":"text/javascript",
  "source":"openidm.action(\"external/rest\", \"call\", {\"url\": \"https://www.forgerock.com/favicon.ico\", \"method\": \"GET\"}, {\"Accept-API-Version\": \"resource=1.0\"});"
}' \
"http://localhost:8080/openidm/script?_action=eval"
```

Standalone Javascript

```javascript
openidm.action("external/rest", "call",
 {"url": "https://www.forgerock.com/favicon.ico", "method": "GET"},
 {"Accept-API-Version": "resource=1.0"});
```

## API Version Header Warnings

IDM can log warnings when API version headers are not specified. Additionally, you can enable warnings when *scripts* don't specify API versions. Warnings are disabled by default. To enable this feature, add one or more of the following to your project's `resolver/boot.properties` file:

* `openidm.apiVersion.warning.enabled=true`

  * A message will be logged once per resource path, at the `info` level. For example:

    ```
    INFO: Accept-API-Version header missing from external request (authentication); transactionId=e017258a-8bac-4507-9575-78a41152e479-1929
    ```

  * The HTTP response will apply a warning header. For example:

    ```
    Warning: 100 CREST "Accept-API-Version should be included in the request."
    ```

* `openidm.apiVersion.warning.includeScripts=true`

  |   |                                                                  |
  | - | ---------------------------------------------------------------- |
  |   | This setting requires `openidm.apiVersion.warning.enabled=true`. |

  * A message will be logged once per resource path *and* script-name pair, at the `info` level.

    Example script file log entry:

    ```
    [127] Sep 22, 2021 4:08:15.162 AM org.forgerock.openidm.servlet.internal.ResourceApiVersionFilterRegistration logOnceForScriptRequest
    INFO: Accept-API-Version header missing from script (policyFilter.js) request: policy
    ```

    Example inline script log entry:

    ```
    INFO: Accept-API-Version header missing from script (d6fc81179beaca37094a23c2fcd00aaf54bb3ef9:router:onRequest) request (config)
    ...
    INFO: Accept-API-Version header missing from script (policy.js) request (managed/user)
    ```

### Filter Resource Path Warnings

To filter which resource paths are logged, edit the `logFilterResourcePaths` array located in the `conf/apiVersion.json` file. You can also modify the configuration over REST:

1. Get the current configuration:

   ```none
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/config/apiVersion"
   ```

   > **Collapse: Default  Configuration**
   >
   > ```json
   > {
   >   "_id": "apiVersion",
   >   "warning": {
   >     "enabled": {
   >       "$bool": "&{openidm.apiVersion.warning.enabled|false}"
   >     },
   >     "includeScripts": {
   >       "$bool": "&{openidm.apiVersion.warning.includeScripts|false}"
   >     },
   >     "logFilterResourcePaths": [
   >       "audit",
   >       "authentication",
   >       "cluster",
   >       "config",
   >       "consent",
   >       "csv",
   >       "external/rest",
   >       "identityProviders",
   >       "info",
   >       "internal",
   >       "internal/role",
   >       "internal/user",
   >       "internal/usermeta",
   >       "managed",
   >       "managed/assignment",
   >       "managed/organization",
   >       "managed/role",
   >       "managed/user",
   >       "notification",
   >       "policy",
   >       "privilege",
   >       "profile",
   >       "recon",
   >       "recon/assoc",
   >       "repo",
   >       "selfservice/kba",
   >       "selfservice/terms",
   >       "scheduler/job",
   >       "scheduler/trigger",
   >       "schema",
   >       "sync",
   >       "sync/mappings",
   >       "system",
   >       "taskscanner"
   >     ]
   >   }
   > }
   > ```

2. Make changes, and replace the configuration:

   ```none
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: resource=1.0" \
   --request PUT \
   --data '{
       "warning" : {
           "enabled" : {
               "$bool" : "&{openidm.apiVersion.warning.enabled|false}"
           },
           "includeScripts" : {
               "$bool" : "&{openidm.apiVersion.warning.includeScripts|false}"
           },
           "logFilterResourcePaths" : [ <Insert modified resourcePaths here>
           ]
       }
   }' \
   "http://localhost:8080/openidm/config/apiVersion"
   ```

---

---
title: Scanning tasks
description: REST endpoints for listing, triggering, and canceling PingIDM task scanner runs
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-task-scanner
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-task-scanner.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Task Scanner"]
---

# Scanning tasks

The [task scanning mechanism](../../schedules-guide/task-scanner.html) lets you perform a batch scan for a specified date, on a scheduled interval, and then execute a task when this date is reached.

IDM provides REST access to the task scanner, as listed in the following table:

| URI                                              | HTTP Operation | Description                                     |
| ------------------------------------------------ | -------------- | ----------------------------------------------- |
| /openidm/taskscanner                             | GET            | Lists all the scanning tasks, past and present. |
| /openidm/taskscanner/id                          | GET            | Lists details of the given task.                |
| /openidm/taskscanner?\_action=execute\&name=name | POST           | Triggers the specified task scan run.           |
| /openidm/taskscanner/id?\_action=cancel          | POST           | Cancels the specified task scan run.            |

---

---
title: Schedules
description: REST endpoints for managing PingIDM scheduled jobs and triggers, including creating, querying, pausing, and resuming schedules
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-schedules
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-schedules.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API"]
---

# Schedules

Use the [scheduler service](../../schedules-guide/schedules.html) to manage and monitor scheduled jobs.

You can access the scheduler service over REST, as indicated in the following table:

| URI                                                        | HTTP Operation                           | Description                                                         |
| ---------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------- |
| /openidm/scheduler?\_action=validateQuartzCronExpression   | POST                                     | Validates a cron expression.                                        |
| /openidm/scheduler/job/id                                  | PUT                                      | Creates or updates a schedule with the specified ID.                |
|                                                            | GET                                      | Obtains the details of the specified schedule.                      |
|                                                            | POST with ?\_action=trigger*API V2 only* | Manually triggers the specified schedule.                           |
|                                                            | POST with ?\_action=pause*API V2 only*   | Suspends the specified schedule.                                    |
|                                                            | POST with ?\_action=resume*API V2 only*  | Resumes the specified schedule.                                     |
|                                                            | DELETE                                   | Deletes the specified schedule.                                     |
| /openidm/scheduler/job?\_action=create                     | POST                                     | Creates a schedule with a system-generated ID.                      |
| /openidm/scheduler/job?\_queryFilter=query                 | GET                                      | Queries the existing defined schedules.                             |
| /openidm/scheduler/job?\_action=listCurrentlyExecutingJobs | POST                                     | Returns a list of the jobs that are currently running.              |
| /openidm/scheduler/job?\_action=pauseJobs                  | POST                                     | Suspends all scheduled jobs.                                        |
| /openidm/scheduler/job?\_action=resumeJobs                 | POST                                     | Resumes all suspended scheduled jobs.                               |
| /openidm/scheduler/trigger?\_queryFilter=query             | GET                                      | Queries the existing triggers.                                      |
| /openidm/scheduler/trigger/id                              | GET                                      | Obtains the details of the specified trigger.                       |
| /openidm/scheduler/acquiredTriggers                        | GET                                      | Returns an array of the triggers that have been acquired, per node. |
| /openidm/scheduler/waitingTriggers                         | GET                                      | Returns an array of the triggers that have not yet been acquired.   |

---

---
title: Schema
description: REST endpoints for reading and managing PingIDM managed object schemas, including creating and deleting custom relationship properties
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-schema
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-schema.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Schema", "Relationships", "REST API"]
---

# Schema

The Schema API lets you perform operations on managed object schemas. You can create, update, and delete custom relationship properties for managed objects using version 2 of the API. The following table lists the available endpoints for the `/schema/` context path:

| URI                                                      | HTTP Operation | Description                                                                                         |
| -------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------- |
| `/openidm/schema/managed/assignment`                     | GET            | Returns the schema for the `managed/assignment` object.                                             |
| `/openidm/schema/managed/organization`                   | GET            | Returns the schema for the `managed/organization` object.                                           |
| `/openidm/schema/managed/role`                           | GET            | Returns the schema for the `managed/role` object.                                                   |
| `/openidm/schema/managed/user`                           | GET            | Returns the schema for the `managed/user` object.                                                   |
| `/openidm/schema/managed/user/properties/custom_Example` | GET            | Returns the `custom_Example` relationship property on the `managed/user` object schema.	API V2 only |
| `/openidm/schema/managed/user/properties/custom_Example` | PUT            | Creates the `custom_Example` relationship property on the `managed/user` object schema.	API V2 only |
| `/openidm/schema/managed/user/properties/custom_Example` | PUT            | Updates the `custom_Example` relationship property on the `managed/user` object schema.	API V2 only |
| `/openidm/schema/managed/user/properties/custom_Example` | DELETE         | Deletes the `custom_Example` relationship property on the `managed/user` object schema.	API V2 only |

The following example creates a custom many-to-many relationship property, `custom_Children`, with a reverse property, `custom_Parents`:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request PUT \
--data '{
  "description": "A user as a child of another user.",
  "title": "Custom children",
  "viewable": true,
  "type": "array",
  "required": false,
  "items": {
    "type": "relationship",
    "title": "Custom Parent",
    "reverseRelationship": true,
    "reversePropertyName": "custom_Parents",
    "notifySelf": false,
    "validate": true,
    "properties": {
      "_ref": {
        "description": "References a relationship from a managed object",
        "type": "string"
      },
      "_refProperties": {
        "description": "Supports metadata within the relationship",
        "type": "object",
        "title": "Custom Provisioning Children Parents _refProperties",
        "properties": {
          "_id": {
            "description": "_refProperties object ID",
            "type": "string"
          }
        }
      }
    },
    "resourceCollection": [
      {
        "path": "managed/alpha_user",
        "label": "User",
        "query": {
          "queryFilter": "true",
          "fields": [
            "userName"
          ]
        },
        "notify": false,
        "reverseProperty": {
          "type": "array",
          "validate": true,
          "resourceCollection": {
            "notify": false,
            "query": {
              "queryFilter": "true",
              "fields": [
                "userName"
              ]
            }
          }
        }
      }
    ]
  }
}
' \
"https://localhost:8443/openidm/schema/managed/user/properties/custom_Children"
```

---

---
title: Scripts
description: REST endpoints to compile and evaluate PingIDM scripts, with examples for JavaScript, file-based scripts, and Base64 operations
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-scripts
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-scripts.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Scripts"]
section_ids:
  example_script_compile: Example script compile
  example_script_eval_from_file: Example script eval from file
  script-base64-example: Example script eval Base64 encode/decode
---

# Scripts

You can interact with the script service over REST, as shown in the following table:

| URI                              | HTTP Operation | Description                                                                                                                                                                                                                        |
| -------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /openidm/script?\_action=compile | POST           | Compiles a script, to validate that it can be executed. Note that this action compiles a script, but does not execute it. A successful compilation returns `true`. An unsuccessful compilation returns the reason for the failure. |
| /openidm/script?\_action=eval    | POST           | Executes a script and returns the result, if any.                                                                                                                                                                                  |

## Example script compile

The following example compiles, but does not execute, the script provided in the JSON payload:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "type": "text/javascript",
  "source": "source.mail ? source.mail.toLowerCase() : null"
}' \
"http://localhost:8080/openidm/script?_action=compile"
True
```

## Example script eval from file

The following example executes the script referenced in the `file` parameter, with the provided input:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "type": "text/javascript",
  "file": "script/autoPurgeAuditRecon.js",
  "globals": {
    "input": {
      "mappings": ["%"],
      "purgeType": "purgeByNumOfRecordsToKeep",
      "numOfRecons": 1
    }
  }
}' \
"http://localhost:8080/openidm/script?_action=eval"
"Must choose to either purge by expired or number of recons to keep"
```

## Example script eval Base64 encode/decode

The following examples evaluate the `atob` (Base64-decode) and `btoa` (Base64-encode) global script bindings:

* atob

* btoa

Request

```none
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "type": "text/javascript",
  "source": "atob(\"SGVsbG8gV29ybGQh\");"
}' \
"http://localhost:8080/openidm/script?_action=eval"
```

Response

```none
"Hello World!"
```

Request

```none
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "type": "text/javascript",
  "source": "btoa(\"Hello World!\");"
}' \
"http://localhost:8080/openidm/script?_action=eval"
```

Response

```none
"SGVsbG8gV29ybGQh"
```

Learn more in [Global utility functions](../../scripting-guide/scripting-func-ref.html#global-utility-functions).

---

---
title: Server configuration
description: REST endpoints for reading, updating, patching, and deleting PingIDM server configuration objects
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-server-config
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-server-config.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Setup &amp; Configuration"]
---

# Server configuration

IDM stores configuration objects in the repository, and exposes them under the context path `/openidm/config`. Single instance configuration objects are exposed under `/openidm/config/object-name`.

Multiple instance configuration objects are exposed under `/openidm/config/object-name/instance-name`. The following table outlines these configuration objects and how they can be accessed through the REST interface.

| URI                                                  | HTTP Operation | Description                                                                                                                       |
| ---------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| /openidm/config                                      | GET            | Returns a list of configuration objects.                                                                                          |
| /openidm/config/access                               | GET            | Returns the current access configuration.                                                                                         |
| /openidm/config/audit                                | GET            | Returns the current audit configuration.                                                                                          |
| /openidm/config/provisioner.openicf/provisioner-name | GET            | Returns the configuration of the specified connector.                                                                             |
| /openidm/config/router                               | PUT            | Changes the router configuration. Modifications are provided with the `--data` option, in JSON format.                            |
| /openidm/config/object                               | PATCH          | Changes one or more fields of the specified configuration object. Modifications are provided as a JSON array of patch operations. |
| /openidm/config/object                               | DELETE         | Deletes the specified configuration object.                                                                                       |
| /openidm/config/object?\_queryFilter=query           | GET            | Queries the specified configuration object. You cannot create custom predefined queries to query the configuration.               |

IDM supports REST operations to create, read, update, query, and delete configuration objects.

For command-line examples of managing the configuration over REST, refer to [Configure the server over REST](../../setup-guide/configuring-over-rest.html).

One entry is returned for each configuration object. To obtain additional information on the configuration object, include its `pid` or `_id` in the URL. The following example displays configuration information on the `sync` object, based on a deployment using the `sync-with-csv` sample:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/config/sync"
{
  "_id": "sync",
  "mappings": [
    {
      "name": "systemCsvfileAccounts_managedUser",
      "source": "system/csvfile/account",
      "target": "managed/user",
      "correlationQuery": {
        "type": "text/javascript",
        "source": "var query = {'_queryId' : 'for-userName', 'uid' : source.name};query;"
      },
      "properties": [
        {
          "source": "email",
          "target": "mail"
        },
        {
          "source": "firstname",
          "target": "givenName"
        },
        {
          "source": "lastname",
          "target": "sn"
        },
        {
          "source": "description",
          "target": "description"
        },
        {
          "source": "_id",
          "target": "_id"
        },
        {
          "source": "name",
          "target": "userName"
        },
        {
          "default": "Passw0rd",
          "target": "password"
        },
        {
          "source": "mobileTelephoneNumber",
          "target": "telephoneNumber"
        },
        {
          "source": "roles",
          "transform": {
            "type": "text/javascript",
            "source": "var _ = require('lib/lodash'); _.map(source.split(','), function(role)
            { return {'_ref': 'internal/role/' + role} });"
          },
          "target": "authzRoles"
        }
      ],
...
```
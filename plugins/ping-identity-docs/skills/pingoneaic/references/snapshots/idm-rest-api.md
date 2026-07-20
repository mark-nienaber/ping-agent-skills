---
title: Bulk import
description: Import large numbers of entries from CSV files into the repository
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-bulk-import
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-bulk-import.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Bulk import

The bulk import service lets you import large numbers of entries from a CSV file into the IDM repository. Importing user entries is a very common use case, but you can import any managed object type.

The following table shows the endpoints used by the bulk import service:

| URI                                                                | HTTP Operation | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `/openidm/csv/template?resourceCollection=managed/realm-name_user` | GET            | Generates a CSV header row that you can use as a template for the import. You can safely remove generated columns for properties that are not required. Set the query parameters `_fields=header` and `_mimeType=text/csv` to download the header file.                                                                                                                                                                                          |
| `/upload/csv/resourceCollection`                                   | POST           | Uploads the file specified by the `--form` (`-F`) parameter to the specified resource collection. `?uniqueProperty=propertyName` is required. Generally, for `managed/realm-name_user` objects, the `uniqueProperty` is `userName`. You can specify multiple comma-delimited values here to identify unique records; for example, `?uniqueProperty=firstName,lastName`. [Example](../../idm-synchronization/import-data.html#query-bulk-import). |
| `/openidm/csv/metadata/?_action=cleanupList`                       | POST           | Returns the import UUIDs that have error records or temporary records. These can be cleaned up to free up database space. If you clean up error records, you will no longer be able to download a CSV of failed import records.                                                                                                                                                                                                                  |
| `/openidm/csv/metadata/importUUID?_action=cleanup`                 | POST           | Cleans up temporary import records for the specified import UUID. To also clean up error records, set the query parameter `?deleteErrorRecords=true`.                                                                                                                                                                                                                                                                                            |
| `/openidm/csv/metadata/importUUID?_action=cancel`                  | POST           | Cancels the specified in-progress import.                                                                                                                                                                                                                                                                                                                                                                                                        |
| `/openidm/csv/metadata/importUUID`                                 | DELETE         | Deletes the specified import record. This does not affect the data that was imported.                                                                                                                                                                                                                                                                                                                                                            |
| `/openidm/csv/metadata?_queryFilter`                               | GET            | Queries bulk imports.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `/openidm/csv/metadata/importUUID`                                 | GET            | Returns the specified import record.                                                                                                                                                                                                                                                                                                                                                                                                             |
| `/export/csvImportFailures/importUUID`                             | GET            | Downloads a CSV file of failed import records. Returns 404 if there were no failures for the specified import UUID.                                                                                                                                                                                                                                                                                                                              |

---

---
title: Email
description: Send email and email templates through the outbound email service
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-email
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-email.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  externalemail_post_parameters: external/email POST parameters
---

# Email

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | To configure the email service, see [Email provider](../../tenants/email-provider.html). |

You can use the IDM outbound email service over REST at the `external/email` endpoint:

| URI                                           | HTTP Operation | Description              |
| --------------------------------------------- | -------------- | ------------------------ |
| /openidm/external/email?\_action=send         | POST           | Sends an email.          |
| /openidm/external/email?\_action=sendTemplate | POST           | Sends an email template. |

For additional examples, refer to [Send mail](../../tenants/email-send.html).

## `external/email` POST parameters

Advanced Identity Cloud supports the following POST parameters:

* `from`

  Sender mail address

* `to`

  Comma-separated list of recipient mail addresses

* `cc`

  Optional comma-separated list of copy recipient mail addresses

* `bcc`

  Optional comma-separated list of blind copy recipient mail addresses

* `subject`

  Email subject

* `body`

  Email body text

* `_locale`

  Takes precedence over `defaultLocale` but not `preferredLocales` specified in the `Accept-Language` header. If no preferred locales are set, uses the specified locale ([ISO 639-1 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).

* `type`

  Optional MIME type. One of `"text/plain"`, `"text/html"`, or `"text/xml"`.

---

---
title: Feature enablement
description: Install and enable features that require updating tenant configuration
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-feature
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-feature.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/2FA-profile-attr.adoc"]
section_ids:
  groups_feature: Groups feature
  feature-enable-pass-timestamp-attributes: Password timestamp attributes
  feature-enable-indexed-string-attributes: Additional indexed string attributes
  feature-enable-2fa-profile-attributes: Two-factor authentication (2FA) profile attributes
---

# Feature enablement

Existing tenants can use the `openidm/feature` endpoint to install new features that require updating existing tenant configuration. Use this endpoint to test the feature in a developer environment before migrating those changes to production.

The `openidm/feature` endpoint requires an [access token](../../developer-docs/authenticate-to-rest-api-with-access-token.html) with the `fr:idm:*` scope. Learn more about making REST calls in [Use an access token](../../developer-docs/authenticate-to-rest-api-with-access-token.html).

|   |                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Uninstalling or disabling a feature once installed requires contacting support and rolling back your tenant. Always test installing a feature *first*, before making any changes to your production environment. |

| URI                                 | HTTP Operation | Description                                                                                          |
| ----------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------- |
| /openidm/feature?\_queryFilter=true | GET            | Returns a list of feature objects. If a feature is not installed, `installedVersion` returns `null`. |

## Groups feature

For more information, refer to [Groups](../../idm-objects/groups.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To install the `groups` feature, ensure the following:- The managed configuration defines the `alpha_user` and `bravo_user` objects.

- The `repo.ds` configuration defines the `alpha_user` and `bravo_user` generic mappings.

- The managed configuration for `alpha_user` and `bravo_user` does *not* define the `groups` or `effectiveGroups` properties.

- The managed configuration does *not* define the `alpha_group` or `bravo_group` objects.

- The `repo.ds` configuration for the `alpha_user` and `bravo_user` generic mappings does *not* define the `groups` or `effectiveGroups` properties.

- Resources do *not* exist in the repository for `alpha_group` or `bravo_group`. |

| URI                                       | HTTP Operation | Description                                                                                                                                                                                 |
| ----------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /openidm/feature/groups                   | GET            | Returns the status of the groups feature.                                                                                                                                                   |
| /openidm/feature/groups?\_action=validate | POST           | Validates that the groups feature is available to install:- Returns `status` as `true` if the feature can be installed.

- Returns `status` as `false` if the feature is already installed. |
| /openidm/feature/groups?\_action=install  | POST           | Attempts to patch and install a tenant's configuration to enable the groups feature.                                                                                                        |

## Password timestamp attributes

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | These attributes are enabled by default in tenants created on or after February 06, 2024. |

This feature adds two indexed string attributes to your tenant that can be used to query when a user password was last changed and when it's set to expire. Learn more in [Password timestamps](../../realms/password-policy.html#password-timestamps).

| URI                                                    | HTTP Operation | Description                                                                                                                                                                                             |
| ------------------------------------------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /openidm/feature/password/timestamps                   | GET            | Returns the status of the password timestamp feature.                                                                                                                                                   |
| /openidm/feature/password/timestamps?\_action=validate | POST           | Validates that the password timestamp feature is available to install:- Returns `status` as `true` if the feature can be installed.

- Returns `status` as `false` if the feature is already installed. |
| /openidm/feature/password/timestamps?\_action=install  | POST           | Attempts to patch and install a tenant's configuration to enable the password timestamp feature.                                                                                                        |

## Additional indexed string attributes

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | These attributes are enabled by default in tenants created on or after November 12, 2024. |

This feature adds 15 additional indexed string attributes to your tenant that can be used as general purpose extension attributes.

You can install this feature using the `feature` endpoint. To do so:

1. Confirm that the feature is available by calling `GET openidm/feature/indexed/strings/6thru20`:

   ```json
   {
       "_id": "indexed/strings/6thru20",
       "installedVersion": null,
       "availableVersions": [
           "1"
       ]
   }
   ```

2. Validate that the feature is installable by calling `POST /openidm/feature/indexed/strings/6thru20?_action=validate`:

   ```json
   {
       "status": 200,
       "success": true,
       "message": "Validate complete."
   }
   ```

3. Install the feature by calling `POST /openidm/feature/indexed/strings/6thru20?_action=install`:

   ```json
   {
       "status": 200,
       "message": "Install complete."
   }
   ```

4. Confirm that the feature is no longer installable by calling `POST /openidm/feature/indexed/strings/6thru20?_action=validate`:

   ```json
   {
       "status": 200,
       "success": false,
       "message": "Validate complete.config/repo.ds: frIndexedString6 must not already exist.",
   }
   ```

| URI                                                        | HTTP Operation | Description                                                                                                                                                                                                     |
| ---------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /openidm/feature/indexed/strings/6thru20                   | GET            | Returns the status of the additional indexed strings feature.                                                                                                                                                   |
| /openidm/feature/indexed/strings/6thru20?\_action=validate | POST           | Validates that the additional indexed strings feature is available to install:- Returns `status` as `true` if the feature can be installed.

- Returns `status` as `false` if the feature is already installed. |
| /openidm/feature/indexed/strings/6thru20?\_action=install  | POST           | Attempts to patch and install a tenant's configuration to enable the additional indexed strings feature.                                                                                                        |

## Two-factor authentication (2FA) profile attributes

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | These attributes are enabled by default in tenants created on or after January 09, 2025. |

This feature adds the following five multivalue (array) strings to existing Alpha and Bravo realm user identities in PingOne Advanced Identity Cloud:

* `deviceProfiles`

* `devicePrintProfiles`

* `webauthnDeviceProfiles`

* `oathDeviceProfiles`

* `pushDeviceProfiles`

The attributes can be used to store references to a user's associated two-factor authentication (2FA) devices.

You can install this feature using the `feature` endpoint:

1. Confirm that the feature is available by calling `GET openidm/feature/am/2fa/profiles`:

   ```json
   {
     "_id": "am/2fa/profiles",
     "installedVersion": null,
     "availableVersions": [
       "1"
     ]
   }
   ```

2. Validate that the feature is installable by calling `POST /openidm/feature/am/2fa/profiles?_action=validate`:

   ```json
   {
     "status": 200,
     "success": true,
     "message": "Validate complete."
   }
   ```

3. Install the feature by calling `POST /openidm/feature/am/2fa/profiles?_action=install`:

   ```json
   {
     "status": 200,
     "message": "Install complete."
   }
   ```

4. Confirm that the feature is no longer installable by calling `POST /openidm/feature/am/2fa/profiles?_action=validate`:

   ```json
   {
     "status": 200,
     "success": false,
     "message": "Validate complete.config/repo.ds: am2faProfiles must not already exist."
   }
   ```

| URI                                                | HTTP Operation | Description                                                                                                                                                                                                 |
| -------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /openidm/feature/am/2fa/profiles                   | GET            | Returns the status of the 2FA profile attributes feature.                                                                                                                                                   |
| /openidm/feature/am/2fa/profiles?\_action=validate | POST           | Validates that the 2FA profile attributes feature is available to install:- Returns `status` as `true` if the feature can be installed.

- Returns `status` as `false` if the feature is already installed. |
| /openidm/feature/am/2fa/profiles?\_action=install  | POST           | Attempts to patch and install a tenant's configuration to enable the 2FA profile attributes feature.                                                                                                        |

---

---
title: Internal objects
description: Manage internal roles and users with limited REST operations
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-internal
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-internal.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Internal objects

The following table lists the REST endpoints associated with internal objects:

| URI                                                     | HTTP Operation | Description                                                                    |
| ------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------ |
| /openidm/internal/role?\_queryFilter=true               | GET            | Returns all internal roles.                                                    |
| /openidm/internal/user?\_queryFilter=true               | GET            | Returns all internal users.                                                    |
| /openidm/internal/user/username                         | PUT            | Adds a new internal user or changes the password of an existing internal user. |
| /openidm/internal/user/username                         | PATCH          | Adds or removes roles of an internal user.                                     |
| /openidm/internal/role?\_queryFilter=true&\_fields=\_id | GET            | Returns internal roles.                                                        |
| /openidm/internal/role/role-id?\_fields=\*,authzMembers | GET            | Returns internal and managed users with the specified internal role.           |

---

---
title: Managed groups
description: Manage group objects including creation, modification, and member operations
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-managed-groups
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-managed-groups.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Managed groups

Groups are exposed under the context path `managed/realm-name_group`. The following table lists the REST commands associated with managed groups.

| URI                                                                 | HTTP Operation | Description                                                                                                                   |
| ------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| /openidm/managed/realm-name\_group?\_queryFilter=true&\_fields=\_id | GET            | Returns the IDs of all managed groups.                                                                                        |
| /openidm/managed/realm-name\_group?\_queryFilter=filter             | GET            | Queries managed groups with the defined filter.                                                                               |
| /openidm/managed/realm-name\_group/\_id                             | GET            | Returns the JSON representation of a specific group.                                                                          |
| /openidm/managed/realm-name\_group/\_id?\_fields=name,members       | GET            | Returns the relationships (members) associated with a group.                                                                  |
| /openidm/managed/realm-name\_group/\_id/members?\_queryFilter=true  | GET            | Returns the members of a group.                                                                                               |
| /openidm/managed/realm-name\_group/\_id/members?\_action=create     | POST           | Adds a member to a group.                                                                                                     |
| /openidm/managed/realm-name\_group/\_id                             | PUT            | Updates a group by replacing the entire object with a new one. If no group entry exists with that `_id`, one will be created. |
| /openidm/managed/realm-name\_group?\_action=create                  | POST           | Creates a new group. `_id` and `name` will be the same.                                                                       |
| /openidm/managed/realm-name\_group/\_id                             | DELETE         | Deletes a group.                                                                                                              |

For additional commands and examples, refer to [Groups](../../idm-objects/groups.html).

---

---
title: Managed organizations
description: Perform REST operations on managed organization objects and hierarchies
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-managed-organizations
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-managed-organizations.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Managed organizations

Organizations are exposed under the context path `/managed/realm-name_organization`. The following table lists the REST commands associated with managed organizations.

| URI                                                                      | HTTP Operation | Description                                                                                                             |
| ------------------------------------------------------------------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `/openidm/managed/realm-name_organization?_queryFilter=true&_fields=_id` | GET            | Returns the IDs of all managed organizations.                                                                           |
| `/openidm/managed/realm-name_organization?_queryFilter=filter`           | GET            | Queries managed organizations with the defined filter.                                                                  |
| `/openidm/managed/realm-name_organization/_id`                           | GET            | Returns the JSON representation of a specific organization.                                                             |
| `/openidm/managed/realm-name_organization/_id`                           | PUT            | Creates an organization with a user-defined ID.                                                                         |
| `/openidm/managed/realm-name_organization/_id`                           | PUT            | Updates an organization by replacing the entire object. If no organization exists with that `_id`, one will be created. |
| `/openidm/managed/realm-name_organization?_action=create`                | POST           | Creates a new organization with a system-generated ID.                                                                  |
| `/openidm/managed/realm-name_organization/_id`                           | DELETE         | Deletes an organization.                                                                                                |

For additional commands and examples, refer to [Manage organizations over REST](../../idm-objects/manage-orgs-rest.html).

---

---
title: Managed users
description: Perform REST operations to create, read, update, and delete managed users
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-managed-users
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-managed-users.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Managed users

User objects are stored in the repository and are exposed under the context path `/managed/realm-name_user`.

The following table lists available functionality associated with the `/managed/realm-name_user` context path:

| URI                                                                                 | HTTP Operation | Description                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/openidm/managed/realm-name_user?_queryFilter=true&_fields=_id`                    | GET            | Returns the IDs of all the managed users in the repository.                                                                                                                                                                                                                 |
| `/openidm/managed/realm-name_user?_queryFilter=true`                                | GET            | Returns all information for all managed users in the repository.                                                                                                                                                                                                            |
| `/openidm/managed/realm-name_user?_queryFilter=filter`                              | GET            | Returns the managed user object with the defined filter.                                                                                                                                                                                                                    |
| `/openidm/managed/realm-name_user/_id`                                              | GET            | Returns the JSON representation of a specific user.                                                                                                                                                                                                                         |
| `/openidm/managed/realm-name_user/_id`                                              | PUT            | Updates a user entry by replacing it entirely with the new data. If a user entry with that `_id` does not exist in the system, one will be created.	If you create an object using PUT, the ID you assign must be a UUID, for example, 4cf65bb9-baa4-4488-aa73-216adf0787a1. |
| `/openidm/managed/realm-name_user?_action=create`                                   | POST           | Creates a new user.                                                                                                                                                                                                                                                         |
| `/openidm/managed/realm-name_user?_action=patch&_queryId=for-userName&uid=userName` | POST           | Updates specified fields of a user entry.                                                                                                                                                                                                                                   |
| `/openidm/managed/realm-name_user/_id`                                              | PATCH          | Updates specified fields of a user entry.                                                                                                                                                                                                                                   |
| `/openidm/managed/realm-name_user/_id`                                              | DELETE         | Deletes a user entry.                                                                                                                                                                                                                                                       |

For additional commands and examples, refer to [Manage identities](../../idm-objects/users.html).

---

---
title: PingIDM REST API reference
description: Guide to creating and managing objects in Advanced Identity Cloud.
component: pingoneaic
page_id: pingoneaic:idm-rest-api:preface
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
---

# PingIDM REST API reference

> Guide to creating and managing objects in Advanced Identity Cloud.

This reference describes specific characteristics of identity management REST APIs. For an overview of ForgeRock REST APIs, refer to [Advanced Identity Cloud REST](../developer-docs/crest/about-crest.html).

Quick Start

[icon: play-circle, set=fas, size=3x]

#### [Start Here](rest-and-idm.html)

Learn about ForgeRock REST APIs and how they apply to identity management.

[icon: cogs, set=fas, size=3x]

#### [REST API Structure](rest-structure.html)

Understand RESTful syntax of the identity management APIs.

[icon: list, set=fas, size=3x]

#### [REST Endpoints](endpoints/rest-server-config.html)

Discover the REST endpoints for identity management.

---

---
title: Privileges
description: Query privileges associated with resources for authenticated users
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-privileges
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-privileges.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Privileges

Privileges are a part of internal roles, and can be created or modified using the REST calls specified in [Internal objects](rest-internal.html). Additionally, `openidm/privilege` can be used for getting information about privileges on a resource as they apply to the authenticated user.

The following table outlines the REST endpoints used to access privileges.

| URI                                        | HTTP Operation | Description                                                                                                               |
| ------------------------------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------- |
| /openidm/privilege?\_action=listPrivileges | POST           | Returns an array of privilege paths for the authenticated user, with additional detail required by the IDM admin console. |
| /openidm/privilege/resource                | GET            | Returns the privileges for the logged in user associated with the given resource path.                                    |
| /openidm/privilege/resource/guid           | GET            | Returns the privileges for the logged in user associated with the specified object.                                       |

---

---
title: Reconciliation operations
description: Launch and monitor reconciliation operations between data stores
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-recon
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-recon.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Reconciliation operations

Reconciliation is the process of ensuring that the objects in two different data stores are consistent. IDM can reconcile any object, such as groups, roles, and devices.

The following table lists available endpoints associated with the reconciliation engine:

| URI                                                            | HTTP Operation | Description                                                                                                            |
| -------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| /openidm/recon                                                 | GET            | Returns all reconciliation runs, including those in progress. The `state` property contains the reconciliation status. |
| /openidm/recon?\_action=recon\&mapping=mapping-name            | POST           | Launches a reconciliation run with the specified mapping.                                                              |
| /openidm/recon?\_action=reconById\&mapping=mapping-name\&id=id | POST           | Restricts the reconciliation run to the specified ID.                                                                  |
| /openidm/recon/id?\_action=cancel                              | POST           | Cancels the specified reconciliation run.                                                                              |

The following example runs a reconciliation for the [mapping](../../idm-synchronization/mappings.html) `systemHrdb_managedUser`:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/recon?_action=recon&mapping=systemHrdb_managedUser"
```

For more information on reconciliation, refer to [Synchronization types](../../idm-synchronization/sync-types.html).

---

---
title: REST and IDM
description: Understand REST architecture and how it applies to Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:idm-rest-api:rest-and-idm
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/rest-and-idm.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  crest-idm-specifics: ForgeRock REST and IDM
---

# REST and IDM

Representational State Transfer (REST) is a software architecture style for exposing resources, using the technologies and protocols of the World Wide Web. REST describes how distributed data objects, or resources, can be defined and addressed.

IDM provides a RESTful API for accessing managed objects, system objects, workflows, and the system configuration.

## ForgeRock REST and IDM

IDM implements the ForgeRock REST API as described in the previous section, with the exception of the following elements:

* IDM provides limited support for the [in expression clause](../idm-objects/queries.html#query-in). You can use this clause for queries on singleton string properties, not arrays. `in` query expressions are not supported through the IDM admin console.

* The PATCH `transform` action is supported only on the `config` endpoint. Note that this is an optional action and not implemented everywhere across the ForgeRock Identity Platform.

* ForgeRock REST supports PATCH operations by list element index, as shown in the example in [Patch](../developer-docs/crest/patch.html). IDM *does not support* PATCH by list element index. So, for PATCH operations, you cannot use an ordinal when adding or removing list items.

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

* IDM does not implement the `ESTIMATE` total paged results policy. The `totalPagedResults` is either the exact total result count (`_totalPagedResultsPolicy=EXACT`) or result counting is disabled (`_totalPagedResultsPolicy=NONE`). For more information, refer to [Page Query Results](../idm-objects/queries.html#paging-query-results).

---

---
title: REST API structure
description: Understand RESTful syntax for identity management APIs including URIs and operations
component: pingoneaic
page_id: pingoneaic:idm-rest-api:rest-structure
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/rest-structure.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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

Every managed and system object has an identifier (expressed as id in the URI scheme) used to address the object through the REST API. The REST API allows for client-generated and server-generated identifiers, through PUT and POST methods. The default server-generated identifier type is a UUID. If you create an object using `POST`, a server-assigned ID is generated in the form of a UUID. If you create a managed user object using PUT the client-assigned ID must be in the form of a UUID.

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
description: Specify REST API version numbers to ensure compatibility across releases
component: pingoneaic
page_id: pingoneaic:idm-rest-api:rest-api-versioning
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/rest-api-versioning.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  api-version-over-rest: Specify the API version in REST calls
  api-version-in-scripts: Specify the API version in scripts
  api_version_header_warnings: API version header warnings
  filter_resource_path_warnings: Filter resource path warnings
---

# REST API versioning

ForgeRock REST API features are assigned version numbers. Providing version numbers in the REST API helps ensure compatibility between releases. The version number of a feature increases when ForgeRock introduces a change that is not backwards-compatible, and that affects clients that use the feature.

If there is more than one version of the API, you must select the version by setting a version header that specifies which version of the *resource* is requested. To ensure that your clients are always compatible with a newer IDM version, you should always include resource versions in your REST calls.

## Specify the API version in REST calls

HTTP requests can optionally include the `Accept-API-Version` header with the value of the resource version, such as `resource=2.0`. If no `Accept-API-Version` header is included, the *latest* resource version is invoked by the HTTP request.

The following call requests version `2.0` of the specified resource:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
--data '{
  "url":"https://www.pingidentity.com/favicon.ico",
  "method":"GET"
}' \
"https://<tenant-env-fqdn>/openidm/external/rest?_action=call"
```

## Specify the API version in scripts

You can specify a resource version in scripts using the fourth (*additional parameters*) argument. If present, the `Accept-API-Version` parameter is applied to the actual REST request. Any other parameters are set as Additional Parameters on the request.

The following examples request specific resource versions:

REST with Inline Javascript

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "type":"text/javascript",
  "source":"openidm.action(\"external/rest\", \"call\", {\"url\": \"https://www.pingidentity.com/favicon.ico\", \"method\": \"GET\"}, {\"Accept-API-Version\": \"resource=1.0\"});"
}' \
"https://<tenant-env-fqdn>/openidm/script?_action=compile"
```

Standalone Javascript

```javascript
openidm.action("external/rest", "call",
 {"url": "https://www.pingidentity.com/favicon.ico", "method": "GET"},
 {"Accept-API-Version": "resource=1.0"});
```

## API version header warnings

IDM can log warnings when API version headers are not specified. Additionally, you can enable warnings when *scripts* don't specify API versions. Warnings are disabled by default. To enable this feature, set one or more of the following properties:

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

### Filter resource path warnings

To filter which resource paths are logged, edit the `logFilterResourcePaths` array located in the `apiVersion` configuration:

1. Get the current configuration:

   ```none
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "https://<tenant-env-fqdn>/openidm/config/apiVersion"
   ```

   > **Collapse: Default  Configuration**
   >
   > ```json
   > {
   >     "warning" : {
   >         "enabled" : {
   >             "$bool" : "&{openidm.apiVersion.warning.enabled|false}"
   >         },
   >         "includeScripts" : {
   >             "$bool" : "&{openidm.apiVersion.warning.includeScripts|false}"
   >         },
   >         "logFilterResourcePaths" : [
   >             "audit",
   >             "authentication",
   >             "cluster",
   >             "config",
   >             "consent",
   >             "csv",
   >             "external/rest",
   >             "identityProviders",
   >             "info",
   >             "internal",
   >             "internal/role",
   >             "internal/user",
   >             "internal/usermeta",
   >             "managed",
   >             "managed/alpha_assignment",
   >             "managed/alpha_organization",
   >             "managed/alpha_role",
   >             "managed/alpha_user",
   >             "managed/alpha_usermeta",
   >             "managed/alpha_group",
   >             "managed/alpha_application",
   >             "managed/bravo_assignment",
   >             "managed/bravo_organization",
   >             "managed/bravo_role",
   >             "managed/bravo_user",
   >             "managed/bravo_usermeta",
   >             "managed/bravo_group",
   >             "managed/bravo_application",
   >             "managed/teammember",
   >             "managed/teammembermeta",
   >             "managed/svcacct",
   >             "notification",
   >             "policy",
   >             "privilege",
   >             "profile",
   >             "recon",
   >             "recon/assoc",
   >             "repo",
   >             "selfservice/kba",
   >             "selfservice/terms",
   >             "scheduler/job",
   >             "scheduler/trigger",
   >             "schema",
   >             "sync",
   >             "sync/mappings",
   >             "system",
   >             "taskscanner"
   >         ]
   >     }
   > }
   > ```

2. Make changes, and replace the configuration:

   ```none
   curl \
   --header "Authorization: Bearer <access-token>" \
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
   "https://<tenant-env-fqdn>/openidm/config/apiVersion"
   ```

---

---
title: Scanning tasks
description: Scan for dates on schedule and execute tasks when dates are reached
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-task-scanner
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-task-scanner.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Scanning tasks

The [task scanner](../../idm-schedules/task-scanner.html) lets you perform a batch scan for a specified date, on a scheduled interval, and then execute a task when this date is reached.

The following table lists the endpoints associated with the task scanner:

| URI                                              | HTTP Operation | Description                                  |
| ------------------------------------------------ | -------------- | -------------------------------------------- |
| /openidm/taskscanner                             | GET            | Returns all present and past scanning tasks. |
| /openidm/taskscanner/id                          | GET            | Returns a task by `id`.                      |
| /openidm/taskscanner?\_action=execute\&name=name | POST           | Triggers the specified task scan run.        |
| /openidm/taskscanner/id?\_action=cancel          | POST           | Cancels the specified task scan run.         |

---

---
title: Schedules
description: Manage scheduled jobs using the scheduler service REST endpoints
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-schedules
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-schedules.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Schedules

Use the [scheduler service](../../idm-schedules/schedules.html) and its associated endpoints to manage and monitor scheduled jobs:

| URI                                                        | HTTP Operation                          | Description                                                         |
| ---------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------- |
| /openidm/scheduler?\_action=validateQuartzCronExpression   | POST                                    | Validates a cron expression.                                        |
| /openidm/scheduler/job/id                                  | PUT                                     | Creates or updates a schedule with the specified ID.                |
|                                                            | GET                                     | Returns the details of the specified schedule.                      |
|                                                            | POST with ?\_action=trigger	API V2 only | Manually triggers the specified schedule.                           |
|                                                            | POST with ?\_action=pause	API V2 only   | Suspends the specified schedule.                                    |
|                                                            | POST with ?\_action=resume	API V2 only  | Resumes the specified schedule.                                     |
|                                                            | DELETE                                  | Deletes the specified schedule.                                     |
| /openidm/scheduler/job?\_action=create                     | POST                                    | Creates a schedule with a system-generated ID.                      |
| /openidm/scheduler/job?\_queryFilter=query                 | GET                                     | Queries the existing defined schedules.                             |
| /openidm/scheduler/job?\_action=listCurrentlyExecutingJobs | POST                                    | Returns a list of the jobs that are currently running.              |
| /openidm/scheduler/job?\_action=pauseJobs                  | POST                                    | Suspends all scheduled jobs.                                        |
| /openidm/scheduler/job?\_action=resumeJobs                 | POST                                    | Resumes all suspended scheduled jobs.                               |
| /openidm/scheduler/trigger?\_queryFilter=query             | GET                                     | Queries the existing triggers.                                      |
| /openidm/scheduler/trigger/id                              | GET                                     | Returns the details of the specified trigger.                       |
| /openidm/scheduler/acquiredTriggers                        | GET                                     | Returns an array of the triggers that have been acquired, per node. |
| /openidm/scheduler/waitingTriggers                         | GET                                     | Returns an array of the triggers that have not yet been acquired.   |

---

---
title: Schema
description: Perform schema operations including creating custom relationship properties
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-schema
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-schema.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Schema", "Relationships", "REST API"]
---

# Schema

The Schema API lets you perform operations on managed object schemas. You can create, update, and delete custom relationship properties for managed objects using version 2 of the API. The following table lists the available endpoints for the `/schema/` context path:

| URI                                                                 | HTTP Operation | Description                                                                                                    |
| ------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------- |
| `/openidm/schema/managed/realm-name_assignment`                     | GET            | Returns the schema for the `managed/realm-name_assignment` object.                                             |
| `/openidm/schema/managed/realm-name_organization`                   | GET            | Returns the schema for the `managed/realm-name_organization` object.                                           |
| `/openidm/schema/managed/realm-name_role`                           | GET            | Returns the schema for the `managed/realm-name_role` object.                                                   |
| `/openidm/schema/managed/realm-name_user`                           | GET            | Returns the schema for the `managed/realm-name_user` object.                                                   |
| `/openidm/schema/managed/realm-name_user/properties/custom_Example` | GET            | Returns the `custom_Example` relationship property on the `managed/realm-name_user` object schema.	API V2 only |
| `/openidm/schema/managed/realm-name_user/properties/custom_Example` | PUT            | Creates the `custom_Example` relationship property on the `managed/realm-name_user` object schema.	API V2 only |
| `/openidm/schema/managed/realm-name_user/properties/custom_Example` | PUT            | Updates the `custom_Example` relationship property on the `managed/realm-name_user` object schema.	API V2 only |
| `/openidm/schema/managed/realm-name_user/properties/custom_Example` | DELETE         | Deletes the `custom_Example` relationship property on the `managed/realm-name_user` object schema.	API V2 only |

The following example creates a custom many-to-many relationship property, `custom_Children`, with a reverse property, `custom_Parents`:

```
curl \
--header "Authorization: Bearer <access-token>" \
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
"https://<tenant-env-fqdn>/openidm/schema/managed/realm-name_user/properties/custom_Children"
```

---

---
title: Scripts
description: Compile and validate scripts through the script service REST endpoint
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-scripts
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-scripts.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Scripts

You can interact with the script service over REST, as shown in the following table:

| URI                              | HTTP Operation | Description                                                                                                                                                                                                                        |
| -------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /openidm/script?\_action=compile | POST           | Compiles a script, to validate that it can be executed. Note that this action compiles a script, but does not execute it. A successful compilation returns `true`. An unsuccessful compilation returns the reason for the failure. |

The following example compiles, but does not execute, the script provided in the JSON payload:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "type": "text/javascript",
  "source": "source.mail ? source.mail.toLowerCase() : null"
}' \
"https://<tenant-env-fqdn>/openidm/script?_action=compile"
True
```

---

---
title: Server configuration
description: Access and modify configuration objects stored in the repository
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-server-config
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-server-config.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Server configuration

Advanced Identity Cloud stores configuration objects in the repository. They are accessed by making API requests to the context path `/openidm/config`.

Single instance configuration objects are accessed by adding the object's name to the request's path, for example, `/openidm/config/object-name`.

Multiple instance configuration objects are accessed by adding the object name and instance name to the request's path, for example, `/openidm/config/object-name/instance-name`.

The following table outlines the REST endpoints used to access configuration objects.

| URI                                                  | HTTP Operation | Description                                                                                                                       |
| ---------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| /openidm/config                                      | GET            | Returns a list of configuration objects.                                                                                          |
| /openidm/config/access                               | GET            | Returns the current access configuration.                                                                                         |
| /openidm/config/audit                                | GET            | Returns the current audit configuration.                                                                                          |
| /openidm/config/privileges                           | GET            | Returns the current privilege configuration for managed objects.                                                                  |
| /openidm/config/provisioner.openicf/provisioner-name | GET            | Returns the configuration of the specified connector.                                                                             |
| /openidm/config/selfservice/function                 | GET            | Returns the configuration of the specified self-service feature, `registration`, `reset`, or `username`.                          |
| /openidm/config/router                               | PUT            | Changes the router configuration. Modifications are provided with the `--data` option, in JSON format.                            |
| /openidm/config/object                               | PATCH          | Changes one or more fields of the specified configuration object. Modifications are provided as a JSON array of patch operations. |
| /openidm/config/object                               | DELETE         | Deletes the specified configuration object.                                                                                       |
| /openidm/config/object?\_queryFilter=query           | GET            | Queries the specified configuration object. You cannot create custom predefined queries to query the configuration.               |

Advanced Identity Cloud supports REST operations to create, read, update, query, and delete configuration objects.

One entry is returned for each configuration object. To obtain additional information on the configuration object, include its `pid` or `_id` in the URL. The following example displays configuration information on the `sync` object, based on a deployment using the `sync-with-csv` sample:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/config/sync"
{
  "_id": "sync",
  "mappings": [
    {
      "name": "systemCsvfileAccounts_managedUser",
      "source": "system/csvfile/account",
      "target": "managed/realm-name_user",
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

---

---
title: Server state
description: Access server state information including authentication status and version
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-info
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-info.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Server state

You can access information about the current state of the IDM instance through the `info` endpoint, as shown in the following table:

| URI                                                                                                                                                                                                            | HTTP Operation | Description                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------ |
| `/openidm/info/login`                                                                                                                                                                                          | GET            | Provides authentication and authorization details for the current user.                                            |
| `/openidm/info/ping`&#xA;&#xA;The /openidm/info/ping endpoint is a deprecated feature. Customers should update any external monitoring to use the Advanced Identity Cloud /monitoring/health endpoint instead. | GET            | Lists the current server state. Possible states are `STARTING`,`ACTIVE_READY`, `ACTIVE_NOT_READY`, and `STOPPING`. |
| `/openidm/info/version`                                                                                                                                                                                        | GET            | Provides the software version of this IDM instance.                                                                |

---

---
title: Synchronization service
description: Interact with synchronization service to manage mappings and queued events
component: pingoneaic
page_id: pingoneaic:idm-rest-api:endpoints/rest-sync
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-rest-api/endpoints/rest-sync.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Synchronization service

You can interact with the synchronization service over REST, as shown in the following table:

| URI                                                              | HTTP Operation | Description                                                                                                                                                                                                          |
| ---------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /openidm/sync?\_action=getLinkedResources\&resourceName=resource | POST           | Provides a list of linked resources for the specified resource.                                                                                                                                                      |
| /openidm/sync/mappings?\_queryFilter=true                        | GET            | Returns a list of all configured [mappings](../../idm-synchronization/mappings.html) in the order they'll be processed. Also supports [paging results](../../idm-synchronization/mappings.html#sync-mapping-paging). |
| /openidm/sync/queue?\_queryFilter=filter                         | GET            | Lists the [queued synchronization events](../../idm-synchronization/chap-implicit-live-sync.html#queued-sync-over-rest), based on the specified filter.                                                              |
| /openidm/sync/queue/eventID                                      | DELETE         | Deletes a queued synchronization event, based on its ID.                                                                                                                                                             |

For example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
"https://<tenant-env-fqdn>/openidm/sync?_action=getLinkedResources&resourceName=managed/realm-name_user/42f8a60e-2019-4110-a10d-7231c3578e2b"
[
  {
    "resourceName": "system/ldap/account/03496258-1c5e-40a0-8744-badc2500f262",
    "content": {
      "uid": "joe.smith1",
      "mail": "joe.smith@example.com",
      "sn": "Smith",
      "givenName": "Joe",
      "employeeType": [],
      "dn": "uid=joe.smith1,ou=People,dc=example,dc=com",
      "ldapGroups": [],
      "cn": "Joe Smith",
      "kbaInfo": [],
      "aliasList": [],
      "objectClass": [
        "top",
        "inetOrgPerson",
        "organizationalPerson",
        "person"
      ],
      "_id": "03496258-1c5e-40a0-8744-badc2500f262"
    },
    "linkQualifier": "default",
    "linkType": "systemLdapAccounts_managedUser"
  }
]
```
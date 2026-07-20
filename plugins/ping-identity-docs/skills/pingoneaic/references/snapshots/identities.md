---
title: Advanced Identity Cloud identity schema
description: Overview of the default and customizable identity schema for managing identity entities
component: pingoneaic
page_id: pingoneaic:identities:identity-cloud-identity-schema
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/identity-cloud-identity-schema.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Schema", "Custom Properties"]
section_ids:
  summary-of-the-identity-schema: Summary of the identity schema
  use-cases-for-customizing-the-identity-schema: Use cases for customizing the identity schema
---

# Advanced Identity Cloud identity schema

PingOne Advanced Identity Cloud uses a default identity schema to organize users, roles, assignments, groups, organizations, and applications. The following diagram shows the identity schema relationships:

![idcloud identity schema](_images/idcloud-identity-schema.png)

Learn more about the Advanced Identity Cloud identity schema in [Summary of the identity schema](#summary-of-the-identity-schema).

You can customize the default identity schema to your business needs in the following ways:

* Create custom properties to store identity information specific to your business.

* Create indexable custom properties that let you search your identities and create customized segments.

* Create [organizations](organizations.html) to structure your identities in a flexible and performant way.

For examples of customizing the Advanced Identity Cloud identity schema, learn more in [Use cases for customizing the identity schema](#use-cases-for-customizing-the-identity-schema).

## Summary of the identity schema

* Users, roles, assignments, groups, organizations, and applications form the default identity schema. Their relationships are also part of the default schema.

* Users are *hybrid* object types:

  * Their default properties are explicitly defined in the schema with indexes also explicitly defined for these properties. These default properties include:

    * `givenName`

    * `mail`

    * `passwordLastChangedTime`

    * `passwordExpirationTime`

    * `sn`

    * `userName`

  * You can add custom properties to them. However, the properties are stored in an unindexed JSON data structure.

  * If you need a custom property for a user to be searchable, use an [indexed extension property](customize-object-types.html#use-general-purpose-extension-attributes) instead of a custom property.

* Roles, assignments, groups, and organizations are *generic* object types:

  * None of their properties are explicitly defined in the schema, and instead they are entirely stored in an indexed JSON data structure.

  * You can add custom properties to them, and they'll also be indexed.

* You can create custom object types. These custom object types are also generic. This means that they are entirely stored in an indexed JSON data structure.

* Applications are also generic object types. However, you shouldn't alter these in any way as they're reserved for modification by Ping Identity to support workforce use cases. You shouldn't add custom properties to them, repurpose their default properties, or reconcile data into them.

|   |                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - Advanced Identity Cloud doesn't support the modification of application object types.

- Ping Identity recommends that you add no more than 12 custom properties each to roles, assignments, groups, and organizations, as this can impact the performance of your tenant environments. |

The following table summarizes the identity schema:

| Object type                            | Type    | Indexes on default properties?           | Indexes on custom properties?              |
| -------------------------------------- | ------- | ---------------------------------------- | ------------------------------------------ |
| Users                                  | Hybrid  | [icon: check, set=fa]Yes (where defined) | [icon: times, set=fa]No                    |
| Roles Assignments Groups Organizations | Generic | [icon: check, set=fa]Yes (all)           | [icon: check, set=fa]Yes (all)             |
| Applications                           | Generic | [icon: check, set=fa]Yes (all)           | n/a (customer modifications not supported) |
| Custom                                 | Generic | n/a                                      | [icon: check, set=fa]Yes (all)             |

## Use cases for customizing the identity schema

The following are examples of how you might customize the default schema to support a media service:

* Add a custom property for membership level to user identities to support subscription-level access or rate limiting. For example, the membership levels might be "gold", "silver", and "bronze".

* Add a custom property for registration level to user identities to support access to premium content or to support progressive profiling in journeys. For example, the registration levels might be "guest", "pending", and "registered".

* Adapt a general purpose extension property to be a searchable user property for date of birth to support age-restricted access. Use the property to support delegated administration for different age segments, allowing separate users to administrate adults and children.

* Create organizations to structure user relationships between family members to support parental control.

The following are examples of how you might customize the default schema to support workforce:

* Add custom properties for job code, department number, or cost center to user identities to support the automatic provisioning of birthright roles.

* Add custom properties for external ID and metadata to user identities to support synchronization using System for Cross-domain Identity Management (SCIM).

Learn more about customizing the identity schema in [Customize managed object types](customize-object-types.html).

---

---
title: Advanced sync
description: Configure one-to-many mappings for complex identity synchronization and reconciliation workflows
component: pingoneaic
page_id: pingoneaic:identities:advanced-sync
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/advanced-sync.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities", "Synchronization"]
section_ids:
  advanced-sync-use-cases: Advanced sync use cases
  configure-advanced-sync: Configure advanced sync
---

# Advanced sync

Advanced sync in Advanced Identity Cloud lets you define one or more mappings that control how data flows between application object types and managed object types during reconciliation. Instead of a single "inbound/outbound" mapping, you can create multiple, independent mappings, enabling more complex provisioning and reconciliation use cases.

Each advanced sync mapping controls the following:

* Direction (source versus target)

* Correlation (how records match)

* Attribute mappings (with transforms, conditions, defaults)

* Situation rules (create, update, link, delete, ignore)

* Schedules, event hooks, and advanced performance settings

## Advanced sync use cases

The following table describes common use cases for advanced sync.

| Method                       | Use cases                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Application advanced sync    | * Sync accounts between an application and workforce identities.

  For example, map a Salesforce user to an Alpha realm user, including identifiers, profile data, and entitlements.

* Bridge two applications through Advanced Identity Cloud.

  For example, map Workday workers to ServiceNow users, with Advanced Identity Cloud acting as the central identity platform.

* Extend default app mappings.

  When a catalog application creates a default mapping, use advanced sync to add additional mappings without changing the default.                                                                                                                                                         |
| Managed object advanced sync | - Review all systems that sync a given managed object type.

  For example, open `Alpha realm – User` to view mappings between users and:

  * HR or directory systems

  * SaaS applications (using managed applications)

  * Other realms or environments (user‑to‑user mappings)

- Prepare for schema changes.

  Before you add, rename, or remove properties on a managed object type, use advanced sync to find all mappings that reference that type. Then update correlation rules, mappings, and scripts as needed.

- Handle cross‑realm or cross‑system identity flows.

  For example, map users between two realms, or map organizations between Advanced Identity Cloud and an external CRM. |

## Configure advanced sync

You can access the Advanced Sync editor from either:

* An application, for app‑centric mappings.

  * Go to [icon: apps, set=material, size=inline] Applications > application-name > Provisioning > Advanced Sync.

* An identity object type, for identity‑centric mappings.

  * Go to [icon: people, set=material, size=inline] Configure > managed-object-type > Advanced Sync.

From the Advanced Sync editor you can:

* [Create and manage mappings](advanced-sync-mappings.html)

* [Configure correlation rules](advanced-sync-correlation.html)

* [Run a manual reconciliation](advanced-sync-reconciliation.html)

* [Manage reconciliation schedules](advanced-sync-schedules.html)

* [Define situation rules](advanced-sync-situation-rules.html)

* [Configure event hooks](advanced-sync-event-hooks.html)

* [Configure advanced reconciliation settings](advanced-sync-advanced-reconciliation.html)

---

---
title: Advanced sync for managed object types
description: Manage advanced synchronization mappings from the perspective of managed object types
component: pingoneaic
page_id: pingoneaic:identities:advanced-sync-managed-objects
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/advanced-sync-managed-objects.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities", "Synchronization"]
section_ids:
  advanced-sync-managed-objects: Manage advanced sync
---

# Advanced sync for managed object types

Configuring advanced sync on a managed object type provides an identity-centric view of all the synchronization rules and mappings for the managed object type and every system the object type synchronizes with.

Learn more in [Advanced sync](advanced-sync.html).

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This page focuses on managing advanced sync from a managed object type. The Advanced Sync editor is also available from an application's Provisioning tab. |

## Manage advanced sync

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Configure.

2. On the Managed Object Types page, select the managed object type. For example, select Alpha realm – User.

3. Click the Advanced Sync tab to display all mappings where the selected managed object type is either the source or the target.

4. To manage advanced sync mappings, do one of the following:

   * To create an advanced sync mapping, click [icon: add, set=material, size=inline] Sync Data.

   * To update an advanced sync mapping, click the mapping you want to edit.

   * To delete an advanced sync mapping, click [icon: more_horiz, set=material, size=inline] for the mapping and select Delete.

   Learn more in [Configure advanced sync](advanced-sync.html#configure-advanced-sync).

---

---
title: Bulk import identities
description: Import identity profiles in bulk using a CSV file for rapid onboarding of users and resources
component: pingoneaic
page_id: pingoneaic:identities:bulk-import-identities
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/bulk-import-identities.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Assignments", "Roles", "Identities", "Bulk Import"]
page_aliases: ["pingoneaic::identities-import.adoc"]
section_ids:
  import_identities_in_bulk: Import identities in bulk
  view_or_delete_a_csv_file: View or delete a CSV file
---

# Bulk import identities

You can use a CSV file to bulk import identities into PingOne Advanced Identity Cloud. This is useful when you want to add a large number of identities to a [role](roles-assignments.html#roles) or [assignment](roles-assignments.html#assignments) in a single operation.

## Import identities in bulk

**Before you begin:**\
You'll need a CSV file containing the identity profiles you want to import. The file must comply with this CSV template example:

> **Collapse: CSV template example**
>
> ```
> {
>   "_id": "template",
>   "header": "\"userName\",\"givenName\",\"sn\",\"mail\",\"description\",\"accountStatus\",\"telephoneNumber\",
>  \"postalAddress\",\"address2\",\"city\",\"postalCode\",\"country\",\"stateProvince\",\"preferences/updates\",
>  \"preferences/marketing\""
> }
> ```
>
> Be sure to use commas as separators. Any other separator may cause errors.
>
> Learn more about generating this file in [Import bulk data](../idm-synchronization/import-data.html).

1. In the Advanced Identity Cloud admin console, go to Identities > Import.

2. On the Import Identities page, click + New Import.

3. On the New Import dialog box, select the realm-target you want to import to.

   > **Collapse: Tell me more**
   >
   > The target can be any managed object such as a user, role, or assignment defined within a realm. For example, you could import ten user profiles to the Bravo realm - Roles target. The imported roles are added to the `bravo_role` managed object in Advanced Identity Cloud.

4. Click Next.

5. (Optional) If you haven't already generated a CSV file, click CSV Template. to download an example file.

   |   |                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you use this file:- Replace the attributes in this file with attributes in your identity resource server.

   - Delete all unused attributes. |

6. Enter the name of the CSV file to upload.

7. Choose a property Advanced Identity Cloud can use to match an entry in the CSV file to an identity profile in your realm-target.

   > **Collapse: Tell me more**
   >
   > For example, you could choose the username property. If username `bjensen` exists in your CSV file, Advanced Identity Cloud tries to verify that a user profile with the username `bjensen` also exists in your tenant. If verified, then Advanced Identity Cloud updates the entire `bjensen` user profile. If no match is found, then Advanced Identity Cloud creates a user profile for `bjensen`.

8. Click Next.

   The Import Complete dialog box indicates real-time import progress. When the import is complete, Advanced Identity Cloud displays the number of new, updated, unchanged, and failed imports.

9. (Optional) To download a CSV file containing a list of identity profiles that failed to import, click Download CSV.

10. Click Done.

## View or delete a CSV file

1. In the Advanced Identity Cloud admin console, go to Identities > Import.

2. On the Import Identities list, find the filename.\
   In the same row, click More ([icon: ellipsis-h, set=fa]).

3. Choose View Details or Delete.

---

---
title: Configure advanced reconciliation settings for advanced sync
description: Configure advanced reconciliation filters and performance settings for identity synchronization mappings
component: pingoneaic
page_id: pingoneaic:identities:advanced-sync-advanced-reconciliation
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/advanced-sync-advanced-reconciliation.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities", "Synchronization"]
section_ids:
  advanced-sync-advanced-reconciliation: Configure advanced reconciliation settings
---

# Configure advanced reconciliation settings for advanced sync

In an advanced sync mapping, the Advanced tab exposes additional reconciliation settings that you can use to filter which records are processed and to tune performance. These options are per-mapping and apply whenever reconciliation runs for that mapping (manually or on a schedule).

Use these settings when you need to restrict reconciliation to specific subsets of data, control how links are stored, or adjust how many concurrent threads are used to process reconciliation for large data sets.

## Configure advanced reconciliation settings

To configure advanced reconciliation for a mapping:

1. In the Advanced Identity Cloud admin console, open the [Advanced Sync editor](advanced-sync.html#configure-advanced-sync).

2. In the Advanced Sync editor, open the mapping you want to configure.

3. On the Advanced tab, configure the following optional settings:

   * (Optional) To restrict reconciliation to specific records in a source by defining an explicit source query:

     1. Select the Filter Source checkbox.

     2. Choose to filter the source if Any or All conditions are met.

     3. Use the remaining fields to define the explicit source query using all properties available in the source system.

   * (Optional) To restrict reconciliation to specific records in the target by defining an explicit target query:

     1. Select the Filter Target checkbox.

     2. Choose to filter the target if Any or All conditions are met.

     3. Use the remaining fields to define the explicit target query using all the properties available in the target.

   * (Optional) To filter the records that are included in reconciliation using a script:

     1. Select the Valid Source Script checkbox.

     2. Edit the script.

   * (Optional) To record associations between source or target objects, which allows the UI to show results of the last reconciliation, set Persist Associations to `true`. Learn more in [View a report about the last reconciliation](../app-management/provision-an-application.html#view_a_report_about_the_last_reconciliation).

     |   |                                                                                                                                                                                                           |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | To avoid performance issues for large reconciliation jobs, set Persist Associations to `false`. Learn more in [Reconciliation association details](../idm-synchronization/manage-recon.html#recon-assoc). |

   * (Optional) To filter the target records that are included in reconciliation using a script:

     1. Select the Valid Target Script checkbox.

     2. Edit the script.

   * (Optional) To allow correlation of source objects to empty target objects, select the Correlate empty target objects checkbox.

   * (Optional) To prefetch each link in the database before processing each source or target object, select the Prefetch Links checkbox.

   * (Optional) To allow reconciliations from an empty source to delete all data in a target resource, select the Allow reconciliations from an Empty Source checkbox.

   * (Optional) To tune performance by adjusting the number of concurrent threads dedicated to reconciliation, in the Threads Per Reconciliation field, enter the number of concurrent threads.

     |   |                                                           |
     | - | --------------------------------------------------------- |
     |   | The default number of Threads Per Reconciliation is `10`. |

4. Click Save.

---

---
title: Configure advanced sync correlation
description: Define correlation rules to match source and target objects during identity synchronization reconciliation
component: pingoneaic
page_id: pingoneaic:identities:advanced-sync-correlation
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/advanced-sync-correlation.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities", "Synchronization"]
section_ids:
  advanced-sync-correlation: Configure a correlation query
  advanced-sync-correlation-best-practice: Best practices for designing reliable correlation queries
  example_correlate_by_email: "Example: Correlate by email"
---

# Configure advanced sync correlation

Correlation rules determine how Advanced Identity Cloud matches source objects to existing target objects during reconciliation, so that updates are applied to the correct records and duplicates are avoided. In an advanced sync mapping, you configure a correlation query that looks up potential target matches based on one or more fields.

A well-designed correlation query typically uses a single, unique, and preferably immutable identifier. It directly influences the *situation* that is evaluated for each record, for example, `Found`, `Ambiguous`, or `Absent`.

Learn more in [Correlate source objects with existing target objects](../idm-synchronization/chap-correlation.html).

## Configure a correlation query

To configure a correlation query for a mapping:

1. In the Advanced Identity Cloud admin console, open the [Advanced Sync editor](advanced-sync.html#configure-advanced-sync).

2. In the Advanced Sync editor, open the mapping you want to configure.

3. On the Correlation Query tab, click Configure to open the Edit Correlation modal.

4. Add your correlation query following the suggestions in [Best practices for designing reliable correlation queries](#advanced-sync-correlation-best-practice). You can use the commented out example query as a starting point.

5. Click Save.

   The correlation query is saved with the name Custom.

|   |                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   | After you've saved a correlation query, click the Ellipsis icon ([icon: ellipsis-h, set=fa]) and select Edit to edit the query, if needed. |

## Best practices for designing reliable correlation queries

When matching source and target objects, identify a single, unique, and ideally immutable identifier. Although usernames or emails are common, they can change over time.

* **Prioritize immutable IDs**: Whenever possible, use immutable identifiers that are less likely to change, such as employee IDs or UUIDs. These provide a stable reference for correlation.

* **Case sensitivity**: Make sure that both sides of your query use a consistent case format. For example, if your source `mail` is mixed case but your target `email` is always lowercase, normalize case before comparing. You can use a transformation script to convert both values to lowercase before correlation.

* **Validate for uniqueness**: A correlation query should ideally return exactly one result. If a query returns multiple matches, for example, two users with the same email, Advanced Identity Cloud identified this as an `Ambiguous` situation. Make sure your target system enforces uniqueness on the correlation field (for example, with a unique index) to prevent this.

* **Handle orphaned data carefully**: If a match isn't found, the system might create a new record depending on your situation rules. For sensitive targets, start with `Report` or `No Report` actions so you can audit the results before enabling automatic `Link` or `Create` actions.

* **Optimize performance**: Correlation queries run for every record during reconciliation, so they should be as efficient as possible. Make sure to index the fields used in the correlation query on the target system, and avoid complex transformations or functions that could slow down the query.

### Example: Correlate by email

When correlating accounts, you typically select a unique property to match, such as a username or an email address. For example, in an account-to-user mapping, you can use the email address as the matching criteria. If the target system stores this in a field named `mail` while the source system uses `Email`, you would configure a correlation query to check the target's `mail` field for a value that matches the source's `Email` field. Advanced Identity Cloud then performs the specific action defined in your situation rules based on whether a match is found.

For example, a scripted correlation query might look like this:

```javascript
var qry = {'_queryFilter': 'mail eq "' + source.Email + '"'}; qry
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | All situation rules have the `Async` action by default. A common action for a successful 1:1 match is to link the matched source and target, which means to set the `Found` situation rule with the `Link` action. Learn more in [Advanced sync situation rules](advanced-sync-situation-rules.html#advanced-sync-situation-rules) and in [Advanced sync rule action types](advanced-sync-situation-rules.html#advanced-sync-rule-action-types). |

---

---
title: Configure advanced sync event hooks
description: Execute scripts at specific events during advanced identity synchronization operations
component: pingoneaic
page_id: pingoneaic:identities:advanced-sync-event-hooks
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/advanced-sync-event-hooks.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities", "Synchronization"]
section_ids:
  add-advanced-sync-event-hook: Add an event hook
---

# Configure advanced sync event hooks

Event hooks let you run scripts at specific points in the lifecycle of an advanced sync reconciliation operation, such as when an object is created, updated, deleted, linked, or unlinked. Each event hook is associated with a single mapping and a particular reconciliation event. By configuring event hooks, you can implement additional business logic, data transformations, or integrations with external systems.

## Add an event hook

To add an event hook to a mapping:

1. In the Advanced Identity Cloud admin console, open the [Advanced Sync editor](advanced-sync.html#configure-advanced-sync).

2. In the Advanced Sync editor, open the mapping you want to add an event hook to.

3. Click the Event Hooks tab to view a table of available event hooks by Name and Script.

   |   |                                                              |
   | - | ------------------------------------------------------------ |
   |   | In the Script column, the default state is `Not Configured`. |

   The event hook workflows include: `Update`, `Delete`, `Link`, and `Unlink`.

4. Click an event hook row or click [icon: add, set=material, size=inline] Add on the right of an event hook row to open the Add Event Hook modal.

5. Edit the script for the event hook.

6. Click Save or Save and Close.

---

---
title: Configure advanced sync mappings
description: Create and manage attribute mappings between identity sources and targets during synchronization
component: pingoneaic
page_id: pingoneaic:identities:advanced-sync-mappings
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/advanced-sync-mappings.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities", "Synchronization"]
section_ids:
  create-advanced-sync-mapping: Create an advanced sync mapping
  edit-delete-advanced-sync-mapping: Edit or delete an advanced sync mapping
  define-preview-mapping-rules: Define and preview mapping rules
---

# Configure advanced sync mappings

Use the Advanced Sync editor to create and manage mappings between the current object (application object type, managed object type, or provisioner object type) and other object types. In each mapping, one side is always this current object type. That side can act as either the source or the target for synchronization.

|   |                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | After you create a mapping, you can't change its source, target, or sync direction, but you can edit mapping rules, correlation, situation rules, schedules, event hooks, and advanced settings. |

## Create an advanced sync mapping

1. In the Advanced Identity Cloud admin console, open the [Advanced Sync editor](advanced-sync.html#configure-advanced-sync).

2. On the Advanced Sync tab, click [icon: add, set=material, size=inline] Sync Data.

3. In the Sync account object type modal:

   1. Set your source to Sync From an application object type or managed object type, and choose from the available object types.

   2. Set your target to Sync To an application object type or managed object type, and choose from the available object types.

      |   |                                                                                                                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you created a custom managed object type through the Advanced Identity Cloud admin console, it's available to select in the Object Type list. Learn more in [Create and modify managed object types](manage-object-types.html). |

      By default, the source side is the current object and its object type, for example, the application and object type you opened advanced sync from, or the managed object type you're configuring. You then choose the object or object type to sync to.

      |   |                                                         |
      | - | ------------------------------------------------------- |
      |   | To reverse the sync source and target, click the arrow. |

   3. Select Link Mapping to reuse the links from an existing mapping, so both mappings share the same set of associations instead of creating separate links. This checkbox is available only when a reverse mapping exists.

4. Click Save to add the mapping.

## Edit or delete an advanced sync mapping

To edit or delete an advanced sync mapping:

1. On the Advanced Sync tab, click the Ellipsis icon ( [icon: ellipsis-h, set=fa]) next to the mapping to edit or delete.

2. Do one of the following:

   * To edit the mapping, click Edit. This opens the Mapping page, where you can define the mapping rules, add properties, apply transformation scripts and conditional updates, and configure other advanced settings. Learn more in [Define and preview mapping rules](#define-preview-mapping-rules).

   * To remove a mapping, click Delete and confirm the deletion.

## Define and preview mapping rules

To define mapping rules to reconcile the source with the target, add at least one property to the mapping:

1. On the Mapping tab, click Add a property to open the Add a property modal, then select a target-property-name in the property list.

2. On the next window of the modal, select a source-property-name (optional) in the property list.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | Selecting a source-property-name is optional if you're defining a transformation script or adding a default value. |

3. (Optional) Select the Apply transformation script checkbox. Learn more about transformation scripts in [Apply a transformation script to a mapping](../app-management/provision-an-application.html#apply-a-transformation-script-to-a-mapping).

4. (Optional) Click Show advanced settings and select:

   1. (Optional) Apply conditional update. Learn more about conditional updates in [Apply a conditional update to the mapping](../app-management/provision-an-application.html#apply-a-conditional-update-to-a-mapping).

   2. (Optional) Apply a default if value is `null`. Learn more about how to [Apply a default value to a mapping](../app-management/provision-an-application.html#apply-a-default-value-to-a-mapping).

5. Repeat these steps to map additional properties between the source and the target data stores.

6. Click Save.

   |   |                                                                                                                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the mapping source is a managed object type, click Preview to view an example of how the mapping displays between the source and target. Learn more in [Preview a mapping](../app-management/provision-an-application.html#preview-a-mapping). |

---

---
title: Configure managed objects
description: Create and configure managed object types to represent identity entities in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:identities:configure-object-types
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/configure-object-types.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities"]
section_ids:
  configure-object-types: Key tasks for configuring managed objects
---

# Configure managed objects

In Advanced Identity Cloud, a managed object represents an identity-related entity or resource managed by the platform, such as users, roles, and organizations. You can configure default managed object types or create custom managed object types to model the identities your organization's needs.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The pages in this section describe how to configure managed object types in the Advanced Identity Cloud admin console. You can also configure managed object types in the following ways:- Using REST API calls. Learn more in [Create a managed object type using the REST API](../idm-objects/creating-modifying-managed-objects.html#manage-object-types-rest).

- In the IDM admin console (legacy). Learn more in [Create a managed object type using the IDM admin console](../idm-objects/creating-modifying-managed-objects.html#manage-object-ui). |

## Key tasks for configuring managed objects

Key tasks for configuring managed objects include:

* [Create and modify managed object types](manage-object-types.html)

* [Add and modify properties on managed object types](customize-object-types.html)

* [Configure relationships between managed object types](configure-relationships.html)

* [Configure advanced sync for managed object types](advanced-sync-managed-objects.html)

---

---
title: Configure relationships
description: Define how managed objects relate to each other through one-to-many or many-to-many connections
component: pingoneaic
page_id: pingoneaic:identities:configure-relationships
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/configure-relationships.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities"]
section_ids:
  best-practices-relationships: Best practices for relationships
  plan-relationships: Plan your relationships
  objects_which_managed_objects_need_relating: "Objects: Which managed objects need relating?"
  cardinality_how_many_managed_objects_are_allowed_on_each_side_of_the_relationship: "Cardinality: How many managed objects are allowed on each side of the relationship?"
  direction_is_the_relationship_exposed_on_one_or_both_of_the_managed_objects: "Direction: Is the relationship exposed on one or both of the managed objects?"
  manage-relationships: Manage relationships
  create-custom-relationship: Create a custom relationship
  modify-relationship: Modify a relationship
  delete-relationship: Delete a relationship
  relationship-properties-reference: Relationship property reference
  relationship-settings-reference: Relationship settings reference
---

# Configure relationships

Relationships in Advanced Identity Cloud let you link managed objects to one another. For example, you can connect end users to managers, end users to devices, or organizations to child organizations.

The default Advanced Identity Cloud schema defines several user properties as relationships. For example, the `manager` property on the user managed object type is a relationship that links a user to their manager (who is also a user). This relationship is many-to-one and bidirectional, which means while each user can have only one manager, a single manager can have many direct reports.

> **Collapse: Default relationship properties on the user managed object type**
>
> | Relationship property | Description                                                                                                                                                                                                                                                                                                       |
> | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `manager`             | A many-to-one relationship linking a user to their manager, who is another `managed/user` object.                                                                                                                                                                                                                 |
> | `reports`             | The reverse relationship of `manager`. This is a one-to-many relationship linking a manager to their direct reports (other `managed/user` objects).                                                                                                                                                               |
> | `roles`               | A relationship linking a user to their assigned provisioning and business roles (typically referencing `managed/role` and `internal/role` objects). This is used to drive automated provisioning and access to downstream applications.                                                                           |
> | `authzRoles`          | A relationship linking a user to their authorization roles. While `roles` govern what a user can access in external systems, `authzRoles` determine a user's security context and administrative privileges within Advanced Identity Cloud (for example, granting a user the `internal/role/openidm-admin` role). |
> | `memberOfOrg`         | A relationship linking the user to one or more organizations (`managed/organization`). This is used to build hierarchical tenant or department structures and enforce delegated administration.                                                                                                                   |

You can create your own custom relationship properties. A common use case is to create a custom `device` managed object type and then create a custom relationship property to link end users to the devices they own. This allows you to find all devices assigned to a specific end user, or to identify the owner of a particular device.

|   |                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This page describes how to manage relationships in the Advanced Identity Cloud admin console. Learn about managing custom relationships using the [schema API](../idm-rest-api/endpoints/rest-schema.html). |

## Best practices for relationships

Consider these best practices when managing relationships:

* Plan your relationships carefully before creating them. Consider the use cases you want to support, the cardinality and direction of the relationships, and how they will be used in the UI and API.

* Use clear and consistent naming conventions for relationship properties to make it easy to understand the purpose of each relationship.

* Document the relationships you create, including their purpose, cardinality, and any RDVPs, to ensure that other administrators and developers understand how to use them effectively.

* Regularly review and maintain your relationships to ensure they continue to meet your needs and that any changes to your identity data model are reflected in your relationships.

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Each managed object type is limited to 10 custom relationship properties. If you need more, you must define additional relationships from the related managed object type instead. Learn more in [Create a custom relationship](#create-custom-relationship). |

## Plan your relationships

Consider the following when planning your relationships.

### Objects: Which managed objects need relating?

You can establish relationships between any two managed object types in the system. Common relationship patterns include:

* **User to Manager**: Linking an employee to their supervisor.

* **User to Device**: Assigning a specific piece of hardware to an individual.

* **Organization to Child Organization**: Structuring parent companies and their subsidiaries.

* **Custom relationships**: Building custom parent/child or owner/member hierarchies between any of your custom managed object types.

### Cardinality: How many managed objects are allowed on each side of the relationship?

It can be one of the following:

* **One-to-one**: Each object can be related to at most one corresponding object.

* **One-to-many**: One object can be related to many corresponding objects, but each of those objects can only relate back to the original object.

* **Many-to-one**: Many objects can be related to the same corresponding object, but that object can only relate back to one object on the original side.

* **Many-to-many**: Objects on both sides can be related to multiple corresponding objects.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You choose the cardinality when you create a custom relationship in the Advanced Identity Cloud admin console. You can't change it later through this UI, so it's important to plan this carefully.To change cardinality after creation, you must update the schema directly, or use the legacy IDM admin console, and then clean up any existing data that violates the new cardinality. Learn more in [Update a custom relationship](../idm-objects/relationships-custom.html#update_a_custom_relationship). |

### Direction: Is the relationship exposed on one or both of the managed objects?

Whether the relationship is exposed on one or both of the related objects:

* **One-way**: Only one side exposes the relationship in the schema.

* **Two-way (bidirectional)**: Both sides expose the relationship in the schema. A change to one object in the relationship is automatically reflected on the other. For example, in a bidirectional relationship between a user and a device, if you assign a new device to the user, the user is automatically set as the owner on the corresponding device object.

  |   |                                                                                                                        |
  | - | ---------------------------------------------------------------------------------------------------------------------- |
  |   | You can't create one-way relationships in the Advanced Identity Cloud admin console, but they can exist in the schema. |

## Manage relationships

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Configure.

2. On the Managed Object Types page, select the managed object type. For example, select Alpha realm – User.

3. Click the Relationships tab to display all existing relationships defined for the managed object type.

4. Do one of the following:

   * To [create a custom relationship](#create-custom-relationship), click [icon: add, set=material, size=inline] Relationship.

   * To [modify a relationship](#modify-relationship), click the relationship you want to edit.

   * To [delete a relationship](#delete-relationship), click [icon: more_horiz, set=material, size=inline] for the relationship and select Delete.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you delete a relationship, Advanced Identity Cloud removes its configuration, including the relationship property definitions on the source and related managed object types, and any derived properties created from it.However, when you delete a custom relationship property, Advanced Identity Cloud doesn't automatically remove existing values for that property from your managed objects. You must manually update those objects to remove any leftover data. Otherwise, this orphaned data might unpredictably resurface if you later reuse the same reference attribute for a different relationship or data set. |

### Create a custom relationship

1. On the Relationships tab, click [icon: add, set=material, size=inline] Relationship.

2. In the Create Relationship modal, define the relationship between the managed object types:

   1. In the Object Type list, select the object type to relate to.

   2. Select the relationship's cardinality.

   3. Click Next.

3. On the Relationship Property page, define the [relationship properties](#relationship-properties-reference) *for each side of the relationship*, and click Next.

4. (optional) On the Derived Properties page, define RDVPs on the relationship, and click Next.

   Learn more in [Manage relationship-derived virtual properties (RDVPs)](manage-rdvps.html).

5. Define additional [relationship settings](#relationship-settings-reference).

6. Click Save.

### Modify a relationship

|   |                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't change the cardinality or direction of an existing relationship in the Advanced Identity Cloud admin console. To change these, you must delete the existing relationship and create a new one with the required configuration. |

1. On the Relationships tab, click the relationship you want to modify.

2. Make your changes in the available tabs:

   * Click the Relationship Properties tab to modify [relationship properties](#relationship-properties-reference).

   * Click the Derived Properties tab to modify RDVPs. Learn more in [Manage relationship-derived virtual properties (RDVPs)](manage-rdvps.html).

   * Click the Relationship Settings tab to edit [relationship settings](#relationship-settings-reference).

3. Click Save.

### Delete a relationship

Before deleting a relationship in the UI, remove any existing data that references it. This prevents orphaned relationship data from reappearing later.

1. Identify objects that currently use the relationship:

   1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) created with the `fr:idm:*` scope.

   2. Run a REST API request to query for objects where the relationship property is present:

      > **Collapse: Show request**
      >
      > The following example returns all managed users with the property `reports`:
      >
      > ```
      > $ curl \
      > --header "Authorization: Bearer <access-token>" \ (1)
      > --header "Accept-API-Version: resource=2.0" \
      > --request GET \
      > "https://<tenant-env-fqdn>/openidm/managed/user?_queryFilter=/reports+pr" (2)
      > ```
      >
      > |       |                                                                      |
      > | ----- | -------------------------------------------------------------------- |
      > | **1** | Replace \<access-token> with the access token created in step 1a.    |
      > | **2** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment. |
      >
      > The `pr` operator means "present", so this query finds all users where the custom property has a value.

2. Update or remove the data on the existing objects so they no longer reference the relationship.

3. Run a reconciliation to ensure the data is cleaned up across the system.

4. On the Relationships tab, click [icon: more_horiz, set=material, size=inline] for the relationship you want to delete, and select [icon: delete, set=material, size=inline] Delete.

5. Click Delete to confirm the deletion.

### Relationship property reference

Use the following settings in the Relationship Property page to configure a relationship:

| Field, option                 | Description                                                                                                                                                                                                                                                                                  |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property Name                 | A name for the relationship property. For example, a relationship between users and devices might be named `assignedDevices` on the user side and `deviceOwner` on the device side.                                                                                                          |
| Label (optional)              | An optional human-readable name for the relationship that appears in the UI.                                                                                                                                                                                                                 |
| Description (optional)        | An optional description for the relationship.                                                                                                                                                                                                                                                |
| Display Properties (optional) | Properties to display in the Advanced Identity Cloud admin console when viewing related objects. For example, you might select `userName` and `email` for a relationship to users, and `deviceName` for a relationship to devices.                                                           |
| Notify                        | Select this checkbox if related managed objects should be notified on modification of the property value.This is typically used for relationships where the related objects have RDVPs that must stay in sync with changes to the relationship.                                              |
| Notify Self                   | Select this checkbox if the managed object type that owns the relationship should be notified on modification.This is typically used for self-referential relationships, such as a user-to-manager relationship where both sides of the relationship reference the same managed object type. |

### Relationship settings reference

Use the following settings in the Relationship Settings page to configure the source relationship property of the relationship:

| Field, option                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Validate Relationship              | Specifies that a relationship between two object types must be validated when the relationship is created. For example, to indicate that a user can't reference a role if that role doesn't exist.When you create a new custom relationship, validation is disabled by default as it involves an expensive query to the relationship that isn't always required.Learn more in [Validate relationships between objects](../idm-objects/relationships-validation.html). |
| Relationship Properties (optional) | Specifies properties on the relationship itself. It configures the `properties._refProperties.properties` on the schema.Use the [icon: add, set=material, size=inline] button to add properties to the relationship, and then define the property name and label for each property.                                                                                                                                                                                   |

---

---
title: Configure scheduled jobs
description: Schedule automated jobs and scanning tasks that execute scripts on identity data
component: pingoneaic
page_id: pingoneaic:identities:manage-scheduled-jobs
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/manage-scheduled-jobs.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  schedule_a_job: Schedule a job
  schedule_a_scanning_task: Schedule a scanning task
  manage_jobs: Manage jobs
---

# Configure scheduled jobs

PingOne Advanced Identity Cloud lets you view, schedule, and manage scheduled jobs and scanning tasks using the Jobs page. You can use jobs to run scripts or reconciliation. You can use scanning tasks to query objects and run a script on the results. Learn more about scripts in [Scripting](../idm-scripting/preface.html).

Although application reconciliation jobs display in the list, you must create and edit them from the [application provisioning settings](../app-management/provision-an-application.html#app-mgmt-manage-recon-schedules).

## Schedule a job

1. In the Advanced Identity Cloud admin console, click [icon: event_available, set=material, size=inline] Jobs.

2. Click [icon: add, set=material, size=inline] Schedule a Job.

3. In the Schedule a Job window, select Script, and click Next.

4. On the Script Job Details page, enter a name for the job in the Job Name field.

5. To configure the job frequency, do one of the following:

   * To use `cron`, enable Use cron, and enter a valid `cron` string in the Frequency field.

     |   |                                                                                                                                                                            |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | To validate a `cron` schedule expression, learn more in [Validate cron trigger expressions](../idm-schedules/configure-dynamic-schedules.html#validating-schedule-syntax). |

   * In the Frequency area, set the applicable fields and options:

     | Field, drop-down, option | Description                                                                                                                                                                 |
     | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | Run Every                | The schedule run frequency.                                                                                                                                                 |
     | value                    | The time period for the adjacent Run every field:- day(s)

     - hour(s)

     - week(s)

     - month(s)                                                                                 |
     | Set a Start Time         | A start time for the first job run. Selecting this option displays the following additional fields:- Date picker

     - Time picker

     - Timezone                                 |
     | Repeat                   | How the job repeats:- X Times

     - Until specific date	If you do not set either value, Advanced Identity Cloud saves the schedule with a Times value of -1 (infinite repeat). |

6. To configure variables, in the Script area, click [icon: add, set=material, size=inline] Variables, and do one of the following:

   * For each variable, enter a Name and Value, and click [icon: add, set=material, size=inline].

   * To specify the variables in JSON format, enable JSON, and enter your JSON data in the PASSED VARIABLES field.

7. In the Script field, enter your script. For example:

   ```javascript
   java.lang.System.out.println('Job executing on ' + identityServer.getProperty('openidm.node.id') + ' at: ' + java.lang.System.currentTimeMillis());
   ```

   Learn more about scripts in [Scripting](../idm-scripting/preface.html).

8. Click Save.

## Schedule a scanning task

Perform the following steps to scan a set of properties with a query filter at a scheduled interval, and execute a script on the objects returned by the query.

1. In the Advanced Identity Cloud admin console, click [icon: event_available, set=material, size=inline] Jobs.

2. Click [icon: add, set=material, size=inline] Schedule a Job.

3. In the Schedule a Job window, select Task Scanner, and click Next.

4. In the Choose Entity to Scan window, from the Entity to Scan drop-down list, select an entity to scan at a scheduled interval. The default options are:

   * realm-name - User

   * realm-name - Role

   * realm-name - Group

   * realm-name - Organization

   * realm-name - Application

5. Click Next.

6. On the Task Scanner Job Details page, enter a name for the job in the Job Name field.

7. To configure the job frequency, do one of the following:

   * To use `cron`, enable Use cron, and enter a valid `cron` string in the Frequency field.

     |   |                                                                                                                                                                            |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | To validate a `cron` schedule expression, learn more in [Validate cron trigger expressions](../idm-schedules/configure-dynamic-schedules.html#validating-schedule-syntax). |

   * In the Frequency area, set the applicable fields and options:

     | Field, drop-down, option | Description                                                                                                                                                                 |
     | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | Run Every                | The schedule run frequency.                                                                                                                                                 |
     | value                    | The time period for the adjacent Run every field:- day(s)

     - hour(s)

     - week(s)

     - month(s)                                                                                 |
     | Set a Start Time         | A start time for the first job run. Selecting this option displays the following additional fields:- Date picker

     - Time picker

     - Timezone                                 |
     | Repeat                   | How the job repeats:- X Times

     - Until specific date	If you do not set either value, Advanced Identity Cloud saves the schedule with a Times value of -1 (infinite repeat). |

8. To limit the task to a subset of entities, select Filter realm-name - Entity, and do one of the following:

   * Use the basic editor to create the query conditions.

     > **Collapse: Show Me**
     >
     > ![Task Scanner filter for entities](_images/ui-jobs-filter.png)

   * Click Advanced Editor to enter the query code. For example:

     ```javascript
     (/city co "Vancouver" and /accountStatus co "active")
     ```

9. Complete the fields in the Task State area:

   * Started

     Specifies the field that stores the timestamp for when the task begins.

   * Completed

     Specifies the field that stores the timestamp for when the task completes its operation. The `completed` field is present as soon as the task has started, but its value is `null` until the task has completed.

   |   |                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The *Task State* indicates the names of the fields in which the start message and completed message are stored. These fields are used to track the status of the task. |

10. To configure variables, in the Script area, click [icon: add, set=material, size=inline] Variables, and do one of the following:

    * For each variable, enter a Name and Value, and click +.

    * To specify the variables in JSON format, enable JSON, and enter your JSON data in the PASSED VARIABLES field.

11. In the Script field, enter your script. For example:

    ```javascript
    java.lang.System.out.println('Job executing on ' + identityServer.getProperty('openidm.node.id') + ' at: ' + java.lang.System.currentTimeMillis());
    ```

    Learn more about scripts in [Scripting](../idm-scripting/preface.html).

12. Click Save.

## Manage jobs

1. In the Advanced Identity Cloud admin console, click [icon: event_available, set=material, size=inline] Jobs.

   The Jobs page displays a list of jobs, the next scheduled run, and the status.

   > **Collapse: Show Me**
   >
   > ![Jobs page](_images/ui-jobs-page.png)

2. To filter job types, click the View drop-down list and select a job type. For example, Task Scanner.

3. To search for jobs by name, enter text in the Search field, and press `Enter`.

4. To view details about a job, click the More ([icon: ellipsis-h, set=fa]) menu adjacent to a job, and click View Details.

5. To edit a job, click it from the jobs list.

6. To manually trigger a job, click the More ([icon: ellipsis-h, set=fa]) menu adjacent to a job, and click Run Now.

   * In the Run Scheduled Job window, click Run Job.

7. To deactivate a job, click the More ([icon: ellipsis-h, set=fa]) menu adjacent to a job, and click Deactivate.

8. To activate a job, click the More ([icon: ellipsis-h, set=fa]) menu adjacent to a job, and click Activate.

9. To delete a job, click the More ([icon: ellipsis-h, set=fa]) menu adjacent to a job, and click Delete.

   * In the Delete Scheduled Job? window, click Delete.

---

---
title: Constrain identity queries
description: Optimize performance by requiring minimum search strings and restricting query capabilities
component: pingoneaic
page_id: pingoneaic:identities:constrain-identity-queries
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/constrain-identity-queries.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Query Performance", "User Interface"]
page_aliases: ["pingoneaic::identities-configure.adoc", "configure-ui.adoc"]
section_ids:
  require-a-minimum-length-search-string: Require a minimum length search string
  forbid-sorting-or-searching-resource-collections: Forbid sorting or searching resource collections
---

# Constrain identity queries

You can constrain queries in two ways when [managing identities](manage-identities.html) with the Advanced Identity Cloud admin console:

* By requiring all Advanced Identity Cloud admin console users to [provide a minimum number of characters when searching](#require-a-minimum-length-search-string) for identities.

* By [forbidding delegated administrators from sorting and searching resource collections](#forbid-sorting-or-searching-resource-collections).

Constraining how the Advanced Identity Cloud admin console can be used can improve overall Advanced Identity Cloud performance because the constraints forbid queries that might inadvertently use a large amount of computing resources.

|   |                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you encounter slow or failed searches when searching for users in the IDM admin UI, learn more in [Searching for users in the UI is very slow in Advanced Identity Cloud](https://support.pingidentity.com/s/article/Searching-for-users-is-very-slow-in-Advanced-Identity-Cloud). |

## Require a minimum length search string

You can require Advanced Identity Cloud administrators to enter a minimum length string when querying identities using the Advanced Identity Cloud admin console. This setting also disables sorting search results unless a minimum length string has been specified in the search box.

Applying this setting can speed up the time it takes to retrieve records from large identity data sets.

This setting only affects queries performed in the Advanced Identity Cloud admin console. It does not affect Advanced Identity Cloud REST API queries.

To apply the setting:

1. In the Advanced Identity Cloud admin console, go to Identities > Configure.

2. Click on an object type. For example, if you want to configure the UI for managing identities in the Alpha realm, click Alpha realm - User.

3. On the Details tab, click Show advanced settings.

4. Select the Require UI Search Filter checkbox.

5. Enter a number greater than zero in the Minimum Characters field.

6. Click Save.

To verify that the setting is in effect:

1. Go to Identities > Manage.

2. Select the object type that corresponds to the one you configured when you applied the setting.

3. Click one of the column titles at the top of the search results to attempt to sort the results.

   You shouldn't be able to sort the results. Sorting by column should have been disabled.

4. Specify a string in the Search field that has fewer characters than the minimum number of characters you specified in the object type's configuration, then press `enter`.

   The search operation shouldn't be permitted.

5. Specify a string in the Search field that has the minimum number of characters you specified in the object type's configuration, then press `enter`.

   The search operation should be permitted.

6. Click one of the column titles at the top of the search results to sort the results.

   Sorting the search results should now be permitted.

## Forbid sorting or searching resource collections

A *resource collection* is a set of identities that has a relationship with another identity. For example:

* All the users with a particular role assignment

* All the users who are members of an organization

You can forbid Advanced Identity Cloud [delegated administrators](../realms/alpha-bravo-realms.html#delegated_administration) from sorting resource collections and performing searches within resource collections in the Advanced Identity Cloud admin console.

This setting only affects delegated administrators using the hosted account pages. It doesn't affect tenant administrators using the Advanced Identity Cloud admin console.

To apply the setting:

1. In the Advanced Identity Cloud admin console, go to Identities > Configure.

2. Click on an object type. For example, if you want to configure the UI for managing identities in the Alpha realm, click Alpha realm - User.

3. On the Details tab, click Show advanced settings.

4. Select the Require UI Search Filter checkbox.

5. Select the Disable sorting and searching on grids that use this object as a resource collection checkbox.

6. Click Save.

To verify that the setting is in effect:

1. Sign off from Advanced Identity Cloud.

2. Sign on to Advanced Identity Cloud as a [delegated administrator](../realms/alpha-bravo-realms.html#delegated_administration).

3. Select an object type that has a relationship with the object type you configured when you applied the setting.

   For example, if you disabled sorting and search for Alpha realm - User grids, then you could select Alpha realm - organization because organizations have members (which are users).

4. Find the name of an organization for which you're the delegated administrator.

5. Click its More ([icon: ellipsis-h, set=fa]) menu, and choose Edit.

6. Click Members to bring up the collection of users that are members of your organization.

7. Click First Name to attempt to sort the identities by first name.

   Sorting the search results should not be permitted.

---

---
title: Create and modify managed object types
description: Create, modify, and delete managed object types to represent custom identity entities
component: pingoneaic
page_id: pingoneaic:identities:manage-object-types
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/manage-object-types.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities"]
section_ids:
  create-custom-object-type: Create a custom managed object type
  modify-object-type: Modify a managed object type
  delete-object-type: Delete a managed object type
  configure-object-settings: Managed object type settings reference
---

# Create and modify managed object types

In Advanced Identity Cloud, you can create, modify, and delete managed object types to meet your organization's needs. You can modify default managed object types (such as users, roles, and groups) and create new custom managed object types to represent additional identity types for your organization, such as devices.

|   |                                                                 |
| - | --------------------------------------------------------------- |
|   | Modifying **application** managed object types isn't supported. |

Learn more about the identity schema in [Advanced Identity Cloud identity schema](identity-cloud-identity-schema.html).

## Create a custom managed object type

To create a custom managed object type:

1. In the Advanced Identity Cloud admin console, switch to the realm where you want to configure the object type.

2. Go to [icon: people, set=material, size=inline] Identities > Configure.

3. On the Configure Identities page, click [icon: add, set=material, size=inline] Managed Object Type.

4. Enter a name and display name for the managed object type, and enter optional details, as needed.

   The name can only include the characters `a-z`, `A-Z`, and `0-9`. The display name specifies what the object type will be called in the object type's UI label.

5. Click Save Profile.

   The new managed object type is created, and its configuration page opens.

6. Use the tabs to configure object type settings and schema. Learn more in [Managed object type settings reference](#configure-object-settings).

## Modify a managed object type

|                 | Users                    | Roles, assignments, groups, organizations | Applications            | Custom                   |
| --------------- | ------------------------ | ----------------------------------------- | ----------------------- | ------------------------ |
| Action allowed? | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes                  | [icon: times, set=fa]No | [icon: check, set=fa]Yes |

To modify a managed object type:

1. In the Advanced Identity Cloud admin console, switch to the realm where you want to configure the managed object type.

2. Go to [icon: people, set=material, size=inline] Identities > Configure.

3. On the Managed Object Types page, click the managed object type you want to modify to open its configuration page.

4. Use the tabs to modify managed object type settings and schema. Learn more in [Managed object type settings reference](#configure-object-settings).

## Delete a managed object type

|                 | Users                   | Roles, assignments, groups, organizations | Applications            | Custom                   |
| --------------- | ----------------------- | ----------------------------------------- | ----------------------- | ------------------------ |
| Action allowed? | [icon: times, set=fa]No | [icon: times, set=fa]No                   | [icon: times, set=fa]No | [icon: check, set=fa]Yes |

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | When you delete a custom managed object type, all identity data associated with it is permanently deleted and can't be recovered. |

To delete a custom managed object type:

1. In the Advanced Identity Cloud admin console, switch to the realm where you want to configure the managed object type.

2. Go to [icon: people, set=material, size=inline] Identities > Configure.

3. On the Managed Object Types page, click [icon: more_horiz, set=material, size=inline] for the managed object type you want to delete and select [icon: delete, set=material, size=inline] Delete.

4. Click Delete to confirm the deletion.

## Managed object type settings reference

Use the following tabs to configure settings for the managed object type in the Advanced Identity Cloud admin console.

* Details

  Use this tab to specify basic details about the managed object type, such as its display name and icon.

  Click Show advanced settings to constrain identity queries. Learn more in [Constrain identity queries](constrain-identity-queries.html).

* Properties

  Use this tab to add, modify, and delete properties for the managed object type.

  Learn more in [Customize managed object types](customize-object-types.html).

* Relationships

  Use this tab to specify relationships for the managed object type. For example, to connect end users to managers, end users to devices, or organizations to child organizations.

Learn more in [Configure relationships](configure-relationships.html).

* Advanced Sync

  Use this tab to configure synchronization settings for that managed object type, such as synchronizing objects of that type to an external system and mapping their properties.

Learn more in [Advanced sync for managed object types](advanced-sync-managed-objects.html).

---

---
title: Customize managed object types
description: Add custom properties and extension attributes to store organization-specific identity data
component: pingoneaic
page_id: pingoneaic:identities:customize-object-types
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/customize-object-types.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities"]
section_ids:
  customize-user-object-types: Customize user managed object types
  use-general-purpose-extension-attributes: Manage general purpose extension properties
  customize-extension-property: Customize an extension property
  customize-nonuser-object-types: Customize role, assignment, group, and organization managed object types
  customize-custom-object-types: Customize custom managed object types
  manage-custom-properties: Manage custom properties
  create-custom-properties: Create a custom property
  modify-custom-properties: Modify a custom property
  delete-custom-properties: Delete a custom property
  property-settings-reference: Property settings reference
  access-user-identity-custom-properties: Access user identity custom properties in scripts
---

# Customize managed object types

You can customize Advanced Identity Cloud managed object types to suit your organization's needs. This allows you to store additional information, such as a user's department, a role's associated cost center, or a device's operating system, directly on the relevant managed object types.

The Advanced Identity Cloud schema includes several managed object types that you can customize:

* **User**: The default managed object type for end users, which includes common properties such as name, email, and phone number.

* **Roles, assignments, groups, and organizations**: Default managed object types used to manage access and organizational structure.

* **Custom**: Any managed object type you create to represent unique entities in your organization, such as devices.

|   |                                                                                            |
| - | ------------------------------------------------------------------------------------------ |
|   | Advanced Identity Cloud does not support the modification of **application** object types. |

Learn more about the Advanced Identity Cloud identity schema in [Advanced Identity Cloud identity schema](identity-cloud-identity-schema.html).

## Customize user managed object types

You can customize user managed object types by either adding *custom properties* or using existing *general purpose extension properties*. This lets you store additional profile data such as department, cost center, application preferences, and device lists.

* Custom properties

  Use custom properties when you need flexible, non-searchable data for journeys and scripts.

  These properties are stored in an unindexed JSON data structure, so they aren't searchable. However, you can [access them in your scripts](#access-user-identity-custom-properties) and use them to make dynamic decisions in your journeys.

  Learn how to [manage custom properties](#manage-custom-properties).

* General purpose extension properties

  Use general purpose extension properties when the data must be searchable or filterable.

  These are predefined properties that are part of the default user identity schema. Some of these properties are indexed, so you can search and filter on them.

  Learn how to [manage general purpose extension properties](#use-general-purpose-extension-attributes).

|   |                                                                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud doesn't support searching on user identity custom properties, which can sometimes render an environment unresponsive. Instead, if you need to make a particular user identity property searchable, use an indexed extension property. Learn more in [Manage general purpose extension properties](#use-general-purpose-extension-attributes). |

### Manage general purpose extension properties

You can use the general purpose extension properties that already exist on user identities. These properties are predefined as part of the default identity schema. The following extension properties are indexed, so you can use them as searchable properties:

* Generic Indexed String 1–20

* Generic Indexed Multivalue 1–5

* Generic Indexed Date 1–5

* Generic Indexed Integer 1–5

#### Customize an extension property

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can only change the display label of an extension property. You can't change its underlying data type (for example, from `String` to `Integer`). |

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Configure.

2. Click the managed object type, for example, Alpha realm - User or Bravo realm - User.

3. Click Properties in the left menu pane.

4. Find an extension property that has one of the following default labels:

   * Generic Indexed String 1–20 or Generic Unindexed String 1–5, 6–20\[[1](#_footnotedef_1 "View footnote.")]

   * Generic Indexed Multivalue 1–5 or Generic Multivalue String 1–5

   * Generic Indexed Date 1–5 or Generic Date String 1–5

   * Generic Indexed Integer 1–5 or Generic Integer String 1–5

     |   |                                                                                               |
     | - | --------------------------------------------------------------------------------------------- |
     |   | If you need to make the property searchable, make sure you use an indexed extension property. |

5. Click on the property to edit it.

6. In the Display Label (optional) field, enter a custom label. For example, `Department`.

7. Click Save.

## Customize role, assignment, group, and organization managed object types

You can customize role, assignment, group, and organization managed object types by adding properties to their default schema. This lets you store more useful information about each identity such as a description of a role or group, or the cost center for an organization.

|   |                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Any custom property you add to a role, assignment, group, or organization is automatically indexed and searchable. Because of this automatic indexing, it's recommended that you add no more than 12 custom properties each to each of these object types. Adding too many indexed properties can negatively impact the performance of your tenant environments. |

Learn how to [manage custom properties](#manage-custom-properties).

## Customize custom managed object types

You can add properties to any custom managed object types you've created. This lets you store useful information about each identity, such as the device type and operating system for a custom managed object type that represents devices.

Learn how to [manage custom properties](#manage-custom-properties).

## Manage custom properties

You can create and modify custom properties directly on the managed object types to store additional information about the object.

### Create a custom property

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Configure.

   The console displays the list of managed object types in the current realm.

2. Click the managed object type, for example, Alpha realm - User or Bravo realm - User.

3. Click the Properties tab and click [icon: add, set=material, size=inline] Add a Property.

4. Select the property type and click Next.

5. Enter the following details in the New *\[type]* Property modal:

   1. In the Property Key field, enter a unique identifier for the property. The property key can only include alphanumeric characters and underscores.

      For user managed object types, all custom properties are automatically prefixed with `custom_`. For example, if you enter `department` as the property key, the full property name will be `custom_department`.

   2. Complete the optional settings for the new property.

   3. Select the Multi-valued checkbox if the property holds multiple values. This is applicable only to `String`, `Number`, and `Object` property types.

   4. Select the Required checkbox if the property is required.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Required policy is enforced only when an identity is created, not when it is updated. This means you can bypass the policy by updating the identity and setting the property to an empty value. To prevent this, select Required in the admin console and add a `not-empty` policy for the same property using the REST API. Learn more in [Apply policies to managed objects](../idm-objects/configuring-default-policy.html). |

1. Do one of the following:

   * Click Save to save the property with default settings.

   * Click Switch to advanced setup to configure additional property settings in a wizard.

   * If you're creating an `Object` type property, click Next to define nested properties.

2. Complete the additional property settings as necessary, and click Save when you're done.

Learn more about configuring property settings in [Property settings reference](#property-settings-reference).

### Modify a custom property

|   |                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you modify a managed object type, review any existing objects of that type to ensure that they're still valid. For example, if you make a property required, make sure that all existing objects of that type have a value for that property. |

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Configure.

2. Click the managed object type that contains the property you want to modify.

3. In the left menu pane, click Properties.

4. Locate and click the property you want to edit.

5. Update the [property settings](#property-settings-reference) and click Save.

### Delete a custom property

|   |                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you don't delete all data stored in the custom property before deleting the property, you might see errors when running subsequent reconciliations. |

To delete a user identity custom property:

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) created with the `fr:idm:*` scope.

2. Delete all data stored in the custom property for all users that have data in the property:

   1. Find all users with data stored in the custom property:

      > **Collapse: Show request**
      >
      > ```none
      > $ curl -G \
      > --request GET 'https://<tenant-env-fqdn>/openidm/managed/alpha_user' \(1)
      > --header 'Content-Type: application/json' \
      > --header 'Accept-API-Version: resource=1.0' \
      > --header 'Authorization: Bearer <access-token>' \(2)
      > --data-urlencode '_fields=userName,givenName,sn,mail,accountStatus,<custom-property>' \(3)
      > --data-urlencode '_queryFilter=<custom-property> pr'(3)
      > ```
      >
      > |       |                                                                                                                                                                                                             |
      > | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                        |
      > | **2** | Replace \<access-token> with the access token created in step 1.                                                                                                                                            |
      > | **3** | Replace \<custom-property> with the name of the custom property (for example, `custom_department`). The `pr` operator means "present", so this query finds all users where the custom property has a value. |

      > **Collapse: Example response**
      >
      > ```json
      > {
      >   "result": [
      >     {
      >       "_id": "ce3c42e2-6f9c-4451-8590-9ee40fad3f83",
      >       "_rev": "2c83eb63-7445-4aa6-a585-1c7dbe58b3a8-29020",
      >       "custom_department": "Accounts",
      >       "givenName": "Barbara",
      >       "accountStatus": "active",
      >       "sn": "Jensen",
      >       "mail": "babs.jensen@example.com",
      >       "userName": "bjensen"
      >     }
      >   ],
      >   "resultCount": 1,
      >   "pagedResultsCookie": null,
      >   "totalPagedResultsPolicy": "NONE",
      >   "totalPagedResults": -1,
      >   "remainingPagedResults": -1
      > }
      > ```

   2. For each user you found in the previous step, delete the data stored in the custom property:

      > **Collapse: Show request**
      >
      > ```none
      > $ curl \
      > --request PATCH 'https://<tenant-env-fqdn>/openidm/managed/alpha_user/<user-id>' \(1)(2)
      > --header 'Content-Type: application/json' \
      > --header 'Accept-API-Version: resource=1.0' \
      > --header 'Authorization: Bearer ' \(3)
      > --data '[
      >   {
      >     "operation":"remove",
      >     "field":"/<custom-property>"(4)
      >   }
      > ]'
      > ```
      >
      > |       |                                                                                                                             |
      > | ----- | --------------------------------------------------------------------------------------------------------------------------- |
      > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                        |
      > | **2** | Replace \<user-id> with the ID of the user identity; for example, `ce3c42e2-6f9c-4451-8590-9ee40fad3f83`.                   |
      > | **3** | Replace \<access-token> with the access token created in step 1.                                                            |
      > | **4** | Replace \<custom-property> with the name of the custom property (for example, `custom_department`) to delete from the user. |

      The response should show the updated user with the custom property removed.

3. Run a full reconciliation.

4. Remove the custom property from the schema:

   1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Configure.

   2. Click the managed object type that contains the property you want to delete.

   3. Click Properties in the left menu pane.

   4. Locate the property you want to delete, click [icon: more_horiz, set=material, size=inline] and select [icon: delete, set=material, size=inline] Delete.

   5. Click Delete to confirm the deletion.

### Property settings reference

Use the following tabs to configure settings for a managed object type's property.

> **Collapse: Details**
>
> Enter the basic details for the property such as its display label and description. You can also set the Property Format; be aware that changing this value clears any existing validation rules.
>
> Select the Required checkbox if a property value is required. This setting also causes it to appear as a field in the UI when you create a new object of that type.
>
> |   |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | The Required policy is enforced only when an identity is created, not when it's updated. This means you can bypass the policy by updating the identity and setting the property to an empty value. To prevent this, select Required in the admin console and add a `not-empty` policy for the same property using the REST API. Learn more in [Apply policies to managed objects](../idm-objects/configuring-default-policy.html). |

> **Collapse: Property Value**
>
> Choose how the value is set for the property:
>
> * Manually: The value is set by the user when creating or updating an identity.
>
>   Select the Enumerate allowable values for this property checkbox to add enumerated values for the property. End users can select from these when setting the value for the property. Enumerated values aren't applicable to `Boolean` and `Object` property types.
>
>   |   |                                                                                                                                                                                                                                                                                                                                                         |
>   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | When you create enumerated values for a property, their display labels are automatically added to your tenant's translation and locale configuration files. If you later update these translation files, you must ensure that these auto-generated enum labels aren't removed. Removing them will break the display of the enumerated values in the UI. |
>
> * Script: The value is automatically set by a script when creating or updating an identity. If you select this option, you must provide the script that sets the value.
>
>   The Return by Default checkbox controls whether a virtual property is included in query results when it isn't explicitly requested. Select this option for most virtual properties and relationship-derived virtual properties (RDVPs), so their values are available in typical reads and searches. Leave unselected only when the data is large, internal-only, or when working with arrays of relationships that are subject to validation policies.
>
> * Relationship: Use this to make the property a virtual property whose value is derived from related objects, using one or more existing relationship properties. These are called RDVPs and are distinct from the relationship properties themselves, which you configure on the Relationships tab.
>
>   * In the Source(s) section, click [icon: add, set=material, size=inline] Add Source to specify the relationship properties that the property value will be derived from. For any single RDVP, all sources must start on the same managed object type (the one that owns the property), and end on the same target managed object type. For example, `Applications I Own` (User → Application), then `Members` (Application → User). This example starts and ends with the User managed object type.
>
>   * In the Referenced Object Properties section, select the properties on the related object to include in the value of this property. Select either:
>
>     * Full Object. The RDVP stores each target as a full JSON object, with `_id`, `_rev`, and all other fields.
>
>     * Select Properties The RDVP stores only the fields you select from each target object.
>
>   * Select Flatten properties, if you want a simple, query-friendly value instead of full object references. For example, a simple array such as `["manager1@example.com", "manager2@example.com"]` instead of an array of objects.
>
>   * Select Return By Default to include the RDVP in query results when it isn't explicitly requested.
>
>   Learn more about RDVPs and relationships in [Relationships](../planning/plan-object-modeling-relationships.html).
>
> Advanced options:
>
> * Select Default Value to provide a default value for the property.
>
> * Select Nullable to allow a null value. For example, if you have a property for `telephoneNumber`, you can set it to null for users who don't have a telephone number.

> **Collapse: Properties (Object properties only)**
>
> Define the array of properties for the object property.
>
> This allows you to group related fields (for example, a `postalAddress` object that contains `street`, `city`, `postalCode`) instead of flattening them all as top-level properties.

> **Collapse: Display**
>
> Choose how the property is displayed in the admin console and the end user's journey and account pages.

> **Collapse: Validation**
>
> Advanced Identity Cloud provides a policy service that lets you apply specific validation requirements to managed object types. Learn more in [Use policies to validate data](../idm-objects/policies.html) and [Policy reference](../idm-objects/configuring-default-policy.html#policy-reference).

> **Collapse: Privacy & Encryption**
>
> Some managed object types contain data that you want to secure, such as credit card numbers and passwords.
>
> Choose how to secure the property to protect sensitive data:
>
> * Select Private to prevent the property value being accessed over REST.
>
> * Select Encode to protect the property value with either reversible encryption or non-reversible salted hashing.
>
> Learn more about [securing identity data](../idm-security/secure-sensitive-data.html).

## Access user identity custom properties in scripts

|   |                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Legacy decision node scripts remain supported, but new development should use next-generation scripting. To access the latest bindings (for example, `nodeState`, `httpClient`, and updated utils), migrate your Scripted Decision node to a next-generation script. Learn more in [Migrate decision node scripts to next-generation scripts](../am-scripting/scripting-api-node-migrate.html). |

To access a user identity custom property called `custom_department` in a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html):

1. Configure the [Identity Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identity-store-decision.html):

   1. Make sure the Identity Store Decision node is placed before the Scripted Decision node in your journey.

   2. Select the Username as Universal Identifier checkbox in the Identity Store Decision node's configuration. This ensures that the user's UUID is stored in the `username` node state variable.

2. Edit the script used by the Scripted Decision node:

   * To access the custom property using access management script functions, use the property `fr-idm-custom-attrs`. This contains a JSON object of all custom properties, so it needs to be parsed to access individual properties.

     ```javascript
     var uuid = nodeState.get('username');
     var customAttrsRaw = idRepository.getIdentity(uuid).getAttributeValues('fr-idm-custom-attrs')[0];
     var customAttrs = JSON.parse(customAttrsRaw);
     var department = customAttrs.custom_department;
     ```

     Learn more in [Access profile data](../am-scripting/scripting-api-node.html#scripting-api-node-id-repo).

   * To access the custom property using identity management script functions, use the specific property name `custom_department`.

     ```javascript
     var uuid = nodeState.get('username');
     var userAttrs = openidm.read('managed/alpha_user/' + uuid, null, ['custom_department']);
     var department = userAttrs.custom_department;
     ```

     Learn more in [Access IDM scripting functions](../am-scripting/script-bindings.html#common-openidm).

***

[1](#_footnoteref_1). Additional indexed string attributes are enabled by default in tenants created on or after November 12, 2024. Learn how to enable them in tenants created before that date in [Additional indexed string attributes](../idm-rest-api/endpoints/rest-feature.html#feature-enable-indexed-string-attributes).

---

---
title: Define advanced sync situation rules
description: Define actions to take when identity reconciliation encounters specific source-to-target match situations
component: pingoneaic
page_id: pingoneaic:identities:advanced-sync-situation-rules
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/advanced-sync-situation-rules.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities", "Synchronization"]
section_ids:
  view-edit-situation-rules: View and edit situation rules
  advanced-sync-situation-rules: Advanced sync situation rules
  advanced-sync-rule-action-types: Advanced sync rule action types
---

# Define advanced sync situation rules

Situation rules control what Advanced Identity Cloud does for each record during reconciliation, based on how the source object relates to the corresponding target object.

For every advanced sync mapping, Advanced Identity Cloud:

* Evaluates the correlation query for each source object.

* Classifies the result into a **situation** (for example, `Found`, `Ambiguous`, `Absent`).

* Performs the **action** you've configured for that situation (for example, `Create`, `Update`, `Link`, `Delete`, `Ignore`) on the target system.

All situation rules default to the `Async` action until you change them.

## View and edit situation rules

To configure situation rules for a mapping:

1. In the Advanced Identity Cloud admin console, open the [Advanced Sync editor](advanced-sync.html#configure-advanced-sync).

2. In the Advanced Sync editor, open the mapping you want to configure.

3. Click the Situation Rules tab to display the Situation and Action that define rules for various sync situations.

4. Click the Situation rule to edit or click the ellipsis icon ([icon: ellipsis-h, set=fa]) adjacent to the Situation and Action, then click Edit.

5. In the Situation Rule modal, in the When situation occurs list, select Perform Action (default) or Execute Script:

   * For Execute Script, enter your script in the commented code block:

     ```bash
     // Script has access to the following variables:
     // source, target, sourceAction, linkQualifier, context, recon
     // the recon.actionParam object contains information about the current recon operation.
     ```

     Learn more about the available variables and action scripting patterns in [Script triggers defined in mappings](../idm-scripting/script-triggers-mappings.html) and [Synchronization actions](../idm-synchronization/sync-actions.html).

6. In the second list for When situation occurs, select an action as described in [Advanced sync rule action types](#advanced-sync-rule-action-types).

7. For advanced settings, click Show advanced settings to display the following options:

   * Restrict situation lets you specify query filters or add a script to restrict policy actions to a subset of records where situation is applicable.

   * Execute script on action complete lets you set up a script to execute after your action is complete.

8. Click Save.

### Advanced sync situation rules

| Situation              | Description                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| `Ambiguous`            | `Source object correlates to multiple target objects, without a link.`                    |
| `Source Missing`       | `Valid target found, link found.`                                                         |
| `Missing`              | `The source links to a missing target object.`                                            |
| `Found Already Linked` | `Correlation from source points to a target object already linked to a different source.` |
| `Unqualified`          | `Source object not qualified, but target objects found.`                                  |
| `Unassigned`           | `Valid target found, no link.`                                                            |
| `Link Only`            | `Link found, target object not found.`                                                    |
| `Target Ignored`       | `Doesn't pass validTarget script.`                                                        |
| `Source Ignored`       | `Doesn't pass validSource script.`                                                        |
| `All Gone`             | `Source object removed, link not found, correlation not possible.`                        |
| `Confirmed`            | `Valid source and target objects linked.`                                                 |
| `Found`                | `Correlation query from source points to one target object.`                              |
| `Absent`               | `Source object has no matching target.`                                                   |

### Advanced sync rule action types

When a reconciliation determines the situation of a record, you must specify the action to be taken.

|   |                                      |
| - | ------------------------------------ |
|   | `Async` is the default action state. |

| Action            | Description                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| `Async` (default) | `An asynchronous process has been started, so do not perform any action or generate any report` |
| `Create`          | `Create and link a target object`                                                               |
| `Delete`          | `Delete and unlink the target object`                                                           |
| `Unlink`          | `Unlink the linked target object`                                                               |
| `Exception`       | `Flag the link situation as an exception`                                                       |
| `Update`          | `Link and update a target object`                                                               |
| `Ignore`          | `Don't change the link or target object state`                                                  |
| `Report`          | `Don't perform any action but report what would happen if the default action were performed`    |
| `No Report`       | `Don't perform any action or generate any report`                                               |

---

---
title: Manage advanced sync schedules
description: Schedule automatic reconciliation jobs to keep identity data synchronized on a recurring basis
component: pingoneaic
page_id: pingoneaic:identities:advanced-sync-schedules
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/advanced-sync-schedules.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities", "Synchronization"]
section_ids:
  configure-advanced-sync-schedules: Configure a full reconciliation schedule
---

# Manage advanced sync schedules

Advanced sync schedules let you run reconciliation for a mapping automatically on a recurring basis. Each schedule is scoped to a single mapping, so you can control how often different systems are synchronized.

You can only configure a **full reconciliation** job that periodically runs the mapping's reconciliation logic. Reconciliation processes all relevant records on the source and target, not just changes. Learn more in [Run advanced sync reconciliation](advanced-sync-reconciliation.html) and [Manage reconciliation](../idm-synchronization/manage-recon.html).

## Configure a full reconciliation schedule

To configure a reconciliation schedule for a mapping:

1. In the Advanced Identity Cloud admin console, open the [Advanced Sync editor](advanced-sync.html#configure-advanced-sync).

2. In the Advanced Sync editor, open the mapping you want to configure.

3. On the Schedules tab, click the Full Reconciliation row or click Set Up adjacent to the `Inactive` Status column.

   |   |                                           |
   | - | ----------------------------------------- |
   |   | The initial schedule state is `inactive`. |

4. In the Schedule Full Reconciliation Job modal, manually configure the frequency and interval or use a [cron expression](https://en.wikipedia.org/wiki/Cron).

   * To manually schedule a full reconciliation (default):

     1. In the Frequency section, choose how often to run the job (for example, every few hours, days, weeks, or months). By default, the schedule runs every day.

     2. (Optional) Set a specific start time and, if needed, an end condition. You can choose to run the job a fixed number of times, until a specific date, or indefinitely.

     3. Click Save.

        |   |                                                                                                      |
        | - | ---------------------------------------------------------------------------------------------------- |
        |   | If you specify a start date and an end date, the time zones *must* match to create a valid schedule. |

   * To schedule a full reconciliation using a cron expression:

     1. Enable the Use cron toggle.

     2. In the Frequency field, Enter a valid cron string.

        |   |                                                                                                                                                                            |
        | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | To validate a `cron` schedule expression, learn more in [Validate cron trigger expressions](../idm-schedules/configure-dynamic-schedules.html#validating-schedule-syntax). |

     3. Click Save.

---

---
title: Manage identities
description: Create and manage user profiles, roles, organizations, and other identity resources
component: pingoneaic
page_id: pingoneaic:identities:manage-identities
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/manage-identities.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities", "Users", "Roles", "Assignments", "Organizations"]
page_aliases: ["pingoneaic::identities-manage.adoc"]
section_ids:
  create-users: Users
  create_a_user_profile: Create a user profile
  edit_a_user_profile: Edit a user profile
  reset_a_user_password: Reset a user password
  delete_a_user: Delete a user
  add_an_application_to_a_user: Add an application to a user
  manage-trusted-devices: Manage trusted devices
  create-roles: Roles
  create_an_external_role: Create an external role
  edit-external-role: Edit an external role
  add_an_application_to_a_role: Add an application to a role
  create_an_internal_role: Create an internal role
  edit-internal-role: Edit an internal role
  assignments: Assignments
  create_a_mapping_identities: Create a mapping
  create_an_assignment: Create an assignment
  edit_an_assignment: Edit an assignment
  organizations: Organizations
  import_identities_into_an_organization: Import identities into an organization
  create_a_parent_organization: Create a parent organization
  create_an_organization_owner: Create an organization owner
  create_an_organization_administrator: Create an organization administrator
  create_a_sub_organization: Create a sub-organization
  tenant_administrators: Tenant administrators
  organization_owners_and_organization_administrators: Organization owners and organization administrators
  edit_an_organization_or_sub_organization: Edit an organization or sub-organization
  tenant_administrators_2: Tenant administrators
  organization_owners_and_organization_administrators_2: Organization owners and organization administrators
  add_or_create_organization_members: Add or create organization members
  add_a_member_to_an_organization: Add a member to an organization
  add_a_member_to_an_organization_tenant_administrators: Tenant administrators
  organization_owners_and_organization_administrators_3: Organization owners and organization administrators
  create_a_new_user_profile_in_an_organization: Create a new user profile in an organization
  create_a_new_user_profile_in_an_organization_tenant_administrators: Tenant administrators
  organization_owners_and_organization_administrators_4: Organization owners and organization administrators
  delete_an_organization: Delete an organization
  delete_an_organization_tenant_administrators: Tenant administrators
  organization_owners_and_organization_administrators_5: Organization owners and organization administrators
---

# Manage identities

A PingOne Advanced Identity Cloud tenant can contain data about people (such as employees, customers, or vendors) and devices (such as cell phones or printers), each of which has a unique combination of defining attributes. Advanced Identity Cloud stores these attributes in *identity profiles*.

In an identity profile, [roles](roles-assignments.html#roles) and [assignments](roles-assignments.html#assignments) define the type and extent of access permissions given to users and devices. Advanced Identity Cloud uses roles and assignments to *provision* identity profiles with permissions.

For quick takes, learn more in [About roles and assignments](roles-assignments.html) and [How provisioning works](roles-assignments.html#how_provisioning_works). To view a list of tenant administrators, learn more in [View the tenant administrators list](../tenants/tenant-administrator-settings.html#view-the-tenant-administrators-list). To view realm settings, learn more in [Realm settings](../realms/realm-settings.html).

Note that identity resources are grouped by realm. If you can't find a resource, make sure that you're looking in the right realm.

## Users

A user is a person, such as a customer, employee, or vendor, whose identity profile is stored in a tenant. A user identity profile is also called a *user profile*.

For a deep dive into Advanced Identity Cloud user identities, learn more in [Manage identities](../idm-objects/users.html).

### Create a user profile

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Users and New Alpha realm - User.

3. On the New Alpha realm - User page, enter information for the user, and then click Save. For a list of user attributes, learn more in [User identity attributes and properties reference](user-identity-properties-attributes-reference.html).

### Edit a user profile

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Users, and click on a username.

3. Edit information for the user, and then click Save. For a list of user attributes, learn more in [User identity attributes and properties reference](user-identity-properties-attributes-reference.html).

### Reset a user password

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Users, and click on a username.

3. Click Reset Password.

4. Enter a new password, and click Reset Password to save the new password.

### Delete a user

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Users, and click on a username.

3. At the bottom of the page, click Delete Alpha realm - User. The Delete operation cannot be undone.

### Add an application to a user

When you add an application to a user, Advanced Identity Cloud automatically provisions an account for them in the target application.

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Users, and click a username.

3. Click the Applications tab.

4. Click + Add Application.

5. On the Account Details page, in the Application drop-down field, select an application.

6. Click Assign. Afterward, in the [Users & Roles](../app-management/manage-users-and-roles.html) tab, the [Assignment](../app-management/manage-users-and-roles.html#view_an_end_user_account) column shows the user has a Direct assignment to the application.

### Manage trusted devices

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To populate the Trusted Devices tab, add the [Device Profile Collector node](https://docs.pingidentity.com/auth-node-ref/latest/device-profile-collector.html) to your authentication journeys to collect end-user device information. |

You can view and delete the list of trusted devices on a user account.

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Users, and click a username.

3. Click the Trusted Devices tab to view a list of devices that the end user has used to sign on to their account.

4. Click a device from the list to open its Device Details modal window. The modal displays device information such as operating system and browser. The modal may also display location information for the device if the [Device Profile Collector node](https://docs.pingidentity.com/auth-node-ref/latest/device-profile-collector.html) is configured to collect it and if the end user consented to the information being collected by their browser.

5. Choose one of the following options:

   * To close the modal, click Done.

   * To remove the device from the list of trusted devices:

     1. Click Remove device.

     2. In the Delete Device? modal window, click Delete.

## Roles

For a quick take, learn more in [Roles](roles-assignments.html#roles) in this guide. For a deeper dive, learn more in [Roles](../idm-objects/roles.html).

### Create an external role

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha Realm - Roles and New Alpha realm - Role.

3. On the role page, enter the following information for the role, and then click Next:

   * Name: Unique identifier to display in the roles list.

   * Description: String to describe the role, such as Sales.

4. (Optional) Assign the role only to identities with specified attributes:

   1. On the Dynamic Alpha realm - role Assignment page, use the slider to create a conditional filter for the role.

   2. Use the choosers to specify conditions that an identity must meet.

   3. (Optional) Click Advanced Editor to create a query-based condition.

   4. Click Next.

5. (Optional) Assign the role only at specified times:

   1. On the Time Constraint page, use the slider to enable a start and end date during which the role is active.

   2. Use the calendar, clock choosers, and time zone offset.

   3. Click Save.

### Edit an external role

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha Realm - Roles, and click on a role name.

3. Add managed assignments to the role:

   1. On the role page, click Managed Assignments and Add Managed Assignments.

   2. Select a managed assignment from the drop-down list, and click Save.

4. Add members to the role:

   1. On the role page, click Role Members and Add Role Members.

   2. Select an identity from the members list.

   3. (Optional) Use the slider to assign the role only at specified times, and then add the dates, times, and timezone offset.

5. Change the time constraints or conditions of a role.

   1. On the Internal Role page, click Settings.

   2. In Time Constraint or Condition, click Set Up to edit the parameters, and then click Save.

### Add an application to a role

When you add an application to a role and then assign a user to the role, Advanced Identity Cloud automatically provisions the user in the target application.

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha Realm - Roles, and click on a role name.

3. Click the Applications tab.

4. Click + Add Application.

5. On the Account Details page, in the Application drop-down field, select an application.

6. Click Assign. Afterward, in the [Users & Roles](../app-management/manage-users-and-roles.html) tab, the [Assignment](../app-management/manage-users-and-roles.html#view_an_end_user_account) column shows the user has a Role-based assignment to the application.

### Create an internal role

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. Click Internal Roles.

3. Click + New Internal Role.

4. In the New Internal role screen, enter role details:

   * Name: Unique identifier to display in the Roles list.

   * Description (optional): String that's meaningful to your organization.\
     Examples: Employee, Customers, Sales Department, and Europe.

5. Click Next.

6. To choose an identity object that the role should grant permissions to, on the Internal role Permissions dialog, choose an identity object.

7. To add the identity, click Add.

8. Set the permission for the identity:

   * View: Grant the identity object view access.

   * Create: Grant the identity object create access.

   * Update: Grant the identity object update access.

   * Delete: Grant the identity object delete access.

9. To add another identity, repeat the above three steps.

10. Click Next.

11. To optionally assign a user to a role based on specific attributes, on the Dynamic Internal role Assignment screen:

    1. Enable A conditional filter for this role.

    2. Use the choosers and drop-down lists to specify conditions for assigning a user to a role.

    3. To create a query-based condition, click Advanced Editor, and edit the query code.

    4. Click Next.

12. To assign a role on a temporary basis, on the Time Constraint screen:

    1. Enable Set a start and end date during which this role will be active.

    2. Use the calendar and date pickers to define when the role is in effect:

       * Specify the time zone to be used for the start date/time and end/date you specified. Choose a time zone relative to Greenwich Mean Time (GMT). GMT is the same as Universal Time Coordinated (UTC).

       * To view a worldwide list of offset times, click Time zones chart to calculate the offset time.

13. Click Save.

### Edit an internal role

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Internal Roles, and click on a role name.

   * To edit role details:

     1. Click the Details tab.

     2. Edit the Name field and possibly the Description field.

     3. Click Save.

   * To edit a privilege:

     1. Click the Privileges tab.

     2. Click a privilege.

     3. Edit the privilege details.

     4. Click Save.

   * To add a privilege:

     1. Click the Privileges tab.

     2. Click + Add Privileges.

     3. To choose an identity that this role should grant administration privileges to, use the drop-down list field to choose an identity object.

     4. To add the identity, click Add.

     5. Set the permission for the identity:

        * View: Grant the identity object view access.

        * Create: Grant the identity object create access.

        * Update: Grant the identity object update access.

        * Delete: Grant the identity object delete access.

     6. To add another identity, repeat the above three steps.

     7. Click Save.

   * To edit a member:

     1. Click the Members tab.

     2. Click a member.

     3. Edit the member's information.

     4. Click Save.

   * To add a member:

     1. Click the Members tab.

     2. Click + Add Members.

     3. Use the drop-down field to choose a member.

     4. Click Save.

   * To set a start and end date for when the role is active:

     1. On the Internal Role page, click Settings.

     2. In the Time Constraint section, click Set Up.

     3. Enable Set a start and end date during which this role will be active.

     4. Set the time parameter fields.

     5. Click Save.

   * To set a conditional filter for the role:

     1. On the Internal Role page, click Settings.

     2. In the Condition section, click Set Up.

     3. Enable A conditional filter for this role.

     4. Set the condition fields.

     5. Click Save.

   * To use JSON to configure internal role details, privileges, and other information:

     1. On the Internal Role page, click Raw JSON.

     2. Edit the JSON sample.

For a deep dive into roles, learn more in [Roles](../idm-objects/roles.html).

## Assignments

For a quick take, learn more in [Assignments](roles-assignments.html#assignments). For a deep dive into roles and assignments, learn more in [Use assignments to provision users](../idm-objects/working-with-role-assignments.html).

### Create a mapping

Before you create an assignment, make sure that you have a mapping, or create a mapping as described in this section.

A mapping specifies a relationship between an object and its attributes, in two data stores. Learn more in [Resource mapping](../idm-synchronization/mappings.html).

1. In the Advanced Identity Cloud admin console, go to Native Consoles > Identity Management. The Identity Management console is displayed.

2. Click Create Mapping, and add a mapping using information from [Configure mappings using the admin UI](../idm-synchronization/cfg-mapping-resource.html#mappings-ui).

### Create an assignment

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Assignments and New Alpha realm - Assignments.

3. On the assignment page, enter the following information for the assignment, and then click Next:

   * Name: Unique identifier to display in the assignments list.

   * Description: String to describe the assignment, such as Sales reporting.

   * Mapping: Select a mapping to which the assignment applies.

4. (Optional) Add an attribute to map to the target system. Learn more in [provision an attribute in the target data store](roles-assignments.html#assignment_mapped_to_attribute).

   1. On the Assignment Attributes page, click Add an Attribute.

   2. Select an attribute from the drop-down list, and enter a value for the attribute. The attribute-value pair is synchronized with user accounts in the target data store.

   3. (Optional) Click [icon: cog, set=fa], and in the Assignment Operation window specify how Advanced Identity Cloud synchronizes assignment attributes on the target data store:

      * On assignment

        * Merge with target: The attribute value is added to any existing values for that attribute.

        * Replace target: The attribute value overwrites any existing values for that attribute. The value from the assignment becomes the authoritative source for the attribute.

      * On unassignment

        * Remove from target: The attribute value is removed from the system object when the user is no longer a member of the role, or when the assignment itself is removed from the role definition.

        * No operation: Removing the assignment from the user's effectiveAssignments has no effect on the current state of the attribute in the system object.

5. Click [icon: plus, set=fa]to add the assignment, and then click Save.

6. (Optional) Add an event script.

   |   |                                   |
   | - | --------------------------------- |
   |   | Groovy scripts are not supported. |

   1. One the Alpha realm - Assignment page, click Add an event script.

   2. Choose whether to trigger the script on assignment or unassignment.

   3. Enter the script in the text box or upload it.

   4. (Optional) Define custom variables to pass to your script. To enter variables in JSON format, use the JSON slider.

   5. Click Save.

7. (Optional) Add managed roles to the assignment

   1. On the Alpha realm - Assignment page, click the Manage Roles tab, and click Add Manage Roles.

   2. Select a managed role from the drop-down list, and click Save.

### Edit an assignment

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Assignments and click on an assignment name.

3. In the Details tab and Manage Roles tab, edit the assignment settings.

## Organizations

For a quick take, learn more in [Organizations](organizations.html).

Organizations can be managed in the following ways:

* By tenant administrators, using the REST APIs:

  Before you can use the IDM REST APIs, you'll have to get an access token and authenticate to the IDM API server. Learn more in [Accessing the IDM REST APIs](../developer-docs/authenticate-to-rest-api-with-access-token.html).

  For examples of API calls for organizations, learn more in [Manage Organizations Over REST](../idm-objects/manage-orgs-rest.html).

* By tenant administrators, using the Advanced Identity Cloud admin console as described on this page.

* By organization owners and organization administrators, using the hosted account pages as described on this page.

### Import identities into an organization

You can build organizations in different ways. For example, you can start with a parent organization that contains all user identities, and then build your organization hierarchy. Alternatively, you can start with a hierarchy of empty organizations, and then add users. Whatever approach you take, at some point you'll have to import identities into an organization.

| Tenant administrators | Organization owners   | Organization administrators |
| --------------------- | --------------------- | --------------------------- |
| [icon: check, set=fa] | [icon: times, set=fa] | [icon: times, set=fa]       |

Only tenant administrators can import identities into an organization.

For this example, it is assumed that the following items already exist:

* A .csv file containing 100 user identities

* A parent organization with no members

1. In the Advanced Identity Cloud admin console, go to Identities > Import.

2. On the Bulk Import page, click New Import.

3. On the Upload CSV page, select Alpha realm - Users, and then click Next.

4. In the Upload CSV page, Enter the following information and then click Next:

   * CSV File: Browse to your file

   * Match Using: Add a property name to use for a unique record match

5. When the Import Complete dialog box is displayed, and you can confirm that the import was successful, click Done.

   You can confirm the import in the following ways:

   * Go to Identities > Manage > Alpha realm - Users, and open any user profile. Click Organizations to which I Belong, and make sure that the organization you created is displayed.

   * Go to Identities > Manage > Alpha realm - Organizations, and make sure that the organization you created is displayed.

   * Click the name of the organization you created, click Members, and then make sure that all the imported user identities are displayed.

### Create a parent organization

| Tenant administrators | Organization owners   | Organization administrators |
| --------------------- | --------------------- | --------------------------- |
| [icon: check, set=fa] | [icon: times, set=fa] | [icon: times, set=fa]       |

Only tenant administrators can create a parent organization.

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Organizations and New Alpha realm - Organizations.

3. On the New Alpha realm - Organizations page, enter a name for the organization. Uppercase, lowercase, alphanumeric, special characters, and white spaces are allowed.

4. Click Save.

5. In the organization page, change the name, add a description, or assign a parent organization. To designate this organization as the parent, leave the Parent Organization field blank.

6. Click Save.

### Create an organization owner

| Tenant administrators | Organization owners   | Organization administrators |
| --------------------- | --------------------- | --------------------------- |
| [icon: check, set=fa] | [icon: times, set=fa] | [icon: times, set=fa]       |

Only tenant administrators can create an organization owner.

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Organizations and click on an organization name.

3. Click Owner and Add Owner.

4. In the Add Owner page, select an identity from the drop-down list.

   |   |                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Make sure that the organization owner is not also an organization member. This can result in giving the organization administrator greater control of the organization than its owner. |

5. Click Save.

### Create an organization administrator

| Tenant administrators | Organization owners   | Organization administrators |
| --------------------- | --------------------- | --------------------------- |
| [icon: check, set=fa] | [icon: check, set=fa] | [icon: times, set=fa]       |

* Tenant administrators can create an organization administrator in any organization.

* Organization owners can create organization administrators only within organizations or sub-organization where they are owner.

* Organization administrators cannot create other organization administrators.

1. On the Manage Identities page, click Alpha realm - Organizations and click on an organization name.

2. Click Administrators and Add Administrators.

3. In the Add Administrators page, select a user from the drop-down list. The user must already belong to the organization.

4. Click Add Administrators. The username is displayed in the members list.

### Create a sub-organization

| Tenant administrators | Organization owners   | Organization administrators |
| --------------------- | --------------------- | --------------------------- |
| [icon: check, set=fa] | [icon: check, set=fa] | [icon: check, set=fa]       |

* Tenant administrators can create sub-organizations within any organization.

* Organization owners can create sub-organizations only within organizations or sub-organizations where they are owner.

* Organization administrators can create sub-organizations only within organizations or sub-organizations where they are administrator.

#### Tenant administrators

|   |                                                   |
| - | ------------------------------------------------- |
|   | Tenant administrators can view all organizations. |

Follow the steps in to [create a parent organization](#create_a_parent_organization), and then set a parent organization that is:

* An existing organization

* One level of hierarchy higher than this child organization

#### Organization owners and organization administrators

|   |                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   | Organization owners and organization administrators can view only the organizations and sub-organizations that they own or administrate. |

1. In the hosted account pages, go to Alpha realm - Organizations and New Alpha realm - Organizations.

2. On the New Alpha realm - Organizations, page enter a name for the organization. Uppercase, lowercase, alphanumeric, special characters, and white spaces are allowed.

3. Click Save.

4. In the organization page, optionally change the name, and add a description.

5. Assign a parent organization that is One level of hierarchy higher than this child organization.

6. Click Save.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | While privileges for default attributes are automatically included when setting up a sub-organization, custom attributes need to be manually added to your privileges configuration before creating the sub-organization.Do this by adding the custom attribute to the `accessFlags` section of the `owner-view-update-delete-orgs` and `owner-create-orgs` privileges. These are accessed through the REST API at the `/openidm/config/alphaOrgPrivileges` or `/openidm/config/bravoOrgPrivileges` endpoints (depending on the realm you are updating). |

### Edit an organization or sub-organization

| Tenant administrators | Organization owners   | Organization administrators |
| --------------------- | --------------------- | --------------------------- |
| [icon: check, set=fa] | [icon: check, set=fa] | [icon: check, set=fa]       |

* Tenant administrators can edit any organization or sub-organization.

* Organization owners can edit only organizations or sub-organization where they are owner.

* Organization administrators can edit only organizations or sub-organizations where they are administrator.

#### Tenant administrators

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Organizations and click on an organization name.

3. In the organization page, change the name, add a description, or assign a parent organization.

   Uppercase, lowercase, alphanumeric, special characters, and white spaces are allowed in the organization name.

   To designate this organization as the parent, leave the Parent Organization field blank.

4. Click Save.

#### Organization owners and organization administrators

1. In the hosted account pages, go to Alpha realm - Organizations, and click on an organization name.

2. In the organization page, change the name, add a description, or assign a parent organization.

   Uppercase, lowercase, alphanumeric, special characters, and white spaces are allowed in the organization name.

   To designate this organization as the parent, leave the Parent Organization field blank.

3. Click Save.

### Add or create organization members

| Tenant administrators | Organization owners   | Organization administrators |
| --------------------- | --------------------- | --------------------------- |
| [icon: check, set=fa] | [icon: check, set=fa] | [icon: check, set=fa]       |

* Tenant administrators can access all members of all organizations.

* Organization owners can access only members of organizations they own.

  * An organization owner can add a user profile to their organization only if the user profile exists inside their ownership area.

  * An organization owner can [create a new user profile as a member of their organization](#create_a_new_user_profile_in_an_organization).

* Organization administrators can access only members in their administrative area.

  * An organization administrator can add a user profile to their organization only if the user profile exists inside their administrative area.

  * An organization administrator can [create a new user profile as a member of their organization](#create_a_new_user_profile_in_an_organization).

#### Add a member to an organization

##### Tenant administrators

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Organizations and click on an organization name.

3. On the organization page, click Members and Add Members.

4. Select an identity from the members list, and then click Save. The username or usernames you added are now displayed in the members list.

##### Organization owners and organization administrators

1. In the hosted account pages, go to Alpha realm - Organizations.

2. Follow steps in the [tenant administrator instructions](#add_a_member_to_an_organization_tenant_administrators).

#### Create a new user profile in an organization

##### Tenant administrators

1. Add a user profile, as described in [Create a user profile](#create_a_user_profile).

2. In the user profile, click Organizations to which I Belong and Add Organizations to which I Belong.

3. In the add organization dialog box, choose one or more organizations from the drop-down list, and click Save.

##### Organization owners and organization administrators

1. In the hosted account pages, go to Alpha realm - Users.

2. Follow steps in the [tenant administrator instructions](#create_a_new_user_profile_in_an_organization_tenant_administrators).

### Delete an organization

| Tenant administrators | Organization owners   | Organization administrators |
| --------------------- | --------------------- | --------------------------- |
| [icon: check, set=fa] | [icon: check, set=fa] | [icon: check, set=fa]       |

* Tenant administrators can delete any organization or sub-organization.

* Organization owners can delete only organizations or sub-organizations where they are owner.

* Organization administrators can delete only organizations or sub-organization where they are administrator.

#### Tenant administrators

1. In the hosted account pages, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Organizations and click on an organization name.

3. On the organization page, click Delete Alpha realm - Organization.

   |   |                                  |
   | - | -------------------------------- |
   |   | This operation cannot be undone. |

#### Organization owners and organization administrators

1. In the Advanced Identity Cloud end-user UI, go to Manage.

2. Follow steps in the [tenant administrator instructions](#delete_an_organization_tenant_administrators).

---

---
title: Manage relationship-derived virtual properties (RDVPs)
description: Create relationship-derived virtual properties to efficiently display related object data
component: pingoneaic
page_id: pingoneaic:identities:manage-rdvps
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/manage-rdvps.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identities"]
section_ids:
  manage-rdvps: Manage RDVPs
  add-rdvps-to-relationship: Add RDVPs to a relationship
  modify-rdvps-on-relationship: Modify RDVPs on a relationship
  delete-rdvps-from-relationship: Delete RDVPs from a relationship
  derived-property-settings-reference: Derived property settings reference
---

# Manage relationship-derived virtual properties (RDVPs)

Relationship-derived virtual properties (RDVPs) are managed object properties that display data from a related object. They make it easier to query and display relationship data without needing to traverse the relationship in your query. RDVPs are one type of [virtual property](../idm-objects/managed-object-virtual-properties.html) available in Advanced Identity Cloud.

An example RDVP uses a `user` object type with a `manager` relationship. A `managerEmail` RDVP pulls the email address from the related manager's object, so you can display or filter by the manager's email as if it were a direct property on the user.

Learn more about RDVPs in [Relationship-derived virtual properties](../idm-objects/managed-object-virtual-properties.html#relationship-derived-virtual-properties) and [Relationships](../planning/plan-object-modeling-relationships.html).

|   |                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This page describes how to add an RDVP from a relationship's Derived Properties tab. RDVPs created this way are regular virtual properties in the schema and behave the same as those created from a managed object type's Properties tab. Learn more in [Manage custom properties](customize-object-types.html#manage-custom-properties). |

## Manage RDVPs

To manage RDVPs for a relationship:

1. In the Advanced Identity Cloud admin console, go to [icon: people, set=material, size=inline] Identities > Configure.

2. On the Managed Object Types page, select the object type. For example, select Alpha realm – User.

3. Click the Relationships tab, and then click the relationship you want to manage RDVPs for.

4. Click the Derived Properties tab.

5. On the Derived Properties page, do one of the following:

   * To [add an RDVP](#add-rdvps-to-relationship), click [icon: add, set=material, size=inline] Add Derived Property.

   * To [modify an RDVP](#modify-rdvps-on-relationship), click ([icon: ellipsis-h, set=fa]) for the RDVP and select [icon: edit, set=material, size=inline] Edit.

   * To [delete an RDVP](#delete-rdvps-from-relationship), click ([icon: ellipsis-h, set=fa]) for the RDVP and select [icon: delete, set=material, size=inline] Delete.

### Add RDVPs to a relationship

1. On the Derived Properties page, click [icon: add, set=material, size=inline] Add Derived Property for the side of the relationship where you want to add the derived property.

2. In the Add Derived Property modal, configure the [derived property settings](#derived-property-settings-reference) and click Add.

3. To add another derived property to the relationship for the same side of the relationship, click Add and repeat step 2.

4. To add derived properties to the other side of the relationship, repeat steps 1 - 3.

5. When you've finished adding properties, click Save.

### Modify RDVPs on a relationship

1. On the Derived Properties page, click the ellipsis icon ([icon: ellipsis-h, set=fa]) for the RDVP you want to modify, and select [icon: edit, set=material, size=inline] Edit.

2. In the Edit Derived Property modal, modify the [derived property settings](#derived-property-settings-reference) and click Update.

3. Click Save.

### Delete RDVPs from a relationship

|   |                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deleting an RDVP removes the underlying virtual property from the schema. Any queries, scripts, or UI components that reference that property will stop working until they're updated. |

1. On the Derived Properties page, click the ellipsis icon ([icon: ellipsis-h, set=fa]) for the RDVP you want to delete, and select [icon: delete, set=material, size=inline] Delete.

2. Click Delete to confirm the deletion.

3. Click Save.

## Derived property settings reference

Use the following settings in the Add/Edit Derived Property modal to configure an RDVP for a relationship.

|   |                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | RDVPs are typically defined as array properties because a relationship can return multiple related objects. The type and multivalued behavior are determined on the property itself in the managed object schema. |

| Field, option                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                               | A unique name for the derived property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Label (optional)                   | A human-readable label for the derived property that appears in the UI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Description (optional)             | An optional description for the derived property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Derive value from                  | The related property from which to derive the value for the derived property.- Select which fields to project from the related objects. For example, if you have a relationship between a user and their manager, you can derive a `managerEmail` RDVP by selecting the manager's `mail` field.

- To derive a property from the entire related managed object type instead of a specific property, select Full \[*managed object type*] Object. For example, you could create a `managerDetails` property on a user to expose the manager's full profile (name, email, department, and so on). |
| Flatten properties                 | Controls how the RDVP values are represented.Select this checkbox if you want a simple, query-friendly value instead of full object references.- When not selected (`flattenProperties = false`), the RDVP returns objects that include `_id`, `_rev`, and the referenced fields from the related object.

- When selected (`flattenProperties = true`), the RDVP returns primitive values (for example, just the email addresses or names) instead of full JSON objects. For multivalued RDVPs, this is an array of primitive values instead of an array of objects.                           |
| Searchable                         | By default, RDVPs aren't searchable. Select this checkbox to make the RDVP searchable in the Advanced Identity Cloud admin console and using the REST API.	Making an RDVP searchable might impact performance, especially if the derived property is based on a relationship with many related objects or if you have a large number of identities in your tenant.                                                                                                                                                                                                                              |
| Notify Related Managed Object Type | Specify a related managed object type that will be notified on modification of the properties.This allows changes to the derived property on one side of a relationship to automatically trigger recalculation of related derived or virtual properties on the other object type.                                                                                                                                                                                                                                                                                                               |

---

---
title: Organizations
description: Use organizations to structure identities hierarchically and delegate administrative control
component: pingoneaic
page_id: pingoneaic:identities:organizations
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/organizations.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Organizations", "User Profiles"]
page_aliases: ["pingoneaic::concepts-organizations.adoc"]
section_ids:
  organization_use_case: Organization use case
  top_level_organizations: Top-level organizations
  owners: Owners
  administrators: Administrators
  more_information: More information
---

# Organizations

Create organizations in PingOne Advanced Identity Cloud when you want to group identities to suit your business needs.

For example, you can build an organization structure modeled after your brand hierarchy. This lets you control access to business applications with tailored sign-on experiences. You can also use organizations to delegate user administration.

## Organization use case

Here's an example to help explain organization concepts. MightyBank is a conglomeration of independently-operated banks. MightyBank organizes its business units into two locales based on banking regulations associated with each locale. Within a business unit, each bank brand is a self-contained organization.

This diagram depicts MightyBank's hierarchy of [realms](../realms/alpha-bravo-realms.html) and organizations for identity management:

![idcloudui concepts organizations hierarchy](_images/idcloudui-concepts-organizations-hierarchy.png)

MightyBank organized their Advanced Identity Cloud tenant similarly to their business units. The Alpha realm contains MightyBank identities in the Americas. The Bravo realm contains MightyBank identities in Europe, the Middle East, and Africa (EMEA). Identities represent all employees, contractors, partners, vendors, customers—anyone who conducts business for or with MightyBank.

Each organization in the hierarchy has a designated [owner](#owners). An owner can create child organizations, or *sub-organizations*. Owners can also add administrators to their organizations and sub-organizations.

[Organization administrators](#administrators) manage user identities within organizations. Administrators also delegate administration to individual users through [roles and assignments](roles-assignments.html).

Users who belong to an organization are known as *members* of the organization.

## Top-level organizations

Only Advanced Identity Cloud tenant administrators can create top-level organizations. In this example, Sam Carter is an Advanced Identity Cloud tenant administrator. Sam has created a top-level organization in each realm.

Sam can view and manage all identities within both the Alpha and Bravo realms:

![idcloudui concepts orgs sam alpha bravo realms](_images/idcloudui-concepts-orgs-sam-alpha-bravo-realms.png)

Sam delegates organization administration by setting up organization [owners](#owners), who in turn set up organization [administrators](#administrators).

## Owners

The main job of organization owners is to create organizations and sub-organizations. They also designate users, within the organizations they own, as administrators. Users who are authorized to manage identities within organizations are called *organization administrators*.

In this example, Sam designated Alma as owner of the top-level organization in the Alpha realm. Alma grouped identities into sub-organizations. One sub-organization contains Acme Bank identities. A second sub-organization contains MexBanco identities.

Alma is authorized to manage the MightyBank Americas organization, and all its sub-organizations.

![idcloudui concepts orgs aspreckles realm](_images/idcloudui-concepts-orgs-aspreckles-realm.png)

Organization owners can do the following, but only within the organizations and sub-organizations they own:

* [Add members](manage-identities.html#add_or_create_organization_members) and [update an organization profile](manage-identities.html#edit_an_organization_or_sub_organization).

* [Add and update sub-organizations](manage-identities.html#create_a_sub_organization).

* [Add an administrator to an organization](manage-identities.html#create_an_organization_administrator) or sub-organization.

  |   |                                                                                                                                                                                                                                                                                                                                                                                               |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * An owner can [add an existing user profile](manage-identities.html#add_or_create_organization_members) to a sub-organization only if the user already belongs to a parent organization.

  * An owner can [create a new user profile](manage-identities.html#create_a_new_user_profile_in_an_organization) in a sub-organization if the user doesn't already belong to a parent organization. |

In this example, before Alma can add a user profile to the Acme Bank organization, the user must belong to MightyBank Americas, the parent organization. If a user doesn't belong to the parent organization, then Alma can open the Acme Bank organization, and create a new user profile directly in the organization.

## Administrators

The main job of organization administrators is to manage user identities within an organization or sub-organization.

In this example, Alma designated Barbara as the administrator for MightyAmericas. Barbara is authorized to manage all identities in the MightyAmericas organization, and in all of its sub-organizations.

Barbara then delegated administration to two employees in the Acme Bank organization, and two employees in the MexBanco organization. These delegated administrators share responsibility for [managing identities](manage-identities.html).

![idcloudui concepts orgs bjensen admin](_images/idcloudui-concepts-orgs-bjensen-admin.png)

Organization administrators can do the following, but only within the organizations they are authorized to manage:

* [Add and update members](manage-identities.html#add_or_create_organization_members).

* [Add](manage-identities.html#create_a_sub_organization) and [update sub-organizations](manage-identities.html#edit_an_organization_or_sub_organization).

* Delegate user identity administration through [roles and assignments](roles-assignments.html).

  |   |                                                                                                                                                                                                                                                                                                                                                                                                         |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * An administrator can [add an existing user profile](manage-identities.html#add_or_create_organization_members) to an organization only if the user already belongs to a parent organization.

  * An administrator can [create a new user profile](manage-identities.html#create_a_new_user_profile_in_an_organization) in an organization if the user doesn't already belong to a parent organization. |

In this example, before an administrator can add a user profile to the Acme Bank organization, the user profile must already belong to MightyBank Americas, the parent organization. If a user profile does not already belong in MightyBank Americas, then the administrator can open the Acme Bank organization and create a new user profile directly in the organization.

Each organization administrator can [manage user profiles](manage-identities.html), but in only the organization they're authorized to manage.

## More information

* For steps to create and manage organizations using Advanced Identity Cloud admin console, learn more in [Organizations](manage-identities.html#organizations) on the [Manage identities](manage-identities.html) page.

* For a deep dive into organizations, learn more in [Organizations](../idm-objects/organizations.html).

* To manage organizations using the REST API, learn more in [Manage organizations over REST](../idm-objects/manage-orgs-rest.html).

* For a deep dive into roles and assignments, learn more in [Authorization and roles](../idm-auth/authorization-and-roles.html) and [Use assignments to provision users](../idm-objects/working-with-role-assignments.html).

---

---
title: Pass-through authentication
description: Validate user passwords against remote systems for password migration or fallback authentication
component: pingoneaic
page_id: pingoneaic:identities:pass-through-authentication
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/pass-through-authentication.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Password", "Passthrough Authentication"]
section_ids:
  prepare_for_pass_through_authentication: Prepare for pass-through authentication
  migrate-passwords: Migrate passwords
  remote_authentication: Remote authentication
---

# Pass-through authentication

PingOne Advanced Identity Cloud pass-through authentication lets you validate passwords with a remote service. Common use cases include:

* Migrating passwords to Advanced Identity Cloud as part of authentication (just-in-time synchronization).

  See [Prepare for pass-through authentication](#prepare_for_pass_through_authentication) and [Migrate passwords](#migrate-passwords).

* Retaining a remote service for authentication.

  See [Prepare for pass-through authentication](#prepare_for_pass_through_authentication) and [Remote authentication](#remote_authentication).

Secure systems typically store passwords using one-way hash algorithms to make the passwords hard to crack. But, unless all systems support the same one-way hash algorithms, using this security measure alone can impede password synchronization.

A better security practice is to synchronize hashed passwords only between services that support the same password storage schemes. This ensures that the target service will always get passwords that it can read or compare. Only synchronize hashed passwords directly between services that support the same password storage schemes. Otherwise, the target service will get passwords that it cannot read or compare!

For example, Active Directory stores passwords using a hash algorithm that Advanced Identity Cloud doesn't support. So when you import identities based on Active Directory accounts, Advanced Identity Cloud can't synchronize the users' passwords. As a result, these users have no local credentials to authenticate to Advanced Identity Cloud.

The Advanced Identity Cloud Passthrough Authentication node uses a connector to validate credentials against the remote Active Directory service. The remote system verifies the user's password even if Advanced Identity Cloud doesn't support the hash algorithm.

For a list of DS schemes Advanced Identity Cloud supports, see [Synchronize passwords](sync-identities.html#synchronize_passwords).

## Prepare for pass-through authentication

Before using pass-through authentication:

1. Set up an Advanced Identity Cloud connector to the remote authentication service:

   * To set up a connector using an application, learn more in [Provision an application](../app-management/provision-an-application.html).

   * To set up a connector without an application, learn more in [Sync identities](sync-identities.html).

2. If Advanced Identity Cloud will save a copy of the password on successful authentication, align password policies so the remote password is certain to pass Advanced Identity Cloud password validation.

3. If you import or synchronize Advanced Identity Cloud profiles from the remote accounts, do not synchronize the passwords from the remote service to Advanced Identity Cloud.

Advanced Identity Cloud uses the local account to find the appropriate identifier, and the connector to authenticate remotely.

For details, see [Sync identities](sync-identities.html).

## Migrate passwords

When you cannot synchronize hashed passwords, you can use the pass-through authentication node to capture them. The following example journey demonstrates password capture and storage.

Advanced Identity Cloud performs authentication through a connector. It also stores the captured password securely using a strong, one-way hash algorithm. Advanced Identity Cloud can then act as the service of record for authentication of that account. After the user has authenticated successfully through this journey, the user can authenticate locally in Advanced Identity Cloud. The user no longer needs to authenticate using the remote service:

![passthrough sync passwords](_images/passthrough-sync-passwords.png)

Here's what happens in this example journey:

1. The Platform Username and Platform Password in the Page Node prompt the user for credentials.

2. The Data Store Decision node attempts local authentication.

   * If authentication succeeds, the Data Store Decision node processes the authentication like the default Login journey.

   * If authentication fails, the Passthrough Authentication node attempts remote authentication.

   When configuring the [Pass-through Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/passthrough-authentication.html), you must identify the connector to the remote authentication service in the node's System Endpoint field.

3. The Identify Existing User and Required Attributes Present nodes ensure that Advanced Identity Cloud has the data needed to update the account.

4. The Patch Object updates the account with the password used for successful remote authentication.

   When configuring this node, be sure to select `Patch As Object`.

5. The rest of the journey processes the authentication like the default Login journey.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This journey can fail when the remote password does not respect Advanced Identity Cloud policy.*This results in a `Failed policy validation` error displayed to the user* as the Patch Object node unsuccessfully tries with a password that fails password validation for the realm:![506](_images/passthrough-policy-violation.png)To avoid this problem, align password policies so that the remote password is sure to pass Advanced Identity Cloud password validation. For details, see [Password policy](../realms/password-policy.html). |

## Remote authentication

You can use the Passthrough Authentication node for remote authentication. This is useful when you can neither synchronize hashed passwords, nor use Advanced Identity Cloud as the service of record for authentication.

The example journey below does not capture the password on successful authentication. But, you could adapt the journey to capture the password. Then you could the cache authentication credentials in Advanced Identity Cloud temporarily. Advanced Identity Cloud then serves as a backup authentication service when the remote service is not available. If you adapt the journey in this way, be sure to configure the journey to authenticate periodically with the remote service, and to refresh the cached password.

The following journey demonstrates remote authentication when local authentication fails:

![passthrough remote authn](_images/passthrough-remote-authn.png)

1. The Platform Username and Platform Password in the Page Node prompt the user for credentials.

2. The Data Store Decision node attempts local authentication.

   * If authentication succeeds, the Data Store Decision node processes the authentication like the default Login journey.

   * If authentication fails, the Passthrough Authentication node attempts remote authentication.

3. The rest of the journey processes the authentication like the default Login journey.
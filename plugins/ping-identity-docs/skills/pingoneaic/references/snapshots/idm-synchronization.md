---
title: Clustered reconciliation
description: Distribute reconciliation across cluster nodes using paged queries and sub-jobs
component: pingoneaic
page_id: pingoneaic:idm-synchronization:clustered-recon
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/clustered-recon.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Reconciliation"]
section_ids:
  clustered-recon-config: Configure clustered reconciliation for a mapping
  clustered-recon-progress: Clustered reconciliation progress
  clustered-recon-cancel: Cancel a clustered reconciliation
---

# Clustered reconciliation

In a clustered deployment, you can configure reconciliation jobs to be distributed across multiple nodes in the cluster. Clustered reconciliation is configured *per mapping* and can improve reconciliation performance, particularly for very large data sets.

Clustered reconciliation uses the paged reconciliation mechanism and the scheduler service to divide the *source* data set into pages, and then to schedule reconciliation "sub-jobs" per page, distributing these sub-jobs across the nodes in the cluster.

Regular (non-clustered) reconciliation has two phases—a source phase and a target phase. Clustered reconciliation effectively has three phases:

* Source page phase

  During this phase, reconciliation sub-jobs are scheduled in succession, page by page. Each source page job does the following:

  * Executes a source query using the paging cookie from the invocation context.

  * Schedules the next source page job.

  * Performs the reconciliation of the source IDs returned by the query.

  * Writes statistics summary information which is aggregated so that you can obtain the status of the complete reconciliation run by performing a GET on the `recon` endpoint.

  * On completion, writes the `repo_id`, `source_id`, and `target_id` to the repository.

* Source phase completion check

  This phase is scheduled when the source query returns null. This check runs, and continues to reschedule itself, as long as source page jobs are running. When the completion check determines that all the source page jobs are complete, it schedules the target phase.

* Target phase

  This phase queries the target IDs, then removes all of the IDs that correspond to the `repo_id`, `source_id`, and `target_id` written by the source pages. The remaining target IDs are used to run the target phase, taking into account all records on the target system that were not correlated to a source ID during the source phase sub-jobs.

## Configure clustered reconciliation for a mapping

To specify that the reconciliation for a specific mapping should be distributed across a cluster, add the `clusteredSourceReconEnabled` property to the mapping and set it to `true`. For example:

```json
{
    "mappings" : [
        {
            "name" : "systemLdapAccounts_managedUser",
            "source" : "system/ldap/account",
            "target" : "managed/realm-name_user",
            "clusteredSourceReconEnabled" : true,
  ...
}
```

|   |                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When clustered reconciliation is enabled, source query paging is enabled automatically, regardless of the value that you set for the `reconSourceQueryPaging` property in the mapping. |

By default, the number of records per page is **10000**. You can also enable *target query paging* with the `reconTargetQueryPaging` property (defaults to `false`). To change the query page sizes, set the `reconSourceQueryPageSize` and `reconTargetQueryPageSize` properties.

The following example enables *target query paging* and changes the target and source query page sizes:

```json
{
      "mappings" : [
          {
              "name" : "systemLdapAccounts_managedUser",
              "source" : "system/ldap/account",
              "target" : "managed/realm-name_user",
              "clusteredSourceReconEnabled" : true,
              "reconTargetQueryPaging" : true,
              "reconSourceQueryPageSize" : 12000,
              "reconTargetQueryPageSize" : 12000,
          ...
}
```

To set these properties using the IDM admin console, click Configure > Mappings, select the mapping to change, and click the Advanced tab.

Clustered reconciliation has the following limitations:

* A complete non-clustered reconciliation run is synchronous with the single reconciliation invocation.

  By contrast, a clustered reconciliation is *asynchronous*. In a clustered reconciliation, the first execution is synchronous only with the reconciliation of the first page. This job also schedules the subsequent pages of the clustered reconciliation to run on other cluster nodes. When you schedule a clustered reconciliation or call the operation over REST, do not set `waitForCompletion` to `true`, because you cannot wait for the operation to complete before the next operation starts.

  Because this first execution does not encompass the entire reconciliation operation for that mapping, you cannot rely on the Quartz `concurrentExecution` property to prevent two reconciliation operations from running concurrently. If you use Quartz to schedule clustered reconciliations (as described in [Configure Scheduled Synchronization](chap-schedules.html#configuring-sync-schedule)), make sure that the interval between scheduled operations exceeds the known run of the entire clustered reconciliation. The run-length of a specific clustered reconciliation can vary. You must therefore build in appropriate buffer times between schedules, or use a scheduled script that performs a GET on the `recon/` endpoint, and dispatches the next reconciliation on a mapping only when the previous reconciliation run has completed.

* Clustered reconciliations can recover missing source pages (for example, if a cluster goes offline during a clustered reconciliation run), except when used with a connector using server-side logic to handle paging that returns a static paging cookie.

## Clustered reconciliation progress

The `sourceProcessedByNode` property indicates how many records are processed by each node. You can verify the load distribution per node by running a GET on the recon endpoint, for example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/recon"
...
    "started": "2017-05-11T10:04:59.563Z",
    "ended": "",
    "duration": 342237,
    "sourceProcessedByNode": {
        "node2": 21500,
        "node1": 22000
    }
}
```

You can also display the nodes responsible for each source page in the IDM admin console. Click on the relevant mapping and expand the In Progress or Reconciliation Results item. The following image shows a clustered reconciliation in progress. The details include the number of records that have been processed, the current duration of the reconciliation, and the load distribution, per node:

![clustered-recon](_images/clustered-recon.png)Figure 1. Clustered Reconciliation Results

## Cancel a clustered reconciliation

You cancel a clustered reconciliation in the same way as a non-clustered reconciliation, for example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/recon/90892122-5ceb-4bbe-86f7-94272df834ad-406025?_action=cancel"
{
  "_id": "90892122-5ceb-4bbe-86f7-94272df834ad-406025",
  "action": "cancel",
  "status": "INITIATED"
}
```

When the cancellation has completed, a query on that reconciliation ID will show the state and stage of the reconciliation as follows:

```json
{
   "_id": "90892122-5ceb-4bbe-86f7-94272df834ad-406025",
   "mapping": "systemLdapAccounts_managedUser",
   "state": "CANCELED",
   "stage": "COMPLETED_CANCELED",
   "stageDescription": "reconciliation aborted.",
   "progress": {
     "source": {
       "existing": {
         "processed": 23500,
         "total": "23500"
       }
     },
     "target": {
       "existing": {
         "processed": 23498,
         "total": "?"
     },
     ...
}
```

In a clustered environment, *all* reconciliation operations are considered to be "cluster-friendly". This means that even if a mapping is configured as `"clusteredSourceReconEnabled" : false`, you can view the in progress operation on *any* node in the cluster, even if that node is not currently processing the reconciliation. You can also cancel a reconciliation in progress from any node in the cluster.

---

---
title: Configure a resource mapping
description: Configure resource mappings between system and managed objects using UI
component: pingoneaic
page_id: pingoneaic:idm-synchronization:cfg-mapping-resource
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/cfg-mapping-resource.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Resource", "Mappings", "Configuration"]
section_ids:
  mappings-ui: Configure mappings using the IDM admin console
---

# Configure a resource mapping

Objects in external resources are specified in a mapping as `system/name/object-type`, where name is the name used in the connector configuration *(tooltip: You can create and change connector configurations over REST at the /openidm/config/provisioner.openicf/\<connector-name> endpoint.)*, and object-type is the object defined in the connector configuration *(tooltip: You can create and change connector configurations over REST at the /openidm/config/provisioner.openicf/\<connector-name> endpoint.)* list of object types. Objects in the repository are specified in the mapping as `managed/object-type`, where object-type is defined in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*.

External resources, and IDM managed objects, can be the *source* or the *target* in a mapping. By convention, the mapping name is a string of the form `source_target`, as shown in the following example:

> **Collapse: Basic LDAP Mapping**
>
> ```json
> {
>     "mappings": [
>         {
>             "name": "systemLdapAccounts_managedUser",
>             "source": "system/ldap/account",
>             "target": "managed/realm-name_user",
>             "properties": [
>                 {
>                     "source": "lastName",
>                     "target": "sn"
>                 },
>                 {
>                     "source": "telephoneNumber",
>                     "target": "telephoneNumber"
>                 },
>                 {
>                     "target": "phoneExtension",
>                     "default": "0047"
>                 },
>                 {
>                     "source": "email",
>                     "target": "mail",
>                     "comment": "Set mail if non-empty.",
>                     "condition": {
>                         "type": "text/javascript",
>                         "source": "(object.email != null)"
>                     }
>                 },
>                 {
>                     "source": "",
>                     "target": "displayName",
>                     "transform": {
>                         "type": "text/javascript",
>                         "source": "source.lastName +', ' + source.firstName;"
>                     }
>                 },
>                {
>                     "source" : "uid",
>                     "target" : "userName",
>                     "condition" : "/linkQualifier eq \"user\""
>                     }
>                },
>             ]
>         }
>     ]
> }
> ```

In this example, the name of the source is the external resource (`ldap`), and the target is IDM's user repository; specifically, `managed/realm-name_user`. The `properties` defined in the mapping correspond to attribute names that are defined in the IDM configuration. For example, the source attribute `uid` is defined in the `ldap` connector configuration file, rather than on the external resource itself.

## Configure mappings using the IDM admin console

To set up a synchronization mapping using the IDM admin console:

1. From the IDM console, click Native Consoles > Identity Management.

2. From the navigation bar in the IDM admin console, click Configure > Mappings.

3. Click New Mapping.

4. On the New Mapping page, select a source and target resource from the configured resources at the bottom of the window, and click Create Mapping.

   You can filter these resources to display only connector configurations or managed objects.

5. Select Add property on the Attributes grid to map a target property to its corresponding source property.

   The Property list shows all configured properties on the target resource. If the target resource is specified in a connector configuration, the Property list shows all properties configured for this connector. If the target resource is a managed object, the Property list shows the list of properties (defined in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)* for that object).

   |   |                                                                                                                                                                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * Select Add Missing Required Properties to add all the properties that are configured as *required* on the target resource. You can then map these required properties individually.

   * Select Quick Mapping to show all source and target properties simultaneously. Drag a source property onto its corresponding target property, or vice versa. When you're done, click Save. |

6. To test your mapping configuration on a single source entry, click the Behaviors tab and scroll down to Single Record Reconciliation. Search for the entry to reconcile.

   The UI displays a preview of the target entry after a reconciliation. You can then click Reconcile Selected Record to perform the reconciliation on that one source entry.

---

---
title: Connections between resources
description: Configure connectors to transfer data between different resource systems
component: pingoneaic
page_id: pingoneaic:idm-synchronization:sync-connections
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/sync-connections.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Connectors"]
section_ids:
  connector-config-adminui: Configure connectors using the IDM admin console
  connector-config-over-rest: Configure connectors using REST
---

# Connections between resources

A connector lets you transfer data between different resource systems. The connector configuration works in conjunction with the [synchronization mapping](mappings.html) and specifies how target object attributes map to attributes on external objects.

To create and modify connector configurations, use one of the following methods:

## Configure connectors using the IDM admin console

1. From the IDM console, click Native Consoles > Identity Management.

2. From the navigation bar, click Configure > Connectors, and do one of the following.

   * Select an existing connector to modify.

   * Click New Connector, and configure the new connector.

## Configure connectors using REST

Create connector configurations using REST with the `createCoreConfig` and `createFullConfig` actions. For more information, see [Configure Connectors Using REST](https://docs.pingidentity.com/openicf/connector-reference/configure-connector.html#connector-wiz-REST).

---

---
title: Correlate source objects with existing target objects
description: Correlate source and target objects using queries or scripts before synchronization
component: pingoneaic
page_id: pingoneaic:idm-synchronization:chap-correlation
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/chap-correlation.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Mappings"]
section_ids:
  correlation-ui: Configure correlation using the IDM admin console
  correlation-queries-configuring: Correlation queries
  correlation-filtered-queries: Use filtered queries to correlate objects
  correlation-expression-builder: Create correlation queries using the expression builder
  correlation-scripts: Correlation scripts
  correlation-script-link-qual: Correlation script using link qualifiers
  correlation-script-ui: Configure a correlation script using the IDM admin console
---

# Correlate source objects with existing target objects

When a synchronization operation creates an object on a target system, it also creates a *link* between the source and target object. IDM then uses that link to determine the object's *synchronization situation* during later synchronization operations. For a list of synchronization situations, refer to [How Advanced Identity Cloud assesses synchronization situations](sync-situations.html).

Every synchronization operation can *correlate* existing source and target objects. Correlation matches source and target objects, based on the results of a query or script, and creates links between matched objects.

Correlation queries and correlation scripts are configured as part of the mapping. Each query or script is specific to the mapping for which it is configured.

## Configure correlation using the IDM admin console

1. From the IDM console, click Native Consoles > Identity Management.

2. From the navigation bar, click Configure > Mappings.

3. From the Mappings page, click the mapping to correlate.

4. From the Mapping Detail page, click the Association tab.

5. Expand the Association Rules tab, click the drop-down menu, and select one of the following:

   * Correlation Queries

   * Correlation Script

6. Build and/or write your script or query, and click Save.

## Correlation queries

IDM processes a correlation query by constructing a query map. The content of the query is generated dynamically, using values from the source object. For each source object, a new query is sent to the target system, using (possibly transformed) values from the source object for its execution.

Queries are run against *target resources*, either managed or system objects, depending on the mapping. Correlation queries on system objects access the connector, which executes the query on the external resource.

You express a correlation query using a query filter (`_queryFilter`). For more information about query filters, refer to [Define and call data queries](../idm-objects/queries.html). The synchronization process executes the correlation query to search through the target system for objects that match the current source object.

To configure a correlation query, define a script whose source returns a query that uses the `_queryFilter`, for example:

```json
{ "_queryFilter" : "uid eq \"" + source.userName + "\"" }
```

### Use filtered queries to correlate objects

For filtered queries, the script that is defined or referenced in the `correlationQuery` property must return an object with the following elements:

* The element that is being compared on the target object; for example, `uid`.

  The element on the target object is not necessarily a single attribute. Your query filter can be simple or complex; valid query filters range from a single operator to an entire boolean expression tree.

  If the target object is a system object, this attribute must be referred to by its IDM name rather than its ICF `nativeName`. For example, with the following provisioner configuration, the attribute to use in the correlation query would be `uid` and not `` +NAME` ``:

  ```json
  ...
      "uid" : {
          "type" : "string",
          "nativeName" : "__NAME__",
          "required" : true,
          "nativeType" : "string"
      }
  ...
  ```

* The value to search for in the query.

  This value is generally based on one or more values from the source object. However, it does not have to match the value of a single source object property. You can define how your script uses the values from the source object to find a matching record in the target system.

  You might use a transformation of a source object property, such as `toUpperCase()`. You can concatenate that output with other strings or properties. You can also use this value to call an external REST endpoint, and redirect the response to the final "value" portion of the query.

The following correlation query matches source and target objects if the value of the `uid` attribute on the target is the same as the `userName` attribute on the source:

```json
"correlationQuery" : {
    "type" : "text/javascript",
    "source" : "var qry = {'_queryFilter': 'uid eq \"' + source.userName + '\"'}; qry"
},
```

The query can return zero or more objects. The situation assigned to the source object depends on the number of target objects that are returned, and on the presence of any *link qualifiers* in the query. For information about synchronization situations, refer to [How Synchronization Situations Are Assessed](chap-situations-actions.html). For information about link qualifiers, refer to [Map a Single Source Object to Multiple Target Objects](linking-multiple-targets.html).

### Create correlation queries using the expression builder

The *Expression Builder* is a wizard that lets you quickly build expressions using drop-down menu options.

1. From the IDM console, click Native Consoles > Identity Management.

2. From the navigation bar, click Configure > Mappings.

3. On the Mappings page, click the mapping to correlate.

4. From the Mapping Detail page, click the Association tab.

5. Expand the Association Rules tab, click the drop-down menu, and select Correlation Queries.

6. Click Add Correlation Query.

7. In the Correlation Query window, click the Link Qualifier drop-down menu, and select a link qualifier.

   If you do not need to correlate multiple potential target objects per source object, select the default link qualifier. For more information about linking to multiple target objects, refer to [Map a Single Source Object to Multiple Target Objects](linking-multiple-targets.html).

8. Select Expression Builder.

9. To create an expression, use the drop-down menus to add and remove items, as necessary. List the fields to use for matching existing items in your source to items in your target.

   The following example displays an Expression Builder correlation query for a mapping from `managed/realm-name_user` to `system/ldap/accounts` objects. The query creates a match between the source (managed) object and the target (LDAP) object if the value of the `givenName` or the `telephoneNumber` of those objects is the same.

   ![expression-builder](_images/expression-builder.png)

10. After you finish building the expression, click Submit.

11. On the Mapping Detail page, under the Association Rules tab, click Save.

The correlation query displays as follows in the mapping:

```json
"correlationQuery" : [
    {
        "linkQualifier" : "default",
        "expressionTree" : {
            "any" : [
                "givenName",
                "telephoneNumber"
            ]
        },
        "mapping" : "managedUser_systemLdapAccounts",
        "type" : "text/javascript",
        "file" : "ui/correlateTreeToQueryFilter.js"
    }
]
```

## Correlation scripts

In general, a correlation query should meet the requirements of most deployments. However, if you need a more powerful correlation mechanism than a simple query can provide, you can write a correlation script with additional logic. Correlation scripts can be useful if your query needs extra processing, such as fuzzy-logic matching or out-of-band verification with a third-party service over REST. Correlation scripts are generally more complex than correlation queries, and impose no restrictions on the methods used to find matching objects.

A correlation script must execute a query and return the result of that query. The result of a correlation script is a list of maps, each of which contains a candidate `_id` value. If no match is found, the script returns a zero-length list. If exactly one match is found, the script returns a single-element list. If there are multiple ambiguous matches, the script returns a list with multiple elements. There is no assumption that the matching target record or records can be found by a simple query on the target system. All of the work required to find matching records is left to the script.

To invoke a correlation script, use one of the following properties:

* `correlationQuery`

  Returns a `Map` whose values specify the `QueryFilter` for the sync engine to execute.

* `correlationScript`

  Returns a `List<Map>` whose value is a list of correlated objects from the target.

  You can invoke a correlation script inline:

  ```json
  "correlationScript" : {
      "type": "text/javascript",
      "source": " var resultData = openidm.query("system/ldap/account", myQuery); return resultData.result;"
  }
  ```

### Correlation script using link qualifiers

The following example shows a correlation script that uses link qualifiers. The script returns `resultData.result`—a list of maps, each of which has an `_id` entry. These entries will be the values that are used for correlation.

```javascript
(function () {
    var query, resultData;
    switch (linkQualifier) {
        case "test":
            logger.info("linkQualifier = test");
	        query = {'_queryFilter': 'uid eq \"' + source.userName + '-test\"'};
            break;
        case "user":
            logger.info("linkQualifier = user");
	        query = {'_queryFilter': 'uid eq \"' + source.userName + '\"'};
            break;
        case "default":
            logger.info("linkQualifier = default");
	        query = {'_queryFilter': 'uid eq \"' + source.userName + '\"'};
            break;
        default:
            logger.info("No linkQualifier provided.");
	        break;
    }
    var resultData = openidm.query("system/ldap/account", query);
    logger.info("found " + resultData.result.length + " results for link qualifier " + linkQualifier)
    for (i=0;i<resultData.result.length;i++) {
        logger.info("found target: " + resultData.result[i]._id);
    }
    return resultData.result;
} ());
```

### Configure a correlation script using the IDM admin console

1. From the IDM console, click Native Consoles > Identity Management.

2. From the navigation bar, click Configure > Mappings.

3. On the Mappings page, select the mapping to correlate.

4. From the Mapping Detail page, click the Association tab.

5. Expand the Association Rules node, click the drop-down menu, and select Correlation Script.

6. Enter the correlation script:

   * To use an inline script, select Inline Script, and type the script source.

     |   |                                                                                                                                                                                                                                                                                                                                                                         |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | To create a correlation script, use the details from the source object to find the matching record in the target system. If you are using link qualifiers to match a single source record to multiple target records, you must also use the value of the `linkQualifier` variable within your correlation script to find the target ID that applies for that qualifier. |

7. Click Save.

---

---
title: Data mapping model
description: Choose meta-directory or virtual data model for identity data synchronization
component: pingoneaic
page_id: pingoneaic:idm-synchronization:sync-data-model
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/sync-data-model.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Data model", "Mapping"]
---

# Data mapping model

IDM uses mappings to determine which data to synchronize, and how that data must be synchronized.

In general, identity management software implements one of the following data models:

* A meta-directory data model, where all data is mirrored in a central repository.

  The meta-directory model offers fast access at the risk of getting outdated data.

* A virtual data model, where only a minimum set of attributes are stored centrally, and most are loaded on demand from the external resources in which they are stored.

  The virtual model guarantees fresh data, but pays for that guarantee in terms of performance.

IDM leaves the data model choice up to you. You determine the right trade-offs for a particular deployment. IDM does not hard code any particular schema or set of attributes stored in the repository. Instead, you define how external system objects map onto managed objects, and IDM dynamically updates the repository to store the managed object attributes that you configure.

---

---
title: Default attribute values in a mapping
description: Set default values for target object attributes in mappings
component: pingoneaic
page_id: pingoneaic:idm-synchronization:mapping-default-attributes
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/mapping-default-attributes.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization", "Attributes", "Mappings"]
section_ids:
  default-values-ui: Configure default attribute values using the IDM admin console
---

# Default attribute values in a mapping

You can use a mapping to *create* attributes on the target resource. The following mapping excerpt creates a `phoneExtension` attribute with a default value of `0047` on the target object:

```json
{
    "target": "phoneExtension",
    "default": "0047"
},
```

The `default` property specifies a value to assign to the attribute on the target object. Before IDM determines the value of the target attribute, it evaluates any applicable conditions, followed by any transformation scripts. If the `source` property and the `transform` script yield a null value, IDM applies the default value in the create and update actions. The default value overrides the target value, if one exists.

## Configure default attribute values using the IDM admin console

1. From the IDM console, click Native Consoles > Identity Management.

2. From the navigation bar, click Configure > Mappings, and click the mapping to edit.

3. Click the Properties tab.

4. Expand the Attributes Grid node, and click the Target property to edit.

5. In the Target Property: name window, click the Default Values tab, and add or edit the default values.

6. Click Save.

   The default value displays in the Attributes Grid.

   ![Default Value displayed in the Attributes Grid](_images/defaultValueUI.png)

---

---
title: Enhance implicit sync and liveSync
description: Configure automatic synchronization through implicit sync and liveSync with retry policies
component: pingoneaic
page_id: pingoneaic:idm-synchronization:chap-implicit-live-sync
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-synchronization/chap-implicit-live-sync.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Synchronization"]
section_ids:
  array-comparison: Array comparison
  disabling-automatic-sync: Disable automatic synchronization operations
  livesync-retry-strategy: Configure the liveSync retry policy
  queued-sync: Improve reliability with queued synchronization
  configure-queued-sync: Configure queued synchronization
  tuning-queued-sync: Tune queued synchronization
  queued-sync-over-rest: Manage the synchronization queue
  queued-sync-recovery: Recover mappings when nodes are down
  queued-sync-balancing: Balance mapping locks across nodes
  sync-failure-compensation: Synchronization failure compensation
---

# Enhance implicit sync and liveSync

You can propagate changes to and from Advanced Identity Cloud and external systems through *implicit synchronization* and *liveSync*. These refer to the automatic synchronization of changes from and to the managed objects (such as users or roles) repository. For more information, refer to [Synchronization types](sync-types.html).

The following topics describe the mechanisms for configuring these automatic synchronization mechanisms.

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you modify sync configuration settings, mappings and connectors must be configured. For more information, refer to [resource mappings](mappings.html) and [sync connectors](sync-connections.html#connector-config-adminui). |

## Array comparison

You can choose how synchronization detects managed object array changes using *unordered* or *ordered* comparison using the configuration property `comparison` in the schema. Unordered JSON array comparison ignores the order of elements and can negate the need for certain custom scripts within mappings.

Relationship and virtual property array fields default to unordered comparisons. All other fields default to ordered comparisons.

Learn more about [managed object schema properties](../idm-objects/appendix-managed-objects.html#managed-object-property-config-properties).

## Disable automatic synchronization operations

By default, all mappings are automatically synchronized. A change to a managed object is automatically synchronized to all resources for which the managed object is configured as a source. If liveSync is enabled for a system, changes to an object on that system are automatically propagated to the managed object repository.

To prevent automatic synchronization for a specific mapping, set the `enableSync` property of that mapping to false. In the following example, implicit synchronization is disabled. This means that changes to objects in the internal repository are not automatically propagated to the LDAP directory. To propagate changes to the LDAP directory, reconciliation must be launched manually:

```json
{
  "mappings" : [
    {
      "name" : "managedUser_systemLdapAccounts",
      "source" : "managed/realm-name_user",
      "target" : "system/ldap/account",
      "enableSync" : false,
      ...
}
```

If `enableSync` is set to `false` for a mapping from a system resource to managed/realm-name\_user (for example `"systemLdapAccounts_managedUser"`), liveSync is disabled for that mapping.

|   |                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To disable automatic synchronization from the IDM admin console:1) From the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2) Click Configure > Mappings.

3) Select the mapping to disable liveSync for.

4) Click the Advanced tab and de-select the Enable Automatic Synchronization option. |

## Configure the liveSync retry policy

If a liveSync operation fails, IDM reattempts the change an infinite number of times until the change is successful. This behavior can increase data consistency in the case of transient failures (for example, when the connection to the database is temporarily lost). However, in situations where the cause of the failure is permanent (for example, if the change does not meet certain policy requirements) the change will never succeed, regardless of the number of attempts. In this case, the infinite retry behavior can effectively block subsequent liveSync operations from starting.

To avoid this, you can configure a liveSync retry policy to specify the number of times a failed modification should be reattempted, and what should happen if the modification is unsuccessful after the specified number of attempts.

Ultimately, a scheduled reconciliation operation forces consistency; however, to prevent repeated retries that block liveSync, restrict the number of times you attempt the same modification. You can then specify what happens to failed liveSync changes.

The failed modification can be stored in a *dead letter queue* , discarded, or reapplied. Alternatively, an administrator can be notified of the failure by email or by some other means. This behavior can be scripted. The default configuration in the samples provided with IDM is to retry a failed modification five times, and then to log and ignore the failure.

You configure the liveSync retry policy in the [connector configuration](https://docs.pingidentity.com/openicf/connector-reference/configure-connector.html). The sample connector configurations have a retry policy defined as follows:

```json
"syncFailureHandler" : {
  "maxRetries" : 5,
  "postRetryAction" : "logged-ignore"
},
```

* `maxRetries`

  Specifies the number of attempts that IDM should make to process the failed modification.

  The value of this property must be a positive integer, or `-1`. A value of zero indicates that failed modifications should not be reattempted. In this case, the post-retry action is executed immediately when a liveSync operation fails. A value of `-1` (or omitting the `maxRetries` property, or the entire `syncFailureHandler` from the configuration) indicates that failed modifications should be retried an infinite number of times. In this case, no post retry action is executed.

  The default retry policy relies on the scheduler, or whatever invokes liveSync. Therefore, if retries are enabled and a liveSync modification fails, IDM will retry the modification the next time that liveSync is invoked.

* `postRetryAction`

  Indicates what should happen if the maximum number of retries has been reached (or if `maxRetries` has been set to zero). The post-retry action can be one of the following:

  * `logged-ignore`

    IDM should ignore the failed modification, and log its occurrence.

  * `dead-letter-queue`

    IDM should save the details of the failed modification in a table in the repository (accessible over REST at `repo/synchronisation/deadLetterQueue/provisioner-name`).

  * `script`

    Specifies a custom script that should be executed when the maximum number of retries has been reached. For information about using custom scripts in the configuration, refer to [scripting functions](../idm-scripting/scripting-func-engine.html). In addition to the regular objects described in that section, the following objects are available in the script scope:

    * `syncFailure`

      Provides details about the failed record. The structure of the `syncFailure` object is as follows:

      ```json
      "syncFailure" :
        {
          "token" : the ID of the token,
          "systemIdentifier" : a string identifier that matches the "name" property in the connector configuration,
          "objectType" : the object type being synced, one of the keys in the "objectTypes" property in the connector configuration,
          "uid" : the UID of the object (for example uid=joe,ou=People,dc=example,dc=com),
          "failedRecord", the record that failed to synchronize
        },
      ```

      To access these fields, include `syncFailure.fieldname` in your script.

    * `failureCause`

      Provides the exception that caused the original liveSync failure.

    * `failureHandlers`

      Two synchronization failure handlers are provided by default:

      * `loggedIgnore` indicates that the failure should be logged, after which no further action should be taken.

      * `deadLetterQueue` indicates that the failed record should be written to a specific table in the repository, where further action can be taken.

  |   |                                                                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To invoke one of the internal failure handlers from your script, use a call similar to the following (shown here for JavaScript):```none
  failureHandlers.deadLetterQueue.invoke(syncFailure, failureCause);
  ``` |

The following liveSync retry policy configuration specifies a maximum of four retries before the failed modification is sent to the dead letter queue:

```json
...
    "syncFailureHandler" : {
        "maxRetries" : 4,
        "postRetryAction" : dead-letter-queue
    },
...
```

In the case of a failed modification, a message similar to the following is output to the logs:

```
INFO: sync retries = 1/4, retrying
```

IDM reattempts the modification the specified number of times. If the modification is still unsuccessful, a message similar to the following is logged:

```none
INFO: sync retries = 4/4, retries exhausted
Jul 19, 2013 11:59:30 AM
    org.forgerock.openidm.provisioner.openicf.syncfailure.DeadLetterQueueHandler invoke
INFO: uid=jdoe,ou=people,dc=example,dc=com saved to dead letter queue
```

The log message indicates the entry for which the modification failed (`uid=jdoe`, in this example).

You can view the failed modification in the dead letter queue, over the REST interface, as follows:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/repo/synchronisation/deadLetterQueue/ldap?_queryFilter=true&_fields=_id"
{
  "result":
    [
      {
        "_id": "4",
        "_rev": "000000001298f6a6"
      }
    ],
  ...
}
```

To view the details of a specific failed modification, include its ID in the URL:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/repo/synchronisation/deadLetterQueue/ldap/4"
{
  "objectType": "account",
  "systemIdentifier": "ldap",
  "failureCause": "org.forgerock.openidm.sync.SynchronizationException:
            org.forgerock.openidm.objset.ConflictException:
            org.forgerock.openidm.sync.SynchronizationException:
            org.forgerock.openidm.script.ScriptException:
            ReferenceError: \"bad\" is not defined.
            (PropertyMapping/mappings/0/properties/3/condition#1)",
  "token": 4,
  "failedRecord": "complete record, in xml format"
  "uid": "uid=jdoe,ou=people,dc=example,dc=com",
  "_rev": "000000001298f6a6",
  "_id": "4"
}
```

|   |                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `repo` endpoint is an *internal interface*. Although it is used in the preceding example for the purposes of demonstration, you should not rely on this endpoint in production. |

## Improve reliability with queued synchronization

By default, IDM implicitly synchronizes managed object changes out to all resources for which the managed object is configured as a source. If there are several targets that must be synchronized, these targets are synchronized one at a time, one after the other. If any of the targets is remote or has a high latency, the implicit synchronization operations can take some time, delaying the successful return of the managed object change.

To decouple the managed object changes from the corresponding synchronizations, you can configure *queued synchronization*, which persists implicit synchronization events to the IDM repository. Queued events are then read from the repository and executed according to the queued synchronization configuration.

Because synchronization operations are performed in parallel, queued synchronization can improve performance if you have several fast, reliable targets. However, queued synchronization is also useful when your targets are slow or unreliable, because the managed object changes can complete before all targets have been synchronized.

The following illustration shows how synchronization operations are added to a local, in-memory queue. Note that this queue is distinct from the repository queue for synchronization events:

![Image shows how synchronization events are added to an in-memory queue.](_images/queued-sync.png)Figure 1. Queued Synchronization

### Configure queued synchronization

Queued synchronization is disabled by default. To enable it, add a `queuedSync` object to your mapping, as follows:

```json
{
  "mappings" : [
    {
      "name" : "managedUser_systemLdapAccounts",
      "source" : "managed/realm-name_user",
      "target" : "system/ldap/account",
      "links" : "systemLdapAccounts_managedUser",
      "queuedSync" : {
        "enabled" : true,
        "pageSize" : 100,
        "pollingInterval" : 1000,
        "maxQueueSize" : 1000,
        "maxRetries" : 5,
        "retryDelay" : 1000,
        "postRetryAction" : "logged-ignore"
      },
      ...
    }
  ]
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * These settings apply *only* to the implicit synchronization operations for that mapping. Reconciliation is unaffected by queued synchronization settings. Events associated with mappings where queued synchronization is enabled are submitted to the synchronization queue for asynchronous processing. Events associated with mappings where queued synchronization is not enabled are processed immediately, and block further event processing until they are complete.

* During implicit synchronization, mappings are processed in the order in which they are defined, regardless of whether queued synchronization is enabled for those mappings. If you want all queued synchronization mappings to be processed first, you must explicitly order your mappings accordingly.

* Processing the synchronization queue for a mapping is *paused* if either the source or target system route is *unregistered*. A route is unregistered when you remove the connector configuration *(tooltip: You can create and change connector configurations over REST at the /openidm/config/provisioner.openicf/\<connector-name> endpoint.)*, set `"enabled" : false` in the connector configuration *(tooltip: You can create and change connector configurations over REST at the /openidm/config/provisioner.openicf/\<connector-name> endpoint.)*, delete the mapping, or remove the managed object type from the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*. |

The `queuedSync` object has the following configuration:

* `enabled`

  Specifies whether queued synchronization is enabled for that mapping. Boolean, `true`, or `false`.

* `pageSize` (integer)

  Specifies the maximum number of events to retrieve from the repository queue within a single polling interval. You can't set this higher than `100` or lower than `10`. If the configured `pageSize` is greater than `maxQueueSize / 10`, Advanced Identity Cloud uses `maxQueueSize / 10` for the page size. The default is `100` events.

* `pollingInterval` (integer)

  Specifies the repository queue polling interval, in milliseconds. The default is `1000` ms.

* `maxQueueSize` (integer)

  Specifies the maximum number of synchronization events that can be accepted into the in-memory queue. You can't set this higher than `1000` or lower than `100`. The default is `1000` events.

* `maxRetries` (integer)

  The number of retries to perform before invoking the `postRetry` action. Most sample configurations set the maximum number of retries to `5`. To set an infinite number of retries, either omit the `maxRetries` property, or set it to a negative value, such as `-1`.

* `retryDelay` (integer)

  In the event of a failed queued synchronization operation, this parameter specifies the number of milliseconds to delay before attempting the operation again. The default is `1000` ms.

* `postRetryAction`

  The action to perform after the retries have been exhausted. Possible options are `logged-ignore`, `dead-letter-queue`, and `script`. These options are described in [Configure the LiveSync Retry Policy](#livesync-retry-strategy). The default action is `logged-ignore`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Retries occur synchronously to the failure. For example, if the `maxRetries` is set to `10`, at least 10 seconds will pass between the failing sync event and the next sync. (There are 10 retries, and the `retryDelay` is 1 second by default.) These 10 seconds do not take into account the latency of the ten sync requests. Retries are configured per-mapping and block processing of all subsequent sync events until the configured retries have been exhausted. |

### Tune queued synchronization

Queued synchronization employs a single worker thread. While implicit synchronization operations are being generated, that worker thread should always be occupied. The occupation of the worker thread is a function of the `pageSize`, the `pollingInterval`, the latency of the poll request, and the latency of each synchronization operation for the mapping.

For example, assume that a poll takes 500 milliseconds to complete. Your system must provide operations to the worker thread at approximately the same rate at which the thread can consume events (based on the page size, poll frequency, and poll latency). Operation consumption is a function of the `notifyaction.execution` for that particular mapping. If the system does not provide operations fast enough, implicit synchronization won't occur as optimally as it could. If the system provides operations too quickly, the operations in the queue could exceed the default maximum of `1000`. If the `maxQueueSize` is reached, additional synchronization events result in a `RejectedExecutionException`.

Depending on your hardware and workload, you might need to adjust the default `pageSize`, `pollingInterval`, and `maxQueueSize`.

Monitor the queued synchronization metrics; specifically, the `rejected-executions`, and adjust the `maxQueueSize` accordingly. Set a large enough `maxQueueSize` to prevent slow mappings and heavy loads from causing newly-submitted synchronization events to be rejected.

Monitor the synchronization latency using the `sync.queue.mapping-name.poll-pending-events` metric.

### Manage the synchronization queue

You can manage queued synchronization events over the REST interface, at the `openidm/sync/queue` endpoint. The following examples show the operations that are supported on this endpoint:

List all events in the synchronization queue:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/sync/queue?_queryFilter=true"
{
  "result": [
    {
      "_id": "03e6ab3b-9e5f-43ac-a7a7-a889c5556955",
      "_rev": "0000000034dba395",
      "mapping": "managedUser_systemLdapAccounts",
      "resourceId": "e6533cfe-81ad-4fe8-8104-55e17bd9a1a9",
      "syncAction": "notifyCreate",
      "state": "PENDING",
      "resourceCollection": "managed/realm-name_user",
      "nodeId": null,
      "createDate": "2018-11-12T07:45:00.072Z"
    },
    {
      "_id": "ed940f4b-ce80-4a7f-9690-1ad33ad309e6",
      "_rev": "000000007878a376",
      "mapping": "managedUser_systemLdapAccounts",
      "resourceId": "28b1bd90-f647-4ba9-8722-b51319f68613",
      "syncAction": "notifyCreate",
      "state": "PENDING",
      "resourceCollection": "managed/realm-name_user",
      "nodeId": null,
      "createDate": "2018-11-12T07:45:00.150Z"
    },
    {
      "_id": "f5af2eed-d83f-4b70-8001-8bc86075134f",
      "_rev": "00000000099aa321",
      "mapping": "managedUser_systemLdapAccounts",
      "resourceId": "d2691a45-0a10-4f51-aa2a-b6854b2f8086",
      "syncAction": "notifyCreate",
      "state": "PENDING",
      "resourceCollection": "managed/realm-name_user",
      "nodeId": null,
      "createDate": "2018-11-12T07:45:00.276Z"
    },
    ...
  ],
  "resultCount": 8,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

Query the queued synchronization events based on the following properties:

* `mapping`—the mapping associated with this event. For example:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --request GET \
  "https://<tenant-env-fqdn>/openidm/sync/queue?_queryFilter=mapping+eq+'managedUser_systemLdapAccount'"
  ```

* `nodeId`—the ID of the node that has acquired this event.

* `resourceId`—the source object resource ID.

* `resourceCollection`—the source object resource collection.

* `_id`—the ID of this sync event.

* `state`—the state of the synchronization event. For example:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --request GET \
  "https://<tenant-env-fqdn>/openidm/sync/queue?_queryFilter=state+eq+'PENDING'"
  ```

  The `state` of a queued synchronization event is one of the following:

  `PENDING`—the event is waiting to be processed.\
  `ACQUIRED`—the event is being processed by a node.

* `remainingRetries`—the number of retries available for this synchronization event before it is abandoned. For more information about how synchronization events are retried, refer to [Configure the LiveSync Retry Policy](#livesync-retry-strategy). For example:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --request GET \
  "https://<tenant-env-fqdn>/openidm/sync/queue?_queryFilter=remainingRetries+lt+2"
  ```

* `syncAction`—the synchronization action that initiated this event. Possible synchronization actions are `notifyCreate`, `notifyUpdate`, and `notifyDelete`. For example:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --request GET \
  "https://<tenant-env-fqdn>/openidm/sync/queue?_queryFilter=syncAction+eq+'notifyCreate'"
  ```

* `createDate`—the date that the event was created.

### Recover mappings when nodes are down

Synchronization events for mappings with queued synchronization enabled are processed by a single cluster node. While a node is present in the cluster, that node holds a *lock* on the specific mapping. The node can release or reacquire the mapping lock if a balancing event occurs (refer to [Balance Mapping Locks Across Nodes](#queued-sync-balancing)). However, the mapping lock is held across all events on that mapping. In a stable running cluster, a single node will hold the lock for a mapping indefinitely.

It is possible a node goes down or is removed from the cluster while holding a mapping lock on operations in the synchronization queue. To prevent these operations from being lost, the queued synchronization facility includes a *recovery monitor* that checks for any *orphaned* mappings in the cluster.

A mapping is considered orphaned in the following cases:

* No active node holds a lock on the mapping.

* The node that holds a lock on the mapping has an instance state of `STATE_DOWN`.

* The node that holds a lock on the mapping does not exist in the cluster.

The recovery monitor periodically checks for orphaned mappings. When all orphaned mappings are recovered, it attempts to initialize new queue consumers.

The recovery monitor is enabled by default and executes every 300 seconds. To change the default behavior for a [mapping](mappings.html), add the following to the mapping configuration and change the parameters as required:

```json
{
    "mappings" : [...],
    "queueRecovery" : {
        "enabled" : true,
        "recoveryInterval" : 300
    }
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If a queued synchronization job has already been claimed by a node, and that node is *shut down*, IDM notifies the entire cluster of the shutdown. This lets a different node pick up the job in progress. The recovery monitor takes over jobs in a synchronization queue that have not been fully processed by an available cluster node, so no job should be lost. If you have configured queued synchronization for one or more mappings, do not use the `enabled` flag in the cluster configuration to remove a node from the cluster. |

### Balance mapping locks across nodes

Queued synchronization mapping locks are balanced equitably across cluster nodes. At a specified interval, each node attempts to release and acquire mapping locks based on the number of running cluster nodes. When new cluster nodes come online, existing nodes release sufficient mapping locks for new nodes to pick them up, resulting in an equitable distribution of locks.

Lock balancing is enabled by default, and the interval at which nodes attempt to balance locks in the queue is five seconds. To change the default configuration, add a `queueBalancing` object to your [mapping](mappings.html) and set the following parameters:

```json
{
    "mappings" : [...],
    "queueBalancing" : {
        "enabled" : true,
        "balanceInterval" : 5
    }
}
```

## Synchronization failure compensation

|   |                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | It is recommended that you first attempt to [Improve reliability with queued synchronization](#queued-sync) before you configure synchronization failure compensation. |

If implicit synchronization fails for a target resource (for example, due to a policy validation failure on the target or the target being unavailable), the synchronization operation stops at that point. In this scenario, a record might be changed in the repository and in the targets on which synchronization was successful but not on the failed target or on any targets that would have been synchronized *after* the failure. This can result in disparate data sets across resources. Although a reconciliation operation would bring all targets back in sync, reconciliation can be expensive with large data sets.

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If synchronization failure compensation is not accounted for, any issues with connections to an external resource can result in out-of-sync data stores. |

You can configure *synchronization failure compensation* to:

* Prevent data sets from becoming out of sync by reverting the implicit synchronization operation if it is not completely successful across all configured mappings.

* Ensure all resources are synchronized successfully or that the original change is rolled back. This mechanism uses an `onSync` script hook in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*.

  The `onSync` hook calls a script that prevents partial synchronization by reverting a partial change in the event that all resources are not synchronized.

> **Collapse: Synchronization failure  inline script**
>
> ```js
> (function() {
>     var _ = require("lib/lodash.js");
>
>     if (syncResults.success) {
>         logger.debug("sync was a success; no compensation necessary");
>         return;
>     }
>
>     if (request !== null
>             && request.additionalParameters !== null
>             && request.additionalParameters.compensating === "true") {
>         logger.debug("already compensating, returning");
>         return;
>     }
>
>     logger.debug("compensating for " + resourceName);
>
>     var params = { "compensating" : true };
>     switch (syncResults.action) {
>         case "notifyCreate":
>             try {
>                 openidm.delete(resourceName.toString(), newObject._rev, params);
>             } catch (e) {
>                 logger.warn("Was not able to delete {} from compensation script. Exception: {}", resourceName.toString(), e);
>             }
>             break;
>         case "notifyUpdate":
>             try {
>                 openidm.update(resourceName.toString(), newObject._rev, oldObject, params);
>             } catch (e) {
>                 logger.warn("Was not able to update {} from compensation script. Exception: {}", resourceName.toString(), e);
>             }
>             break;
>         case "notifyDelete":
>             try {
>                 openidm.create(resourceName.parent().toString(), resourceName.leaf().toString(), oldObject, params);
>             } catch (e) {
>                 logger.warn("Was not able to create {} from compensation script. Exception: {}", resourceName.toString(), e);
>             }
>             break;
>     }
>     logger.debug(resourceName + " sync failure compensation complete");
>
>     // throw the error that caused the sync failure
>     var firstFailure = _.find(syncResults.syncDetails,
>             function (r) {
>                 return r.result === "FAILED" && r.cause !== undefined;
>             });
>
>     if (firstFailure !== null) {
>           throw firstFailure.cause;
>     }
>
> }());
> ```

With this script:

* A change to a managed object triggers an implicit synchronization for each configured [mapping](mappings.html), in the order in which the mappings are defined. If synchronization is successful for all configured mappings, IDM exits from the script.

  If synchronization fails for a particular resource, the `onSync` hook invokes inline script. script, which attempts to revert the original change by performing another update to the managed object. This change triggers another implicit synchronization operation to all external resources for which mappings are configured.

* If the synchronization operation fails again, the script is triggered a second time. This time, however, the script recognizes that the change was originally called as a result of a compensation and aborts. IDM logs warning messages related to the sync action (`notifyCreate`, `notifyUpdate`, `notifyDelete`), along with the error that caused the sync failure.

* Any such errors result in each data store retaining the information it had before implicit synchronization started. This information is stored temporarily in the `oldObject` variable.

---

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
  restricting-recons-ui: Restrict reconciliation queries using the IDM admin console
  recon-by-id: Restrict reconciliation to a specific ID
  restricting-implicit-sync: Restrict implicit synchronization to specific property changes
---

# Filter synchronization data

By default, IDM synchronizes all objects that match those defined in the connector configuration for the resource. Many connectors let you limit the scope of objects that the connector accesses. For example, the LDAP connector lets you specify base DNs and LDAP filters so that you do not need to access every entry in the directory.

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

### Restrict reconciliation queries using the IDM admin console

1. From the IDM console, click Native Consoles > Identity Management.

2. From the navigation bar, click Configure > Mappings.

3. On the Mappings page, select the mapping to restrict.

4. Click the Association tab, and expand the Reconciliation Query Filters tab.

5. Create a source or target query, and click Save.

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

IDM performs reconciliation in two phases:

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

The bulk import facility lets you import large numbers of external entries over REST. You import entries from a comma-separated values (CSV) file, to a specified managed object type in the IDM repository. Bulk import works as follows:

* Loads bulk CSV entries and stores them temporarily (in the IDM repository) as JSON objects

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
> When you have a CSV file, with the structure of the template generated in the previous example, upload the file to the IDM repository with the following request:
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
> |   |                                                               |
> | - | ------------------------------------------------------------- |
> |   | Note that the endpoint (`upload/csv`) is not an IDM endpoint. |

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
> |   |                                                                                                                                                                                                                                             |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | IDM does not scan for possible [CSV injection](https://owasp.org/www-community/attacks/CSV_Injection) attacks on uploaded files. *Do not* edit the downloaded CSV file with Microsoft Excel, as this can expose your data to CSV injection. |

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
  trigger-livesync-ui: Trigger liveSync using the IDM admin console
  troubleshooting-livesync: Troubleshoot liveSync failures
---

# Manage liveSync

Because you can trigger liveSync operations using REST (or the resource API) you can use an external scheduler to trigger liveSync operations, rather than using the IDM scheduling mechanism.

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

## Trigger liveSync using the IDM admin console

LiveSync operations are specific to a system object type (such as `system/ldap/account`). Apart from scheduling liveSync, as described in [Scheduling LiveSync Through the UI](chap-schedules.html#livesync-ui), you can launch a liveSync operation on demand for a particular system object type as follows:

1. From the IDM console, click Native Consoles > Identity Management.

2. From the navigation bar, click Configure > Connectors.

3. On the Connectors page, select a connector.

4. On the connector-name page, click the Object Types tab.

5. Click the edit button [icon: pencil-alt, set=fa]adjacent to the object type to synchronize.

6. Click the Sync tab, and then click Sync Now.

   The Sync Token field displays the current synchronization token for the object type.

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
  recon-details-ui: View reconciliation details using the IDM admin console
  recon-assoc: Reconciliation association details
  recon-delete: Purge reconciliation statistics
---

# Manage reconciliation

To trigger, cancel, and monitor reconciliation operations over REST, use the `openidm/recon` REST endpoint. You can perform most of these actions using the IDM admin console.

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

|   |                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To trigger this reconciliation using the IDM admin console, click Configure > Mappings, select a mapping, then click Reconcile.If you click Cancel Reconciliation before it completes, you will need to start the reconciliation again. |

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

|   |                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To cancel a reconciliation run in progress using the IDM admin console, click Configure > Mappings, click on the mapping reconciliation to cancel, and click Cancel Reconciliation. |

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

In contrast, the IDM admin console displays the results of only the most recent reconciliation. For more information, refer to [View reconciliation details using the IDM admin console](#recon-details-ui).

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

### View reconciliation details using the IDM admin console

You can display the details of the most recent reconciliation in the IDM admin console. Select the mapping. In the page that displays, you will see a message similar to:

```
Completed: Last reconciled November 20, 2019 15:28
```

Clicking on the reconciliation run date displays the details of the reconciliation run. Click Reconciliation Results for additional information.

If a reconciliation fails, select the Failure Summary tab for more information about the failure.

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
  link-qualifiers-ui: Configure Link Qualifiers Using the IDM admin console
---

# Map a single source object to multiple target objects

In certain cases, you might have a single object in a resource that maps to more than one object in another resource. For example, assume that managed user, bjensen, has two distinct accounts in an LDAP directory: an `employee` account (under `uid=bjensen,ou=employees,dc=example,dc=com`) and a `customer` account (under `uid=bjensen,ou=customers,dc=example,dc=com`). You want to map both of these LDAP accounts to the same managed user account.

IDM uses *link qualifiers* to manage this one-to-many scenario. A link qualifier is essentially a label that identifies the *type* of link (or relationship) between objects.

The following diagram shows two link qualifiers that let you link both of bjensen's LDAP accounts to her managed user object:

![link-qualifier](_images/link-qualifier.png)

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The previous diagram displays that the link qualifier is a property of the *link* between the source and target object, and not a property of the source or target object itself. |

Link qualifiers are defined as part of the mapping. Each link qualifier must be unique within the mapping. If no link qualifier is specified (when only one possible matching target object exists), IDM uses a default link qualifier with the value `default`.

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

IDM evaluates the list of static link qualifiers for *every* source record. That is, every reconciliation processes all synchronization operations, for each link qualifier, in turn.

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

  During source synchronization, IDM queries the target system for every source record *and* link qualifier, to check if there are any matching target records. If a match is found, the sourceId, targetId, and linkQualifier are all saved as the *link*.

  The following excerpt of a sample mapping shows the two link qualifiers described previously (`employee` and `customer`). The correlation query first searches the target system for the `employee` link qualifier. If a target object matches the query, based on the value of its `dn` attribute, IDM creates a link between the source object and that target object, and assigns the `employee` link qualifier to that link. This process is repeated for all source records. Then, the correlation query searches the target system for the `customer` link qualifier. If a target object matches that query, IDM creates a link between the source object and that target object and assigns the `customer` link qualifier to that link:

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

## Configure Link Qualifiers Using the IDM admin console

1. From the IDM console, click Native Consoles > Identity Management.

2. From the navigation bar, click Configure > Mappings, and click the mapping to edit.

3. Click the Properties tab, and expand the Link Qualifier node.

4. Select Static or Dynamic, configure the link qualifier, and click Save.

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
  preventing-accidental-deletion-ui: Prevent accidental target deletion using the IDM admin console
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

## Prevent accidental target deletion using the IDM admin console

1. From the IDM console, click Native Consoles > Identity Management.

2. From the navigation bar, click Configure > Mappings, and click the mapping to edit.

3. Click the Advanced tab, and expand the Additional Mapping Options node.

4. Enable Allow Reconciliations From an Empty Source.

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

* To remove a mapping using the IDM admin console, select Configure > Mappings, and then click Delete under the mapping to remove.

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you delete the mapping in the IDM admin console, the `delete-mapping-links` script removes all links related to that mapping from the repository. |

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

A synchronization mapping specifies a relationship between objects and their attributes in two data stores. The following example shows a typical attribute mapping, between objects in an external LDAP directory and an IDM managed user data store:

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

Mappings are always defined from a *source* resource to a *target* resource. To configure bidirectional synchronization, you must define two mappings. For example, to configure bidirectional synchronization between an LDAP server and an IDM repository, you would define the following two mappings:

* LDAP Server > IDM Repository

* IDM Repository > LDAP Server

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
  reusing-mapping-links-ui: Reuse links between mappings using the IDM admin console
---

# Reuse links between mappings

When two mappings synchronize the same objects bidirectionally, use the `links` property in one mapping to have IDM use the same link for both mappings. If you do not specify a `links` property, IDM maintains a separate link for each mapping.

The following excerpt shows two mappings, one from MyLDAP accounts to managed users, and another from managed users to MyLDAP accounts. In the second mapping, the `link` property indicates that IDM should reuse the links created in the first mapping, rather than create new links:

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

## Reuse links between mappings using the IDM admin console

1. From the IDM console, click Native Consoles > Identity Management.

2. From the navigation bar, click Configure > Mappings.

3. Click New Mapping.

4. On the Create Mapping screen select a mapping to link on the Linked Mapping attribute.

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
  livesync-ui: Schedule liveSync using the IDM admin console
---

# Schedule synchronization

You can schedule synchronization operations, such as liveSync and reconciliation, using Quartz triggers. IDM supports simple triggers and cron triggers.

Use the trigger type that suits your scheduling requirements. Because simple triggers are not bound to the local timezone, they are better suited to scenarios such as liveSync, where the requirement is to trigger the schedule at regular intervals, regardless of the local time. For more information, refer to the Quartz documentation on [SimpleTriggers](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-05.html) and [CronTriggers](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-06.html).

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

## Schedule liveSync using the IDM admin console

To configure liveSync using the IDM admin console, set up a liveSync schedule:

1. Go to `https://<tenant-env-fqdn>/admin/#scheduler/`, and click Add Schedule.

2. Complete the schedule configuration, and click Save.

   For more information about these fields, refer to [Configure Scheduled Synchronization](#configuring-sync-schedule).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The scheduler configuration assumes a `simple` trigger type by default, so the `Cron-like Trigger` field is disabled. You should use simple triggers for liveSync schedules to avoid problems related to daylight savings time. For more information, refer to [Schedules and daylight savings time](../idm-schedules/schedules-dst.html).By default, the IDM admin console creates schedules using the scheduler service, rather than the configuration service. To create this schedule in the configuration service, select the Save as Config Object option.For more information on the distinction between the scheduler service and the configuration service, refer to [Configure the scheduler service](../idm-schedules/scheduler-configuration-file.html). |

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
  mapping-conditions-ui: Configure mapping conditions using the IDM admin console
---

# Scriptable conditions in a mapping

By default, IDM synchronizes all attributes in a mapping. For more complex relationships between source and target objects, you can define conditions under which IDM maps certain attributes. You can define two types of mapping conditions:

* *Scriptable conditions*, in which an attribute is mapped only if the defined script evaluates to `true`.

* *Condition filters*, a declarative filter that sets the conditions under which the attribute is mapped. Condition filters can include a *link qualifier* , that identifies the *type* of relationship between the source object and multiple target objects. For more information, see [Map a Single Source Object to Multiple Target Objects](linking-multiple-targets.html).

  The following list shows examples of condition filters:

  * `"condition": "/object/country eq 'France'"`—Only map the attribute if the object's `country` attribute equals `France`.

  * `"condition": "/object/password pr"`—Only map the attribute if the object's `password` attribute is present.

  * `"condition": "/linkQualifier eq 'admin'"`—Only map the attribute if the link between this source and target object is of type `admin`.

## Configure mapping conditions using the IDM admin console

1. From the IDM console, click Native Consoles > Identity Management.

2. From the navigation bar, click Configure > Mappings, and click the mapping to edit.

3. Click the Properties tab.

4. Expand the Attributes Grid node, click the property to edit, click the Conditional Updates tab, and then do one of the following:

   * To configure a filtered condition, click Condition Filter.

   * To configure a scriptable condition, click Script.

5. Click Save.

Scriptable conditions create mapping logic, based on the result of the condition script. If the script does not return `true`, IDM does not manipulate the target attribute during a synchronization operation.

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

|   |                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can add comments to JSON files. This example includes a property named `comment`; however, you can use any unique property name, as long as it is not used elsewhere in the server. IDM ignores unknown property names in JSON configuration files. |

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

[Construct and Manipulate Attributes With Scripts](#construct-attributes) shows how to manipulate attributes with scripts when objects are created and updated. You can also trigger scripts in response to other synchronization actions. For example, you might not want to delete a managed user directly when an external account is deleted, but instead unlink the objects and deactivate the user in another resource. Alternatively, you might delete the object in IDM and run a script to perform some subsequent action.

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

IDM provides a `logger` object that you can use from scripts defined in your mapping. These scripts can log messages to the OSGi console and to log files, which are then ingested by the `monitoring/logs` endpoint. The `logger` object includes the following functions:

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
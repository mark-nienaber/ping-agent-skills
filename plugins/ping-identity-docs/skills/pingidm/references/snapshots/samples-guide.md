---
title: Asynchronous reconciliation using workflow
description: Run asynchronous PingIDM reconciliation using a workflow that requires administrator approval before creating new users from a CSV file
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:sync-asynchronous
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/sync-asynchronous.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Asynchronous", "Reconciliation", "Workflows"]
section_ids:
  run-asynchronous-recon: Run the sample
---

# Asynchronous reconciliation using workflow

This sample demonstrates asynchronous reconciliation using workflows.

The data for this sample is in the file `samples/sync-asynchronous/data/csvConnectorData.csv`. That file contains two users, as follows:

```csv
"description", "uid", "username", "firstname", "lastname", "email", "mobile..."
"Created ...", "bjensen", "bjensen@example.com", "Barbara", "Jensen", "bjensen@example.com", 1234..."
"Created ...", "scarter", "scarter@example.com", "Steven", "Carter", "scarter@example.com", 1234..."
```

During the sample, you will reconcile the users in the CSV file with the managed user repository. Instead of creating each user immediately, the reconciliation operation generates an approval request for each ABSENT user (users who are not found in the repository). The configuration for this action is defined in the `conf/sync.json` file, which specifies that an `ABSENT` condition should launch the `managedUserApproval` workflow:

```json
...
    {
        "situation" : "ABSENT",
        "action" : {
            "workflowName" : "managedUserApproval",
            "type" : "text/javascript",
            "file" : "workflow/triggerWorkflowFromSync.js"
        }
    },
 ...
```

When each request is approved by an administrator, an asynchronous reconciliation operation is launched, that ultimately creates the users in the repository.

## Run the sample

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

Before you start, prepare IDM as described in [Prepare IDM](start-here.html#preparing-openidm).

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Workflows are not supported with a DS repository. Before you test this sample, [install a JDBC repository](../install-guide/chap-repository.html). |

1. Edit the `/path/to/openidm/samples/sync-asynchronous/conf/datasource.jdbc-default.json` file with the details of your JDBC repository. For more information, refer to [Select a repository](../install-guide/chap-repository.html).

2. Start IDM with the configuration for this sample:

   ```
   /path/to/openidm/startup.sh -p samples/sync-asynchronous
   ```

3. The sample is configured to assign new workflow tasks to an admin account named `async.admin`. Create this account before you begin:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
    "userName": "async.admin",
    "givenName": "async",
    "sn" : "admin",
    "password" : "Passw0rd",
    "displayName" : "async admin",
    "mail" : "async.admin@example.com",
    "authzRoles": [
        { "_ref": "internal/role/openidm-admin" },
        { "_ref": "internal/role/openidm-authorized" }
    ],
    "_id" : "asyncadmin"
    }' \
   "http://localhost:8080/openidm/managed/user?_action=create"
   {
     "_id":"asyncadmin",
     "_rev":"00000000e8f502db",
     "userName":"async.admin",
     "givenName":"async",
     "sn":"admin",
     "displayName":"async admin",
     "mail":"async.admin@example.com",
     "accountStatus":"active",
     "effectiveRoles":[],
     "effectiveAssignments":[]
   }
   ```

4. Run reconciliation over the REST interface:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "http://localhost:8080/openidm/recon?_action=recon&mapping=systemCsvfileAccounts_managedUser"
   {
     "_id": "98d7f3c5-684e-4ef0-b4f9-f2e816a339cf-32",
     "state": "ACTIVE"
   }
   ```

   The reconciliation operation returns a reconciliation run ID, and the status of the operation.

   This reconciliation launches a workflow that generates an approval process for each ABSENT user. The approval processes must be approved by an administrator before the workflow can continue.

5. Review the approval tasks launched by the reconciliation.

   * To review the tasks in the admin UI, log in to the admin UI at `https://localhost:8443/admin/` using an administrator account (either `openidm-admin` or `async.admin` will work) and select Manage > Tasks.

     You should see two task instances launched by the Managed User Approval Workflow.

   * To view the approval tasks over REST run the following command:

     ```
     curl \
     --header "X-OpenIDM-Username: openidm-admin" \
     --header "X-OpenIDM-Password: openidm-admin" \
     --header "Accept-API-Version: resource=1.0" \
     --request GET \
     "http://localhost:8080/openidm/workflow/taskinstance?_queryFilter=true&_fields=_id,processDefinitionId"
     ```

     The request returns two task instances, each with a process ID (`_id`) and a process definition ID.

     ```json
     {
       "result": [
         {
           "_id": "38",
           "processDefinitionId": "managedUserApproval:1:5"
         },
         {
           "_id": "39",
           "processDefinitionId": "managedUserApproval:1:5"
         }
       ],
       ...
     }
     ```

6. Complete each approval task.

   * To complete the approval tasks using the UI, sign on to the end-user UI at `https://localhost:8443/#/login` as user `async.admin` with password `Passw0rd`.

     You should see two Evaluate request tasks under My Tasks on the Dashboard.

     For each task, select Edit, and then click Approve to add the noted users.

     |   |                                                                                                                           |
     | - | ------------------------------------------------------------------------------------------------------------------------- |
     |   | The end-user UI is not bundled with PingIDM. Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html). |

   * To approve the requests over REST, set `requestApproved` to `true` for each task instance, and use the `complete` action. Specify the `_id` of each task in the URL.

     For example, to approve the first request:

     ```
     curl \
     --header "X-OpenIDM-Username: async.admin" \
     --header "X-OpenIDM-Password: Passw0rd" \
     --header "Accept-API-Version: resource=1.0" \
     --header "Content-Type: application/json" \
     --request POST \
     --data '{"requestApproved": "true"}' \
     "http://localhost:8080/openidm/workflow/taskinstance/38?_action=complete"
     {
       "Task action performed": "complete"
     }
     ```

     Repeat this command for each task ID.

7. When the requests have been approved, select Manage > User in the admin UI to view the new users in the repository, or query the managed users over REST as follows:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/managed/user?_queryFilter=true&_fields=_id"
   {
     "result": [
       {
          "_id": "asyncadmin",
          "_rev": "00000000e8f502db"
       }, {
          "_id": "scarter",
          "_rev": "000000007e120780"
       }, {
          "_id": "bjensen",
          "_rev": "00000000d9390751"
       }
     ],
    ...
   }
   ```

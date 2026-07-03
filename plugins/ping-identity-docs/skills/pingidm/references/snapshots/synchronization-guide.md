---
title: Asynchronous reconciliation
description: Configure PingIDM asynchronous reconciliation to launch approval workflows before completing sync actions using the ASYNC reconciliation action
component: pingidm
version: 8.1
page_id: pingidm:synchronization-guide:chap-asynchronous-sync
canonical_url: https://docs.pingidentity.com/pingidm/8.1/synchronization-guide/chap-asynchronous-sync.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Reconciliation"]
section_ids:
  configure_asynchronous_reconciliation_using_a_workflow: Configure asynchronous reconciliation using a workflow
---

# Asynchronous reconciliation

Reconciliation can work in tandem with workflows to provide additional business logic to the reconciliation process. You can define scripts to determine the action that should be taken for a particular reconciliation situation. A reconciliation process can launch a workflow after it has assessed a situation, and then perform the reconciliation or some other action.

For example, you might want a reconciliation process to assess new user accounts that need to be created on a target resource. However, new user account creation might require some kind of approval from a manager before the accounts are actually created. The initial reconciliation process can assess the accounts that need to be created, then launch a workflow to request management approval for those accounts. The workflow performs the sync action, based upon the situation assessed during reconciliation (and provided to the workflow through the `ASYNC` action). The workflow then calls the `sync` endpoint with the `performAction` action and triggers a synchronization operation for the specified object.

In this scenario, the defined script returns `ASYNC` for new accounts, and the reconciliation engine does not continue processing the given object. The script then initiates an asynchronous process which, on completion, performs an explicit sync of the source object.

A sample configuration for this scenario is available in `openidm/samples/sync-asynchronous`, and described in [Asynchronous reconciliation using workflow](../samples-guide/sync-asynchronous.html).

## Configure asynchronous reconciliation using a workflow

1. Create the workflow definition file (`.xml or .bar` file) and place it in the `openidm/workflow` directory. For more information about creating workflows, refer to [Create workflows](../workflow-guide/create-workflow.html).

2. Modify the mapping for the situation or situations that should call the workflow. Reference the workflow name in the configuration for that situation.

   For example, the following mapping excerpt calls the `managedUserApproval` workflow if the situation is assessed as `ABSENT`:

   ```json
   {
       "situation" : "ABSENT",
       "action" : {
           "workflowName" : "managedUserApproval",
           "type" : "text/javascript",
           "file" : "workflow/triggerWorkflowFromSync.js"
       }
   }
   ```

   In the sample configuration, the workflow makes an explicit call to the `sync` endpoint with the `performAction` action (`openidm.action('sync', 'performAction', content, params)`).

You can also use this kind of explicit synchronization to perform a specific action on a source or target record, regardless of the assessed situation.

To call such an operation over the REST interface, specify the source, and/or target IDs, the mapping, and the action to be taken. The action can be any one of the supported reconciliation actions: `CREATE, UPDATE, DELETE, LINK, UNLINK, EXCEPTION, REPORT, NOREPORT, ASYNC, IGNORE`.

The following example calls the DELETE action on user `bjensen`, whose `_id` in the LDAP directory is `uid=bjensen,ou=People,dc=example,dc=com`. The user is deleted in the target resource; in this case, the repository.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `_id` must be URL-encoded in the REST call:```none
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/sync?_action=performAction&sourceId=uid%3Dbjensen%2Cou%3DPeople%2Cdc%3Dexample%2Cdc%3Dcom&mapping=
 systemLdapAccounts_ManagedUser&action=DELETE"
{
    "status": "OK"
}
``` |

The following example creates a link between a managed object and its corresponding system object. Such a call is useful in the context of manual data association, when correlation logic has linked an incorrect object, or when IDM has been unable to determine the correct target object.

In this example, there are two separate target accounts (`scarter.user` and `scarter.admin`) that should be mapped to the managed object. This call creates a link to the `user` account and specifies a link qualifier that indicates the type of link that will be created:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/sync?_action=performAction&action=LINK
   &sourceId=4b39f74d-92c1-4346-9322-d86cb2d828a8&targetId=scarter.user
   &mapping=managedUser_systemCsvfileAccounts&linkQualifier=user"
{
    "status": "OK"
}
```

For more information about linking to multiple accounts, refer to [Map a Single Source Object to Multiple Target Objects](linking-multiple-targets.html).

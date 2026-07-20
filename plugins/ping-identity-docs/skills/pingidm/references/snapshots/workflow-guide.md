---
title: BPMN 2.0 and workflow tools
description: Use BPMN 2.0 to define PingIDM workflows and business processes with Groovy or JavaScript scripts for provisioning and identity management tasks
component: pingidm
version: 8.1
page_id: pingidm:workflow-guide:about-workflow-tools
canonical_url: https://docs.pingidentity.com/pingidm/8.1/workflow-guide/about-workflow-tools.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Workflows", "BPMN", "BPM", "Groovy", "JavaScript", "Scripting"]
section_ids:
  workflow_limitations: Workflow limitations
---

# BPMN 2.0 and workflow tools

The [Business Process Model and Notation (BPMN)](https://www.omg.org/spec/BPMN/) is a standard maintained by the [Object Management Group (OMG)](https://omg.org/).

Use BPMN 2.0 to add workflow and business process artifacts to IDM for provisioning and other identity management tasks. You can create workflow definitions with a text editor or a compatible tool. Workflow scripts can use Groovy or JavaScript.

Scripts in BPMN 2.0 XML files can access the following variables:

* `openidm`

* `identityServer`

* `console`

For example, to log a message with Groovy:

```groovy
console.log('my message')
```

|   |                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For more information about graphical notations and XML representations for BPMN 2.0, refer to the [Flowable BPMN 2.0 Constructs](https://flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs/) documentation. |

## Workflow limitations

IDM doesn't support the following constructs:

* [Mule task](https://flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs/#mule-task)

* [Camel task](https://flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs/#camel-task)

The following reserved terms can't be used as variable names:

* `out`

* `out:print`

* `lang:import`

* `context`

* `elcontext`

---

---
title: Create workflows
description: Create PingIDM BPMN 2.0 workflows using Flowable constructs and package them as business archive files for deployment
component: pingidm
version: 8.1
page_id: pingidm:workflow-guide:create-workflow
canonical_url: https://docs.pingidentity.com/pingidm/8.1/workflow-guide/create-workflow.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Workflows", "BPMN", "Workflow Definition", "Business Archive File"]
---

# Create workflows

For more information about the graphical notations and XML representations for events, flows, gateways, tasks, process constructs, and more, refer to [BPMN 2.0 Constructs](https://flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs/).

IDM does not support the following constructs:

* [Mule task](https://flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs/#mule-task)

* [Camel task](https://flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs/#camel-task)

1. Create a workflow definition, and save it with a `bpmn20.xml` extension.

2. Package the workflow definition file in a Business Archive File (`.bar`). A `.bar` file is similar to a `.zip` file, but with a different extension.

3. Copy the `.bar` file to the `openidm/workflow` directory.

4. Invoke the workflow using a script (`openidm/script/`), or directly, using the REST interface. For more information, refer to [Invoke workflows](invoke-workflow.html).

   You can also [schedule](../schedules-guide/schedules.html) the workflow to be invoked repeatedly, or at a future time.

---

---
title: Custom workflow templates
description: Build custom Vue.js workflow form templates for the PingIDM end-user UI to support input validation, rich field types, and complex CSS
component: pingidm
version: 8.1
page_id: pingidm:workflow-guide:custom-workflow-template
canonical_url: https://docs.pingidentity.com/pingidm/8.1/workflow-guide/custom-workflow-template.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Workflows", "Custom Templates", "Flowable", "Vue JS Framework"]
section_ids:
  vue3-workflow-migration: Update custom workflow templates for Vue 3
  vue3-workflow-sample-reference: Updated workflow sample
  vue3-workflow-overview-changes: Overview of changes
  vue3-workflow-validation-changes: ValidationObserver and ValidationProvider removal
  vue3-workflow-template-changes: Template syntax changes
  vue3-workflow-slot-syntax: Slot syntax
  vue3-workflow-reactivity-changes: Reactivity changes
  vue3-workflow-localization: Localization keys
---

# Custom workflow templates

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | The end-user UI is not bundled with PingIDM. Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html). |

The embedded workflow engine integrates with the default end-user UI. For simple custom workflows, you can use the standard Flowable form properties and have the UI render the corresponding generic forms automatically. For more complex functionality, including input validation, rich input field types, complex CSS, and more, you must define a custom form template.

The default workflows provided with IDM use the [Vue JS framework](https://vuejs.org/guide/introduction.html) for display in the end-user UI. To write a custom form template, you must have a basic understanding of the Vue JS framework and how to create components. A sample workflow template is provided at `/path/to/samples/provisioning-with-workflow/workflow/contractorOnboarding.bar`. To extract the archive, run the following command:

```
jar -xvf contractorOnboarding.bar
inflated: contractorForm.js
inflated: contractorOnboarding.bpmn20.xml
```

The archive includes the workflow definition `contractorOnboarding.bpmn20.xml` and the corresponding JavaScript template `contractorForm.js` to render the workflow in the UI.

## Update custom workflow templates for Vue 3

The end-user UI has been upgraded from Vue 2 to Vue 3. If you have custom workflow form templates written for Vue 2, you must update them to work with Vue 3.

|   |                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------- |
|   | For in-depth Vue 3 migration guidance, check out the [Vue 3 Migration Guide](https://v3-migration.vuejs.org/). |

### Updated workflow sample

The sample workflow template provided at `samples/provisioning-with-workflow/workflow/contractorOnboarding.bar` has been updated to work with Vue 3. Use this as a reference when updating your own custom workflow form templates.

### Overview of changes

The following changes are specific to custom workflow form templates when moving from Vue 2 to Vue 3.

#### `ValidationObserver` and `ValidationProvider` removal

`ValidationObserver` and `ValidationProvider` from the `vee-validate` library were previously registered as global components by the end-user UI. They are no longer available in Vue 3.

Remove all `ValidationObserver` and `ValidationProvider` elements and replace them with component-local validation. The general pattern is:

1. Add an `errors` object to your component's `data` to track field-level error messages.

2. Replace the `ValidationObserver` ref-based `validate()` call in `submit()` with a synchronous `validateForm()` method that iterates over your form properties.

3. Implement a `validateField()` method that uses the native [`checkValidity()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checkValidity) API to validate individual inputs. For fields that require custom format checking (such as telephone numbers), apply a regex check before calling `checkValidity()`.

4. Replace `getValidationState()` with a `getFieldState()` method that maps the `errors` object state to a boolean: `null` (untouched), `true` (valid), or `false` (invalid).

5. In `resetForm()`, clear the `errors` object alongside resetting the form data so fields return to the untouched state.

#### Template syntax changes

Update the HTML template string in your custom workflow form to reflect the following changes:

* Remove `<ValidationObserver>` and `<ValidationProvider>` wrapper elements.

* Add the `novalidate` attribute to the `<b-form>` element because you're handling validation in JavaScript.

* Replace the static `type="text"` attribute with a dynamic `:type` binding that returns the appropriate HTML5 input type (`email`, `tel`, `date`, and so on) based on the field ID.

* Add `:required="formProperty.required"` to bind the HTML `required` attribute directly.

* Replace `:state="getValidationState(validationContext)"` with `:state="getFieldState(formProperty._id)"`.

* Add `@blur="validateField(formProperty)"` to trigger validation when the user leaves a field.

* Replace `<b-form-invalid-feedback>{{ validationContext.errors[0] }}</b-form-invalid-feedback>` with `<b-form-invalid-feedback v-if="errors[formProperty._id]">{{ errors[formProperty._id] }}</b-form-invalid-feedback>`.

#### Slot syntax

Update the deprecated `slot` attribute syntax to the Vue 3 shorthand:

* Vue 2 (before)

* Vue 3 (after)

```html
<template slot="label">...</template>
```

```html
<template #label>...</template>
```

#### Reactivity changes

Vue 3 uses a proxy-based reactivity system. Replace any calls to `this.$set()` with direct property assignment:

* Vue 2 (before)

* Vue 3 (after)

```javascript
this.$set(this.formData, 'requestApproved', null);
```

```javascript
this.formData.requestApproved = null;
```

#### Localization keys

Do not rely on localization keys from the end-user UI (such as `$t('pages.profile.editProfile.optional')`) in your custom workflow templates. The UI does not guarantee the stability of its internal localization keys, and they could change between releases. Instead, use hardcoded strings or provide your own localization mechanism in your custom form template.

---

---
title: Enable workflows
description: Enable the PingIDM Flowable workflow engine by configuring workflow.json and datasource.jdbc-default.json through the admin UI or manually
component: pingidm
version: 8.1
page_id: pingidm:workflow-guide:enable-workflows
canonical_url: https://docs.pingidentity.com/pingidm/8.1/workflow-guide/enable-workflows.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Workflows", "Flowable Process Engine", "OSGi", "Configuration", "JDBC", "JavaScript", "Groovy"]
section_ids:
  configure-workflow: Configure the workflow engine
  conf-workflow-email: Configure workflow email
  workflow-datasource: Configure the workflow data source
  workflow-custom-objects: Custom workflow object mapping
---

# Enable workflows

IDM embeds a Flowable Process Engine that starts in the OSGi container. Workflows are not active by default. IDM needs two configuration files to activate the workflow bundle:

* `workflow.json`

  The Flowable engine configuration, including the data source.

* `datasource.jdbc-default.json`

  The default data source for Flowable.

When you enable workflows in the admin UI, IDM creates `workflow.json` in your project's `conf/` directory.

1. Log in to the admin UI.

2. From the navigation bar, select Configure > System Preferences.

3. On the System Preferences page, click the Workflow tab.

4. Enable the display of workflows, and click Save.

5. Optionally, [configure the workflow engine](#configure-workflow).

6. [Configure the workflow data source](#workflow-datasource).

## Configure the workflow engine

IDM creates the default `workflow.json` file with the following structure:

```json
{
    "useDataSource" : "default",
    "workflowDirectory" : "&{idm.instance.dir}/workflow",
    "userResource": {
        "path": "managed/user",
        "queryFilter": "/userName eq \"${username}\""
    },
    "groupResource": {
        "path": "managed/group",
        "queryFilter": "/id eq \"${gid}\""
    }
}
```

* `useDataSource`

  The datasource configuration file that points to the repository where Flowable should store data.

  By default, this is the `datasource.jdbc-default.json` file. For information about changing the data store that Flowable uses, refer to [Configure the Workflow Data Source](#workflow-datasource).

* `workflowDirectory`

  Specifies the location where IDM expects to find workflow processes. By default, IDM looks for workflow processes in the `project-dir/workflow` directory.

In addition to these default properties, you can configure the Flowable engine `history` level:

```json
{
    "history" : "audit"
}
```

When a workflow is executed, information can be logged as determined by the history level. The history level can be one of the following:

* `none` This level results in the best performance for workflow execution, but no historical information is retained.

* `activity` Logs all process instances and activity instances, without details.

* `audit` This is the default level. All process instances, activity instances, and submitted form properties are logged so that all user interaction through forms is traceable and can be audited.

* `full` This is the highest level of history logging and has the greatest performance impact. This history level stores all the information that is stored for the `audit` level, as well as any process variable updates.

### Configure workflow email

Workflows can send an email using the following methods:

> **Collapse: Flowable email tasks**
>
> To use [workflow email tasks](https://flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs/#email-task), add the email configuration to `workflow.json`.
>
> Example email configuration:
>
> ```json
> "mail" : {
>     "host" : "mail.example.com",
>     "port" : 1025,
>     "username" : "username",
>     "password" : "password",
>     "useSSL" : false,
>     "starttls" : true,
>     "defaultFrom" : "workflow@example.com",
>     "forceTo" : "overrideSendToEmail@example.com"
> }
> ```

> **Collapse:&#x20;**
>
> Only JavaScript and Groovy are supported as `ScriptTask#scriptFormat` languages.
>
> [Emails sent using `scriptTask`](../external-services-guide/email.html#send-mail-script) utilize [IDM's email client configuration.](../external-services-guide/email.html)
>
> Example script:
>
> ```none
> openidm.action("external/email", "send", { "to": "bob@example.com" }, { waitForCompletion: true });
> ```

## Configure the workflow data source

The Flowable engine requires a JDBC database. The connection details to the database are specified in the `datasource.jdbc-default.json` file. If you are using a JDBC repository for IDM data, you will already have a `datasource.jdbc-default.json` file in your project's `conf/` directory. In this case, when you enable workflows, IDM uses the existing JDBC repository and creates the required Flowable tables in that JDBC repository.

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are using a DS repository for IDM data, you must configure a separate JDBC repository as the workflow datasource. For more information, refer to [Select a repository](../install-guide/chap-repository.html). |

To specify a Flowable data source separate from your existing IDM repository, create a new *datasource* configuration file in your project's `conf/` directory (for example, `datasource.jdbc-flowable.json`) with the connection details to the separate data source. Then, reference that file in the `useDataSource` property of the `workflow.json` file (for example, `"useDataSource" : "flowable"`).

For more information about the fields in this file, refer to [JDBC Connection Configuration](../objects-guide/repo-config.html#datasource-jdbc-json).

## Custom workflow object mapping

For custom object mapping, edit the default `workflow.json` configuration:

```json
"userResource": {
    "path": "managed/user",
    "queryFilter": "/userName eq \"${username}\""
},
"groupResource": {
    "path": "managed/group",
    "queryFilter": "/id eq \"${gid}\""
}
```

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Do not replace `${username}` or `${gid}` in the queryFilter; for example:- OK: `"queryFilter": "/callSign eq \"${username}\""`

- *NOT* OK: `"queryFilter": "/callSign eq \"${callsign}\""` |

---

---
title: Invoke workflows
description: Invoke PingIDM workflows from scripts using openidm.create() or directly over REST, including from reconciliation situation triggers
component: pingidm
version: 8.1
page_id: pingidm:workflow-guide:invoke-workflow
canonical_url: https://docs.pingidentity.com/pingidm/8.1/workflow-guide/invoke-workflow.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Workflows", "Workflow Definition", "Call", "Scripting", "Functions", "REST"]
---

# Invoke workflows

You can invoke workflows and business processes from any trigger point within IDM, including reacting to situations discovered during reconciliation. Workflows can be invoked from script files, using the `openidm.create()` function, or directly from the REST interface.

The following sample script extract shows how to invoke a workflow from a script file:

```javascript
/*
 * Calling 'myWorkflow' workflow
 */

var params = {
  "_key": "myWorkflow"
};

openidm.create('workflow/processinstance', null, params);
```

The `null` in this example indicates that you do not want to specify an ID as part of the create call. For more information, refer to [`openidm.create()`](../scripting-guide/scripting-func-ref.html#function-create).

You can invoke the same workflow from the REST interface with the following REST call:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{"_key":"myWorkflow"}' \
"http://localhost:8080/openidm/workflow/processinstance?_action=create"
```

For more information, refer to [Workflows](../rest-api-reference/endpoints/rest-workflows.html).

There are two ways in which you can specify the workflow definition that is used when a new workflow instance is started.

* `_key` specifies the `id` attribute of the workflow process definition, for example:

  ```xml
  <process id="sendNotificationProcess" name="Send Notification Process">
  ```

  If there is more than one workflow definition with the same `_key` parameter, the latest deployed version of the workflow definition is invoked.

* `_processDefinitionId` specifies the ID that is generated by the Flowable Process Engine when a workflow definition is deployed; for example:

  ```javascript
  "sendNotificationProcess:1:104";
  ```

  To obtain the `processDefinitionId`, query the available workflows, for example:

  ```json
  {
    "result": [
      {
        "name": "Process Start Auto Generated Task Auto Generated",
        "_id": "ProcessSAGTAG:1:728"
      },
      {
        "name": "Process Start Auto Generated Task Empty",
        "_id": "ProcessSAGTE:1:725"
      },
      ...
    ]
  }
  ```

  If you specify a `_key` and a `_processDefinitionId`, the `_processDefinitionId` is used because it is more precise.

Use the optional `_businessKey` parameter to add specific business logic information to the workflow when it is invoked. For example, the following workflow invocation assigns the workflow a business key of `"newOrder"`. This business key can later be used to query "newOrder" processes.

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
--data '{"_key":"myWorkflow", "_businessKey":"newOrder"}' \
"http://localhost:8080/openidm/workflow/processinstance?_action=create"
```

Access to workflows is based on IDM roles, and is configured in your project's `conf/process-access.json` file. For more information, refer to [Secure Access to Workflows](../auth-guide/authorization-and-roles.html#managing-workflow-access).

---

---
title: Query workflows
description: Query running PingIDM workflow process instances and tasks over REST using filtered GET requests on the workflow/processinstance endpoint
component: pingidm
version: 8.1
page_id: pingidm:workflow-guide:query-workflow
canonical_url: https://docs.pingidentity.com/pingidm/8.1/workflow-guide/query-workflow.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Workflows", "Query"]
---

# Query workflows

The workflow implementation supports filtered queries that let you query the running process instances and tasks, based on specific query parameters. To perform a filtered query, send a GET request to the `workflow/processinstance` context path, including the query in the URL.

For example, the following query returns all process instances with the business key `"newOrder"`, as invoked in the previous example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/workflow/processinstance?_queryId=filtered-query&processInstanceBusinessKey=newOrder"
```

Any workflow properties can be queried using the same notation; for example, `processDefinitionId=managedUserApproval:1:6405`. The query syntax applies to all queries with `_queryId=filtered-query`. The following query returns all process instances that were started by the user `openidm-admin`:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/workflow/processinstance?_queryId=filtered-query&startUserId=openidm-admin"
```

You can also query process instances based on the value of any process instance variable, by prefixing the variable name with `var-`. For example:

```
var-processvariablename=processvariablevalue
```

---

---
title: Test workflow integration
description: Test PingIDM workflow integration using the provisioning-with-workflow sample and the contractorOnboarding.bar workflow definition
component: pingidm
version: 8.1
page_id: pingidm:workflow-guide:test-workflow
canonical_url: https://docs.pingidentity.com/pingidm/8.1/workflow-guide/test-workflow.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Workflows", "Integration"]
---

# Test workflow integration

IDM reads workflow definitions from the `/path/to/openidm/workflow` directory.

The `/path/to/openidm/samples/provisioning-with-workflow/` sample provides a workflow definition (`contractorOnboarding.bar`) that you can use to test the workflow integration.

1. Create a `workflow` directory in your project directory and copy the sample workflow to that directory:

   ```
   cd project-dir
   mkdir workflow
   cp samples/provisioning-with-workflow/workflow/contractorOnboarding.bar workflow/
   ```

2. Verify the workflow integration by using the REST API. The following REST call lists the defined workflows:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/workflow/processdefinition?_queryFilter=true"
   ```

   The result is similar to:

   ```json
   {
     "result": [
       {
         "_id": "contractorOnboarding:1:5",
         "_rev": "1",
         "candidateStarterGroupIdExpressions": [],
         "candidateStarterUserIdExpressions": [],
         "category": "Examples",
         "deploymentId": "1",
         "description": null,
         "eventSupport": {},
         "executionListeners": {},
         "graphicalNotationDefined": false,
         "hasStartFormKey": true,
         "historyLevel": null,
         "ioSpecification": null,
         "key": "contractorOnboarding",
         "laneSets": [],
         "name": "Contractor onboarding process",
         "participantProcess": null,
         "processDiagramResourceName": "contractorOnboarding.contractorOnboarding.png",
         "properties": {},
         "resourceName": "contractorOnboarding.bpmn20.xml",
         "revisionNext": 2,
         "startFormHandler": null,
         "suspended": false,
         "suspensionState": 1,
         "taskDefinitions": null,
         "tenantId": "",
         "variables": null,
         "version": 1
       }
     ],
     "resultCount": 1,
     "pagedResultsCookie": null,
     "totalPagedResultsPolicy": "NONE",
     "totalPagedResults": -1,
     "remainingPagedResults": -1
   }
   ```

For more information about the above workflow, refer to [Provision users with workflow](../samples-guide/provisioning-with-workflow.html).

For more information about managing workflows over REST, refer to [Workflows](../rest-api-reference/endpoints/rest-workflows.html).

---

---
title: Workflow
description: Guide to enabling and using PingIDM workflows
component: pingidm
version: 8.1
page_id: pingidm:workflow-guide:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/workflow-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Workflows"]
page_aliases: ["index.adoc"]
---

# Workflow

> Guide to enabling and using PingIDM workflows.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

IDM provides an embedded workflow and business process engine based on [Flowable](https://flowable.com/open-source/docs/) and the Business Process Model and Notation (BPMN) 2.0 standard. This guide describes how to configure the workflow engine, and how to manage workflow tasks and processes using the REST interface and the admin UI.

[icon: toolbox, set=fad, size=3x]

#### [Workflow Tools](about-workflow-tools.html)

Learn about BPMN 2.0 and the workflow tools.

[icon: toggle-on, set=fad, size=3x]

#### [Enable Workflows](enable-workflows.html)

Configure the workflow engine and datasource to enable workflows.

[icon: hat-wizard, set=fad, size=3x]

#### [Invoke Workflows](invoke-workflow.html)

Learn where and how to trigger workflows.

[icon: dice-d20, set=fad, size=3x]

#### [Custom Workflows](custom-workflow-template.html)

Create custom workflow templates.

|   |                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Workflows are not supported with a DS repository. If you are using a DS repository for IDM data, you must configure a separate JDBC repository as the [workflow datasource](enable-workflows.html#workflow-datasource). |

---

---
title: Workflow audit
description: Understand how PingIDM logs workflow events in the activity audit topic, with examples from the provisioning-with-workflow sample
component: pingidm
version: 8.1
page_id: pingidm:workflow-guide:workflow-audit
canonical_url: https://docs.pingidentity.com/pingidm/8.1/workflow-guide/workflow-audit.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Workflows", "Audit", "Provisioning"]
section_ids:
  example_workflow_audit_events_using_the_provisioning_with_workflow_sample: Example workflow audit events using the provisioning-with-workflow sample:
---

# Workflow audit

The audit service logs workflow information in the [activity event topic](../audit-guide/audit-log-topics.html#default-audit-topics) (default location: `openidm/audit/activity.audit.json`).

## Example workflow audit events using the [provisioning-with-workflow sample](../samples-guide/provisioning-with-workflow.html):

Each step shows the action performed along with the resulting audit data.

1. `user1` completes the *Contractor Onboarding Form*.

   ```json
   {
     "_id": "f24ac83b-200c-449d-b017-d12b9c6c9091-3871",
     "timestamp": "2020-05-06T17:39:52.021Z",
     "eventName": "workflow-create_process",
     "transactionId": "f24ac83b-200c-449d-b017-d12b9c6c9091-3865",
     "userId": "user1",
     "runAs": "user1",
     "objectId": "workflow/processinstance/6",
     "operation": "CREATE",
     "changedFields": [],
     "revision": null,
     "status": "SUCCESS",
     "message": "Process created. processDefinitionId = contractorOnboarding:1:5, processDefinitionKey = null, businessKey = null",
     "passwordChanged": false
   }
   ```

2. `manager1` self-assigns the task.

   ```json
   {
     "_id": "f24ac83b-200c-449d-b017-d12b9c6c9091-5748",
     "timestamp": "2020-05-06T17:43:18.058Z",
     "eventName": "workflow-update_task",
     "transactionId": "f24ac83b-200c-449d-b017-d12b9c6c9091-3865",
     "userId": "manager1",
     "runAs": "manager1",
     "objectId": "workflow/taskinstance/36",
     "operation": "UPDATE",
     "changedFields": [
       "/assignee"
     ],
     "revision": null,
     "status": "SUCCESS",
     "message": "Task updated",
     "passwordChanged": false
   }
   ```

   |   |                                                                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | `"changedFields":["/assignee"]` only displays when `conf/audit.json` contains the property `"watchedFields" : [ "assignee" ]`. For a complete list of fields that can be watched in this situation, refer to the API Descriptor for `UPDATE workflow/taskinstance/`. |

3. `manager1` completes the task. Notice that `transactionId` is correlated to all managed/user, and other, operations.

   ```json
   {
     "_id": "f24ac83b-200c-449d-b017-d12b9c6c9091-5868",
     "timestamp": "2020-05-06T17:43:22.138Z",
     "eventName": "activity",
     "transactionId": "f24ac83b-200c-449d-b017-d12b9c6c9091-3865",
     "userId": "user1",
     "runAs": "user1",
     "objectId": "managed/user/d736487d-c146-4a0e-b677-ebfd6805b1d2",
     "operation": "CREATE",
     "changedFields": [],
     "revision": "000000001edd9dc2",
     "status": "SUCCESS",
     "message": "create",
     "passwordChanged": false
   }
   {
     "_id": "f24ac83b-200c-449d-b017-d12b9c6c9091-5871",
     "timestamp": "2020-05-06T17:43:22.141Z",
     "eventName": "activity",
     "transactionId": "f24ac83b-200c-449d-b017-d12b9c6c9091-3865",
     "userId": "user1",
     "runAs": "user1",
     "objectId": "internal/usermeta/cd237cca-913e-481e-9282-ba16c84b5131",
     "operation": "CREATE",
     "changedFields": [],
     "revision": "0000000030b45c3e",
     "status": "SUCCESS",
     "message": "create",
     "passwordChanged": false
   }
   {
     "_id": "f24ac83b-200c-449d-b017-d12b9c6c9091-5876",
     "timestamp": "2020-05-06T17:43:22.145Z",
     "eventName": "relationship_created",
     "transactionId": "f24ac83b-200c-449d-b017-d12b9c6c9091-3865",
     "userId": "user1",
     "runAs": "user1",
     "objectId": "managed/user/d736487d-c146-4a0e-b677-ebfd6805b1d2/authzRoles/ee5bbbce-a020-45db-ab41-66c80d84d8be",
     "operation": "CREATE",
     "changedFields": [],
     "revision": "00000000fe6da3a7",
     "status": "SUCCESS",
     "message": "Relationship originating from managed/user/d736487d-c146-4a0e-b677-ebfd6805b1d2 via the relationship field authzRoles and referencing internal/role/openidm-authorized was created.",
     "passwordChanged": false
   }
   {
     "_id": "f24ac83b-200c-449d-b017-d12b9c6c9091-5879",
     "timestamp": "2020-05-06T17:43:22.147Z",
     "eventName": "relationship_created",
     "transactionId": "f24ac83b-200c-449d-b017-d12b9c6c9091-3865",
     "userId": "user1",
     "runAs": "user1",
     "objectId": "managed/user/d736487d-c146-4a0e-b677-ebfd6805b1d2/manager/b58e5695-9e43-4e76-b89c-e5d69d3bf52d",
     "operation": "CREATE",
     "changedFields": [],
     "revision": "000000008dcca1b6",
     "status": "SUCCESS",
     "message": "Relationship originating from managed/user/d736487d-c146-4a0e-b677-ebfd6805b1d2 via the relationship field manager and referencing managed/user/038e65de-95ce-4180-94d3-4ea64bf25c6b was created.",
     "passwordChanged": false
   }
   {
     "_id": "f24ac83b-200c-449d-b017-d12b9c6c9091-5882",
     "timestamp": "2020-05-06T17:43:22.149Z",
     "eventName": "relationship_created",
     "transactionId": "f24ac83b-200c-449d-b017-d12b9c6c9091-3865",
     "userId": "user1",
     "runAs": "user1",
     "objectId": "managed/user/d736487d-c146-4a0e-b677-ebfd6805b1d2/_meta/d9299603-b768-44b6-a4c9-9b6441ca212e",
     "operation": "CREATE",
     "changedFields": [],
     "revision": "0000000027b29fb4",
     "status": "SUCCESS",
     "message": "Relationship originating from managed/user/d736487d-c146-4a0e-b677-ebfd6805b1d2 via the relationship field _meta and referencing internal/usermeta/cd237cca-913e-481e-9282-ba16c84b5131 was created.",
     "passwordChanged": false
   }
   {
     "_id": "f24ac83b-200c-449d-b017-d12b9c6c9091-5908",
     "timestamp": "2020-05-06T17:43:22.778Z",
     "eventName": "activity",
     "transactionId": "f24ac83b-200c-449d-b017-d12b9c6c9091-3865",
     "userId": "user1",
     "runAs": "user1",
     "objectId": "internal/notification/12aa1698-bb1e-42c6-a92d-2e959c217ad0",
     "operation": "CREATE",
     "changedFields": [],
     "revision": "000000004d025d75",
     "status": "SUCCESS",
     "message": "create",
     "passwordChanged": false
   }
   {
     "_id": "f24ac83b-200c-449d-b017-d12b9c6c9091-5911",
     "timestamp": "2020-05-06T17:43:22.781Z",
     "eventName": "relationship_created",
     "transactionId": "f24ac83b-200c-449d-b017-d12b9c6c9091-3865",
     "userId": "user1",
     "runAs": "user1",
     "objectId": "internal/notification/12aa1698-bb1e-42c6-a92d-2e959c217ad0/target/eec80d30-be1e-4c5d-9873-b4395373c833",
     "operation": "CREATE",
     "changedFields": [],
     "revision": "00000000b4c7a701",
     "status": "SUCCESS",
     "message": "Relationship originating from internal/notification/12aa1698-bb1e-42c6-a92d-2e959c217ad0 via the relationship field target and referencing managed/user/038e65de-95ce-4180-94d3-4ea64bf25c6b was created.",
     "passwordChanged": false
   }
   {
     "_id": "f24ac83b-200c-449d-b017-d12b9c6c9091-5920",
     "timestamp": "2020-05-06T17:43:22.791Z",
     "eventName": "activity",
     "transactionId": "f24ac83b-200c-449d-b017-d12b9c6c9091-3865",
     "userId": "user1",
     "runAs": "user1",
     "objectId": "internal/notification/eec030e5-e520-4cf1-99c2-a9bbecb0627b",
     "operation": "CREATE",
     "changedFields": [],
     "revision": "0000000033465ada",
     "status": "SUCCESS",
     "message": "create",
     "passwordChanged": false
   }
   {
     "_id": "f24ac83b-200c-449d-b017-d12b9c6c9091-5923",
     "timestamp": "2020-05-06T17:43:22.794Z",
     "eventName": "relationship_created",
     "transactionId": "f24ac83b-200c-449d-b017-d12b9c6c9091-3865",
     "userId": "user1",
     "runAs": "user1",
     "objectId": "internal/notification/eec030e5-e520-4cf1-99c2-a9bbecb0627b/target/11eb13f8-991f-45ea-95dc-e8f0fd0b95c3",
     "operation": "CREATE",
     "changedFields": [],
     "revision": "000000005134a80d",
     "status": "SUCCESS",
     "message": "Relationship originating from internal/notification/eec030e5-e520-4cf1-99c2-a9bbecb0627b via the relationship field target and referencing managed/user/d736487d-c146-4a0e-b677-ebfd6805b1d2 was created.",
     "passwordChanged": false
   }
   ```

4. The audit service logs the `workflow-complete_task` event.

   ```json
   {
     "_id": "f24ac83b-200c-449d-b017-d12b9c6c9091-5926",
     "timestamp": "2020-05-06T17:43:22.827Z",
     "eventName": "workflow-complete_task",
     "transactionId": "f24ac83b-200c-449d-b017-d12b9c6c9091-3865",
     "userId": "manager1",
     "runAs": "manager1",
     "objectId": "workflow/taskinstance/36",
     "operation": "complete",
     "changedFields": [],
     "revision": null,
     "status": "SUCCESS",
     "message": "Task completed",
     "passwordChanged": false
   }
   ```
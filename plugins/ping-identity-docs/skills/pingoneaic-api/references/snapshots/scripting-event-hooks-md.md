---
title: Event hooks
description: Event hooks let you trigger scripts during various stages of the lifecycle of users, roles, assignments, organizations, groups[1], and applications.
component: pingoneaic-api
page_id: pingoneaic-api::scripting-event-hooks
canonical_url: https://developer.pingidentity.com/pingoneaic-api/scripting-event-hooks.html
keywords: ["Extensibility", "Scripts", "Identities"]
section_ids:
  create-a-new-event-hook: Create a new event hook
  scripting-tips: Scripting tips
  use-a-variable-in-an-event-hook-script: Use a variable in an event hook script
  use-an-esv-in-an-event-hook-script: Use an ESV in an event hook script
---

# Event hooks

|   |                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The topics on this page are for tenants created on or after January 12, 2023. Learn more in [Event hooks migration FAQ](https://docs.pingidentity.com/pingoneaic/latest/product-information/migration-dependent-features/event-hooks-migration-faq.html). |

*Event hooks* let you trigger scripts during various stages of the lifecycle of users, roles, assignments, organizations, groups\[[1](#_footnotedef_1 "View footnote.")], and applications.

You can trigger scripts when one of these [identity objects](https://docs.pingidentity.com/pingoneaic/latest/identities/identity-cloud-identity-schema.html) is created, updated, retrieved, deleted, validated, or stored in the repository. You can also trigger a script when a change to an identity object triggers an implicit synchronization operation.

Post-action scripts let you manipulate identity objects after they are created, updated, or deleted.

For some links to help with writing scripts for event hooks, and a few examples, learn more in [Scripting tips](#scripting-tips).

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Scripts can potentially emit the personally identifiable information (PII) of your end users into Advanced Identity Cloud logs, and then into external services that consume Advanced Identity Cloud logs.Ping Identity recommends that you establish a review and testing process for all scripts to prevent PII leaking out of your Advanced Identity Cloud tenant environments. |

## Create a new event hook

1. In the Advanced Identity Cloud admin console, go to *Realm* > Event Hooks.

2. On the Event Hooks page, click + New Event Hook.

3. On the New Event Hook page, enter event hook details:

   1. Enter the Name for the event hook.

   2. (Optional) Enter a Description for the event hook.

   3. Identify a condition that will trigger a script to run. In the Condition field:

      * Select an identity object type—​a user, role, assignment, organization, group, or application—​from the Object Name drop-down list.

      * Select an event type from the Event drop-down list.\
        Note that event types that have already been configured in event hooks do not appear in the drop-down list. Advanced Identity Cloud lets you configure exactly one event hook per condition.

   4. Specify a [script to run](#scripting-tips) when the event hook is triggered. Either:

      * Type JavaScript code into the Script field.

      * Or, click the Upload File toggle, and then click Browse. Then, select the file that contains the JavaScript code that will run when the event hook is triggered.

   5. (Optional) Enter variables to be passed to the event hook's script. Either:

      * Click + Add Variables, and then enter variable names and values in the Variables > Name and Variables > Value fields.

      * Or, click the JSON toggle, and then type JSON-formatted values into the Variables field.

4. Click Save.

## Scripting tips

The following links contain general information to help you write scripts triggered by event hooks:

* [Script triggers defined in the managed object configuration](https://docs.pingidentity.com/pingoneaic/latest/idm-scripting/script-triggers-managedConfig.html)

* [Functions available in identity-related scripts](https://docs.pingidentity.com/pingoneaic/latest/idm-scripting/scripting-func-ref.html)

* [The `identityServer` variable](https://docs.pingidentity.com/pingoneaic/latest/idm-scripting/script-variables-identity-server.html)

The sections that follow contain code snippets that might be helpful when you start developing your own event hook scripts.

### Use a variable in an event hook script

This example adds a prefix to a user's last name (`sn` attribute) in the user creation event hook.

1. Add a variable named `myCompany` to the event hook, and set its value to the desired prefix.

2. Specify a script similar to the following in the event hook:

   ```javascript
   object.sn = myCompany + "-" + object.sn;
   ```

### Use an ESV in an event hook script

This example sets the value of a user's `Description` attribute to the value of an ESV in the user creation event hook.

* Either specify the ESV in a variable:

  1. Add a variable named `myDescriptionESVValue` to the event hook.

  2. Set the variable's value to `&{esv.myDescription}`.

  3. Specify a script similar to the following in the event hook:

     ```javascript
     object.description = myDescriptionESVValue;
     ```

* Or, use the `identityServer` object to get the ESV value:

  ```javascript
  object.description = identityServer.getProperty("esv.myDescription")
  ```

***

[1](#_footnoteref_1). Event hooks are available for groups if you have enabled the groups feature in your Advanced Identity Cloud tenant.

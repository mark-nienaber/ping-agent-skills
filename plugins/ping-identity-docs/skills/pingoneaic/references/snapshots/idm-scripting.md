---
title: Call a script from the IDM configuration
description: Call scripts from identity management with inline source or file references
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-call
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-call.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  examples: Examples
---

# Call a script from the IDM configuration

To call a script from the IDM configuration, edit the configuration object. For example:

Provide a script source

```json
{
    "type" : "text/javascript",
    "source": "scriptSource"
}
```

Script variables are not necessarily simple `key:value` pairs, and can be any arbitrarily complex JSON object.

* type

  string, required

  The script type.

  IDM supports `"text/javascript"`.

* source

  string, required

  Specifies the source code of the script to be executed.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use namespace variables passed into scripts with the `globals` map. Passing variables in this way prevents collisions with the top-level reserved words for script maps, such as `source` and `type`. This example uses the `globals` map to namespace the variables passed in the previous example.```json
"script": {
    "type" : "text/javascript",
    "source" : "scriptSource",
    "globals" : {
        "fromSender" : "admin@example.com",
        "toEmail" : "user@example.com"
    }
}
``` |

## Examples

The following example script (in the mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint.)*) determines whether to include or ignore a target object in the reconciliation process based on an `employeeType` of `true`:

```json
"validTarget" : {
    "type" : "text/javascript",
    "source" : "target.employeeType == 'external'"
}
```

The following example script (in the mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint.)*) sets the `__PASSWORD__` attribute to `defaultpwd` when IDM creates a target object:

```json
"onCreate" : {
    "type" : "text/javascript",
    "source" : "target.__PASSWORD__ = 'defaultpwd'"
}
```

You can pass variables to your scripts to provide contextual details at runtime by declaring the variable name in the script reference.

The following scheduled task configuration calls a script that triggers an email notification, but sets the sender and recipient of the email in the schedule configuration, rather than in the script itself:

```json
{
    "enabled" : true,
    "type" : "cron",
    "schedule" : "0 0/1 * * * ?",
    "persisted" : true,
    "invokeService" : "script",
    "invokeContext" : {
        "script" : {
            "type" : "text/javascript",
            "source" : "scriptSource",
            "fromSender" : "admin@example.com",
            "toEmail" : "user@example.com"
        }
    }
}
```

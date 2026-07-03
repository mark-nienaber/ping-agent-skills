---
title: Call a script from the IDM configuration
description: Call a script from the PingIDM configuration using inline source or a file reference, with examples of passing variables and globals
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-call
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-call.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Configuration", "Call"]
section_ids:
  examples: Examples
---

# Call a script from the IDM configuration

To call a script from the IDM configuration, edit the configuration object. For example:

Provide a script source

```json
{
    "type" : "text/javascript",
    "source": "scriptSource",
    "resourceBindings" : [{
        "resource" : "resourceName",
        "version" : "1.0",
        "binding" : "customName"
    }]
}
```

or

Provide a file reference

```json
{
    "type" : "text/javascript",
    "file" : "file location"
}
```

Script variables are not necessarily simple `key:value` pairs, and can be any arbitrarily complex JSON object.

* type

  string, required

  The script type.

  IDM supports `"text/javascript"` and `"groovy"`.

* source

  string, required if `file` is not specified

  Specifies the source code of the script to be executed.

* resourceBindings

  JSON object, optional

  Allows specifying a resource, a vanity binding for that resource, and the API version the script should use. For example:

  ```json
  {
      "source" : "var response = consent.action(\"getConsentMappings\", {}); response[0];",
      "resourceBindings" : [{
          "resource" : "consent",
          "version" : "1.0",
          "binding" : "consent"
      }],
      "type" : "text/javascript"
  }
  ```

  This can improve the legibility of your scripts, by no longer needing to pass additional information within your script function.

* file

  string, required if `source` is not specified

  Specifies the file containing the source code of the script to execute. The file path must be relative to project-dir. Absolute paths are not supported.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In general, you should namespace variables passed into scripts with the `globals` map. Passing variables in this way prevents collisions with the top-level reserved words for script maps, such as `source`, `file`, and `type`. This example uses the `globals` map to namespace the variables passed in the previous example.```json
"script": {
    "type" : "text/javascript",
    "file" : "script/triggerEmailNotification.js",
    "globals" : {
        "fromSender" : "admin@example.com",
        "toEmail" : "user@example.com"
    }
}
``` |

## Examples

The following example script (in the mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint, directly in the conf/sync.json file, or in individual conf/mapping-\<mappingName>.json files.)*) determines whether to include or ignore a target object in the reconciliation process based on an `employeeType` of `true`:

```json
"validTarget" : {
    "type" : "text/javascript",
    "source" : "target.employeeType == 'external'"
}
```

The following example script (in the mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint, directly in the conf/sync.json file, or in individual conf/mapping-\<mappingName>.json files.)*) sets the `__PASSWORD__` attribute to `defaultpwd` when IDM creates a target object:

```json
"onCreate" : {
    "type" : "text/javascript",
    "source" : "target.__PASSWORD__ = 'defaultpwd'"
}
```

Often, script files are reused in different contexts. You can pass variables to your scripts to provide these contextual details at runtime. You pass variables to the scripts that are referenced in configuration files by declaring the variable name in the script reference.

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
            "file" : "script/triggerEmailNotification.js",
            "fromSender" : "admin@example.com",
            "toEmail" : "user@example.com"
        }
    }
}
```

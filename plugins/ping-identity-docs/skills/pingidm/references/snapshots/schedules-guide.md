---
title: Activate and deactivate accounts
description: Configure PingIDM scanning tasks to activate or deactivate managed user accounts based on activeDate and inactiveDate values
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:activate-deactivate-tasks
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/activate-deactivate-tasks.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "JSON"]
section_ids:
  activate-task: The activate task
  expire-task: The expire task
---

# Activate and deactivate accounts

The default IDM configuration includes two scanning tasks that *activate* and *deactivate* a user's `accountStatus`, based on their `activeDate` and `inactiveDate`. The tasks run once a day by default.

|   |                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Both tasks are disabled by default. To enable them, set `"enabled" : true` in the schedule configuration *(tooltip: You can create and change schedule configurations over REST at the openidm/scheduler/job endpoint, or directly in conf/schedule-schedule-name.json files.)* for each task. |

## The `activate` task

The `activate` task (`conf/schedule-taskscan_activate.json`) has the following configuration:

```json
{
  "enabled" : false,
  "type" : "simple",
  "repeatInterval" : 86400000,
  "persisted" : true,
  "concurrentExecution" : false,
  "invokeService" : "taskscanner",
  "invokeContext" : {
    "waitForCompletion" : false,
    "numberOfThreads" : 5,
    "scan" : {
      "_queryFilter" : "((/activeDate le \"${Time.nowWithOffset}\") AND (!(/inactiveDate pr) or /inactiveDate ge \"${Time.nowWithOffset}\"))",
      "object" : "managed/user",
      "taskState" : {
        "started" : "/activateAccount/task-started",
        "completed" : "/activateAccount/task-completed"
      },
      "recovery" : {
        "timeout" : "10m"
      }
    },
    "task" : {
      "script" : {
        "type" : "text/javascript",
        "globals" : { },
        "source" : "var patch = [{ \"operation\" : \"replace\", \"field\" : \"/accountStatus\", \"value\" : \"active\" }];\n\nlogger.debug(\"Performing Activate Account Task on {} ({})\", input.mail, objectID);\n\nopenidm.patch(objectID, null, patch); true;"
      }
    }
  }
}
```

When you run this task, a user account is *activated* if both of the following are true:

* Their `activeDate` is less than or equal to the value of `Time.nowWithOffset`.

* Their `inactiveDate` is greater than or equal to the value of `Time.nowWithOffset`, or they do not have an `inactiveDate` set.

  |   |                                                                                                       |
  | - | ----------------------------------------------------------------------------------------------------- |
  |   | `Time.nowWithOffset` is the current time plus the UTC time offset for the user's geographical region. |

## The `expire` task

The `expire` task (`conf/schedule-taskscan_expire.json`) has the following configuration:

```json
{
  "enabled" : false,
  "type" : "simple",
  "repeatInterval" : 86400000,
  "persisted" : true,
  "concurrentExecution" : false,
  "invokeService" : "taskscanner",
  "invokeContext" : {
    "waitForCompletion" : false,
    "numberOfThreads" : 5,
    "scan" : {
      "_queryFilter" : "((/inactiveDate lt \"${Time.nowWithOffset}\") AND (!(/activeDate pr) or /activeDate le \"${Time.nowWithOffset}\"))",
      "object" : "managed/user",
      "taskState" : {
        "started" : "/expireAccount/task-started",
        "completed" : "/expireAccount/task-completed"
      },
      "recovery" : {
        "timeout" : "10m"
      }
    },
    "task" : {
      "script" : {
        "type" : "text/javascript",
        "globals" : { },
        "source" : "var patch = [{ \"operation\" : \"replace\", \"field\" : \"/accountStatus\", \"value\" : \"inactive\" }];\n\nlogger.debug(\"Performing Expire Account Task on {} ({})\", input.mail, objectID);\n\nopenidm.patch(objectID, null, patch); true;"
      }
    }
  }
}
```

When you run this task, a user account is *deactivated* if both of the following are true:

* Their `inactiveDate` (expiry date) is less than the value of `Time.nowWithOffset`.

* Their `activeDate` is less than or equal to the value of `Time.nowWithOffset`, or they do not have an `activeDate` set.

  |   |                                                                                                       |
  | - | ----------------------------------------------------------------------------------------------------- |
  |   | `Time.nowWithOffset` is the current time plus the UTC time offset for the user's geographical region. |

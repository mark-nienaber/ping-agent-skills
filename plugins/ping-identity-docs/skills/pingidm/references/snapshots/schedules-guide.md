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

---

---
title: Configure schedules
description: Configure PingIDM schedules using the admin UI or REST API, covering schedule properties, triggers, and job management operations
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:configure-schedules
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/configure-schedules.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "Rest", "Configuration", "Triggers"]
section_ids:
  sched-config-properties: Schedule configuration properties
  schedules-over-rest: Manage schedules using REST
  validating-schedule-syntax: Validate cron trigger expressions
  define-schedules: Define a schedule
  schedule-details: View scheduled job details
  querying-schedules: Query scheduled jobs
  updating-schedules: Update a schedule
  schedules-listing-current-tasks: List running scheduled jobs
  trigger-scheduled-task: Trigger a schedule manually
  pause-scheduled-job: Pause and resume a scheduled job
  schedules-pausing-current-tasks: Pause all scheduled jobs
  schedules-resuming-current-tasks: Resume all scheduled jobs
  query-schedule-triggers: Query schedule triggers
  delete-schedules: Delete a schedule
  schedules-admin-ui: Manage schedules using the admin UI
---

# Configure schedules

You can schedule tasks and events using:

* [Admin UI](#schedules-admin-ui)

* [REST](#schedules-over-rest)

By convention, IDM uses file names of the form `schedule-schedule-name.json`, where schedule-name is a logical name for the scheduled operation; for example, `schedule-reconcile_systemCsvAccounts_managedUser.json`. There are several example schedule configuration files in the `openidm/samples/example-configurations/schedules` directory.

Each schedule configuration has the following format:

```json
{
 "enabled"             : boolean,
 "persisted"           : boolean,
 "recoverable"         : boolean,
 "concurrentExecution" : boolean,
 "type"                : "simple | cron",
 "repeatInterval"      : (optional) integer,
 "repeatCount"         : (optional) integer,
 "startTime"           : "(optional) time",
 "endTime"             : "(optional) time",
 "schedule"            : "cron expression",
 "misfirePolicy"       : "optional, string",
 "invokeService"       : "service identifier",
 "invokeContext"       : "service specific context info",
 "invokeLogLevel"      : "(optional) level"
}
```

## Schedule configuration properties

The schedule configuration properties are defined as follows:

* `enabled`

  Set to `true` to enable the schedule. When this property is `false`, IDM considers the schedule configuration dormant, and does not allow it to be triggered or launched.

  If you want to retain a schedule configuration, but do not want it used, set `enabled` to `false` for task and event schedulers, instead of changing the configuration or `cron` expressions.

* `persisted` (optional)

  Specifies whether the schedule state should be persisted or stored only in memory. Boolean (`true` or `false`), `true` by default.

  In a clustered environment, this property must be set to `true` to have the schedule fire only once across the cluster. For more information, refer to [Configure Persistent Schedules](persistent-schedules.html).

  |   |                                                                      |
  | - | -------------------------------------------------------------------- |
  |   | If the schedule is stored only in memory, it is lost on IDM restart. |

  |   |                                                                                                                                                                                          |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Non-persisted (in memory) schedules are [deprecated](../release-notes/deprecated-functionality.html#deprecation-non-persisted-schedules) and will be removed in a future release of IDM. |

* `recoverable` (optional)

  Specifies whether jobs that have failed mid-execution (as a result of a JVM crash or otherwise unexpected termination) should be recovered. Boolean (`true` or `false`), `false` by default.

* `concurrentExecution`

  Specifies whether multiple instances of the same schedule can run concurrently. Boolean (`true` or `false`), `false` by default. Multiple instances of the same schedule cannot run concurrently by default. This setting prevents a new scheduled task from being launched before the same previously launched task has completed. For example, under normal circumstances you would want a liveSync operation to complete before the same operation was launched again. To enable multiple schedules to run concurrently, set this parameter to `true`. The behavior of missed scheduled tasks is governed by the [misfire policy](#misfire-policy).

* `type`

  The trigger type, either `simple` or `cron`.

  To decide which trigger type to use, refer to the Quartz documentation on [SimpleTriggers](https://www.quartz-scheduler.org/documentation/quartz-2.5.x/tutorials/tutorial-lesson-05.html) and [CronTriggers](https://www.quartz-scheduler.org/documentation/quartz-2.5.x/tutorials/crontrigger.html).

* `repeatCount`

  Used only for simple triggers (`"type" : "simple"`).

  The number of times the schedule must be repeated. The repeat count can be zero, a positive integer, or -1. A value of -1 indicates that the schedule should repeat indefinitely.

  If you do not specify a repeat count, the value defaults to -1.

* `repeatInterval`

  Used only for simple triggers (`"type" : "simple"`).

  Specifies the interval, in milliseconds, between trigger firings. The repeat interval must be zero or a positive long value. If you set the repeat interval to zero, the scheduler will trigger `repeatCount` firings concurrently (or as close to concurrently as possible).

  If you do not specify a repeat interval, the value defaults to 0.

* `startTime` (optional)

  This parameter starts the schedule at some time in the future. If the parameter is omitted, empty, or set to a time in the past, the task or event is scheduled to start immediately.

  Use ISO 8601 format to specify times and dates (`yyyy-MM-dd'T'HH:mm:ss`).

  To specify a time zone, include the time zone at the end of the `startTime`, in the format `+|-hh:mm`; for example `2017-10-31T15:53:00+05:00`. If you specify both a `startTime` and an `endTime`, they must have the same time zone.

* `endTime` (optional)

  Specifies when the schedule must end, in ISO 8601 format (`yyyy-MM-dd'T'HH:mm:ss+|-hh:mm`).

* `schedule`

  Used only for cron triggers (`"type" : "cron"`).

  Takes `cron` expression syntax. Learn more in [CronTrigger Tutorial](https://www.quartz-scheduler.org/documentation/quartz-2.5.x/tutorials/crontrigger.html) and [Lesson 6: CronTrigger](https://www.quartz-scheduler.org/documentation/quartz-2.5.x/tutorials/tutorial-lesson-06.html).

- `misfirePolicy`

  This optional parameter specifies the behavior if IDM misses a scheduled task in a persistent schedule.

  Simple schedules only support the `MISFIRE_INSTRUCTION_FIRE_NOW` value.

  For cron-based schedules, the possible values include:

  * `fireAndProceed`. IDM attempts to run the missed schedule when the server is back online and discards all subsequent runs. After this, the normal schedule is resumed.

  * `doNothing`. IDM discards all missed schedules and resumes the normal schedule when the server is back online.

- `invokeService`

  Defines the type of scheduled event or action. The value of this parameter can be one of the following:

  * `sync` for reconciliation.

  * `provisioner` for liveSync.

  * `script` to call some other scheduled operation defined in a script.

  * `taskScanner` to define a scheduled task that queries a set of objects. For more information, refer to [Scan data to trigger tasks](task-scanner.html).

- `invokeContext`

  Specifies contextual information, depending on the type of scheduled event (the value of the `invokeService` parameter).

  The following example invokes reconciliation:

  ```json
  {
      "invokeService": "sync",
      "invokeContext": {
          "action": "reconcile",
          "mapping": "systemLdapAccount_managedUser"
      }
  }
  ```

  The following example invokes a liveSync operation:

  ```json
  {
      "invokeService": "provisioner",
      "invokeContext": {
          "action": "liveSync",
          "source": "system/ldap/__ACCOUNT__"
      }
  }
  ```

  For scheduled liveSync tasks, the `source` property follows IDM's convention for a pointer to an external resource object and takes the form `system/resource-name/object-type`.

  The following example invokes a script, which prints the node ID performing the scheduled job and the time to the console.

  A similar sample schedule is provided in `schedule-script.json` in the `/path/to/openidm/samples/example-configurations/schedules` directory.

  ```json
  {
      "enabled" : true,
      "type": "simple",
      "repeatInterval": 3600000,
      "persisted" : true,
      "concurrentExecution" : false,
      "invokeService": "script",
      "invokeContext": {
          "script" : {
              "type" : "text/javascript",
              "source" : "java.lang.System.out.println('Job executing on ' + identityServer.getProperty('openidm.node.id') + ' at: ' + java.lang.System.currentTimeMillis());"
          }
      }
  }
  ```

  |   |                                                                                                                        |
  | - | ---------------------------------------------------------------------------------------------------------------------- |
  |   | These are sample configurations only. Your schedule configuration will differ according to your specific requirements. |

- `invokeLogLevel` (optional)

  Specifies the level at which the invocation will be logged. Particularly for schedules that run very frequently, such as liveSync, the scheduled task can generate significant output to the log file, and you should adjust the log level accordingly. The default schedule log level is `info`. The value can be set to any one of the [SLF4J](http://www.slf4j.org/apidocs/org/apache/commons/logging/Log.html) log levels:

  * `trace`

  * `debug`

  * `info`

  * `warn`

  * `error`

  * `fatal`

## Manage schedules using REST

The scheduler service is exposed under the `/openidm/scheduler` context path. Within this context path, the defined scheduled jobs are accessible at `/openidm/scheduler/job`. A *job* is the actual task that is run. Each job contains a *trigger* that starts the job. The trigger defines the schedule according to which the job is executed. You can read and query the existing triggers on the `/openidm/scheduler/trigger` context path.

The following examples show how schedules are validated, created, read, queried, updated, and deleted, over REST, by using the scheduler service.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you configure schedules over REST, changes made to the schedules aren't pushed back into the configuration service. Managing schedules by using the `/openidm/scheduler/job` context path essentially bypasses the configuration service and sends the request directly to the scheduler.If you need to perform an operation on a schedule that was created by using the configuration service by placing a schedule file in the `conf/` directory, you must direct your request to the `/openidm/config/schedule` context path and not to the `/openidm/scheduler/job` context path.PATCH operations are not supported on the `scheduler` context path. To patch a schedule, use the `config` context path. |

### Validate cron trigger expressions

Schedules are defined using Quartz cron or simple triggers. If you use a cron trigger, you can validate your cron expression by sending the expression as a JSON object to the `scheduler` context path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
--data '{
    "cronExpression": "0 0/1 * * * ?"
}' \
"http://localhost:8080/openidm/scheduler/job?_action=validateQuartzCronExpression"
{
  "valid": true
}
```

### Define a schedule

To define a new schedule, send a PUT or POST request to the `scheduler/job` context path with the details of the schedule in the JSON payload. A PUT request lets you specify the ID of the schedule. A POST request assigns an ID automatically.

The following example uses a PUT request to create a schedule that fires a script (`script/testlog.js`) every second. The example assumes that the script exists in the specified location. The schedule configuration is as described in [Configure Schedules](configure-schedules.html):

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0" \
--request PUT \
--data '{
    "enabled": true,
    "type": "cron",
    "schedule": "0/1 * * * * ?",
    "persisted": true,
    "misfirePolicy": "fireAndProceed",
    "invokeService": "script",
    "invokeContext": {
        "script": {
            "type": "text/javascript",
            "file": "script/testlog.js"
        }
    }
}' \
"http://localhost:8080/openidm/scheduler/job/testlog-schedule"
{
  "_id": "testlog-schedule",
  "enabled": true,
  "persisted": true,
  "recoverable": false,
  "misfirePolicy": "fireAndProceed",
  "schedule": "0/1 * * * * ?",
  "repeatInterval": 0,
  "repeatCount": 0,
  "type": "cron",
  "invokeService": "org.forgerock.openidm.script",
  "invokeContext": {
    "script": {
      "type": "text/javascript",
      "file": "script/testlog.js"
    }
  },
  "invokeLogLevel": "info",
  "startTime": null,
  "endTime": null,
  "concurrentExecution": false,
  "triggers": [
    {
      "calendar": null,
      "group": "scheduler-service-group",
      "jobKey": "scheduler-service-group.testlog-schedule",
      "name": "trigger-testlog-schedule",
      "nodeId": "node1",
      "previousState": null,
      "serialized": {
        "type": "CronTriggerImpl",
        "calendarName": null,
        "cronEx": {
          "cronExpression": "0/1 * * * * ?",
          "timeZone": "Africa/Johannesburg"
        },
        "description": null,
        "endTime": null,
        "fireInstanceId": "node1_1570611359345",
        "group": "scheduler-service-group",
        "jobDataMap": {
          "scheduler.invokeService": "org.forgerock.openidm.script",
          "scheduler.config-name": "scheduler-testlog-schedule",
          "scheduler.invokeContext": {
            "script": {
              "type": "text/javascript",
              "file": "script/testlog.js"
            }
          },
          "schedule.config": {
            "enabled": true,
            "persisted": true,
            "recoverable": false,
            "misfirePolicy": "fireAndProceed",
            "schedule": "0/1 * * * * ?",
            "repeatInterval": 0,
            "repeatCount": 0,
            "type": "cron",
            "invokeService": "org.forgerock.openidm.script",
            "invokeContext": {
              "script": {
                "type": "text/javascript",
                "file": "script/testlog.js"
              }
            },
            "invokeLogLevel": "info",
            "startTime": null,
            "endTime": null,
            "concurrentExecution": false
          },
          "scheduler.invokeLogLevel": "info"
        },
        "jobGroup": "scheduler-service-group",
        "jobName": "testlog-schedule",
        "misfireInstruction": 1,
        "name": "trigger-testlog-schedule",
        "nextFireTime": 1570611569000,
        "previousFireTime": 1570611568000,
        "priority": 5,
        "startTime": 1570611391000,
        "volatility": false
      },
      "state": "NORMAL",
      "_rev": "000000001d4724d6",
      "_id": "scheduler-service-group.trigger-testlog-schedule"
    }
  ],
  "previousRunDate": "2019-10-09T08:59:28.000Z",
  "nextRunDate": "2019-10-09T08:59:29.000Z"
}
```

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The previous output includes the `trigger` that was created as part of the scheduled job, as well as the `nextRunDate` for the job. For more information about the `trigger` properties, refer to [Query Schedule Triggers](#query-schedule-triggers). |

The following example uses a POST request to create an identical schedule to the one created in the previous example, but with a *server-assigned ID*:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
--data '{
    "enabled": true,
    "type": "cron",
    "schedule": "0/1 * * * * ?",
    "persisted": true,
    "misfirePolicy": "fireAndProceed",
    "invokeService": "script",
    "invokeContext": {
        "script": {
            "type": "text/javascript",
            "file": "script/testlog.js"
        }
    }
}' \
"http://localhost:8080/openidm/scheduler/job?_action=create"
{
  "_id": "b12e4a77-a626-4a38-a1dc-8edc7498ca1c",
  "enabled": true,
  "persisted": true,
  "recoverable": false,
  "misfirePolicy": "fireAndProceed",
  "schedule": "0/1 * * * * ?",
  "repeatInterval": 0,
  "repeatCount": 0,
  "type": "cron",
  "invokeService": "org.forgerock.openidm.script",
  "invokeContext": {
    "script": {
      "type": "text/javascript",
      "file": "script/testlog.js"
    }
  },
  "invokeLogLevel": "info",
  "startTime": null,
  "endTime": null,
  "concurrentExecution": false,
  "triggers": [
    {
      "calendar": null,
      "group": "scheduler-service-group",
      "jobKey": "scheduler-service-group.b12e4a77-a626-4a38-a1dc-8edc7498ca1c",
      "name": "trigger-b12e4a77-a626-4a38-a1dc-8edc7498ca1c",
      "nodeId": null,
      "previousState": null,
      "serialized": {
        "type": "CronTriggerImpl",
        "calendarName": null,
        "cronEx": {
          "cronExpression": "0/1 * * * * ?",
          "timeZone": "Africa/Johannesburg"
        },
        "description": null,
        "endTime": null,
        "fireInstanceId": null,
        "group": "scheduler-service-group",
        "jobDataMap": {
          "scheduler.invokeService": "org.forgerock.openidm.script",
          "scheduler.config-name": "scheduler-b12e4a77-a626-4a38-a1dc-8edc7498ca1c",
          "scheduler.invokeContext": {
            "script": {
              "type": "text/javascript",
              "file": "script/testlog.js"
            }
          },
          "schedule.config": {
            "enabled": true,
            "persisted": true,
            "recoverable": false,
            "misfirePolicy": "fireAndProceed",
            "schedule": "0/1 * * * * ?",
            "repeatInterval": 0,
            "repeatCount": 0,
            "type": "cron",
            "invokeService": "org.forgerock.openidm.script",
            "invokeContext": {
              "script": {
                "type": "text/javascript",
                "file": "script/testlog.js"
              }
            },
            "invokeLogLevel": "info",
            "startTime": null,
            "endTime": null,
            "concurrentExecution": false
          },
          "scheduler.invokeLogLevel": "info"
        },
        "jobGroup": "scheduler-service-group",
        "jobName": "b12e4a77-a626-4a38-a1dc-8edc7498ca1c",
        "misfireInstruction": 1,
        "name": "trigger-b12e4a77-a626-4a38-a1dc-8edc7498ca1c",
        "nextFireTime": 1570611659000,
        "previousFireTime": null,
        "priority": 5,
        "startTime": 1570611659000,
        "volatility": false
      },
      "state": "NORMAL",
      "_rev": "000000009e2e2212",
      "_id": "scheduler-service-group.trigger-b12e4a77-a626-4a38-a1dc-8edc7498ca1c"
    }
  ],
  "previousRunDate": null,
  "nextRunDate": "2019-10-09T09:00:59.000Z"
}
```

The output includes the generated `_id` of the schedule, in this case:

```
"_id": "b12e4a77-a626-4a38-a1dc-8edc7498ca1c"
```

### View scheduled job details

The following example displays the details of the schedule created in the previous example. Specify the job ID in the URL:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"http://localhost:8080/openidm/scheduler/job/testlog-schedule"
{
  "_id": "testlog-schedule",
  "enabled": true,
  "persisted": true,
  "recoverable": false,
  "misfirePolicy": "fireAndProceed",
  "schedule": "0/1 * * * * ?",
  "repeatInterval": 0,
  "repeatCount": 0,
  "type": "cron",
  "invokeService": "org.forgerock.openidm.script",
  "invokeContext": {
    "script": {
      "type": "text/javascript",
      "file": "script/testlog.js"
    }
  },
  "invokeLogLevel": "info",
  "startTime": null,
  "endTime": null,
  "concurrentExecution": false,
  "triggers": [
    {
      "calendar": null,
      "group": "scheduler-service-group",
      "jobKey": "scheduler-service-group.testlog-schedule",
      "name": "trigger-testlog-schedule",
      "nodeId": null,
      "previousState": null,
      "serialized": {
        "type": "CronTriggerImpl",
        "calendarName": null,
        "cronEx": {
          "cronExpression": "0/1 * * * * ?",
          "timeZone": "Africa/Johannesburg"
        },
        "description": null,
        "endTime": null,
        "fireInstanceId": "node1_1570611359712",
        "group": "scheduler-service-group",
        "jobDataMap": {
          "scheduler.invokeService": "org.forgerock.openidm.script",
          "scheduler.config-name": "scheduler-testlog-schedule",
          "scheduler.invokeContext": {
            "script": {
              "type": "text/javascript",
              "file": "script/testlog.js"
            }
          },
          "schedule.config": {
            "enabled": true,
            "persisted": true,
            "recoverable": false,
            "misfirePolicy": "fireAndProceed",
            "schedule": "0/1 * * * * ?",
            "repeatInterval": 0,
            "repeatCount": 0,
            "type": "cron",
            "invokeService": "org.forgerock.openidm.script",
            "invokeContext": {
              "script": {
                "type": "text/javascript",
                "file": "script/testlog.js"
              }
            },
            "invokeLogLevel": "info",
            "startTime": null,
            "endTime": null,
            "concurrentExecution": false
          },
          "scheduler.invokeLogLevel": "info"
        },
        "jobGroup": "scheduler-service-group",
        "jobName": "testlog-schedule",
        "misfireInstruction": 1,
        "name": "trigger-testlog-schedule",
        "nextFireTime": 1570611719000,
        "previousFireTime": 1570611718000,
        "priority": 5,
        "startTime": 1570611391000,
        "volatility": false
      },
      "state": "NORMAL",
      "_rev": "000000002d1c2465",
      "_id": "scheduler-service-group.trigger-testlog-schedule"
    }
  ],
  "previousRunDate": "2019-10-09T09:01:58.000Z",
  "nextRunDate": "2019-10-09T09:01:59.000Z"
}
```

### Query scheduled jobs

You can query defined and running scheduled jobs using a regular [query filter](../objects-guide/queries.html#constructing-queries).

The following query returns the IDs of all defined schedules:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"http://localhost:8080/openidm/scheduler/job?_queryFilter=true&_fields=_id"
{
  "result": [
    {
      "_id": "reconcile_systemLdapAccounts_managedUser"
    },
    {
      "_id": "testlog-schedule"
    }
  ]
  ...
}
```

The following query returns the IDs, enabled status, and next run date of all defined schedules:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"http://localhost:8080/openidm/scheduler/job?_queryFilter=true&_fields=_id,enabled,nextRunDate"
{
  "result": [
    {
      "_id": "reconcile_systemLdapAccounts_managedUser",
      "enabled": false,
      "nextRunDate": null
    },
    {
      "_id": "testlog-schedule",
      "enabled": true,
      "nextRunDate": "2019-10-09T09:43:17.000Z"
    }
  ]
  ...
}
```

### Update a schedule

To update a schedule definition, use a PUT request and update all the static properties of the object.

This example disables the `testlog` schedule created in the previous example by setting `"enabled":false`:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0" \
--request PUT \
--data '{
    "enabled": false,
    "type": "cron",
    "schedule": "0/1 * * * * ?",
    "persisted": true,
    "misfirePolicy": "fireAndProceed",
    "invokeService": "script",
    "invokeContext": {
        "script": {
            "type": "text/javascript",
            "file": "script/testlog.js"
        }
    }
}' \
"http://localhost:8080/openidm/scheduler/job/testlog-schedule"
{
  "_id": "testlog-schedule",
  "enabled": false,
  "persisted": true,
  "recoverable": false,
  "misfirePolicy": "fireAndProceed",
  "schedule": "0/1 * * * * ?",
  "repeatInterval": 0,
  "repeatCount": 0,
  "type": "cron",
  "invokeService": "org.forgerock.openidm.script",
  "invokeContext": {
    "script": {
      "type": "text/javascript",
      "file": "script/testlog.js"
    }
  },
  "invokeLogLevel": "info",
  "startTime": null,
  "endTime": null,
  "concurrentExecution": false,
  "triggers": [],
  "previousRunDate": null,
  "nextRunDate": null
}
```

When you disable a schedule, all triggers are removed, and the `nextRunDate` is set to `null`. If you re-enable the schedule, a new trigger is generated, and the `nextRunDate` is recalculated.

### List running scheduled jobs

This example returns a list of the jobs that are currently executing. The list lets you decide whether to wait for a specific job to complete before shutting down a server.

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * This action does not list the jobs across a cluster, only the jobs currently executing on the node to which the request is routed.

* The list is accurate only at the moment the request was issued, and can change at any time after the response is received. |

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
"http://localhost:8080/openidm/scheduler/job?_action=listCurrentlyExecutingJobs"
[
  {
    "enabled": true,
    "persisted": true,
    "misfirePolicy": "fireAndProceed",
    "type": "simple",
    "repeatInterval": 3600000,
    "repeatCount": -1,
    "invokeService": "org.forgerock.openidm.sync",
    "invokeContext": {
      "action": "reconcile",
      "mapping": "systemLdapAccounts_managedUser"
    },
    "invokeLogLevel": "info",
    "timeZone": null,
    "startTime": null,
    "endTime": null,
    "concurrentExecution": false
  }
]
```

### Trigger a schedule manually

For testing purposes, and for certain administrative tasks, you can trigger a scheduled task manually, outside of its specified schedule. A scheduled task must be `enabled` before it can be triggered.

This command triggers the `testlog-schedule` job created previously:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
"http://localhost:8080/openidm/scheduler/job/testlog-schedule?_action=trigger"
{
  "success": true
}
```

|   |                                                                              |
| - | ---------------------------------------------------------------------------- |
|   | This action is available only from version 2.0 of the scheduler API onwards. |

### Pause and resume a scheduled job

Instead of deleting and recreating scheduled jobs, you can pause and resume them if necessary. This command pauses the `testlog-schedule` job:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
"http://localhost:8080/openidm/scheduler/job/testlog-schedule?_action=pause"
{
  "success": true
}
```

This command resumes the `testlog-schedule` job:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
"http://localhost:8080/openidm/scheduler/job/testlog-schedule?_action=resume"
{
  "success": true
}
```

|   |                                                                                 |
| - | ------------------------------------------------------------------------------- |
|   | These actions are available only from version 2.0 of the scheduler API onwards. |

### Pause all scheduled jobs

You can temporarily suspend all scheduled jobs. This action does not cancel or interrupt jobs that are already in progress; it simply prevents any scheduled jobs from being invoked during the suspension period.

This command suspends all scheduled tasks and returns `true` if the tasks could be suspended successfully:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
"http://localhost:8080/openidm/scheduler/job?_action=pauseJobs"
{
  "success": true
}
```

### Resume all scheduled jobs

You can resume scheduled jobs to start them up again. Any jobs that were missed during the downtime follow their configured [`misfirePolicy`](#misfire-policy).

This command resumes all scheduled jobs and returns `true` if the jobs could be resumed successfully:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
"http://localhost:8080/openidm/scheduler/job?_action=resumeJobs"
{
  "success": true
}
```

### Query schedule triggers

When a scheduled job is created, a trigger for that job is created automatically and is included in the schedule definition. The trigger is essentially what causes the job to be started. You can read all the triggers that have been generated on a system with the following query on the `openidm/scheduler/trigger` context path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"http://localhost:8080/openidm/scheduler/trigger?_queryFilter=true"
{
  "result": [
    {
      "_id": "scheduler-service-group.trigger-testlog-schedule",
      "_rev": "00000000db3523f1",
      "calendar": null,
      "group": "scheduler-service-group",
      "jobKey": "scheduler-service-group.testlog-schedule",
      "name": "trigger-testlog-schedule",
      "nodeId": "node1",
      "previousState": null,
      "serialized": {
      ...
      },
      "state": "NORMAL"
    }
  ]
}
```

The trigger object contents are:

* `_id`

  The ID of the trigger, which is based on the schedule ID. The trigger ID is made up of the group name, followed by `trigger-` prepended to the schedule ID: `group.trigger-schedule-id`. For example, if the schedule ID was `testlog-schedule`, then the trigger ID would be `scheduler-service-group.trigger-testlog-schedule`.

* `_rev`

  The revision of the trigger object. This property is reserved for internal use and specifies the revision of the object in the repository. This is the same value that is exposed as the object's ETag through the REST API. The content of this property is not defined. No consumer should make any assumptions of its content beyond equivalence comparison.

* `previousState`

  The previous state of the trigger, before its current state. For a description of Quartz trigger states, refer to the [Quartz API documentation](https://www.quartz-scheduler.org/api/2.5.x/org/quartz/Trigger.TriggerState.html).

* `name`

  The trigger name, which matches the ID of the schedule that created the trigger, with `trigger-` added: `trigger-schedule-id`.

* `state`

  The current state of the trigger. For a description of Quartz trigger states, refer to the [Quartz API documentation](https://www.quartz-scheduler.org/api/2.5.x/org/quartz/Trigger.TriggerState.html).

* `nodeId`

  The ID of the node that has acquired the trigger, useful in a clustered deployment. If the trigger has not been acquired by a node yet, this will return `null`.

* `calendar`

  This is a part of the Quartz implementation, but is not currently supported by IDM. This will always return `null`.

* `serialized`

  The JSON serialization of the trigger class.

* `group`

  The name of the group that the trigger is in, always `scheduler-service-group`.

* `jobKey`

  The name of the job associated with the trigger: `group.schedule-id`.

To read the contents of a specific trigger, send a GET request to the trigger ID; for example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"http://localhost:8080/openidm/scheduler/trigger/scheduler-service-group.trigger-testlog-schedule"
{
  "_id": "scheduler-service-group.trigger-testlog-schedule",
  "_rev": "00000000cd1723dd",
  "calendar": null,
  "group": "scheduler-service-group",
  "jobKey": "scheduler-service-group.testlog-schedule",
  "name": "trigger-testlog-schedule",
  "nodeId": "node1",
  "previousState": null,
  "serialized": {
  ...
  },
  "state": "NORMAL"
}
```

To view the triggers that have been acquired, send a GET request to the scheduler, with a `_queryFilter` of `nodeId`. For example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"http://localhost:8080/openidm/scheduler/trigger?_queryFilter=(nodeId+pr)"
```

To view the triggers that have not yet been acquired by any node, send a GET request to the scheduler, with a `_queryFilter` to list the triggers with a null `nodeId`. For example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"http://localhost:8080/openidm/scheduler/trigger?_queryFilter=%21(nodeId+pr)"
```

### Delete a schedule

To delete a schedule, send a DELETE request to the schedule ID. For example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request DELETE \
"http://localhost:8080/openidm/scheduler/job/testlog-schedule"
{
  "_id": "testlog-schedule",
  "enabled": false,
  "persisted": true,
  "recoverable": false,
  "misfirePolicy": "fireAndProceed",
  "schedule": "0/1 * * * * ?",
  "repeatInterval": 0,
  "repeatCount": 0,
  "type": "cron",
  "invokeService": "org.forgerock.openidm.script",
  "invokeContext": {
    "script": {
      "type": "text/javascript",
      "file": "script/testlog.js"
    }
  },
  "invokeLogLevel": "info",
  "startTime": null,
  "endTime": null,
  "concurrentExecution": false,
  "triggers": [],
  "previousRunDate": null,
  "nextRunDate": null
}
```

The DELETE request returns the entire JSON object.

## Manage schedules using the admin UI

To manage schedules using the admin UI, click Configure > Schedules.

Add, remove, and change schedules here. By default, only persisted schedules are shown in the Schedules list. To show non-persisted (in memory) schedules, select Filter by Type > In Memory.

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Non-persisted (in memory) schedules are [deprecated](../release-notes/deprecated-functionality.html#deprecation-non-persisted-schedules) and will be removed in a future release of IDM. |

![ui-schedules](_images/ui-schedules.png)

---

---
title: Configure the scheduler service
description: Configure the PingIDM scheduler service, including thread pool size and whether persistent schedules execute on a node
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:scheduler-configuration-file
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/scheduler-configuration-file.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks"]
---

# Configure the scheduler service

There is a distinction between the configuration of the scheduler service, and the configuration of individual scheduled tasks and events. The scheduler configuration *(tooltip: You can edit the scheduler configuration over REST at the openidm/scheduler endpoint, or directly in the conf/scheduler.json file.)* has the following format, and configures the Quartz Scheduler:

```json
{
    "threadPool" : {
        "threadCount" : 10
    },
    "scheduler" : {
        "executePersistentSchedules" : {
            "$bool" : "&{openidm.scheduler.execute.persistent.schedules}"
        }
    }
}
```

* `threadCount` specifies the maximum number of threads that are available for running scheduled tasks concurrently.

* `executePersistentSchedules` lets you disable persistent schedules for a specific node. If this parameter is set to `false`, the Scheduler Service will support the management of persistent schedules (CRUD operations) but it will not run any persistent schedules. The value of this property can be a string or boolean. Its default value (set in `resolver/boot.properties` ) is `true`.

---

---
title: Create a new scanning task
description: Configure a PingIDM scanning task using a schedule definition, query filter, task state tracking, and script invocation
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:task-scanner-config
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/task-scanner-config.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "Rest", "JSON"]
---

# Create a new scanning task

The following example (`openidm/samples/example-configurations/task-scanner/conf/schedule-taskscan_sunset.json`) defines a scheduled scanning task that triggers a sunset script:

```json
{
  "enabled" : true,
  "type" : "simple",
  "repeatInterval" : 3600000,
  "persisted": true,
  "concurrentExecution" : false,
  "invokeService" : "taskscanner",
  "invokeContext" : {
    "waitForCompletion" : false,
    "numberOfThreads" : 5,
    "scan" : {
      "_queryFilter" : "((/sunset/date lt \"${Time.now}\") AND !(/sunset/task-completed pr))",
      "object" : "managed/user",
      "taskState" : {
        "started" : "/sunset/task-started",
        "completed" : "/sunset/task-completed"
      },
      "recovery" : {
        "timeout" : "10m"
      }
    },
    "task" : {
      "script" : {
        "type" : "text/javascript",
        "file" : "script/sunset.js"
      }
    }
  }
}
```

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `${Time.now}` macro object fetches the current time and is available only when you configure a scanning task query filter. You can't use the macro outside of this context. |

The schedule configuration calls a script ([`sunset.js`](../_attachments/sunset.js)). To test the sample, copy this file to your project's `script` directory or replace `"file" : "script/sunset.js"` with the script source (`"source" : "contents of sunset.js"`). The sample script marks all user objects that match the specified conditions as inactive. You can use this sample script to trigger a specific workflow, or any other task associated with the sunset process.

The task will only execute on users who have a valid `sunset/date` field. You can add a `sunset/date` field to user entries over REST. To make the field visible in the admin UI, you must add it to your managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*.

This example command adds a `sunset/date` field to `bjensen`'s entry, over REST:

```
curl \
--header "Content-Type: application/json" \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
--data '[{
  "operation" : "add",
  "field" : "sunset/date",
  "value" : "2019-12-20T12:00:00Z"
}]' \
"http://localhost:8080/openidm/managed/user?_action=patch&_queryFilter=userName+eq+'bjensen'"
```

The remaining properties in the schedule configuration are as follows:

The `invokeContext` parameter takes the following properties:

* `waitForCompletion` (optional)

  This property specifies whether the task should be performed synchronously. Tasks are performed asynchronously by default (with `waitForCompletion` set to false). A task ID (such as `{"_id":"354ec41f-c781-4b61-85ac-93c28c180e46"}`) is returned immediately. If this property is set to true, tasks are performed synchronously, and the ID is not returned until all tasks have completed.

* `maxRecords` (optional)

  The maximum number of records that can be processed. This property is not set by default so the number of records is unlimited. If a maximum number of records is specified, that number will be spread evenly over the number of threads.

* `numberOfThreads` (optional)

  By default, the task scanner runs in a multi-threaded manner; that is, numerous threads are dedicated to the same scanning task run. Multi-threading generally improves the performance of the task scanner. The default number of threads for a single scanning task is 10. To change this default, set the `numberOfThreads` property. The sample configuration sets the default number of threads to 5.

* `scan`

  The details of the scan. The following properties are defined:

  * `_queryFilter`

    The query filter that identifies the entries for which this task should be run.

    The query filter provided in the sample schedule configuration (`/sunset/date lt \"${Time.now}\") AND !(/sunset/task-completed pr`) identifies managed users whose `sunset/date` property is before the current date and for whom the sunset task has not yet completed.

    The sample query supports time-based conditions, with the time specified in ISO 8601 format (Zulu time). You can write any query to target the set of entries that you want to scan.

    For time-based queries, it's possible to use the `${Time.now}` macro object (which fetches the current time). You can also specify any date/time in relation to the current time, using the ``` ` or `-` operator, and a duration modifier. For example: changing the sample query to `${Time.now + 1d}` would return all user objects whose `/sunset/date` is the following day (current time plus one day). Note: you must include space characters around the operator (`` or -` ```). The duration modifier supports the following unit specifiers:

    * `s` second

    * `m` minute

    * `h` hour

    * `d` day

    * `M` month

    * `y` year

  * `object`

    Defines the managed object type against which the query should be performed, as defined in the `managed.json` file.

  * `taskState`

    Indicates the names of the fields in which the start message, and the completed message are stored. These fields are used to track the status of the task.

    * `started`

      specifies the field that stores the timestamp for when the task begins.

    * `completed`

      specifies the field that stores the timestamp for when the task completes its operation. The `completed` field is present as soon as the task has started, but its value is `null` until the task has completed.

  * `recovery` (optional)

    Specifies a configurable `timeout`, after which the task scanner process ends. For clustered IDM instances, there might be more than one task scanner running at a time. A task cannot be launched by two task scanners at the same time. When one task scanner "claims" a task, it indicates that the task has been started. That task is then unavailable to be claimed by another task scanner and remains unavailable until the end of the task is indicated. In the event that the first task scanner does not complete the task by the specified timeout, for whatever reason, a second task scanner can pick up the task.

* `task`

  Provides details of the task that is performed. Usually, the task is invoked by a script, whose details are defined in the `script` property:

  * `type`

    The script type.

    IDM supports `"text/javascript"` and `"groovy"`.

  * `file`

    The path to the script file. The script file takes at least two objects (in addition to the default objects that are provided to all IDM scripts):

    * `input`

      The individual object that is retrieved from the query (in the example, this is the individual user object).

    * `objectID`

      A string that contains the full identifier of the object. The `objectID` is useful for performing updates with the script as it allows you to target the object directly. For example: `openidm.update(objectID, input['_rev'], input);`.

|   |                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------ |
|   | For more information about using scripts, refer to [Scripting function reference](../scripting-guide/scripting-func-ref.html). |

---

---
title: Manage scanning tasks
description: Manage PingIDM scanning tasks using REST or the admin UI, including triggering, canceling, and listing tasks
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:manage-scanning-tasks
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/manage-scanning-tasks.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "Rest", "User Interface"]
---

# Manage scanning tasks

Once you create scanning tasks, you may want to update them. For example, you might want to trigger, cancel, or list the existing scanning tasks.

You can manage scanning tasks in IDM using:

* [REST](task-scanner-rest.html)

* [Admin UI](task-scanner-ui.html)

---

---
title: Manage scanning tasks using REST
description: Manage PingIDM scanning tasks over REST, including creating, triggering, canceling, and listing tasks with progress details
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:task-scanner-rest
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/task-scanner-rest.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "Rest", "Triggers"]
section_ids:
  create-scanning-task: Create a scanning task
  trigger-task-scanner: Trigger a scanning task
  cancel-task-scanner: Cancel a scanning task
  list-task-scanner: List the scanning tasks
---

# Manage scanning tasks using REST

You can trigger, cancel, and monitor scanning tasks over the REST interface, using the REST endpoint `openidm/taskscanner`.

## Create a scanning task

You can define a scanning task in a configuration file or directly over the REST interface. For an example of a file-based scanning task, refer to the file `/path/to/openidm/samples/example-configurations/task-scanner/conf/schedule-taskscan_sunset.json`.

The following command defines a scanning task named `sunsetTask`:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-type: application/json" \
--header "Accept-API-Version: resource=2.0" \
--request PUT \
--data '{
  "enabled" : true,
  "type" : "simple",
  "repeatInterval" : 3600000,
  "persisted": true,
  "concurrentExecution" : false,
  "invokeService" : "taskscanner",
  "invokeContext" : {
    "waitForCompletion" : false,
    "numberOfThreads" : 5,
    "scan" : {
      "_queryFilter" : "/sunset/date lt \"$\{Time.now}\") AND !(/sunset/task-completed pr",
      "object" : "managed/user",
      "taskState" : {
        "started" : "/sunset/task-started",
        "completed" : "/sunset/task-completed"
      },
      "recovery" : {
        "timeout" : "10m"
      }
    },
    "task" : {
      "script" : {
        "type" : "text/javascript",
        "file" : "script/sunset.js"
      }
    }
  }
}' \
"http://localhost:8080/openidm/scheduler/job/sunsetTask"
{
  "_id": "sunsetTask",
  "enabled": true,
  "persisted": true,
  "recoverable": false,
  "misfirePolicy": "fireAndProceed",
  "schedule": null,
  "repeatInterval": 3600000,
  "repeatCount": -1,
  "type": "simple",
  "invokeService": "org.forgerock.openidm.taskscanner",
  "invokeContext": {
    "waitForCompletion": false,
    "numberOfThreads": 5,
    "scan": {
      "_queryFilter": "/sunset/date lt \"$\{Time.now}\") AND !(/sunset/task-completed pr",
      "object": "managed/user",
      "taskState": {
        "started": "/sunset/task-started",
        "completed": "/sunset/task-completed"
      },
      "recovery": {
        "timeout": "10m"
      }
    },
    "task": {
      "script": {
        "type": "text/javascript",
        "file": "script/sunset.js"
      }
    }
  },
  "invokeLogLevel": "info",
  "startTime": null,
  "endTime": null,
  "concurrentExecution": false,
  "triggers": [
    {
      "calendar": null,
      "group": "scheduler-service-group",
      "jobKey": "scheduler-service-group.sunsetTask",
      "name": "trigger-sunsetTask",
      "nodeId": null,
      "previousState": null,
      "serialized": {
        "type": "SimpleTriggerImpl",
        "calendarName": null,
        "complete": false,
        "description": null,
        "endTime": null,
        "fireInstanceId": null,
        "group": "scheduler-service-group",
        "jobDataMap": {
          "scheduler.invokeService": "org.forgerock.openidm.taskscanner",
          "scheduler.config-name": "scheduler-sunsetTask",
          "scheduler.invokeContext": {
            "waitForCompletion": false,
            "numberOfThreads": 5,
            "scan": {
              "_queryFilter": "/sunset/date lt \"$\{Time.now}\") AND !(/sunset/task-completed pr",
              "object": "managed/user",
              "taskState": {
                "started": "/sunset/task-started",
                "completed": "/sunset/task-completed"
              },
              "recovery": {
                "timeout": "10m"
              }
            },
            "task": {
              "script": {
                "type": "text/javascript",
                "file": "script/sunset.js"
              }
            }
          },
          "schedule.config": {
            "enabled": true,
            "persisted": true,
            "recoverable": false,
            "misfirePolicy": "fireAndProceed",
            "schedule": null,
            "repeatInterval": 3600000,
            "repeatCount": -1,
            "type": "simple",
            "invokeService": "org.forgerock.openidm.taskscanner",
            "invokeContext": {
              "waitForCompletion": false,
              "numberOfThreads": 5,
              "scan": {
                "_queryFilter": "/sunset/date lt \"$\{Time.now}\") AND !(/sunset/task-completed pr",
                "object": "managed/user",
                "taskState": {
                  "started": "/sunset/task-started",
                  "completed": "/sunset/task-completed"
                },
                "recovery": {
                  "timeout": "10m"
                }
              },
              "task": {
                "script": {
                  "type": "text/javascript",
                  "file": "script/sunset.js"
                }
              }
            },
            "invokeLogLevel": "info",
            "startTime": null,
            "endTime": null,
            "concurrentExecution": false
          },
          "scheduler.invokeLogLevel": "info"
        },
        "jobGroup": "scheduler-service-group",
        "jobName": "sunsetTask",
        "misfireInstruction": 1,
        "name": "trigger-sunsetTask",
        "nextFireTime": 1570618094818,
        "previousFireTime": null,
        "priority": 5,
        "repeatCount": -1,
        "repeatInterval": 3600000,
        "startTime": 1570618094818,
        "timesTriggered": 0,
        "volatility": false
      },
      "state": "NORMAL",
      "_rev": "000000006751ccf1",
      "_id": "scheduler-service-group.trigger-sunsetTask"
    }
  ],
  "previousRunDate": null,
  "nextRunDate": "2019-10-09T10:48:14.818Z"
}
```

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `${Time.now}` macro object fetches the current time and is available only when you configure a scanning task query filter. You can't use the macro outside of this context. |

## Trigger a scanning task

To trigger a scanning task over REST, use the `execute` action and specify the `name` of the task (effectively the scheduled job name). To obtain a list of task names, you can query the `/openidm/scheduler/job` endpoint. Note, however, that not all jobs are scanning tasks. Only those jobs that have which have the correct task scanner `invokeContext` can be triggered in this way.

The following example triggers the `sunsetTask` defined in the previous example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/taskscanner?_action=execute&name=sunsetTask"
{
  "_id": "9f2564c8-193c-4871-8869-6080f374b1bd-2073"
}
```

For scanning tasks that are defined in configuration files, you can determine the task name from the file name, for example, `schedule-task-name.json`. The following example triggers a task named `taskscan_sunset` that is defined in a file named `conf/schedule-taskscan_sunset.json`:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/taskscanner?_action=execute&name=taskscan_sunset"
{
  "_id": "8d7742f0-5245-41cf-89a5-de32fc50e326-3323"
}
```

By default, a scanning task ID is returned immediately when the task is initiated. Clients can make subsequent calls to the task scanner service, using this task ID to query its state and to call operations on it.

To have the scanning task complete before the ID is returned, set the `waitForCompletion` property to `true` in the task definition file (`schedule-taskscan_sunset.json`).

## Cancel a scanning task

To cancel a scanning task that is in progress, send a REST call with the `cancel` action, specifying the task ID. The following call cancels the scanning task initiated in the previous example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/taskscanner/9f2564c8-193c-4871-8869-6080f374b1bd-2073?_action=cancel"
{
  "_id":"9f2564c8-193c-4871-8869-6080f374b1bd-2073",
  "status":"SUCCESS"
}
```

|   |                                                               |
| - | ------------------------------------------------------------- |
|   | You cannot cancel a scanning task that has already completed. |

## List the scanning tasks

To retrieve a list of scanning tasks, query the `openidm/taskscanner` context path. The following example displays *all* scanning tasks, regardless of their state:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/taskscanner?_queryFilter=true"
{
  "result": [
    {
      "_id": "9f2564c8-193c-4871-8869-6080f374b1bd-2073",
      "name": "schedule/taskscan_sunset",
      "progress": {
        "state": "COMPLETED",
        "processed": 0,
        "total": 0,
        "successes": 0,
        "failures": 0
      },
      "started": "2017-12-19T11:45:53.433Z",
      "ended": "2017-12-19T11:45:53.438Z"
    },
    {
      "_id": "b32aafe5-b484-4d00-89ff-83554341f321-9970",
      "name": "schedule/taskscan_sunset",
      "progress": {
        "state": "ACTIVE",
        "processed": 80,
        "total": 980,
        "successes": 80,
        "failures": 0
      },
      "started": "2017-12-19T16:41:04.185Z",
      "ended": null
    }
  ]
  ...
}
```

Each scanning task has the following properties:

* `_id`

  The unique ID of that task instance.

* `name`

  The name of the scanning task, determined by the name of the schedule configuration file or over REST when the task is executed.

* `started`

  The time at which the scanning task started.

* `ended`

  The time at which the scanning task ended.

* `progress`

  The progress of the scanning task, summarized in the following fields:

  |             |                                                                                               |
  | ----------- | --------------------------------------------------------------------------------------------- |
  | `failures`  | The number of records not able to be processed.                                               |
  | `successes` | The number of records processed successfully.                                                 |
  | `total`     | The total number of records.                                                                  |
  | `processed` | The number of processed records.                                                              |
  | `state`     | The current state of the task, `INITIALIZED`, `ACTIVE`, `COMPLETED`, `CANCELLED`, or `ERROR`. |

The number of processed tasks whose details are retained is governed by the `openidm.taskscanner.maxcompletedruns` property in the `conf/system.properties` file. By default, the last 100 completed tasks are retained.

---

---
title: Manage scanning tasks using the admin UI
description: Use the PingIDM admin UI to configure and run scanning tasks that query managed objects and execute scripts on matching results
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:task-scanner-ui
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/task-scanner-ui.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "User Interface"]
---

# Manage scanning tasks using the admin UI

The task scanner queries a set of managed objects, then executes a script on the objects returned in the query result. The scanner then sets a field on a specific managed object property to indicate the state of the task. Before you start, you must set up this object type property on the managed user object.

In the example that follows, the task scanner queries managed user objects and returns objects whose `sunset` property holds a date that is prior to the current date. The scanner then sets the state of the task in the `task-completed` field of the user's `sunset` property.

1. Click Configure > Schedules, and click Add Schedule.

2. Enable the schedule, and set the times that the task should run.

3. Under Perform Action, select Execute a script on objects returned by a query (Task Scanner).

4. Select the managed object on which the query should be run; in this case, `user`.

5. Build the query that will be run against the managed user objects.

   The following query returns all managed users whose `sunset` date is prior to the current date (`${Time.now}`) and for whom the `sunset` task has not already completed (`/sunset/task-completed pr`):

   ```javascript
   ((/sunset/date lt \"${Time.now}\") AND !(/sunset/task-completed pr))
   ```

   |   |                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `${Time.now}` macro object fetches the current time and is available only when you configure a scanning task query filter. You can't use the macro outside of this context. |

6. In the Object Property Field, enter the property whose values will determine the state of the task; in this case, `sunset`.

7. In the Script field, enter an inline script, or a path to the file containing the script that should be launched on the results of the query.

   The sample task scanner runs the following script on the managed users returned by the previous query:

   ```javascript
   var patch = [{ "operation" : "replace", "field" : "/active", "value" : false },{ "operation" : "replace", "field" : "/accountStatus", "value" : "inactive" }];
   openidm.patch(objectID, null, patch);
   ```

   This script essentially deactivates the accounts of users returned by the query by setting the value of their `active` property to `false`.

8. Configure the advanced properties of the schedule described in [Configure Schedules](configure-schedules.html).

---

---
title: Persistent schedules
description: Configure PingIDM persistent schedules to survive restarts and launch on only one node in the cluster, with misfire policy options
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:persistent-schedules
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/persistent-schedules.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "Configuration"]
---

# Persistent schedules

By default, scheduling information is persistent. The schedule state is stored in the repository rather than in memory. This ensures that schedules survive server restarts and effectively manages execution across a cluster. In a persistent model, a scheduled task launches on only one node in the cluster.

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Non-persisted (in memory) schedules are [deprecated](../release-notes/deprecated-functionality.html#deprecation-non-persisted-schedules) and will be removed in a future release of IDM. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Persistent schedules rely on timestamps. In a deployment where IDM instances run on separate machines, you *must* synchronize the system clocks of these machines using a time synchronization service that runs regularly. The clocks of all machines involved in persistent scheduling must be within one second of each other. For information on how you can achieve this using the Network Time Protocol (NTP) daemon, refer to the [NTP RFC](https://www.rfc-editor.org/rfc/rfc7822.html). |

To configure persistent schedules, set `persisted` to `true` in the schedule configuration *(tooltip: You can create and change schedule configurations over REST at the openidm/scheduler/job endpoint, or directly in conf/schedule-schedule-name.json files.)*.

If the server is down when a scheduled task was set to occur, one or more runs of that schedule might be missed. To specify what action should be taken if schedules are missed, set the [`misfirePolicy`](configure-schedules.html#misfire-policy) in the schedule configuration file. The [`misfirePolicy`](configure-schedules.html#misfire-policy) determines what IDM should do if scheduled tasks are missed. Possible values are as follows:

* `fireAndProceed`

  The first run of a missed schedule is immediately implemented when the server is back online. Subsequent runs are discarded. After this, the normal schedule is resumed.

* `doNothing`

  All missed schedules are discarded and the normal schedule is resumed when the server is back online.

---

---
title: Scan data to trigger tasks
description: Overview of the PingIDM task scanner, which queries managed objects on a schedule and runs scripts when conditions are met
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:task-scanner
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/task-scanner.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "Triggers"]
---

# Scan data to trigger tasks

In addition to the fine-grained scheduling facility, IDM provides a task scanning mechanism. The task scanner lets you scan a set of properties with a complex query filter, at a scheduled interval, and then launches a script on the objects returned by the query.

For example, the task scanner can scan all `managed/user` objects for a specific date, and invoke a script that launches a task on the user object when that date is reached.

The task scanner runs a scheduled task that queries a managed object, then launches a script based on the query results. Scanning tasks are configured in the same way as standard scheduled tasks, as part of the schedule configuration *(tooltip: You can create and change schedule configurations over REST at the openidm/scheduler/job endpoint, or directly in conf/schedule-schedule-name.json files.)*, with the `invokeService` parameter set to `taskscanner`. The `invokeContext` parameter defines the scan details, and the task that should be launched when the specified condition is triggered.

---

---
title: Schedule examples
description: Example PingIDM schedule configurations for reconciliation and liveSync, using simple triggers with repeat intervals
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:scheduler-examples
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/scheduler-examples.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "JSON"]
---

# Schedule examples

The following example shows a schedule for reconciliation that is not enabled. When the schedule is enabled (`"enabled" : true,`), reconciliation runs every 30 minutes (1800000 milliseconds), and repeats indefinitely:

```json
{
    "enabled": false,
    "persisted": true,
    "type": "simple",
    "repeatInterval": 1800000,
    "invokeService": "sync",
    "invokeContext": {
        "action": "reconcile",
        "mapping": "systemLdapAccounts_managedUser"
    }
}
```

The following example shows a schedule for liveSync enabled to run every 15 seconds, repeating indefinitely. Note that the schedule is persisted; that is, stored in the repository rather than in memory. If one or more liveSync runs are missed, as a result of the server being unavailable, the first run of the liveSync operation is implemented when the server is back online. Subsequent runs are discarded. After this, the normal schedule is resumed:

```json
{
    "enabled": true,
    "persisted": true,
    "misfirePolicy" : "fireAndProceed",
    "type": "simple",
    "repeatInterval": 15000,
    "invokeService": "provisioner",
    "invokeContext": {
        "action": "liveSync",
        "source": "system/ldap/account"
    }
}
```

---

---
title: Schedule tasks and events
description: Overview of the PingIDM scheduler service for scheduling reconciliation, sync, scripts, workflows, and task scanner operations
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:schedules
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/schedules.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "Configuration", "Triggers"]
---

# Schedule tasks and events

The scheduler service lets you schedule reconciliation and synchronization tasks, trigger scripts, collect and run reports, trigger workflows, and perform custom logging.

The service depends on the Quartz Scheduler (bundled with IDM), and supports Quartz simple triggers and cron triggers. Use the trigger type that suits your scheduling requirements. For more information, refer to the Quartz documentation on [SimpleTriggers](https://www.quartz-scheduler.org/documentation/quartz-2.5.x/tutorials/tutorial-lesson-05.html) and [CronTriggers](https://www.quartz-scheduler.org/documentation/quartz-2.5.x/tutorials/crontrigger.html).

By default, IDM picks up changes to scheduled tasks and events dynamically, during initialization and also at runtime. For more information, refer to [Configuration changes](../setup-guide/changing-configuration.html).

In addition to the fine-grained scheduling facility, you can perform a scheduled batch scan for a specified date in IDM data, and then automatically run a task when this date is reached. For more information, refer to [Scan data to trigger tasks](task-scanner.html).

---

---
title: Scheduler metrics
description: View and query PingIDM scheduler metrics including trigger acquisition, fired events, and per-job execution statistics
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:schedule-metrics
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/schedule-metrics.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "JSON", "metrics"]
section_ids:
  example_scheduler_metrics: Example scheduler metrics
  scheduler_trigger_acquired_success: scheduler.trigger.acquired.success
  scheduler_trigger_fired: scheduler.trigger.fired
  scheduler_job_job_group_job_name_executed: scheduler.job.job-group.job-name.executed
  scheduler_job_job_group_job_name_completed: scheduler.job.job-group.job-name.completed
---

# Scheduler metrics

Before you can use scheduler metrics, you must [enable metrics](../monitoring-guide/monitoring.html). For the complete list of scheduler metrics, refer to [API scheduler metrics available in IDM](../monitoring-guide/api-metrics.html#api-scheduler-metric-names).

## Example scheduler metrics

### `scheduler.trigger.acquired.success`

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/metrics/api?_queryFilter=/_id+eq+"scheduler.trigger.acquired.success"'
```

Response

```json
{
  "result": [
    {
      "_id": "scheduler.trigger.acquired.success",
      "m15_rate": 1.3331465689081097,
      "m1_rate": 1.0309301543856877,
      "m5_rate": 1.2318064768948462,
      "mean_rate": 1.0258321337261471,
      "units": "events/second",
      "total": 183,
      "count": 183,
      "_type": "summary"
    }
  ],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "EXACT",
  "totalPagedResults": 1,
  "remainingPagedResults": -1
}
```

### `scheduler.trigger.fired`

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/metrics/api?_queryFilter=/_id+eq+"scheduler.trigger.fired"'
```

Response

```json
{
  "result": [
    {
      "_id": "scheduler.trigger.fired",
      "m15_rate": 1.1575004755551879,
      "m1_rate": 1.0055565867908252,
      "m5_rate": 1.0976754941332376,
      "mean_rate": 1.0083534436743353,
      "units": "events/second",
      "total": 224,
      "count": 224,
      "_type": "summary"
    }
  ],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "EXACT",
  "totalPagedResults": 1,
  "remainingPagedResults": -1
}
```

### `scheduler.job.job-group.job-name.executed`

The following example retrieves the metric for an executed schedule with the following details:

* job-group = `scheduler-service-group`

* job-name = `script`

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/metrics/api?_queryFilter=/_id+eq+"scheduler.job.scheduler-service-group.script.executed"'
```

Response

```json
{
  "result": [
    {
      "_id": "scheduler.job.scheduler-service-group.script.executed",
      "count": 391,
      "max": 17.04553,
      "mean": 1.3264534620189976,
      "min": 0.524604,
      "p50": 1.3127419999999999,
      "p75": 1.555721,
      "p95": 1.7416239999999998,
      "p98": 1.898285,
      "p99": 2.075185,
      "p999": 2.4402909999999998,
      "stddev": 0.39220923689155185,
      "m15_rate": 1.1311176673815566,
      "m1_rate": 1.000355220709147,
      "m5_rate": 1.056353857818992,
      "mean_rate": 1.0048492196855094,
      "duration_units": "milliseconds",
      "rate_units": "calls/second",
      "total": 580.803062,
      "_type": "timer"
    }
  ],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "EXACT",
  "totalPagedResults": 1,
  "remainingPagedResults": -1
}
```

### `scheduler.job.job-group.job-name.completed`

The following example retrieves the metric for a completed schedule with the following details:

* job-group = `scheduler-service-group`

* job-name = `script`

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/metrics/api?_queryFilter=/_id+eq+"scheduler.job.scheduler-service-group.script.completed"'
```

Response

```json
{
  "result": [
    {
      "_id": "scheduler.job.scheduler-service-group.script.completed",
      "m15_rate": 1.2596544396953329,
      "m1_rate": 1.0147166389216893,
      "m5_rate": 1.1109942946670412,
      "mean_rate": 1.0036465219104702,
      "units": "events/second",
      "total": 398,
      "count": 398,
      "_type": "summary"
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
title: Schedules
description: Guide to configuring schedules and scanning tasks
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "REST API"]
page_aliases: ["index.adoc"]
---

# Schedules

> Guide to configuring schedules and scanning tasks.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

This guide covers schedules and scanning tasks.

[icon: calendar-days, set=fad, size=3x]

#### [Scheduling](schedules.html)

Schedule tasks and events.

[icon: tasks, set=fad, size=3x]

#### [Task Scanner](task-scanner.html)

Scan data to trigger tasks.

---

---
title: Schedules and daylight savings time
description: Understand how daylight savings time affects PingIDM cron and simple triggers, and how to prevent scheduling interruptions
component: pingidm
version: 8.1
page_id: pingidm:schedules-guide:schedules-dst
canonical_url: https://docs.pingidentity.com/pingidm/8.1/schedules-guide/schedules-dst.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scheduled Tasks", "Triggers"]
---

# Schedules and daylight savings time

The scheduler service supports Quartz cron triggers and simple triggers. Cron triggers schedule jobs to fire at specific times with respect to a calendar (rather than every N milliseconds). This scheduling can cause issues when clocks change for daylight savings time (DST) if the trigger time falls around the clock change time in your specific time zone.

Depending on the trigger schedule, and on the daylight event, the trigger might be skipped or might appear not to fire for a short period. This interruption can be particularly problematic for liveSync where schedules execute continuously. In this case, the time change (for example, from 02:00 back to 01:00) causes an hour break between each liveSync execution.

To prevent DST from having an impact on your schedules, use simple triggers instead of cron triggers.
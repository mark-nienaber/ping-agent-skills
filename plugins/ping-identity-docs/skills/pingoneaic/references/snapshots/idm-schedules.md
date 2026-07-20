---
title: Configure schedules
description: Configure static and dynamic schedules with environment secrets and variables support
component: pingoneaic
page_id: pingoneaic:idm-schedules:configure-schedules
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/configure-schedules.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  config-static-schedules: Configure static schedule configuration
  config-dynamic-schedules: Configure dynamic schedule configuration
  static-dynamic-config: Use static or dynamic schedule configuration in development
  sched-config-properties: Schedule configuration format and properties
---

# Configure schedules

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

You can configure schedules in two ways:

* [Configure static schedule configuration](#config-static-schedules)

* [Configure dynamic schedule configuration](#config-dynamic-schedules)

## Configure static schedule configuration

When you configure schedules in a static configuration, you can use environment secrets and variables ([ESVs](../tenants/esvs.html)) in schedules to allow different settings between environments. For example, you can use ESVs to control whether a schedule is enabled and when it should run.

To use ESVs in your schedules, create or update your schedule definition by using a `PUT` request against the `/openidm/config/schedule/` endpoint. This endpoint creates the schedule as a *static configuration* and includes it in promotions.

Learn more in [Configure schedules in static configuration](configure-static-schedules.html).

## Configure dynamic schedule configuration

Creating a schedule directly in your staging or production environment allows you to have greater control over your schedules on a per-environment basis. For example, you can control the intervals and enable or disable different schedules as required. Creating schedules directly in an environment sets them as a *dynamic configuration* that won't be included in any subsequent promotions.

Learn more in [Configure schedules in dynamic configuration](configure-dynamic-schedules.html).

|   |                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use the [PingIDM REST API](configure-dynamic-schedules.html#schedules-over-rest) to create dynamic schedules. However, you cannot create dynamic schedules through the UI in staging and production environments. |

## Use static or dynamic schedule configuration in development

When you create schedules in your development environment, consider the following:

* If you create a schedule through the Advanced Identity Cloud user interface (UI) in your development environment, the schedule will have a static configuration and be promoted.

* If you use PingIDM REST to create a schedule in your development environment or you include ESVs in the schedule definition, you must use a `PUT` request against the `/openidm/config/schedule/` endpoint. This endpoint ensures you create the schedule as a static configuration that is included in promotions.

* If you use the `/openidm/scheduler/job/` endpoint to create a schedule, it will bypass the configuration service and send the request directly to the scheduler. The schedule won't be promoted because it will have a dynamic configuration. Learn more in [Manage schedules using REST](configure-dynamic-schedules.html#schedules-over-rest).

## Schedule configuration format and properties

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

The schedule configuration properties are defined as follows:

* `enabled`

  Set to `true` to enable the schedule. When this property is `false`, PingIDM considers the schedule configuration inactive and does not allow it to be triggered or launched.

  If you want to retain a schedule configuration, but do not want it used, set `enabled` to `false` for task and event schedulers, instead of changing the configuration or `cron` expressions.

* `persisted` (optional)

  Specifies whether the schedule state should be persisted or stored only in memory. Boolean (`true` or `false`), `true` by default.

  |   |                                                                                                    |
  | - | -------------------------------------------------------------------------------------------------- |
  |   | If the schedule is stored only in memory, the schedule is lost on Advanced Identity Cloud restart. |

  |   |                                                                                                                                                                                    |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Non-persisted (in memory) schedules are [deprecated](../product-information/deprecation-notices.html#deprecation-non-persisted-schedules) and will be removed in a future release. |

* `recoverable` (optional)

  Specifies whether jobs that have failed mid-execution (as a result of a JVM crash or otherwise unexpected termination) should be recovered. Boolean (`true` or `false`), `false` by default.

* `concurrentExecution`

  Specifies whether multiple instances of the same schedule can run concurrently. Boolean (`true` or `false`), `false` by default. Multiple instances of the same schedule cannot run concurrently by default. This setting prevents a new scheduled task from being launched before the same previously launched task has completed. For example, under normal circumstances you would want a liveSync operation to complete before the same operation was launched again. To enable multiple schedules to run concurrently, set this parameter to `true`. The behavior of missed scheduled tasks is governed by the [misfire policy](#misfire-policy).

* `type`

  The trigger type, either `simple` or `cron`.

  Learn more about these trigger types in the Quartz documentation on [SimpleTriggers](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-05.html) and [CronTriggers](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-06.html).

* `repeatCount`

  Used only for simple triggers (`"type" : "simple"`).

  The number of times the schedule must be repeated. The repeat count can be `0`, a *positive integer*, or `-1`. A value of `-1` indicates that the schedule should repeat indefinitely.

  If you do not specify a repeat count, the value defaults to `-1`.

* `repeatInterval`

  Used only for simple triggers (`"type" : "simple"`).

  Specifies the interval, in milliseconds, between trigger firings. The repeat interval must be zero or a positive long value. If you set the repeat interval to zero, the scheduler will trigger `repeatCount` firings concurrently (or as close to concurrently as possible).

  If you do not specify a repeat interval, the value defaults to 0.

* `startTime` (optional)

  This parameter starts the schedule at some time in the future. If the parameter is omitted, empty, or set to a time in the past, the task or event is scheduled to start immediately.

  Use ISO 8601 format to specify times and dates (`yyyy-MM-dd'T'HH:mm:ss`).

  To specify a time zone, include the time zone at the end of the `startTime`, in the format `+|-hh:mm`; for example `2017-10-31T15:53:00+05:00`. If you specify both a `startTime` and an `endTime`, they must have the same time zone.

* `endTime` (optional)

  Specifies when the schedule must end, in ISO 8601 format (`yyyy-MM-dd'T'HH:mm:ss+|-hh:mm`.

* `schedule`

  Used only for cron triggers (`"type" : "cron"`).

  Takes `cron` expression syntax. Learn more in the [CronTrigger Tutorial](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) and in [Lesson 6: CronTrigger](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-06.html).

- `misfirePolicy`

  This optional parameter specifies the system behavior if the scheduled task is missed. Possible values are:

  * `fireAndProceed`: The first run of a missed schedule is immediately launched when the server is back online. Subsequent runs are discarded. After this, the normal schedule is resumed.

  * `doNothing`: All missed schedules are discarded and the normal schedule is resumed when the server is back online.

- `invokeService`

  Defines the type of scheduled event or action. The value of this parameter can be one of the following:

  * `sync` for reconciliation.

  * `provisioner` for liveSync.

  * `script` to call some other scheduled operation defined in a script.

  * `taskScanner` to define a scheduled task that queries a set of objects. Learn more in [Scan data to trigger tasks](task-scanner.html).

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

  For scheduled liveSync tasks, the `source` property follows PingIDM's convention for a pointer to an external resource object and takes the form `system/resource-name/object-type`.

  The following example invokes a script, which prints the node ID performing the scheduled job and the time to the console.

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

  Specifies the level at which the invocation will be logged. For schedules that run very frequently, such as liveSync, the scheduled task can generate significant output to the log file. You should adjust this parameter accordingly. The default schedule log level is `info`. The value can be set to any one of the [SLF4J](http://www.slf4j.org/apidocs/org/apache/commons/logging/Log.html) log levels:

  * `trace`

  * `debug`

  * `info`

  * `warn`

  * `error`

  * `fatal`

---

---
title: Configure schedules in dynamic configuration
description: Create and manage schedules in dynamic configuration using REST API and identity management scheduler service
component: pingoneaic
page_id: pingoneaic:idm-schedules:configure-dynamic-schedules
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/configure-dynamic-schedules.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  create-dynamic-schedules: Create a dynamic schedule using REST
  schedules-over-rest: Manage schedules using REST
  validating-schedule-syntax: Validate cron trigger expressions
  define-schedules: Define a schedule
  schedule-details: View scheduled job details
  querying-schedules: Query scheduled jobs
  updating-schedules: Update a schedule
  schedules-listing-current-tasks: List running scheduled jobs
  trigger-scheduled-task: Trigger a schedule manually
  pause-scheduled-job: Pause and resume a scheduled job
  query-schedule-triggers: Query schedule triggers
  delete-schedules: Delete a schedule
  schedules-admin-ui: Manage schedules using the IDM admin console
---

# Configure schedules in dynamic configuration

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

Creating a schedule directly in your staging or production environment allows you to have greater control over your schedules on a per-environment basis. For example, you can control the intervals and enable or disable different schedules as required. Creating schedules directly in an environment sets them as a *dynamic configuration* that won't be included in any subsequent promotions.

|   |                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use the [PingIDM REST API](#schedules-over-rest) to create dynamic schedules. However, you cannot create dynamic schedules through the Advanced Identity Cloud user interface (UI) in staging and production environments. |

## Create a dynamic schedule using REST

To create a dynamic schedule in your environments using PingIDM REST, replace `<tenant-env-fqdn>` with your Advanced Identity Cloud tenant name and `<token>`.

|   |                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The access token is the token you obtained when you authenticated to the Advanced Identity Cloud REST API. The access token is set as a bearer token in the `Authorization` HTTP header for each API request. Learn more in [Authenticate to Advanced Identity Cloud with access token](../developer-docs/authenticate-to-rest-api-with-access-token.html). |

For example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "content-type: application/json" \
--header "Accept-API-Version: resource=2.0" \
--request PUT "https://<tenant-env-fqdn>/openidm/scheduler/job/reconciliation-schedule" \
--data '{
    "enabled": true,
    "persisted": true,
    "type": "simple",
    "repeatInterval": 1800000,
    "invokeService": "sync",
    "invokeContext": {
        "action": "reconcile",
        "mapping": "systemLdapAccounts_managedAlpha_user"
    }
}'
```

This example creates a *reconciliation schedule* that runs a reconciliation for the systemLdapAccounts\_managedAlpha\_user mapping every 30 minutes (`1800000 milliseconds`) and repeats indefinitely. Learn more about reconciliation in [Synchronization operations](../idm-synchronization/chap-sync-operations.html).

## Manage schedules using REST

The scheduler service is exposed under the `/openidm/scheduler` context path. Within this context path, the defined scheduled jobs are accessible at `/openidm/scheduler/job`. A job is the actual task that is run. Each job contains a *trigger* that starts the job. The trigger defines the schedule according to which the job is executed. You can read and query the existing triggers on the `/openidm/scheduler/trigger` context path.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For dynamic schedule configuration, use the `openidm/scheduler/job` endpoint. Learn more in [Configure schedules in dynamic configuration](configure-dynamic-schedules.html).To use environment secrets and variables ([ESVs](../tenants/esvs.html)) in your schedules, use the `openidm/config/schedule` endpoint. This endpoint creates the schedule as static configuration and is included in promotions. Learn more in [Configure schedules in static configuration](configure-static-schedules.html). |

The following examples show how schedules are validated, created, read, queried, updated, and deleted, over REST by using the scheduler service.

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you configure schedules over REST, changes made to the schedules are not pushed back into the configuration service. Managing schedules by using the `/openidm/scheduler/job` context path essentially bypasses the configuration service and sends the request directly to the scheduler. |

### Validate cron trigger expressions

Schedules are defined using Quartz cron or simple triggers. If you use a cron trigger, you can validate your cron expression by sending the expression as a JSON object to the `scheduler` context path:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
--data '{
    "cronExpression": "0 0/1 * * * ?"
}' \
"https://<tenant-env-fqdn>/openidm/scheduler/job?_action=validateQuartzCronExpression"
{
  "valid": true
}
```

### Define a schedule

To define a new schedule, send a PUT or POST request to the `scheduler/job` context path with the details of the schedule in the JSON payload. A PUT request lets you specify the ID of the schedule. A POST request assigns an ID automatically.

The following example uses a PUT request to create a schedule that fires a script every second. The example assumes the script exists in the specified location. The schedule configuration is as described in [Configure Schedules](configure-schedules.html):

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0" \
--request PUT \
--data \
'{
  "enabled": true,
  "type": "cron",
  "schedule": "0/1 * * * * ?",
  "persisted": true,
  "misfirePolicy": "fireAndProceed",
  "invokeService": "script",
  "invokeContext": {
    "script": {
      "type": "text/javascript",
      "source": "logger.info('Testing schedules!');"
    }
  }
}' \
"https://<tenant-env-fqdn>/openidm/scheduler/job/testlog-schedule"
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
      "source": "logger.info('Testing schedules!');"
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
          "timeZone": "Etc/UTC"
        },
        "description": null,
        "endTime": null,
        "fireInstanceId": null,
        "group": "scheduler-service-group",
        "jobDataMap": {
          "scheduler.invokeService": "org.forgerock.openidm.script",
          "scheduler.config-name": "scheduler-testlog-schedule",
          "scheduler.invokeContext": {
            "script": {
              "type": "text/javascript",
              "source": "logger.info('Testing schedules!');"
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
                "source": "logger.info('Testing schedules!');"
              }
            },
            "invokeLogLevel": "info",
            "startTime": null,
            "endTime": null,
            "concurrentExecution": false,
            "configAlias": null
          },
          "scheduler.invokeLogLevel": "info"
        },
        "jobGroup": "scheduler-service-group",
        "jobName": "testlog-schedule",
        "misfireInstruction": 1,
        "name": "trigger-testlog-schedule",
        "nextFireTime": 1680204234000,
        "previousFireTime": null,
        "priority": 5,
        "startTime": 1680204234000,
        "volatility": false
      },
      "state": "NORMAL",
      "_rev": "2cf55cac-ce2b-4ef8-a4a2-6f98a803bc07-4600",
      "_id": "scheduler-service-group.trigger-testlog-schedule"
    }
  ],
  "previousRunDate": "2023-03-30T19:22:54.000Z",
  "nextRunDate": "2023-03-30T19:23:54.000Z"
}
```

|   |                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The previous output includes the `trigger` that was created as part of the scheduled job, as well as the `nextRunDate` for the job. Learn more about `trigger` properties in [Query Schedule Triggers](#query-schedule-triggers). |

The following example uses a POST request to create an identical schedule to the one created in the previous example, but with a *server-assigned ID*:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
--data \
'{
  "enabled": true,
  "type": "cron",
  "schedule": "0/1 * * * * ?",
  "persisted": true,
  "misfirePolicy": "fireAndProceed",
  "invokeService": "script",
  "invokeContext": {
    "script": {
      "type": "text/javascript",
      "source": "logger.info('Testing schedules!');"
    }
  }
}' \
"https://<tenant-env-fqdn>/openidm/scheduler/job?_action=create"
{
  "_id": "71fd1b5f-5ebc-4c94-89ac-dbc8e05138d3",
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
      "source": "logger.info('Testing schedules!');"
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
      "jobKey": "scheduler-service-group.71fd1b5f-5ebc-4c94-89ac-dbc8e05138d3",
      "name": "trigger-71fd1b5f-5ebc-4c94-89ac-dbc8e05138d3",
      "nodeId": "idm-57855cff6c-l8jrb",
      "previousState": null,
      "serialized": {
        "type": "CronTriggerImpl",
        "calendarName": null,
        "cronEx": {
          "cronExpression": "0/1 * * * * ?",
          "timeZone": "Etc/UTC"
        },
        "description": null,
        "endTime": null,
        "fireInstanceId": "idm-57855cff6c-l8jrb_1680180846805",
        "group": "scheduler-service-group",
        "jobDataMap": {
          "scheduler.invokeService": "org.forgerock.openidm.script",
          "scheduler.config-name": "scheduler-71fd1b5f-5ebc-4c94-89ac-dbc8e05138d3",
          "scheduler.invokeContext": {
            "script": {
              "type": "text/javascript",
              "source": "logger.info('Testing schedules!');"
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
                "source": "logger.info('Testing schedules!');"
              }
            },
            "invokeLogLevel": "info",
            "startTime": null,
            "endTime": null,
            "concurrentExecution": false,
            "configAlias": null
          },
          "scheduler.invokeLogLevel": "info"
        },
        "jobGroup": "scheduler-service-group",
        "jobName": "71fd1b5f-5ebc-4c94-89ac-dbc8e05138d3",
        "misfireInstruction": 1,
        "name": "trigger-71fd1b5f-5ebc-4c94-89ac-dbc8e05138d3",
        "nextFireTime": 1680204679000,
        "previousFireTime": null,
        "priority": 5,
        "startTime": 1680204679000,
        "volatility": false
      },
      "state": "NORMAL",
      "_rev": "2cf55cac-ce2b-4ef8-a4a2-6f98a803bc07-5927",
      "_id": "scheduler-service-group.trigger-71fd1b5f-5ebc-4c94-89ac-dbc8e05138d3"
    }
  ],
  "previousRunDate": "2023-03-30T19:30:19.000Z",
  "nextRunDate": "2023-03-30T19:31:19.000Z"
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
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/scheduler/job/testlog-schedule"
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
      "source": "logger.info('Testing schedules!');"
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
      "nodeId": "idm-57855cff6c-l8jrb",
      "previousState": null,
      "serialized": {
        "type": "CronTriggerImpl",
        "calendarName": null,
        "cronEx": {
          "cronExpression": "0/1 * * * * ?",
          "timeZone": "Etc/UTC"
        },
        "description": null,
        "endTime": null,
        "fireInstanceId": "idm-57855cff6c-l8jrb_1680180847170",
        "group": "scheduler-service-group",
        "jobDataMap": {
          "scheduler.invokeService": "org.forgerock.openidm.script",
          "scheduler.config-name": "scheduler-testlog-schedule",
          "scheduler.invokeContext": {
            "script": {
              "type": "text/javascript",
              "source": "logger.info('Testing schedules!');"
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
                "source": "logger.info('Testing schedules!');"
              }
            },
            "invokeLogLevel": "info",
            "startTime": null,
            "endTime": null,
            "concurrentExecution": false,
            "configAlias": null
          },
          "scheduler.invokeLogLevel": "info"
        },
        "jobGroup": "scheduler-service-group",
        "jobName": "testlog-schedule",
        "misfireInstruction": 1,
        "name": "trigger-testlog-schedule",
        "nextFireTime": 1680205063000,
        "previousFireTime": 1680205062000,
        "priority": 5,
        "startTime": 1680205024000,
        "volatility": false
      },
      "state": "NORMAL",
      "_rev": "2cf55cac-ce2b-4ef8-a4a2-6f98a803bc07-7099",
      "_id": "scheduler-service-group.trigger-testlog-schedule"
    }
  ],
  "previousRunDate": "2023-03-30T19:37:42.000Z",
  "nextRunDate": "2023-03-30T19:37:43.000Z"
}
```

### Query scheduled jobs

You can query defined and running scheduled jobs using a regular [query filter](../idm-objects/queries.html#constructing-queries).

The following query returns the IDs of all defined schedules:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/scheduler/job?_queryFilter=true&_fields=_id"
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
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/scheduler/job?_queryFilter=true&_fields=_id,enabled,nextRunDate"
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
--header "Authorization: Bearer <access-token>" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.0" \
--request PUT \
--data \
'{
  "enabled": false,
  "type": "cron",
  "schedule": "0/1 * * * * ?",
  "persisted": true,
  "misfirePolicy": "fireAndProceed",
  "invokeService": "script",
  "invokeContext": {
    "script": {
      "type": "text/javascript",
      "source": "logger.info('Testing schedules!');"
    }
  }
}' \
"https://<tenant-env-fqdn>/openidm/scheduler/job/testlog-schedule"
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
      "source": "logger.info('Testing schedules!');"
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

This example returns a list of the jobs that are currently running. The list lets you decide whether to wait for a specific job to complete before shutting down a server.

|   |                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The request only returns jobs currently running on the node that processes the request.

* The list is accurate only at the moment the request was issued and can change at any time after the response is received. |

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/scheduler/job?_action=listCurrentlyExecutingJobs"
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

For testing purposes and for certain administrative tasks, you can trigger a scheduled task manually, outside of its specified schedule. A scheduled task must be `enabled` before it can be triggered.

This command triggers the `testlog-schedule` job created previously:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/scheduler/job/testlog-schedule?_action=trigger"
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
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/scheduler/job/testlog-schedule?_action=pause"
{
  "success": true
}
```

This command resumes the `testlog-schedule` job:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/scheduler/job/testlog-schedule?_action=resume"
{
  "success": true
}
```

|   |                                                                                 |
| - | ------------------------------------------------------------------------------- |
|   | These actions are available only from version 2.0 of the scheduler API onwards. |

### Query schedule triggers

When a scheduled job is created, a trigger for that job is created automatically and is included in the schedule definition. The trigger is essentially what causes the job to be started. You can read all the triggers that have been generated on a system with the following query on the `openidm/scheduler/trigger` context path:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/scheduler/trigger?_queryFilter=true"
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

  The previous state of the trigger, before its current state. Learn more about Quartz trigger states in the [Quartz API documentation](https://www.quartz-scheduler.org/api/2.3.0/org/quartz/Trigger.TriggerState.html).

* `name`

  The trigger name, which matches the ID of the schedule that created the trigger, with `trigger-` added: `trigger-schedule-id`.

* `state`

  The current state of the trigger. Learn more about descriptions of Quartz trigger states in the [Quartz API documentation](https://www.quartz-scheduler.org/api/2.3.0/org/quartz/Trigger.TriggerState.html).

* `nodeId`

  The ID of the node that has acquired the trigger, useful in a clustered deployment. If the trigger has not been acquired by a node yet, this will return `null`.

* `calendar`

  This is a part of the Quartz implementation, but is not currently supported by PingIDM. This will always return `null`.

* `serialized`

  The JSON serialization of the trigger class.

* `group`

  The name of the group that the trigger is in, always `scheduler-service-group`.

* `jobKey`

  The name of the job associated with the trigger: `group.schedule-id`.

To read the contents of a specific trigger, send a GET request to the trigger ID. For example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/scheduler/trigger/scheduler-service-group.trigger-testlog-schedule"
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
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/scheduler/trigger?_queryFilter=(nodeId+pr)"
```

To view the triggers that have not yet been acquired by any node, send a GET request to the scheduler, with a `_queryFilter` to list the triggers with a null `nodeId`. For example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/scheduler/trigger?_queryFilter=%21(nodeId+pr)"
```

### Delete a schedule

To delete a schedule, send a DELETE request to the schedule ID. For example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request DELETE \
"https://<tenant-env-fqdn>/openidm/scheduler/job/testlog-schedule"
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
      "source": "logger.info('Testing schedules!');"
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
      "nodeId": "idm-57855cff6c-l8jrb",
      "previousState": null,
      "serialized": {
        "type": "CronTriggerImpl",
        "calendarName": null,
        "cronEx": {
          "cronExpression": "0/1 * * * * ?",
          "timeZone": "Etc/UTC"
        },
        "description": null,
        "endTime": null,
        "fireInstanceId": "idm-57855cff6c-l8jrb_1680180847387",
        "group": "scheduler-service-group",
        "jobDataMap": {},
        "jobGroup": "scheduler-service-group",
        "jobName": "testlog-schedule",
        "misfireInstruction": 1,
        "name": "trigger-testlog-schedule",
        "nextFireTime": 1680205354000,
        "previousFireTime": 1680205353000,
        "priority": 5,
        "startTime": 1680205240000,
        "volatility": false
      },
      "state": "NORMAL",
      "_rev": "2cf55cac-ce2b-4ef8-a4a2-6f98a803bc07-7809",
      "_id": "scheduler-service-group.trigger-testlog-schedule"
    }
  ],
  "previousRunDate": "2023-03-30T19:42:33.000Z",
  "nextRunDate": "2023-03-30T19:42:34.000Z"
}
```

The DELETE request returns the entire JSON object.

## Manage schedules using the IDM admin console

Manage schedules using the IDM admin console at `https://<tenant-env-fqdn>/admin/#scheduler/`.

Add, remove, and change schedules here. By default, only persisted schedules are shown in the Schedules list. To show non-persisted (in memory) schedules, select Filter by Type > In Memory.

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Non-persisted (in memory) schedules are [deprecated](../product-information/deprecation-notices.html#deprecation-non-persisted-schedules) and will be removed in a future release. |

![ui-schedules](_images/ui-schedules.png)

---

---
title: Configure schedules in static configuration
description: Configure schedules in static configuration with environment variables for multi-environment deployments
component: pingoneaic
page_id: pingoneaic:idm-schedules:configure-static-schedules
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/configure-static-schedules.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  create-esv-variables: Create ESV variables
  create-schedules-esvs: Create schedules using ESV variables
---

# Configure schedules in static configuration

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

When you create or update your schedule definition by using a `PUT` request against the `/openidm/config/schedule/` endpoint, this endpoint creates the schedule as a *static configuration* and includes it in promotions.

## Create ESV variables

When you configure schedules in a static configuration, you can use environment secrets and variables ([ESVs](../tenants/esvs.html)) in schedules to allow different settings between environments.

Example ESVs include:

* `esv-schedule-enabled`

  This ESV controls whether the schedule is enabled and should be set to `true` or `false` in each environment as needed.

* `esv-sync-schedule`

  This ESV controls when the schedule is run for cron triggers. For example, you could set the ESV to `0 0 10 ? * WED` to run the schedule every Wednesday at 10 AM in one environment and then set the ESV to `0 0 17 * * ?` to run the schedule every day at 5 PM in another environment.

  |   |                                                                                                                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To avoid a known issue where day `1` is Monday rather than Sunday, use three letters to specify the day instead. Learn more in [Schedule configuration properties](configure-schedules.html#sched-config-properties). |

Learn more about creating ESV variables and applying updates in the [Introduction to ESVs](../tenants/esvs.html) and in [Set up configuration placeholders to reference an ESV.](../tenants/configuration-placeholders.html)

## Create schedules using ESV variables

You can create the two example ESVs (&{esv.schedule.enabled} and &{esv.sync.schedule}) described in the [Create ESV variables](#create-esv-variables) section to control whether a schedule is enabled and when a schedule will run.

To create your schedule or update an existing schedule using these example variables, ensure you use a `PUT` request against the `/openidm/config/schedule/` endpoint.

For example:

```
curl \
--header "Authorization: Bearer <access-token>" \ (1)
--header "content-type: application/json" \
--header "Accept-API-Version: resource=1.0" \
--header "If-None-Match: *" \
--request PUT "https://<tenant-env-fqdn>/openidm/config/schedule/<schedule-name>" \ (2) (3)
--data '{
    "isCron": true,
    "enabled": {
      "$bool": "&{esv.schedule.enabled}" (4)
  },
    "persisted": true,
    "type": "cron",
    "misfirePolicy": "fireAndProceed",
    "invokeService": "sync",
    "invokeLogLevel": "info",
    "invokeContext": {
        "action": "reconcile",
        "mapping": "systemLdapAccounts_managedAlpha_user"
    },
    "concurrentExecution": false,
    "schedule": "&{esv.sync.schedule}" (5)
}'
```

|       |                                                                                                                                                                                                                                                                                                                                                |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | The access token you obtained when you authenticated to the Advanced Identity Cloud REST API. The access token is set as a bearer token in the `Authorization` HTTP header for each API request. Learn more in [Authenticate to Advanced Identity Cloud with access token](../developer-docs/authenticate-to-rest-api-with-access-token.html). |
| **2** | Your Advanced Identity Cloud tenant name.                                                                                                                                                                                                                                                                                                      |
| **3** | The name of your schedule.                                                                                                                                                                                                                                                                                                                     |
| **4** | Placeholder for the ESV you created.                                                                                                                                                                                                                                                                                                           |
| **5** | Placeholder for the ESV you created.                                                                                                                                                                                                                                                                                                           |

After you've created or updated your schedule through REST, you should restart Advanced Identity Cloud services to substitute the placeholders with the corresponding ESV values. Learn more about how to [Restart Advanced Identity Cloud services](../tenants/configuration-placeholders.html#restart-identity-cloud-services).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can view your schedules in the Advanced Identity Cloud user interface (UI), but you should only update them using the ESVs you created. Alternatively, [manage schedules using REST](configure-dynamic-schedules.html#schedules-over-rest) to keep your schedules using the ESV placeholders. If you make changes to the schedule in the UI, the ESV placeholders will be overwritten with the actual values. |

---

---
title: Configure the scheduler service
description: Configure the Quartz Scheduler service thread pool and persistent schedule execution settings
component: pingoneaic
page_id: pingoneaic:idm-schedules:scheduler-configuration-file
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/scheduler-configuration-file.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Configure the scheduler service

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

There is a distinction between the configuration of the scheduler service, and the configuration of individually scheduled tasks and events (which execute based off of the configurations of the scheduler service). The scheduler configuration *(tooltip: You can edit the scheduler configuration over REST at the openidm/scheduler endpoint.)* has the following format, and configures the Quartz Scheduler:

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

* `executePersistentSchedules` lets you disable persistent schedules for a specific node. If this parameter is set to `false`, the Scheduler Service will support the management of persistent schedules (CRUD operations) but it will not run any persistent schedules. The value of this property can be a string or boolean. Its default value is `true`.

* `advancedProperties` (optional) lets you configure additional properties for the Quartz Scheduler.

For details of all the configurable properties for the Quartz Scheduler, refer to the [Quartz Scheduler Configuration Reference](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/configuration/ConfigMain).

---

---
title: Manage scanning tasks
description: Trigger, cancel, and list scanning tasks using REST and admin UI
component: pingoneaic
page_id: pingoneaic:idm-schedules:manage-scanning-tasks
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/manage-scanning-tasks.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Manage scanning tasks

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

You can trigger, cancel, or list the existing scanning tasks in IDM.

You can manage scanning tasks in IDM using:

* [REST](task-scanner-rest.html)

* [IDM admin console](task-scanner-ui.html)

---

---
title: Manage scanning tasks using REST
description: Manage scanning tasks over REST including trigger, cancel, and list operations
component: pingoneaic
page_id: pingoneaic:idm-schedules:task-scanner-rest
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/task-scanner-rest.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  trigger-task-scanner: Trigger a scanning task
  cancel-task-scanner: Cancel a scanning task
  list-task-scanner: List the scanning tasks
---

# Manage scanning tasks using REST

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

You can trigger, cancel, and monitor scanning tasks over the REST interface, using the REST endpoint `openidm/taskscanner`.

## Trigger a scanning task

To trigger a scanning task over REST, use the `execute` action and specify the `name` of the task (effectively the scheduled job name). To obtain a list of task names, you can query the `/openidm/scheduler/job` endpoint. Note, however, that not all jobs are scanning tasks. Only those jobs that have the correct task scanner `invokeContext` can be triggered in this way.

The following example triggers a scanning task named `myTask`:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/taskscanner?_action=execute&name=myTask"
{
  "_id": "9f2564c8-193c-4871-8869-6080f374b1bd-2073"
}
```

By default, a scanning task ID is returned immediately when the task is initiated. Clients can make subsequent calls to the task scanner service, using this task ID to query its state and to call operations on it.

To have the scanning task complete before the ID is returned, set the `waitForCompletion` property to `true` in the `invokeContext` of the schedule configuration.

## Cancel a scanning task

To cancel a scanning task that is in progress, send a REST call with the `cancel` action, specifying the task ID. The following call cancels the scanning task initiated in the previous example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"https://<tenant-env-fqdn>/openidm/taskscanner/9f2564c8-193c-4871-8869-6080f374b1bd-2073?_action=cancel"
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
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/taskscanner?_queryFilter=true"
{
  "result": [
    {
      "_id": "9f2564c8-193c-4871-8869-6080f374b1bd-2073",
      "name": "schedule/myTask",
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
      "name": "schedule/myTask",
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

The number of processed tasks whose details are retained is governed by the `openidm.taskscanner.maxcompletedruns` property. By default, the last 100 completed tasks are retained.

---

---
title: Manage scanning tasks using the IDM admin console
description: Create and configure task scanner schedules to execute scripts on queried managed objects
component: pingoneaic
page_id: pingoneaic:idm-schedules:task-scanner-ui
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/task-scanner-ui.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Manage scanning tasks using the IDM admin console

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

The task scanner queries a set of managed objects, then executes a script on the objects returned in the query result. The scanner then sets a field on a specific managed object property to indicate the state of the task. Before you start, you must identify the indexed managed object property that the scanner will use to track task state.

1. Go to `https://<tenant-env-fqdn>/admin/#scheduler/`, and click Add Schedule.

2. Enable the schedule, and set the times that the task should run.

3. Under Perform Action, select Execute a script on objects returned by a query (Task Scanner).

4. Select the managed objects on which the query should be run.

5. Build the query that will be run against the selected managed objects.

   The query must use indexed fields. For time-based queries, use the `${Time.now}` macro object, which fetches the current time and is available only when you configure a scanning task query filter.

6. In the Object Property Field, enter the indexed property whose values will determine the state of the task.

7. In the Script field, enter an inline script.

   The following script deactivates the accounts of users returned by the query:

   ```javascript
   var patch = [{ "operation" : "replace", "field" : "/active", "value" : false },{ "operation" : "replace", "field" : "/accountStatus", "value" : "inactive" }];
   openidm.patch(objectID, null, patch);
   ```

   This script essentially deactivates the accounts of users returned by the query by setting the value of their `active` property to `false`.

8. Configure the advanced properties of the schedule described in [Configure Schedules](configure-schedules.html).

---

---
title: Persistent schedules
description: Configure persistent schedule handling and misfire policies for missed scheduled tasks
component: pingoneaic
page_id: pingoneaic:idm-schedules:persistent-schedules
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/persistent-schedules.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Persistent schedules

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

By default, scheduling information is persistent. The schedule state is stored in the repository rather than in memory. This ensures that schedules survive server restarts and effectively manages execution across a cluster. In a persistent model, a scheduled task launches on only one node in the cluster.

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Non-persisted (in memory) schedules are [deprecated](../product-information/deprecation-notices.html#deprecation-non-persisted-schedules) and will be removed in a future release. |

If the server is down when a scheduled task was set to occur, one or more runs of that schedule might be missed. To specify what action should be taken if schedules are missed, set the [`misfirePolicy`](configure-schedules.html#misfire-policy) in the schedule configuration file. The [`misfirePolicy`](configure-schedules.html#misfire-policy) determines what IDM should do if scheduled tasks are missed. Possible values are as follows:

* `fireAndProceed`

  The first run of a missed schedule is immediately implemented when the server is back online. Subsequent runs are discarded. After this, the normal schedule is resumed.

* `doNothing`

  All missed schedules are discarded and the normal schedule is resumed when the server is back online.

---

---
title: Scan data to trigger tasks
description: Scan managed objects based on complex query filters and execute scripts on matching records
component: pingoneaic
page_id: pingoneaic:idm-schedules:task-scanner
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/task-scanner.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Scan data to trigger tasks

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

In addition to the fine-grained scheduling facility, IDM provides a task scanning mechanism. The task scanner lets you scan a set of properties with a complex query filter, at a scheduled interval, and then launches a script on the objects returned by the query.

The task scanner runs a scheduled task that queries a managed object, then launches a script based on the query results. Scanning tasks are configured in the same way as standard scheduled tasks, as part of the schedule configuration *(tooltip: You can create and change schedule configurations over REST at the openidm/scheduler/job endpoint.)*, with the `invokeService` parameter set to `taskscanner`. The `invokeContext` parameter defines the scan details, and the task that should be launched when the specified condition is triggered.

---

---
title: Schedule examples
description: Example configurations for reconciliation and liveSync scheduling scenarios
component: pingoneaic
page_id: pingoneaic:idm-schedules:scheduler-examples
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/scheduler-examples.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Schedule examples

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

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
description: Schedule reconciliation and synchronization tasks using Quartz simple and cron triggers
component: pingoneaic
page_id: pingoneaic:idm-schedules:schedules
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/schedules.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Schedule tasks and events

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

The scheduler service lets you schedule reconciliation and synchronization tasks.

The service depends on the Quartz Scheduler (bundled with IDM), and supports Quartz simple triggers and cron triggers. Use the trigger type that suits your scheduling requirements. For more information, refer to the Quartz documentation on [SimpleTriggers](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-05.html) and [CronTriggers](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-06.html).

In addition to the fine-grained scheduling facility, you can perform a scheduled batch scan for a specified date in IDM data, and then automatically run a task when this date is reached. For more information, refer to [Scan data to trigger tasks](task-scanner.html).

---

---
title: Schedules
description: Guide to configuring schedules and scanning tasks.
component: pingoneaic
page_id: pingoneaic:idm-schedules:preface
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
---

# Schedules

This guide covers schedules and scanning tasks.

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

[icon: clock, set=far, size=3x]

#### [Scheduling](schedules.html)

Schedule tasks and events.

[icon: tasks, set=fas, size=3x]

#### [Task Scanner](task-scanner.html)

Scan data to trigger tasks.

---

---
title: Schedules and daylight savings time
description: Manage daylight saving time effects on cron-based schedules using simple triggers
component: pingoneaic
page_id: pingoneaic:idm-schedules:schedules-dst
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-schedules/schedules-dst.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Schedules and daylight savings time

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can [schedule jobs](../identities/manage-scheduled-jobs.html) directly in the Advanced Identity Cloud admin console. |

The scheduler service supports Quartz cron triggers and simple triggers. Cron triggers schedule jobs to fire at specific times with respect to a calendar (rather than every N milliseconds). This scheduling can cause issues when clocks change for daylight savings time (DST) if the trigger time falls around the clock change time in your specific time zone.

Depending on the trigger schedule, and on the daylight event, the trigger might be skipped or might appear not to fire for a short period. This interruption can be particularly problematic for liveSync where schedules execute continuously. In this case, the time change (for example, from 02:00 back to 01:00) causes an hour break between each liveSync execution.

To prevent DST from having an impact on your schedules, **use simple triggers instead of cron triggers**.
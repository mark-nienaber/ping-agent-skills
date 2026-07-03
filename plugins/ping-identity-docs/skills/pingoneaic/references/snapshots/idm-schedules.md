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

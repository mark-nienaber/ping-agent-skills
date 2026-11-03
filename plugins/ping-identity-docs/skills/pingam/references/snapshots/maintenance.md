---
title: Back up configurations
description: Back up PingAM configuration files and directory data to recover from server loss or administrative errors
component: pingam
version: 8.1
page_id: pingam:maintenance:backup-restore
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/backup-restore.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Backup &amp; Restore"]
page_aliases: ["maintenance-guide:backup-restore.adoc"]
section_ids:
  backup-for-disaster: Back up instance configuration data
---

# Back up configurations

During normal production operations, you rely on directory replication to maintain multiple, current copies of AM's configuration. To recover from the loss of a server or from a serious administrative error, back up directory data and configuration files.

Find information on backing up your configuration directory server in [Backup and Restore](https://docs.pingidentity.com/pingds/8.1/maintenance-guide/backup-restore.html) in the DS documentation.

## Back up instance configuration data

This procedure backs up the configuration files stored with the server. You can restore this backup when rebuilding a failed server.

Consider the following when using this procedure:

* Refer to the documentation for your external directory server or work with your directory server administrator to back up and restore configuration data stored in the directory server.

  For PingDS, find information in [Backup and restore](https://docs.pingidentity.com/pingds/8.1/maintenance-guide/backup-restore.html) in the DS documentation.

* Do not restore configuration data from a backup of a different major version of AM. The structure of the configuration data can change from release to release.

Follow these steps for each AM server that you want to back up:

1. Stop AM or the container in which it runs.

2. Back up AM server files.

   This example uses the default configuration location, and excludes logs. `$HOME` is the home directory of the user who runs the web container where AM is deployed. AM is deployed in Apache Tomcat under `am`:

   ```bash
   $ cd $HOME
   $ zip -r AM-config-dir-backup-`date -u +%F-%H-%M`.zip am .openamcfg/* \
     -x am/var/debug/* am/var/audit/* am/var/stats*
   …​
   $ ls AM-config-dir-backup-*.zip
   AM-config-dir-backup-2022-10-01-05-07-50.zip
   ```

3. Start AM or the container in which it runs.

---

---
title: Capture troubleshooting information
description: Initiate PingAM recording events through REST calls to capture debug logs, thread dumps, runtime properties, and configuration for troubleshooting
component: pingam
version: 8.1
page_id: pingam:maintenance:record-troubleshooting
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/record-troubleshooting.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Troubleshooting"]
page_aliases: ["maintenance-guide:record-troubleshooting.adoc"]
---

# Capture troubleshooting information

The AM recording facility lets you initiate events to monitor AM while saving output that is useful when performing troubleshooting.

AM recording events save four types of information:

* AM debug logs

* Thread dumps, which show you the status of every active thread, with output similar to a JStack stack trace

* Important runtime properties

* The AM configuration

You initiate a recording event through a REST call with a JSON payload. The payload controls the amount of information AM records, the duration of the recording, and the location of recording output files.

> **Collapse: Recording control payload reference**
>
> Record control payload configuration properties
>
> * `issueID`
>
>   Type: Number
>
>   *Required*. The issue identifier—a positive integer stored internally as a Java `long` data type. A case number is a good choice for the `issueID` value.
>
>   The `issueID` is a component of the path at which recorded information is stored.
>
>   See [Retrieving Recording Information](#recording-location) for more information.
>
> * `referenceID`
>
>   Type: String
>
>   *Required*. A second identifier for the recording event. Use this property to segregate multiple recording events for the same issue.
>
>   The `referenceID` is a component of the path at which recorded information is stored.
>
>   Spaces are not allowed in the `referenceID` value.
>
>   See [Retrieving Recording Information](#recording-location) for more information.
>
> * `Description`
>
>   Type: String
>
>   *Required*. A textual description of the recording event.
>
> * `zipEnable`
>
>   Type: Boolean
>
>   *Required*. Whether to compress the output directory into a zip file when recording has stopped.
>
> * `configExport`
>
>   Type: Object
>
>   *Required*. An object containing the following properties:
>
>   * `enable`
>
>     Type: Boolean
>
>     *Required*. Whether to export the AM configuration upon completion of the recording event. Exporting the AM configuration is a best practice, because it is extremely useful to have access to the configuration when troubleshooting.
>
>   * `password`
>
>     Type: String
>
>     *Required* if `enable` is `true`. A key required to import the exported configuration.
>
>   * `sharePassword`
>
>     Type: Boolean
>
>     *Required* if `enable` is `true`. Whether to show the `password` value in the `info.json` file. This file is output during recording events and contains runtime properties.
>
> * `debugLogs`
>
>   Type: Object
>
>   *Required*. An object containing the following properties:
>
>   * `debugLevel`
>
>     Type: String
>
>     *Required*. The debug level to set for the recording event. Set the value of `debugLevel` to `MESSAGE` to get the most troubleshooting information from your recording period. Other acceptable but less commonly used values are `ERROR` and `WARNING`.
>
>   * `autoStop`
>
>     Type: Object
>
>     *Optional*. Contains another object used to specify an event that automatically ends a recording period. For time-based termination, specify a `time` object; for termination based on uncompressed file size, specify a `fileSize` object. If you specify both `time` and `fileSize` objects, the event that occurs first causes recording to stop.
>
>     Specifying `fileSize` and `time` objects is a best practice, because it ensures that the recorded output does not occupy a larger than expected amount of space on your file system, and that recording events end in a timely fashion.
>
>     * `time`
>
>       Type: Object
>
>       *Optional*; must be specified in the `autoStop` object if `fileSize` is not specified. Configures a recording period to terminate recording after this amount of time.
>
>       * `timeUnit`:
>
>         Type: String
>
>         *Required*. Acceptable values are `MILLISECONDS`, `SECONDS`, `MINUTES`, `HOURS`, and `DAYS`.
>
>         * `value`:
>
>           Type: Numeric
>
>           *Required*. Values in `MILLISECONDS` are rounded down to the second. The minimum acceptable value for `autoStop` is one second.
>
>     * `fileSize`
>
>       Type: Object
>
>       *Optional*; must be specified in the `autoStop` object if `time` is not specified. Configures a recording period to terminate after the aggregate size of uncompressed debug logs has reached this size.
>
>       * `sizeUnit`:
>
>         Type: String
>
>         *Required*. Acceptable values are `B`, `KB`, `MB`, and `GB`.
>
>         * `value`:
>
>           Type: Numeric
>
>           *Required*.
>
> * `threadDump`
>
>   Type: Object
>
>   *Required*. An object containing the following properties:
>
>   * `enable`
>
>     Type: Boolean
>
>     *Required*. Whether to dump threads during the recording event. Thread dumps are especially useful when troubleshooting performance issues and issues with unresponsive servers.
>
>   * `delay`
>
>     Type: Object
>
>     *Required* if `enable` is `true`. Contains another object used to specify an interval at which thread dumps are taken. The initial thread dump is taken at the start of the recording event; subsequent thread dumps are taken at multiples of the `delay` interval.
>
>     * `timeUnit`
>
>       Type: String
>
>       *Required*. Acceptable values are `MILLISECONDS`, `SECONDS`, `MINUTES`, `HOURS`, and `DAYS`.
>
>     * `value`
>
>       Type: Numeric
>
>       *Required*. The minimum acceptable value is one second. Time units that are smaller than seconds, such as `MILLISECONDS`, are rounded to the closest second.

> **Collapse: Recording control payload example**
>
> ```json
> {
>   "issueID": 103572,
>   "referenceID": "policyEvalFails",
>   "description": "Troubleshooting artifacts in support of case 103572",
>   "zipEnable": true,
>   "configExport": {
>     "enable": true,
>     "password": "5x2RR70",
>     "sharePassword": false
>   },
>   "debugLogs": {
>     "debugLevel": "MESSAGE",
>     "autoStop": {
>       "time": {
>         "timeUnit": "SECONDS",
>         "value": 15
>       },
>       "fileSize": {
>         "sizeUnit": "GB",
>         "value": 1
>       }
>     }
>   },
>   "threadDump": {
>     "enable": true,
>     "delay": {
>       "timeUnit": "SECONDS",
>       "value": 5
>     }
>   }
> }
> ```
>
> The recording control payload properties in the preceding example affect the recording output as follows:
>
> **Recording control file example properties and effects on recording behavior**
>
> | Recording Control File Property       | Value                                                 | Effect                                                                                                                                                                                                                             |
> | ------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `issueID`, `referenceID`              | `103572`, `policyEvalFails`                           | Recording output is stored at the path `debugFileLocation/record/103572/policyEvalFails_timestamp.zip`. Find more information about the location of recording output in [Retrieve recording information](recording-location.html). |
> | `Description`                         | `Troubleshooting artifacts in support of case 103572` | No effect.                                                                                                                                                                                                                         |
> | `zipEnable`                           | `true`                                                | Recording output is compressed into a `.zip` file.                                                                                                                                                                                 |
> | `configExport` / `enable`             | `true`                                                | The AM configuration is exported at the start of the recording event.                                                                                                                                                              |
> | `configExport` / `password`           | `5x2RR70`                                             | Knowledge of this password will be required to access the AM configuration that was saved during recording.                                                                                                                        |
> | `configExport` / `sharePassword`      | `false`                                               | The password is not displayed in output messages displayed during the recording event or in the `info.json` file.                                                                                                                  |
> | `debugLogs` / `debugLevel`            | `MESSAGE`                                             | Recording enables message-level debug logs during the recording event.                                                                                                                                                             |
> | `debugLogs` / `autoStop` / `time`     | `SECONDS`, `15`                                       | Because both the `time` and `fileSize` properties are set, recording stops after 15 seconds, or after the size of the debug logs exceeds 1 GB, whichever occurs first.                                                             |
> | `debugLogs` / `autoStop` / `fileSize` | `GB`, `1`                                             | Because both the `time` and `fileSize` properties are set, recording stops after 15 seconds, or after the size of the debug logs exceeds 1 GB, whichever occurs first.                                                             |
> | `threadDump` / `enable`               | `true`                                                | Thread dumps are taken throughout the recording event.                                                                                                                                                                             |
> | `threadDump` / `delay`                | `SECONDS`, `5`                                        | The first thread dump is taken when the recording event starts. Additional thread dumps are taken every five seconds hence.                                                                                                        |

The following table shows different tasks related to recording troubleshooting information:

| Task or Requirement                                                                                                                                      | Resources                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Start and stop recording information**Use REST calls to start and stop recording information. You can also check if there are active recording events. | * [Start and stop recording](rest-api-record-start-stop.html)

* [Get recording status](rest-api-records-get-status.html) |
| **Retrieve information**AM stores the troubleshooting information you gathered, so it is ready to be sent to Ping Identity Support representatives.      | - [Retrieve recording information](recording-location.html)                                                               |

---

---
title: Get recording status
description: Retrieve the current status of a recording event using the PingAM REST API
component: pingam
version: 8.1
page_id: pingam:maintenance:rest-api-records-get-status
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/rest-api-records-get-status.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Monitoring", "REST API"]
page_aliases: ["maintenance-guide:rest-api-records-get-status.adoc"]
---

# Get recording status

To get the status of a recording event, perform an HTTP POST using the `/json/records` endpoint, specifying the `_action=status` parameter in the URL:

```bash
$ curl \
--request POST \
--header "iPlanetDirectoryPro: AQIC5…​" \
--header "Accept-API-Version: resource=1.0" \
https://am.example.com:8443/am/json/records?_action=status
```

If there is no active recording event, the following output appears:

```none
{
    "recording":false
}
```

If there is an active recording event, output similar to the following appears:

```none
{
    "recording":true,
    "record":{
        "issueID":103572,
        "referenceID":"policyEvalFails",
        "description":"Troubleshooting artifacts in support of case 103572",
        "zipEnable":true,
        "threadDump":{
            "enable":true,
            "delay":{
                "timeUnit":"SECONDS",
                "value":5
            }
        },
        "configExport":{
            "enable":true,
            "password":"xxxxxx",
            "sharePassword":false
        },
        "debugLogs":{
            "debugLevel":"message",
            "autoStop":{
                "time":{
                    "timeUnit":"MILLISECONDS",
                    "value":15000
                },
                "fileSize":{
                    "sizeUnit":"KB",
                    "value":1048576
                }
            }
        },
        "status":"RUNNING",
        "folder":"/path/to/am/var/debug/record/103572/policyEvalFails/"
    }
}
```
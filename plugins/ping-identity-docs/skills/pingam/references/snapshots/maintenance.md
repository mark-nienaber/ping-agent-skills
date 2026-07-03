---
title: Back up configurations
description: Back up PingAM configuration files and directory data to recover from server loss or administrative errors
component: pingam
version: 8.1
page_id: pingam:maintenance:backup-restore
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/backup-restore.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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

---

---
title: Maintenance
description: Perform maintenance tasks in PingAM including backing up, restoring, tuning instances, and capturing troubleshooting information
component: pingam
version: 8.1
page_id: pingam:maintenance:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Tuning", "Troubleshooting"]
page_aliases: ["index.adoc", "maintenance-guide:preface.adoc"]
---

# Maintenance

This guide covers how to perform maintenance tasks in PingAM such as backing up and restoring.

[icon: save, set=fad, size=3x]

#### [Back up and restore configurations](backup-restore.html)

How to back up and restore AM.

[icon: cogs, set=fad, size=3x]

#### [Tune instances](tuning-am.html)

Best practices about tuning your AM environment.

[icon: bug, set=fad, size=3x]

#### [Capture troubleshooting](record-troubleshooting.html)

Save output useful for troubleshooting.

---

---
title: Retrieve recording information
description: Locate recorded debugging information by issue ID and reference ID in the PingAM debug file location directory structure
component: pingam
version: 8.1
page_id: pingam:maintenance:recording-location
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/recording-location.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Troubleshooting"]
page_aliases: ["maintenance-guide:recording-location.adoc"]
---

# Retrieve recording information

Information recorded by AM is stored in `debugFileLocation/record/issueID/referenceID`. For example, if the debug file location is `/path/to/am/var/debug`, the issue ID `103572`, and the reference ID `policyEvalFails`, the path containing recorded information is `/path/to/am/var/debug/record/103572/policyEvalFails`.

When there are multiple recording events with the same `issueID` and `referenceID`, AM appends a timestamp to the `referenceID` of the earliest paths. For example, multiple recording events for issue ID `103572` and reference ID `policyEvalFails` might be stored at the following paths:

* Most recent recording: `debugFileLocation/record/103572/policyEvalFails`

* Next most recent recording: `debugFileLocation/record/103572/policyEvalFails_2015-10-24-11-48-51-902-PDT`

* Earliest recording: `debugFileLocation/record/103572/policyEvalFails_2015-08-10-15-15-10-140-PDT`

AM compresses the output from recording events when you set the `zipEnable` property to `true`. The output file can be found at the path `debugFileLocation/record/issueID/referenceID_timestamp.zip`. For example, compressed output for a recording event for issue ID `103572` and reference ID `policyEvalFails` might be stored at the following path: `debugFileLocation/record/103572/policyEvalFails_2015-08-12-12-19-02-683-PDT.zip`.

Use the `referenceID` property value to segregate output when reproducing the same problem multiple times. For example, while troubleshooting case 103572, you notice that you only have a problem when evaluating policy for members of the Finance realm. You could trigger two recording events as follows:

**Segregate recording output using the referenceID**

| AM behavior                                                                 | referenceIDValue     | Recording output path                                |
| --------------------------------------------------------------------------- | -------------------- | ---------------------------------------------------- |
| Policy evaluation behaves as expected for members of the Engineering realm. | `policyEvalSucceeds` | `debugFileLocation/record/103572/policyEvalSucceeds` |
| Policy evaluation unexpectedly fails for members of the Finance realm.      | `policyEvalFails`    | `debugFileLocation/record/103572/policyEvalFails`    |

---

---
title: Start and stop recording
description: Use the PingAM REST API to start and stop recording events for troubleshooting and debugging
component: pingam
version: 8.1
page_id: pingam:maintenance:rest-api-record-start-stop
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/rest-api-record-start-stop.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "REST API"]
page_aliases: ["maintenance-guide:rest-api-record-start-stop.adoc"]
---

# Start and stop recording

To start a recording event:

1. Send an HTTP POST request to the `/json/records` endpoint with the `_action=start` parameter.

2. Specify a JSON payload.

   Find details of the payload contents and an example in [Capture troubleshooting information](record-troubleshooting.html).

You must authenticate to AM as an administrative user to obtain an SSO token prior to calling the `/json/records` REST endpoint. You then pass the SSO token in the `iPlanetDirectoryPro` header as proof of authentication.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: AQIC5…​" \
--header "Accept-API-Version: resource=1.0" \
--data ' {
  "issueID": 103572,
  "referenceID": "policyEvalFails",
  "description": "Troubleshooting artifacts in support of case 103572",
  "zipEnable": true,
  "configExport": {
   "enable": true,
   "password": "5x2RR70",
   "sharePassword": false
  },
  "debugLogs": {
   "debugLevel": "MESSAGE",
   "autoStop": {
    "time":  {
     "timeUnit": "SECONDS",
     "value": 15
    },
    "fileSize": {
     "sizeUnit": "GB",
     "value": 1
    }
   }
  },
  "threadDump" : {
   "enable": true,
   "delay" :  {
    "timeUnit": "SECONDS",
    "value": 5
   }
  }
 }' \
https://am.example.com:8443/am/json/records?_action=start
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

The `curl` command output is indented for ease of reading. The actual output is *not* indented, and the actions available from the `/json/records` endpoint do not support the `_prettyPrint` parameter.

To **stop** a recording event, send an HTTP POST request to the `/json/records` endpoint, specifying the `_action=stop` parameter in the URL:

```bash
$ curl \
--request POST \
--header "iPlanetDirectoryPro: AQIC5…​" \
--header "Accept-API-Version: resource=1.0" \
https://am.example.com:8443/am/json/records?_action=stop
```

If there is no active recording event, AM returns a 400 error code.

If there is an active recording event, output similar to the following appears:

```none
{
  "recording": false,
  "record": {
    "issueID": 103572,
    "referenceID": "policyEvalFails",
    "description": "Troubleshooting artifacts in support of case 103572",
    "zipEnable": true,
    "threadDump": {
      "enable": true,
      "delay": {
        "timeUnit": "SECONDS",
        "value": 5
      }
    },
    "configExport": {
      "enable": true,
      "password": "xxxxxx",
      "sharePassword": false
    },
    "debugLogs": {
      "debugLevel": "message",
      "autoStop": {
        "time": {
          "timeUnit": "MILLISECONDS",
          "value": 15000
        },
        "fileSize": {
          "sizeUnit": "KB",
          "value": 1048576
        }
      }
    },
    "status": "STOPPED",
    "folder": "/path/to/am/var/debug/record/103572/policyEvalFails/"
  }
}
```

---

---
title: Tune AM
description: Learn key PingAM tuning strategies to optimize performance, maximize throughput, and minimize response times for access and federation management
component: pingam
version: 8.1
page_id: pingam:maintenance:tuning-am
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/tuning-am.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Tuning"]
page_aliases: ["maintenance-guide:tuning-am.adoc"]
---

# Tune AM

This page covers key AM tuning strategies to ensure performant access and federation management, and to maximize throughput while minimizing response times.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The recommendations provided here are guidelines for your testing rather than hard and fast rules for every situation. Said another way, the fact that a given setting is configurable implies that no one setting is right in all circumstances.The extent to which performance tuning advice applies depends to a large extent on your requirements, on your workload, and on what resources you have available. Test suggestions before rolling them out into production. |

The suggestions in this page apply to AM deployments with the following characteristics:

* The deployment has a dedicated DS server for the Core Token Service. The host running this directory server is a high-end server with a large amount of memory and multiple CPUs.

* The AM server is configured to use server-side sessions.

The following table summarizes the high-level tasks required to tune an AM instance:

| Task                                      | Resources                                           |
| ----------------------------------------- | --------------------------------------------------- |
| **Tune general AM settings**              | [Tuning server settings](tuning-openam-server.html) |
| **Tune connectivity to LDAP datastores**  | [Tune LDAP connectivity](tuning-ldap-settings.html) |
| **Tune the JVM where AM runs**            | [Tune JVM settings](tuning-jvm-for-openam.html)     |
| **Tune the configuration and user cache** | [Tune caching](caching.html)                        |

---

---
title: Tune caching
description: Configure PingAM caching to optimize performance by tuning global user data cache settings, managing DN cache for authentication, and clearing configuration cache without restarting the server
component: pingam
version: 8.1
page_id: pingam:maintenance:caching
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/caching.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Tuning"]
page_aliases: ["maintenance-guide:caching.adoc"]
section_ids:
  caching-server-settings: Overall server cache settings
  turn-off-global-user-data-caching: Turn off global user data caching
  change-max-cache-size: Change the maximum size of the global user data cache
  clear-config-cache: Clear the configuration cache
  caching-properties: Cache settings
---

# Tune caching

AM caches data to avoid having to query user and configuration datastores each time it needs the information. By default, AM makes use of LDAP persistent search to receive notification of changes to cached data. For this reason, caching works best when data are stored in a directory server that supports LDAP persistent search.

AM has two kinds of configurable cache on the server side; one for configuration data and one for user data. You can generally use the default settings for configuration data cache. This section covers the configuration choices available for caching user data.

AM implements the global user data cache for its user datastores.

The user datastore also supports a *DN cache*, used to cache DN lookups that tend to occur in bursts during authentication. The DN cache can become out of date when a user is moved or renamed in the underlying LDAP store, events that are not always reflected in a persistent search result. You can enable the DN cache when the underlying LDAP store supports persistent search and `mod DN` operations (that is, move or rename DN).

The following diagram depicts the two kinds of cache, and also the two types of caching available for user data:

![Servers cache user data and configuration data separately.](_images/openam-caches.png)Figure 1. Caches

The rest of this page covers settings for global user data cache and for SDK clients. You can find information on datastore cache settings in [Tune LDAP connectivity](tuning-ldap-settings.html).

## Overall server cache settings

By default, AM has caching enabled for both configuration data and user data. This setting is governed by the server property `com.iplanet.am.sdk.caching.enabled`, which is `true` by default. If you set this advanced property to `false`, you can enable caching independently for configuration data and for user data.

### Turn off global user data caching

|   |                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Disabling caching can have a **severe negative impact** on performance. This is because when caching is disabled, AM must query a datastore each time it needs data. |

If, however, you have at least one identity store that does not support LDAP persistent search, then you must disable the *global* cache for user data. Otherwise, user data caches cannot stay in sync with changes to user data entries:

1. In the AM admin UI, go to Deployment > Servers > *server name* > Advanced.

2. Set the value of the `com.iplanet.am.sdk.caching.enabled` property to `false` to disable caching overall.

3. Set the value of the `com.sun.identity.sm.cache.enabled` property to `true` to enable configuration data caching.

   All supported configuration datastores support LDAP persistent search, so it is safe to enable configuration data caching.

   |   |                                                                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You must explicitly set this property to `true`, because setting the value of the property `com.iplanet.am.sdk.caching.enabled` to `false` in the previous step disables both user and configuration data caching. |

4. Save your work.

5. AM starts persistent searches on user datastores when possible(1) in order to monitor changes.

   With user datastore caching disabled, AM still starts the persistent searches, even though it no longer uses the results.

   Therefore, if you disable user datastore caching, you should also disable persistent searches on identity stores in your deployment to improve performance.

   To disable persistent search on an identity store, go to Realms > *realm name* > Identity Stores > *Identity Store Name* > Persistent Search Controls and remove the value of the Persistent Search Base DN configuration property (leave it blank).

(1) AM starts persistent searches on user datastores on directory servers that support the `psearch` control.

### Change the maximum size of the global user data cache

With a large user datastore and active user base, the number of user entries in cache can grow large.

1. In the AM admin UI, go to Configure > Server Defaults > SDK.

2. Change the value of SDK Caching Maximum Size.

   There is no corresponding setting for configuration data, because the number of configuration entries in a large deployment is not likely to grow nearly as large as the number of user entries.

## Clear the configuration cache

When you change configuration property values, the old value remains in effect until the affected service is restarted. To avoid having to restart AM when you change a property value, you can clear the configuration cache and force the new property value to take effect.

To clear the configuration cache, send an empty POST request to the `/json/cache` endpoint with the `clear` action, for example:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: kYQVVJ2YFCuAe-b1xjm7evGBDkw.AAJTSQACMDEAAlNLABxQS0ZIYzBPeFVWUzBQOTNLaHV0elVQemdqVU09AAR0eXBlAANDVFMAAlMxAAA.	" \
--header  "Accept-API-Version: resource=1.0" \
--data '{}' \
https://am.example.com:8443/am/json/cache?_action=clear
{}
```

Only members of a group with the `Realm Admin` or `Cache Admin` privilege can run this operation to clear the cache. All attempts to access the endpoint are audited, including information about the user that attempted to clear the cache.

## Cache settings

The table below provides a quick reference, primarily for user data cache settings.

Notice that many properties for configuration data cache have `sm` (for Service Management) in their names, whereas those for user data have `idm` (for Identity Management) in their names:

**Cache properties**

| Property                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                         | Default      | Applies to     |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------- |
| `com.iplanet.am.sdk.cache.maxSize`                     | Maximum number of user entries cached.                                                                                                                                                                                                                                                                                                                                                                              | 10000        | Server and SDK |
| `com.iplanet.am.sdk.caching.enabled`                   | Whether to enable caching for both configuration data and also for user data.If `true`, this setting overrides `com.sun.identity.idm.cache.enabled` and `com.sun.identity.sm.cache.enabled`.If `false`, you can enable caching independently for configuration data and for user data using the aforementioned properties.                                                                                          | `true`       | Server and SDK |
| `com.iplanet.am.sdk.remote.pollingTime`                | How often in minutes the SDK client, such as a web or a Java agent, should poll AM for modified user data entries.The SDK also uses this value to determine the age of the oldest changes requested. The oldest changes requested are 2 minutes older than this setting. In other words, by default the SDK polls for entries changed in the last 3 minutes.Set this to 0 or a negative integer to disable polling. | 1 (minute)   | SDK            |
| `com.sun.am.event.notification.expire.time`            | How long AM stores a given change to a cached entry, so that clients polling for changes do not miss the change.                                                                                                                                                                                                                                                                                                    | 30 (minutes) | Server only    |
| `com.sun.identity.idm.cache.enabled`                   | If `com.iplanet.am.sdk.caching.enabled` is `true`, this property is ignored.Otherwise, set this to `true` to enable caching of user data.                                                                                                                                                                                                                                                                           | `false`      | Server and SDK |
| `com.sun.identity.idm.cache.entry.default.expire.time` | How many minutes to store a user data entry in the global user data cache.                                                                                                                                                                                                                                                                                                                                          | 30 (minutes) | Server and SDK |
| `com.sun.identity.idm.cache.entry.expire.enabled`      | Whether user data entries in the global user data cache should expire over time.                                                                                                                                                                                                                                                                                                                                    | `false`      | Server and SDK |
| `com.sun.identity.idm.remote.notification.enabled`     | Whether the SDK client, such as a web or a Java agent, should register a notification listener for user data changes with the AM server.The SDK client uses the URL specified by `com.sun.identity.client.notification.url` to register the listener so that AM knows where to send notifications.If notifications cannot be enabled for some reason, then the SDK client falls back to polling for changes.        | `true`       | SDK            |
| `com.sun.identity.sm.cache.enabled`                    | If `com.iplanet.am.sdk.caching.enabled` is `true`, this property is ignored.Otherwise, set this to `true` to enable caching of configuration data. It is recommended that you always set this to `true`.                                                                                                                                                                                                            | `false`      | Server and SDK |
| `sun-idrepo-ldapv3-dncache-enabled`                    | Set this to `true` to enable DN caching of user data.                                                                                                                                                                                                                                                                                                                                                               | `false`      | Server and SDK |
| `sun-idrepo-ldapv3-dncache-size`                       | Sets the cache size.                                                                                                                                                                                                                                                                                                                                                                                                | `1500`       | Server and SDK |

---

---
title: Tune JVM settings
description: This section gives some initial guidance on configuring the JVM for running AM when the deployment has a dedicated CTS token store, and AM is configured to use server-side sessions.
component: pingam
version: 8.1
page_id: pingam:maintenance:tuning-jvm-for-openam
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/tuning-jvm-for-openam.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["maintenance-guide:tuning-jvm-for-openam.adoc"]
---

# Tune JVM settings

This section gives some initial guidance on configuring the JVM for running AM when the deployment has a dedicated CTS token store, and AM is configured to use server-side sessions.

These settings provide a strong foundation to the JVM before a more detailed garbage collection tuning exercise, or as best practice configuration for production:

**Heap size settings**

| JVM parameters                               | Suggested value                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                     |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-Xms` & `-Xmx`                              | At least 1 GB. In production environments, at least 2 to 3 GB. This setting depends on the available physical memory and whether a 32- or 64-bit JVM is used.                                                                                                                                                                                                                   |                                                                                                                                                                                                                                 |
| `-XX:MetaspaceSize` & `-XX:MaxMetaspaceSize` | Set both to 256 MB	Metadata space (Metaspace) is a dedicated region within Native Memory. It can grow automatically if you don't set a maximum size. The ideal Metaspace size depends on your deployment and the number of scripts you're running. 256 MB is considered a safe value for production deployments, but you might need to tweak this for your specific deployment. | Controls the size of the metaspace in the JVM.                                                                                                                                                                                  |
| `-Dsun.net.client.defaultReadTimeout`        | 60000                                                                                                                                                                                                                                                                                                                                                                           | Controls the read timeout in the Java HTTP client implementation.This applies only to the Sun/Oracle HotSpot JVM.                                                                                                               |
| `-Dsun.net.client.defaultConnectTimeout`     | High setting: 30000 (30 seconds)                                                                                                                                                                                                                                                                                                                                                | Controls the connect timeout in the Java HTTP client implementation.When you have hundreds of incoming requests per second, reduce this value to avoid a huge connection queue.This applies only to the Sun/Oracle HotSpot JVM. |

**Security settings**

| JVM parameters                                        | Suggested value | Description                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `-Dhttps.protocols`                                   | `TLSv1.2`       | Controls the protocols used for outbound HTTPS connections from AM.Specify one or more of the following values, separated by commas:- TLSv1.2

- TLSv1.3This setting applies only to Sun/Oracle Java environments.                                                                                                                                     |
| `-Dorg.forgerock.openam.ldap.secure.protocol.version` | `TLSv1.2`       | Controls the protocol AM uses to connect to affected external resources.Specify one or more of the following values, separated by commas:- TLSv1.2

- TLSv1.3This setting overrides the default server value. Learn more in [advanced properties](../setup/deployment-configuration-reference.html#org.forgerock.openam.ldap.secure.protocol.version). |

**Garbage collection settings**

| JVM parameters                    | Suggested value                                      | Description                                                                                                                            |
| --------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `-verbose:gc`                     |                                                      | Verbose garbage collection reporting.                                                                                                  |
| `-Xlog:gc*`                       | `-Xlog:gc=info:file=$CATALINA_HOME/logs/gc-info.log` | Logs detailed information about garbage collection. When using the `-Xlog:gc` option, you can also specify the level, and output file. |
| `-XX:+HeapDumpOnOutOfMemoryError` |                                                      | Out of Memory errors generate a heap dump automatically.                                                                               |
| `-XX:HeapDumpPath`                | `$CATALINA_HOME/logs/heapdump.hprof`                 | Location of the heap dump.                                                                                                             |
| `-XX:+PrintClassHistogram`        |                                                      | Prints a heap histogram when the JVM receives a SIGTERM signal.                                                                        |

**Other settings**

| JVM parameters                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--add-opens java.xml/com.sun.org.apache.xerces.internal.dom=ALL-UNNAMED`    | When running AM, SAML Artifact flows, WS-Federation flows and any flows that use Xerces SOAP libraries can fail with the following error:`Caused by: java.lang.IllegalAccessError: superclass access check failed: class com.sun.xml.messaging.saaj.soap.SOAPDocumentImpl (in unnamed module @0x774ca796) cannot access class com.sun.org.apache.xerces.internal.dom.DocumentImpl (in module java.xml) because module java.xml does not export com.sun.org.apache.xerces.internal.dom to unnamed module @0x774ca796`Set these JVM parameters to avoid this error. |
| `--add-exports java.xml/com.sun.org.apache.xerces.internal.jaxp=ALL-UNNAMED` |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `--add-exports java.xml/com.sun.org.apache.xerces.internal.util=ALL-UNNAMED` |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

---

---
title: Tune LDAP connectivity
description: Configure PingAM LDAP connection pools to improve performance and help with load balancing during failover events
component: pingam
version: 8.1
page_id: pingam:maintenance:tuning-ldap-settings
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/tuning-ldap-settings.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Tuning", "LDAP"]
page_aliases: ["maintenance-guide:tuning-ldap-settings.adoc"]
section_ids:
  to-configure-global-connection-pool-timeout: Configure connection pool timeouts
  tuning-ldap-settings-config: Tune configuration store LDAP connections
  tuning-ldap-settings-cts: Tune CTS store LDAP connections
  tuning-ldap-settings-policies-and-apps: Tune external policy and applications store LDAP connections
  tuning-ldap-settings-data-stores: Tune identity store LDAP connections
  tuning-ldap-settings-uma: Tune UMA store LDAP connections
  tuning-ldap-settings-auth-nodes: Tune authentication node LDAP connections
---

# Tune LDAP connectivity

AM instances use pools of connections when communicating with LDAP datastores. You can tune these connection pools to improve performance and help with load balancing in the case of failover.

AM provides a global timeout setting for connections in a pool. Each store has properties for the maximum pool size, and in some cases, the minimum pool size.

AM attempts to use as few connections to LDAP datastores as possible, down to the minimum pool value, if specified. Under heavy load, AM creates additional connections to the configured datastores, up to the maximum pool value. These connections are made to any of the available LDAP datastores that are configured for the relevant purpose.

When the load begins to drop, some of those connections become idle. If a connection is idle for longer than the configured connection idle time, AM closes the connection, until any specified minimum pool size is reached.

By closing idle connections and recreating them when needed, AM balances connections across all available LDAP servers, rather than keeping the entire pool connected to a single server.

Tuning the connection pool settings can increase performance, or make AM more responsive to LDAP datastore outages.

## Configure connection pool timeouts

1. To configure the timeout used for connections to LDAP stores:

   * Open the `bootstrapConfig.properties` file in the AM classpath; for example, in `/path/to/tomcat/webapps/am/WEB-INF/classes/`.

   * Add, or update the following property, and set the idle timeout, in seconds:

     ```properties
     com.sun.am.ldap.connection.idle.seconds=300
     ```

2. You must also configure the setting in the Advanced section of the server defaults, as follows:

   * In the AM admin UI, go to Configure > Server Defaults > Advanced.

   * Add, or edit the following property, and set the idle timeout, in seconds:

     ```properties
     com.sun.am.ldap.connection.idle.seconds=300
     ```

3. Restart AM or the container in which it runs for these changes to take effect.

   After configuring the timeout for the stores, set the pool sizes assigned to the different stores in the AM admin UI:

   * [Tune configuration store LDAP connections](#tuning-ldap-settings-config)

   * [Tune CTS store LDAP connections](#tuning-ldap-settings-cts)

   * [Tune identity store LDAP connections](#tuning-ldap-settings-data-stores)

   * [Tune external policy and applications store LDAP connections](#tuning-ldap-settings-policies-and-apps)

   * [Tune UMA store LDAP connections](#tuning-ldap-settings-uma)

   * [Tune authentication node LDAP connections](#tuning-ldap-settings-auth-nodes)

## Tune configuration store LDAP connections

To change LDAP configuration store settings, go to Deployment > Servers > *server name* > Directory Configuration.

**LDAP configuration store settings**

| Setting                 | Default value | Details                                                                                                                                                              |
| ----------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Minimum Connection Pool | 1             | Property: `minConnectionPool`                                                                                                                                        |
| Maximum Connection Pool | 10            | The default value of `10` is suitable for most cases; tuning this setting does not affect operational performance, only system startup.Property: `maxConnectionPool` |

## Tune CTS store LDAP connections

You can increase the number of connections used for connecting to the CTS to increase throughput.

The default maximum number of connections to the CTS is 100.

To change the default, go to Deployment > Servers > *server name* > CTS > CTS Token Store, and set the `Max Connections` property.

You may need to click the Inherit value property to unlock the value for editing.

|   |                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also edit the `Max Connections` default setting globally under Configure > Server Defaults > CTS > CTS Token Store tab. |

If you need to change the default CTS connection timeout, go to Deployment > Servers > *server name* > Advanced and set the `org.forgerock.services.datalayer.connection.timeout.cts.async` property.

Most CTS requests to the directory server are handled quickly, so the default timeout of 10 seconds is suitable in most cases.

You must restart AM or the container in which it runs for these changes to take effect.

## Tune external policy and applications store LDAP connections

To change external policy and application datastore settings, go to Configure > Global Services > External Data Stores > Secondary Configurations > *store name*.

|   |                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Policy and application data is stored in the configuration datastore if not configured separately. To manage the configuration store connection pool, refer to [Tune configuration store LDAP connections](#tuning-ldap-settings-config). |

**LDAP policy and application store settings**

| Setting                      | Default value | Information                                                                                       |
| ---------------------------- | ------------- | ------------------------------------------------------------------------------------------------- |
| Minimum Connection Pool Size | 1             | Must be less than the maximum size to allow reaping to function.Property: `minimumConnectionPool` |
| Maximum Connection Pool Size | 10            | Property: `maximumConnectionPool`                                                                 |

## Tune identity store LDAP connections

To change LDAP datastore settings, go to Realms > *realm name* > Identity Stores > *identity store name*. Each store has its own connection pool, so each store needs its own tuning:

**LDAP identity store settings**

| Setting                           | Default value | Details                                                                                                                                                                                                                                                                                                           |
| --------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LDAP Connection Pool Minimum Size | 1             | A good tuning value for this property is 10.Property: `sun-idrepo-ldapv3-config-connection_pool_min_size`                                                                                                                                                                                                         |
| LDAP Connection Pool Maximum Size | 10            | The maximum LDAP connection pool size; a high tuning value for this property is 65, though you might well be able to reduce this for your deployment. Ensure your LDAP server can cope with the maximum number of clients across all the AM servers.Property: `sun-idrepo-ldapv3-config-connection_pool_max_size` |

## Tune UMA store LDAP connections

To increase the number of connections used for UMA-related datastores, go to Deployment > Servers > *server name* > UMA > *UMA store*, and edit the `Max Connections` property.

You may need to click the Inherit value property to unlock the value for editing.

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You can also edit the `Max Connections` default settings globally under Configure > Server Defaults > UMA > *UMA store*. |

**LDAP UMA store settings**

| Setting                                     | Default value | Details                                                                  |
| ------------------------------------------- | ------------- | ------------------------------------------------------------------------ |
| UMA Resource Store > Max Connections        | 10            | Property: `org.forgerock.services.resourcesets.store.max.connections`    |
| UMA Audit Store > Max Connections           | 10            | Property: `org.forgerock.services.umaaudit.store.max.connections`        |
| Pending Requests Store > Max Connections    | 10            | Property: `org.forgerock.services.pendingrequests.store.max.connections` |
| UMA Resource Labels Store > Max Connections | 2             | Property: `org.forgerock.services.uma.labels.store.max.connections`      |

## Tune authentication node LDAP connections

To change connection pool settings for the [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/ldap-decision.html), go to Configure > Authentication > Core Attributes > Global Attributes.

**LDAP authentication node settings**

| Setting                           | Default value | Details                                                                                                                                                                                                                       |
| --------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Default LDAP Connection Pool Size | 1:10          | The minimum and maximum LDAP connection pool used by the LDAP authentication node, separated by a colon (`:`) character.Use `10:65` for production AM instances.Property: `iplanet-am-auth-ldap-connection-pool-default-size` |

---

---
title: Tuning server settings
description: Optimize PingAM server performance by tuning logging, notification thread pools, and session cache settings
component: pingam
version: 8.1
page_id: pingam:maintenance:tuning-openam-server
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/tuning-openam-server.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Tuning", "Sessions"]
page_aliases: ["maintenance-guide:tuning-openam-server.adoc"]
section_ids:
  tuning-general-settings: Logging settings
  tuning-notification-settings: Notification settings
  tuning-session-settings: Session settings
---

# Tuning server settings

AM has a number of settings that can be tuned to increase performance.

## Logging settings

The following general points apply:

* Set debug logging level to `error`.

* Set container-level logging to a low level, such as `error` or `severe`.

## Notification settings

AM has two thread pools used to send notifications to clients. The Service Management Service (SMS) thread pool can be tuned in the AM admin UI, under Configure > Server Defaults > SDK > Data Store:

**SMS notification setting**

| Property               | Default value | Suggestions                                                                                                                                                                                                                                                                                                                                        |
| ---------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Notification Pool Size | 1             | Specifies the size of the thread pool used to send notifications. A value of `1` causes notifications to be processed sequentially, avoiding any potential out-of-order conditions. In production, where configuration is unlikely to change often, keeping the default of `1` is recommended.(`com.sun.identity.sm.notification.threadpool.size`) |

The session service has its own thread pool to send notifications to listeners about changes to server-side sessions. This is configured under Configure > Server Defaults > Session > Notification:

**Session service notification settings**

| Property                           | Default value | Suggestions                                                                                                                                                                                         |
| ---------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Notification Pool Size             | 10            | This is the size of the thread pool used to send notifications. In production this should be around 25-30.(`com.iplanet.am.notification.threadpool.size`)                                           |
| Notification Thread Pool Threshold | 5000          | This is the maximum number of notifications in the queue waiting to be sent. The default value should be fine in the majority of installations.(`com.iplanet.am.notification.threadpool.threshold`) |

## Session settings

The Session service has additional properties to tune, which are configured under Configure > Server Defaults > Session > Session Limits. The following suggestion applies to deployments using server-side sessions:

**Session Settings**

| Property                   | Default Value | Suggestion                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximum Session Cache Size | 5000          | Maximum number of AM sessions to cache on the server.In production, this value can safely be set into the 100,000s. The maximum session cache size is really controlled by the maximum size of the JVM heap which must be tuned appropriately to match the desired session cache size.(`org.forgerock.openam.session.service.access.persistence.caching.maxsize`) |
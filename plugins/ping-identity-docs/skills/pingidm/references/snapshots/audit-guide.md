---
title: Access event topic properties
description: A reference of all properties available in the PingIDM access audit event topic, including request, response, server, and client fields
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:access-event-prop
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/access-event-prop.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Access", "Event", "Properties"]
---

# Access event topic properties

| Event Property                 | Description                                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `_id`                          | UUID for the message object, such as `"0419d364-1b3d-4e4f-b769-555c3ca098b0"`.                                  |
| `timestamp`                    | Time that IDM logged the message, in UTC format; for example, `"2020-05-18T08:48:00.160Z"`.                     |
| `eventName`                    | Name of the audit event: `access` for this log.                                                                 |
| `transactionId`                | UUID of the transaction; the same transaction might display for the same event in different audit event topics. |
| `userId`                       | User ID.                                                                                                        |
| `trackingId`                   | A unique value for the object being tracked.                                                                    |
| `server.ip`                    | IP address of the IDM server.                                                                                   |
| `server.port`                  | Port number used by the IDM server.                                                                             |
| `client.ip`                    | Client IP address.                                                                                              |
| `client.port`                  | Client port number.                                                                                             |
| `request.protocol`             | Protocol for request, typically Common REST.                                                                    |
| `request.operation`            | Common REST operation taken on the object; for example, UPDATE, DELETE, or ACTION.                              |
| `request.detail`               | Typically, details for an ACTION request.                                                                       |
| `http.request.secure`          | Boolean for request security.                                                                                   |
| `http.request.method`          | HTTP method requested by the client.                                                                            |
| `http.request.path`            | Path of the HTTP request.                                                                                       |
| `http.request.queryParameters` | Parameters sent in the HTTP request, such as a key/value pair.                                                  |
| `http.request.headers`         | HTTP headers for the request (optional).                                                                        |
| `http.request.cookies`         | HTTP cookies for the request (optional).                                                                        |
| `http.response.headers`        | HTTP response headers (optional).                                                                               |
| `response.status`              | Normally, SUCCESSFUL, FAILED, or null.                                                                          |
| `response.statusCode`          | SUCCESS in `response.status` leads to a null `response.statusCode`; FAILURE leads to a 400-level error.         |
| `response.detail`              | Message associated with `response.statusCode`, such as Not Found or Internal Server Error.                      |
| `response.elapsedTime`         | Time to execute the access event.                                                                               |
| `response.elapsedTimeUnits`    | Units for response time.                                                                                        |
| `roles`                        | IDM roles associated with the request.                                                                          |

---

---
title: Activity event topic properties
description: Reference for the activity audit event topic properties logged by PingIDM, including fields such as operation, changedFields, and status
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:activity-event-prop
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/activity-event-prop.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Activity", "Event", "Properties"]
---

# Activity event topic properties

| Event Property    | Description                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------- |
| `_id`             | UUID for the message object, such as `"0419d364-1b3d-4e4f-b769-555c3ca098b0"`.                                  |
| `timestamp`       | Time that IDM logged the message, in UTC format; for example, `"2020-05-18T08:48:00.160Z"`.                     |
| `eventName`       | Describes the audit event. Examples include `activity`, `workflow-complete_task`, and `relationship_created`.   |
| `transactionId`   | UUID of the transaction; the same transaction might display for the same event in different audit event topics. |
| `userId`          | User ID.                                                                                                        |
| `trackingId`      | A unique value for the object being tracked.                                                                    |
| `runAs`           | User to run the activity as; may be used in delegated administration.                                           |
| `objectId`        | Object identifier, such as `/managed/user/42f8a60e-2019-4110-a10d-7231c3578e2b`.                                |
| `operation`       | Common REST operation taken on the object; for example, UPDATE, DELETE, or ACTION.                              |
| `before`          | JSON representation of the object prior to the activity.                                                        |
| `after`           | JSON representation of the object after the activity.                                                           |
| `changedFields`   | Fields changed based on [Fields to Watch](activity-log-watch-fields.html#audit-watched-fields).                 |
| `revision`        | Object revision number.                                                                                         |
| `status`          | Result, such as SUCCESS.                                                                                        |
| `message`         | Human readable text about the action.                                                                           |
| `passwordChanged` | True/False entry on changes to the password.                                                                    |

---

---
title: Audit
description: Guide to configuring audit logs and notifications.
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit"]
page_aliases: ["index.adoc"]
---

# Audit

> Guide to configuring audit logs and notifications.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

[icon: glasses, set=fad, size=3x]

#### [Configure Audit](audit.html)

Configure audit logging.

[icon: project-diagram, set=fad, size=3x]

#### [Schema](audit-schema.html)

Learn about the audit schema.

[icon: bell, set=fad, size=3x]

#### [Notifications](notification-config.html)

Configure notifications.

---

---
title: Audit event handler configuration
description: Configure audit event handlers in PingIDM by setting properties in `audit.json` or the admin UI, including common and handler-specific configuration options
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:event-handler-config
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/event-handler-config.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Event", "Handlers"]
---

# Audit event handler configuration

To configure an audit event handler, set the `config` properties for that handler in your project's `conf/audit.json` file.

To configure these properties from the admin UI, click Configure > System Preferences > Audit, and click the edit icon for your event handler.

The tables in this section show the configuration properties common to all audit event handlers, then the properties specific to each audit event handler.

---

---
title: Audit event topics
description: "Describes the six default PingIDM audit event topics: access, activity, authentication, configuration, reconciliation, and synchronization, and how to create custom topics"
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:audit-log-topics
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/audit-log-topics.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration", "Event", "Topics"]
section_ids:
  default-audit-topics: Default audit event topics
  custom-event-topics: Custom audit event topics
---

# Audit event topics

The audit service logs information from six event topics: access, activity, authentication, configuration, reconciliation, and synchronization.

When you start IDM, it creates audit log files in the `openidm/audit` directory. The default file-based audit event handler is the JSON handler, which creates one JSON file for each event topic.

To configure default and custom audit topics in the admin UI, select Configure > System Preferences. Click on the Audit tab, and scroll down to Event Topics.

## Default audit event topics

The audit service logs the following event topics by default:

* Access Events

  IDM writes messages at *system boundaries*, that is REST endpoints and the invocation of scheduled tasks in this log. In short, it includes who, what, and output for every access request.

  Default file: `openidm/audit/access.audit.json`

* Activity Events

  IDM logs operations on internal (managed) and external (system) objects to this log.

  Entries in the activity log contain identifiers, both for the action that triggered the activity, and for the original caller and the relationships between related actions, on internal and external objects.

  Default file: `openidm/audit/activity.audit.json`

* Authentication Events

  IDM logs the results of authentication operations to this log, including situations and the actions taken on each object, including when and how a user authenticated and related events. The activity log contains additional detail about each authentication action.

  Default file: `openidm/audit/authentication.audit.json`

* Configuration Events

  IDM logs the changes to the configuration in this log. The configuration log includes the "before" and "after" settings for each configuration item, with timestamps.

  Default file: `openidm/audit/config.audit.json`

* Reconciliation Events

  IDM logs the results of reconciliation runs to this log (including situations and the resulting actions taken). The activity log contains details about the actions, where log entries display parent activity identifiers, `recon/reconID`, links, and policy events by data store.

  Default file: `openidm/audit/recon.audit.json`

* Synchronization Events

  IDM logs the results of automatic synchronization operations (liveSync and implicit synchronization) to this log, including situations and the actions taken on each object, by account. The activity log contains additional detail about each action.

  Default file: `openidm/audit/sync.audit.json`

For detailed information about each audit event topic, refer to [Audit event handler configuration](event-handler-config.html).

## Custom audit event topics

You can create custom event topics to collect audit information for customizations, such as scripts. Creating a new event topic has a few additional requirements:

* You must specify a schema for your custom topic. The schema determines the structure and type of information stored in audit logs.

* Your script needs to call the new audit event topic (for example `audit/example`), providing the values you specified in your topic schema.

Create custom event topics directly in `audit.json`, or using the admin UI. The following example, from an `audit.json` file, has been modified to include a custom audit event topic named `example`:

```json
"eventTopics": {
  "authentication": {},
  "access": {},
  ...
  "example": {
    "schema": {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "/",
      "type": "object",
      "properties": {
        "_id": {
          "id": "_id",
          "type": "string"
        },
        "transactionId": {
          "id": "transactionId",
          "type": "string"
        },
        "timestamp": {
          "id": "timestamp",
          "type": "string"
        },
        "status": {
          "id": "status",
          "type": "string"
        },
        "message": {
          "id": "message",
          "type": "string"
        }
      },
      "filter": {
        "actions": []
      }
    }
  }
}
```

When your topic has been created, add it to an event handler such as the `JsonAuditEventHandler`, in order to output the audit logs in your desired format. New audit events can be sent by calling the audit topic endpoint (in this example, `audit/example`). For example, the following REST call will add a new audit event for the `example` topic:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
   "transactionId": "779d3cda-dab3-4e54-9ab1-e0ca4c7ae6df-699",
   "timestamp": "2019-02-12T01:11:02.675Z",
   "status": "SUCCESS",
   "message": "Script has run successfully."
}' \
"http://localhost:8080/openidm/audit/example"
{
  "_id": "2091c3f2-7a22-47bf-a618-b2af4c322e46-1192",
  "transactionId": "779d3cda-dab3-4e54-9ab1-e0ca4c7ae6df-699",
  "timestamp": "2019-02-12T01:11:02.675Z",
  "status": "SUCCESS",
  "message": "Script has run successfully."
}
```

This new audit event will be logged to the audit log specified by your event handler. For example, if you had added the `example` topic to the `JsonAuditEventHandler`, you can find your new audit event logged in `audit/example.audit.json`.

---

---
title: Audit log schema
description: "Schema for the six PingIDM audit event topics: access, activity, authentication, config, recon, and sync, and how to parse audit log files"
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:audit-schema
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/audit-schema.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Schema"]
---

# Audit log schema

The tables in this section show the schema for the six audit event topics. For the JSON audit event handler, each audit topic is logged to a distinct JSON file, with the topic in the filename. Files are created in the `openidm/audit` directory by default:

* `access.audit.json`

* `activity.audit.json`

* `authentication.audit.json`

* `config.audit.json`

* `recon.audit.json`

* `sync.audit.json`

You can parse the files in the `openidm/audit` directory using a JSON processor, such as `jq`. For example:

```
tail -f authentication.audit.json | jq .
{
  "context": {
    "component": "internal/user",
    "roles": [
      "internal/role/openidm-admin",
      "internal/role/openidm-authorized"
    ],
    "ipAddress": "0:0:0:0:0:0:0:1",
    "id": "openidm-admin",
    "moduleId": "INTERNAL_USER"
  },
  "entries": [
    {
      "moduleId": "JwtSession",
      "result": "SUCCESSFUL",
      "info": {
        "org.forgerock.authentication.principal": "openidm-admin"
      }
    }
  ],
  "principal": [
    "openidm-admin"
  ],
...
```

---

---
title: Authentication event topic properties
description: Reference for authentication event topic properties logged by the PingIDM audit service, including fields like userId, result, and context
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:auth-event-prop
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/auth-event-prop.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Authentication", "Event", "Properties"]
---

# Authentication event topic properties

| Event Property  | Description                                                                                                                                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`           | UUID for the message object, such as `"0419d364-1b3d-4e4f-b769-555c3ca098b0"`.                                                                                                                                                  |
| `timestamp`     | Time that IDM logged the message, in UTC format; for example, `"2020-05-18T08:48:00.160Z"`.                                                                                                                                     |
| `eventName`     | Name of the audit event: `authentication` for this log.&#xA;&#xA;The eventName field identifies an audit event as a certain type of authentication event, such as a LOGIN, SUCCESS, SESSION, or a FAILED event.                 |
| `transactionId` | UUID of the transaction; the same transaction might display for the same event in different audit event topics.                                                                                                                 |
| `userId`        | User ID.                                                                                                                                                                                                                        |
| `trackingId`    | A unique value for the object being tracked.                                                                                                                                                                                    |
| `result`        | Result of the transaction, either "SUCCESSFUL", or "FAILED".                                                                                                                                                                    |
| `principal`     | An array of the accounts used to authenticate, such as \[ "openidm-admin" ].                                                                                                                                                    |
| `context`       | The complete security context of the authentication operation, including the authenticating ID, targeted endpoint, authentication module, any roles applied, and the IP address from which the authentication request was made. |
| `entries`       | JSON representation of the authentication session.                                                                                                                                                                              |
| `method`        | The authentication module used to authenticate, such as `JwtSession` or `MANAGED_USER`.                                                                                                                                         |

---

---
title: Change audit write behavior
description: Configure buffering for PingIDM audit logging to minimize write operations, using `audit.json` or the admin UI
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:audit-write-adjustments
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/audit-write-adjustments.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration", "Buffering", "Writes"]
---

# Change audit write behavior

You can buffer audit logging to minimize the writes on your systems. Configure buffering either in `conf/audit.json`, or using the admin UI.

To configure buffering for specific event handler in the admin UI, click Configure > System Preferences and click on the Audit tab. When you customize or create an event handler, you can configure the following settings:

**Audit Buffering Options**

| Property    | UI Text       | Description                                                                                       |
| ----------- | ------------- | ------------------------------------------------------------------------------------------------- |
| `enabled`   | True or false | Enables / disables buffering.                                                                     |
| `autoFlush` |               | True or false; whether the Audit Service automatically flushes events after writing them to disk. |

The following sample code illustrates where you would configure these properties in the `audit.json` file.

```json
...
    "eventHandlers" : [
      {
        "config" : {
          ...
          "buffering" : {
            "autoFlush" : false,
            "enabled" : false
          }
        },
...
```

You can set up `autoFlush` when buffering is enabled. IDM then writes data to audit logs asynchronously, while `autoFlush` functionality ensures that the audit service writes data to logs on a regular basis.

If audit data is important, do activate `autoFlush`. It minimizes the risk of data loss in case of a server crash.

---

---
title: Choose audit event handlers
description: Configure PingIDM audit event handlers, including JSON, CSV, Repository, Router, JMS, JsonStdout, and Syslog handlers (JMS, Repository, Router, and Syslog deprecated)
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:configuring-topic-handlers
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/configuring-topic-handlers.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration", "Topics", "Events", "Handlers"]
section_ids:
  audit-json-handler: JSON audit event handler
  audit-json-stdout-handler: JSON standard output audit event handler
  audit-csv-handler: CSV audit event handler
  audit-csv-min: Restrictions on configuring the CSV audit handler in the admin UI
  audit-router-handler: Router Audit Event Handler
  audit-repo-handler: Repository Audit Event Handler
  audit-jms-handler: JMS audit event handler
  dependencies_for_jms_messaging: Dependencies for JMS messaging
  audit-jms-config: Configure the JMS audit event handler
  configure_ssl_for_apache_activemq_artemis: Configure SSL for Apache ActiveMQ Artemis
  audit-jms-message: JMS message format
  audit-jms-tibco-ssl: JMS, TIBCO, and SSL
  audit-syslog-handler: Syslog audit event handler
---

# Choose audit event handlers

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [JMS](#audit-jms-handler), [Repository](#audit-repo-handler), [Router](#audit-router-handler), and [Syslog](#audit-syslog-handler) audit event handlers are [deprecated](../release-notes/deprecated-functionality.html#deprecation-audit-event-handlers) and will be removed in a future release of IDM. Use the [JSON audit event handler](#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack). |

An audit event handler manages audit events, sends audit output to a defined location, and controls the output format. IDM provides a number of default audit event handlers, and audit event handlers for third-party log management tools.

Each audit event handler has a set of [Common audit event handler properties](audit-event-prop.html). Specific audit event handlers have [additional configuration properties](event-handler-config.html).

The standard configuration for a new install includes the following handlers:

* `JsonAuditEventHandler`

  Default state: Enabled

  Property: `openidm.audit.handler.json.enabled`

* `JsonStdoutAuditEventHandler`

  Default state: Disabled

  Property: `openidm.audit.handler.stdout.enabled`

* `RepositoryAuditEventHandler`

  Default state: Disabled

  Property: `openidm.audit.handler.repo.enabled`

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | To change the enable state for any of these handlers, use [Property value substitution](../setup-guide/using-property-substitution.html). |

|   |                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ping recommends you *DO NOT* configure an audit event handler that points to the same repo IDM uses (`RepositoryAuditEventHandler`), as this causes audit records to compete with IDM for resources on the database, which impacts performance. |

> **Collapse: List the Active Audit Event Handlers**
>
> This command returns the available audit event handlers, along with the audit configuration (in the `conf/audit.json` file):
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request POST \
> "http://localhost:8080/openidm/audit?_action=availableHandlers"
> ```
>
> The output includes the configured options for each audit event handler.
>
> To view the audit configuration in the admin UI, click Configure > System Preferences > Audit.

The following sections show how to configure the standard audit event handlers. For additional audit event handlers, refer to [Audit event handler configuration](event-handler-config.html).

## JSON audit event handler

The JSON audit event handler logs events as JSON objects to a set of JSON files. This is the default handler for queries on the audit logs.

|   |                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Result paging can improve responsiveness when scanning large numbers of audit records through the IDM REST API. The default JSON audit handler does not support paging. If you need to page audit results, use a handler that does support paging, such as the [Repository Audit Event Handler](#audit-repo-handler). |

The following excerpt of an `audit.json` file shows a sample JSON audit event handler configuration:

```json
"eventHandlers" : [
    {
        "class" : "org.forgerock.audit.handlers.json.JsonAuditEventHandler",
        "config" : {
            "name" : "json",
            "enabled" : {
                "$bool" : "&{openidm.audit.handler.json.enabled|true}"
            },
            "logDirectory" : "&{idm.data.dir}/audit",
            "buffering" : {
                "maxSize" : 100000,
                "writeInterval" : "100 millis"
            },
            "topics" : [
                "access",
                "activity",
                "sync",
                "authentication",
                "config"
            ]
        }
    },
```

A JSON audit event handler configuration includes the following mandatory properties:

* `name`

  The audit event handler name (`json`).

* `logDirectory`

  The name of the directory in which the JSON log files should be written, relative to the *working location*. For more information on the working location, refer to [Startup configuration](../install-guide/startup-configuration.html).

  You can use property value substitution to direct log files to another location on the filesystem. For more information, refer to [Property value substitution](../setup-guide/using-property-substitution.html).

* `buffering` - `maxSize`

  The maximum number of events that can be buffered. The default (and minimum) number of buffered events is 100000.

* `buffering` - `writeInterval`

  The delay after which the file-writer thread is scheduled to run after encountering an empty event buffer. The default delay is 100 milliseconds.

* `topics`

  The list of topics for which audit events are logged.

  One JSON file is created for each audit topic that is included in this list:

  `access.audit.json`\
  `activity.audit.json`\
  `authentication.audit.json`\
  `config.audit.json`\
  `sync.audit.json`

  |   |                                                                                                                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Reconciliations are available as an audit topic, but are not enabled by default. To enable auditing on reconciliations, add `recon` to the list of topics. This will add a `recon.audit.json` file to the audit directory. |

  If you want to get information about a reconciliation without enabling the audit topic, you can get similar details from the `recon/assoc` endpoint. For more information about recon association data, refer to [Viewing Reconciliation Association Details](../synchronization-guide/manage-recon.html#recon-assoc).

  For a description of all the configurable properties of the JSON audit event handler, refer to [JSON Audit Event Handler Properties](event-handler-config.html#audit-config-prop-json).

The following excerpt of an `authentication.audit.json` file shows the log message format for authentication events:

```json
{
	"context": {
		"ipAddress": "0:0:0:0:0:0:0:1"
	},
	"entries": [{
		"moduleId": "JwtSession",
		"result": "FAILED",
		"reason": {},
		"info": {}
	},
 ...
	{
		"moduleId": "INTERNAL_USER",
		"result": "SUCCESSFUL",
		"info": {
			"org.forgerock.authentication.principal": "openidm-admin"
		}
	}],
	"principal": ["openidm-admin"],
	"result": "SUCCESSFUL",
	"userId": "openidm-admin",
	"transactionId": "94b9b85f-fbf1-4c4c-8198-ab1ff52ed0c3-24",
	"timestamp": "2016-10-11T12:12:03.115Z",
	"eventName": "authentication",
	"trackingIds": ["5855a363-a1e0-4894-a2dc-fd5270fb99d1"],
	"_id": "94b9b85f-fbf1-4c4c-8198-ab1ff52ed0c3-30"
} {
	"context": {
		"component": "internal/user",
		"roles": ["internal/role/openidm-admin", "internal/role/openidm-authorized"],
		"ipAddress": "0:0:0:0:0:0:0:1",
		"id": "openidm-admin",
		"moduleId": "INTERNAL_USER"
	}...
```

## JSON standard output audit event handler

Standard output is also known as `stdout`. A JSON stdout handler sends messages to standard output. The following code is an excerpt of the `audit.json` file, which depicts a sample JSON stdout audit event handler configuration:

```json
{
    "class" : "org.forgerock.audit.handlers.json.stdout.JsonStdoutAuditEventHandler",
    "config" : {
        "name" : "stdout",
        "enabled" : {
            "$bool" : "&{openidm.audit.handler.stdout.enabled|false}"
        },
        "topics" : [
            "access",
            "activity",
            "sync",
            "authentication",
            "config"
        ]
    }
}...
```

## CSV audit event handler

The CSV audit event handler logs events to a comma-separated value (CSV) file.

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The CSV handler does not sanitize messages when writing to CSV log files.Do not open CSV logs in spreadsheets and other applications that treat data as code. |

The following excerpt of the `audit.json` file shows a sample CSV handler configuration:

```json
"eventHandlers" : [
{
    "class" : "org.forgerock.audit.events.handlers.csv.CSVAuditEventHandler",
    "config" : {
        "name" : "csv",
        "logDirectory" : "&{idm.data.dir}/audit",
        "topics" : [ "access", "activity", "sync", "authentication", "config" ]
    }
}
```

The `logDirectory` indicates the name of the directory in which log files should be written, relative to the *working location*. For more information on the working location, refer to [Startup configuration](../install-guide/startup-configuration.html).

You can use property value substitution to direct logs to another location on the filesystem. For more information, refer to [Property Value Substitution](../setup-guide/chap-configuration.html#using-property-substitution).

If you set up a custom CSV handler, you may configure over 20 different properties, as described in [Common Audit Event Handler Properties](event-handler-config.html#audit-event-prop).

Audit file names are fixed and correspond to the event being audited:

`access.csv`\
`activity.csv`\
`authentication.csv`\
`config.csv`\
`recon.csv`\
`sync.csv`

### Restrictions on configuring the CSV audit handler in the admin UI

If you configure the CSV handler in the admin UI, set at least the following properties:

* The `logDirectory`, the full path to the directory with audit logs, such as `/path/to/openidm/audit` . You can substitute &{idm.install.dir} for `/path/to/openidm` .

* Differing entries for the quote character, `quoteChar` and delimiter character, `delimiterChar`.

  After you have set these options, *do not change them* in the admin UI. Rather, rotate any CSV audit files and edit the configuration properties directly in `conf/audit.json`. Changing the properties in the admin UI generates an error in the console.

|   |                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `signatureInterval` property supports time settings in a human-readable format (default = 1 hour). Examples of allowable `signatureInterval` settings are:* 3 days, 4 m

* 1 hour, 3 secAllowable time units include:* days, day, d

* hours, hour, h

* minutes, minute, min, m

* seconds, second, sec, s |

## Router Audit Event Handler

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [JMS](#audit-jms-handler), [Repository](#audit-repo-handler), [Router](#audit-router-handler), and [Syslog](#audit-syslog-handler) audit event handlers are [deprecated](../release-notes/deprecated-functionality.html#deprecation-audit-event-handlers) and will be removed in a future release of IDM. Use the [JSON audit event handler](#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack). |

The router audit event handler logs events to any external or custom endpoint, such as `system/scriptedsql` or `custom-endpoint/myhandler`. It uses target-assigned values of `_id`.

A sample configuration for a `router` event handler is provided in the `audit.json` file in the `openidm/samples/audit-jdbc/conf` directory, and described in [About the Configuration Files](../samples-guide/audit-jdbc.html#audit-config-files). This sample directs log output to a JDBC repository. The audit configuration file (`conf/audit.json`) for the sample shows the following event handler configuration:

```json
{
    "class": "org.forgerock.openidm.audit.impl.RouterAuditEventHandler",
    "config": {
        "name": "router",
        "topics" : [ "access", "activity", "sync", "authentication", "config" ],
        "resourcePath" : "system/auditdb"
    }
},
```

The `resourcePath` property in the configuration indicates that logs should be directed to the `system/auditdb` endpoint. This endpoint, and the JDBC connection properties, are defined in the connector configuration file (`conf/provisioner.openicf-auditdb.json`), as follows:

```json
{
    "configurationProperties" : {
        "username" : "root",
        "password" : "password",
        "driverClassName" : "com.mysql.cj.jdbc.Driver",
        "url" : "jdbc:mysql://&{openidm.repo.host}:&{openidm.repo.port}/audit",
        "autoCommit" : true,
        "jdbcDriver" : "com.mysql.cj.jdbc.Driver",
        "scriptRoots" : ["&{idm.instance.dir}/tools"],
        "createScriptFileName" : "CreateScript.groovy",
        "testScriptFileName" : "TestScript.groovy",
        "searchScriptFileName" : "SearchScript.groovy"
    },
...
```

Include the correct URL or IP address of your remote JDBC repository in the `boot.properties` file for your project.

When JSON information is sent to the router audit event handler, the value of `_id` is replaced with `eventId`.

## Repository Audit Event Handler

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [JMS](#audit-jms-handler), [Repository](#audit-repo-handler), [Router](#audit-router-handler), and [Syslog](#audit-syslog-handler) audit event handlers are [deprecated](../release-notes/deprecated-functionality.html#deprecation-audit-event-handlers) and will be removed in a future release of IDM. Use the [JSON audit event handler](#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack). |

The repository audit event handler sends information to a JDBC repository. If you are using PingDS (DS) as the repository, you cannot enable this audit event handler, because audit data cannot be stored in DS.

|   |                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Ping recommends you *DO NOT* use the `RepositoryAuditEventHandler`, as this causes audit records to compete with IDM for resources on the database, which impacts performance. |

Log entries are stored in the following tables of a JDBC repository:

* `auditaccess`

* `auditactivity`

* `auditauthentication`

* `auditconfig`

* `auditrecon`

* `auditsync`

You can use the repository audit event handler to generate reports that combine information from multiple tables.

Each of these JDBC tables maps to an object in the database table configuration file (`repo.jdbc.json`). The following excerpt of that file illustrates the mappings for the `auditauthentication` table:

```json
"audit/authentication" : {
    "table" : "auditauthentication",
    "objectToColumn" : {
        "_id" : "objectid",
        "transactionId" : "transactionid",
        "timestamp" : "activitydate",
        "userId" : "userid",
        "eventName" : "eventname",
        "result" : "result",
        "principal" : {"column" : "principals", "type" : "JSON_LIST"},
        "context" : {"column" : "context", "type" : "JSON_MAP"},
        "entries" : {"column" : "entries", "type" : "JSON_LIST"},
        "trackingIds" : {"column" : "trackingids", "type" : "JSON_LIST"},
    }
},
```

The tables correspond to the `topics` listed in the `audit.json` file. For example:

```json
{
    "class": "org.forgerock.openidm.audit.impl.RepositoryAuditEventHandler",
    "config": {
        "name": "repo",
        "topics" : [ "access", "activity", "sync", "authentication", "config" ]
    }
},
```

## JMS audit event handler

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [JMS](#audit-jms-handler), [Repository](#audit-repo-handler), [Router](#audit-router-handler), and [Syslog](#audit-syslog-handler) audit event handlers are [deprecated](../release-notes/deprecated-functionality.html#deprecation-audit-event-handlers) and will be removed in a future release of IDM. Use the [JSON audit event handler](#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack). |

The Java Message Service (JMS) is a Java API for sending asynchronous messages between clients. IDM audit information can be handled by the JMS audit event handler, which sends information to message brokers. The message brokers can then forward that information to external log analysis systems.

The JMS audit event handler works with the following message brokers:

* [Apache ActiveMQ Artemis](http://activemq.apache.org/).

  For a demonstration, refer to [Direct audit information to a JMS broker](../samples-guide/audit-jms.html).

* [TIBCO Enterprise Message Service](https://tap.tibco.com/storefront/trialware/tibco-enterprise-message-service/prod15032.html), as described in this topic.

This implementation supports the *publish/subscribe* model. Learn more in [Basic JMS API Concepts](http://docs.oracle.com/javaee/6/tutorial/doc/bncdx.html).

|   |                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The JMS audit event handler does not support queries. If you enable JMS, and need to query audit events, you must enable a second audit handler that supports queries. Specify that audit handler in the `audit.json` file with the `handlerForQueries` property, or in the admin UI with the Use For Queries option. |

The JMS audit event handler supports JMS communication, based on the following components:

* A JMS message broker that provides clients with connectivity, along with message storage and message delivery functionality.

* JMS messages that follow a specific format, described in [JMS Message Format](#audit-jms-message).

* Destinations external to IDM and the message broker. IDM (including the audit service) is a *producer* and not a destination. IDM sends messages to a topic in a message broker. Consumers (clients) subscribe to the message broker.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | *JMS Topics* are not the same as the Ping audit event `topics` listed in your project's `audit.json` file. For more information about JMS topics, refer to the documentation on the [publish/subscribe model](http://docs.oracle.com/javaee/6/tutorial/doc/bncdx.html#bnced). Ping audit event topics specify categories of events (including access, activity, authentication, configuration, reconciliation, and synchronization). These event topics are published via the audit handler(s). |

### Dependencies for JMS messaging

The JMS audit event handler requires Apache ActiveMQ Artemis and additional dependencies bundled with the ActiveMQ Artemis delivery. This section lists the dependencies, and where they must be installed in the IDM instance. If you use a different ActiveMQ version, you may need to download the corresponding dependencies separately.

1. Download the following files:

   * [Apache ActiveMQ Artemis](https://activemq.apache.org/components/artemis/download/).

     |   |                                             |
     | - | ------------------------------------------- |
     |   | This sample was tested with version 2.20.0. |

   * The most recent `bnd` JAR file from <https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd/>.

     |   |                                                                                                                   |
     | - | ----------------------------------------------------------------------------------------------------------------- |
     |   | The [bnd](https://bnd.bndtools.org/) utility lets you create OSGi bundles for libraries that do not support OSGi. |

2. Unpack the ActiveMQ Artemis archive. For example:

   ```
   tar -xvf ~/Downloads/apache-artemis-2.20.0-bin.tar.gz
   ```

3. Create a temporary directory, and then change to that directory:

   ```
   mkdir ~/Downloads/tmp
   cd ~/Downloads/tmp/
   ```

4. Move the ActiveMQ Artemis Client and `bnd` JAR files to the temporary directory.

   ```
   mv ~/Downloads/apache-artemis-2.20.0/lib/client/artemis-jms-client-all-2.20.0.jar ~/Downloads/tmp/
   mv ~/Downloads/biz.aQute.bnd-version.jar ~/Downloads/tmp/
   ```

5. Create an OSGi bundle:

   1. In a text editor, create a BND file named `activemq.bnd` with the following contents, and save it to the current directory:

      ```
      version=2.20.0
      Export-Package: *;version=${version}
      Import-Package: !org.apache.log4j.*,!org.apache.log.*,!org.apache.avalon.framework.logger.*,!org.apache.avalon.framework.logger.*,!org.glassfish.json.*,!org.conscrypt.*,!org.apache.logging.*,!org.bouncycastle.jsse.*,!org.eclipse.*,!sun.security.*,!reactor.*,!org.apache.activemq.artemis.shaded.*,!com.aayushatharva.*,!com.github.luben.zstd,!com.jcraft.jzlib,!com.ning.compress,!com.ning.compress.lzf,!com.ning.compress.lzf.util,!com.oracle.svm.core.annotate,!lzma.*,!net.jpountz.*,*
      Bundle-Name: ActiveMQArtemis :: Client
      Bundle-SymbolicName: org.apache.activemq
      Bundle-Version: ${version}
      ```

      Your `tmp/` directory should now contain the following files:

      ```
      ls -1 ~/Downloads/tmp/
      activemq.bnd
      artemis-jms-client-all-2.20.0.jar
      biz.aQute.bnd-version.jar
      ```

   2. In the same directory, create the OSGi bundle archive file. For example:

      ```
      java -jar biz.aQute.bnd-version.jar wrap \
      --properties activemq.bnd \
      --output artemis-jms-client-all-2.20.0-osgi.jar \
      artemis-jms-client-all-2.20.0.jar
      ```

6. Copy the resulting `artemis-jms-client-all-2.20.0-osgi.jar` file to the `openidm/bundle` directory:

   ```
   cp artemis-jms-client-all-2.20.0-osgi.jar /path/to/openidm/bundle/
   ```

### Configure the JMS audit event handler

You can configure the JMS audit event handler in the admin UI, or in your `conf/audit.json` file.

To configure the JMS audit event handler in the admin UI:

1. Select Configure > System Preferences > Audit.

2. Under Event Handlers, select JmsAuditEventHandler > Add Event Handler.

The event handler configuration properties are discussed in this section. For a complete list of configuration options, refer to [JMS Audit Event Handler Properties](audit-config-prop-jms.html).

To configure the audit event handler in the `conf/audit.json` file, refer to the sample configuration provided in `/path/to/openidm/samples/audit-jms/conf/audit.json`. The following excerpt of that file shows the JMS audit event handler configuration:

```json
{
    "class" : "org.forgerock.audit.handlers.jms.JmsAuditEventHandler",
    "config" : {
        "name": "jms",
        "enabled" : true,
        "topics": [
            "access",
            "activity",
            "config",
            "authentication",
            "sync",
            "recon"
        ],
        "deliveryMode": "NON_PERSISTENT",
        "sessionMode": "AUTO",
        "batch": {
            "writeInterval": "1 second",
            "capacity": 1000,
            "maxBatchedEvents": 100
        },
        "jndi": {
            "contextProperties": {
                "java.naming.factory.initial" : "org.apache.activemq.artemis.jndi.ActiveMQInitialContextFactory",
                "java.naming.provider.url" : "tcp://127.0.0.1:61616?daemon=true",
                "topic.forgerock.idm.audit" : "forgerock.idm.audit"
            },
            "topicName": "forgerock.idm.audit",
            "connectionFactoryName": "ConnectionFactory"
        }
    }
}
```

In this sample configuration, the JMS audit event handler is `enabled`, with `NON_PERSISTENT` delivery of audit events in batches. The handler is configured to use the Apache ActiveMQ Artemis Java Naming and Directory Interface (JNDI) message broker, on port 61616.

For an example of how to configure Apache ActiveMQ Artemis, refer to [Direct audit information to a JMS broker](../samples-guide/audit-jms.html).

If you substitute a different JNDI message broker, change the `jndi.contextProperties` accordingly. If you configure the JNDI message broker on a remote system, substitute the corresponding IP address.

#### Configure SSL for Apache ActiveMQ Artemis

For information on configuring Apache ActiveMQ Artemis security features, including SSL, download [ActiveMQ Artemis 2.2.0](https://archive.apache.org/dist/activemq/activemq-artemis/2.2.0/) and view the included documentation.

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also view the [latest Apache Artemis documentation](https://artemis.apache.org/components/artemis/documentation/latest/index.html), but the features described might differ from the version tested with IDM. |

### JMS message format

The following JMS message reflects the authentication of the `openidm-admin` user, logging into the admin UI from a remote location, IP address 172.16.209.49.

```json
{
  "event": {
    "_id": "134ee773-c081-436b-ae61-a41e8158c712-565",
    "trackingIds": [
      "4dd1f9de-69ac-4721-b01e-666df388fb17",
      "185b9120-406e-47fe-ba8f-e95fd5e0abd8"
    ],
  "context": {
    "id": "openidm-admin",
    "ipAddress": "172.16.209.49",
    "roles": [
      "internal/role/openidm-admin",
      "internal/role/openidm-authorized"
    ],
    "component": "internal/user"
  },
  "entries": [
    {
      "info": {
        "org.forgerock.authentication.principal": "openidm-admin"
      },
      "result": "SUCCESSFUL",
      "moduleId": "JwtSession"
    }
  ],
  "principal": [
    "openidm-admin"
  ],
    "result": "SUCCESSFUL",
    "userId": "openidm-admin",
    "transactionId": "134ee773-c081-436b-ae61-a41e8158c712-562",
    "timestamp": "2016-04-15T14:57:53.114Z",
    "eventName": "authentication"
  },
  "auditTopic": "authentication"
}
```

### JMS, TIBCO, and SSL

You can integrate the JMS audit event handler with the [TIBCO Enterprise Message Service](https://docs.tibco.com/products/tibco-enterprise-message-service).

You'll need to use two bundles from your TIBCO installation: `tibjms.jar`, and if you're setting up a secure connection, `tibcrypt.jar`. With the following procedure, you'll process `tibjms.jar` into an OSGi bundle:

1. Download the most recent `bnd` JAR file from <https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd/>. The [bnd](http://bnd.bndtools.org/) utility lets you create OSGi bundles for libraries that do not yet support OSGi. If you have previously set up the ActiveMQ Artemis server, you may have already downloaded this file.

2. In the same directory, create a file named `tibco.bnd` , and add the following lines to that file:

   ```none
   version=8.3.0
   Export-Package: *;version=${version}
   Bundle-Name: TIBCO Enterprise Message Service
   Bundle-SymbolicName: com/tibco/tibjms
   Bundle-Version: ${version}
   ```

3. Add the `tibco.jar` file to the same directory.

4. Run the following command to create the bundle:

   ```
   java \
   -jar biz.aQute.bnd-version.jar wrap \
   -properties tibco.bnd tibjms.jar
   ```

5. Rename the newly created `tibjms.bar` file to `tibjms-osgi.jar` , and copy it to the `/path/to/openidm/bundle` directory.

6. If you're configuring SSL, copy the `tibcrypt.jar` file from your TIBCO installation to the `/path/to/openidm/bundle` directory.

You also need to configure your project's `audit.conf` configuration file. The options are similar to those listed previously in [Configure the JMS audit event handler](#audit-jms-config), except for the following `jndi` code block:

```json
"jndi": {
   "contextProperties": {
      "java.naming.factory.initial" : "com.tibco.tibjms.naming.TibjmsInitialContextFactory",
      "java.naming.provider.url" : "tibjmsnaming://localhost:7222"
   },
   "topicName": "audit",
   "connectionFactoryName": "ConnectionFactory"
}
```

If your TIBCO server is on a remote system, substitute appropriately for `localhost`. If you're configuring a secure TIBCO installation, you'll want to configure a different code block:

```json
"jndi": {
   "contextProperties": {
      "java.naming.factory.initial" : "com.tibco.tibjms.naming.TibjmsInitialContextFactory",
      "java.naming.provider.url" : "ssl://localhost:7243",
      "com.tibco.tibjms.naming.security_protocol" : "ssl",
      "com.tibco.tibjms.naming.ssl_trusted_certs" : "/path/to/tibco/server/certificate/cert.pem",
      "com.tibco.tibjms.naming.ssl_enable_verify_hostname" : "false"
   },
   "topicName": "audit",
   "connectionFactoryName": "SSLConnectionFactory"
}
```

Do not add the TIBCO certificate to the IDM `truststore`. The formats are not compatible.

When this configuration work is complete, don't forget to start your TIBCO server before starting IDM. For more information, refer to the [TIBCO Enterprise Message Service Users's Guide](https://docs.tibco.com/pub/ems/8.3.0/doc/pdf/TIB_ems_8.3_users_guide.pdf).

## Syslog audit event handler

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [JMS](#audit-jms-handler), [Repository](#audit-repo-handler), [Router](#audit-router-handler), and [Syslog](#audit-syslog-handler) audit event handlers are [deprecated](../release-notes/deprecated-functionality.html#deprecation-audit-event-handlers) and will be removed in a future release of IDM. Use the [JSON audit event handler](#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack). |

The Syslog audit event handler lets you log messages to a Syslog server, based on the [Syslog Protocol](https://www.rfc-editor.org/rfc/rfc5424.html).

You can configure the Syslog audit event handler in the admin UI, or in your project's `conf/audit.json` file. The following excerpt from this file shows a possible Syslog configuration:

```json
{
    "class" : "org.forgerock.audit.handlers.syslog.SyslogAuditEventHandler",
    "config" : {
        "protocol" : "UDP",
        "host" : "172.16.206.5",
        "port" : 514,
        "connectTimeout" : 5,
        "facility" : "KERN",
        "severityFieldMappings" : [
            {
                "topic" : "recon",
                "field" : "exception",
                "valueMappings" : {
                    "SEVERE" : "EMERGENCY",
                    "INFO" : "INFORMATIONAL"
                }
            }
        ],
        "buffering" : {
            "enabled" : false
        },
        "name" : "syslog1",
        "topics" : [
            "config",
            "activity",
            "authentication",
            "access",
            "recon",
            "sync"
        ],
        "enabled" : true
    }
}
```

The `name`, `topics`, and `enabled` options in the last part of the excerpt are common to all audit event handlers. For detailed information on the remaining properties, refer to [Syslog Audit Event Handler Properties](event-handler-config.html#audit-config-prop-syslog).

---

---
title: Common audit event handler properties
description: Reference table of common audit event handler properties, including name, topics, query handling, and enabled status
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:audit-event-prop
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/audit-event-prop.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Common Audit Event", "Handlers"]
---

# Common audit event handler properties

| UI Label / Text            | audit.json File Label | Description                                                                                                                                                                 |
| -------------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                       | `name`                | `config` sub-property. The name of the audit event handler.                                                                                                                 |
| Audit Events               | `topics`              | `config` sub-property; the list of audit topics that are logged by this audit event handler, for example, `access`, `activity`, and `config`.                               |
| Use for Queries            | `handlerForQueries`   | Specifies whether this audit event handler manages the queries on audit logs.                                                                                               |
| Enabled                    | `enabled`             | `config` sub-property; specifies whether the audit event handler is enabled. An audit event handler can be configured, but disabled; in which case, it will not log events. |
| n/a                        | `config`              | The JSON object used to configure the handler; includes several sub-properties.                                                                                             |
| Shown only in `audit.json` | `class`               | The class name in the Java file(s) used to build the handler.                                                                                                               |

---

---
title: Configuration event topic properties
description: Reference for the properties logged in PingIDM configuration audit events, including object identifiers, operations, and changed field data
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:config-event-prop
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/config-event-prop.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration", "Event", "Properties"]
---

# Configuration event topic properties

| Event Property  | Description                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| `_id`           | UUID for the message object, such as `"0419d364-1b3d-4e4f-b769-555c3ca098b0"`.                                  |
| `timestamp`     | Time that IDM logged the message, in UTC format; for example, `"2020-05-18T08:48:00.160Z"`.                     |
| `eventName`     | Name of the audit event: `config` for this log.                                                                 |
| `transactionId` | UUID of the transaction; the same transaction might display for the same event in different audit event topics. |
| `userId`        | User ID.                                                                                                        |
| `trackingId`    | A unique value for the object being tracked.                                                                    |
| `runAs`         | User to run the activity as; can be used in delegated administration.                                           |
| `objectId`      | Object identifier, such as `ui`.                                                                                |
| `operation`     | Common REST operation taken on the object; for example, UPDATE, DELETE, or ACTION.                              |
| `before`        | JSON representation of the object prior to the activity.                                                        |
| `after`         | JSON representation of the object after to the activity.                                                        |
| `changedFields` | Fields changed based on [Fields to Watch](activity-log-watch-fields.html#audit-watched-fields).                 |
| `revision`      | Object revision number.                                                                                         |

---

---
title: Configure an audit exception formatter
description: Configure the PingIDM audit exception formatter, which controls how exceptions are formatted and written to the audit log
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:audit-exception-formatter
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/audit-exception-formatter.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration", "Exception Formatter"]
---

# Configure an audit exception formatter

The audit service includes an *exception formatter*, configured in the following snippet of the `audit.json` file:

```json
"exceptionFormatter" : {
   "type" : "text/javascript",
   "file" : "bin/defaults/script/audit/stacktraceFormatter.js"
},
```

As shown, you may find the script that defines how the exception formatter works in the `stacktraceFormatter.js` file. That file handles the formatting and display of exceptions written to the audit logger.

---

---
title: Configure audit logging
description: Configure the PingIDM audit service to publish and log system activity, access, authentication, and configuration changes to local or remote targets
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:audit
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/audit.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration"]
---

# Configure audit logging

The audit service publishes and logs information to one or more targets, including local data files, the repository, and remote systems.

Audit logs help you to record activity by account. With audit data, you can monitor logins, identify problems such as unresponsive devices, and collect information to comply with regulatory requirements.

The audit service logs information related to the following events:

* System access

* System activity

* Authentication operations

* Configuration changes

* Reconciliations

* Synchronizations

You can customize what is logged for each event type. Auditing provides the data for all relevant reports, including those related to orphan accounts.

When you first start IDM, an audit log file for each configured audit event topic is created in the `/path/to/openidm/audit` directory. Until there is a relevant event, these files will be empty.

When IDM sends data to these audit logs, you can [query](querying-audit-over-rest.html) them over the REST interface.

---

---
title: Configure notifications
description: Configure the PingIDM notification service to send messages on object changes, including enabling the service and setting up custom notification files
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:notification-config
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/notification-config.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration", "Notifications"]
section_ids:
  changes_to_the_notification_property_name: Changes to the notification property name
  notification-config-files: Custom notifications
  notification-limits: Limits on notification endpoints
---

# Configure notifications

The customizable notification service sends messages, based on changes to objects. The notification service uses filters to assess incoming requests. If the filter conditions are met, the service sends the corresponding notification. Notification messages are sent to whatever routes you specify.

In a JDBC repository, notifications are stored in the `notificationobjects` table. The `notificationobjectproperties`, serves as the index table. In a DS repository, notifications are stored under the DN `"ou=notification,ou=internal,dc=openidm,dc=forgerock,dc=com"`.

The notification service is disabled by default. To enable the service, add `openidm.notifications=true` to your project's `resolver/boot.properties` file. You can perform additional configuration using the `conf/notificationFactory.json` file.

Default `notificationFactory.json` configuration

```json
{
    "enabled" :{
        "$bool" : "&{openidm.notifications|false}"
    },
    "threadPool" : {
        "steadyPoolThreads" : 1,
        "maxPoolThreads" : 2,
        "threadKeepAlive" : 60,
        "maxQueueSize" : 20000
    }
}
```

|   |                                                                                   |
| - | --------------------------------------------------------------------------------- |
|   | Changing the notifications thread pool settings can adversely affect performance. |

Notifications for a managed object are injected into a property in that object. The name of this property is specified in the managed object schema, in `conf/managed.json`. For example, notifications for managed user objects rely on the following construct in the `user` object definition in `managed.json`:

```json
{
    "objects" : [
        {
            "name" : "user",
            ...
            "notifications" : {
                "property" : "_notifications"
            },
            ...
        },
        ...
    ]
}
```

This excerpt indicates that notifications are injected into the `_notifications` property of the user object by default. The `notifications` object is mandatory for notifications to be generated for that managed object type. However, you can change the name of the property that is injected into the managed object when notifications are generated. If you omit the `property` field from the `notifications` object, notifications are stored in the `_notifications` field by default.

## Changes to the notification property name

The ability to tie a specific notification to its corresponding managed object is regarded as an *internal object relation*. Notifications are therefore also configured in `conf/internal.json` with the following object:

```json
{
    "name" : "notification",
    "properties" : {
        "target" : {
            "reversePropertyName" : "_notifications"
        }
    }
}
```

If you change the `property` field in `managed.json` to something other than `_notifications`, you must also update the corresponding `reversePropertyName` in `internal.json`.

|   |                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The internal object service does not support runtime changes. If you update `conf/internal.json` over REST, you must restart IDM for the change to take effect. |

If you have configured notifications for more than one managed object type, all the object types must use the same notification property name.

## Custom notifications

Notifications are configured in files named `notification-event.json`, where event refers to the event that triggers the notification.

By default, IDM doesn't send any notifications for password or profile updates. To enable these notifications, add the applicable line to your project's `resolver/boot.properties` file:

* `openidm.notifications.passwordUpdate=true`

* `openidm.notifications.profileUpdate=true`

These notifications are configured in the `conf/notification-passwordUpdate.json` and `conf/notification-profileUpdate.json` files, respectively. You can use these default notification configuration files as the basis for setting up custom notifications.

The default `notification-passwordUpdate.json` file shows the structure of a notification configuration:

```json
{
    "enabled" : {
        "$bool" : "&{openidm.notifications.passwordUpdate|false}"
    },
    "path" : "managed/user/*",
    "methods" : [
        "update",
        "patch"
    ],
    "condition" : {
        "type" : "groovy",
        "globals" : {
            "propertiesToCheck" : [
                "password"
            ]
        },
        "file" : "propertiesModifiedFilter.groovy"
    },
    "target" : {
        "resource" : "managed/user/{{response/_id}}"
    },
    "notification" : {
        "notificationType": "info",
        "message": "Your password has been updated."
    }
}
```

* `enabled` boolean, true or false

  Specifies whether notifications will be triggered for that configured event. To enable or disable, set the `openidm.notifications.passwordUpdate` property in the `resolver/boot.properties` file.

* `path` string

  Specifies where the filter listens on the router. For user notifications, this is typically `managed/user/*`.

* `methods` array of strings (optional)

  One or more Ping REST verbs, specifying the actions that should trigger the notification. These can include `create`, `read`, `update`, `delete`, `patch`, `action`, and `query`. If no `methods` are specified, the default is to listen for all methods.

* `condition` string or object

  An inline script or a path to a script `file` that specifies the condition on which the notification is triggered. The `passwordUpdate` notification configuration references the groovy script, `/path/to/openidm/bin/defaults/script/propertiesModifiedFilter.groovy`. This script monitors the properties listed in the `propertiesToCheck` array, and sends a notification when those properties are changed. The script also checks whether a modified property is the child (or parent) of a watched property.

  To specify additional properties to watch, add the property names to the array of `propertiesToCheck`. The properties that you can specify here are limited to existing user properties defined in your `managed.json` file. For example, the following excerpt of the `notification-profileUpdate.json` file shows the properties that will trigger notifications if their values are changed:

  ```json
  ...
      "condition" : {
          "type" : "groovy",
          "globals" : {
              "propertiesToCheck" : [
                  "userName",
                  "givenName",
                  "sn",
                  "mail",
                  "description",
                  "accountStatus",
                  "telephoneNumber",
                  "postalAddress",
                  "city",
                  "postalCode",
                  "country",
                  "stateProvince",
                  "preferences"
              ]
          },
          "file" : "propertiesModifiedFilter.groovy"
      },
  ...
  ```

* `target` object

  The target resource to which notifications are sent, typically `managed/user/{{response/_id}}`.

  The `target.resource` field supports `{{token}}` replacement with contextual variables. The following variables are in scope:

  * `request`

  * `context`

  * `resourceName`

  * `response`

* `notification`

  The actual notification, including the `notificationType` (`info`, `warning`, or `error`) and the `message` that is sent to the user.

  The `notification.message` field supports `{{token}}` replacement with contextual variables, as described previously for `target.resource`.

Notification configuration files follow the format of the `router.json` file. For more information about how filtering is configured in `router.json`, refer to [Router configuration](../scripting-guide/router-config.html).

## Limits on notification endpoints

Although notifications are highly configurable, you cannot apply them to services with their own internal routers, including internal objects. This list includes:

* `workflow/taskinstance`

* `workflow/processdefinition`

* `workflow/processinstance`

* `metrics/api`

* `metrics/prometheus`

* `scheduler/job`

* `scheduler/trigger`

* `scheduler/waitingTriggers`

* `scheduler/acquiredTriggers`

* `info/ping`

* `info/login`

* `info/version`

* `info/uiconfig`

* `info/features`

* `internal/{object}`

* `internal/{object}/{object_id}/relationship`

* `managed/{object}/{object_id}/relationship`

---

---
title: Configure the audit service
description: Configure the PingIDM audit service by editing `audit.json` or using the admin UI to set up audit event handlers, event logging, and query options
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:configure-audit-service
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/configure-audit-service.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration", "Handlers", "Options"]
---

# Configure the audit service

You access the audit logging configuration over REST at the `openidm/config/audit` context path and in the `conf/audit.json` file. To configure the audit service, edit the `audit.json` file or use the admin UI. Select Configure > System Preferences, and click the Audit tab. The fields on that form correspond to the configuration parameters described in this section.

You can configure the following major options for the audit service:

* Which audit handlers are used

  [Audit event handlers](configuring-topic-handlers.html) are responsible for handling audit events. They are listed in the `availableAuditEventHandlers` property in your `conf/audit.json` file.

* Which handler is used for queries

  You *must* configure one audit event handler to manage [queries](audit-queries.html) on the audit logs.

* What events are logged

  The [events](audit-log-topics.html) that are logged are configured in the `events` list for each audit event handler.

* Track transactions across products

  If you use more than one Ping product, you can specify that a common `transactionId` be used to track audit data across products. Edit your `conf/system.properties` file and set:

  ```
  org.forgerock.http.TrustTransactionHeader=true
  ```

---

---
title: CSV audit event handler properties
description: Reference for the CSV audit event handler properties in PingIDM, including file rotation, retention, formatting, and buffering configuration
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:audit-config-prop-csv
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/audit-config-prop-csv.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration", "CSV", "Event", "Handlers", "Properties"]
---

# CSV audit event handler properties

| UI Label / Text                    | audit.json File Label            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| File Rotation                      | `fileRotation`                   | Groups the file rotation configuration parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| rotationEnabled                    | `rotationEnabled`                | Specifies whether file rotation is enabled. Boolean: true, or false.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| maxFileSize                        | `maxFileSize`                    | The maximum size of an audit file, in bytes, before rotation is triggered.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| rotationFilePrefix                 | `rotationFilePrefix`             | The prefix to add to the start of an audit file name when it is rotated.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Rotation Times                     | `rotationTimes`                  | Specifies a list of times when file rotation should be triggered.The times must be provided as durations, offset from midnight. For example, a list of `10 minutes, 20 minutes, 30 minutes` will cause files to rotate at 10, 20 and 30 minutes after midnight.                                                                                                                                                                                                                                                      |
| File Rotation Suffix               | `rotationFileSuffix`             | The suffix appended to rotated audit file names. This suffix should take the form of a timestamp, in simple date format. The default suffix format, if none is specified, is `-yyyy.MM.dd-HH.mm.ss`.                                                                                                                                                                                                                                                                                                                 |
| Rotation Interval                  | `rotationInterval`               | The interval to trigger a file rotation, expressed as a duration. For example, `5 seconds`, `5 minutes`, `5 hours`. A value of `0` or `disabled` disables time-based file rotation. Note that you can specify a list of `rotationTimes` and a `rotationInterval`. The audit event handler checks all rotation and retention policies on a periodic basis, and assesses whether each policy should be triggered at the current time, for a particular audit file. The first policy to meet the criteria is triggered. |
| File Retention                     | `fileRetention`                  | Groups the file retention configuration parameters. The retention policy specifies how long audit files remain on disk before they are automatically deleted.                                                                                                                                                                                                                                                                                                                                                        |
| Maximum Number of Historical Files | `maxNumberOfHistoryFiles`        | The maximum number of historical audit files that can be stored. If the total number of audit files exceeds this maximum, older files are deleted.A value of `-1` disables purging of old log files.                                                                                                                                                                                                                                                                                                                 |
| Maximum Disk Space                 | `maxDiskSpaceToUse`              | The maximum disk space, in bytes, that can be used for audit files. If the total space occupied by the audit files exceeds this maximum, older files are deleted. A negative or zero value indicates that this policy is disabled; that is, that unlimited disk space can be used for historical audit files.                                                                                                                                                                                                        |
| Minimum Free Space Required        | `minFreeSpaceRequired`           | The minimum free disk space, in bytes, required on the system that houses the audit files. If the free space drops below this minimum, older files are deleted. A negative or zero value indicates that this policy is disabled; that is, that no minimum space requirements apply.                                                                                                                                                                                                                                  |
| rotationRetentionCheckInterval     | `rotationRetentionCheckInterval` | Interval for periodically checking file rotation and retention policies.The interval must be a duration; for example, `5 seconds`, `5 minutes`, or `5 hours`.                                                                                                                                                                                                                                                                                                                                                        |
| Log Directory                      | `logDirectory`                   | Directory with CSV audit files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| CSV Output Formatting              | `formatting`                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| quoteChar                          | `quoteChar`                      | Formatting: Character used around a CSV field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| delimiterChar                      | `delimiterChar`                  | Formatting: Character between CSV fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| End of Line Symbols                | `endOfLineSymbols`               | Formatting: end of line symbol, such as `\n` or `\r`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Buffering                          | `buffering`                      | Configuration for optional event buffering.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| enabled                            | `enabled`                        | Buffering: true, or false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| autoFlush                          | `autoFlush`                      | Buffering: avoids flushing after each event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

---

---
title: Filter audit data
description: Configure PingIDM audit event filtering by action, field value, script, or trigger using the filter parameter in `conf/audit.json`
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:filtering-audit-events
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/filtering-audit-events.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration", "Filters", "Policies"]
section_ids:
  filtering-by-action: Filter by action
  filtering-by-field: Filter by field value
  audit-filter-scripts: Filter with a script
  filtering-by-trigger: Filter by trigger
---

# Filter audit data

The audit configuration (in `conf/audit.json`) includes a `filter` parameter that lets you specify what should be logged, per event topic. The information that is logged can be filtered in various ways.

The following excerpt of a sample `audit.json` file shows the filter element for the activity log:

```json
"eventTopics" : {
    "authentication" : { },
    "access" : { },
    "activity" : {
        "filter" : {
            "actions" : [
                "create",
                "update",
                "delete",
                "patch",
                "action"
            ]
        },
  ...
}
```

To configure audit filtering in the admin UI, select Configure > System Preferences > Audit. Scroll down to Event Topics, and click the pencil icon next to the event that you want to filter. The filter tabs, Filter Actions, Filter Fields, Filter Script, and Filter Triggers, correspond to the filtering capabilities discussed here.

## Filter by action

The `filter` `actions` list enables you to specify the actions that are logged, per event type. This filter is essentially a `fields` filter (as described in [Filter by Field Value](audit.html#filtering-by-field)) that filters log entries by the value of their `actions` field.

The following configuration specifies that the actions create, update, delete, patch, and action should be included in the log, for the activity audit event topic.

```none
"eventTopics" : {
...
    "activity": {
        "filter" : {
            "actions" : [
                "create",
                "update",
                "delete",
                "patch",
                "action"
            ]
        },
        ...
    }
}
```

The list of actions that can be filtered into the log depend on the event type. The following table lists the actions that can be filtered, per event type.

**Actions that can be Filtered Per Event Type**

| Event Type                         | Actions     | Description                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Activity and Configuration         | `read`      | When an object is read by using its identifier. By default, read actions are not logged.Note that due to the potential result size in the case of read operations on `system/` endpoints, only the read is logged, and not the resource detail. If you really need to log the complete resource detail, set the following property in your `resolver/boot.properties` file:```none
openidm.audit.logFullObjects=true
``` |
|                                    | `create`    | When an object is created.                                                                                                                                                                                                                                                                                                                                                                                               |
|                                    | `update`    | When an object is updated.                                                                                                                                                                                                                                                                                                                                                                                               |
|                                    | `delete`    | When an object is deleted.                                                                                                                                                                                                                                                                                                                                                                                               |
|                                    | `patch`     | When an object is partially modified. (Activity only.)                                                                                                                                                                                                                                                                                                                                                                   |
|                                    | `query`     | When a query is performed on an object. By default, query actions are not logged.Note that, due to the potential result size in the case of query operations on `system/` endpoints, only the query is logged, and not the resource detail. If you really need to log the complete resource detail, add the following line to your `resolver/boot.properties` file:```none
openidm.audit.logFullObjects=true
```         |
|                                    | `action`    | When an action is performed on an object. (Activity only.)                                                                                                                                                                                                                                                                                                                                                               |
| Reconciliation and Synchronization | `create`    | When a target object is created.                                                                                                                                                                                                                                                                                                                                                                                         |
|                                    | `delete`    | When a target object is deleted.                                                                                                                                                                                                                                                                                                                                                                                         |
|                                    | `update`    | When a target object is updated.                                                                                                                                                                                                                                                                                                                                                                                         |
|                                    | `link`      | When a link is created between a source object and an existing target object.                                                                                                                                                                                                                                                                                                                                            |
|                                    | `unlink`    | When a link is removed between a source object and a target object.                                                                                                                                                                                                                                                                                                                                                      |
|                                    | `exception` | When the synchronization situation results in an exception. For more information, refer to [Synchronization situations and actions](../synchronization-guide/chap-situations-actions.html).                                                                                                                                                                                                                              |
|                                    | `ignore`    | When the target object is ignored; that is, no action is taken.                                                                                                                                                                                                                                                                                                                                                          |
| Authentication and Access          | `-`         | No actions can be specified for the authentication or the access log event type.                                                                                                                                                                                                                                                                                                                                         |

## Filter by field value

You can add a list of `filter` `fields` to the audit configuration, that lets you filter log entries by specific fields. For example, you might want to restrict the reconciliation or audit log so that only summary information is logged for each reconciliation operation. The following addition to the `audit.json` file specifies that entries are logged in the reconciliation log only if their `entryType` is `start` or `summary`.

```json
"eventTopics" : {
    ...
    "activity" : {
        "filter" : {
            "actions" : [
                "create",
                "update",
                "delete",
                "patch",
                "action
            ],
            "fields" : [
                {
                    "name" : "entryType",
                    "values" : [
                        "start",
                        "summary"
                    ]
                }
            ]
        }
    }
    ...
},
...
```

To use nested properties, specify the field name as a JSON pointer. For example, to filter entries according to the value of the `authentication.id`, you would specify the field name as `authentication/id`.

## Filter with a script

Apart from the audit filtering options described in the previous sections, you can use a JavaScript or Groovy script to filter what is logged. Audit filter scripts are referenced in the audit configuration file (`conf/audit.json`), and can be configured per event type. The following sample configuration references a script named `auditfilter.js`, which is used to limit what is logged in the reconciliation audit log:

```json
{
    "eventTopics" : {
        ...
        "recon" : {
            "filter" : {
                "script" : {
                    "type" : "text/javascript",
                    "file" : "auditfilter.js"
                }
            }
        },
        ...
}
```

The `request` and `context` objects are available to the script. Before writing the audit entry, IDM can access the entry as a `request.content` object. For example, to set up a script to log just the summary entries for mapping managed users in an LDAP data store, you could include the following in the `auditfilter.js` script:

```javascript
(function() {
    return request.content.entryType == 'summary' &&
    request.content.mapping == 'systemLdapAccounts_managedUser'
}());
```

The script must return `true` to include the log entry; `false` to exclude it.

## Filter by trigger

You can add a ``filter`triggers list to the audit configuration, that specifies the actions that will be logged for a specific trigger. For example, the following addition to the audit.json file specifies that only `create`` and `update` actions are logged for in the activity log, for an activity that was triggered by a `recon`.

```json
"eventTopics" : {
    "activity" : {
        "filter" : {
            "actions" : [
            ...
            ],
            "triggers" : {
                "recon" : [
                    "create",
                    "update"
                ]
            }
    ...
```

If a trigger is provided, but no actions are specified, nothing is logged for that trigger. If a trigger is omitted, all actions are logged for that trigger. Only the `recon` trigger is implemented. For a list of reconciliation actions that can be logged, refer to [Synchronization Actions](../synchronization-guide/chap-situations-actions.html#sync-actions).

---

---
title: JMS audit event handler properties
description: (Deprecated; use JSON audit event handler) Configuration properties reference for the JMS audit event handler in PingIDM
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:audit-config-prop-jms
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/audit-config-prop-jms.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration", "JMS", "Event", "Handlers", "Properties"]
---

# JMS audit event handler properties

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [JMS](configuring-topic-handlers.html#audit-jms-handler), [Repository](configuring-topic-handlers.html#audit-repo-handler), [Router](configuring-topic-handlers.html#audit-router-handler), and [Syslog](configuring-topic-handlers.html#audit-syslog-handler) audit event handlers are [deprecated](../release-notes/deprecated-functionality.html#deprecation-audit-event-handlers) and will be removed in a future release of IDM. Use the [JSON audit event handler](configuring-topic-handlers.html#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack). |

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The JMS audit handler `config` in `audit.json` includes the IDM audit event topics *and* JMS audit topics. |

To use the JMS resources provided by your web application container, leave the `JNDI Context Properties` settings empty. Values for `topicName` and `connectionFactoryName` will then depend on the configuration of your web application container.

| UI Label / Text              | audit.json File Label         | Description                                                                                                    |
| ---------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Delivery Mode                | `deliveryMode`                | Required property, for messages from a JMS provider; may be `PERSISTENT` or `NON_PERSISTENT`                   |
| Session Mode                 | `sessionMode`                 | Acknowledgement mode, in sessions without transactions. May be `AUTO`, `CLIENT`, or `DUPS_OK`.                 |
| Batch Configuration Settings | `batch`                       | Options for batch messaging.                                                                                   |
| Write Interval               | `writeInterval`               | Interval at which buffered events are written to JMS (units of 'ms' or 's' are recommended). Default is 10 ms. |
| Capacity                     | `capacity`                    | Maximum event count in the batch queue; additional events are dropped.                                         |
| Maximum Batched Events       | `maxBatchedEvents`            | Maximum number of events per batch.                                                                            |
| JNDI Configuration           | `jndiConfiguration`           | Java Naming and Directory Interface (JNDI) Configuration Settings.                                             |
| JNDI Context Properties      | `contextProperties`           | Settings to populate the JNDI initial context with.                                                            |
| JNDI Context Factory         | `java.naming.factory.initial` | Initial JNDI context factory, such as `com.tibco.tibjms.naming.TibjmsInitialContextFactory`.                   |
| JNDI Provider URL            | `java.naming.provider.url`    | Depends on provider; options include `tcp://localhost:61616` and `tibjmsnaming://192.168.1.133:7222`.          |
| JNDI Topic                   | `topic.forgerock.idm.audit`   | Relevant JNDI topic; default=`forgerock.idm.audit`.                                                            |
| JNDI Topic Name              | `topicName`                   | JNDI lookup name for the JMS topic.                                                                            |
| Connection Factory           | `connectionFactoryName`       | JNDI lookup name for the JMS connection factory.                                                               |

---

---
title: JSON audit event handler properties
description: Reference for JSON audit event handler properties in PingIDM, including file rotation, retention, buffering, and Elasticsearch compatibility settings
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:audit-config-prop-json
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/audit-config-prop-json.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration", "JSON", "Event", "Handlers", "Properties"]
---

# JSON audit event handler properties

| Property                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `fileRotation`                   | Groups the file rotation configuration parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `rotationEnabled`                | Specifies whether file rotation is enabled. Boolean: true, or false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `maxFileSize`                    | The maximum size of an audit file, in bytes, before rotation is triggered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `rotationFilePrefix`             | The prefix to add to the start of an audit file name when it is rotated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `rotationTimes`                  | Specifies a list of times when file rotation should be triggered. The times must be provided as durations, offset from midnight. For example, a list of `10 minutes, 20 minutes, 30 minutes` will cause files to rotate at 10, 20 and 30 minutes after midnight.                                                                                                                                                                                                                                                                                               |
| `rotationFileSuffix`             | The suffix appended to rotated audit file names. This suffix should take the form of a timestamp, in simple date format. The default suffix format, if none is specified, is `-yyyy.MM.dd-HH.mm.ss`.                                                                                                                                                                                                                                                                                                                                                           |
| `rotationInterval`               | The interval to trigger a file rotation, expressed as a duration. For example, `5 seconds`, `5 minutes`, `5 hours`. A value of `0` or `disabled` disables time-based file rotation. Note that you can specify a list of `rotationTimes` and a `rotationInterval`. The audit event handler checks all rotation and retention policies on a periodic basis, and assesses whether each policy should be triggered at the current time, for a particular audit file. The first policy to meet the criteria is triggered.                                           |
| `fileRetention`                  | Groups the file retention configuration parameters. The retention policy specifies how long audit files remain on disk before they are automatically deleted.                                                                                                                                                                                                                                                                                                                                                                                                  |
| `maxNumberOfHistoryFiles`        | The maximum number of historical audit files that can be stored. If the total number of audit files exceeds this maximum, older files are deleted.A value of `-1` disables purging of old log files.                                                                                                                                                                                                                                                                                                                                                           |
| `maxDiskSpaceToUse`              | The maximum disk space, in bytes, that can be used for audit files. If the total space occupied by the audit files exceeds this maximum, older files are deleted. A negative or zero value indicates that this policy is disabled; that is, that unlimited disk space can be used for historical audit files.                                                                                                                                                                                                                                                  |
| `minFreeSpaceRequired`           | The minimum free disk space, in bytes, required on the system that houses the audit files. If the free space drops below this minimum, older files are deleted. A negative or zero value indicates that this policy is disabled; that is, that no minimum space requirements apply.                                                                                                                                                                                                                                                                            |
| `rotationRetentionCheckInterval` | Interval for periodically checking file rotation and retention policies.The interval must be a duration; for example, `5 seconds`, `5 minutes`, or `5 hours`.                                                                                                                                                                                                                                                                                                                                                                                                  |
| `logDirectory`                   | Directory with JSON audit files                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `elasticsearchCompatible`        | Enable ElasticSearch JSON format compatibility. Boolean, true or false. Set this property to `true`, for example, if you are using Logstash to feed into ElasticSearch. When `elasticsearchCompatible` is `true`, the handler renames the `_id` field to `_eventId` because `_id` is reserved by ElasticSearch. The rename is reversed after JSON serialization, so that other handlers can safely use the original field name. For more information, refer to the [ElasticSearch](https://www.elastic.co/guide/en/logstash/current/index.html) documentation. |
| `buffering`                      | Configuration for event buffering.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `maxSize`                        | The maximum number of events that can be buffered (default/minimum: 100000).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `writeInterval`                  | The delay after which the file-writer thread is scheduled to run after encountering an empty event buffer (units of 'ms' are recommended).Default: 100 ms.                                                                                                                                                                                                                                                                                                                                                                                                     |

---

---
title: Log file retention
description: Configure how long PingIDM audit log files are retained on disk before automatic deletion using the `fileRetention` properties in `audit.json`
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:audit-log-file-retention
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/audit-log-file-retention.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Configuration", "Retention"]
---

# Log file retention

Log file retention specifies how long audit files remain on disk before they are automatically deleted.

To configure log file retention, set the following properties in your project's `audit.json` file:

```json
"fileRetention" : {
    "maxNumberOfHistoryFiles" : 100,
    "maxDiskSpaceToUse" : 1000,
    "minFreeSpaceRequired" : 10
},
```

The file retention properties are described in [JSON Audit Event Handler Properties](audit-config-prop-json.html).

To configure log file retention in the admin UI, click Configure > System Preferences > Audit, and edit the JSON audit event handler (or the CSV audit event handler if you are logging to CSV). You can set all the log retention properties on this screen.
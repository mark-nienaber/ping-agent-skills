---
title: Audit logs
description: (Deprecated; use JSON audit event handler) REST endpoints for querying and writing PingIDM audit logs, covering reconciliation, sync, activity, access, and authentication topics
component: pingidm
version: 8.1
page_id: pingidm:rest-api-reference:endpoints/rest-audit-logs
canonical_url: https://docs.pingidentity.com/pingidm/8.1/rest-api-reference/endpoints/rest-audit-logs.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "logs"]
---

# Audit logs

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Query and read operations on the `/audit` API endpoint are [deprecated](../../release-notes/deprecated-functionality.html#deprecation-read-query-audit-endpoint) and will be removed in a future release of IDM. Use the [JSON audit event handler](../../audit-guide/configuring-topic-handlers.html#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack). |

You can interact with the audit logs over REST, as shown in the following table. Queries on the audit endpoint must use `queryFilter` syntax.

| URI                                                                                   | HTTP Operation | Description                                                                       |
| ------------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------- |
| /openidm/audit/recon?\_queryFilter=true                                               | GET            | Displays the reconciliation audit log.                                            |
| /openidm/audit/recon/id                                                               | GET            | Reads a specific reconciliation audit log entry.                                  |
| /openidm/audit/recon/id                                                               | PUT            | Creates a reconciliation audit log entry.                                         |
| /openidm/audit/recon?\_queryFilter=/reconId+eq+"reconId"                              | GET            | Queries the audit log for a particular reconciliation operation.                  |
| /openidm/audit/recon?\_queryFilter=/reconId+eq+"reconId"+and+situation+eq+"situation" | GET            | Queries the reconciliation audit log for a specific reconciliation situation.     |
| /openidm/audit/sync?\_queryFilter=true                                                | GET            | Displays the synchronization audit log.                                           |
| /openidm/audit/sync/id                                                                | GET            | Reads a specific synchronization audit log entry.                                 |
| /openidm/audit/sync/id                                                                | PUT            | Creates a synchronization audit log entry.                                        |
| /openidm/audit/activity?\_queryFilter=true                                            | GET            | Displays the activity log.                                                        |
| /openidm/audit/activity/id                                                            | GET            | Returns activity information for a specific action.                               |
| /openidm/audit/activity/id                                                            | PUT            | Creates an activity audit log entry.                                              |
| /openidm/audit/activity?\_queryFilter=transactionId=id                                | GET            | Queries the activity log for all actions resulting from a specific transaction.   |
| /openidm/audit/access?\_queryFilter=true                                              | GET            | Displays the full list of auditable actions.                                      |
| /openidm/audit/access/id                                                              | GET            | Displays information on the specific audit item.                                  |
| /openidm/audit/access/id                                                              | PUT            | Creates an access audit log entry.                                                |
| /openidm/audit/authentication?\_queryFilter=true                                      | GET            | Displays a complete list of authentication attempts, successful and unsuccessful. |
| /openidm/audit/authentication?\_queryFilter=/principal+eq+"principal"                 | GET            | Displays the authentication attempts by a specified user.                         |
| /openidm/audit?\_action=availableHandlers                                             | POST           | Returns a list of audit event handlers.                                           |
| openidm/audit/config?\_queryFilter=true                                               | GET            | Lists changes made to the configuration.                                          |

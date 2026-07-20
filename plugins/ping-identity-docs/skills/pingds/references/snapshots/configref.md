---
title: About this reference
description: This reference describes server configuration settings that you can view and edit with the dsconfig command. The dsconfig command is the primary tool for managing the server configuration, which follows an object-oriented configuration model. Each configuration object has its own properties. Configuration objects can be related to each other by inheritance and by reference.
component: pingds
version: 8.1
page_id: pingds:configref:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
---

# About this reference

This reference describes server configuration settings that you can view and edit with the `dsconfig` command. The `dsconfig` command is the primary tool for managing the server configuration, which follows an object-oriented configuration model. Each configuration object has its own properties. Configuration objects can be related to each other by inheritance and by reference.

The server configuration model exposes a wide range of configurable features. As a consequence, the `dsconfig` command has many subcommands.

Subcommands exist to create, list, and delete configuration objects, and to get and set properties of configuration objects. Their names reflect these five actions:

* `create-`*object*

* `list-`*objects*

* `delete-`*object*

* `get-`*object*`-prop`

* `set-`*object*`-prop`

Each configuration *object* has a user-friendly name, such as `Connection Handler`. Subcommand names use lower-case, hyphenated versions of the friendly names, as in `create-connection-handler`.

---

---
title: Access Control Handler
description: This is an abstract object type that cannot be instantiated.
component: pingds
version: 8.1
page_id: pingds:configref:objects-access-control-handler
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-access-control-handler.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  access_control_handlers: Access Control Handlers
  access_control_handler_properties: Access Control Handler properties
  basic_properties: Basic properties
  enabled: enabled
  java-class: java-class
---

# Access Control Handler

*This is an abstract object type that cannot be instantiated.*

Access Control Handlers manage the application-wide access control. The PingDS access control handler is defined through an extensible interface, so that alternate implementations can be created. Only one access control handler may be active in the server at any given time.

Note that PingDS also has a privilege subsystem, which may have an impact on what clients may be allowed to do in the server. For example, any user with the bypass-acl privilege is not subject to access control checking regardless of whether the access control implementation is enabled.

## Access Control Handlers

The following Access Control Handlers are available:

* [DSEE Compatible Access Control Handler](objects-dsee-compat-access-control-handler.html)

* [Policy Based Access Control Handler](objects-policy-based-access-control-handler.html)

These Access Control Handlers inherit the properties described below.

## Access Control Handler properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                              |
| --------------------------------------------- |
| [enabled](#enabled) [java-class](#java-class) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### enabled

|                         |                                                                                                                                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Indicates whether the Access Control Handler is enabled. If set to FALSE, then any client (including unauthenticated or anonymous clients) is allowed to bind to the server and any connection with the "bypass-acl" privilege is allowed to perform any operation. |
| *Default value*         | None                                                                                                                                                                                                                                                                |
| *Allowed values*        | truefalse                                                                                                                                                                                                                                                           |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                  |
| *Required*              | Yes                                                                                                                                                                                                                                                                 |
| *Admin action required* | None                                                                                                                                                                                                                                                                |
| *Advanced*              | No                                                                                                                                                                                                                                                                  |
| *Read-only*             | No                                                                                                                                                                                                                                                                  |

### java-class

|                         |                                                                                                               |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the fully-qualified name of the Java class that provides the Access Control Handler implementation. |
| *Default value*         | None                                                                                                          |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.AccessControlHandler                          |
| *Multi-valued*          | No                                                                                                            |
| *Required*              | Yes                                                                                                           |
| *Admin action required* | The object must be disabled and re-enabled for changes to take effect.                                        |
| *Advanced*              | No                                                                                                            |
| *Read-only*             | No                                                                                                            |

---

---
title: Access Log Filtering Criteria
description: A set of rules which determine whether a log record should be logged or not. All the specified rules must match for this overall filtering criteria to match.
component: pingds
version: 8.1
page_id: pingds:configref:objects-access-log-filtering-criteria
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-access-log-filtering-criteria.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  dependencies: Dependencies
  access_log_filtering_criteria_properties: Access Log Filtering Criteria properties
  basic_properties: Basic properties
  connection-client-address-equal-to: connection-client-address-equal-to
  connection-client-address-not-equal-to: connection-client-address-not-equal-to
  connection-port-equal-to: connection-port-equal-to
  connection-protocol-equal-to: connection-protocol-equal-to
  log-record-type: log-record-type
  request-target-dn-equal-to: request-target-dn-equal-to
  request-target-dn-not-equal-to: request-target-dn-not-equal-to
  response-entry-size-greater-than: response-entry-size-greater-than
  response-etime-greater-than: response-etime-greater-than
  response-etime-less-than: response-etime-less-than
  response-etime-processing-greater-than: response-etime-processing-greater-than
  response-etime-processing-less-than: response-etime-processing-less-than
  response-etime-queueing-greater-than: response-etime-queueing-greater-than
  response-etime-queueing-less-than: response-etime-queueing-less-than
  response-result-code-equal-to: response-result-code-equal-to
  response-result-code-not-equal-to: response-result-code-not-equal-to
  search-response-is-indexed: search-response-is-indexed
  search-response-nentries-greater-than: search-response-nentries-greater-than
  search-response-nentries-less-than: search-response-nentries-less-than
  user-dn-equal-to: user-dn-equal-to
  user-dn-not-equal-to: user-dn-not-equal-to
  user-is-member-of: user-is-member-of
  user-is-not-member-of: user-is-not-member-of
---

# Access Log Filtering Criteria

A set of rules which determine whether a log record should be logged or not. All the specified rules must match for this overall filtering criteria to match.

## Dependencies

The following objects depend on Access Log Filtering Criteria:

* [Access Log Publisher](objects-access-log-publisher.html)

## Access Log Filtering Criteria properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [connection-client-address-equal-to](#connection-client-address-equal-to) [connection-client-address-not-equal-to](#connection-client-address-not-equal-to) [connection-port-equal-to](#connection-port-equal-to) [connection-protocol-equal-to](#connection-protocol-equal-to) [log-record-type](#log-record-type) [request-target-dn-equal-to](#request-target-dn-equal-to) [request-target-dn-not-equal-to](#request-target-dn-not-equal-to) [response-entry-size-greater-than](#response-entry-size-greater-than) [response-etime-greater-than](#response-etime-greater-than) [response-etime-less-than](#response-etime-less-than) [response-etime-processing-greater-than](#response-etime-processing-greater-than) [response-etime-processing-less-than](#response-etime-processing-less-than) [response-etime-queueing-greater-than](#response-etime-queueing-greater-than) [response-etime-queueing-less-than](#response-etime-queueing-less-than) [response-result-code-equal-to](#response-result-code-equal-to) [response-result-code-not-equal-to](#response-result-code-not-equal-to) [search-response-is-indexed](#search-response-is-indexed) [search-response-nentries-greater-than](#search-response-nentries-greater-than) [search-response-nentries-less-than](#search-response-nentries-less-than) [user-dn-equal-to](#user-dn-equal-to) [user-dn-not-equal-to](#user-dn-not-equal-to) [user-is-member-of](#user-is-member-of) [user-is-not-member-of](#user-is-not-member-of) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### connection-client-address-equal-to

|                         |                                                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| *Synopsis*              | Filters log records associated with connections which match at least one of the specified client host names or address masks.        |
| *Description*           | Valid values include a host name, a fully qualified domain name, a domain name, an IP address, or a subnetwork with subnetwork mask. |
| *Default value*         | None                                                                                                                                 |
| *Allowed values*        | An IP address mask.                                                                                                                  |
| *Multi-valued*          | Yes                                                                                                                                  |
| *Required*              | No                                                                                                                                   |
| *Admin action required* | None                                                                                                                                 |
| *Advanced*              | No                                                                                                                                   |
| *Read-only*             | No                                                                                                                                   |

### connection-client-address-not-equal-to

|                         |                                                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| *Synopsis*              | Filters log records associated with connections which do not match any of the specified client host names or address masks.          |
| *Description*           | Valid values include a host name, a fully qualified domain name, a domain name, an IP address, or a subnetwork with subnetwork mask. |
| *Default value*         | None                                                                                                                                 |
| *Allowed values*        | An IP address mask.                                                                                                                  |
| *Multi-valued*          | Yes                                                                                                                                  |
| *Required*              | No                                                                                                                                   |
| *Admin action required* | None                                                                                                                                 |
| *Advanced*              | No                                                                                                                                   |
| *Read-only*             | No                                                                                                                                   |

### connection-port-equal-to

|                         |                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters log records associated with connections to any of the specified listener port numbers. |
| *Default value*         | None                                                                                           |
| *Allowed values*        | An integer.Lower limit: 1.Upper limit: 65535.                                                  |
| *Multi-valued*          | Yes                                                                                            |
| *Required*              | No                                                                                             |
| *Admin action required* | None                                                                                           |
| *Advanced*              | No                                                                                             |
| *Read-only*             | No                                                                                             |

### connection-protocol-equal-to

|                         |                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters log records associated with connections which match any of the specified protocols. |
| *Description*           | Typical values include "ldap", or "ldaps".                                                  |
| *Default value*         | None                                                                                        |
| *Allowed values*        | The protocol name as reported in the access log.                                            |
| *Multi-valued*          | Yes                                                                                         |
| *Required*              | No                                                                                          |
| *Admin action required* | None                                                                                        |
| *Advanced*              | No                                                                                          |
| *Read-only*             | No                                                                                          |

### log-record-type

|                         |                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters log records based on their type.                                                                                                                                                                                                                                                                                                                                                  |
| *Default value*         | None                                                                                                                                                                                                                                                                                                                                                                                      |
| *Allowed values*        | * abandon: Abandon operations

* add: Add operations

* bind: Bind operations

* compare: Compare operations

* connect: Client connections

* delete: Delete operations

* disconnect: Client disconnections

* extended: Extended operations

* modify: Modify operations

* rename: Rename operations

* search: Search operations

* tls: TLS handshakes

* unbind: Unbind operations |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                                                                                                                                                       |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                        |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                                                                      |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                        |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                        |

### request-target-dn-equal-to

|                         |                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters operation log records associated with operations which target entries matching at least one of the specified DN patterns.                                                                                                                                                                                                                                                                  |
| *Description*           | Valid DN filters are strings composed of zero or more wildcards. A double wildcard \*\* replaces one or more RDN components (as in uid=dmiller,\*\*,dc=example,dc=com). A simple wildcard \* replaces either a whole RDN, or a whole type, or a value substring (as in uid=bj\*,ou=people,dc=example,dc=com). To match the root DN, use two double quote characters with no space in between (""). |
| *Default value*         | None                                                                                                                                                                                                                                                                                                                                                                                               |
| *Allowed values*        | A string.                                                                                                                                                                                                                                                                                                                                                                                          |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                                                                                                                                                                |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                                                                               |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                 |

### request-target-dn-not-equal-to

|                         |                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters operation log records associated with operations which target entries matching none of the specified DN patterns.                                                                                                                                                                                                                                                                          |
| *Description*           | Valid DN filters are strings composed of zero or more wildcards. A double wildcard \*\* replaces one or more RDN components (as in uid=dmiller,\*\*,dc=example,dc=com). A simple wildcard \* replaces either a whole RDN, or a whole type, or a value substring (as in uid=bj\*,ou=people,dc=example,dc=com). To match the root DN, use two double quote characters with no space in between (""). |
| *Default value*         | None                                                                                                                                                                                                                                                                                                                                                                                               |
| *Allowed values*        | A string.                                                                                                                                                                                                                                                                                                                                                                                          |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                                                                                                                                                                |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                                                                               |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                 |

### response-entry-size-greater-than

|                         |                                                                                                                                                                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters operation response log records associated with operations which target one or more entries whose encoded size is bigger than the specified size.                                                                                           |
| *Description*           | Frequent operations on large entries may impact performance. It is recommended to only use this criteria in conjunction with the "combined" output mode of the access logger, since this filter criteria is only applied to response log messages. |
| *Default value*         | 0 KB                                                                                                                                                                                                                                               |
| *Allowed values*        | Uses [size syntax](size-syntax.html).                                                                                                                                                                                                              |
| *Multi-valued*          | No                                                                                                                                                                                                                                                 |
| *Required*              | No                                                                                                                                                                                                                                                 |
| *Admin action required* | None                                                                                                                                                                                                                                               |
| *Advanced*              | No                                                                                                                                                                                                                                                 |
| *Read-only*             | No                                                                                                                                                                                                                                                 |

### response-etime-greater-than

|                         |                                                                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters operation response log records associated with operations whose total response time, including queuing and processing time, took longer than the specified number of milli-seconds to complete. |
| *Description*           | It is recommended to only use this criteria in conjunction with the "combined" output mode of the access logger, since this filter criteria is only applied to response log messages.                   |
| *Default value*         | None                                                                                                                                                                                                    |
| *Allowed values*        | An integer.Lower limit: 0.                                                                                                                                                                              |
| *Multi-valued*          | No                                                                                                                                                                                                      |
| *Required*              | No                                                                                                                                                                                                      |
| *Admin action required* | None                                                                                                                                                                                                    |
| *Advanced*              | No                                                                                                                                                                                                      |
| *Read-only*             | No                                                                                                                                                                                                      |

### response-etime-less-than

|                         |                                                                                                                                                                                                       |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters operation response log records associated with operations whose total response time, including queuing and processing time, took less than the specified number of milli-seconds to complete. |
| *Description*           | It is recommended to only use this criteria in conjunction with the "combined" output mode of the access logger, since this filter criteria is only applied to response log messages.                 |
| *Default value*         | None                                                                                                                                                                                                  |
| *Allowed values*        | An integer.Lower limit: 0.                                                                                                                                                                            |
| *Multi-valued*          | No                                                                                                                                                                                                    |
| *Required*              | No                                                                                                                                                                                                    |
| *Admin action required* | None                                                                                                                                                                                                  |
| *Advanced*              | No                                                                                                                                                                                                    |
| *Read-only*             | No                                                                                                                                                                                                    |

### response-etime-processing-greater-than

|                         |                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters operation response log records associated with operations whose processing time was greater than the specified number of milli-seconds.                                       |
| *Description*           | It is recommended to only use this criteria in conjunction with the "combined" output mode of the access logger, since this filter criteria is only applied to response log messages. |
| *Default value*         | None                                                                                                                                                                                  |
| *Allowed values*        | An integer.Lower limit: 0.                                                                                                                                                            |
| *Multi-valued*          | No                                                                                                                                                                                    |
| *Required*              | No                                                                                                                                                                                    |
| *Admin action required* | None                                                                                                                                                                                  |
| *Advanced*              | No                                                                                                                                                                                    |
| *Read-only*             | No                                                                                                                                                                                    |

### response-etime-processing-less-than

|                         |                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters operation response log records associated with operations whose processing time was less than the specified number of milli-seconds.                                          |
| *Description*           | It is recommended to only use this criteria in conjunction with the "combined" output mode of the access logger, since this filter criteria is only applied to response log messages. |
| *Default value*         | None                                                                                                                                                                                  |
| *Allowed values*        | An integer.Lower limit: 0.                                                                                                                                                            |
| *Multi-valued*          | No                                                                                                                                                                                    |
| *Required*              | No                                                                                                                                                                                    |
| *Admin action required* | None                                                                                                                                                                                  |
| *Advanced*              | No                                                                                                                                                                                    |
| *Read-only*             | No                                                                                                                                                                                    |

### response-etime-queueing-greater-than

|                         |                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters operation response log records associated with operations whose queuing time was greater than the specified number of milli-seconds.                                          |
| *Description*           | It is recommended to only use this criteria in conjunction with the "combined" output mode of the access logger, since this filter criteria is only applied to response log messages. |
| *Default value*         | None                                                                                                                                                                                  |
| *Allowed values*        | An integer.Lower limit: 0.                                                                                                                                                            |
| *Multi-valued*          | No                                                                                                                                                                                    |
| *Required*              | No                                                                                                                                                                                    |
| *Admin action required* | None                                                                                                                                                                                  |
| *Advanced*              | No                                                                                                                                                                                    |
| *Read-only*             | No                                                                                                                                                                                    |

### response-etime-queueing-less-than

|                         |                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters operation response log records associated with operations whose queuing time was less than the specified number of milli-seconds.                                             |
| *Description*           | It is recommended to only use this criteria in conjunction with the "combined" output mode of the access logger, since this filter criteria is only applied to response log messages. |
| *Default value*         | None                                                                                                                                                                                  |
| *Allowed values*        | An integer.Lower limit: 0.                                                                                                                                                            |
| *Multi-valued*          | No                                                                                                                                                                                    |
| *Required*              | No                                                                                                                                                                                    |
| *Admin action required* | None                                                                                                                                                                                  |
| *Advanced*              | No                                                                                                                                                                                    |
| *Read-only*             | No                                                                                                                                                                                    |

### response-result-code-equal-to

|                         |                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters operation response log records associated with operations which include any of the specified result codes.                                                                    |
| *Description*           | It is recommended to only use this criteria in conjunction with the "combined" output mode of the access logger, since this filter criteria is only applied to response log messages. |
| *Default value*         | None                                                                                                                                                                                  |
| *Allowed values*        | An integer.Lower limit: 0.                                                                                                                                                            |
| *Multi-valued*          | Yes                                                                                                                                                                                   |
| *Required*              | No                                                                                                                                                                                    |
| *Admin action required* | None                                                                                                                                                                                  |
| *Advanced*              | No                                                                                                                                                                                    |
| *Read-only*             | No                                                                                                                                                                                    |

### response-result-code-not-equal-to

|                         |                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters operation response log records associated with operations which do not include any of the specified result codes.                                                             |
| *Description*           | It is recommended to only use this criteria in conjunction with the "combined" output mode of the access logger, since this filter criteria is only applied to response log messages. |
| *Default value*         | None                                                                                                                                                                                  |
| *Allowed values*        | An integer.Lower limit: 0.                                                                                                                                                            |
| *Multi-valued*          | Yes                                                                                                                                                                                   |
| *Required*              | No                                                                                                                                                                                    |
| *Admin action required* | None                                                                                                                                                                                  |
| *Advanced*              | No                                                                                                                                                                                    |
| *Read-only*             | No                                                                                                                                                                                    |

### search-response-is-indexed

|                         |                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters search operation response log records associated with searches which were either indexed or unindexed.                                                                        |
| *Description*           | It is recommended to only use this criteria in conjunction with the "combined" output mode of the access logger, since this filter criteria is only applied to response log messages. |
| *Default value*         | None                                                                                                                                                                                  |
| *Allowed values*        | truefalse                                                                                                                                                                             |
| *Multi-valued*          | No                                                                                                                                                                                    |
| *Required*              | No                                                                                                                                                                                    |
| *Admin action required* | None                                                                                                                                                                                  |
| *Advanced*              | No                                                                                                                                                                                    |
| *Read-only*             | No                                                                                                                                                                                    |

### search-response-nentries-greater-than

|                         |                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters search operation response log records associated with searches which returned more than the specified number of entries.                                                      |
| *Description*           | It is recommended to only use this criteria in conjunction with the "combined" output mode of the access logger, since this filter criteria is only applied to response log messages. |
| *Default value*         | None                                                                                                                                                                                  |
| *Allowed values*        | An integer.Lower limit: 0.                                                                                                                                                            |
| *Multi-valued*          | No                                                                                                                                                                                    |
| *Required*              | No                                                                                                                                                                                    |
| *Admin action required* | None                                                                                                                                                                                  |
| *Advanced*              | No                                                                                                                                                                                    |
| *Read-only*             | No                                                                                                                                                                                    |

### search-response-nentries-less-than

|                         |                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters search operation response log records associated with searches which returned less than the specified number of entries.                                                      |
| *Description*           | It is recommended to only use this criteria in conjunction with the "combined" output mode of the access logger, since this filter criteria is only applied to response log messages. |
| *Default value*         | None                                                                                                                                                                                  |
| *Allowed values*        | An integer.Lower limit: 0.                                                                                                                                                            |
| *Multi-valued*          | No                                                                                                                                                                                    |
| *Required*              | No                                                                                                                                                                                    |
| *Admin action required* | None                                                                                                                                                                                  |
| *Advanced*              | No                                                                                                                                                                                    |
| *Read-only*             | No                                                                                                                                                                                    |

### user-dn-equal-to

|                         |                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters log records associated with users matching at least one of the specified DN patterns.                                                                                                                                                                                                                                                                                                             |
| *Description*           | Valid DN filters are strings composed of zero or more wildcards. A double wildcard \*\* replaces one or more RDN components (as in uid=dmiller,\*\*,dc=example,dc=com). A simple wildcard \* replaces either a whole RDN, or a whole type, or a value substring (as in uid=bj\*,ou=people,dc=example,dc=com). To match the anonymous user, use two double quote characters with no space in between (""). |
| *Default value*         | None                                                                                                                                                                                                                                                                                                                                                                                                      |
| *Allowed values*        | A string.                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                                                                                                                                                                       |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                        |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                                                                                      |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                        |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                        |

### user-dn-not-equal-to

|                         |                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters log records associated with users which do not match any of the specified DN patterns.                                                                                                                                                                                                                                                                                                            |
| *Description*           | Valid DN filters are strings composed of zero or more wildcards. A double wildcard \*\* replaces one or more RDN components (as in uid=dmiller,\*\*,dc=example,dc=com). A simple wildcard \* replaces either a whole RDN, or a whole type, or a value substring (as in uid=bj\*,ou=people,dc=example,dc=com). To match the anonymous user, use two double quote characters with no space in between (""). |
| *Default value*         | None                                                                                                                                                                                                                                                                                                                                                                                                      |
| *Allowed values*        | A string.                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                                                                                                                                                                       |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                        |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                                                                                      |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                        |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                        |

### user-is-member-of

|                         |                                                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters log records associated with users which are members of at least one of the specified groups. |
| *Default value*         | None                                                                                                 |
| *Allowed values*        | A valid DN.                                                                                          |
| *Multi-valued*          | Yes                                                                                                  |
| *Required*              | No                                                                                                   |
| *Admin action required* | None                                                                                                 |
| *Advanced*              | No                                                                                                   |
| *Read-only*             | No                                                                                                   |

### user-is-not-member-of

|                         |                                                                                                 |
| ----------------------- | ----------------------------------------------------------------------------------------------- |
| *Synopsis*              | Filters log records associated with users which are not members of any of the specified groups. |
| *Default value*         | None                                                                                            |
| *Allowed values*        | A valid DN.                                                                                     |
| *Multi-valued*          | Yes                                                                                             |
| *Required*              | No                                                                                              |
| *Admin action required* | None                                                                                            |
| *Advanced*              | No                                                                                              |
| *Read-only*             | No                                                                                              |

---

---
title: Access Log Publisher
description: This is an abstract object type that cannot be instantiated.
component: pingds
version: 8.1
page_id: pingds:configref:objects-access-log-publisher
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-access-log-publisher.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  access_log_publishers: Access Log Publishers
  parent: Parent
  dependencies: Dependencies
  access_log_publisher_properties: Access Log Publisher properties
  basic_properties: Basic properties
  enabled: enabled
  filtering-policy: filtering-policy
  java-class: java-class
  advanced_properties: Advanced properties
  suppress-internal-operations: suppress-internal-operations
  suppress-synchronization-operations: suppress-synchronization-operations
---

# Access Log Publisher

*This is an abstract object type that cannot be instantiated.*

Access Log Publishers are responsible for distributing access log messages from the access logger to a destination.

Access log messages provide information about the types of operations processed by the server.

## Access Log Publishers

The following Access Log Publishers are available:

* [Common Audit Access Log Publisher](objects-common-audit-access-log-publisher.html)

* [File Based Access Log Publisher (DEPRECATED)](objects-file-based-access-log-publisher.html)

* [File Based Audit Log Publisher](objects-file-based-audit-log-publisher.html)

These Access Log Publishers inherit the properties described below.

## Parent

The Access Log Publisher object inherits from [Log Publisher](objects-log-publisher.html).

## Dependencies

Access Log Publishers depend on the following objects:

* [Access Log Filtering Criteria](objects-access-log-filtering-criteria.html)

## Access Log Publisher properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                                                                    | Advanced Properties                                                                                                                       |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [enabled](#enabled) [filtering-policy](#filtering-policy) [java-class](#java-class) | [suppress-internal-operations](#suppress-internal-operations) [suppress-synchronization-operations](#suppress-synchronization-operations) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### enabled

|                         |                                                         |
| ----------------------- | ------------------------------------------------------- |
| *Synopsis*              | Indicates whether the Log Publisher is enabled for use. |
| *Default value*         | None                                                    |
| *Allowed values*        | truefalse                                               |
| *Multi-valued*          | No                                                      |
| *Required*              | Yes                                                     |
| *Admin action required* | None                                                    |
| *Advanced*              | No                                                      |
| *Read-only*             | No                                                      |

### filtering-policy

|                         |                                                                                                                                                                                                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *Synopsis*              | Specifies how filtering criteria should be applied to log records.                                                                                                                                                                                                       |
| *Default value*         | no-filtering                                                                                                                                                                                                                                                             |
| *Allowed values*        | * exclusive: Records must not match any of the filtering criteria in order to be logged.

* inclusive: Records must match at least one of the filtering criteria in order to be logged.

* no-filtering: No filtering will be performed, and all records will be logged. |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                       |
| *Required*              | No                                                                                                                                                                                                                                                                       |
| *Admin action required* | None                                                                                                                                                                                                                                                                     |
| *Advanced*              | No                                                                                                                                                                                                                                                                       |
| *Read-only*             | No                                                                                                                                                                                                                                                                       |

### java-class

|                         |                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------- |
| *Synopsis*              | The fully-qualified name of the Java class that provides the Access Log Publisher implementation. |
| *Default value*         | org.opends.server.loggers.AccessLogPublisher                                                      |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.loggers.LogPublisher                  |
| *Multi-valued*          | No                                                                                                |
| *Required*              | Yes                                                                                               |
| *Admin action required* | None                                                                                              |
| *Advanced*              | No                                                                                                |
| *Read-only*             | No                                                                                                |

## Advanced properties

Use the `--advanced` option to access advanced properties.

### suppress-internal-operations

|                         |                                                                                                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Indicates whether internal operations (for example, operations that are initiated by plugins) should be logged along with the operations that are requested by users. |
| *Default value*         | true                                                                                                                                                                  |
| *Allowed values*        | truefalse                                                                                                                                                             |
| *Multi-valued*          | No                                                                                                                                                                    |
| *Required*              | No                                                                                                                                                                    |
| *Admin action required* | None                                                                                                                                                                  |
| *Advanced*              | Yes                                                                                                                                                                   |
| *Read-only*             | No                                                                                                                                                                    |

### suppress-synchronization-operations

|                         |                                                                                                          |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Indicates whether access messages that are generated by synchronization operations should be suppressed. |
| *Default value*         | false                                                                                                    |
| *Allowed values*        | truefalse                                                                                                |
| *Multi-valued*          | No                                                                                                       |
| *Required*              | No                                                                                                       |
| *Admin action required* | None                                                                                                     |
| *Advanced*              | Yes                                                                                                      |
| *Read-only*             | No                                                                                                       |

---

---
title: Account Status Notification Handler
description: This is an abstract object type that cannot be instantiated.
component: pingds
version: 8.1
page_id: pingds:configref:objects-account-status-notification-handler
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-account-status-notification-handler.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  account_status_notification_handlers: Account Status Notification Handlers
  dependencies: Dependencies
  account_status_notification_handler_properties: Account Status Notification Handler properties
  basic_properties: Basic properties
  enabled: enabled
  java-class: java-class
---

# Account Status Notification Handler

*This is an abstract object type that cannot be instantiated.*

Account Status Notification Handlers are invoked to provide notification to users in some form (for example, by an email message) when the status of a user's account has changed in some way. The Account Status Notification Handler can be used to notify the user and/or administrators of the change.

## Account Status Notification Handlers

The following Account Status Notification Handlers are available:

* [Error Log Account Status Notification Handler](objects-error-log-account-status-notification-handler.html)

* [SMTP Account Status Notification Handler](objects-smtp-account-status-notification-handler.html)

These Account Status Notification Handlers inherit the properties described below.

## Dependencies

The following objects depend on Account Status Notification Handlers:

* [Password Policy](objects-password-policy.html)

## Account Status Notification Handler properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                              |
| --------------------------------------------- |
| [enabled](#enabled) [java-class](#java-class) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### enabled

|                         |                                                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *Synopsis*              | Indicates whether the Account Status Notification Handler is enabled. Only enabled handlers are invoked whenever a related event occurs in the server. |
| *Default value*         | None                                                                                                                                                   |
| *Allowed values*        | truefalse                                                                                                                                              |
| *Multi-valued*          | No                                                                                                                                                     |
| *Required*              | Yes                                                                                                                                                    |
| *Admin action required* | None                                                                                                                                                   |
| *Advanced*              | No                                                                                                                                                     |
| *Read-only*             | No                                                                                                                                                     |

### java-class

|                         |                                                                                                                            |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the fully-qualified name of the Java class that provides the Account Status Notification Handler implementation. |
| *Default value*         | None                                                                                                                       |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.AccountStatusNotificationHandler                           |
| *Multi-valued*          | No                                                                                                                         |
| *Required*              | Yes                                                                                                                        |
| *Admin action required* | The object must be disabled and re-enabled for changes to take effect.                                                     |
| *Advanced*              | No                                                                                                                         |
| *Read-only*             | No                                                                                                                         |

---

---
title: Administration Connector
description: The Administration Connector is used to interact with administration tools using LDAP.
component: pingds
version: 8.1
page_id: pingds:configref:objects-administration-connector
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-administration-connector.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  dependencies: Dependencies
  administration_connector_properties: Administration Connector properties
  basic_properties: Basic properties
  advertised-listen-address: advertised-listen-address
  allowed-client: allowed-client
  denied-client: denied-client
  key-manager-provider: key-manager-provider
  listen-address: listen-address
  listen-port: listen-port
  proxy-protocol-allowed-client: proxy-protocol-allowed-client
  proxy-protocol-enabled: proxy-protocol-enabled
  restricted-client: restricted-client
  restricted-client-connection-limit: restricted-client-connection-limit
  ssl-cert-nickname: ssl-cert-nickname
  ssl-cipher-suite: ssl-cipher-suite
  ssl-protocol: ssl-protocol
  trust-manager-provider: trust-manager-provider
---

# Administration Connector

The Administration Connector is used to interact with administration tools using LDAP.

It is a dedicated entry point for administration.

## Dependencies

Administration Connectors depend on the following objects:

* [Key Manager Provider](objects-key-manager-provider.html)

* [Trust Manager Provider](objects-trust-manager-provider.html)

## Administration Connector properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [advertised-listen-address](#advertised-listen-address) [allowed-client](#allowed-client) [denied-client](#denied-client) [key-manager-provider](#key-manager-provider) [listen-address](#listen-address) [listen-port](#listen-port) [proxy-protocol-allowed-client](#proxy-protocol-allowed-client) [proxy-protocol-enabled](#proxy-protocol-enabled) [restricted-client](#restricted-client) [restricted-client-connection-limit](#restricted-client-connection-limit) [ssl-cert-nickname](#ssl-cert-nickname) [ssl-cipher-suite](#ssl-cipher-suite) [ssl-protocol](#ssl-protocol) [trust-manager-provider](#trust-manager-provider) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### advertised-listen-address

|                         |                                                                                                                      |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | The advertised address(es) which clients should use for connecting to this Administration Connector.                 |
| *Description*           | Multiple addresses may be provided as separate values for this attribute. The meta-address 0.0.0.0 is not permitted. |
| *Default value*         | None                                                                                                                 |
| *Allowed values*        | A hostname or an IP address.                                                                                         |
| *Multi-valued*          | Yes                                                                                                                  |
| *Required*              | Yes                                                                                                                  |
| *Admin action required* | None                                                                                                                 |
| *Advanced*              | No                                                                                                                   |
| *Read-only*             | No                                                                                                                   |

### allowed-client

|                         |                                                                                                                                                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | A set of clients who will be allowed to establish connections to this Administration Connector.                                                                                                                                                            |
| *Description*           | Valid values include a host name, a fully qualified domain name, a domain name, an IP address, or a subnetwork with subnetwork mask. Specifying a value for this property in a connection handler will override any value set in the global configuration. |
| *Default value*         | All clients with addresses that do not match an address on the deny list are allowed. If there is no deny list, then all clients are allowed.                                                                                                              |
| *Allowed values*        | An IP address mask.                                                                                                                                                                                                                                        |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                        |
| *Required*              | No                                                                                                                                                                                                                                                         |
| *Admin action required* | NoneChanges to this property take effect immediately and do not interfere with established connections.                                                                                                                                                    |
| *Advanced*              | No                                                                                                                                                                                                                                                         |
| *Read-only*             | No                                                                                                                                                                                                                                                         |

### denied-client

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | A set of clients who are not allowed to establish connections to this Administration Connector.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Description*           | Valid values include a host name, a fully qualified domain name, a domain name, an IP address, or a subnetwork with subnetwork mask. If both allowed and denied client masks are defined and a client connection matches one or more masks in both lists, then the connection is denied. If only a denied list is specified, then any client not matching a mask in that list is allowed. Specifying a value for this property in a connection handler will override any value set in the global configuration. |
| *Default value*         | If an allow list is specified, then only clients with addresses on the allow list are allowed. Otherwise, all clients are allowed.                                                                                                                                                                                                                                                                                                                                                                              |
| *Allowed values*        | An IP address mask.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| *Admin action required* | NoneChanges to this property take effect immediately and do not interfere with established connections.                                                                                                                                                                                                                                                                                                                                                                                                         |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### key-manager-provider

|                         |                                                                                                                                        |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the name of the key manager that is used with the Administration Connector .                                                 |
| *Default value*         | None                                                                                                                                   |
| *Allowed values*        | The name of an existing [key-manager-provider](objects-key-manager-provider.html).The referenced key manager provider must be enabled. |
| *Multi-valued*          | No                                                                                                                                     |
| *Required*              | Yes                                                                                                                                    |
| *Admin action required* | Restart the server for changes to take effect.                                                                                         |
| *Advanced*              | No                                                                                                                                     |
| *Read-only*             | No                                                                                                                                     |

### listen-address

|                         |                                                                                                                                                               |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | The network interface(s) on which this Administration Connector should listen for incoming client connections.                                                |
| *Description*           | Multiple addresses may be provided as separate values for this attribute. If no values are provided, then the directory server will listen on all interfaces. |
| *Default value*         | 0.0.0.0                                                                                                                                                       |
| *Allowed values*        | A hostname or an IP address.                                                                                                                                  |
| *Multi-valued*          | Yes                                                                                                                                                           |
| *Required*              | No                                                                                                                                                            |
| *Admin action required* | Restart the server for changes to take effect.                                                                                                                |
| *Advanced*              | No                                                                                                                                                            |
| *Read-only*             | No                                                                                                                                                            |

### listen-port

|                         |                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the port number on which the Administration Connector will listen for connections from clients. |
| *Description*           | Only a single port number may be provided.                                                                |
| *Default value*         | None                                                                                                      |
| *Allowed values*        | An integer.Lower limit: 1.Upper limit: 65535.                                                             |
| *Multi-valued*          | No                                                                                                        |
| *Required*              | Yes                                                                                                       |
| *Admin action required* | The object must be disabled and re-enabled for changes to take effect.                                    |
| *Advanced*              | No                                                                                                        |
| *Read-only*             | No                                                                                                        |

### proxy-protocol-allowed-client

|                         |                                                                                                                                                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | When the proxy protocol is enabled, this property represents the set of clients who will be allowed to establish connections to this Administration Connector and will be required to use proxy protocol.                                                  |
| *Description*           | Valid values include a host name, a fully qualified domain name, a domain name, an IP address, or a subnetwork with subnetwork mask. Specifying a value for this property in a connection handler will override any value set in the global configuration. |
| *Default value*         | If the proxy protocol is enabled then only clients with addresses matching an address on the proxy-protocol-allowed-client list and using proxy protocol are allowed.                                                                                      |
| *Allowed values*        | An IP address mask.                                                                                                                                                                                                                                        |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                        |
| *Required*              | No                                                                                                                                                                                                                                                         |
| *Admin action required* | NoneChanges to this property take effect immediately and do not interfere with established connections.                                                                                                                                                    |
| *Advanced*              | No                                                                                                                                                                                                                                                         |
| *Read-only*             | No                                                                                                                                                                                                                                                         |

### proxy-protocol-enabled

|                         |                                                                                                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *Synopsis*              | Indicates whether the proxy protocol is enabled.                                                                                                                                     |
| *Description*           | If enabled, the Administration Connector makes the server use proxy protocol for connections with a source IP address matching an address in the proxy-protocol-allowed-client list. |
| *Default value*         | false                                                                                                                                                                                |
| *Allowed values*        | truefalse                                                                                                                                                                            |
| *Multi-valued*          | No                                                                                                                                                                                   |
| *Required*              | No                                                                                                                                                                                   |
| *Admin action required* | None                                                                                                                                                                                 |
| *Advanced*              | No                                                                                                                                                                                   |
| *Read-only*             | No                                                                                                                                                                                   |

### restricted-client

|                         |                                                                                                                                                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | A set of clients who will be limited to the maximum number of connections specified by the "restricted-client-connection-limit" property.                                                                                                                  |
| *Description*           | Valid values include a host name, a fully qualified domain name, a domain name, an IP address, or a subnetwork with subnetwork mask. Specifying a value for this property in a connection handler will override any value set in the global configuration. |
| *Default value*         | No restrictions are imposed on the number of connections a client can open.                                                                                                                                                                                |
| *Allowed values*        | An IP address mask.                                                                                                                                                                                                                                        |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                        |
| *Required*              | No                                                                                                                                                                                                                                                         |
| *Admin action required* | NoneChanges to this property take effect immediately and do not interfere with established connections.                                                                                                                                                    |
| *Advanced*              | No                                                                                                                                                                                                                                                         |
| *Read-only*             | No                                                                                                                                                                                                                                                         |

### restricted-client-connection-limit

|                         |                                                                                                                                                                                                                                                                                                                                          |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the maximum number of connections a restricted client can open at the same time to this Administration Connector.                                                                                                                                                                                                              |
| *Description*           | Once Directory Server accepts the specified number of connections from a client specified in restricted-client, any additional connection will be rejected. The number of connections is maintained by IP address. Specifying a value for this property in a connection handler will override any value set in the global configuration. |
| *Default value*         | 100                                                                                                                                                                                                                                                                                                                                      |
| *Allowed values*        | An integer.Lower limit: 0.                                                                                                                                                                                                                                                                                                               |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                                                                                       |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                       |
| *Admin action required* | NoneChanges to this property take effect immediately and do not interfere with established connections.                                                                                                                                                                                                                                  |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                       |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                       |

### ssl-cert-nickname

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *Synopsis*              | Specifies the nicknames (also called the aliases) of the keys or key pairs that the Administration Connector should use when performing SSL communication.                                                                                                                                                                                                                                                                                                                                                                                             |
| *Description*           | The property can be used multiple times (referencing different nicknames) when server certificates with different public key algorithms are used in parallel (for example, RSA, DSA, and ECC-based algorithms). When a nickname refers to an asymmetric (public/private) key pair, the nickname for the public key certificate and associated private key entry must match exactly. A single nickname is used to retrieve both the public key and the private key. This is only applicable when the Administration Connector is configured to use SSL. |
| *Default value*         | Let the server decide.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Allowed values*        | A string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| *Admin action required* | Restart the server for changes to take effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### ssl-cipher-suite

|                         |                                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| *Synopsis*              | Specifies the names of the SSL cipher suites that are allowed for use in SSL communication.                                    |
| *Default value*         | Uses the default set of SSL cipher suites provided by the server's JVM.                                                        |
| *Allowed values*        | A string.                                                                                                                      |
| *Multi-valued*          | Yes                                                                                                                            |
| *Required*              | No                                                                                                                             |
| *Admin action required* | NoneChanges to this property take effect immediately but will only impact new SSL/TLS-based sessions created after the change. |
| *Advanced*              | No                                                                                                                             |
| *Read-only*             | No                                                                                                                             |

### ssl-protocol

|                         |                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the names of the SSL protocols that are allowed for use in SSL or StartTLS communication.                       |
| *Default value*         | Uses the default set of SSL protocols provided by the server's JVM.                                                       |
| *Allowed values*        | A string.                                                                                                                 |
| *Multi-valued*          | Yes                                                                                                                       |
| *Required*              | No                                                                                                                        |
| *Admin action required* | NoneChanges to this property take effect immediately but only impact new SSL/TLS-based sessions created after the change. |
| *Advanced*              | No                                                                                                                        |
| *Read-only*             | No                                                                                                                        |

### trust-manager-provider

|                         |                                                                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the name(s) of the trust manager(s) that is used with the Administration Connector .                                               |
| *Default value*         | None                                                                                                                                         |
| *Allowed values*        | The name of an existing [trust-manager-provider](objects-trust-manager-provider.html).The referenced trust manager provider must be enabled. |
| *Multi-valued*          | Yes                                                                                                                                          |
| *Required*              | Yes                                                                                                                                          |
| *Admin action required* | Restart the server for changes to take effect.                                                                                               |
| *Advanced*              | No                                                                                                                                           |
| *Read-only*             | No                                                                                                                                           |

---

---
title: AES Password Storage Scheme (LEGACY)
description: "LEGACY since 7.0.0: Reversible password storage schemes are weaker than modern hash based schemes and should be avoided if possible. They are only required when using legacy SASL mechanisms. Alternative: A strong hash-based scheme such as one of the schemes enabled by default."
component: pingds
version: 8.1
page_id: pingds:configref:objects-aes-password-storage-scheme
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-aes-password-storage-scheme.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parent: Parent
  aes_password_storage_scheme_properties: AES Password Storage Scheme properties
  basic_properties: Basic properties
  enabled: enabled
  advanced_properties: Advanced properties
  java-class: java-class
---

# AES Password Storage Scheme (LEGACY)

|   |                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | LEGACY since 7.0.0: Reversible password storage schemes are weaker than modern hash based schemes and should be avoided if possible. They are only required when using legacy SASL mechanisms. Alternative: A strong hash-based scheme such as one of the schemes enabled by default. |

The AES Password Storage Scheme provides a mechanism for encoding user passwords using the AES reversible encryption mechanism.

This scheme contains only an implementation for the user password syntax, with a storage scheme name of "AES".

## Parent

The AES Password Storage Scheme object inherits from [Password Storage Scheme](objects-password-storage-scheme.html).

## AES Password Storage Scheme properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties    | Advanced Properties       |
| ------------------- | ------------------------- |
| [enabled](#enabled) | [java-class](#java-class) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### enabled

|                         |                                                                   |
| ----------------------- | ----------------------------------------------------------------- |
| *Synopsis*              | Indicates whether the Password Storage Scheme is enabled for use. |
| *Default value*         | None                                                              |
| *Allowed values*        | truefalse                                                         |
| *Multi-valued*          | No                                                                |
| *Required*              | Yes                                                               |
| *Admin action required* | None                                                              |
| *Advanced*              | No                                                                |
| *Read-only*             | No                                                                |

## Advanced properties

Use the `--advanced` option to access advanced properties.

### java-class

|                         |                                                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------ |
| *Synopsis*              | Specifies the fully-qualified name of the Java class that provides the AES Password Storage Scheme implementation. |
| *Default value*         | org.opends.server.extensions.AESPasswordStorageScheme                                                              |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.PasswordStorageScheme                              |
| *Multi-valued*          | No                                                                                                                 |
| *Required*              | Yes                                                                                                                |
| *Admin action required* | None                                                                                                               |
| *Advanced*              | Yes                                                                                                                |
| *Read-only*             | No                                                                                                                 |

---

---
title: Alert Handler
description: This is an abstract object type that cannot be instantiated.
component: pingds
version: 8.1
page_id: pingds:configref:objects-alert-handler
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-alert-handler.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  alert_handlers: Alert Handlers
  alert_handler_properties: Alert Handler properties
  basic_properties: Basic properties
  disabled-alert-type: disabled-alert-type
  enabled: enabled
  enabled-alert-type: enabled-alert-type
  java-class: java-class
---

# Alert Handler

*This is an abstract object type that cannot be instantiated.*

Alert Handlers are used to notify administrators of significant problems or notable events that occur in the PingDS directory server.

## Alert Handlers

The following Alert Handlers are available:

* [JMX Alert Handler](objects-jmx-alert-handler.html)

* [SMTP Alert Handler](objects-smtp-alert-handler.html)

These Alert Handlers inherit the properties described below.

## Alert Handler properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| [disabled-alert-type](#disabled-alert-type) [enabled](#enabled) [enabled-alert-type](#enabled-alert-type) [java-class](#java-class) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### disabled-alert-type

|                         |                                                                                                                                                                                                                                                                                                                                         |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the names of the alert types that are disabled for this alert handler.                                                                                                                                                                                                                                                        |
| *Description*           | If there are any values for this attribute, then no alerts with any of the specified types are allowed. If there are no values for this attribute, then only alerts with a type included in the set of enabled alert types are allowed, or if there are no values for the enabled alert types option, then all alert types are allowed. |
| *Default value*         | If there is a set of enabled alert types, then only alerts with one of those types are allowed. Otherwise, all alerts are allowed.                                                                                                                                                                                                      |
| *Allowed values*        | A string.                                                                                                                                                                                                                                                                                                                               |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                                                                                                     |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                      |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                    |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                      |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                      |

### enabled

|                         |                                                 |
| ----------------------- | ----------------------------------------------- |
| *Synopsis*              | Indicates whether the Alert Handler is enabled. |
| *Default value*         | None                                            |
| *Allowed values*        | truefalse                                       |
| *Multi-valued*          | No                                              |
| *Required*              | Yes                                             |
| *Admin action required* | None                                            |
| *Advanced*              | No                                              |
| *Read-only*             | No                                              |

### enabled-alert-type

|                         |                                                                                                                                                                                                                                                                                                          |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the names of the alert types that are enabled for this alert handler.                                                                                                                                                                                                                          |
| *Description*           | If there are any values for this attribute, then only alerts with one of the specified types are allowed (unless they are also included in the disabled alert types). If there are no values for this attribute, then any alert with a type not included in the list of disabled alert types is allowed. |
| *Default value*         | All alerts with types not included in the set of disabled alert types are allowed.                                                                                                                                                                                                                       |
| *Allowed values*        | A string.                                                                                                                                                                                                                                                                                                |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                                                                      |
| *Required*              | No                                                                                                                                                                                                                                                                                                       |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                     |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                       |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                       |

### java-class

|                         |                                                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the fully-qualified name of the Java class that provides the Alert Handler implementation. |
| *Default value*         | None                                                                                                 |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.AlertHandler                         |
| *Multi-valued*          | No                                                                                                   |
| *Required*              | Yes                                                                                                  |
| *Admin action required* | The object must be disabled and re-enabled for changes to take effect.                               |
| *Advanced*              | No                                                                                                   |
| *Read-only*             | No                                                                                                   |

---

---
title: Alive HTTP endpoint
description: The Alive HTTP endpoint provides a way to check whether the server is facing serious problems that need administrative actions to recover.
component: pingds
version: 8.1
page_id: pingds:configref:objects-alive-endpoint
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-alive-endpoint.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parent: Parent
  alive_http_endpoint_properties: Alive HTTP endpoint properties
  basic_properties: Basic properties
  authorization-mechanism: authorization-mechanism
  base-path: base-path
  enabled: enabled
  advanced_properties: Advanced properties
  java-class: java-class
---

# Alive HTTP endpoint

The Alive HTTP endpoint provides a way to check whether the server is facing serious problems that need administrative actions to recover.

This endpoint responds 200 without content when the server is alive or 503 with a JSON containing an array of serious errors in the field "alive-errors".

## Parent

The Alive HTTP endpoint object inherits from [HTTP Endpoint](objects-http-endpoint.html).

## Alive HTTP endpoint properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                                                                                | Advanced Properties       |
| ----------------------------------------------------------------------------------------------- | ------------------------- |
| [authorization-mechanism](#authorization-mechanism) [base-path](#base-path) [enabled](#enabled) | [java-class](#java-class) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### authorization-mechanism

|                         |                                                                                                                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | The HTTP authorization mechanisms supported by this HTTP Endpoint.                                                                                                                          |
| *Default value*         | None                                                                                                                                                                                        |
| *Allowed values*        | The name of an existing [http-authorization-mechanism](objects-http-authorization-mechanism.html).The referenced authorization mechanism must be enabled when the HTTP Endpoint is enabled. |
| *Multi-valued*          | Yes                                                                                                                                                                                         |
| *Required*              | Yes                                                                                                                                                                                         |
| *Admin action required* | None                                                                                                                                                                                        |
| *Advanced*              | No                                                                                                                                                                                          |
| *Read-only*             | No                                                                                                                                                                                          |

### base-path

|                         |                                                                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| *Synopsis*              | All HTTP requests matching the base path or subordinate to it will be routed to the HTTP endpoint unless a more specific HTTP endpoint is found. |
| *Default value*         | None                                                                                                                                             |
| *Allowed values*        | A string.                                                                                                                                        |
| *Multi-valued*          | No                                                                                                                                               |
| *Required*              | Yes                                                                                                                                              |
| *Admin action required* | None                                                                                                                                             |
| *Advanced*              | No                                                                                                                                               |
| *Read-only*             | Yes                                                                                                                                              |

### enabled

|                         |                                                 |
| ----------------------- | ----------------------------------------------- |
| *Synopsis*              | Indicates whether the HTTP Endpoint is enabled. |
| *Default value*         | None                                            |
| *Allowed values*        | truefalse                                       |
| *Multi-valued*          | No                                              |
| *Required*              | Yes                                             |
| *Admin action required* | None                                            |
| *Advanced*              | No                                              |
| *Read-only*             | No                                              |

## Advanced properties

Use the `--advanced` option to access advanced properties.

### java-class

|                         |                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the fully-qualified name of the Java class that provides the Alive HTTP endpoint implementation. |
| *Default value*         | org.opends.server.protocols.http.AliveEndpoint                                                             |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.HttpEndpoint                               |
| *Multi-valued*          | No                                                                                                         |
| *Required*              | Yes                                                                                                        |
| *Admin action required* | None                                                                                                       |
| *Advanced*              | Yes                                                                                                        |
| *Read-only*             | No                                                                                                         |

---

---
title: Anonymous SASL Mechanism Handler
description: The ANONYMOUS SASL mechanism provides the ability for clients to perform an anonymous bind using a SASL mechanism.
component: pingds
version: 8.1
page_id: pingds:configref:objects-anonymous-sasl-mechanism-handler
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-anonymous-sasl-mechanism-handler.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parent: Parent
  anonymous_sasl_mechanism_handler_properties: Anonymous SASL Mechanism Handler properties
  basic_properties: Basic properties
  enabled: enabled
  advanced_properties: Advanced properties
  java-class: java-class
---

# Anonymous SASL Mechanism Handler

The ANONYMOUS SASL mechanism provides the ability for clients to perform an anonymous bind using a SASL mechanism.

The only real benefit that this provides over a normal anonymous bind (that is, using simple authentication with no password) is that the ANONYMOUS SASL mechanism also allows the client to include a trace string in the request. This trace string can help identify the application that performed the bind (although since there is no authentication, there is no assurance that some other client did not spoof that trace string).

## Parent

The Anonymous SASL Mechanism Handler object inherits from [SASL Mechanism Handler](objects-sasl-mechanism-handler.html).

## Anonymous SASL Mechanism Handler properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties    | Advanced Properties       |
| ------------------- | ------------------------- |
| [enabled](#enabled) | [java-class](#java-class) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### enabled

|                         |                                                                  |
| ----------------------- | ---------------------------------------------------------------- |
| *Synopsis*              | Indicates whether the SASL mechanism handler is enabled for use. |
| *Default value*         | None                                                             |
| *Allowed values*        | truefalse                                                        |
| *Multi-valued*          | No                                                               |
| *Required*              | Yes                                                              |
| *Admin action required* | None                                                             |
| *Advanced*              | No                                                               |
| *Read-only*             | No                                                               |

## Advanced properties

Use the `--advanced` option to access advanced properties.

### java-class

|                         |                                                                                                               |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the fully-qualified name of the Java class that provides the SASL mechanism handler implementation. |
| *Default value*         | org.opends.server.extensions.AnonymousSASLMechanismHandler                                                    |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.SASLMechanismHandler                          |
| *Multi-valued*          | No                                                                                                            |
| *Required*              | Yes                                                                                                           |
| *Admin action required* | The object must be disabled and re-enabled for changes to take effect.                                        |
| *Advanced*              | Yes                                                                                                           |
| *Read-only*             | No                                                                                                            |

---

---
title: Argon2 Password Storage Scheme
description: The Argon2 Password Storage Scheme provides a mechanism for encoding user passwords using the Argon2 message digest algorithm.
component: pingds
version: 8.1
page_id: pingds:configref:objects-argon2-password-storage-scheme
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-argon2-password-storage-scheme.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parent: Parent
  argon2_password_storage_scheme_properties: Argon2 Password Storage Scheme properties
  basic_properties: Basic properties
  argon2-iterations: argon2-iterations
  argon2-length: argon2-length
  argon2-memory: argon2-memory
  argon2-parallelism: argon2-parallelism
  argon2-salt-length: argon2-salt-length
  argon2-variant: argon2-variant
  enabled: enabled
  rehash-policy: rehash-policy
  advanced_properties: Advanced properties
  argon2-memory-pool-size: argon2-memory-pool-size
  java-class: java-class
---

# Argon2 Password Storage Scheme

The Argon2 Password Storage Scheme provides a mechanism for encoding user passwords using the Argon2 message digest algorithm.

This scheme contains an implementation for the user password syntax, with a storage scheme name of "ARGON2".

## Parent

The Argon2 Password Storage Scheme object inherits from [Password Storage Scheme](objects-password-storage-scheme.html).

## Argon2 Password Storage Scheme properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                                                                                                                                                                                                                                                                  | Advanced Properties                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [argon2-iterations](#argon2-iterations) [argon2-length](#argon2-length) [argon2-memory](#argon2-memory) [argon2-parallelism](#argon2-parallelism) [argon2-salt-length](#argon2-salt-length) [argon2-variant](#argon2-variant) [enabled](#enabled) [rehash-policy](#rehash-policy) | [argon2-memory-pool-size](#argon2-memory-pool-size) [java-class](#java-class) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### argon2-iterations

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | The number of iterations to perform.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| *Description*           | By default, changes to this setting impact only newly created and updated passwords. However, if the rehash-policy is set to always or only-increase, it causes the server to recalculate each user's password hash on their next authentication, and write the new hash to the user's entry on disk. Changing the number of iterations therefore leads to a short-term spike in CPU and disk use as the server updates each user's password when they next authenticate. Longer term, increasing this setting results in more secure passwords at the expense of much higher CPU consumption and lower throughput. |
| *Default value*         | 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| *Allowed values*        | An integer.Lower limit: 1.Upper limit: 30.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### argon2-length

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | The length of the produced hash.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| *Description*           | By default, changes to this setting impact only newly created and updated passwords. However, if the rehash-policy is set to always or only-increase, it causes the server to recalculate each user's password hash on their next authentication, and write the new hash to the user's entry on disk. Changing the length of the produced hash therefore leads to a short-term spike in CPU and disk use as the server updates each user's password when they next authenticate. Longer term, increasing this setting results in more secure passwords at the expense of much higher CPU consumption and lower throughput. |
| *Default value*         | 32                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| *Allowed values*        | An integer.Lower limit: 4.Upper limit: 32768.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### argon2-memory

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | The amount of memory to use for a single hash, expressed in kibibytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| *Description*           | By default, changes to this setting impact only newly created and updated passwords. However, if the rehash-policy is set to always or only-increase, it causes the server to recalculate each user's password hash on their next authentication, and write the new hash to the user's entry on disk. Changing the amount of memory to use therefore leads to a short-term spike in CPU and disk use as the server updates each user's password when they next authenticate. Longer term, increasing this setting results in more secure passwords at the expense of longer response times and lower throughput. |
| *Default value*         | 15360                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| *Allowed values*        | An integer.Lower limit: 8.Upper limit: 4194304.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| *Admin action required* | Restart the server for changes to take effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### argon2-parallelism

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | The number of threads to use in parallel to compute a hash.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| *Description*           | The number of threads should not exceed twice the number of physical CPU cores that are dedicated to password hashing. By default, changes to this setting impact only newly created and updated passwords. However, if the rehash-policy is set to always or only-increase, it causes the server to recalculate each user's password hash on their next authentication, and write the new hash to the user's entry on disk. Changing the amount of parallelism to use therefore leads to a short-term spike in CPU and disk use as the server updates each user's password when they next authenticate. Longer term, increasing this setting results in more secure passwords at the expense of much higher CPU consumption and lower throughput. |
| *Default value*         | 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *Allowed values*        | An integer.Lower limit: 1.Upper limit: 32768.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### argon2-salt-length

|                         |                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------ |
| *Synopsis*              | The length of the salt used during the hash.                                         |
| *Description*           | By default, changes to this setting impact only newly created and updated passwords. |
| *Default value*         | 16                                                                                   |
| *Allowed values*        | An integer.Lower limit: 8.Upper limit: 4096.                                         |
| *Multi-valued*          | No                                                                                   |
| *Required*              | No                                                                                   |
| *Admin action required* | None                                                                                 |
| *Advanced*              | No                                                                                   |
| *Read-only*             | No                                                                                   |

### argon2-variant

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | The variant of Argon2 algorithm to use (between I, D and ID).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| *Description*           | Argon2D maximizes resistance to GPU cracking attacks. Argon2I is optimized to resist side-channel attacks. Argon2ID is a hybrid version that combines both approaches and has stronger resistance to attacks, but it's more expensive. By default, changes to this setting impact only newly created and updated passwords. However, if the rehash-policy is set to always or only-increase, it causes the server to recalculate each user's password hash on their next authentication, and writes the new hash to the user's entry on disk. Changing the variant of Argon2 algorithm to use therefore leads to a short-term spike in CPU and disk use as the server updates each user's password when they next authenticate. Longer term, increasing this setting results in more secure passwords at the expense of much higher CPU consumption and lower throughput. |
| *Default value*         | ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| *Allowed values*        | * D: Use Argon2d variant.

* I: Argon2i.

* ID: Argon2id.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### enabled

|                         |                                                                   |
| ----------------------- | ----------------------------------------------------------------- |
| *Synopsis*              | Indicates whether the Password Storage Scheme is enabled for use. |
| *Default value*         | None                                                              |
| *Allowed values*        | truefalse                                                         |
| *Multi-valued*          | No                                                                |
| *Required*              | Yes                                                               |
| *Admin action required* | None                                                              |
| *Advanced*              | No                                                                |
| *Read-only*             | No                                                                |

### rehash-policy

|                         |                                                                                                                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Indicates whether the server should rehash passwords after the cost has been changed.                                                                                            |
| *Description*           | Passwords will be rehashed when a user successfully authenticates. Note that rehashing will increase the write load on the server.                                               |
| *Default value*         | never                                                                                                                                                                            |
| *Allowed values*        | * always: Rehash passwords when the cost is increased or decreased.

* never: Never rehash passwords when the cost changes. Only rehash passwords when the password is modified. |
| *Multi-valued*          | No                                                                                                                                                                               |
| *Required*              | No                                                                                                                                                                               |
| *Admin action required* | None                                                                                                                                                                             |
| *Advanced*              | No                                                                                                                                                                               |
| *Read-only*             | No                                                                                                                                                                               |

## Advanced properties

Use the `--advanced` option to access advanced properties.

### argon2-memory-pool-size

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | The amount of memory dedicated to Argon2 password hashing.                                                                                                                                                                                                                                                                                                                                                                 |
| *Description*           | This amount of memory places an upper limit on the number of argon2 password hashes which can be computed concurrently. Every bind request using argon2 password hashing will acquire memory from this pool, and release it once computation has completed. When the pool is empty, incoming bind requests using argon2 will be paused, waiting for concurrent argon2 computation to finish and return memory to the pool. |
| *Default value*         | 122880                                                                                                                                                                                                                                                                                                                                                                                                                     |
| *Allowed values*        | An integer.Lower limit: 0.Upper limit: 4194304.                                                                                                                                                                                                                                                                                                                                                                            |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                                                                                                                                                                         |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                                         |
| *Admin action required* | Restart the server for changes to take effect.                                                                                                                                                                                                                                                                                                                                                                             |
| *Advanced*              | Yes                                                                                                                                                                                                                                                                                                                                                                                                                        |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                                         |

### java-class

|                         |                                                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the fully-qualified name of the Java class that provides the Argon2 Password Storage Scheme implementation. |
| *Default value*         | org.opends.server.extensions.Argon2PasswordStorageScheme                                                              |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.PasswordStorageScheme                                 |
| *Multi-valued*          | No                                                                                                                    |
| *Required*              | Yes                                                                                                                   |
| *Admin action required* | None                                                                                                                  |
| *Advanced*              | Yes                                                                                                                   |
| *Read-only*             | No                                                                                                                    |

---

---
title: Attribute Cleanup Plugin
description: A pre-parse plugin which can be used to remove and rename attributes in ADD and MODIFY requests before being processed.
component: pingds
version: 8.1
page_id: pingds:configref:objects-attribute-cleanup-plugin
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-attribute-cleanup-plugin.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parent: Parent
  attribute_cleanup_plugin_properties: Attribute Cleanup Plugin properties
  basic_properties: Basic properties
  enabled: enabled
  java-class: java-class
  remove-inbound-attributes: remove-inbound-attributes
  rename-inbound-attributes: rename-inbound-attributes
  advanced_properties: Advanced properties
  invoke-for-internal-operations: invoke-for-internal-operations
  plugin-type: plugin-type
---

# Attribute Cleanup Plugin

A pre-parse plugin which can be used to remove and rename attributes in ADD and MODIFY requests before being processed.

This plugin should be used in order maintain interoperability with client applications which attempt to update attributes in a way which is incompatible with LDAPv3 or PingDS. For example, this plugin may be used in order to remove changes to operational attributes such as modifiersName, creatorsName, modifyTimestamp, and createTimestamp (Sun DSEE chaining does this).

## Parent

The Attribute Cleanup Plugin object inherits from [Plugin](objects-plugin.html).

## Attribute Cleanup Plugin properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                                                                                                                                              | Advanced Properties                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [enabled](#enabled) [java-class](#java-class) [remove-inbound-attributes](#remove-inbound-attributes) [rename-inbound-attributes](#rename-inbound-attributes) | [invoke-for-internal-operations](#invoke-for-internal-operations) [plugin-type](#plugin-type) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### enabled

|                         |                                                   |
| ----------------------- | ------------------------------------------------- |
| *Synopsis*              | Indicates whether the plug-in is enabled for use. |
| *Default value*         | None                                              |
| *Allowed values*        | truefalse                                         |
| *Multi-valued*          | No                                                |
| *Required*              | Yes                                               |
| *Admin action required* | None                                              |
| *Advanced*              | No                                                |
| *Read-only*             | No                                                |

### java-class

|                         |                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the fully-qualified name of the Java class that provides the plug-in implementation. |
| *Default value*         | org.opends.server.plugins.AttributeCleanupPlugin                                               |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.plugin.DirectoryServerPlugin   |
| *Multi-valued*          | No                                                                                             |
| *Required*              | Yes                                                                                            |
| *Admin action required* | None                                                                                           |
| *Advanced*              | No                                                                                             |
| *Read-only*             | No                                                                                             |

### remove-inbound-attributes

|                         |                                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------- |
| *Synopsis*              | A list of attributes which should be removed from incoming add or modify requests. |
| *Default value*         | No attributes will be removed                                                      |
| *Allowed values*        | A string.                                                                          |
| *Multi-valued*          | Yes                                                                                |
| *Required*              | No                                                                                 |
| *Admin action required* | None                                                                               |
| *Advanced*              | No                                                                                 |
| *Read-only*             | No                                                                                 |

### rename-inbound-attributes

|                         |                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------- |
| *Synopsis*              | A list of attributes which should be renamed in incoming add or modify requests. |
| *Default value*         | No attributes will be renamed                                                    |
| *Allowed values*        | An attribute name mapping.                                                       |
| *Multi-valued*          | Yes                                                                              |
| *Required*              | No                                                                               |
| *Admin action required* | None                                                                             |
| *Advanced*              | No                                                                               |
| *Read-only*             | No                                                                               |

## Advanced properties

Use the `--advanced` option to access advanced properties.

### invoke-for-internal-operations

|                         |                                                                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Indicates whether the plug-in should be invoked for internal operations.                                                                                                  |
| *Description*           | Any plug-in that can be invoked for internal operations must ensure that it does not create any new internal operations that can cause the same plug-in to be re-invoked. |
| *Default value*         | false                                                                                                                                                                     |
| *Allowed values*        | truefalse                                                                                                                                                                 |
| *Multi-valued*          | No                                                                                                                                                                        |
| *Required*              | No                                                                                                                                                                        |
| *Admin action required* | None                                                                                                                                                                      |
| *Advanced*              | Yes                                                                                                                                                                       |
| *Read-only*             | No                                                                                                                                                                        |

### plugin-type

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the set of plug-in types for the plug-in, which specifies the times at which the plug-in is invoked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| *Default value*         | preparseaddpreparsemodify                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| *Allowed values*        | * initialization: Invoked at the initialization of the directory server.

* intermediateresponse: Invoked before sending an intermediate response message to the client.

* ldifimport: Invoked for each entry read during an LDIF import.

* ldifimportbegin: Invoked at the beginning of an LDIF import session.

* ldifimportend: Invoked at the end of an LDIF import session.

* postcommitadd: Invoked after completing post-commit processing for an add operation.

* postcommitdelete: Invoked after completing post-commit processing for a delete operation.

* postcommitmodify: Invoked after completing post-commit processing for a modify operation.

* postcommitmodifydn: Invoked after completing post-commit processing for a modify DN operation.

* postconnect: Invoked whenever a new connection is established to the server.

* postdisconnect: Invoked whenever an existing connection is terminated (by either the client or the server).

* postoperationabandon: Invoked after completing the abandon processing.

* postoperationadd: Invoked after completing the core add processing but before sending the response to the client.

* postoperationbind: Invoked after completing the core bind processing but before sending the response to the client.

* postoperationcompare: Invoked after completing the core compare processing but before sending the response to the client.

* postoperationdelete: Invoked after completing the core delete processing but before sending the response to the client.

* postoperationextended: Invoked after completing the core extended processing but before sending the response to the client.

* postoperationmodify: Invoked after completing the core modify processing but before sending the response to the client.

* postoperationmodifydn: Invoked after completing the core modify DN processing but before sending the response to the client.

* postoperationsearch: Invoked after completing the core search processing but before sending the response to the client.

* postoperationunbind: Invoked after completing the unbind processing.

* postresponseadd: Invoked after sending the add response to the client.

* postresponsebind: Invoked after sending the bind response to the client.

* postresponsecompare: Invoked after sending the compare response to the client.

* postresponsedelete: Invoked after sending the delete response to the client.

* postresponseextended: Invoked after sending the extended response to the client.

* postresponsemodify: Invoked after sending the modify response to the client.

* postresponsemodifydn: Invoked after sending the modify DN response to the client.

* postresponsesearch: Invoked after sending the search result done message to the client.

* postsynchronizationadd: Invoked after completing post-synchronization processing for an add operation.

* postsynchronizationdelete: Invoked after completing post-synchronization processing for a delete operation.

* postsynchronizationmodify: Invoked after completing post-synchronization processing for a modify operation.

* postsynchronizationmodifydn: Invoked after completing post-synchronization processing for a modify DN operation.

* preoperationadd: Invoked prior to performing the core add processing.

* preoperationbind: Invoked prior to performing the core bind processing.

* preoperationcompare: Invoked prior to performing the core compare processing.

* preoperationdelete: Invoked prior to performing the core delete processing.

* preoperationextended: Invoked prior to performing the core extended processing.

* preoperationmodify: Invoked prior to performing the core modify processing.

* preoperationmodifydn: Invoked prior to performing the core modify DN processing.

* preoperationsearch: Invoked prior to performing the core search processing.

* preparseabandon: Invoked prior to parsing an abandon request.

* preparseadd: Invoked prior to parsing an add request.

* preparsebind: Invoked prior to parsing a bind request.

* preparsecompare: Invoked prior to parsing a compare request.

* preparsedelete: Invoked prior to parsing a delete request.

* preparseextended: Invoked prior to parsing an extended request.

* preparsemodify: Invoked prior to parsing a modify request.

* preparsemodifydn: Invoked prior to parsing a modify DN request.

* preparsesearch: Invoked prior to parsing a search request.

* preparseunbind: Invoked prior to parsing an unbind request.

* searchresultentry: Invoked before sending a search result entry to the client.

* searchresultreference: Invoked before sending a search result reference to the client.

* shutdown: Invoked during a graceful directory server shutdown.

* startup: Invoked during the directory server startup process.

* subordinatedelete: Invoked in the course of deleting a subordinate entry of a delete operation.

* subordinatemodifydn: Invoked in the course of moving or renaming an entry subordinate to the target of a modify DN operation. |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| *Required*              | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| *Admin action required* | The object must be disabled and re-enabled for changes to take effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *Advanced*              | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

---

---
title: Attribute Value Password Validator
description: The Attribute Value Password Validator attempts to determine whether a proposed password is acceptable for use by checking whether the password matches or contains attribute values from the user's entry.
component: pingds
version: 8.1
page_id: pingds:configref:objects-attribute-value-password-validator
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-attribute-value-password-validator.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parent: Parent
  attribute_value_password_validator_properties: Attribute Value Password Validator properties
  basic_properties: Basic properties
  check-substrings: check-substrings
  enabled: enabled
  match-attribute: match-attribute
  min-substring-length: min-substring-length
  test-reversed-password: test-reversed-password
  advanced_properties: Advanced properties
  java-class: java-class
---

# Attribute Value Password Validator

The Attribute Value Password Validator attempts to determine whether a proposed password is acceptable for use by checking whether the password matches or contains attribute values from the user's entry.

It can be configured to look in all attributes or in a specified subset of attributes.

## Parent

The Attribute Value Password Validator object inherits from [Password Validator](objects-password-validator.html).

## Attribute Value Password Validator properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                                                                                                                                                                              | Advanced Properties       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| [check-substrings](#check-substrings) [enabled](#enabled) [match-attribute](#match-attribute) [min-substring-length](#min-substring-length) [test-reversed-password](#test-reversed-password) | [java-class](#java-class) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### check-substrings

|                         |                                                                                                                                                                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Indicates whether this password validator is to match portions of the password string against attribute values and portions of attribute values against the password string.                                                     |
| *Description*           | If "false" then only match the entire password against attribute values; otherwise ("true"), check whether the password contains portions of attribute values and whether the attribute values contain portions of the password. |
| *Default value*         | true                                                                                                                                                                                                                             |
| *Allowed values*        | truefalse                                                                                                                                                                                                                        |
| *Multi-valued*          | No                                                                                                                                                                                                                               |
| *Required*              | No                                                                                                                                                                                                                               |
| *Admin action required* | None                                                                                                                                                                                                                             |
| *Advanced*              | No                                                                                                                                                                                                                               |
| *Read-only*             | No                                                                                                                                                                                                                               |

### enabled

|                         |                                                              |
| ----------------------- | ------------------------------------------------------------ |
| *Synopsis*              | Indicates whether the password validator is enabled for use. |
| *Default value*         | None                                                         |
| *Allowed values*        | truefalse                                                    |
| *Multi-valued*          | No                                                           |
| *Required*              | Yes                                                          |
| *Admin action required* | None                                                         |
| *Advanced*              | No                                                           |
| *Read-only*             | No                                                           |

### match-attribute

|                         |                                                                                                                                                                                                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *Synopsis*              | Specifies the name(s) of the attribute(s) whose values should be checked to determine whether they match the provided password. If no values are provided, then the server checks if the proposed password matches the value of any attribute in the user's entry. |
| *Default value*         | All attributes in the user entry will be checked.                                                                                                                                                                                                                  |
| *Allowed values*        | The name of an attribute type defined in the LDAP schema.                                                                                                                                                                                                          |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                                |
| *Required*              | No                                                                                                                                                                                                                                                                 |
| *Admin action required* | None                                                                                                                                                                                                                                                               |
| *Advanced*              | No                                                                                                                                                                                                                                                                 |
| *Read-only*             | No                                                                                                                                                                                                                                                                 |

### min-substring-length

|                         |                                                                                                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Indicates the minimal length (inclusive) of the substring within the password in case substring checking is enabled.                                              |
| *Description*           | If "check-substrings" option is set to true, then this parameter defines the length (inclusive) of the smallest word which should be used for substring matching. |
| *Default value*         | 5                                                                                                                                                                 |
| *Allowed values*        | An integer.Lower limit: 3.                                                                                                                                        |
| *Multi-valued*          | No                                                                                                                                                                |
| *Required*              | No                                                                                                                                                                |
| *Admin action required* | None                                                                                                                                                              |
| *Advanced*              | No                                                                                                                                                                |
| *Read-only*             | No                                                                                                                                                                |

### test-reversed-password

|                         |                                                                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Indicates whether this password validator should test the reversed value of the provided password as well as the order in which it was given. |
| *Default value*         | None                                                                                                                                          |
| *Allowed values*        | truefalse                                                                                                                                     |
| *Multi-valued*          | No                                                                                                                                            |
| *Required*              | Yes                                                                                                                                           |
| *Admin action required* | None                                                                                                                                          |
| *Advanced*              | No                                                                                                                                            |
| *Read-only*             | No                                                                                                                                            |

## Advanced properties

Use the `--advanced` option to access advanced properties.

### java-class

|                         |                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the fully-qualified name of the Java class that provides the password validator implementation. |
| *Default value*         | org.opends.server.extensions.AttributeValuePasswordValidator                                              |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.PasswordValidator                         |
| *Multi-valued*          | No                                                                                                        |
| *Required*              | Yes                                                                                                       |
| *Admin action required* | The object must be disabled and re-enabled for changes to take effect.                                    |
| *Advanced*              | Yes                                                                                                       |
| *Read-only*             | No                                                                                                        |

---

---
title: Authentication Policy
description: This is an abstract object type that cannot be instantiated.
component: pingds
version: 8.1
page_id: pingds:configref:objects-authentication-policy
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-authentication-policy.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  authentication_policies: Authentication Policies
  dependencies: Dependencies
  authentication_policy_properties: Authentication Policy properties
  basic_properties: Basic properties
  java-class: java-class
---

# Authentication Policy

*This is an abstract object type that cannot be instantiated.*

Authentication Policies define the policies which should be used for authenticating users and managing the password and other account related state.

## Authentication Policies

The following Authentication Policies are available:

* [LDAP Pass Through Authentication Policy](objects-ldap-pass-through-authentication-policy.html)

* [Password Policy](objects-password-policy.html)

These Authentication Policies inherit the properties described below.

## Dependencies

The following objects depend on Authentication Policies:

* [Global Configuration](objects-global.html)

## Authentication Policy properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties          |
| ------------------------- |
| [java-class](#java-class) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### java-class

|                         |                                                                                                               |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the fully-qualified name of the Java class which provides the Authentication Policy implementation. |
| *Default value*         | None                                                                                                          |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.AuthenticationPolicyFactory                   |
| *Multi-valued*          | No                                                                                                            |
| *Required*              | Yes                                                                                                           |
| *Admin action required* | The object must be disabled and re-enabled for changes to take effect.                                        |
| *Advanced*              | No                                                                                                            |
| *Read-only*             | No                                                                                                            |

---

---
title: Backend
description: This is an abstract object type that cannot be instantiated.
component: pingds
version: 8.1
page_id: pingds:configref:objects-backend
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-backend.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  backends: Backends
  backend_properties: Backend properties
  basic_properties: Basic properties
  backend-id: backend-id
  enabled: enabled
  java-class: java-class
---

# Backend

*This is an abstract object type that cannot be instantiated.*

Backends are responsible for providing access to the underlying data presented by the server.

The data may be stored locally in an embedded database, remotely in an external system, or generated on the fly (for example, calculated from other information that is available).

## Backends

The following Backends are available:

* [Local Backend](objects-local-backend.html)

* [Proxy Backend](objects-proxy-backend.html)

These Backends inherit the properties described below.

## Backend properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                                                        |
| ----------------------------------------------------------------------- |
| [backend-id](#backend-id) [enabled](#enabled) [java-class](#java-class) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### backend-id

|                         |                                                                                                                                                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies a name to identify the associated backend.                                                                                                                                                 |
| *Description*           | The name must be unique among all backends in the server. The backend ID may not be altered after the backend is created in the server.                                                              |
| *Default value*         | None                                                                                                                                                                                                 |
| *Allowed values*        | A string.                                                                                                                                                                                            |
| *Multi-valued*          | No                                                                                                                                                                                                   |
| *Required*              | Yes                                                                                                                                                                                                  |
| *Admin action required* | NoneNo base entry has been created as part of this process. A base entry needs to be created before adding further entries to the backend. Please refer to the documentation to create a base entry. |
| *Advanced*              | No                                                                                                                                                                                                   |
| *Read-only*             | Yes                                                                                                                                                                                                  |

### enabled

|                         |                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| *Synopsis*              | Indicates whether the backend is enabled in the server.                                       |
| *Description*           | If a backend is not enabled, then its contents are not accessible when processing operations. |
| *Default value*         | None                                                                                          |
| *Allowed values*        | truefalse                                                                                     |
| *Multi-valued*          | No                                                                                            |
| *Required*              | Yes                                                                                           |
| *Admin action required* | None                                                                                          |
| *Advanced*              | No                                                                                            |
| *Read-only*             | No                                                                                            |

### java-class

|                         |                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the fully-qualified name of the Java class that provides the backend implementation. |
| *Default value*         | None                                                                                           |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.Backend                        |
| *Multi-valued*          | No                                                                                             |
| *Required*              | Yes                                                                                            |
| *Admin action required* | The object must be disabled and re-enabled for changes to take effect.                         |
| *Advanced*              | No                                                                                             |
| *Read-only*             | No                                                                                             |

---

---
title: Backend Index
description: Backend Indexes are used to store information that makes it possible to locate entries very quickly when processing search operations.
component: pingds
version: 8.1
page_id: pingds:configref:objects-backend-index
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-backend-index.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  dependencies: Dependencies
  backend_index_properties: Backend Index properties
  basic_properties: Basic properties
  attribute: attribute
  big-index-extensible-matching-rule: big-index-extensible-matching-rule
  big-index-included-attribute-value: big-index-included-attribute-value
  confidentiality-enabled: confidentiality-enabled
  index-extensible-matching-rule: index-extensible-matching-rule
  index-type: index-type
  ttl-age: ttl-age
  ttl-enabled: ttl-enabled
  advanced_properties: Advanced properties
  index-entry-limit: index-entry-limit
  substring-length: substring-length
---

# Backend Index

Backend Indexes are used to store information that makes it possible to locate entries very quickly when processing search operations.

Indexing is performed on a per-attribute level and different types of indexing may be performed for different kinds of attributes, based on how they are expected to be accessed during search operations.

## Dependencies

The following objects depend on Backend Indexes:

* [Pluggable Backend](objects-pluggable-backend.html)

## Backend Index properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                                                                                                                                                                                                                                                                                                                                                            | Advanced Properties                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [attribute](#attribute) [big-index-extensible-matching-rule](#big-index-extensible-matching-rule) [big-index-included-attribute-value](#big-index-included-attribute-value) [confidentiality-enabled](#confidentiality-enabled) [index-extensible-matching-rule](#index-extensible-matching-rule) [index-type](#index-type) [ttl-age](#ttl-age) [ttl-enabled](#ttl-enabled) | [index-entry-limit](#index-entry-limit) [substring-length](#substring-length) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### attribute

|                         |                                                                              |
| ----------------------- | ---------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the name of the attribute for which the index is to be maintained. |
| *Default value*         | None                                                                         |
| *Allowed values*        | The name of an attribute type defined in the LDAP schema.                    |
| *Multi-valued*          | No                                                                           |
| *Required*              | Yes                                                                          |
| *Admin action required* | None                                                                         |
| *Advanced*              | No                                                                           |
| *Read-only*             | Yes                                                                          |

### big-index-extensible-matching-rule

|                         |                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------- |
| *Synopsis*              | The extensible matching rule in a big index.                                                   |
| *Description*           | An extensible matching rule must be specified using either LOCALE or OID of the matching rule. |
| *Default value*         | No big index extensible matching rules will be indexed.                                        |
| *Allowed values*        | A Locale or an OID.                                                                            |
| *Multi-valued*          | Yes                                                                                            |
| *Required*              | No                                                                                             |
| *Admin action required* | NoneThe index must be rebuilt before it will reflect the new value.                            |
| *Advanced*              | No                                                                                             |
| *Read-only*             | No                                                                                             |

### big-index-included-attribute-value

|                         |                                                                                                                |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | An attribute value which should be indexed in any big indexes.                                                 |
| *Description*           | Restricts the set of attribute values indexed by big indexes. All attribute values will be indexed by default. |
| *Default value*         | All attribute values will be indexed.                                                                          |
| *Allowed values*        | A string.                                                                                                      |
| *Multi-valued*          | Yes                                                                                                            |
| *Required*              | No                                                                                                             |
| *Admin action required* | NoneThe index must be rebuilt before it will reflect the new attribute value(s).                               |
| *Advanced*              | No                                                                                                             |
| *Read-only*             | No                                                                                                             |

### confidentiality-enabled

|                         |                                                                                                                                                                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies whether contents of the index should be confidential.                                                                                                                                                                                                                 |
| *Description*           | Setting the flag to true will hash keys for equality type indexes using SHA-1 and encrypt the list of entries matching a substring key for substring indexes.                                                                                                                   |
| *Default value*         | false                                                                                                                                                                                                                                                                           |
| *Allowed values*        | truefalse                                                                                                                                                                                                                                                                       |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                              |
| *Required*              | No                                                                                                                                                                                                                                                                              |
| *Admin action required* | NoneIf the index for the attribute must be protected for security purposes and values for that attribute already exist in the database, the index must be rebuilt before it will be accurate. The property cannot be set on a backend for which confidentiality is not enabled. |
| *Advanced*              | No                                                                                                                                                                                                                                                                              |
| *Read-only*             | No                                                                                                                                                                                                                                                                              |

### index-extensible-matching-rule

|                         |                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------- |
| *Synopsis*              | The extensible matching rule in an extensible index.                                           |
| *Description*           | An extensible matching rule must be specified using either LOCALE or OID of the matching rule. |
| *Default value*         | No extensible matching rules will be indexed.                                                  |
| *Allowed values*        | A Locale or an OID.                                                                            |
| *Multi-valued*          | Yes                                                                                            |
| *Required*              | No                                                                                             |
| *Admin action required* | NoneThe index must be rebuilt before it will reflect the new value.                            |
| *Advanced*              | No                                                                                             |
| *Read-only*             | No                                                                                             |

### index-type

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the type(s) of indexing that should be performed for the associated attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| *Description*           | For equality, presence, and substring index types, the associated attribute type must have a corresponding matching rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| *Default value*         | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| *Allowed values*        | * approximate: This index type is used to improve the efficiency of searches using approximate matching search filters.

* big-equality: This index type is used to perform efficient equality filter queries against attributes with few unique values.

* big-extensible: This index type is used to improve the efficiency of searches using extensible matching rule search filters against attributes with few unique values.

* equality: This index type is used to improve the efficiency of searches using equality search filters.

* extensible: This index type is used to improve the efficiency of searches using extensible matching search filters.

* ordering: This index type is used to improve the efficiency of searches using "greater than or equal to" or "less then or equal to" search filters.

* presence: This index type is used to improve the efficiency of searches using the presence search filters.

* substring: This index type is used to improve the efficiency of searches using substring search filters. |
| *Multi-valued*          | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *Required*              | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *Admin action required* | NoneIf any new index types are added for an attribute, and values for that attribute already exist in the database, the index must be rebuilt before it will be accurate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### ttl-age

|                         |                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | After reaching the time of the indexed attribute plus this age, PingDS considers the entry expired and ready for deletion. Use a low setting to quickly delete entries with expiration timestamps, for example, with coreTokenExpirationDate. Use a high setting to delay deleting entries with "last use" timestamps, for example, with lastLoginTime. |
| *Default value*         | 0s                                                                                                                                                                                                                                                                                                                                                      |
| *Allowed values*        | Uses [duration syntax](duration-syntax.html).Lower limit: 0 milliseconds.                                                                                                                                                                                                                                                                               |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                                                                                                      |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                      |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                                    |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                      |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                      |

### ttl-enabled

|                         |                                             |
| ----------------------- | ------------------------------------------- |
| *Synopsis*              | Enable TTL for this generalized time index. |
| *Default value*         | false                                       |
| *Allowed values*        | truefalse                                   |
| *Multi-valued*          | No                                          |
| *Required*              | No                                          |
| *Admin action required* | None                                        |
| *Advanced*              | No                                          |
| *Read-only*             | No                                          |

## Advanced properties

Use the `--advanced` option to access advanced properties.

### index-entry-limit

|                         |                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the maximum number of entries that are allowed to match a given index key before that particular index key is no longer maintained.                                                                                                                                                                                                               |
| *Description*           | This is analogous to the ALL IDs threshold in the Sun Java System Directory Server. If this is specified, its value overrides the JE backend-wide configuration. For no limit, use 0 for the value. Changing the index entry limit significantly can result in serious performance degradation. Please read the documentation before changing this setting. |
| *Default value*         | 4000                                                                                                                                                                                                                                                                                                                                                        |
| *Allowed values*        | An integer.Lower limit: 0.Upper limit: 2147483647.                                                                                                                                                                                                                                                                                                          |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                                                                                                          |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                          |
| *Admin action required* | NoneIf any index keys have already reached this limit, indexes must be rebuilt before they will be allowed to use the new limit.                                                                                                                                                                                                                            |
| *Advanced*              | Yes                                                                                                                                                                                                                                                                                                                                                         |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                          |

### substring-length

|                         |                                                                     |
| ----------------------- | ------------------------------------------------------------------- |
| *Synopsis*              | The length of substrings in a substring index.                      |
| *Default value*         | 6                                                                   |
| *Allowed values*        | An integer.Lower limit: 3.                                          |
| *Multi-valued*          | No                                                                  |
| *Required*              | No                                                                  |
| *Admin action required* | NoneThe index must be rebuilt before it will reflect the new value. |
| *Advanced*              | Yes                                                                 |
| *Read-only*             | No                                                                  |

---

---
title: Backend VLV Index
description: Backend VLV Indexes are used to store information about a specific search request that makes it possible to efficiently process them using the VLV control.
component: pingds
version: 8.1
page_id: pingds:configref:objects-backend-vlv-index
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-backend-vlv-index.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  dependencies: Dependencies
  backend_vlv_index_properties: Backend VLV Index properties
  basic_properties: Basic properties
  base-dn: base-dn
  filter: filter
  name: name
  scope: scope
  sort-order: sort-order
---

# Backend VLV Index

Backend VLV Indexes are used to store information about a specific search request that makes it possible to efficiently process them using the VLV control.

A VLV index effectively notifies the server that a virtual list view, with specific query and sort parameters, will be performed. This index also allows the server to collect and maintain the information required to make using the virtual list view faster.

## Dependencies

The following objects depend on Backend VLV Indexes:

* [Pluggable Backend](objects-pluggable-backend.html)

## Backend VLV Index properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                                                                              |
| --------------------------------------------------------------------------------------------- |
| [base-dn](#base-dn) [filter](#filter) [name](#name) [scope](#scope) [sort-order](#sort-order) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### base-dn

|                         |                                                                       |
| ----------------------- | --------------------------------------------------------------------- |
| *Synopsis*              | Specifies the base DN used in the search query that is being indexed. |
| *Default value*         | None                                                                  |
| *Allowed values*        | A valid DN.                                                           |
| *Multi-valued*          | No                                                                    |
| *Required*              | Yes                                                                   |
| *Admin action required* | NoneThe index must be rebuilt after modifying this property.          |
| *Advanced*              | No                                                                    |
| *Read-only*             | No                                                                    |

### filter

|                         |                                                                    |
| ----------------------- | ------------------------------------------------------------------ |
| *Synopsis*              | Specifies the LDAP filter used in the query that is being indexed. |
| *Default value*         | None                                                               |
| *Allowed values*        | A valid LDAP search filter.                                        |
| *Multi-valued*          | No                                                                 |
| *Required*              | Yes                                                                |
| *Admin action required* | NoneThe index must be rebuilt after modifying this property.       |
| *Advanced*              | No                                                                 |
| *Read-only*             | No                                                                 |

### name

|                         |                                                                      |
| ----------------------- | -------------------------------------------------------------------- |
| *Synopsis*              | Specifies a unique name for this VLV index.                          |
| *Default value*         | None                                                                 |
| *Allowed values*        | A string.                                                            |
| *Multi-valued*          | No                                                                   |
| *Required*              | Yes                                                                  |
| *Admin action required* | NoneThe VLV index name cannot be altered after the index is created. |
| *Advanced*              | No                                                                   |
| *Read-only*             | Yes                                                                  |

### scope

|                         |                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the LDAP scope of the query that is being indexed.                                                                                                                                                                                                                                                                                      |
| *Default value*         | None                                                                                                                                                                                                                                                                                                                                              |
| *Allowed values*        | * single-level: Search the immediate children of the base object but do not include any of their descendants or the base object itself.

* subordinate-subtree: Search the entire subtree below the base object but do not include the base object itself.

* whole-subtree: Search the base object and the entire subtree below the base object. |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                                                                                                |
| *Required*              | Yes                                                                                                                                                                                                                                                                                                                                               |
| *Admin action required* | NoneThe index must be rebuilt after modifying this property.                                                                                                                                                                                                                                                                                      |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                |

### sort-order

|                         |                                                                                                                                                                                                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the names of the attributes that are used to sort the entries for the query being indexed.                                                                                                                                                              |
| *Description*           | Multiple attributes can be used to determine the sort order by listing the attribute names from highest to lowest precedence. Optionally, + or - can be prefixed to the attribute name to sort the attribute in ascending order or descending order respectively. |
| *Default value*         | None                                                                                                                                                                                                                                                              |
| *Allowed values*        | Valid attribute types defined in the schema, separated by a space and optionally prefixed by + or -.                                                                                                                                                              |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                |
| *Required*              | Yes                                                                                                                                                                                                                                                               |
| *Admin action required* | NoneThe index must be rebuilt after modifying this property.                                                                                                                                                                                                      |
| *Advanced*              | No                                                                                                                                                                                                                                                                |
| *Read-only*             | No                                                                                                                                                                                                                                                                |

---

---
title: Base64 Password Storage Scheme (LEGACY)
description: "LEGACY since 7.0.0: is insecure. Alternative: A strong hash-based scheme such as one of the schemes enabled by default."
component: pingds
version: 8.1
page_id: pingds:configref:objects-base64-password-storage-scheme
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-base64-password-storage-scheme.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parent: Parent
  base64_password_storage_scheme_properties: Base64 Password Storage Scheme properties
  basic_properties: Basic properties
  enabled: enabled
  advanced_properties: Advanced properties
  java-class: java-class
---

# Base64 Password Storage Scheme (LEGACY)

|   |                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------- |
|   | LEGACY since 7.0.0: is insecure. Alternative: A strong hash-based scheme such as one of the schemes enabled by default. |

The Base64 Password Storage Scheme provides a mechanism for encoding user passwords using the BASE64 encoding mechanism.

This scheme contains only an implementation for the user password syntax, with a storage scheme name of "BASE64". The Base64 Password Storage Scheme merely obscures the password so that the clear-text password is not available to casual observers. However, it offers no real protection and should only be used if there are client applications that specifically require this capability.

## Parent

The Base64 Password Storage Scheme object inherits from [Password Storage Scheme](objects-password-storage-scheme.html).

## Base64 Password Storage Scheme properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties    | Advanced Properties       |
| ------------------- | ------------------------- |
| [enabled](#enabled) | [java-class](#java-class) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### enabled

|                         |                                                                   |
| ----------------------- | ----------------------------------------------------------------- |
| *Synopsis*              | Indicates whether the Password Storage Scheme is enabled for use. |
| *Default value*         | None                                                              |
| *Allowed values*        | truefalse                                                         |
| *Multi-valued*          | No                                                                |
| *Required*              | Yes                                                               |
| *Admin action required* | None                                                              |
| *Advanced*              | No                                                                |
| *Read-only*             | No                                                                |

## Advanced properties

Use the `--advanced` option to access advanced properties.

### java-class

|                         |                                                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the fully-qualified name of the Java class that provides the Base64 Password Storage Scheme implementation. |
| *Default value*         | org.opends.server.extensions.Base64PasswordStorageScheme                                                              |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.PasswordStorageScheme                                 |
| *Multi-valued*          | No                                                                                                                    |
| *Required*              | Yes                                                                                                                   |
| *Admin action required* | None                                                                                                                  |
| *Advanced*              | Yes                                                                                                                   |
| *Read-only*             | No                                                                                                                    |

---

---
title: Bcrypt Password Storage Scheme
description: The Bcrypt Password Storage Scheme provides a mechanism for encoding user passwords using the bcrypt message digest algorithm.
component: pingds
version: 8.1
page_id: pingds:configref:objects-bcrypt-password-storage-scheme
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-bcrypt-password-storage-scheme.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parent: Parent
  bcrypt_password_storage_scheme_properties: Bcrypt Password Storage Scheme properties
  basic_properties: Basic properties
  bcrypt-cost: bcrypt-cost
  enabled: enabled
  rehash-policy: rehash-policy
  version: version
  advanced_properties: Advanced properties
  java-class: java-class
  remote-password-hashing-base-uri: remote-password-hashing-base-uri
  remote-password-hashing-connection-timeout: remote-password-hashing-connection-timeout
  remote-password-hashing-enabled: remote-password-hashing-enabled
  remote-password-hashing-max-connections: remote-password-hashing-max-connections
  remote-password-hashing-request-timeout: remote-password-hashing-request-timeout
---

# Bcrypt Password Storage Scheme

The Bcrypt Password Storage Scheme provides a mechanism for encoding user passwords using the bcrypt message digest algorithm.

This scheme contains an implementation for the user password syntax, with a storage scheme name of "BCRYPT".

## Parent

The Bcrypt Password Storage Scheme object inherits from [Cost Based Password Storage Scheme](objects-cost-based-password-storage-scheme.html).

## Bcrypt Password Storage Scheme properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties                                                                                    | Advanced Properties                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bcrypt-cost](#bcrypt-cost) [enabled](#enabled) [rehash-policy](#rehash-policy) [version](#version) | [java-class](#java-class) [remote-password-hashing-base-uri](#remote-password-hashing-base-uri) [remote-password-hashing-connection-timeout](#remote-password-hashing-connection-timeout) [remote-password-hashing-enabled](#remote-password-hashing-enabled) [remote-password-hashing-max-connections](#remote-password-hashing-max-connections) [remote-password-hashing-request-timeout](#remote-password-hashing-request-timeout) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### bcrypt-cost

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | The cost parameter specifies a key expansion iteration count as a power of two. A default value of 12 (2^12 iterations) is considered in 2016 as a reasonable balance between responsiveness and security for regular users.                                                                                                                                                                                                                                                                                                                                                                                           |
| *Description*           | By default, changes to this setting impact only newly created and updated passwords. However, if the rehash-policy is set to only-increase or only-decrease, it may cause the server to recalculate the user's password hash on their next authentication, and write the new hash to the user's entry on disk. Changing the number of iterations therefore leads to a short-term spike in CPU and disk use as the server updates each user's password when they next authenticate. Longer term, increasing this setting results in more secure passwords at the expense of longer response times and lower throughput. |
| *Default value*         | 12                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| *Allowed values*        | An integer.Lower limit: 4.Upper limit: 30.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### enabled

|                         |                                                                   |
| ----------------------- | ----------------------------------------------------------------- |
| *Synopsis*              | Indicates whether the Password Storage Scheme is enabled for use. |
| *Default value*         | None                                                              |
| *Allowed values*        | truefalse                                                         |
| *Multi-valued*          | No                                                                |
| *Required*              | Yes                                                               |
| *Admin action required* | None                                                              |
| *Advanced*              | No                                                                |
| *Read-only*             | No                                                                |

### rehash-policy

|                         |                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Indicates whether the server should rehash passwords after the cost has been changed.                                                                                                                                                                                                                                                                                  |
| *Description*           | Passwords will be rehashed when a user successfully authenticates. Note that rehashing will increase the write load on the server.                                                                                                                                                                                                                                     |
| *Default value*         | never                                                                                                                                                                                                                                                                                                                                                                  |
| *Allowed values*        | * never: Never rehash passwords when the cost changes. Only rehash passwords when the password is modified.

* only-decrease: Only rehash passwords when the cost has been decreased (downgrade the security of the hashed password).

* only-increase: Only rehash passwords when the cost has been increased (do not downgrade the security of the hashed password). |
| *Multi-valued*          | No                                                                                                                                                                                                                                                                                                                                                                     |
| *Required*              | No                                                                                                                                                                                                                                                                                                                                                                     |
| *Admin action required* | None                                                                                                                                                                                                                                                                                                                                                                   |
| *Advanced*              | No                                                                                                                                                                                                                                                                                                                                                                     |
| *Read-only*             | No                                                                                                                                                                                                                                                                                                                                                                     |

### version

|                         |                                                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Indicates the bcrypt algorithm version to use.                                                                                                             |
| *Description*           | Password hashes are prefixed with a version. The bcrypt authors have defined two versions so far, to fix a problem in the original OpenBSD implementation. |
| *Default value*         | 2b                                                                                                                                                         |
| *Allowed values*        | The value can either be '2a' for the original OpenBSD version, or '2b' for the fixed version from 2014.                                                    |
| *Multi-valued*          | No                                                                                                                                                         |
| *Required*              | No                                                                                                                                                         |
| *Admin action required* | None                                                                                                                                                       |
| *Advanced*              | No                                                                                                                                                         |
| *Read-only*             | No                                                                                                                                                         |

## Advanced properties

Use the `--advanced` option to access advanced properties.

### java-class

|                         |                                                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the fully-qualified name of the Java class that provides the Bcrypt Password Storage Scheme implementation. |
| *Default value*         | org.opends.server.extensions.BcryptPasswordStorageScheme                                                              |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.PasswordStorageScheme                                 |
| *Multi-valued*          | No                                                                                                                    |
| *Required*              | Yes                                                                                                                   |
| *Admin action required* | None                                                                                                                  |
| *Advanced*              | Yes                                                                                                                   |
| *Read-only*             | No                                                                                                                    |

### remote-password-hashing-base-uri

|                         |                                                                         |
| ----------------------- | ----------------------------------------------------------------------- |
| *Synopsis*              | Specifies the base URI to connect to the password hashing microservice. |
| *Default value*         | None                                                                    |
| *Allowed values*        | A string.                                                               |
| *Multi-valued*          | No                                                                      |
| *Required*              | No                                                                      |
| *Admin action required* | None                                                                    |
| *Advanced*              | Yes                                                                     |
| *Read-only*             | No                                                                      |

### remote-password-hashing-connection-timeout

|                         |                                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the timeout to use when connecting to the password hashing microservice. |
| *Default value*         | 10 s                                                                               |
| *Allowed values*        | Uses [duration syntax](duration-syntax.html).Lower limit: 0 seconds.               |
| *Multi-valued*          | No                                                                                 |
| *Required*              | No                                                                                 |
| *Admin action required* | None                                                                               |
| *Advanced*              | Yes                                                                                |
| *Read-only*             | No                                                                                 |

### remote-password-hashing-enabled

|                         |                                                                             |
| ----------------------- | --------------------------------------------------------------------------- |
| *Synopsis*              | Specifies whether to delegate password hashing to a dedicated microservice. |
| *Default value*         | false                                                                       |
| *Allowed values*        | truefalse                                                                   |
| *Multi-valued*          | No                                                                          |
| *Required*              | No                                                                          |
| *Admin action required* | None                                                                        |
| *Advanced*              | Yes                                                                         |
| *Read-only*             | No                                                                          |

### remote-password-hashing-max-connections

|                         |                                                                                   |
| ----------------------- | --------------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the maximum number of connections to the password hashing microservice. |
| *Default value*         | 64                                                                                |
| *Allowed values*        | An integer.Lower limit: 0.                                                        |
| *Multi-valued*          | No                                                                                |
| *Required*              | No                                                                                |
| *Admin action required* | None                                                                              |
| *Advanced*              | Yes                                                                               |
| *Read-only*             | No                                                                                |

### remote-password-hashing-request-timeout

|                         |                                                                           |
| ----------------------- | ------------------------------------------------------------------------- |
| *Synopsis*              | Specifies the timeout for a request to the password hashing microservice. |
| *Default value*         | 10 s                                                                      |
| *Allowed values*        | Uses [duration syntax](duration-syntax.html).Lower limit: 0 seconds.      |
| *Multi-valued*          | No                                                                        |
| *Required*              | No                                                                        |
| *Admin action required* | None                                                                      |
| *Advanced*              | Yes                                                                       |
| *Read-only*             | No                                                                        |

---

---
title: Blind Trust Manager Provider
description: The blind trust manager provider always trusts any certificate that is presented to it, regardless of its issuer, subject, and validity dates.
component: pingds
version: 8.1
page_id: pingds:configref:objects-blind-trust-manager-provider
canonical_url: https://docs.pingidentity.com/pingds/8.1/configref/objects-blind-trust-manager-provider.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parent: Parent
  blind_trust_manager_provider_properties: Blind Trust Manager Provider properties
  basic_properties: Basic properties
  enabled: enabled
  advanced_properties: Advanced properties
  java-class: java-class
---

# Blind Trust Manager Provider

The blind trust manager provider always trusts any certificate that is presented to it, regardless of its issuer, subject, and validity dates.

Use the blind trust manager provider only for testing purposes, because it allows clients to use forged certificates and authenticate as virtually any user in the server.

## Parent

The Blind Trust Manager Provider object inherits from [Trust Manager Provider](objects-trust-manager-provider.html).

## Blind Trust Manager Provider properties

You can use configuration expressions to set property values at startup time. For details, see [Property value substitution](expressions.html).

| Basic Properties    | Advanced Properties       |
| ------------------- | ------------------------- |
| [enabled](#enabled) | [java-class](#java-class) |

### Basic properties

Use the `--advanced` option to access advanced properties.

### enabled

|                         |                                                                 |
| ----------------------- | --------------------------------------------------------------- |
| *Synopsis*              | Indicate whether the Trust Manager Provider is enabled for use. |
| *Default value*         | None                                                            |
| *Allowed values*        | truefalse                                                       |
| *Multi-valued*          | No                                                              |
| *Required*              | Yes                                                             |
| *Admin action required* | None                                                            |
| *Advanced*              | No                                                              |
| *Read-only*             | No                                                              |

## Advanced properties

Use the `--advanced` option to access advanced properties.

### java-class

|                         |                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| *Synopsis*              | The fully-qualified name of the Java class that provides the Blind Trust Manager Provider implementation. |
| *Default value*         | org.opends.server.extensions.BlindTrustManagerProvider                                                    |
| *Allowed values*        | A Java class that extends or implements:- org.opends.server.api.TrustManagerProvider                      |
| *Multi-valued*          | No                                                                                                        |
| *Required*              | Yes                                                                                                       |
| *Admin action required* | None                                                                                                      |
| *Advanced*              | Yes                                                                                                       |
| *Read-only*             | No                                                                                                        |
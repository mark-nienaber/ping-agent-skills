---
title: Access Denied URI Map
description: The URIs of custom pages to return when access is denied. The key is the web application name. The value is the custom URI.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.access.denied.uri.map
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.access.denied.uri.map.html
---

# Access Denied URI Map

The URIs of custom pages to return when access is denied. The key is the web application name. The value is the custom URI.

To set a global custom access denied URI for web applications without other custom access denied URIs defined, leave the key empty and set the value to the global custom access denied URI, `/s6ample/accessdenied.html`.

To set a custom access denied URI for a specific web application, set the key to the name of the web application, and the value to the web application access denied URI, such as `/myApp/accessdenied.html`.

Specify a full URL if required, including the host name. For example: `https://help.example.com/errors/accessdenied.html`.

|                          |                                                                                                                                                                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.access.denied.uri.map`                                                                                                                                                                                        |
| Aliases                  | `com.sun.identity.agents.config.access.denied.uri`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6`org.forgerock.agents.access.denied.uri.map`   Introduced in Java Agent 5.6 |
| Function                 | Access denied                                                                                                                                                                                                                       |
| Type                     | Map- Keys: web application

- Values: URI of page saying 'access denied'                                                                                                                                                            |
| Bootstrap property       | No                                                                                                                                                                                                                                  |
| Required property        | No                                                                                                                                                                                                                                  |
| Restart required         | No                                                                                                                                                                                                                                  |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                            |
| AM console               | Tab: `Application`Title: `Access Denied URI Map`Legacy title: `Resource Access Denied URI`                                                                                                                                          |

---

---
title: Agent Debug Level
description: The agent log level.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.debug.level
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.debug.level.html
---

# Agent Debug Level

The agent log level.

Make sure your container captures messages written to the standard output. Some containers do not, and warnings or critical errors can disappear forever.

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.debug.level`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Aliases                  | `com.iplanet.services.debug.level`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6`org.forgerock.agents.debug.level`   Introduced in Java Agent 5.6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Function                 | Logs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Supported settings       | * OFF

  (Deprecated) Uses the same log level as `ERROR`. To disable logging, edit `agent-logback.xml`. Forgerock advises not to disable logging.

* ERROR

  Log only errors.

* WARNING

  Log errors and warnings.

* MESSAGE

  Log errors, warnings, and informative messages.

* DEBUG

  Log errors, warnings, informative messages, and some debugging messages.

* TRACE

  Log fine-grained information, when you need the full visibility of what is happening in your application. This log level can create big log files, so use only when necessary, and then reduce the log level.

* ON

  (Deprecated) Uses the same log level as `TRACE`. When the log level is `ON`, `TRACE` level logs are written to file. In previous releases, `TRACE` level logs were written to the standard output. Make sure your container captures messages written to the standard output. |
| Default                  | `ERROR`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Bootstrap property       | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AM console               | Tab: `Global`Title: `Agent Debug Level`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

---

---
title: Agent Filter Mode Map
description: A map of web application name to agent filter mode:
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.filter.mode.map
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.filter.mode.map.html
---

# Agent Filter Mode Map

A map of web application name to agent filter mode:

* Key: Web application name.

* Value: Agent filter mode.

The following example configures one filter mode for the `BankApp` web application. All other web applications use the default filter mode, `URL_POLICY`: `org.forgerock.agents.filter.mode.map[BankApp]=SSO_ONLY`

The following example configures the `NONE` filter mode for all applications in the web container: `org.forgerock.agents.filter.mode.map[ALL]=NONE`

The mode `J2EE_POLICY` does not apply to Java Agents 5.10. However, for backward-compatibility, it is displayed in the AM agent profile page.

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.filter.mode.map`                                                                                                                                                                                                                                                                                                                                                                                        |
| Aliases                  | `com.sun.identity.agents.config.filter.mode`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6`org.forgerock.agents.filter.mode.map`   Introduced in Java Agent 5.6.2.1                                                                                                                                                                                                   |
| Function                 | Agent                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Supported settings       | * NONE

  The agent performs no authentication check, and grants access to any resource. When the value is `NONE` and logging is enabled, for auditing purposes, the agent filter logs all incoming requests.

* SSO\_ONLY

  Any user having either a valid SSO token or JWT can access any resource.

* URL\_POLICY

  The normal operating mode of the agent, in which resource access is granted by AM policy evaluation. |
| Default                  | `URL_POLICY`                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Bootstrap property       | Yes                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Local configuration file | `AgentBootstrap.properties`                                                                                                                                                                                                                                                                                                                                                                                                   |
| AM console               | Tab: `Global`Title: `Agent Filter Mode Map`Legacy title: `Agent Filter Mode`                                                                                                                                                                                                                                                                                                                                                  |

---

---
title: Agent Profile Name
description: The profile name used to fetch agent configuration data from AM, to evaluate policies for users, retrieve session info, and so on.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.profile.name
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.profile.name.html
---

# Agent Profile Name

The profile name used to fetch agent configuration data from AM, to evaluate policies for users, retrieve session info, and so on.

Default: Empty

|                          |                                                                                                                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Property name            | `org.forgerock.agents.profile.name`                                                                                                                                                                                |
| Aliases                  | `com.sun.identity.agents.app.username`   Introduced in Java Agent 5.0`com.sun.identity.agents.config.profilename`   Introduced in Java Agent 5.0`org.forgerock.agents.profile.name`   Introduced in Java Agent 5.6 |
| Function                 | Profile, Required                                                                                                                                                                                                  |
| Type                     | String                                                                                                                                                                                                             |
| Bootstrap property       | Yes                                                                                                                                                                                                                |
| Required property        | Yes - If this property is missing, the agent fails to start                                                                                                                                                        |
| Restart required         | Yes - Restart the container after changing the property                                                                                                                                                            |
| Local configuration file | `AgentBootstrap.properties`                                                                                                                                                                                        |

---

---
title: Agent Profile Realm
description: The realm in which the agent profile is defined.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.agent.profile.realm
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.agent.profile.realm.html
---

# Agent Profile Realm

The realm in which the agent profile is defined.

When [Enable Policy Evaluation in User Authentication Realm](org.forgerock.agents.user.realm.overrides.policy.evaluation.realm.enabled.html) is `true`, AM uses this realm to evaluate polices for policy decision requests from the agent.

|                          |                                                                                                                                                            |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.agent.profile.realm`                                                                                                                 |
| Aliases                  | `org.forgerock.agents.agent.profile.realm`   Introduced in Java Agent 5.6`com.sun.identity.agents.config.organization.name`   Introduced in Java Agent 5.0 |
| Function                 | Profile, Required                                                                                                                                          |
| Type                     | String                                                                                                                                                     |
| Default                  | `/`                                                                                                                                                        |
| Bootstrap property       | Yes                                                                                                                                                        |
| Required property        | Yes - If this property is missing, the agent fails to start                                                                                                |
| Restart required         | Yes - Restart the container after changing the property                                                                                                    |
| Local configuration file | `AgentBootstrap.properties`                                                                                                                                |

---

---
title: Alternative Agent Host Name
description: In environments when agents are behind a load balancer or reverse proxy which does a SSL offloading, the request URL is changed to match the URL that the agent receives.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.agent.hostname
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.agent.hostname.html
---

# Alternative Agent Host Name

In environments when agents are behind a load balancer or reverse proxy which does a SSL offloading, the request URL is changed to match the URL that the agent receives.

The agent then uses the new URL as the redirection value in the pre-authentication cookie, created during the first unauthenticated request to the agent.

Use the following properties to override the agent redirection value with the URL of the original client request: [Alternative Agent Port Number](org.forgerock.agents.agent.port.html) and [Alternative Agent Protocol](org.forgerock.agents.agent.protocol.html).

|                          |                                                                                                                                                                                                                       |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.agent.hostname`                                                                                                                                                                                 |
| Aliases                  | `com.sun.identity.agents.config.agent.host`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6`org.forgerock.agents.agent.hostname`   Introduced in Java Agent 5.6 |
| Function                 | Agent                                                                                                                                                                                                                 |
| Type                     | String                                                                                                                                                                                                                |
| Bootstrap property       | No                                                                                                                                                                                                                    |
| Required property        | No                                                                                                                                                                                                                    |
| Restart required         | No                                                                                                                                                                                                                    |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                              |
| AM console               | Tab: `Advanced`Title: `Alternative Agent Host Name`                                                                                                                                                                   |

---

---
title: Alternative Agent Port Number
description: In environments when agents are behind a load balancer or reverse proxy which does a SSL offloading, the request URL is changed to match the URL that the agent receives.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.agent.port
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.agent.port.html
---

# Alternative Agent Port Number

In environments when agents are behind a load balancer or reverse proxy which does a SSL offloading, the request URL is changed to match the URL that the agent receives.

The agent then uses the new URL as the redirection value in the pre-authentication cookie, created during the first unauthenticated request to the agent.

Use the following properties to override the agent redirection value with the URL of the original client request: [Alternative Agent Host Name](org.forgerock.agents.agent.hostname.html), and [Alternative Agent Protocol](org.forgerock.agents.agent.protocol.html).

|                          |                                                                                                                                                                                                                   |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.agent.port`                                                                                                                                                                                 |
| Aliases                  | `com.sun.identity.agents.config.agent.port`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6`org.forgerock.agents.agent.port`   Introduced in Java Agent 5.6 |
| Function                 | Agent                                                                                                                                                                                                             |
| Type                     | Integer                                                                                                                                                                                                           |
| Default                  | `-2147483648`                                                                                                                                                                                                     |
| Bootstrap property       | No                                                                                                                                                                                                                |
| Required property        | No                                                                                                                                                                                                                |
| Restart required         | No                                                                                                                                                                                                                |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                          |
| AM console               | Tab: `Advanced`Title: `Alternative Agent Port Number`                                                                                                                                                             |

---

---
title: Continuous Security Cookie Map
description: Maps cookie values available in inbound resource requests to entries in the environmental conditions map, which agents send to AM during policy evaluation.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.continuous.security.cookies.map
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.continuous.security.cookies.map.html
---

# Continuous Security Cookie Map

Maps cookie values available in inbound resource requests to entries in the environmental conditions map, which agents send to AM during policy evaluation.

|                          |                                                                                                                                                                                                                                                             |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.continuous.security.cookies.map`                                                                                                                                                                                                      |
| Aliases                  | `org.forgerock.agents.continuous.security.cookies.map`   Introduced in Java Agent 5.6`org.forgerock.openam.agents.config.continuous.security.cookies`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6 |
| Function                 | Continuous security                                                                                                                                                                                                                                         |
| Type                     | Map- Keys: incoming cookie name

- Values: name of entry in environment map                                                                                                                                                                                 |
| Bootstrap property       | No                                                                                                                                                                                                                                                          |
| Required property        | No                                                                                                                                                                                                                                                          |
| Restart required         | No                                                                                                                                                                                                                                                          |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                    |
| AM console               | Tab: `Application`Title: `Continuous Security Cookie Map`Legacy title: `Continuous Security Cookies`                                                                                                                                                        |

---

---
title: Continuous Security Header Map
description: Maps header values in inbound resource requests to entries in the environmental conditions map, which agents send to AM during policy evaluation.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.continuous.security.headers.map
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.continuous.security.headers.map.html
---

# Continuous Security Header Map

Maps header values in inbound resource requests to entries in the environmental conditions map, which agents send to AM during policy evaluation.

Example:

`org.forgerock.agents.continuous.security.headers.map[User-Agent]=myUserAgentHeaderEntry`

|                          |                                                                                                                                                                                                                                                             |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.continuous.security.headers.map`                                                                                                                                                                                                      |
| Aliases                  | `org.forgerock.agents.continuous.security.headers.map`   Introduced in Java Agent 5.6`org.forgerock.openam.agents.config.continuous.security.headers`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6 |
| Function                 | Continuous security                                                                                                                                                                                                                                         |
| Type                     | Map- Keys: incoming header name

- Values: name of entry in environment map                                                                                                                                                                                 |
| Bootstrap property       | No                                                                                                                                                                                                                                                          |
| Required property        | No                                                                                                                                                                                                                                                          |
| Restart required         | No                                                                                                                                                                                                                                                          |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                    |
| AM console               | Tab: `Application`Title: `Continuous Security Header Map`Legacy title: `Continuous Security Headers`                                                                                                                                                        |

---

---
title: Control Handling of Path Traversal Attempts
description: When set to true any incoming URL containing a path segment of .. will cause the incoming request to be rejected with an HTTP 400 response.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.reject.path.traversal.attempts.enabled
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.reject.path.traversal.attempts.enabled.html
---

# Control Handling of Path Traversal Attempts

When set to `true` any incoming URL containing a path segment of `..` will cause the incoming request to be rejected with an HTTP 400 response.

Note that requests will be rejected if any path parameter contains `..` anywhere, even though path parameters do not take part in URI normalisation.

When the property [Control Handling of the URL Encoded Sequence %2e](org.forgerock.agents.percent.2e.handling.strategy.html) is set to ACCEPT\_AND\_INTERPRET, path segments or path parameters containing `.%2e`, `%2e.` and `%2e%2e` will also be rejected.

Note that this will NOT affect access to resources such as `index..html`, for example.

|                          |                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------ |
| Property name            | `org.forgerock.agents.reject.path.traversal.attempts.enabled`                                    |
| Aliases                  | `org.forgerock.agents.reject.path.traversal.attempts.enabled`   Introduced in Java Agent 2024.11 |
| Function                 | Configure behaviour                                                                              |
| Type                     | Boolean: `true` returns true; all other strings return `false`.                                  |
| Default                  | `false`                                                                                          |
| Bootstrap property       | No                                                                                               |
| Required property        | No                                                                                               |
| Restart required         | No                                                                                               |
| Local configuration file | `AgentConfig.properties`                                                                         |

---

---
title: Control Handling of the Backslash Character
description: This property controls whether the backslash character, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.backslash.handling.strategy
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.backslash.handling.strategy.html
---

# Control Handling of the Backslash Character

This property controls whether the backslash character, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.

When set to `REJECT_OUTRIGHT`, if a backslash occurs anywhere in the incoming URI path, or path parameters, the agent will reject the incoming request with an HTTP 400 response.

When set to `ACCEPT_BUT_NOT_INTERPRET`, any occurrence of backslash in the incoming URI path, or path parameters, will be left unconverted.

When set to `ACCEPT_AND_INTERPRET`, any occurrence of backslash in the incoming URI path, or path parameters, will be replaced by a forward slash character.

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.backslash.handling.strategy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Aliases                  | `org.forgerock.agents.backslash.handling.strategy`   Introduced in Java Agent 2024.11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Function                 | Configure behaviour                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Supported settings       | * REJECT\_OUTRIGHT

  Any and all occurrences of the specified sequence within the incoming URL will cause the agent to reject the incoming request with HTTP 400.

* ACCEPT\_BUT\_NOT\_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, but the sequence will be left decoded.

* ACCEPT\_AND\_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, and the sequence will be decoded for the purposes of not-enforced rule matching and AM policy evaluation |
| Default                  | `REJECT_OUTRIGHT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Bootstrap property       | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

---

---
title: Control Handling of the URL Encoded Sequence %2e
description: This property controls whether the encoding sequence %2e, if used in incoming URL paths, is rejected, accepted (without decoding) or treated as a . character.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.percent.2e.handling.strategy
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.percent.2e.handling.strategy.html
---

# Control Handling of the URL Encoded Sequence %2e

This property controls whether the encoding sequence `%2e`, if used in incoming URL paths, is rejected, accepted (without decoding) or treated as a `.` character.

When set to `REJECT_OUTRIGHT`, if the sequence `%2e` occurs anywhere in the incoming URI path, or path parameters, the agent will reject the incoming request with an HTTP 400 response.

When set to `ACCEPT_BUT_NOT_INTERPRET`, any occurrence of `%2e` in the incoming URI path, or path parameters, will be left unconverted.

When set to `ACCEPT_AND_INTERPRET`, any occurrence of `%2e` in the incoming URI path will be interpreted as a `.` character.

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.percent.2e.handling.strategy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Aliases                  | `org.forgerock.agents.percent.2e.handling.strategy`   Introduced in Java Agent 2024.11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Function                 | Configure behaviour                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Supported settings       | * REJECT\_OUTRIGHT

  Any and all occurrences of the specified sequence within the incoming URL will cause the agent to reject the incoming request with HTTP 400.

* ACCEPT\_BUT\_NOT\_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, but the sequence will be left decoded.

* ACCEPT\_AND\_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, and the sequence will be decoded for the purposes of not-enforced rule matching and AM policy evaluation |
| Default                  | `REJECT_OUTRIGHT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Bootstrap property       | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

---

---
title: Control Handling of the URL Encoded Sequence %2f
description: This property controls whether the encoding sequence %2f, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.percent.2f.handling.strategy
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.percent.2f.handling.strategy.html
---

# Control Handling of the URL Encoded Sequence %2f

This property controls whether the encoding sequence `%2f`, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.

When set to `REJECT_OUTRIGHT`, if the sequence `%2f` occurs anywhere in the incoming URI path, or path parameters, the agent will reject the incoming request with an HTTP 400 response.

When set to `ACCEPT_BUT_NOT_INTERPRET`, any occurrence of `%2f` in the incoming URI path, or path parameters, will be left unconverted.

When set to `ACCEPT_AND_INTERPRET`, any occurrence of `%2f` in the incoming URI path, or path parameters, will be replaced by a forward slash character.

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.percent.2f.handling.strategy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Aliases                  | `org.forgerock.agents.percent.2f.handling.strategy`   Introduced in Java Agent 2024.11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Function                 | Configure behaviour                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Supported settings       | * REJECT\_OUTRIGHT

  Any and all occurrences of the specified sequence within the incoming URL will cause the agent to reject the incoming request with HTTP 400.

* ACCEPT\_BUT\_NOT\_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, but the sequence will be left decoded.

* ACCEPT\_AND\_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, and the sequence will be decoded for the purposes of not-enforced rule matching and AM policy evaluation |
| Default                  | `REJECT_OUTRIGHT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Bootstrap property       | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

---

---
title: Control Handling of the URL Encoded Sequence %3b
description: This property controls whether the encoding sequence %3b, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.percent.3b.handling.strategy
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.percent.3b.handling.strategy.html
---

# Control Handling of the URL Encoded Sequence %3b

This property controls whether the encoding sequence `%3b`, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.

When set to `REJECT_OUTRIGHT`, if the sequence `%3b` occurs anywhere in the incoming URI path, or path parameters, the agent will reject the incoming request with an HTTP 400 response..

When set to `ACCEPT_BUT_NOT_INTERPRET`, any occurrence of `%3b` in the incoming URI path, or path parameters, will be left unconverted.

When set to `ACCEPT_AND_INTERPRET`, any occurrence of `%3b` in the incoming URI path will be replaced by a semicolon and used as a path segment/path parameter separator.

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.percent.3b.handling.strategy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Aliases                  | `org.forgerock.agents.percent.3b.handling.strategy`   Introduced in Java Agent 2024.11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Function                 | Configure behaviour                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Supported settings       | * REJECT\_OUTRIGHT

  Any and all occurrences of the specified sequence within the incoming URL will cause the agent to reject the incoming request with HTTP 400.

* ACCEPT\_BUT\_NOT\_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, but the sequence will be left decoded.

* ACCEPT\_AND\_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, and the sequence will be decoded for the purposes of not-enforced rule matching and AM policy evaluation |
| Default                  | `REJECT_OUTRIGHT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Bootstrap property       | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

---

---
title: Control Handling of the URL Encoded Sequence %5c
description: This property controls whether the encoding sequence %5c, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.percent.5c.handling.strategy
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.percent.5c.handling.strategy.html
---

# Control Handling of the URL Encoded Sequence %5c

This property controls whether the encoding sequence `%5c`, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.

When set to `REJECT_OUTRIGHT`, if the sequence `%5c` occurs anywhere in the incoming URI path, or path parameters, the agent will reject the incoming request with an HTTP 400 response.

When set to `ACCEPT_BUT_NOT_INTERPRET`, any occurrence of `%5c` in the incoming URI path, or path parameters, will be left unconverted.

When set to `ACCEPT_AND_INTERPRET`, any occurrence of `%5c` in the incoming URI path, or path parameters, will be replaced by a forward slash character.

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.percent.5c.handling.strategy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Aliases                  | `org.forgerock.agents.percent.5c.handling.strategy`   Introduced in Java Agent 2024.11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Function                 | Configure behaviour                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Supported settings       | * REJECT\_OUTRIGHT

  Any and all occurrences of the specified sequence within the incoming URL will cause the agent to reject the incoming request with HTTP 400.

* ACCEPT\_BUT\_NOT\_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, but the sequence will be left decoded.

* ACCEPT\_AND\_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, and the sequence will be decoded for the purposes of not-enforced rule matching and AM policy evaluation |
| Default                  | `REJECT_OUTRIGHT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Bootstrap property       | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

---

---
title: Convert SSO Tokens Into OIDC JWTs
description: For each incoming request, the agent looks for an OIDC JWT in the cookie named by JWT Cookie Name. Set this property as follows:
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.accept.ipdp.cookie
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.accept.ipdp.cookie.html
---

# Convert SSO Tokens Into OIDC JWTs

For each incoming request, the agent looks for an OIDC JWT in the cookie named by [JWT Cookie Name](org.forgerock.agents.jwt.cookie.name.html). Set this property as follows:

* `true`: Use this value to allow users to access resources protected with systems that continue to use SSO tokens, and to use the default login redirection mode.

  * If the agent does not find a JWT in the cookie, the agent looks for an SSO token in the iPDP cookie defined during AM installation. During agent startup, the agent retrieves the name of this cookie from AM.

  * If the agent finds an SSO token in the iPDP cookie, it makes a request to AM to convert the SSO token into an OIDC JWT.

  * The agent caches the SSO token, so that if it is presented in another incoming request, the agent substitutes the JWT without making a request to AM.

  * If the agent does not find either token, authentication fails. The user can only access resources that are available through not-enforced rules.

* `false`: Do not convert SSO tokens into OIDC JWTs.

|                          |                                                                                                                                                                                                                                                                                                                      |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.accept.ipdp.cookie`                                                                                                                                                                                                                                                                            |
| Aliases                  | `com.forgerock.agents.accept.ipdp.cookie`   Introduced in Java Agent 5.6   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 7`org.forgerock.agents.accept.ipdp.cookie.enabled`   Introduced in Java Agent 5.7`org.forgerock.agents.exchange.ipdp.cookie.enabled`   Introduced in Java Agent 2024.9 |
| Function                 | SSO cookie handling                                                                                                                                                                                                                                                                                                  |
| Type                     | Boolean: `true` returns true; all other strings return `false`.                                                                                                                                                                                                                                                      |
| Default                  | `false`                                                                                                                                                                                                                                                                                                              |
| Bootstrap property       | No                                                                                                                                                                                                                                                                                                                   |
| Required property        | No                                                                                                                                                                                                                                                                                                                   |
| Restart required         | No                                                                                                                                                                                                                                                                                                                   |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                                                                             |
| AM console               | Tab: `SSO (from AM 7)`Title: `Convert SSO Tokens Into OIDC JWTs`Legacy title: `Convert SSO Tokens into OpenID Connect JWTs`                                                                                                                                                                                          |

---

---
title: Cookie Reset
description: When true, the agent resets the cookies in the response before redirecting the client for login, and when the client logs out.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.cookie.reset.enabled
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.cookie.reset.enabled.html
---

# Cookie Reset

When `true`, the agent resets the cookies in the response before redirecting the client for login, and when the client logs out.

The agent resets the cookies listed in [Reset Cookie List](org.forgerock.agents.cookie.reset.name.list.html), and cookies that store profile or session attributes (when [Profile Attribute Fetch Mode](org.forgerock.agents.profile.attribute.fetch.mode.html) or [Session Attribute Fetch Mode](org.forgerock.agents.session.attribute.fetch.mode.html) has the value `HTTP_COOKIE`).

To reset cookies that store response attributes (when [Response Attribute Fetch Mode](org.forgerock.agents.response.attribute.fetch.mode.html) has the value `HTTP_COOKIE`), add them to the [Reset Cookie List](org.forgerock.agents.cookie.reset.name.list.html).

|                          |                                                                                                                                                                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Property name            | `org.forgerock.agents.cookie.reset.enabled`                                                                                                                                                                                          |
| Aliases                  | `org.forgerock.agents.cookie.reset.enabled`   Introduced in Java Agent 5.6`com.sun.identity.agents.config.cookie.reset.enable`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6 |
| Function                 | Cookie reset                                                                                                                                                                                                                         |
| Type                     | Boolean: `true` returns true; all other strings return `false`.                                                                                                                                                                      |
| Default                  | `false`                                                                                                                                                                                                                              |
| Bootstrap property       | No                                                                                                                                                                                                                                   |
| Required property        | No                                                                                                                                                                                                                                   |
| Restart required         | No                                                                                                                                                                                                                                   |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                             |
| AM console               | Tab: `SSO`Title: `Cookie Reset`                                                                                                                                                                                                      |

---

---
title: Cookie Separator Character
description: The separator for multiple values of the same attribute when it is set as a cookie.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.attribute.cookie.separator
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.attribute.cookie.separator.html
---

# Cookie Separator Character

The separator for multiple values of the same attribute when it is set as a cookie.

|                          |                                                                                                                                                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.attribute.cookie.separator`                                                                                                                                                                                                 |
| Aliases                  | `com.sun.identity.agents.config.attribute.cookie.separator`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6`org.forgerock.agents.attribute.cookie.separator`   Introduced in Java Agent 5.6 |
| Function                 | Attributes                                                                                                                                                                                                                                        |
| Type                     | String                                                                                                                                                                                                                                            |
| Default                  | `\|`                                                                                                                                                                                                                                              |
| Bootstrap property       | No                                                                                                                                                                                                                                                |
| Required property        | No                                                                                                                                                                                                                                                |
| Restart required         | No                                                                                                                                                                                                                                                |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                          |
| AM console               | Tab: `Application`Title: `Cookie Separator Character`                                                                                                                                                                                             |

---

---
title: CSV Monitoring Directory
description: The full path to the directory where the agent writes CSV monitoring files, when CSV monitoring is enabled.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.csv.monitoring.directory
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.csv.monitoring.directory.html
---

# CSV Monitoring Directory

The full path to the directory where the agent writes CSV monitoring files, when CSV monitoring is enabled.

The default is set by the installer and written to the bootstrap properties file.

Default: `/logs/debug` directory relative to the definedBy of the agent installation

|                          |                                                                                |
| ------------------------ | ------------------------------------------------------------------------------ |
| Property name            | `org.forgerock.agents.csv.monitoring.directory`                                |
| Aliases                  | `org.forgerock.agents.csv.monitoring.directory`   Introduced in Java Agent 5.7 |
| Function                 | Monitoring                                                                     |
| Type                     | String                                                                         |
| Bootstrap property       | Yes                                                                            |
| Required property        | No                                                                             |
| Restart required         | Yes - Restart the container after changing the property                        |
| Local configuration file | `AgentBootstrap.properties`                                                    |

---

---
title: Custom Response Header Map
description: A key:value map of custom headers set by the agent for the client, where the key is the header name, and the value is the header value. For example, org.forgerock.agents.response.header.map[Cache-Control]=no-cache
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.response.header.map
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.response.header.map.html
---

# Custom Response Header Map

A key:value map of custom headers set by the agent for the client, where the key is the header name, and the value is the header value. For example, `org.forgerock.agents.response.header.map[Cache-Control]=no-cache`

Format `org.forgerock.agents.response.header.map[HEADER-NAME]=HEADER-VALUE`

|                          |                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.response.header.map`                                                                                                                                                                                      |
| Aliases                  | `org.forgerock.agents.response.header.map`   Introduced in Java Agent 5.6`com.sun.identity.agents.config.response.header`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6 |
| Function                 | Miscellaneous                                                                                                                                                                                                                   |
| Type                     | Map- Keys: from header

- Values: to header                                                                                                                                                                                     |
| Bootstrap property       | No                                                                                                                                                                                                                              |
| Required property        | No                                                                                                                                                                                                                              |
| Restart required         | No                                                                                                                                                                                                                              |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                        |
| AM console               | Tab: `Global`Title: `Custom Response Header Map`Legacy title: `Custom Response Header`                                                                                                                                          |
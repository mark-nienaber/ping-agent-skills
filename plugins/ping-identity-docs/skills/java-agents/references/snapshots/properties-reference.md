---
title: Access Denied URI Map
description: The URIs of custom pages to return when access is denied. The key is the web application name. The value is the custom URI.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.access.denied.uri.map
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.access.denied.uri.map.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
title: Alternative Agent Protocol
description: In environments when agents are behind a load balancer or reverse proxy which does a SSL offloading, the request URL is changed to match the URL that the agent receives.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.agent.protocol
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.agent.protocol.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Alternative Agent Protocol

In environments when agents are behind a load balancer or reverse proxy which does a SSL offloading, the request URL is changed to match the URL that the agent receives.

The agent then uses the new URL as the redirection value in the pre-authentication cookie, created during the first unauthenticated request to the agent.

Use the following properties to override the agent redirection value with the URL of the original client request: [Alternative Agent Host Name](org.forgerock.agents.agent.hostname.html), and [Alternative Agent Port Number](org.forgerock.agents.agent.port.html).

|                          |                                                                                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.agent.protocol`                                                                                                                                                                                     |
| Aliases                  | `com.sun.identity.agents.config.agent.protocol`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6`org.forgerock.agents.agent.protocol`   Introduced in Java Agent 5.6 |
| Function                 | Agent                                                                                                                                                                                                                     |
| Type                     | String                                                                                                                                                                                                                    |
| Bootstrap property       | No                                                                                                                                                                                                                        |
| Required property        | No                                                                                                                                                                                                                        |
| Restart required         | No                                                                                                                                                                                                                        |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                  |
| AM console               | Tab: `Advanced`Title: `Alternative Agent Protocol`                                                                                                                                                                        |

---

---
title: Always invalidate sessions
description: When false, the agent does not invoke the AM REST logout endpoint to kill the user session.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.config.logout.session.invalidate.enabled
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.config.logout.session.invalidate.enabled.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Always invalidate sessions

When `false`, the agent does not invoke the AM REST logout endpoint to kill the user session.

If [Conditional Logout URL List](org.forgerock.agents.conditional.logout.url.list.html) is configured with a URL that does not perform a REST logout to AM, set this property to `true`. The agent additionally invokes the AM REST logout endpoint to invalidate the session.

|                          |                                                                                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Property name            | `org.forgerock.agents.config.logout.session.invalidate.enabled`                                                                                                                            |
| Aliases                  | `org.forgerock.agents.config.logout.session.invalidate.enabled`   Introduced in Java Agent 5.10.1`org.forgerock.agents.config.logout.session.invalidate`   Introduced in Java Agent 5.10.1 |
| Function                 | Logout                                                                                                                                                                                     |
| Type                     | Boolean: `true` returns true; all other strings return `false`.                                                                                                                            |
| Default                  | `true`                                                                                                                                                                                     |
| Bootstrap property       | No                                                                                                                                                                                         |
| Required property        | No                                                                                                                                                                                         |
| Restart required         | No                                                                                                                                                                                         |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                   |

---

---
title: AM Authentication Service Host Name
description: The AM server host name.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.am.hostname
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.am.hostname.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# AM Authentication Service Host Name

The AM server host name.

|                          |                                                                                                                                                                                                     |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.am.hostname`                                                                                                                                                                  |
| Aliases                  | `com.iplanet.am.server.host`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6`org.forgerock.agents.am.hostname`   Introduced in Java Agent 5.6 |
| Function                 | Authentication service, Required                                                                                                                                                                    |
| Type                     | String                                                                                                                                                                                              |
| Bootstrap property       | Yes                                                                                                                                                                                                 |
| Required property        | Yes - If this property is missing, the agent fails to start                                                                                                                                         |
| Restart required         | Yes - Restart the container after changing the property                                                                                                                                             |
| Local configuration file | `AgentBootstrap.properties`                                                                                                                                                                         |
| AM console               | Tab: `AM Services`Title: `AM Authentication Service Host Name`                                                                                                                                      |

---

---
title: AM Authentication Service Path
description: The path to the AM server.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.am.path
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.am.path.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# AM Authentication Service Path

The path to the AM server.

|                          |                                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Property name            | `org.forgerock.agents.am.path`                                                                                                             |
| Aliases                  | `com.iplanet.am.services.deploymentDescriptor`   Introduced in Java Agent 5.0`org.forgerock.agents.am.path`   Introduced in Java Agent 5.6 |
| Function                 | Authentication service, Required                                                                                                           |
| Type                     | String                                                                                                                                     |
| Bootstrap property       | Yes                                                                                                                                        |
| Required property        | Yes - If this property is missing, the agent fails to start                                                                                |
| Restart required         | Yes - Restart the container after changing the property                                                                                    |
| Local configuration file | `AgentBootstrap.properties`                                                                                                                |

---

---
title: AM Authentication Service Port
description: The AM server port number.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.am.port
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.am.port.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# AM Authentication Service Port

The AM server port number.

|                          |                                                                                                                                                                                                 |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.am.port`                                                                                                                                                                  |
| Aliases                  | `com.iplanet.am.server.port`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6`org.forgerock.agents.am.port`   Introduced in Java Agent 5.6 |
| Function                 | Authentication service, Required                                                                                                                                                                |
| Type                     | String                                                                                                                                                                                          |
| Bootstrap property       | Yes                                                                                                                                                                                             |
| Required property        | Yes - If this property is missing, the agent fails to start                                                                                                                                     |
| Restart required         | Yes - Restart the container after changing the property                                                                                                                                         |
| Local configuration file | `AgentBootstrap.properties`                                                                                                                                                                     |
| AM console               | Tab: `AM Services`Title: `AM Authentication Service Port`                                                                                                                                       |

---

---
title: AM Authentication Service Protocol
description: The protocol used by the AM server. Set to one of the following values:
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.am.protocol
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.am.protocol.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# AM Authentication Service Protocol

The protocol used by the AM server. Set to one of the following values:

* HTTP

* HTTPS

|                          |                                                                                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.am.protocol`                                                                                                                                                                      |
| Aliases                  | `org.forgerock.agents.am.protocol`   Introduced in Java Agent 5.6`com.iplanet.am.server.protocol`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6 |
| Function                 | Authentication service, Required                                                                                                                                                                        |
| Type                     | String                                                                                                                                                                                                  |
| Bootstrap property       | Yes                                                                                                                                                                                                     |
| Required property        | Yes - If this property is missing, the agent fails to start                                                                                                                                             |
| Restart required         | Yes - Restart the container after changing the property                                                                                                                                                 |
| Local configuration file | `AgentBootstrap.properties`                                                                                                                                                                             |
| AM console               | Tab: `AM Services`Title: `AM Authentication Service Protocol`                                                                                                                                           |

---

---
title: AM Login URL List
description: The URL of the login page to use for authentication.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:com.sun.identity.agents.config.login.url
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/com.sun.identity.agents.config.login.url.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# AM Login URL List

The URL of the login page to use for authentication.

During the redirect, the agent appends the following parameters to the agent's CDSSO endpoint:

* The goto parameter configured in [Goto Parameter Name](com.sun.identity.agents.config.redirect.param.html)

* A nonce parameter

Use the format `URL[?realm=realm_name?parameter1=value1&…​]`, where:

* `URL`: URL of the login page to use for authentication

* `[?realm=realm_name&service=tree_name&parameter1=value1&…​]`: Optional parameters that the agent passes to the

login page, for example, the AM realm at which to authenticate and the authentication tree to authenticate with.

You do not need to specify an authentication realm if any of the following conditions are true:

* The custom login page sets the realm parameter, for example, because it lets the user choose the realm.

* The user authenticates into a realm that has DNS aliases configured in AM. AM then logs the user into the realm whose DNS alias matches the incoming request URL. For example, an inbound request from `http://marketplace.example.com` logs in the marketplace realm if the realm alias is set to `marketplace.example.com`.

* The user authenticates to the top-level realm.

This parameter can be overwritten by the custom login page if, for example, the user chooses the authentication realm.

Specify as many parameters your custom login pages require.

Example:

`https://login.example.com/login.jsp?realm=marketplace&param1=value1`

In some versions of AM you can configure more than one value for this property, but only the first value is honored.

|                          |                                                                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Property name            | `com.sun.identity.agents.config.login.url`                                                                                                       |
| Aliases                  | `com.sun.identity.agents.config.login.url`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6 |
| Function                 | Custom login redirect, Default Login Redirect, Login redirect, Login Redirect (Default)                                                          |
| Type                     | List                                                                                                                                             |
| Bootstrap property       | No                                                                                                                                               |
| Required property        | No                                                                                                                                               |
| Restart required         | No                                                                                                                                               |
| Local configuration file | `AgentConfig.properties`                                                                                                                         |
| AM console               | Tab: `AM Services`Title: `AM Login URL List`Legacy title: `AM Login URL`                                                                         |

---

---
title: Audit Access Types
description: The type of messages to audit.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.audit.what
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.audit.what.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Audit Access Types

The type of messages to audit.

|                          |                                                                                                                                                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.audit.what`                                                                                                                                                                                       |
| Aliases                  | `com.sun.identity.agents.config.audit.accesstype`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6`org.forgerock.agents.audit.what`   Introduced in Java Agent 5.6 |
| Function                 | Audit                                                                                                                                                                                                                   |
| Supported settings       | * LOG\_NONE

  Don't audit anything.

* LOG\_ALLOW

  Audit only allowed requests.

* LOG\_DENY

  Audit only denied requests.

* LOG\_BOTH

  Audit both allowed and denied requests.                                  |
| Default                  | `LOG_NONE`                                                                                                                                                                                                              |
| Bootstrap property       | No                                                                                                                                                                                                                      |
| Required property        | No                                                                                                                                                                                                                      |
| Restart required         | No                                                                                                                                                                                                                      |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                |
| AM console               | Tab: `Global`Title: `Audit Access Types`                                                                                                                                                                                |

---

---
title: Audit Log Directory
description: The full path to the directory for the agent's local audit log files.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.local.audit.dir.path
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.local.audit.dir.path.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Audit Log Directory

The full path to the directory for the agent's local audit log files.

Default: None; local auditing is disabled

|                          |                                                                               |
| ------------------------ | ----------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.local.audit.dir.path`                                   |
| Aliases                  | `org.forgerock.agents.local.audit.dir.path`   Introduced in Java Agent 2024.6 |
| Function                 | Audit                                                                         |
| Type                     | String                                                                        |
| Bootstrap property       | Yes                                                                           |
| Required property        | No                                                                            |
| Restart required         | Yes - Restart the container after changing the property                       |
| Local configuration file | `AgentBootstrap.properties`                                                   |

---

---
title: Audit Log Exclude Paths
description: A list of JSON paths to exclude from audit logs. Audit event fields use JSON pointer notation and are taken from the JSON schema for the audit event content.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.audit.exclude.path.list
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.audit.exclude.path.list.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Audit Log Exclude Paths

A list of JSON paths to exclude from audit logs. Audit event fields use JSON pointer notation and are taken from the JSON schema for the audit event content.

To prevent logging of sensitive data for an audit event, the Common Audit Framework uses a safelist to specify which audit event fields appear in the logs. By default, only safelisted audit event fields are included in the logs.

This property takes precedence over [Audit Log Include Paths](org.forgerock.agents.audit.include.path.list.html). If a path is specified here and in [Audit Log Include Paths](org.forgerock.agents.audit.include.path.list.html), the corresponding audit event field is excluded.

The following example excludes Header1 but includes Header2 and Cookie1:

`org.forgerock.agents.audit.exclude.path.list[0]=/access/http/request/headers/Header1Name`

`org.forgerock.agents.audit.include.path.list[0]=/access/http/request/headers/Header2Name`

`org.forgerock.agents.audit.include.path.list[1]=/access/http/request/cookies/Cookie1Name`

|                          |                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.audit.exclude.path.list`                                   |
| Aliases                  | `org.forgerock.agents.audit.exclude.path.list`   Introduced in Java Agent 2024.6 |
| Function                 | Audit                                                                            |
| Type                     | List                                                                             |
| Bootstrap property       | Yes                                                                              |
| Required property        | No                                                                               |
| Restart required         | Yes - Restart the container after changing the property                          |
| Local configuration file | `AgentBootstrap.properties`                                                      |

---

---
title: Audit Log Filename (deprecated)
description: This property is deprecated; the log filename is fixed and can't be specified. If this property is specified and Audit Log Directory is empty, the directory name is extracted from this property and used in Audit Log Directory.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.local.audit.file.path
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.local.audit.file.path.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Audit Log Filename (deprecated)

This property is deprecated; the log filename is fixed and can't be specified. If this property is specified and [Audit Log Directory](org.forgerock.agents.local.audit.dir.path.html) is empty, the directory name is extracted from this property and used in [Audit Log Directory](org.forgerock.agents.local.audit.dir.path.html).

Default: None; local auditing is disabled

|                          |                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.local.audit.file.path`                                                                                                                                                                                    |
| Aliases                  | `com.sun.identity.agents.config.local.logfile`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 7`org.forgerock.agents.local.audit.file.path`   Introduced in Java Agent 5.6 |
| Function                 | Deprecated                                                                                                                                                                                                                      |
| Type                     | String                                                                                                                                                                                                                          |
| Bootstrap property       | Yes                                                                                                                                                                                                                             |
| Required property        | No                                                                                                                                                                                                                              |
| Restart required         | Yes - Restart the container after changing the property                                                                                                                                                                         |
| Local configuration file | `AgentBootstrap.properties`                                                                                                                                                                                                     |

---

---
title: Audit Log Include Paths
description: A list of JSON paths to include in audit logs. Audit event fields use JSON pointer notation and are taken from the JSON schema for the audit event content.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.audit.include.path.list
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.audit.include.path.list.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Audit Log Include Paths

A list of JSON paths to include in audit logs. Audit event fields use JSON pointer notation and are taken from the JSON schema for the audit event content.

To prevent logging of sensitive data for an audit event, the Common Audit Framework uses a safelist to specify which audit event fields appear in the logs. By default, only safelisted audit event fields are included in the logs.

|   |                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you include non-safelisted audit event fields in the logs, consider the impact on security. Inclusion of some headers, query parameters, or cookies could cause credentials or tokens to be logged, and allow anyone with access to the logs to impersonate the holder of these credentials or tokens. |

[Audit Log Exclude Paths](org.forgerock.agents.audit.exclude.path.list.html) takes precedence over this property. If a path is specified here and in [Audit Log Exclude Paths](org.forgerock.agents.audit.exclude.path.list.html), the corresponding audit event field is excluded.

The following example excludes Header1 but includes Header2 and Cookie1:

`org.forgerock.agents.audit.exclude.path.list[0]=/access/http/request/headers/Header1Name`

`org.forgerock.agents.audit.include.path.list[0]=/access/http/request/headers/Header2Name`

`org.forgerock.agents.audit.include.path.list[1]=/access/http/request/cookies/Cookie1Name`

|                          |                                                                                                                                                           |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.audit.include.path.list`                                                                                                            |
| Aliases                  | `org.forgerock.agents.audit.include.path.list`   Introduced in Java Agent 2024.6   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 7.1 |
| Function                 | Audit                                                                                                                                                     |
| Type                     | List                                                                                                                                                      |
| Bootstrap property       | Yes                                                                                                                                                       |
| Required property        | No                                                                                                                                                        |
| Restart required         | Yes - Restart the container after changing the property                                                                                                   |
| Local configuration file | `AgentBootstrap.properties`                                                                                                                               |

---

---
title: Audit Log Location
description: The location where the agent logs audit messages. If Audit Access Types is LOG_NONE, this property has no effect.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.audit.where
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.audit.where.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Audit Log Location

The location where the agent logs audit messages. If [Audit Access Types](org.forgerock.agents.audit.what.html) is `LOG_NONE`, this property has no effect.

|                          |                                                                                                                                                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.audit.where`                                                                                                                                                                                      |
| Aliases                  | `com.sun.identity.agents.config.log.disposition`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6`org.forgerock.agents.audit.where`   Introduced in Java Agent 5.6 |
| Function                 | Audit                                                                                                                                                                                                                   |
| Supported settings       | * NONE

  Don't audit anything, anywhere.

* LOCAL

  Audit locally only.

* REMOTE

  Audit remotely only.

* ALL

  Audit both locally and remotely.                                                                  |
| Default                  | `NONE`                                                                                                                                                                                                                  |
| Bootstrap property       | No                                                                                                                                                                                                                      |
| Required property        | No                                                                                                                                                                                                                      |
| Restart required         | No                                                                                                                                                                                                                      |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                |
| AM console               | Tab: `Global`Title: `Audit Log Location`                                                                                                                                                                                |
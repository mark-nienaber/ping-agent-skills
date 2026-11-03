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

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.filter.mode.map`                                                                                                                                                                                                                                                                                                                                                                                      |
| Aliases                  | `com.sun.identity.agents.config.filter.mode`   Introduced in Java Agent 5.0   [Recognized](preface.html#how_am_manages_multiple_aliases) from AM 6`org.forgerock.agents.filter.mode.map`   Introduced in Java Agent 5.6.2.1                                                                                                                                                                                                 |
| Function                 | Agent                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Supported settings       | * NONE

  The agent performs no authentication check, and grants access to any resource. When the value is `NONE` and logging is enabled, for auditing purposes, the agent filter logs all incoming requests.

* SSO_ONLY

  Any user having either a valid SSO token or JWT can access any resource.

* URL_POLICY

  The normal operating mode of the agent, in which resource access is granted by AM policy evaluation. |
| Default                  | `URL_POLICY`                                                                                                                                                                                                                                                                                                                                                                                                                |
| Bootstrap property       | Yes                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Local configuration file | `AgentBootstrap.properties`                                                                                                                                                                                                                                                                                                                                                                                                 |
| AM console               | Tab: `Global`Title: `Agent Filter Mode Map`Legacy title: `Agent Filter Mode`                                                                                                                                                                                                                                                                                                                                                |

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
title: Control Handling of the Backslash Character
description: This property controls whether the backslash character, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.backslash.handling.strategy
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.backslash.handling.strategy.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Control Handling of the Backslash Character

This property controls whether the backslash character, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.

When set to `REJECT_OUTRIGHT`, if a backslash occurs anywhere in the incoming URI path, or path parameters, the agent will reject the incoming request with an HTTP 400 response.

When set to `ACCEPT_BUT_NOT_INTERPRET`, any occurrence of backslash in the incoming URI path, or path parameters, will be left unconverted.

When set to `ACCEPT_AND_INTERPRET`, any occurrence of backslash in the incoming URI path, or path parameters, will be replaced by a forward slash character.

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.backslash.handling.strategy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Aliases                  | `org.forgerock.agents.backslash.handling.strategy`   Introduced in Java Agent 2024.11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Function                 | Configure behaviour                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Supported settings       | * REJECT_OUTRIGHT

  Any and all occurrences of the specified sequence within the incoming URL will cause the agent to reject the incoming request with HTTP 400.

* ACCEPT_BUT_NOT_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, but the sequence will be left decoded.

* ACCEPT_AND_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, and the sequence will be decoded for the purposes of not-enforced rule matching and AM policy evaluation |
| Default                  | `REJECT_OUTRIGHT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Bootstrap property       | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

---

---
title: Control Handling of the URL Encoded Sequence %2e
description: This property controls whether the encoding sequence %2e, if used in incoming URL paths, is rejected, accepted (without decoding) or treated as a . character.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.percent.2e.handling.strategy
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.percent.2e.handling.strategy.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Control Handling of the URL Encoded Sequence %2e

This property controls whether the encoding sequence `%2e`, if used in incoming URL paths, is rejected, accepted (without decoding) or treated as a `.` character.

When set to `REJECT_OUTRIGHT`, if the sequence `%2e` occurs anywhere in the incoming URI path, or path parameters, the agent will reject the incoming request with an HTTP 400 response.

When set to `ACCEPT_BUT_NOT_INTERPRET`, any occurrence of `%2e` in the incoming URI path, or path parameters, will be left unconverted.

When set to `ACCEPT_AND_INTERPRET`, any occurrence of `%2e` in the incoming URI path will be interpreted as a `.` character.

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.percent.2e.handling.strategy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Aliases                  | `org.forgerock.agents.percent.2e.handling.strategy`   Introduced in Java Agent 2024.11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Function                 | Configure behaviour                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Supported settings       | * REJECT_OUTRIGHT

  Any and all occurrences of the specified sequence within the incoming URL will cause the agent to reject the incoming request with HTTP 400.

* ACCEPT_BUT_NOT_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, but the sequence will be left decoded.

* ACCEPT_AND_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, and the sequence will be decoded for the purposes of not-enforced rule matching and AM policy evaluation |
| Default                  | `REJECT_OUTRIGHT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Bootstrap property       | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

---

---
title: Control Handling of the URL Encoded Sequence %2f
description: This property controls whether the encoding sequence %2f, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.percent.2f.handling.strategy
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.percent.2f.handling.strategy.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Control Handling of the URL Encoded Sequence %2f

This property controls whether the encoding sequence `%2f`, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.

When set to `REJECT_OUTRIGHT`, if the sequence `%2f` occurs anywhere in the incoming URI path, or path parameters, the agent will reject the incoming request with an HTTP 400 response.

When set to `ACCEPT_BUT_NOT_INTERPRET`, any occurrence of `%2f` in the incoming URI path, or path parameters, will be left unconverted.

When set to `ACCEPT_AND_INTERPRET`, any occurrence of `%2f` in the incoming URI path, or path parameters, will be replaced by a forward slash character.

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.percent.2f.handling.strategy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Aliases                  | `org.forgerock.agents.percent.2f.handling.strategy`   Introduced in Java Agent 2024.11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Function                 | Configure behaviour                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Supported settings       | * REJECT_OUTRIGHT

  Any and all occurrences of the specified sequence within the incoming URL will cause the agent to reject the incoming request with HTTP 400.

* ACCEPT_BUT_NOT_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, but the sequence will be left decoded.

* ACCEPT_AND_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, and the sequence will be decoded for the purposes of not-enforced rule matching and AM policy evaluation |
| Default                  | `REJECT_OUTRIGHT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Bootstrap property       | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

---

---
title: Control Handling of the URL Encoded Sequence %3b
description: This property controls whether the encoding sequence %3b, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.percent.3b.handling.strategy
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.percent.3b.handling.strategy.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Control Handling of the URL Encoded Sequence %3b

This property controls whether the encoding sequence `%3b`, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.

When set to `REJECT_OUTRIGHT`, if the sequence `%3b` occurs anywhere in the incoming URI path, or path parameters, the agent will reject the incoming request with an HTTP 400 response..

When set to `ACCEPT_BUT_NOT_INTERPRET`, any occurrence of `%3b` in the incoming URI path, or path parameters, will be left unconverted.

When set to `ACCEPT_AND_INTERPRET`, any occurrence of `%3b` in the incoming URI path will be replaced by a semicolon and used as a path segment/path parameter separator.

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.percent.3b.handling.strategy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Aliases                  | `org.forgerock.agents.percent.3b.handling.strategy`   Introduced in Java Agent 2024.11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Function                 | Configure behaviour                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Supported settings       | * REJECT_OUTRIGHT

  Any and all occurrences of the specified sequence within the incoming URL will cause the agent to reject the incoming request with HTTP 400.

* ACCEPT_BUT_NOT_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, but the sequence will be left decoded.

* ACCEPT_AND_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, and the sequence will be decoded for the purposes of not-enforced rule matching and AM policy evaluation |
| Default                  | `REJECT_OUTRIGHT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Bootstrap property       | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

---

---
title: Control Handling of the URL Encoded Sequence %5c
description: This property controls whether the encoding sequence %5c, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.percent.5c.handling.strategy
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.percent.5c.handling.strategy.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Control Handling of the URL Encoded Sequence %5c

This property controls whether the encoding sequence `%5c`, if used in incoming URL paths, is rejected, accepted (without decoding) or decoded.

When set to `REJECT_OUTRIGHT`, if the sequence `%5c` occurs anywhere in the incoming URI path, or path parameters, the agent will reject the incoming request with an HTTP 400 response.

When set to `ACCEPT_BUT_NOT_INTERPRET`, any occurrence of `%5c` in the incoming URI path, or path parameters, will be left unconverted.

When set to `ACCEPT_AND_INTERPRET`, any occurrence of `%5c` in the incoming URI path, or path parameters, will be replaced by a forward slash character.

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Property name            | `org.forgerock.agents.percent.5c.handling.strategy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Aliases                  | `org.forgerock.agents.percent.5c.handling.strategy`   Introduced in Java Agent 2024.11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Function                 | Configure behaviour                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Supported settings       | * REJECT_OUTRIGHT

  Any and all occurrences of the specified sequence within the incoming URL will cause the agent to reject the incoming request with HTTP 400.

* ACCEPT_BUT_NOT_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, but the sequence will be left decoded.

* ACCEPT_AND_INTERPRET

  Occurrences of the specified sequence within the incoming URL will not cause the agent to reject the incoming request, and the sequence will be decoded for the purposes of not-enforced rule matching and AM policy evaluation |
| Default                  | `REJECT_OUTRIGHT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Bootstrap property       | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Required property        | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Restart required         | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Local configuration file | `AgentConfig.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

---

---
title: Convert SSO Tokens Into OIDC JWTs
description: For each incoming request, the agent looks for an OIDC JWT in the cookie named by JWT Cookie Name. Set this property as follows:
component: java-agents
version: 2026
page_id: java-agents:properties-reference:org.forgerock.agents.accept.ipdp.cookie
canonical_url: https://docs.pingidentity.com/java-agents/2026/properties-reference/org.forgerock.agents.accept.ipdp.cookie.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
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

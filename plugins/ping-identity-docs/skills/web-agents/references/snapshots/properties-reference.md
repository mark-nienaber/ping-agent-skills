---
title: Accept Secure Cookies From AM Over HTTP
description: A flag to accept secure cookies.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.forgerock.agents.config.plain.channels.insecure
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.forgerock.agents.config.plain.channels.insecure.html
---

# Accept Secure Cookies From AM Over HTTP

A flag to accept secure cookies.

When `true`, the agent accepts secure cookies from AM over HTTP. When `false`, the agent rejects them.

For requests that arrive over a secure channel, by default, AM upgrades cookies to secure. However, during internal communication with the agent, AM can send these secure cookies over HTTP.

|   |                                                               |
| - | ------------------------------------------------------------- |
|   | It is best practice to use HTTPS for *all* connections to AM. |

Default: `false`

|                    |                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------- |
| Property name      | `com.forgerock.agents.config.plain.channels.insecure`   Introduced in Web Agent 5.7 |
| Function           | Encryption                                                                          |
| Type               | Integer                                                                             |
| Bootstrap property | Yes                                                                                 |
| Required property  | No                                                                                  |
| Restart required   | No                                                                                  |

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

---

---
title: Accept SSO Token
description: A flag for whether the agent accepts SSO tokens and ID tokens as session cookies:
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.forgerock.agents.accept.sso.token
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.forgerock.agents.accept.sso.token.html
---

# Accept SSO Token

A flag for whether the agent accepts SSO tokens and ID tokens as session cookies:

* `0`. The agent does not accept SSO tokens as session cookies.

* `1`. The agent accepts both SSO tokens and ID tokens as session tokens during the login flow, and afterwards. SSO tokens *are not converted* to ID tokens. Set this property to `1` only for environments migrating from earlier versions of the agent, in the following scenarios:

  * Your custom login pages use SSO tokens as session tokens, and [Custom Login Mode](org.forgerock.openam.agents.config.allow.custom.login.html) is set to `2`.

  * Your applications, for example, REST or JavaScript clients, can only set SSO tokens.

The SSO token name is given by [Cookie Name](com.sun.identity.agents.config.cookie.name.html).

If the agent receives a request with both an SSO token and an ID token, it checks the ID token first. If invalid, it checks the SSO token. If both are invalid, the agent redirects the user for authentication.

The agent caches session information for SSO tokens.

Configure this property with [Custom Login Mode](org.forgerock.openam.agents.config.allow.custom.login.html), as described in [Login redirect configuration options](../user-guide/login-redirect.html#table-login-redirect) in the *User Guide*.

Default: `0`

|                    |                                                                       |
| ------------------ | --------------------------------------------------------------------- |
| Property name      | `com.forgerock.agents.accept.sso.token`   Introduced in Web Agent 5.7 |
| Function           | Cookies                                                               |
| Type               | Integer                                                               |
| Bootstrap property | No                                                                    |
| Required property  | No                                                                    |
| Restart required   | No                                                                    |
| AM console         | Tab: `SSO`Title: `Accept SSO Token`                                   |

---

---
title: Accept SSO token cookie (deprecated)
description: Use Accept SSO Token instead of this property.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.forgerock.agents.accept.ipdp.cookie
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.forgerock.agents.accept.ipdp.cookie.html
---

# Accept SSO token cookie (deprecated)

Use [Accept SSO Token](com.forgerock.agents.accept.sso.token.html) instead of this property.

|                    |                                                                         |
| ------------------ | ----------------------------------------------------------------------- |
| Property name      | `com.forgerock.agents.accept.ipdp.cookie`   Introduced in Web Agent 5.7 |
| Function           | Profile                                                                 |
| Type               | Integer                                                                 |
| Bootstrap property | No                                                                      |
| Required property  | No                                                                      |
| Restart required   | No                                                                      |
| AM console         | Tab: `Global`Title: `Accept SSO token cookie (deprecated)`              |

---

---
title: Add Cache-Control Headers
description: When true, enables the use of Cache-Control headers to prevent proxies from caching resources accessed by unauthenticated users.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.forgerock.agents.cache_control_header.enable
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.forgerock.agents.cache_control_header.enable.html
---

# Add Cache-Control Headers

When `true`, enables the use of Cache-Control headers to prevent proxies from caching resources accessed by unauthenticated users.

Default: `false`

|                    |                                                                                  |
| ------------------ | -------------------------------------------------------------------------------- |
| Property name      | `com.forgerock.agents.cache_control_header.enable`   Introduced in Web Agent 4.x |
| Function           | Headers                                                                          |
| Type               | Boolean: `true` returns true; all other strings return `false`.                  |
| Bootstrap property | No                                                                               |
| Required property  | No                                                                               |
| Restart required   | No                                                                               |
| AM console         | Tab: `Miscellaneous`Title: `Add Cache-Control Headers`                           |

---

---
title: Agent Authentication Mode
description: Configure the authentication mechanism that the Agent uses to login to PingAM.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.forgerock.agents.config.agent.auth.mode
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.forgerock.agents.config.agent.auth.mode.html
---

# Agent Authentication Mode

Configure the authentication mechanism that the Agent uses to login to PingAM.

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingAM 7.3 and 7.4 may have session quota issues with agents and authentication trees. Starting with PingAM 7.5, there should be no session quota issues. |

Advanced Identity Cloud is not impacted by session quotas for Agents. This property should be set to `1` if the agent is connecting to Advanced Identity Cloud.

* `1`: Agent authentication using only Trees/Journeys.

* `2`: Agent authentication using only deprecated authentication modules.

Default: `1`

|                    |                                                                                 |
| ------------------ | ------------------------------------------------------------------------------- |
| Property name      | `com.forgerock.agents.config.agent.auth.mode`   Introduced in Web Agent 2024.11 |
| Function           | Miscellaneous                                                                   |
| Type               | Integer                                                                         |
| Bootstrap property | Yes                                                                             |
| Required property  | No                                                                              |
| Restart required   | No                                                                              |

---

---
title: Agent Debug File Size
description: File size in bytes at which the debug log file is rotated.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.sun.identity.agents.config.debug.file.size
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.sun.identity.agents.config.debug.file.size.html
---

# Agent Debug File Size

File size in bytes at which the debug log file is rotated.

Default: `0`, debug log file is never rotated

|                    |                                                                                |
| ------------------ | ------------------------------------------------------------------------------ |
| Property name      | `com.sun.identity.agents.config.debug.file.size`   Introduced in Web Agent 4.x |
| Function           | Debug                                                                          |
| Type               | Integer                                                                        |
| Bootstrap property | Yes                                                                            |
| Required property  | No                                                                             |
| Restart required   | No                                                                             |
| AM console         | Tab: `Global (From AM 7.1)`Title: `Agent Debug File Size`                      |

---

---
title: Agent Debug Level
description: Debug level. Set to one of the constrained values.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.sun.identity.agents.config.debug.level
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.sun.identity.agents.config.debug.level.html
---

# Agent Debug Level

Debug level. Set to one of the constrained values.

Default: `Error`

|                    |                                                                            |
| ------------------ | -------------------------------------------------------------------------- |
| Property name      | `com.sun.identity.agents.config.debug.level`   Introduced in Web Agent 4.x |
| Function           | Debug                                                                      |
| Type               | Constrained Values: "info", "warning", "error", "debug", "all"             |
| Bootstrap property | Yes                                                                        |
| Required property  | No                                                                         |
| Restart required   | No                                                                         |
| AM console         | Tab: `Global`Title: `Agent Debug Level`                                    |

---

---
title: Agent Deployment URI Prefix
description: Overrides the request URL given by the agent, when the agent is configured behind a load balancer or proxy. Use this property when the protocol, hostname, or port of the load balancer or proxy differ from those of the agent.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.sun.identity.agents.config.agenturi.prefix
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.sun.identity.agents.config.agenturi.prefix.html
---

# Agent Deployment URI Prefix

Overrides the request URL given by the agent, when the agent is configured behind a load balancer or proxy. Use this property when the protocol, hostname, or port of the load balancer or proxy differ from those of the agent.

At least one of the following properties must be enabled:

* [Enable Override Request URL Port](com.sun.identity.agents.config.override.port.html)

* [Enable Override Request URL Protocol](com.sun.identity.agents.config.override.protocol.html)

* [Enable Override Request URL Host](com.sun.identity.agents.config.override.host.html)

Use these properties only if you are not using `x-forwarded` headers from the load balancer or proxy to override the agent's protocol, hostname, and port values.

Default: `agent-root-URL`

|                    |                                                                                |
| ------------------ | ------------------------------------------------------------------------------ |
| Property name      | `com.sun.identity.agents.config.agenturi.prefix`   Introduced in Web Agent 4.x |
| Function           | Profile                                                                        |
| Type               | String                                                                         |
| Bootstrap property | No                                                                             |
| Required property  | No                                                                             |
| Restart required   | No                                                                             |
| AM console         | Tab: `Global`Title: `Agent Deployment URI Prefix`                              |

---

---
title: Agent Logout URL Regular Expression (deprecated)
description: "d: 2023.9"
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.forgerock.agents.agent.logout.url.regex
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.forgerock.agents.agent.logout.url.regex.html
---

# Agent Logout URL Regular Expression (deprecated)

d: 2023.9

A Perl-compatible or ECMAScript-compatible (IIS) regular expression that resolves to one or more application logout URLs.

This property is deprecated; use [Agent Logout URL Regular Expression (deprecated)](com.forgerock.agents.agent.logout.url.regex.html) instead.

If this property is used, it is evaluated before [Enable Regex for Logout URL List](org.forgerock.agents.config.logout.regex.enable.html).

You can find more details about the logout flow and properties to manage logout in [Trigger logout with a URL](../user-guide/logout.html##trigger_logout_with_a_url) in the *User Guide*.

Example: `com.forgerock.agents.agent.logout.url.regex=https:\/\/example.domain.com:443\/(protectedA|protectedB)\?(.\&)*op=logout(\&.)*$`

Default: Empty

|                    |                                                                                         |
| ------------------ | --------------------------------------------------------------------------------------- |
| Property name      | `com.forgerock.agents.agent.logout.url.regex`   Introduced in Web Agent 4.x             |
| Function           | Logout redirect                                                                         |
| Type               | String                                                                                  |
| Bootstrap property | No                                                                                      |
| Required property  | No                                                                                      |
| Restart required   | No                                                                                      |
| AM console         | Tab: `AM Services (From AM 7)`Title: `Agent Logout URL Regular Expression (deprecated)` |

---

---
title: Agent Profile ID Allow List
description: A comma-separated list of profile IDs that the agent considers as valid values for the aud claim. This claim is represented in the ID token containing the end user's session.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.forgerock.agents.jwt.aud.whitelist
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.forgerock.agents.jwt.aud.whitelist.html
---

# Agent Profile ID Allow List

A comma-separated list of profile IDs that the agent considers as valid values for the `aud` claim. This claim is represented in the ID token containing the end user's session.

When several agents are configured with different agent profiles to protect the same application, set this property to a list of the agent profiles that are protecting the same application.

With the following setting, the agent considers `agentprofile1` and `agentprofile2` to be valid, and does not validate them: `com.forgerock.agents.jwt.aud.whitelist=agentprofile1,agentprofile2`

Default: Empty

|                    |                                                                        |
| ------------------ | ---------------------------------------------------------------------- |
| Property name      | `com.forgerock.agents.jwt.aud.whitelist`   Introduced in Web Agent 5.7 |
| Function           | Profile                                                                |
| Type               | String                                                                 |
| Bootstrap property | No                                                                     |
| Required property  | No                                                                     |
| Restart required   | No                                                                     |
| AM console         | Tab: `Global`Title: `Agent Profile ID Allow List`                      |

---

---
title: Agent Profile Name
description: The name of the agent profile in AM.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.sun.identity.agents.config.username
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.sun.identity.agents.config.username.html
---

# Agent Profile Name

The name of the agent profile in AM.

|                    |                                                                         |
| ------------------ | ----------------------------------------------------------------------- |
| Property name      | `com.sun.identity.agents.config.username`   Introduced in Web Agent 4.x |
| Function           | Agent profile                                                           |
| Type               | String                                                                  |
| Bootstrap property | Yes                                                                     |
| Required property  | No                                                                      |
| Restart required   | No                                                                      |

---

---
title: Agent Profile Password
description: The password required by the agent profile and encrypted with the key specified in Agent Profile Password Encryption Key.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.sun.identity.agents.config.password
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.sun.identity.agents.config.password.html
---

# Agent Profile Password

The password required by the agent profile and encrypted with the key specified in [Agent Profile Password Encryption Key](com.sun.identity.agents.config.key.html).

This property is provided in the `agent-password.conf` file.

To encrypt an agent profile password, run the `agentadmin` command with the `--p` option.

When the agent can't decrypt the password it writes a message to the logs.

Default: Empty

|                    |                                                                         |
| ------------------ | ----------------------------------------------------------------------- |
| Property name      | `com.sun.identity.agents.config.password`   Introduced in Web Agent 4.x |
| Function           | Agent profile                                                           |
| Type               | String                                                                  |
| Bootstrap property | Yes                                                                     |
| Required property  | No                                                                      |
| Restart required   | No                                                                      |

---

---
title: Agent Profile Password Encryption Key
description: The key used to encrypt the agent profile password in Agent Profile Password
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.sun.identity.agents.config.key
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.sun.identity.agents.config.key.html
---

# Agent Profile Password Encryption Key

The key used to encrypt the agent profile password in [Agent Profile Password](com.sun.identity.agents.config.password.html)

This property is provided in the `agent-key.conf` file.

To create a encryption key, run the `agentadmin` command with the `--k` option.

Default: Empty

|                    |                                                                    |
| ------------------ | ------------------------------------------------------------------ |
| Property name      | `com.sun.identity.agents.config.key`   Introduced in Web Agent 4.x |
| Function           | Agent profile                                                      |
| Type               | String                                                             |
| Bootstrap property | Yes                                                                |
| Required property  | No                                                                 |
| Restart required   | No                                                                 |

---

---
title: Agent Profile Realm
description: The AM realm where the agent profile is located. For example, /Customers.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.sun.identity.agents.config.organization.name
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.sun.identity.agents.config.organization.name.html
---

# Agent Profile Realm

The AM realm where the agent profile is located. For example, `/Customers`.

Realm names are case-sensitive. Failure to set the realm name exactly as configured in AM causes the agent to fail to recognize the realm.

Default: `/`

|                    |                                                                                  |
| ------------------ | -------------------------------------------------------------------------------- |
| Property name      | `com.sun.identity.agents.config.organization.name`   Introduced in Web Agent 4.x |
| Function           | Agent profile                                                                    |
| Type               | String                                                                           |
| Bootstrap property | Yes                                                                              |
| Required property  | No                                                                               |
| Restart required   | No                                                                               |

---

---
title: Agent Root URL for CDSSO
description: The agent root URLs for CDSSO. The valid value is in the format protocol://hostname:port/, where protocol represents the protocol used, such as http or https, hostname represents the host name of the system where the agent resides, and port represents the port number on which the agent is installed. The slash following the port number is required.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:sunIdentityServerDeviceKeyValue
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/sunIdentityServerDeviceKeyValue.html
---

# Agent Root URL for CDSSO

The agent root URLs for CDSSO. The valid value is in the format `protocol://hostname:port/`, where protocol represents the protocol used, such as `http` or `https`, hostname represents the host name of the system where the agent resides, and port represents the port number on which the agent is installed. The slash following the port number is required.

If your agent system has virtual host names, add URLs with the virtual host names to this list. AM checks that the `goto` URLs match one of the agent root URLs for CDSSO.

Default: `agent-root-URL`

|                    |                                                                 |
| ------------------ | --------------------------------------------------------------- |
| Property name      | `sunIdentityServerDeviceKeyValue`   Introduced in Web Agent 4.x |
| Function           | Profile                                                         |
| Type               | Unused                                                          |
| Bootstrap property | No                                                              |
| Required property  | No                                                              |
| Restart required   | No                                                              |
| AM console         | Tab: `Global`Title: `Agent Root URL for CDSSO`                  |

---

---
title: AM Conditional Login URL
description: Conditionally redirect users based on the incoming request URL.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.forgerock.agents.conditional.login.url
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.forgerock.agents.conditional.login.url.html
---

# AM Conditional Login URL

Conditionally redirect users based on the incoming request URL.

If the incoming request URL matches a domain name in this list, the agent redirects the unauthenticated request to the specified URL for login. The URL can be an AM instance, site, or a different website.

Format, with no spaces between values:

`[String]|[URL, URL…​][?service=value2]`

* \[String]

  Incoming login request URLs, with the following values:

  * `Domain`: Agents match both the domain and its subdomains. For example, `example.com` matches `mydomain.example.com` and `www.example.com`. To combine domain and path, provide the port number: `www.example.com:8443/market`.

  * `Subdomain`: For example, `example.com`. To combine subdomain and path, provide the port number: `example.com:8443/market`.

  * `Path`: For example, `/myapp`.

  * Anything in the request URL: For example, a port, such as `8443`.

  * No value: Nothing is specified before the pipe (`|`) character. Conditional rules that do not specify the incoming request's domain apply to every incoming request.

  To specify the string as a regular expression, configure the following properties instead: [Regular Expression Conditional Login Pattern](org.forgerock.agents.config.conditional.login.pattern.html) and [Regular Expression Conditional Login URL](org.forgerock.agents.config.conditional.login.url.html).

* \[URL, URL…​]

  The URL to which incoming login requests are redirected. The URL can be the following:

  * AM instance or site: Specify the URL of an AM instance or site in the format `protocol://FQDN[:port]/URI/oauth2/realms/root/realms/value/authorize`, where the port is optional if it is `80` or `443`. For example, `https://am.example.com/am/oauth2/realms/root/realms/alpha/authorize`.

  * The realm where the agent should log users in should be specified in the URL. Prefix each realm in the hierarchy with the `realms` keyword. For example, `/realms/root/realms/alpha`.

    You do not need to specify the realm if any of the following conditions is true:

  * The custom login page sets the realm parameter, for example, because it lets the user chose it. In this case, ensure the custom login page always appends a realm parameter to the goto URL.

  * The realm where the agent must log the user to has DNS aliases configured in AM. AM logs the user in to the realm whose DNS alias matches the incoming request URL. For example, an inbound request from `http://marketplace.example.com` URL logs into the marketplace realm if the realm alias is set to `marketplace.example.com`.

  * The users should always log in to the top level realm.

  If you specify the realm by default, this parameter can be overwritten by the custom login page if, for example, the user can chose the realm for authentication.

  * Website other than AM: Specify a URL in the format `protocol://FQDN[:port]/URI`, where the port is optional if it is ``80 or `443``. For example, `https://myweb.example.com/authApp`.

  * List of AM instances or sites, or websites other than AM: If the redirection URL is not specified, the agent redirects the request to the AM instance or site specified by [AM Connection URL](com.sun.identity.agents.config.naming.url.html).

* \&service=value2

  A parameter that can be added to the URL(s) to specify the authentication tree the user authenticates against. For example, `?service=myTree`.

Include any other parameters your custom login pages require. Chain parameters with an ampersand (`&`) character, for example, `service=value&param=value`.

When configuring conditional login with multiple URLs, set up the parameters for each URL.

Examples:

`com.forgerock.agents.conditional.login.url[0]=example.com|https://am.example.com/am/oauth2/realms/root/authorize`

`com.forgerock.agents.conditional.login.url[1]=myapp.domain.com|https://am2.example.com/am/oauth2/realms/root/realms/alpha/authorize`

`com.forgerock.agents.conditional.login.url[3]=sales.example.com/marketplace|https://am1.example.com/am/oauth2/realms/root/realms/sales/authorize, https://am2.example.com/am/oauth2/realms/root/realms/marketplace/authorize`

`com.forgerock.agents.conditional.login.url[5]=|https://am3.example.com/am/oauth2/realms/root/realms/alpha/authorize?service=myTree`

Learn more in [Login redirect](../user-guide/login-redirect.html) in the *User Guide*.

|                    |                                                                            |
| ------------------ | -------------------------------------------------------------------------- |
| Property name      | `com.forgerock.agents.conditional.login.url`   Introduced in Web Agent 4.x |
| Function           | Login redirect                                                             |
| Type               | String Map                                                                 |
| Bootstrap property | No                                                                         |
| Required property  | No                                                                         |
| Restart required   | No                                                                         |
| AM console         | Tab: `AM Services`Title: `AM Conditional Login URL`                        |

---

---
title: AM Connection URL
description: A space-delimited list of AM URLs to which the agent connects. Set this property to the URL of the load balancer in front of the AM instances (or load balancers, in case of disaster-recovery configurations).
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.sun.identity.agents.config.naming.url
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.sun.identity.agents.config.naming.url.html
---

# AM Connection URL

A space-delimited list of AM URLs to which the agent connects. Set this property to the URL of the load balancer in front of the AM instances (or load balancers, in case of disaster-recovery configurations).

When the agent cannot connect to the first URL in the list, it automatically connects to the next available URL. The agent stays connected to the new URL until the URL fails, or the agent is restarted.

Default: `AM_URL/am/`

|                    |                                                                           |
| ------------------ | ------------------------------------------------------------------------- |
| Property name      | `com.sun.identity.agents.config.naming.url`   Introduced in Web Agent 4.x |
| Function           | Miscellaneous                                                             |
| Type               | String List                                                               |
| Bootstrap property | Yes                                                                       |
| Required property  | No                                                                        |
| Restart required   | No                                                                        |

---

---
title: AM Login URL
description: The URL of a custom login page to which the agent redirects users for authentication.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.sun.identity.agents.config.login.url
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.sun.identity.agents.config.login.url.html
---

# AM Login URL

The URL of a custom login page to which the agent redirects users for authentication.

|   |                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When redirecting incoming login requests to a custom login page, add the login page to [Not-Enforced IP List](com.sun.identity.agents.config.notenforced.ip.html) or [Not-Enforced URL List](com.sun.identity.agents.config.notenforced.url.html). |

The login URL has the format `URL[?realm=realm_name&parameter1=value1&…​]`, where:

* `URL` is the custom SSO-token-compliant login page to where the agent redirects the unauthenticated users.

* `[?realm=realm_name?parameter1=/value1&…​]` specifies optional parameters that the agent will pass to the custom login page, for example, the AM realm which the user should log into.

Specify as many parameters as your custom login pages require: `https://login.example.com/login.jsp?realm=marketplace&param1=value1`

You do not need to specify the realm in the login URL if any of the following conditions is true:

* The custom login page itself sets the `realm` parameter, for example, because it lets the user chose it. In this case, you must ensure the custom login page *always* appends a `realm` parameter to the `goto` URL.

* The realm where the agent must log the user to has DNS aliases configured in AM. AM will log in the user to the realm whose DNS alias matches the incoming request URL. For example, an inbound request from the `https://marketplace.example.com` URL logs into the `marketplace` realm if the realm alias is set to `marketplace.example.com`.

* Users should always log in to the Top Level Realm.

Even if you specify the realm by default, this parameter can be overwritten by the custom login page if, for example, the user can chose the realm for authentication.

Default: `AMURL/am/UI/Login`

|                    |                                                                          |
| ------------------ | ------------------------------------------------------------------------ |
| Property name      | `com.sun.identity.agents.config.login.url`   Introduced in Web Agent 4.x |
| Function           | Login redirect                                                           |
| Type               | String Map                                                               |
| Bootstrap property | No                                                                       |
| Required property  | No                                                                       |
| Restart required   | No                                                                       |
| AM console         | Tab: `AM Services`Title: `AM Login URL`                                  |

---

---
title: AM Logout URL
description: The page to which the agent redirects the end user on log out. It can be a page in AM, such as https://am.example.com:8443/am/UI/Logout?realm=/alpha, or a page in the application.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.sun.identity.agents.config.logout.url
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.sun.identity.agents.config.logout.url.html
---

# AM Logout URL

The page to which the agent redirects the end user on log out. It can be a page in AM, such as `https://am.example.com:8443/am/UI/Logout?realm=/alpha`, or a page in the application.

The AM logout page invalidates the user session in AM, but pages in an application might not invalidate the user session in AM. See [Enable Invalidate Logout Session](org.forgerock.agents.config.logout.session.invalidate.html) for configuration options.

Default: `AM_URL/am/UI/Logout`

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | By default, a realm is not included in the logout URL, and the user is redirected to the root realm on logout. Take care to include a realm if required. |

|                    |                                                                           |
| ------------------ | ------------------------------------------------------------------------- |
| Property name      | `com.sun.identity.agents.config.logout.url`   Introduced in Web Agent 4.x |
| Function           | Logout redirect                                                           |
| Type               | String Map                                                                |
| Bootstrap property | No                                                                        |
| Required property  | No                                                                        |
| Restart required   | No                                                                        |
| AM console         | Tab: `AM Services`Title: `AM Logout URL`                                  |

---

---
title: Anonymous User
description: Enable or disable REMOTE_USER processing for anonymous users.
component: web-agents
version: 2026
page_id: web-agents:properties-reference:com.sun.identity.agents.config.anonymous.user.enable
canonical_url: https://docs.pingidentity.com/web-agents/2026/properties-reference/com.sun.identity.agents.config.anonymous.user.enable.html
---

# Anonymous User

Enable or disable REMOTE\_USER processing for anonymous users.

Default: `false`

|                    |                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------ |
| Property name      | `com.sun.identity.agents.config.anonymous.user.enable`   Introduced in Web Agent 4.x |
| Function           | Client identification                                                                |
| Type               | Boolean: `true` returns true; all other strings return `false`.                      |
| Bootstrap property | No                                                                                   |
| Required property  | No                                                                                   |
| Restart required   | No                                                                                   |
| AM console         | Tab: `Miscellaneous`Title: `Anonymous User`                                          |
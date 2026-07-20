---
title: About Web Agent
description: "Overview of PingAM Web Agent: components, configuration locations, request processing flow, realms, and session management."
component: web-agents
version: 2026
page_id: web-agents:user-guide:about
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/about.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  about-components: Agent components
  configuration-location: Agent configuration
  configuration_location: Configuration location
  centralized_configuration: Centralized configuration
  agentconf: Local configuration
  configuration_files: Configuration files
  agent_password_conf: agent-password.conf
  agent_key_conf: agent-key.conf
  agent_conf: agent.conf
  request-process-flow: Request process flow
  realms: Realms
  agent_profile_realm: Agent profile realm
  policy_evaluation_realm: Policy evaluation realm
  user_realm: User realm
  sessions: Sessions
---

# About Web Agent

Web Agent is a PingAM or Advanced Identity Cloud add-on component that operates as a Policy Enforcement Point (PEP) or policy agent for applications deployed in a web server.

Web Agents intercept inbound requests to applications. Depending on the *filter mode* configuration, Web Agents interact with AM to:

* Ensure that clients provide appropriate authentication.

* Enforce AM resource-based policies.

  For information about how to enforce user authentication only, refer to [SSO-only mode](sso-only-mode.html).

This chapter covers how Web Agent works and how it protects applications.

## Agent components

Web Agent includes the following main components:

* Agent Modules

  Intercepts and processes inbound requests to protected resources.

* Native Shared Libraries

  Enables agents to interact with AM.

* Agent Profile

  The agent profile is not strictly part of Web Agent, but plays an important part in the agent operation. It contains a set of configuration properties that define the agent behavior.

The following image shows the Web Agent components when the agent profile is stored in the AM configuration store:

![Web Agent components](_images/web-policy-agent.svg)

## Agent configuration

Web Agent configuration properties decide the behavior of the agent.

### Configuration location

AM stores configuration properties either centrally or in local configuration files.

#### Centralized configuration

When the agent is operating in [centralized configuration mode](glossary.html#def-central-configuration-mode) its configuration is stored in the AM configuration store. Storing the agent configuration centrally allows you to configure your agents using the AM admin UI, and the REST API.

To access the centralized web agent configuration, on the AM admin UI go to Realms > *Realm Name* > Applications > Agents > Web > *Agent Name*.

Configure properties that aren't present in the AM admin UI as *custom properties*, on the Advanced tab of the console. For a list of property names, refer to the [Properties reference](../properties-reference/preface.html).

When properties and value pairs are defined as custom properties, they take precedence for that property. To prevent configuration errors, if a property is present in the AM admin UI don't configure it as a custom property.

For information about creating centrally-stored agent profiles, refer to [Create agent profiles](../installation-guide/pre-installation.html#create-agent-profiles).

#### Local configuration

When the agent is operating in [local configuration mode](glossary.html#def-local-configuration-mode) the agent bootstrap properties, configuration properties, and password are stored in local files created by the installer.

### Configuration files

Web Agent uses the configuration files described in this section. For information about agent properties, refer to the [Properties reference](../properties-reference/preface.html).

#### `agent-password.conf`

AES-256-GCM encrypted password properties, including the agent profile password, stored at `/path/to/web_agents/agent_type/instances/agent_n/config/agent-password.conf`.

```none
#------------------------------------------------------------------------------
# Web Agents Passwords
...
#------------------------------------------------------------------------------
com.sun.identity.agents.config.password = AM_AGENT_PASSWORD
com.forgerock.agents.config.cert.key.password = AM_SSL_PASSWORD
com.sun.identity.agents.config.forward.proxy.password = AM_PROXY_PASSWORD
```

#### `agent-key.conf`

The key to decrypt the agent password in `agent-password.conf`, stored at `/path/to/web_agents/agent_type/instances/agent_n/config/agent-key.conf`.

```none
#------------------------------------------------------------------------------
# Web Agents Encryption Key
...
#------------------------------------------------------------------------------
com.sun.identity.agents.config.key = AM_AGENT_KEY
```

#### `agent.conf`

Bootstrap and configuration settings, stored at `/path/to/web_agents/agent_type/instances/agent_n/config/agent.conf`.

To manage the configuration, edit `agent.conf` manually. The `agent.conf` file can't be updated using the AM admin UI, or the REST API.

The `agent.conf` file must contain at least the following properties:

```none
# Bootstrap properties
com.sun.identity.agents.config.organization.name = AM_AGENT_REALM
com.sun.identity.agents.config.username = AM_AGENT_NAME
com.sun.identity.agents.config.naming.url = AM_OPENAM_URL

# Configuration properties
com.sun.identity.agents.config.repository.location = local
org.forgerock.openam.agents.config.jwt.name = am-auth-jwt
com.sun.identity.agents.config.cdsso.redirect.uri = agent/cdsso-oauth2
org.forgerock.openam.agents.config.policy.evaluation.application = iPlanetAMWebAgentService
org.forgerock.openam.agents.config.policy.evaluation.realm = /
com.sun.identity.agents.config.polling.interval = 180
com.sun.identity.agents.config.sso.cache.polling.interval = 60
com.sun.identity.agents.config.policy.cache.polling.interval = 60
com.sun.identity.agents.config.cookie.name = iPlanetDirectoryPro
com.sun.identity.agents.config.debug.file.size = 0
com.sun.identity.agents.config.local.logfile = AM_DEBUG_FILE_PATHdebug.log
com.sun.identity.agents.config.local.audit.logfile = AM_AUDIT_FILE_PATHaudit.log
com.sun.identity.agents.config.debug.level = error
```

## Request process flow

When a client requests access to an application resource, the Web Agent intercepts the request. AM then validates the identity of the client, and their authorization to access the protected resource.

The following simplified data flow occurs when an unauthenticated client requests a resource protected by a Web Agent and AM. The flow assumes that requests must meet the requirements of an AM policy. For a detailed diagram, refer to [Single sign-on](https://docs.pingidentity.com/pingam/8.1/am-authentication/about-sso.html) in AM's *Authentication and SSO guide*.

![Flow of a request through an agent.](_images/web-agent-process-flow.svg)

* FQDN check

  When FQDN checking is enabled, the agent can redirect requests to different domains, depending on the hostname of the request. Learn more in [FQDN checks](fqdn-checking.html).

* Not-enforced rules check

  The agent evaluates whether the requested resource or the client IP address matches a not-enforced rule.

  * *Alternate flow*. The requested resource or the client IP address matches a not-enforced rule. The agent allows access to the resource.

  * *Alternate flow*. The client receives a response from `www.example.com`. The flow ends.

  * The requested resource or the client IP address does not match a not-enforced rule. The agent redirects the client to log in to AM.

  Learn more in [Not-enforced rules](not-enforced-rules.html).

* Authentication

  1-2: The client authenticates to AM.

  During client authentication, and to protect against reply attacks, the agent issues a pre-authentication cookie, named `agent-authn-tx`. The agent uses the cookie to track the authentication request to AM, and deletes it immediately after authentication.

  Depending on the configuration, the agent can either issue a single cookie to track all concurrent authentication requests, or one cookie for each request.

  The pre-authentication cookie expires after 5 minutes, or after the time specified in [Profile Attributes Cookie Maxage](../properties-reference/com.sun.identity.agents.config.profile.attribute.cookie.maxage.html).

  If POST data preservation is enabled, the request expires after the time specified in [POST Data Entries Cache Period](../properties-reference/com.sun.identity.agents.config.postcache.entry.lifetime.html), which is by default 10 minutes. In this case, consider increasing [Profile Attributes Cookie Maxage](../properties-reference/com.sun.identity.agents.config.profile.attribute.cookie.maxage.html) to at least 10 minutes.

  3: AM's authentication service verifies the client credentials and creates a valid OIDC JWT, with session information.

  4: AM sends the client a self-submitting form with the OIDC JWT.

  5: The client posts the self-submitting form to the agent endpoint, and the Web Agent consumes it.

  6: The agent contacts AM to validate the session contained in the ID token.

  7: AM validates the session.

* Authorization

  1: The agent contacts AM's policy service, requesting a decision about whether the client is authorized to access the resource.

  2: AM's policy service returns `ALLOW`.

  3: The agent writes the policy decision to the audit log.

  4: The agent enforces the policy decision. Because the Policy Service returned `ALLOW`, the agent performs a pass-through operation to return the resource to the client.

  5: The client accesses the resource.

## Realms

### Agent profile realm

The *agent profile realm* is the AM realm in which the agent profile is stored. The agent profile stores a set of configuration properties that define the behavior of the agent.

During agent installation, the installer prompts for the agent profile realm, and populates the property [Agent Profile Realm](../properties-reference/com.sun.identity.agents.config.organization.name.html) in the bootstrap properties file. By default, the agent profile realm is set to the top-level realm.

The agent profile realm can be different to the user realm and policy evaluation realm. Groups of agents can use the same agent profile realm, which can be separate from the user realm and policy evaluation realm.

For information about creating agent profiles in the top-level realm or other realms, refer to [Create agent profiles](../installation-guide/pre-installation.html#create-agent-profiles).

### Policy evaluation realm

The *policy evaluation realm* is the realm that the agent uses to request policy decisions from AM. In most circumstances, the policy evaluation realm is the same as the user realm.

The policy evaluation realm is configured by [Policy Evaluation Realm](../properties-reference/org.forgerock.openam.agents.config.policy.evaluation.realm.html), and defaults to the top-level realm. The policy set to use is configured by [Policy Set](../properties-reference/org.forgerock.openam.agents.config.policy.evaluation.application.html).

In AM, only the top-level realm has a default policy set, called iPlanetAMWebAgentService. If you use a policy evaluation realm that is in a subrealm of the top-level realm, you must also define a policy set and policies in the equivalent realm in AM.

### User realm

The *user realm* is the realm in which a user is authenticated. In most circumstances, the user evaluation realm is the same as the policy evaluation realm.

By default, users authenticate to AM in the top-level realm, however, the agent can authenticate users in different realms depending on the request domain, path, or resource.

When a user logs out, the agent maintains the user realm. The agent obtains the realm info from the JWT, if one is available, or by calling `sessioninfo`. When the user logs out, the stored realm is passed to the logout endpoint automatically.

The first time an authenticated user requests a resource from the agent, the agent establishes the user realm from the session. It permanently associates the realm with the session in the session cache. When the session ends, the agent automatically passes the realm to the logout endpoint.

For more information about changing the user realm, refer to [Login redirect](login-redirect.html).

## Sessions

On startup, Web Agent uses the following properties to obtain a session from AM:

* [Agent Profile Name](../properties-reference/com.sun.identity.agents.config.username.html)

* [Agent Profile Password](../properties-reference/com.sun.identity.agents.config.password.html)

* [Agent Profile Realm](../properties-reference/com.sun.identity.agents.config.organization.name.html)

The agent session lifetime is defined by the AM version and configuration, and is essentially indefinite.

For the security of your deployment, set the agent session lifetime as described in [Manage Web Agent sessions](../security-guide/access.html#agent_sessions).

If you clear agent sessions in the AM admin UI, you can accidentally kill an active agent session. If this happens, the agent detects that its session has expired and automatically obtains a new one.

---

---
title: Caches
description: "Configure PingAM Web Agent caches: configuration cache, session and policy decision cache, and policy cache for local authorization decisions."
component: web-agents
version: 2026
page_id: web-agents:user-guide:caching
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/caching.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  configuration-cache: Configuration cache
  session-cache: Session and policy decision cache
  policy-cache: Policy cache
---

# Caches

Web Agent supports the following caches to speed up agent operations:

## Configuration cache

The configuration cache stores web agent configuration properties.

When a Web Agent starts up, it either makes a call to AM to retrieve a copy of the agent profile ([centralized configuration mode](glossary.html#def-central-configuration-mode)) or reads the agent profile from the local configuration file ([local configuration mode](glossary.html#def-local-configuration-mode)). Then, the agent stores the configuration in its cache. The cached information is valid until one of the following events occur:

* AM notifies the agent of changes to hot-swappable agent configuration properties. This only applies to deployments that use [centralized configuration mode](glossary.html#def-central-configuration-mode).

* The information in the cache reaches the expiration time specified by [Configuration Reload Interval](../properties-reference/com.sun.identity.agents.config.polling.interval.html).

  When a configuration property in the cache is invalid, the agent clears the cached property value and rereads it from the agent profile.

## Session and policy decision cache

Stored in the shared memory pool defined by the `AM_MAX_SESSION_CACHE_SIZE` environment variable, the session and policy decision cache stores session information, and the results of previous policy decisions.

The default size of the cache is 16 MB, but you may need to increase its size if you plan to hold many active sessions in the cache at any given time. For more information about the environment variable, refer to [Environment variables](configure-envvars.html).

After authentication, AM presents the client with an ID token containing session information. The web agent stores part of that session information in the cache. When a client attempts to access a protected resource, the agent checks whether there is a policy decision cached for the resource:

* If there is a cached policy decision, the agent reuses it without contacting AM.

* If there is no cached policy decision, the validity of the client's session determines the agent's behavior:

  * If the client's session is valid, the web agent requests a policy decision from AM, caches it, and then enforces it.

  * If the client's session is not valid, the agent redirects the client to AM for authentication regardless of why the session is invalid. The agent does not specify the reason why the client needs to authenticate.

    After the client authenticates, and the session is cached, the agent requests a policy decision from AM, caches it, and then enforces it.

  Session and policy decisions are valid in the cache until one of the following events occur:

**Session and policy decision validity in cache**

| Event                                                                                                                                                                              | What is invalidated?                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Session contained in the ID token expires                                                                                                                                          | Session and policy decisions related to the session |
| Client logs out from AM (and session notifications are enabled)                                                                                                                    | Session and policy decisions related to the session |
| Session reaches the expiration time specified by [SSO Cache Polling Period](../properties-reference/com.sun.identity.agents.config.sso.cache.polling.interval.html).               | Session                                             |
| Policy decision reaches the expiration time specified by [Policy Cache Polling Period](../properties-reference/com.sun.identity.agents.config.policy.cache.polling.interval.html). | Policy decision                                     |
| Administrator makes a change to policy configuration (and policy notifications are enabled)                                                                                        | All sessions and all policy decisions               |

|   |                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A Web Agent that loses connectivity with AM cannot request policy decisions. Therefore, the agent denies access to inbound requests that do not have a policy decision cached until the connection is restored(\*). |

## Policy cache

The policy cache builds upon the session and policy decision cache. It downloads and stores details about policies from AM, and uses the downloaded policies to make authorization decisions, without contacting AM each time.

Web Agent uses the policy cache without contacting AM in the following situations:

* A requested resource matches the resource pattern of a policy that has been cached due to a previous evaluation.

* A requested resource **does not** match a pattern of policy rules downloaded locally. In this case, the agent denies access.

* A requested resource matches the resource pattern of a simple policy that applies to the `All Authenticated Users` virtual group.

  If the resource matches the policy used for a previous policy decision, the agent does not request policy evaluation from AM. Therefore, policy conditions based on scripts, LDAP filter conditions, or session properties, which rely on attributes that can vary during a session, may not be enforced.

  To reduce this risk, you should:

* Enable session property change notifications, as described in [Notifications](../maintenance-guide/notifications.html).

* Reduce the amount of time that sessions can remain in the agent session cache.

Consider the following caveats when using the policy cache:

* If you have a large number of policies, for example more than one million in an UMA deployment, the time to download the policies and the memory consumption of the agent may affect performance.

* The agent downloads the policy rules, and uses them to evaluate policies locally. If a policy is customized in AM in a way that changes the way it is evaluated (for example, a wildcard or delimiter is changed), the policy decision made by the agent might not match the policy defined in AM.

* Even though delimiters and wildcards are configurable in AM (Configure > Global Services > Policy Configuration > Global Attributes > Resource Comparator), the policy cache supports only the default configuration.

Do not enable the agent's policy cache if your policies use custom delimiters and/or wildcards.

Enable the policy cache by creating an environment variable named `AM_POLICY_CACHE_MODE`.

Change the location of the policy cache by creating an environment variable named `AM_POLICY_CACHE_DIR`.

For more information about properties related to the policy cache, refer to [Environment variables](configure-envvars.html).

---

---
title: Configure load balancers and reverse proxies
description: Configure PingAM Web Agent for environments with load balancers and reverse proxies, covering client identification, POST data preservation, FQDN mapping, and WebSocket support.
component: web-agents
version: 2026
page_id: web-agents:user-guide:load-balancers-proxies
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/load-balancers-proxies.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  client-identification: Identify clients behind load balancers and reverse proxies
  comms-am-agents: Agent - load balancer/reverse proxy - AM
  agents_ip_address_andor_fqdn: Agent's IP address and/or FQDN
  am_sessions_and_session_stickiness: AM sessions and session stickiness
  websockets: WebSockets
  am-forwarded-headers: Configure AM to use forwarded headers
  comms-clients-agents: Agent - load balancer/reverse proxy - client
  forward_clients_ip_address_andor_fqdns: Forward client's IP address and/or FQDNs
  use_sticky_load_balancing_with_post_data_preservation: Use sticky load balancing with POST data preservation
  lb-same-protocol-and-port: Map the agent host name to a load balancer or reverse proxy
  lb-different-protocol-and-port: Override the request protocol, host, and port
  bypass_load_balancers_to_directly_access_agents: Bypass load balancers to directly access agents
  lb-client-properties: Configure client identification properties
  lb-POST-data: Configure POST Data Preservation for load balancers or reverse proxies
  lb-POST-data-121: Map one agent profile to one agent instance when POST data preservation is enabled
  lb-POST-data-12all: Map one agent profile to multiple agent instances when POST data preservation is enabled
---

# Configure load balancers and reverse proxies

Most environments deploy a load balancer and reverse proxy between the agent and clients, and another between the agent and AM, as shown in the following diagram:

![Simplified diagram showing reverse proxies and load balancers configured in an environment with web agents.](_images/LB-proxy-AM-agent.svg)Figure 1. Environments with load balancers and reverse proxies

The reverse proxy and the load balancer can be the same entity. In complex environments, multiple load balancers and reverse proxies can be deployed in the network.

## Identify clients behind load balancers and reverse proxies

When a load balancer or reverse proxy is situated in the request path between the agent and a client, the agent does not have direct access to the IP address or hostname of the client. The agent cannot identify the client.

For load balancers and reverse proxies that support provision of the client IP and hostname in HTTP headers, configure the following properties:

* [Client IP Address Header](../properties-reference/com.sun.identity.agents.config.client.ip.header.html)

* [Client Hostname Header](../properties-reference/com.sun.identity.agents.config.client.hostname.header.html)

When there are multiple load balancers or reverse proxies in the request path, the header values can include a comma-separated list of values, where the first value represents the client, as in `client,next-proxy,first-proxy`.

## Agent - load balancer/reverse proxy - AM

When a reverse proxy is situated between the agent and AM, it can be used to protect the AM APIs.

When a load balancer is situated between the agent and AM, it can be used to regulate the load between different instances of AM.

Consider the points in this section when installing Web Agent in an environment where AM is behind a load balancer or a reverse proxy.

### Agent's IP address and/or FQDN

The load balancer or reverse proxy conceals the IP addresses and FQDNs of the agent and of AM. Consequently, AM cannot determine the agent base URL.

To prevent problems during installation or redirection, do the following:

* Configure the load balancer or reverse proxy to forward the agent IP address and/or FQDN in a header.

* Configure AM to recover the forwarded headers. Learn more in [Configure AM to use forwarded headers](#am-forwarded-headers).

* Install the agent using the IP address or FQDN of the load balancer or reverse proxy as the point of contact for the AM site.

### AM sessions and session stickiness

Improve the performance of policy evaluation by setting AM's sticky cookie (by default, `amlbcookie`) to the AM's server ID. For more information, refer to [Configuring site sticky load balancing](https://docs.pingidentity.com/pingam/8.1/setup/configure-lb.html#configure-lb-stateful) in AM's *Setup guide*.

When configuring multiple agents, consider the impact on sticky load balancer requirements of using one or multiple agent profiles:

* If agents are configured with multiple agent profiles, configure sticky load balancing. The agent profile name is contained in the OpenID Connect JWT, used by the agent and AM for communication. Without session stickiness, it is not possible to make sure the appropriate JWT ends in the appropriate agent instance.

  To have multiple agent profiles without sticky load balancing, disable validation of the `aud` claim in the session ID token. Either enable [Disable Audience Claim Validation](../properties-reference/com.forgerock.agents.jwt.aud.disable.html), or configure [Agent Profile ID Allow List](../properties-reference/com.forgerock.agents.jwt.aud.whitelist.html).

  For security reasons, agents should validate all claims in session ID tokens. Therefore, use this approach sparingly and mostly for migrations.

* If multiple agents are configured with the same agent profile, decide whether to configure sticky load balancing depending on other requirements of your environment.

### WebSockets

For communication between the agents and AM servers, the load balancers and reverse proxies must support the WebSocket protocol. Learn more in the load balancer or proxy documentation.

|   |                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For configuration examples, refer to [Apache as a reverse proxy](../installation-guide/apache.html#configure-apache-server) and [NGINX as a reverse proxy](../installation-guide/apache.html#nginx-reverse-proxy-server). |

### Configure AM to use forwarded headers

When a load balancer or reverse proxy is situated between the agent and AM, configure AM to recover the forwarded headers that expose the agents' real IP address or FQDN.

To configure how AM obtains the base URL of web agents, use the Base URL Source service:

1. Log in to the AM admin UI as an administrative user, such as `amAdmin`.

2. Select Realms > *Realm Name* > Services.

3. Select Add a Service > Base URL Source, and create a default service, leaving the fields empty.

4. Configure the service with the following properties, leaving the other fields empty:

   * Base URL Source: `X-Forwarded-* headers`

     This property allows AM to retrieve the base URL from the `Forwarded` header field in the HTTP request. The Forwarded HTTP header field is specified in [RFC 7239: Forwarded HTTP Extension](https://www.rfc-editor.org/rfc/rfc7239).

   * Context path: AM's deployment URI. For example, `/am`.

   Learn more in [Base URL source](https://docs.pingidentity.com/pingam/8.1/setup/services-configuration.html#global-baseurl) in AM's *Reference*.

5. Save your changes.

## Agent - load balancer/reverse proxy - client

When a reverse proxy is situated between the agent and client, it can be used to anonymize the client traffic that enters the network.

When a load balancer is situated between the agent and client, it can be used to regulate the load between the agents and the web application servers.

Consider the points in this section when installing Web Agent in an environment where clients are behind a load balancer or a reverse proxy.

### Forward client's IP address and/or FQDNs

The load balancer or reverse proxy conceals the IP addresses and FQDNs of the agent and clients. Consequently, the agent cannot determine the client base URL.

Configure the load balancer or reverse proxy to forward the client IP address and/or the client FQDN in a header. Failure to do so prevents the agent from performing policy evaluation, and applying not-enforced and conditional login/logout rules.

Learn more in [Configuring client identification properties](#lb-client-properties).

### Use sticky load balancing with POST data preservation

For POST data preservation, use sticky load balancing to ensure that after login the client hits the same agent as before and can therefore get their saved POST data.

Agents provide properties to set either sticky cookie or URL query string for load balancers and reverse proxies.

Learn more in [Configure POST Data Preservation for Load Balancers or Reverse Proxies](#lb-POST-data).

### Map the agent host name to a load balancer or reverse proxy

In the following diagram, the agent and load balancer/reverse proxy use the same protocol and port, but different FQDNs:

![Simplified diagram showing reverse proxies and load balancers using the same protocol and port than the web servers.](_images/LB-same.svg)Figure 2. Same protocol and port, different FQDN

Map the host name of the agent to that of the load balancer or reverse proxy.

1. Log in to the AM admin UI as an administrative user with rights to modify the web agent profile.

2. Go to Realms > *Realm Name* > Applications > Agents > Web > *Agent Name*.

3. Set the following options in the Global tab:

   * FQDN Check: Enable

     The equivalent property setting is [Enable FQDN Check](../properties-reference/com.sun.identity.agents.config.fqdn.check.enable.html) = `true`.

   * FQDN Default: Set to the FQDN of the load balancer or proxy, for example `lb.example.com`. Do not set it to the protected server FQDN where the agent is installed.

     The equivalent property setting is [FQDN Default](../properties-reference/com.sun.identity.agents.config.fqdn.default.html) = `lb.example.com`.

   * Agent Root URL for CDSSO: Set to the FQDN of the load balancer or proxy, for example `https://lb.example.com:80/`.

     The equivalent property setting is [Agent Root URL for CDSSO](../properties-reference/sunIdentityServerDeviceKeyValue.html) = `lb.example.com`.

   * FQDN Virtual Host Map: Map the load balancer or proxy FQDN to the FQDN where the agent is installed. For example,

     * Key: `agent.example.com` (protected server)

     * Value: `lb.example.com` (load balancer or proxy)

       The equivalent property setting is `com.sun.identity.agents.config.fqdn.mapping[agent.example.com]=lb.example.com`.

4. Save your work.

### Override the request protocol, host, and port

In the following diagram, a load balancer or reverse proxy forwards requests and responses between clients and protected web servers. The protocol, port, and FQDN configured on the load balancer and reverse proxy are different from those on the protected web server:

![Simplified diagram showing reverse proxies and load balancers using different protocol, port, and FQDN than the web servers.](_images/LB-different.svg)Figure 3. Different protocol, port, and FQDN

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Agent configuration for TLS offloading prevents FQDN checking and mapping. Consequently, URL rewriting and redirection don't work correctly when the agent is accessed directly instead of through the load balancer or proxy. This should not be a problem for client traffic, but could be a problem for web applications accessing the protected web server directly from behind the load balancer. |

Use [Agent Deployment URI Prefix](../properties-reference/com.sun.identity.agents.config.agenturi.prefix.html) to override the agent protocol, host, and port with that of the load balancer or reverse proxy.

|   |                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When the following headers are defined on the proxy or load-balancer, they override the value of [Agent Deployment URI Prefix](../properties-reference/com.sun.identity.agents.config.agenturi.prefix.html):- `X-Forwarded-Proto`

- `X-Forwarded-Host`

- `X-Forwarded-Port`If you are using these headers, do not configure the agent to override its hostname, port, or protocol. |

1. Log in to the AM admin UI as an administrative user with rights to modify the agent profile.

2. Go to Realms > *Realm Name* > Applications > Agents > Web > *Agent Name*.

3. Set the following options in the Global tab:

   * Agent Deployment URI Prefix: Set to the URI of the load balancer or proxy.

     This value is used to override the protocol, host, and port of the protected server.

     The equivalent property setting is [Agent Deployment URI Prefix](../properties-reference/com.sun.identity.agents.config.agenturi.prefix.html) = `external.example.com`.

   * Agent Root URL for CDSSO: Set to the URL of the load balancer or proxy.

     The equivalent property setting is [Agent Root URL for CDSSO](../properties-reference/sunIdentityServerDeviceKeyValue.html) = `https://external.example.com:443`.

4. Enable the following options in the Advanced tab:

   * Override Request URL Protocol

     The equivalent property setting is [Enable Override Request URL Protocol](../properties-reference/com.sun.identity.agents.config.override.protocol.html) = `true`.

   * Override Request URL Host

     The equivalent property setting is [Enable Override Request URL Host](../properties-reference/com.sun.identity.agents.config.override.host.html) = `true`.

   * Override Request URL Port

     The equivalent property setting is [Enable Override Request URL Port](../properties-reference/com.sun.identity.agents.config.override.port.html) = `true`.

5. Save your work.

### Bypass load balancers to directly access agents

In most load balanced deployments, `X-Forwarded-*` headers provide the protocol, port, and host of the load balancer to the agent. The agent returns a URL that points to the load balancer instead of to the agent.

To access the agent directly, bypassing the load balancer, disable port, host, and protocol overrides with the property [Disable Override Request URL Port, Host, or Protocol](../properties-reference/com.sun.identity.agents.config.override.disable.hostmap.html).

When you access the agent directly, authentication flows bypass the load balancer.

|   |                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Configuration with disabled overrides isn't recommended. If you disable overrides, make sure that when bypassing the load balancer you meet the security requirements of your application deployment. Other access controls might be required to ensure that only authorized users have direct access to the application. |

The agent disables overrides when all the following circumstances are true:

* The request host header matches the key.

* The load balancer uses the agent IP address instead of hostname.

* `X-Forwarded-`** headers aren't defined on the proxy or load balancer. When `X-Forwarded-`** headers are defined, they override. [Disable Override Request URL Port, Host, or Protocol](../properties-reference/com.sun.identity.agents.config.override.disable.hostmap.html).

In the following example, when the request host header matches `am.fr.*` the overrides for the protocol and host are disabled:

```none
com.sun.identity.agents.config.override.hostmap[am.fr.*]=proto|host
com.sun.identity.agents.config.override.protocol=true
com.sun.identity.agents.config.override.host=true
```

### Configure client identification properties

After configuring proxies or load balancers to forward the client FQDN and/or IP address, configure the agents to check the appropriate headers.

This procedure explains how to configure the client identification properties for a centralized web agent profile configured in the AM admin UI. The steps also mention the properties for web agent profiles that rely on local, file-based configurations:

1. Log in to the AM admin UI with a user that has permissions to modify the web agent profile.

2. Go to Realms > *Realm Name* > Applications > Agents > Web > *Agent Name*.

3. Set the following options in the Advanced tab:

   * Client IP Address Header: Configure the name of the header containing the IP address of the client. For example, `X-Forwarded-For`.

     The equivalent property setting is [Client IP Address Header](../properties-reference/com.sun.identity.agents.config.client.ip.header.html) = `X-Forwarded-For`.

     Configure this property if any of the following points are true:

     * AM policies are IP address-based.

     * The agent is configured for not-enforced IP rules.

     * The agent is configured take any decision based on the client's IP address.

   * Client Hostname Header: Configure the name of the header containing the FQDN of the client. For example, `X-Forwarded-Host`.

     The equivalent property setting is [Client Hostname Header](../properties-reference/com.sun.identity.agents.config.client.hostname.header.html) = `X-Forwarded-Host`.

     Configure this property if any of the following points are true:

     * AM policies are URL address-based.

     * The agent is configured for not-enforced URL rules.

     * The agent is configured take decisions based on the client's URL address.

4. Save your changes.

### Configure POST Data Preservation for load balancers or reverse proxies

Use one of the following procedures to configure post data preservation for load balancers or reverse proxies.

#### Map one agent profile to one agent instance when POST data preservation is enabled

In this procedure, a separate agent profile must created in AM for each agent instance. For scalable deployments, where resources are dynamically created and destroyed, use [Map one agent profile to multiple agent instances when POST data preservation is enabled](#lb-POST-data-12all) instead.

1. Configure your load balancer or reverse proxy to ensure session stickiness when the cookie or URL query parameter are present.

2. Log in to the AM admin UI as a user that has permissions to modify the agent profile.

3. Go to Realms > *Realm Name* > Applications > Agents > Web > *Agent Name*.

4. Set the following options in the Advanced tab:

   * [POST Data Sticky Load Balancing Mode](../properties-reference/com.sun.identity.agents.config.postdata.preserve.stickysession.mode.html):

     * COOKIE: The agent creates a cookie for POST data preservation session stickiness. The content of the cookie is configured in the next step.

     * URL: The agent appends to the URL a string specified in the next step.

       The equivalent property setting is `com.sun.identity.agents.config.postdata.preserve.stickysession.mode=COOKIE` or `com.sun.identity.agents.config.postdata.preserve.stickysession.mode=URL`.

   * [POST Data Sticky Load Balancing Value](../properties-reference/com.sun.identity.agents.config.postdata.preserve.stickysession.value.html): Configure a key-pair value separated by the `=` character.

     The agent creates the value when it evaluates [POST Data Sticky Load Balancing Mode](../properties-reference/com.sun.identity.agents.config.postdata.preserve.stickysession.mode.html). For example, specifying `lb=myserver` either sets a cookie called `lb` with `myserver` as a value, or appends `lb=myserver` to the URL query string.

     The equivalent property setting is `com.sun.identity.agents.config.postdata.preserve.stickysession.value=lb=myserver`.

5. Save your changes.

#### Map one agent profile to multiple agent instances when POST data preservation is enabled

Use this procedure for scalable deployments, where resources can be dynamically created or destroyed. For example, use it in deployments with load balancing, or environments running Kubernetes.

1. Configure your load balancer or reverse proxy to ensure session stickiness when the cookie or URL query parameter are present.

2. For each agent instance, configure post data preservation in the agent configuration file `agent.conf`. This configuration overrides the configuration in AM.

   In the following example, the settings in `agent.conf` configure two agents behind a load balancer to use the same agent profile, and provide uniqueness to the load balancer:

   * Agent 1:

     ```none
     com.sun.identity.agents.config.postdata.preserve.stickysession.mode = COOKIE
     com.sun.identity.agents.config.postdata.preserve.stickysession.value = EXAMPLE=Agent1
     ```

   * Agent 2:

     ```none
     com.sun.identity.agents.config.postdata.preserve.stickysession.mode = COOKIE
     com.sun.identity.agents.config.postdata.preserve.stickysession.value = EXAMPLE=Agent2
     ```

   For information about the values to use, refer to the following properties:

   * [POST Data Sticky Load Balancing Mode](../properties-reference/com.sun.identity.agents.config.postdata.preserve.stickysession.mode.html)

   * [POST Data Sticky Load Balancing Value](../properties-reference/com.sun.identity.agents.config.postdata.preserve.stickysession.value.html)

3. Restart the web server where the agent is installed.

---

---
title: Continuous security
description: Configure PingAM Web Agent to pass request context to PingAM in an environment map, enabling policy conditions based on client IP, DNS name, cookies, and headers.
component: web-agents
version: 2026
page_id: web-agents:user-guide:continuous-security
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/continuous-security.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  continuous-security-custom: Environment maps with customizable keys
---

# Continuous security

When a user requests a resource through AM, excluding proxies and load balancers, the Web Agent is usually the first point of contact. Because Web Agent is closer to the user than AM, and outside the firewalls that separate the user and AM, the Web Agent can sometimes gather information about the request, which AM cannot access.

When Web Agent requests a policy decision from AM, it can include the additional information in an *environment map*, a set of name/value pairs that describe the request IP and DNS name, along with other, optional, information. The additional information can then be included in the policy, for example, to allow only incoming requests that contain the `InternalNetwork`.

In AM, use server-side authorization scripts to access the environment map, and write scripted conditions based on cookies and headers in the request. For information about server-side authorization scripts, refer to [Scripting a policy condition](https://docs.pingidentity.com/pingam/8.1/am-authorization/scripted-policy-condition.html) in AM's *Authorization guide*.

## Environment maps with customizable keys

In Web Agent, use the continuous security properties [Continuous Security Cookie Map](../properties-reference/org.forgerock.openam.agents.config.continuous.security.cookies.html) and [Continuous Security Header Map](../properties-reference/org.forgerock.openam.agents.config.continuous.security.headers.html) to configure an environment map with the following parts:

* requestIp

  The IP address of the inbound request, determined as follows:

  * If [Client IP Address Header](../properties-reference/com.sun.identity.agents.config.client.ip.header.html) is configured, Web Agent extracts the IP address from the header.

  * Otherwise, Web Agent uses the web server connection information to determine the client IP address.

  This entry is always created in the map.

* requestDNSName

  The host name address of the inbound request, determined as follows:

  * If [Client Hostname Header](../properties-reference/com.sun.identity.agents.config.client.hostname.header.html) is configured, Web Agent extracts the host name from the header.

  * Otherwise, Web Agent uses the web server connection information to determine the client's host name.

  This entry is always created in the map.

* Other variable names

  An array of cookie or header values. An entry is created for each value specified in the continuous security properties.

  In the following example, the continuous security properties are configured to map values for the `ssid` cookie and `User-Agent` header to fields in an environment map:

  ```
  org.forgerock.openam.agents.config.continuous.security.cookies[ssid]=mySsid
  org.forgerock.openam.agents.config.continuous.security.headers[User-Agent]=myUser-Agent
  ```

  If the incoming request contains an `ssid` cookie and a `User-Agent` header, the environment map takes the value of the cookie and header, as shown in this example:

  ```
  requestIp=192.16.8.0.1
  requestDnsName=client.example.com
  mySsid=77xe99f4zqi1l99z
  myUser-Agent=Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko
  ```

---

---
title: Cookies
description: Configure PingAM Web Agent SSO token cookie name and cookie reset to clear cookies before redirecting clients to the login page.
component: web-agents
version: 2026
page_id: web-agents:user-guide:cookie-reset
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/cookie-reset.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sso-cookie-name: SSO token cookie name
  change_the_sso_token_cookie_name_for_an_agent: Change the SSO token cookie name for an agent
  change_the_sso_token_cookie_name_for_an_agent_group: Change the SSO token cookie name for an agent group
  cookie-reset: Cookie reset
---

# Cookies

## SSO token cookie name

By default, the agent's single sign-on (SSO) token [cookie name](../properties-reference/com.sun.identity.agents.config.cookie.name.html) is `iPlanetDirectoryPro`.

Unless you use [Accept SSO Token](../properties-reference/com.forgerock.agents.accept.sso.token.html) mode or have enabled [Custom Login Mode](../properties-reference/org.forgerock.openam.agents.config.allow.custom.login.html), you should remove the default cookie name value from the agent. A blank value ensures the agent gets the correct cookie name from AM for authentication.

You only need to set the agent's cookie name to a specific value if you use custom login mode or accept SSO token mode and want to use a cookie different from the one defined in the realm.

|   |                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you're using Advanced Identity Cloud, you don't need to change the agent cookie name because the agent automatically uses the Advanced Identity Cloud session cookie name for authentication. |

You can change the name of the cookie for a specific agent or for an agent group in AM.

### Change the SSO token cookie name for an agent

1. In the AM admin UI, go to Realms > *Realm Name* > Applications > Agents > Web > *Agent Name*.

2. On the SSO tab, remove the default value from the Cookie Name field or enter the SSO token cookie name, if applicable.

3. Click Save Changes.

### Change the SSO token cookie name for an agent group

1. In the AM admin UI, go to Realms > *Realm Name* > Applications > Agents > Web, and select the Groups tab followed by the *Group ID*.

2. On the SSO tab, remove the default value from the Cookie Name field or enter the SSO token cookie name, if applicable.

3. Click Save Changes.

## Cookie reset

Web Agent can reset cookies before redirecting the client to a login page, by issuing a Set-Cookie header to the client to reset the cookie values.

Cookie reset is typically used when multiple parallel authentication mechanisms are in play with the web agent and another authentication system. The agent can reset the cookies set by the other mechanism before redirecting the client to a login page.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To set and reset secure or HTTP Only cookies, in addition to the cookie reset properties, set the relevant cookie option, as follows:- To reset secure cookies, set [Enable Cookie Security](../properties-reference/com.sun.identity.agents.config.cookie.secure.html) to `true`.

- To reset HTTP only cookies, set [Enable HTTP Only Mode](../properties-reference/com.sun.identity.cookie.httponly.html) to `true`. |

If you have enabled attribute fetching by using cookies to retrieve user data, it is good practice to use cookie reset, which will reset the cookies when accessing an enforced URL without a valid session.

---

---
title: Cross-domain single sign-on
description: Configure PingAM Web Agent for cross-domain single sign-on (CDSSO) to let users access multiple services across different DNS domains from one login session.
component: web-agents
version: 2026
page_id: web-agents:user-guide:cdsso
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/cdsso.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Cross-domain single sign-on

Cross-domain single sign-on (CDSSO) is an AM capability that lets users access multiple independent services from a single login session, using the agent to transfer a validated session ID on a single DNS domain or across domains.

Without AM's CDSSO, SSO cannot be implemented across domains; the session cookie from one domain would not be accessible from another domain. For example, in a configuration where the AM server (`am.example.com`) is in a different DNS domain than the web agent (`myapp.website.com`), single sign-on would not be possible.

Web Agent works in CDSSO mode by default, regardless of the DNS domain of the AM servers and the DNS domain of the web agents.

Learn more in [Single sign-on](https://docs.pingidentity.com/pingam/8.1/am-authentication/about-sso.html) and [Implement CDSSO](https://docs.pingidentity.com/pingam/8.1/am-authentication/about-sso.html#implementing-cdsso) in AM's *Authentication and SSO guide*.

---

---
title: Environment variables
description: Reference for PingAM Web Agent runtime environment variables, including cache sizes, policy evaluation mode, log settings, and TLS key logging.
component: web-agents
version: 2026
page_id: web-agents:user-guide:configure-envvars
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/configure-envvars.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Environment variables

Configure environment variables to affect the user that is running the web server, virtual host, or location that the agent protects.

This section describes Web Agent properties that are configured by environment variables. After setting an environment variable, restart Web Agent.

You can find details about environment variables for installation in [Installation environment variables](../installation-guide/installer-env-vars.html).

You can find details about allowing environment variables to be used in NGINX in [env directive](http://nginx.org/en/docs/ngx_core_module.html#env) in the *NGINX Core functionality documentation*.

* `AM_IPC_BASE`

  (Unix only) The base number for IPC identifiers used by the agent. The shared memory semaphore ID range used by the agent starts at the specified value. Set this variable only if you detect that the agent semaphores are clashing with those of other processes in your environment.

  Default: Arbitrary value

* `AM_MAX_AGENTS`

  The maximum number of agent instances in the installation. The higher the number, the more shared memory the agent reserves.

  When the maximum is reached, if another agent instance starts, an error is logged and the agent won't protect any resources.

  Default: `32`

* `AM_MAX_SESSION_CACHE_SIZE`

  The maximum size in bytes of the shared memory for the session and policy cache:

  * Not set, or set to `0`: `16777216` (16 MB)

  * Maximum value: `1073741824` (1 GB)

  * Minimum value `1024` (1 MB)

  For multiple concurrent sessions, consider using a higher value.

* `AM_NET_TIMEOUT`

  The number of seconds for which the agent installer can contact AM during agent configuration validation.

  If the installer takes longer than this value to contact AM and validate the configuration, installation fails.

  Default: 4 seconds

- `Policy evaluation mode (AM_POLICY_CACHE_MODE)`

  Policy evaluation mode:

  * `off` or `0` (default): When a request requires a policy decision, the agent contacts AM for the decision.

  * `on`: The agent downloads all policies from AM at startup. When a request requires a policy decision, the agent uses the downloaded policies to make the policy decision.

  In both modes, the agent caches the policy decision. If a request requires the same policy decision again, the agent uses the cached decision.

  (Optional) Use the `AM_POLICY_CACHE_DIR` environment variable to specify a directory in which to store the policy cache.

- `AM_POLICY_CACHE_DIR`

  The directory in which to store the policy cache. The agent must be able to write to this directory.

  For example, `/path/to/web_agents/agent_type/log`.

- `AM_RESOURCE_PERMISSIONS`

  (Unix only) The permissions that the agent sets for its runtime resources.

  Allowed values:

  * `0600`

  * `0660`

  * `0666`

  The `AM_RESOURCE_PERMISSIONS` environment variable requires the `umask` value to allow these permissions for the files.

  Consider an example where the Apache agent is running with the `apache` user. The `umask` value is `0022` and the `AM_RESOURCE_PERMISSIONS` is `0666`. The agent runtime resources have the following permissions:

  **Resource Permissions Example in Linux**

  | Resource                                                                | Permission | Owner    |
  | ----------------------------------------------------------------------- | ---------- | -------- |
  | `/path/to/web_agents/agent_type/log/system_n.log`                       | 644        | `apache` |
  | `/path/to/web_agents/agent_type/log/monitor_n.log`                      | 644        | `apache` |
  | `/path/to/web_agents/agent_type/instances/agent_n/conf/agent.conf`      | 640        | `apache` |
  | `/path/to/web_agents/agent_type/instances/agent_n/logs/debug/debug.log` | 644        | `apache` |
  | `/dev/shm/am_cache_0`                                                   | 644        | `apache` |
  | `/dev/shm/am_log_data_0`                                                | 644        | `apache` |

  Any semaphores owned by the `apache` user have `644` permissions as well.

  Consider another example where `umask` is `0002` and `AM_RESOURCE_PERMISSIONS` is `0666`. The files are created with `664` permissions, which allows them to be read and written by the members of the group.

* `AM_SSL_KEYLOG_FILE`

  The name of the SSL key log file. For example, `/tmp/keylog.log`. Ensure the agent has write access to this file.

  The [Enable TLS key logging](../properties-reference/org.forgerock.agents.config.tls.keylog.enable.html) property or the [AM\_SSL\_KEYLOG\_ENABLE](../installation-guide/installer-env-vars.html#am-ssl-keylog-enable) installation environment variable must also be configured to enable TLS key logging.

  Learn more in [TLS key logging](../maintenance-guide/troubleshooting.html#tls-key-logging).

* `AM_SSL_OPTIONS`

  Overrides the default SSL/TLS protocols for the agent, set in the [Security Protocol List](../properties-reference/org.forgerock.agents.config.tls.html) bootstrap property.

  Specifies a space-separated list of security protocols preceded by a dash (`-`) that *won't* be used when connecting to AM.

  Supported protocols:

  * `TLSv1`

  * `TLSv1.1`

  * `TLSv1.2` (Enabled)

  * `TLSv1.3` (Enabled)

  For example, to configure `TLSv1.1`, set the environment variable to `AM_SSL_OPTIONS = -TLSv1 -TLSv1.2 -TLSv1.3`.

* `AM_SYSTEM_LOG_LEVEL`

  The log level for messages from the agent startup and background processes. Messages provide information about the agent initialisation, local files that the agent uses, or resources that the agent uses.

  By default, messages are written to the file given by [AM\_SYSTEM\_LOG\_PATH](#AM_SYSTEM_LOG_PATH), by default `/path/to/web_agents/agent_type/log/system_n.log`.

  The value `n` in the `system_n.log` file indicates the agent group number. Consider an environment with the following Apache HTTP Server installations:

  * `Apache_1` has two agent instances configured, `agent_1` and `agent_2`, configured to share runtime resources (AmAgentId is set to 0). Both agent instances write to the `system_0.log` file.

  * `Apache_2` has one agent instance configured, `agent_3`, with AmAgentId set to 1. The instance write to the `system_1.log` file.

  The `system_n.log` file can contain the following information:

  * Agent version information, written when the agent instance starts up.

  * Logs for the agent background processes.

  * WebSocket connection errors.

  * Cache stats and removal of old POST data preservation files.

  * Agent notifications.

  The following case-insensitive values are valid:

  * All

  * Message

  * Warning

  * Error (default)

  * Info

- `AM_SYSTEM_LOG_PATH`

  The full path and filename to the `system_n.log` file.

  Default: `/path/to/web_agents/agent_type/log/system_n.log`

* `AM_SYSTEM_LOG_FILES`

  The maximum number of rotated `system_n.log` files that the agent stores.

  Default: `0`

* `AM_SYSTEM_LOG_SIZE`

  The maximum size in bytes of the `system_n.log` file.

  Valid range: 0 (unlimited log file size) to 4294967295 bytes (4GB)

  Default: `0`

* `AM_SYSTEM_PIPE_DIR`

  (Unix only) The directory where agent instances store temporary pipe files.

  Default: `/path/to/web_agents/agent_type/log/`

---

---
title: Features
description: Overview of PingAM Web Agent features, including support for multiple sites, virtual hosts, and independent agent configuration instances.
component: web-agents
version: 2026
page_id: web-agents:user-guide:features
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/features.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  multi-site-and-vhost-support: Multiple sites and virtual hosts
---

# Features

## Multiple sites and virtual hosts

Web Agent instances can be configured to operate with multiple websites in IIS and ISAPI, and with multiple virtual hosts in Apache.

Each configuration instance is independent and has its own configuration file, debug logs, and audit logs. Each instance can connect to a different AM realm, or even different AM servers.

Learn more in [Installing Apache Web Agents on a Virtual Host](../installation-guide/apache.html#install-apache-web-agent-vhost) and [Install IIS and ISAPI Web Agent](../installation-guide/install-iis.html#install-iis-web-agent).

---

---
title: Fetch user attributes
description: Configure PingAM Web Agent to fetch user profile, session, and policy response attributes and inject them into HTTP headers or cookies for protected applications.
component: web-agents
version: 2026
page_id: web-agents:user-guide:fetch-user-attributes
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/fetch-user-attributes.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["passing-attributes.adoc"]
---

# Fetch user attributes

Web Agent can fetch user attributes and inject them into HTTP request headers and cookies, and pass them on to the protected client applications. The client applications can then personalize content using these attributes in their web pages or responses.

Use the following properties to configure fetching user attributes:

* [Profile Attribute Fetch Mode](../properties-reference/com.sun.identity.agents.config.profile.attribute.fetch.mode.html)

* [Profile Attribute Map](../properties-reference/com.sun.identity.agents.config.profile.attribute.mapping.html)

* [Response Attribute Fetch Mode](../properties-reference/com.sun.identity.agents.config.response.attribute.fetch.mode.html)

* [Response Attribute Map](../properties-reference/com.sun.identity.agents.config.response.attribute.mapping.html)

* [Session Attribute Fetch Mode](../properties-reference/com.sun.identity.agents.config.session.attribute.fetch.mode.html)

* [Session Attribute Map](../properties-reference/com.sun.identity.agents.config.session.attribute.mapping.html)

The `Mode` properties let you choose whether to map attributes to HTTP headers or HTTP cookies. The `Map` properties let you configure which attribute maps to which header or cookie.

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When injecting information into HTTP headers, don't use underscores (`_`) in the header name. Underscores are incompatible with some web servers and the header can be silently dropped. |

The agent securely fetches the user and session data from the authenticated user, as well as policy response attributes.

For example, you can have a web page that addresses the user by name retrieved from the user profile, for example "Welcome Your-Name!". AM populates part of the request (header, form data) with the CN from the user profile, and the website consumes and displays it.

---

---
title: FQDN checks
description: Configure PingAM Web Agent FQDN checking to validate and remap request domains before authentication or authorization, supporting load balanced and virtual host environments.
component: web-agents
version: 2026
page_id: web-agents:user-guide:fqdn-checking
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/fqdn-checking.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  examples: Examples
---

# FQDN checks

When FQDN checking is enabled, the agent checks the FQDN of a request before it evaluates the authentication or authorization of the request, as follows:

* If the request matches the default domain, or the value of a mapped domain, the agent passes the request on to the next step without changing the domain.

* Otherwise, the agent redirects the request to the specified domain before passing it on to the next step.

Use this feature to prevent the redirect of requests in the following scenarios:

* Where resource URLs differ from the FQDNs in AM policies, for example, in load balanced and virtual host environments.

* Where hostnames are virtual, allocated dynamically, or match a pattern, for example in a Kubernetes deployment.

* Where hostnames are partial.

FQDN checking requires [Enable FQDN Check](../properties-reference/com.sun.identity.agents.config.fqdn.check.enable.html) to be `true`, [FQDN Default](../properties-reference/com.sun.identity.agents.config.fqdn.default.html) to be set to a suitable value, and optionally, [FQDN Virtual Host Map](../properties-reference/com.sun.identity.agents.config.fqdn.mapping.html) to map incoming URLs to valid outgoing domains.

The agent maps FQDNs as follows:

1. If the request matches the domain in [FQDN Default](../properties-reference/com.sun.identity.agents.config.fqdn.default.html), the agent passes the request to the next step without changing the request domain.

2. Otherwise, if the request matches a mapped domain (map value) in [FQDN Virtual Host Map](../properties-reference/com.sun.identity.agents.config.fqdn.mapping.html), the agent passes the request to the next step without changing the request domain.

3. Otherwise, if the request matches a mapped host (map key) in [FQDN Virtual Host Map](../properties-reference/com.sun.identity.agents.config.fqdn.mapping.html), the agent redirects the request to the mapped domain before passing it to the next step.

4. Otherwise, the agent redirects the request to the domain in [FQDN Default](../properties-reference/com.sun.identity.agents.config.fqdn.default.html) before passing it to the next step.

## Examples

The following example configuration and requests illustrate how the agent checks and remaps FQDNs:

* Example configuration

- [Agent Root URL for CDSSO](../properties-reference/sunIdentityServerDeviceKeyValue.html):

  `sunIdentityServerDeviceKeyValue=agent.example.com`

- [Not-Enforced URL List](../properties-reference/com.sun.identity.agents.config.notenforced.url.html)

  `com.sun.identity.agents.config.notenforced.url[0]=http://www.agent1*.example.com`

- [Enable FQDN Check](../properties-reference/com.sun.identity.agents.config.fqdn.check.enable.html):

  `com.sun.identity.agents.config.fqdn.check.enable=true`

- [FQDN Default](../properties-reference/com.sun.identity.agents.config.fqdn.default.html):

  `com.sun.identity.agents.config.fqdn.default=agent.default.com`

- [FQDN Virtual Host Map](../properties-reference/com.sun.identity.agents.config.fqdn.mapping.html):

  `com.sun.identity.agents.config.fqdn.mapping[agent.example.com]=agent.example.com`

  `com.sun.identity.agents.config.fqdn.mapping[agent.example.com]=agent-*`

  `com.sun.identity.agents.config.fqdn.mapping[any.value.com]=ag*.example.com`

  `com.sun.identity.agents.config.fqdn.mapping[agent.othertest.com]=other.example.com`

* Example requests

- `http://agent.default.com/app`: The request URL matches the domain of the default mapping, so the agent does not redirect the request.

- `https://agent.example.com/app`: The request URL matches the value (domain) in the first mapping, so the agent does not redirect the request.

- `http://agent-4738294739287492/foo/bar/`: The request URL matches the value (domain) in the second mapping, using the wildcard, so the agent does not redirect the request. Note that the value of the key is irrelevant in this match.

- `https://agent123.example.com/app`: The request URL matches the value (domain) in the third mapping, so the agent does not redirect the request.

- `https://agent.othertest.me/app`: The request URL matches the key (host) in the fourth mapping, so the agent redirects the request to `https://other.example.com/app`.

- `https://agent.othertest2.me/app`: The request URL doesn't match any mapping, so the agent redirects the request to the default domain, `https://agent.example.com/app`.

---

---
title: Glossary
description: Glossary of key terms for PingAM Web Agent, including definitions for agent profiles, sessions, policy concepts, and SSO terminology.
component: web-agents
version: 2026
page_id: web-agents:user-guide:glossary
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/glossary.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Glossary

* Access control

  Control to grant or to deny access to a resource.

* Account lockout

  The act of making an account temporarily or permanently inactive after successive authentication failures.

* Actions

  Defined as part of policies, these verbs indicate what authorized identities can do to resources.

* Advice

  In the context of a policy decision denying access, a hint to the policy enforcement point about remedial action to take that could result in a decision allowing access.

* Agent administrator

  User having privileges only to read and write agent profile configuration information, typically created to delegate agent profile creation to the user installing a web or Java agent.

- Agent group

  A group of agent instances that share runtime resources and shared memory.

* Agent profile

  A set of configuration properties that define the behavior of the agent.

- Agent profile realm

  The AM realm in which the agent profile is stored.

- Application

  A service exposing protected resources.

  In the context of AM policies, the application is a template that constrains the policies that govern access to protected resources. An application can have zero or more policies.

- Application type

  Application types act as templates for creating policy applications.

  Application types define a preset list of actions and functional logic, such as policy lookup and resource comparator logic.

  Application types also define the internal normalization, indexing logic, and comparator logic for applications.

- Attribute-based access control (ABAC)

  Access control that is based on attributes of a user, such as how old a user is or whether the user is a paying customer.

- Authentication

  The act of confirming the identity of a principal.

- Authentication level

  Positive integer associated with an authentication service, usually used to require success with more stringent authentication measures when requesting resources requiring special protection. Learn more in AM's [Authentication levels for trees](https://docs.pingidentity.com/pingam/8.1/am-authentication/auth-nodes-and-journeys.html#authentication-levels-trees).

- Authentication Session

  The interval while the user or entity is authenticating to AM.

* Session

  The interval that starts after the user has authenticated and ends when the user logs out, or when their session is terminated. For browser-based clients, AM manages user sessions across one or more applications by setting a session cookie.

* Authorization

  The act of determining whether to grant or to deny a principal access to a resource.

* Authorization Server

  In OAuth 2.0, issues access tokens to the client after authenticating a resource owner and confirming that the owner authorizes the client to access the protected resource. AM can play this role in the OAuth 2.0 authorization framework.

* Auto-federation

  Arrangement to federate a principal's identity automatically based on a common attribute value shared across the principal's profiles at different providers.

* Bulk federation

  Batch job permanently federating user profiles between a service provider and an identity provider, based on a list of matched user identifiers that exist on both providers.

- Centralized configuration mode

  AM stores the agent properties in the AM configuration store. Learn more in [local configuration mode](#def-local-configuration-mode).

  The configuration mode is defined by [Location of Agent Configuration Repository](../properties-reference/com.sun.identity.agents.config.repository.location.html).

- Circle of trust

  Group of providers, including at least one identity provider, who have agreed to trust each other to participate in a SAML v2.0 provider federation.

- Client

  In OAuth 2.0, requests protected web resources on behalf of the resource owner given the owner's authorization. AM can play this role in the OAuth 2.0 authorization framework.

* Client-based OAuth 2.0 tokens

  After a successful OAuth 2.0 grant flow, AM returns a token to the client. This differs from [CTS-based OAuth 2.0 tokens](#def-CTS-based-token), where AM returns a *reference* to token to the client.

- Client-based sessions

  AM [sessions](#def-session) for which AM returns session state to the client after each request, and require it to be passed in with the subsequent request. For browser-based clients, AM sets a cookie in the browser that contains the session information.

  For browser-based clients, AM sets a cookie in the browser that contains the session state. When the browser transmits the cookie back to AM, AM decodes the session state from the cookie.

- Conditions

  Defined as part of policies, these determine the circumstances under which a policy applies.

  Environmental conditions reflect circumstances like the client IP address, time of day, how the subject authenticated, or the authentication level achieved.

  Subject conditions reflect characteristics of the subject like whether the subject authenticated, the identity of the subject, or claims in the subject's JWT.

- Configuration datastore

  LDAP directory service holding AM configuration data.

- Cross-domain single sign-on (CDSSO)

  AM capability allowing single sign-on across different DNS domains.

* CTS-based OAuth 2.0 tokens

  After a successful OAuth 2.0 grant flow, AM returns a *reference* to the token to the client, rather than the token itself. This differs from client-based OAuth 2.0 tokens, where AM returns the entire token to the client.

- CTS-based sessions

  AM sessions that reside in the Core Token Service's token store. CTS-based sessions might also be cached in memory on one or more AM servers. AM tracks these sessions in order to handle events like logout and timeout, to permit session constraints, and to notify applications involved in SSO when a session ends.

- Delegation

  Granting users administrative privileges with AM.

- Entitlement

  Decision that defines which resource names can and cannot be accessed for a given identity in the context of a particular application, which actions are allowed and which are denied, and any related advice and attributes.

- Extensible Access Control Markup Language (XACML)

  Standard, XML-based access control policy language, including a processing model for making authorization decisions based on policies.

- Federation

  Standardized means for aggregating identities, sharing authentication and authorization data information between trusted providers, and allowing principals to access services across different providers without authenticating repeatedly.

- Fedlet

  Service provider application capable of participating in a circle of trust and allowing federation without installing all of AM on the service provider side; AM lets you create Java Fedlets.

- Hot swappable

  Configuration properties for which changes take effect without restarting the container where AM runs.

- Identity

  Set of data that uniquely describes a person or a thing such as a device or an application.

- Identity federation

  Linking of a principal's identity across multiple providers.

- Identity provider (IdP)

  Entity that produces assertions about a principal (such as how and when a principal authenticated, or that the principal's profile has a specified attribute value).

- Identity repository

  Data store holding user profiles and group information; different identity repositories can be defined for different realms.

- Identity store

  Data storage service holding principals' profiles; underlying storage can be an LDAP directory service or a custom `IdRepo` implementation.

- Java agent

  Java web application installed in a java container that acts as a policy enforcement point, filtering requests to other applications in the container, with policies based on application resource URLs.

* Local configuration mode

  The Web Agent installer creates the file `/web_agents/agent_type/instances/agent_nnn/config/agent.conf` to store the agent configuration properties. Learn more in [centralized configuration mode](#def-central-configuration-mode).

  The configuration mode is defined by [Location of Agent Configuration Repository](../properties-reference/com.sun.identity.agents.config.repository.location.html).

* Metadata

  Federation configuration information for a provider.

* Policy

  Set of rules that define who is granted access to a protected resource when, how, and under what conditions.

* Policy agent

  Java, web, or custom agent that intercepts requests for resources, directs principals to AM for authentication, and enforces policy decisions from AM.

* Policy Administration Point (PAP)

  Entity that manages and stores policy definitions.

* Policy Decision Point

  Entity that evaluates access rights, and then issues authorization decisions.

* Policy Enforcement Point (PEP)

  Entity that intercepts a request for a resource, and then enforces policy decisions from a policy decision point.

- Policy evaluation realm

  The AM realm that the agent uses to request policy decisions from AM.

- Policy Information Point (PIP)

  Entity that provides extra information, such as user profile attributes, that a policy decision point needs in order to make a decision.

* Principal

  Represents an entity that has been authenticated (such as a user, a device, or an application), and thus is distinguished from other entities.

  When an AM identity successfully authenticates, AM associates the identity with the Principal.

* Privilege

  In the context of delegated administration, a set of administrative tasks that can be performed by specified identities in a given realm.

* Provider federation

  Agreement among providers to participate in a circle of trust.

* Realm

  AM unit for organizing configuration and identity information.

  Realms can be used, for example, when different parts of an organization have different applications and identity stores, and when different organizations use the same AM deployment.

  Administrators can delegate realm administration. The administrator assigns administrative privileges to users, allowing them to perform administrative tasks within the realm.

* Resource

  Something a user can access over the network such as a web page.

  Defined as part of policies, these can include wildcards in order to match multiple actual resources.

* Resource owner

  In OAuth 2.0, entity who can authorize access to protected web resources, such as an end user.

* Resource server

  In OAuth 2.0, server hosting protected web resources, capable of handling access tokens to respond to requests for such resources.

* Response attributes

  Defined as part of policies, these allow AM to return additional information in the form of "attributes" with the response to a policy decision.

* Role based access control (RBAC)

  Access control that is based on whether a user has been granted a set of permissions (a role).

* Security Assertion Markup Language (SAML)

  Standard, XML-based language for exchanging authentication and authorization data between identity providers and service providers.

* Service provider (SP)

  Entity that consumes assertions about a principal (and provides a service that the principal is trying to access).

* Session high availability

  Capability that lets any AM server in a clustered deployment access shared, persistent information about users' sessions from the CTS token store. The user does not need to log in again unless the entire deployment goes down.

* Session token

  Unique identifier issued by AM after successful authentication. For CTS-based sessions, the session token is used to track a principal's session.

* Single log out (SLO)

  Capability allowing a principal to end a session once, thereby ending her session across multiple applications.

* Single sign-on (SSO)

  Capability allowing a principal to authenticate once and gain access to multiple applications without authenticating again.

* Site

  Group of AM servers configured the same way, accessed through a load balancer layer. The load balancer handles failover to provide service-level availability.

  The load balancer can also be used to protect AM services.

* Standard metadata

  Standard federation configuration information that you can share with other access management software.

- Stateless Service

  Stateless services do not store any data locally to the service. When the service requires data to perform any action, it requests it from a data store. For example, a stateless authentication service stores session state for logged-in users in a database. This way, any server in the deployment can recover the session from the database and service requests for any user.

  All AM services are stateless unless otherwise specified.

* Subject

  Entity that requests access to a resource

  When an identity successfully authenticates, AM associates the identity with the Principal that distinguishes it from other identities. An identity can be associated with multiple principals.

- User realm

  The AM realm in which a user is authenticated.

- Web Agent

  Native library installed in a web server that acts as a policy enforcement point with policies based on web page URLs.

---

---
title: Login redirect
description: "Configure PingAM Web Agent login redirect: default, custom same-domain, cross-domain, and conditional redirect modes to authenticate unauthenticated users."
component: web-agents
version: 2026
page_id: web-agents:user-guide:login-redirect
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/login-redirect.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  web-agent-default-redirect: Default login redirect
  custom-redirect: Custom login redirect
  web-agent-custom-redirect: Same domain custom login redirect
  same_domain_custom_login_redirect_with_final_redirect_to_the_protected_resource: Same domain custom login redirect with final redirect to the protected resource
  custom-redirect-cross-domain: Cross-domain custom login redirect
  cross_domain_custom_login_redirect_on_a_shared_network: Cross-domain custom login redirect on a shared network
  cross_domain_custom_login_redirect_with_am_behind_a_proxy: Cross-domain custom login redirect with AM behind a proxy
  web-agent-conditional-redirect: Conditional login redirect
  conditionally_redirect_login_by_domain_name: Conditionally redirect login by domain name
  conditionally_redirect_login_by_matching_regular_expressions: Conditionally redirect login by matching regular expressions
  login-redirect-am-custom-url: Redirect login to a custom URL configured in AM
---

# Login redirect

When an unauthenticated user requests access to a protected resource, the agent redirects the user to log in. The choice of the login endpoint, and the parameters it receives, is defined by the login redirect mode and whether the agent accepts SSO tokens and ID tokens as session cookies.

Configure login redirect options as follows:

|                                                                                                         |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------- | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                         |   | [Accept SSO Token](../properties-reference/com.forgerock.agents.accept.sso.token.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                         |   | 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Custom Login Mode](../properties-reference/org.forgerock.openam.agents.config.allow.custom.login.html) | 0 | [Default login redirect](#web-agent-default-redirect):- Don't configure [AM Login URL](../properties-reference/com.sun.identity.agents.config.login.url.html).

- (Optional) Configure [AM Conditional Login URL](../properties-reference/com.forgerock.agents.conditional.login.url.html) to point to the AM admin UI or the AM `oauth2/authorize` endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                         |   | * Doesn't accept SSO tokens as session cookies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | - Accepts SSO tokens and ID tokens as session tokens during and after the login flow.

- Doesn't convert SSO tokens to ID tokens.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                         | 1 | [Same domain custom login redirect](#web-agent-custom-redirect) or [Cross domain custom login redirect](#custom-redirect-cross-domain):- Redirects login to the originally requested resource.

- Converts SSO tokens to ID tokens.

- Configure [AM Login URL](../properties-reference/com.sun.identity.agents.config.login.url.html) to point to a custom login page.

- (Optional) Configure [AM Conditional Login URL](../properties-reference/com.forgerock.agents.conditional.login.url.html) to point to the same URL as [AM Login URL](../properties-reference/com.sun.identity.agents.config.login.url.html) with additional parameters such as the login realm. Requests are logged conditionally to this URL.

- Don't configure [AM Conditional Login URL](../properties-reference/com.forgerock.agents.conditional.login.url.html) or [AM Login URL](../properties-reference/com.sun.identity.agents.config.login.url.html) to point to the AM admin UI or the AM `oauth2/authorize` endpoint. | * Not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                         | 2 | - Not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Same domain custom login redirect](#web-agent-custom-redirect):- This non-standard flow has limitations. Use only for environments migrating from earlier versions of the agent.

- Redirects login with a `goto` query parameter to the originally requested resource

- Accepts SSO tokens

- Configure [AM Login URL](../properties-reference/com.sun.identity.agents.config.login.url.html) to point to a custom login page

- (Optional) Configure [AM Conditional Login URL](../properties-reference/com.forgerock.agents.conditional.login.url.html) to point to the same URL as [AM Login URL](../properties-reference/com.sun.identity.agents.config.login.url.html) with additional parameters such as the login realm. Requests are logged conditionally to this URL.

- Don't configure [AM Conditional Login URL](../properties-reference/com.forgerock.agents.conditional.login.url.html) or [AM Login URL](../properties-reference/com.sun.identity.agents.config.login.url.html) to point to the AM admin UI or the AM `oauth2/authorize` endpoint. |

## Default login redirect

In default login redirect, the agent redirects users for authentication to a page on the AM admin UI. The agent uses OpenID Connect ID JTWs as session tokens. Default login always redirects users to the top-level realm, irrespective of the [user realm](glossary.html#def-user-realm).

The following image shows the flow of data during a default login redirect. When an unauthenticated user requests access to a protected resource. The agent wraps the SSO session token inside an OpenID Connect JWT. Authentication requires access to the `/oauth2/authorize` endpoint, which invokes the AM admin UI and other endpoints such as `oauth2/authorize`, `json/authenticate`, `json/sessions`, `json/serverinfo`, and `XUI/*`.

![Simplified sequence diagram showing the default login redirection flow.](_images/login-redirection-default.svg)

## Custom login redirect

In custom login redirect, the agent can redirect login in the following ways:

* Redirect login to custom login pages, in the same or a different realm

* Conditionally redirect login to different AM instances, AM sites, or authentication realms, based on the request URL.

* Use AM-specific SSO tokens as session tokens

### Same domain custom login redirect

The agent redirects unauthenticated users to a custom login page in the same domain, adding the `original_request_url` parameter to the redirect. The parameter records the requested URL, which can then be used by custom login application or page.

The custom login page posts an SSO token to `agent/custom-login-response`, with the realm as an optional parameter, and sets an SSO token in the same domain as the agent.

The agent attempts to validate the SSO token against the AM endpoints.

At the end of the login flow, the agent can do the final redirect to the protected resource, or to the originally requested resource, with a `goto` query parameter

#### Same domain custom login redirect with final redirect to the protected resource

Set the following properties:

* [Custom Login Mode](../properties-reference/org.forgerock.openam.agents.config.allow.custom.login.html) as `1`, to use the OIDC-compliant custom login redirection mode

* [AM Login URL](../properties-reference/com.sun.identity.agents.config.login.url.html), to the URL of the custom login page

If the custom login page is a part of the agent's protected application, add the custom login pages to the not-enforced lists.

The following image shows the data flow for a custom login redirect when the custom login pages are in the same domain as the agent, and the agent redirects the request to the originally requested resource.

![Custom login redirection flow where the agent and the custom login pages are on the same domain. The agent redirects to the originally requested resource after authentication.](_images/login-redirection-custom1-accepttoken0.svg)

### Cross-domain custom login redirect

The agent redirects unauthenticated users to a custom login page in a different domain, including the `original-request-uri` parameter in the redirect. The parameter records the requested URL, which can then be used by custom login application or page.

The custom login page provides a `custom-login-response`, and sets an SSO token, which can be accessed only in that domain. Because the agent can't access the cookie, it redirects to AM for the [Default login redirection mode](#web-agent-default-redirect).

Depending on your environment, the agent can contact AM to validate the cookie even if it can't detect it. In other cases, you need to configure an additional property.

If AM can validate the SSO token, it returns an ID token as part of the default redirection login flow.

Consider the following:

* Ensure the login pages **don't** set the SSO token cookie with the `SameSite=Strict` attribute.

* If AM can't validate the SSO token (for example, because it can't recognize the domain set for the cookie), it redirects the end user to authenticate again using the [Default login redirection mode](#web-agent-default-redirect).

* AM must be visible to the custom login pages, either because they both are in the same network/domain, or because you exposed the relevant AM endpoints using a proxy:

#### Cross-domain custom login redirect on a shared network

On a shared network, the server where AM is running has two interfaces: one connected to the internal network, where the agent is, and another connected to the external network, where the custom login pages are.

Use the following properties to configure this scenario:

* [Custom Login Mode](../properties-reference/org.forgerock.openam.agents.config.allow.custom.login.html)

* [AM Login URL](../properties-reference/com.sun.identity.agents.config.login.url.html)

The following image illustrates the environment. The web server housing the protected resources can be connected to the external network in different ways; with two interfaces, or through a proxy. It isn't important for custom login, so it isn't shown.

![The agent and the custom login pages are on different domains. There is no proxy between AM and the custom login pages](_images/custom-login-different-domains-noproxy.svg)

The following image shows the data flow:

![Sequence diagram of the custom login mode when the agent and the custom login pages are on a different domain. There is no proxy between AM and the custom login pages](_images/login-redirection-custom1-different-domain.svg)

#### Cross-domain custom login redirect with AM behind a proxy

The server where AM is running has one interface to the internal network, where the agent is. A proxy hides AM from the external network, which forwards traffic to the `/oauth2/authorize` endpoint.

Use the following properties to configure this scenario:

* [Custom Login Mode](../properties-reference/org.forgerock.openam.agents.config.allow.custom.login.html)

* [AM Login URL](../properties-reference/com.sun.identity.agents.config.login.url.html)

* [Public AM URL](../properties-reference/com.forgerock.agents.public.am.url.html)

The following image illustrates the environment. The web server where the protected resources are can be connected to the external network in different ways; with two interfaces, or through a proxy. It isn't important for custom login, so it isn't shown in the following diagram:

![The agent and the custom login pages are on different domains. There is a proxy between AM and the custom login pages.](_images/custom-login-different-domains-proxy.svg)

The following image shows the data flow:

![Sequence diagram of the custom login mode when the agent and the custom login pages are on a different domain. There is a proxy between AM and the custom login pages.](_images/login-redirection-custom1-different-domain-publicAM.svg)

## Conditional login redirect

Use conditional redirects to redirect the end user to different AM instances or sites, or to different custom pages, depending on the incoming request URL.

To redirect login to a specific authentication tree, add the `service` parameter, for example: `https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/authorize?service=myTree` would authenticate users using an authentication tree called `myTree`.

### Conditionally redirect login by domain name

When the incoming request URL matches a specified domain name, configure the following properties to redirect to a specified URL:

* [Custom Login Mode](../properties-reference/org.forgerock.openam.agents.config.allow.custom.login.html) = 0

* [AM Conditional Login URL](../properties-reference/com.forgerock.agents.conditional.login.url.html)

* [CDSSO Redirect URI](../properties-reference/com.sun.identity.agents.config.cdsso.redirect.uri.html)

The following image shows the data flow when requests to the domain `customers.example.com` are redirected to the `alpha` realm. Other requests are redirected to the top-level realm.

![Simplified flow for login redirect when conditional redirection is configured](_images/login-redirection-default-conditional.svg)

### Conditionally redirect login by matching regular expressions

When the incoming request URL matches a regular expression, configure the following properties to redirect to a specified URL:

* [Custom Login Mode](../properties-reference/org.forgerock.openam.agents.config.allow.custom.login.html) = 0

* [Regular Expression Conditional Login Pattern](../properties-reference/org.forgerock.agents.config.conditional.login.pattern.html)

* [Regular Expression Conditional Login URL](../properties-reference/org.forgerock.agents.config.conditional.login.url.html)

In the following example, when the request matches the regular expression `.*shop`, the agent redirects it to the `alpha` realm for authentication:

```none
org.forgerock.openam.agents.config.allow.custom.login = 0
org.forgerock.agents.config.conditional.login.pattern[0] = .*shop
org.forgerock.agents.config.conditional.login.url[0] = https://am.example.com/am/oauth2/realms/root/realms/alpha/authorize
```

## Redirect login to a custom URL configured in AM

AM's OAuth2 Provider service can be configured to use a custom URL to handle login, to override the default AM login page. When a custom login page is configured in AM, configure the agent to ensure that it redirects the login to that page.

1. In the AM admin UI, go to Services > OAuth2 Provider > Advanced > Custom Login URL Template, and note the custom URL.

2. Go to Applications > Agents > Web, and select your Web Agent.

3. On the AM Services tab set the following properties:

   * [Custom Login Mode](../properties-reference/org.forgerock.openam.agents.config.allow.custom.login.html): Set to `1`.

   * [AM Conditional Login URL](../properties-reference/com.forgerock.agents.conditional.login.url.html): Set to the custom URL in step 1.

---

---
title: Logout
description: "Configure PingAM Web Agent logout: trigger logout on URL patterns, redirect users after logout, invalidate PingAM sessions, and reset cookies on logout."
component: web-agents
version: 2026
page_id: web-agents:user-guide:logout
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/logout.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  trigger_logout_with_a_url: Trigger logout with a URL
  redirect_logout_to_a_landing_page: Redirect logout to a landing page
  end_am_sessions_on_logout: End AM sessions on logout
  reset_cookies_on_logout: Reset cookies on logout
  example_logout_flow_with_am_as_the_logout_page: Example logout flow with AM as the logout page
  example_logout_flow_with_the_application_serving_the_logout_page: Example logout flow with the application serving the logout page
---

# Logout

This section describes how to trigger a logout based on the properties of a request, and how to redirect users after logout to a specified logout resource.

The agent maintains the [user realm](glossary.html#def-user-realm) for each session, obtaining it from the JWT or `sessioninfo` endpoint. When a user logs out, the agent automatically passes the stored realm to the logout endpoint.

Web Agent provides the following properties to configure logout:

| Task                  | Property                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Trigger logout        | * [Enable Regex for Logout URL List](../properties-reference/org.forgerock.agents.config.logout.regex.enable.html)             | A flag to evaluate expressions in [Logout URL List](../properties-reference/com.sun.identity.agents.config.agent.logout.url.html) as regular expressions instead of as wildcard expressions.                                                                                                                                                                                                                                                            |
|                       | - [Logout URL List](../properties-reference/com.sun.identity.agents.config.agent.logout.url.html)                              | An expression that resolves to one or more application logout URLs.When the end user accesses a logout URL, the agent triggers a logout flow. The web server must be able to handle the logout URLs.Expressions can be wildcard expressions, Perl-compatible regular expressions, or ECMAScript-compatible (IIS) regular expressions.                                                                                                                   |
|                       | * [Agent Logout URL Regular Expression (deprecated)](../properties-reference/com.forgerock.agents.agent.logout.url.regex.html) | A Perl-compatible or ECMAScript-compatible (IIS) regular expression that resolves to one or more application logout URLs.This property is deprecated; use [Logout URL List](../properties-reference/com.sun.identity.agents.config.agent.logout.url.html) instead.If this property is used, it is evaluated before [Enable Regex for Logout URL List](../properties-reference/org.forgerock.agents.config.logout.regex.enable.html) in the logout flow. |
| Manage logout         | - [AM Logout URL](../properties-reference/com.sun.identity.agents.config.logout.url.html)                                      | A URL to manage the logout.                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                       | * [Enable Invalidate Logout Session](../properties-reference/org.forgerock.agents.config.logout.session.invalidate.html)       | A flag to kill the AM session when the value of [Logout URL List](../properties-reference/com.sun.identity.agents.config.agent.logout.url.html) is a page in your application and your application doesn't handle the session invalidation process.                                                                                                                                                                                                     |
|                       | - [Reset Cookies on Logout List](../properties-reference/com.sun.identity.agents.config.logout.cookie.reset.html)              | A list of cookies to reset on logout.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Redirect after logout | * [Logout Redirect URL](../properties-reference/com.sun.identity.agents.config.logout.redirect.url.html)                       | A URL to which the user is redirected after logout.                                                                                                                                                                                                                                                                                                                                                                                                     |
|                       | - [Disable Logout Redirection](../properties-reference/com.forgerock.agents.config.logout.redirect.disable.html)               | A flag to disallow redirect after logout. When `true`, the agent performs session logout in the background and continues processing access to the current URL.                                                                                                                                                                                                                                                                                          |

## Trigger logout with a URL

The agent triggers logout according to the configuration of the following properties:

* [Logout URL List](../properties-reference/com.sun.identity.agents.config.agent.logout.url.html)

* [Agent Logout URL Regular Expression (deprecated)](../properties-reference/com.forgerock.agents.agent.logout.url.regex.html)

* [Enable Regex for Logout URL List](../properties-reference/org.forgerock.agents.config.logout.regex.enable.html)

The following image shows how the properties are applied:

![Properties to trigger logout](_images/logout.svg)Examples

* The following example triggers logout when the request URL is from `*/bank/log-me-out`:

  ```none
  org.forgerock.agents.config.logout.regex.enable=false
  com.forgerock.agents.agent.logout.url=*//*:*/bank/log-me-out
  ```

* The following example triggers logout when the request URL is anywhere in the path `*/logout/*`:

  ```none
  org.forgerock.agents.config.logout.regex.enable=false
  com.forgerock.agents.agent.logout.url=*//*:*/*/logout/*
  ```

* The following example triggers logout when:

  * The request URL is on the path `*/protectedA/*` or `*/protectedB/*`,

  * The request URL contains a second query section that includes `op=logout` anywhere in the parameter list

  ```bash
  org.forgerock.agents.config.logout.regex.enable=true
  com.forgerock.agents.agent.logout.url=https:\/\/example.domain.com:443\/(protectedA|protectedB)\?(.*\&)*op=logout(\&.*)*$
  ```

## Redirect logout to a landing page

The agent redirects users to a specified resource after logout when the following properties are configured:

* [Disable Logout Redirection](../properties-reference/com.forgerock.agents.config.logout.redirect.disable.html)

  * Set to `false` to allow redirect on logout. The agent appends a goto parameter to the logout URL with the value of the [Logout Redirect URL](../properties-reference/com.sun.identity.agents.config.logout.redirect.url.html).

  * Set to `true` to disable redirect in logout. The agent doesn't perform the last redirection and leaves the web client on the logout page.

    Consider setting [Enable Invalidate Logout Session](../properties-reference/org.forgerock.agents.config.logout.session.invalidate.html) to `true` when this property is `true`.

* [Logout Redirect URL](../properties-reference/com.sun.identity.agents.config.logout.redirect.url.html)

  Specify an HTML page to which the agent redirects the end user on logout. The page must be available in your web server.

Depending on the redirect URL, perform this additional configuration:

* Add the URL to the [Not-Enforced URL List](../properties-reference/com.sun.identity.agents.config.notenforced.url.html).

* If the URL doesn't perform a REST logout to AM, set [Enable Invalidate Logout Session](../properties-reference/org.forgerock.agents.config.logout.session.invalidate.html) to `true`.

* If the URL isn't relative to AM, or in the same scheme, FQDN, and port, add it to the AM validation service.

  Learn more in Advanced Identity Cloud's [Configure trusted URLs](https://docs.pingidentity.com/pingoneaic/am-authentication/redirection-url-precedence.html#configure_trusted_urls) or AM's [Configure trusted URLs](https://docs.pingidentity.com/pingam/8.1/am-authentication/redirection-url-precedence.html#configure_trusted_urls).

## End AM sessions on logout

Configure one of the following properties to manage logout:

* [AM Logout URL](../properties-reference/com.sun.identity.agents.config.logout.url.html) to redirect the request to AM's `/am/UI/Logout` endpoint. This is the default value.

* [Enable Invalidate Logout Session](../properties-reference/org.forgerock.agents.config.logout.session.invalidate.html)

  * Set to `true` when [Logout URL List](../properties-reference/com.sun.identity.agents.config.agent.logout.url.html) is configured with a page in your application, but your application *doesn't handle* the session invalidation process.

    The agent doesn't add the `goto` parameter to the URL, and the web client remains in the logout page.

    The agent deletes its own JWT cookie and invalidates the AM session.

  * Set to `false` when [Logout URL List](../properties-reference/com.sun.identity.agents.config.agent.logout.url.html) has any of the following values:

    * A SAML v2.0 logout page.

    * An AM logout page.

    * A page in your application, and your application *does handle* the session invalidation process.

    The agent deletes its own JWT cookie but doesn't invalidate the AM session.

## Reset cookies on logout

To reset specified cookies during logout, configure [Reset Cookies on Logout List](../properties-reference/com.sun.identity.agents.config.logout.cookie.reset.html).

## Example logout flow with AM as the logout page

![Simplified diagram showing the logout flow when AM is set as the logout pages](_images/logout-flow-am.svg)

## Example logout flow with the application serving the logout page

![Simplified diagram showing the logout flow when the application serves the logout pages](_images/logout-flow-custom.svg)

---

---
title: Not-enforced rules
description: Configure PingAM Web Agent not-enforced rules to allow unauthenticated access to public resources, bypassing authentication and policy evaluation for matched requests.
component: web-agents
version: 2026
page_id: web-agents:user-guide:not-enforced-rules
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/not-enforced-rules.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  conventions_for_not_enforced_rules: Conventions for not-enforced rules
  invert_not_enforced_url_rules: Invert not-enforced URL rules
  wildcards: Wildcards
  multi_level_wildcard: Multi-level wildcard (*)
  one_level_wildcard: One-level wildcard (-*-)
  multiple_wildcards: Multiple wildcards
  regular_expressions: Regular expressions
  http_methods: HTTP Methods
  compound_rules: Compound rules
  encoding_non_ascii_characters_in_rules: Encoding non-ASCII characters in rules
---

# Not-enforced rules

Some resources, such as the "public" directory of a web application, contain data that is not sensitive. It can be accessed by any, authenticated or unauthenticated, clients. The agent uses lists of *not-enforced rules* to identify these resources in the web application.

The agent matches incoming requests to the lists of not-enforced rules. When a request matches a not-enforced rule, the agent bypasses the call to AM:

* If an unauthenticated user sent the request, the agent does not redirect the user to log in.

* If an authenticated user sent the request, the agent does not request a policy evaluation from AM.

Use not-enforced rules to reduce the number of unnecessary calls to AM, and therefore improve the performance and speed of your application.

The following image shows the data flow when Web Agent evaluates not-enforced rules for a request:

![Data flow when Web Agent evaluates not-enforced rules for a request](_images/not-enforced-flow.svg)

1-2. A client requests a resource and the agent checks whether the request matches a rule in a not-enforced list.

3-5. If the request matches a rule, the agent passes the request without requiring authentication or policy decisions. Otherwise, the agent checks whether rules are inverted.

6-10. If the request matches an inverted rule, the agent passes the request without requiring authentication or policy decisions. Otherwise, the agent enforces authentication and policy decisions.

## Conventions for not-enforced rules

Consider the following about not-enforced rules:

* Web servers normalize request URLs as described in [RFC 3986: Normalization and comparison](https://datatracker.ietf.org/doc/html/rfc3986#section-6) before passing them to the agent. The agent compares the normalized URL to the not-enforced rule.

* Trailing forward-slashes `/` can represent a directory. Therefore, `/images/` does not match `/images`, but does match `/images/index.html`

### Invert not-enforced URL rules

Invert all rules in a not-enforced URL list by setting [Invert Not-Enforced URLs](../properties-reference/com.sun.identity.agents.config.notenforced.url.invert.html) to `true`.

Consider the following when you invert all rules:

* If [Not-Enforced URL List](../properties-reference/com.sun.identity.agents.config.notenforced.url.html) is empty, all URLs are enforced.

* At least one URL must be enforced. To allow access to any URL without authentication, consider disabling the agent.

### Wildcards

For more information about using wildcards, refer to [Wildcards](https://docs.pingidentity.com/pingam/8.1/am-authorization/resource-types-ui.html#wildcards).

#### Multi-level wildcard (`*`)

The following list summarizes the behavior of the multi-level wildcard (`*`):

* Matches zero or more occurrences of any character except for the question mark (`?`).

* Spans multiple levels in a URL.

* Cannot be escaped. Therefore, the backslash (`\`) or other characters cannot be used to escape the asterisk, as such `\*`.

* Cannot be used in the same rule as the one-level wildcard (`-*-`) or regular expression.

* Explicit patterns are required to match URL parameters. For example:

  * URL patterns ending with `/foo*` do not match URLs with parameters

  * URL patterns ending with `/foo*?*` match any parameter

**Multi-level wildcard for not-enforced IP rules**

| Rules in [Not-Enforced IP List](../properties-reference/com.sun.identity.agents.config.notenforced.ip.html) | Matches request IP            | Does not match request IP |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------- |
| `192.168.1.*`                                                                                               | `192.168.1.0``192.168.1.0/24` | `192.168.0.1`             |

**Multi-level wildcard for not-enforced URI rules**

| Rules in [Not-Enforced URL List](../properties-reference/com.sun.identity.agents.config.notenforced.url.html) | Matches request URL                                                                                            | Does not match request URL                                                                          |
| ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `http://A-examp.com:8080/*`                                                                                   | `http://A-examp.com:8080/``http://A-examp.com:8080/index.html``http://A-examp.com:8080/x.gif`                  | `http://B-examp.com:8080/``http://A-examp.com:8090/index.html``http://A-examp.com:8080/a?b=1`       |
| `http://A-examp.com:8080/*.html`                                                                              | `http://A-examp.com:8080/index.html``http://A-examp.com:8080/pub/ab.html``http://A-examp.com:8080/pri/xy.html` | `http://A-examp.com/index.html``http://A-examp.com:8080/x.gif``http://B-examp.com/index.html`       |
| `http://A-examp.com:8080/*/ab`                                                                                | `http://A-examp.com:8080/pri/xy/ab/xy/ab``http://A-examp.com:8080/xy/ab`                                       | `http://A-examp.com/ab``http://A-examp.com/ab.html``http://B-examp.com:8080/ab`                     |
| `http://A-examp.com:8080/ab/*/de`                                                                             | `http://A-examp.com:8080/ab/123/de``http://A-examp.com:8080/ab/ab/de``http://A-examp.com:8080/ab/de/ab/de`     | `http://A-examp.com:8080/ab/de``http://A-examp.com:8090/ab/de``http://B-examp.com:8080/ab/de/ab/de` |

#### One-level wildcard (`-*-`)

The following list summarizes the behavior of the one-level wildcard (`-*-`):

* Matches zero or more occurrences of any character except for the forward-slash (`/`) and the question mark (`?`).

* Does not span across multiple levels in a URL.

* Cannot be escaped. Therefore, the backslash (`\`) or other characters cannot be used to escape the hyphen-asterisk-hyphen, like this `\-*-`.

* Cannot be used in the same rule as the multi-level wildcard (`*`) or regular expression.

**One-level wildcard for not-enforced URI rules**

| Rules in [Not-Enforced URL List](../properties-reference/com.sun.identity.agents.config.notenforced.url.html) | Matches request URL                                                                              | Does not match request URL                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `http://A-examp.com:8080/b/-*-`                                                                               | `http://A-examp.com:8080/b/``http://A-examp.com:8080/b/cd`                                       | `http://A-examp.com:8080/b``http://A-examp.com:8080/b/cd/` (This URL should match the rule, but does not because of the known issue AMAGENTS-4672.)`http://A-examp.com:8080/b/c?d=e``http://A-examp.com:8080/b/cd/e``http://A-examp.com:8090/b/` |
| `http://A-examp.com:8080/b/-*-/f`                                                                             | `http://A-examp.com:8080/b/c/f``http://A-examp.com:8080/b/cde/f`                                 | `http://A-examp.com:8080/b/c/e/f``http://A-examp.com:8080/f/`                                                                                                                                                                                    |
| `http://A-examp.com:8080/b/c-*-/f`                                                                            | `http://A-examp.com:8080/b/cde/f``http://A-examp.com:8080/b/cd/f``http://A-examp.com:8080/b/c/f` | `http://A-examp.com:8080/b/c/e/f``http://A-examp.com:8080/b/c/``http://A-examp.com:8080/b/c/fg`                                                                                                                                                  |

#### Multiple wildcards

When multiple wildcards are included in the same rule of a [Not-Enforced URL List](../properties-reference/com.sun.identity.agents.config.notenforced.url.html), the agent matches the parameters in any order that they appear in a resource URI.

For example, the following rule applies to any resource URI that contains a `member_level` and `location` query parameter, in any order:

```
com.sun.identity.agents.config.notenforced.url[1]={agentUrl}/customers/*?*member_level=*&location=*
```

In the following example, the requests would be not-enforced:

```
https://www.example.com/customers/default.jsp?member_level=silver&location=fr
https://www.example.com/customers/default.jsp?location=es&member_level=silver
https://www.example.com/customers/default.jsp?location=uk&vip=true&member_level=gold
```

### Regular expressions

|   |                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Regular expressions are evaluated differently by different engines. When you use regular expressions in not-enforced lists, make sure that the expressions are evaluated in the way you expect. Double check that the correct URLs are enforced and not enforced. |

Set [Regular Expressions for Not-Enforced URLs](../properties-reference/com.forgerock.agents.notenforced.url.regex.enable.html) to `true`, and consider the following for using regular expressions in not-enforced rules:

* Wildcards cannot be used. The asterisk `*` is not treated as a wildcard, but is treated as part of the expression, representing repetition of the last character 0-n times.

* The following formats cannot be used:

  * Netmask CIDR notation

  * IP address ranges

  However, regular expressions can match a range of IP addresses, such as:

  ```
  com.sun.identity.agents.config.notenforced.ip[1]=192\.168\.10\.(10|\d)
  ```

* If an invalid regular expression is specified in a rule, the rule is dropped, and an error message is logged.

### HTTP Methods

Rules that apply an HTTP method filter are configured as custom properties in AM.

Add one or more HTTP method keywords followed by an index value. The not-enforced rule is applied when the incoming request uses the HTTP method. Keywords include but are not restricted to `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE`, and `OPTIONS`.

If the same method is used in multiple rules, increment the index to make the rule unique:

```
com.sun.identity.agents.config.notenforced.url[PATCH,1]=http://www.example.com:8080/scripts/*
com.sun.identity.agents.config.notenforced.url[PATCH,2]=http://www.other.com:8080/scripts/*
```

By default, no HTTP method is specified for a rule, and all methods are not-enforced for that rule. When one or more HTTP methods are specified, only those methods are not-enforced; methods that are not specified are enforced.

The following example does not enforce OPTIONS requests to the `scripts` directory, but does enforce other HTTP methods:

```
com.sun.identity.agents.config.notenforced.url[OPTIONS,1]=http://www.example.com:8080/scripts/*
```

To specify a list of methods, add multiple rules:

```
com.sun.identity.agents.config.notenforced.url[OPTIONS,1]=http://www.example.com:8080/scripts/*
com.sun.identity.agents.config.notenforced.url[PATCH,2]=http://www.other.com:8080/scripts/*
com.sun.identity.agents.config.notenforced.url[TRACE,3]=http://www.example.com:8080/scripts/*
```

Unrecognized methods can invalidate a rule.

### Compound rules

Configure compound rules in [Not-Enforced URL from IP Processing List](../properties-reference/org.forgerock.agents.config.notenforced.ipurl.html).

In the following example, the agent does not enforce HTTP requests from the IP addresses `192.6.8.0/24` to any file in `/public`, or any files or directories that start with the string `login` in the directory `/free_access URI`:

```
org.forgerock.agents.config.notenforced.ipurl[1]=192.6.8.0/24|http://www.example.com:8080/public/* */free_access/login*
```

### Encoding non-ASCII characters in rules

Percent-encode resources that use non-ASCII characters.

For example, to match resources to the URI `http://www.example.com/forstå`, specify the following percent-encoded rule:

```
/forst%C3%A5/*
```

---

---
title: Policy enforcement
description: Set up PingAM as the policy decision point for PingAM Web Agent, enforce resource policies, and retrieve advice and response attributes from policy decisions.
component: web-agents
version: 2026
page_id: web-agents:user-guide:pep
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/pep.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  pep-enforce: Enforce a policy decision from AM
  retrieve_advice_or_response_attributes_from_policy_decisions: Retrieve advice or response attributes from policy decisions
---

# Policy enforcement

The agent evaluates policies as defined by the [Policy evaluation mode (AM\_POLICY\_CACHE\_MODE)](configure-envvars.html#envvar-AM_POLICY_CACHE_MODE) environment variable. For information about caching policy decisions, refer to [Caches](caching.html).

This example sets up AM as a policy decision point for requests processed by Web Agent. Before you start, install a Web Agent as described in the [Installation](../installation-guide/preface.html), with the following values:

* AM server URL: `https://am.example.com:8443/am`

* Agent URL: `https://agent.example.com:443`

* Agent profile name: `web-agent`

* Agent profile realm: `/`

* Agent profile password: `/secure-directory/pwd.txt`

## Enforce a policy decision from AM

1. Using the [PingAM documentation](https://docs.pingidentity.com/pingam/8.1/index.html) for information, log in to AM as an administrator, and make sure you are managing the `/` realm.

2. Add a Web Agent profile:

   1. In the AM admin UI, select Applications > Agents > Web.

   2. Add an agent with the following values:

      * Agent ID: `web-agent`

      * Agent URL: `https://agent.example.com:443`

      * Server URL: `https://am.example.com:8443/am`

      * Password: `password`

3. Add a policy set and policy:

   1. In the AM admin UI, select Authorization > Policy Sets, and add a policy set with the following values:

      * Id : `PEP`

      * Resource Types : `URL`

   2. In the policy set, add a policy with the following values:

      * Name : `PEP-policy`

      * Resource Type : `URL`

      * Resources : `*://*:*/*`

   3. On the Actions tab, add actions to allow HTTP `GET` and `POST`.

   4. On the Subjects tab, remove any default subject conditions, add a subject condition for all `Authenticated Users`.

4. Assign the new policy set to the agent profile:

   1. In the AM admin UI, Select Applications > Agents > Web, and select your agent.

   2. On the agent page, select the AM Services tab.

   3. Set Policy Set to `PEP`, and then click Save.

5. Test the setup:

   1. In the AM admin UI, select Identities > Add Identity, and add a test user with the following values:

      * Username : `bjensen`

      * First name : `Babs`

      * Last name : `Jensen`

      * Email Address : `bjensen@example.com`

      * Password : `Ch4ng3!t`

   2. Log out of AM, and clear any cookies.

   3. Go to `https://agent.example.com:443`. The AM login page is displayed.

   4. Log in to AM as user `bjensen`, password `Ch4ng3!t`, to access the web page protected by the Web Agent.

## Retrieve advice or response attributes from policy decisions

When AM makes a policy decision, it communicates an entitlement to the agent, which can optionally include advice and response attributes.

When AM denies a request with advice, the agent uses the advice to take remedial action. For example, when AM denies a request because the authentication level is too low, it can send advice to increase the authentication level. The agent then prompts the user to reauthenticate at a higher level, for example, by using a one-time password.

When AM allows a request it can include the following types of response attributes in the entitlement:

* Subject response attributes: Any LDAP user attribute configured for the identity store where AM looks up the user's profile. Learn more in [Identity stores](https://docs.pingidentity.com/pingam/8.1/setup/setting-up-identity-stores.html) in AM's *Setup guide*.

  The agent adds the listed attributes to the response.

* Static response attributes: Any key:value pair, for example, `FrequentFlyerStatus`: `gold`.

  Depending on the value of [Response Attribute Map](../properties-reference/com.sun.identity.agents.config.response.attribute.mapping.html), and [Response Attribute Fetch Mode](../properties-reference/com.sun.identity.agents.config.response.attribute.fetch.mode.html), the agent adds the listed attributes to HTTP headers or HTTP cookies in the response.

This example builds on the example in [Enforce a policy decision from AM](#pep-enforce). Set up and test that example first.

1. Configure subject response attributes and static response attributes in the AM policy you created earlier:

   1. In the AM admin UI, select the `PEP-policy`, and go to the Response Attributes tab.

   2. In the SUBJECT ATTRIBUTES frame, select one or more of the available attributes. For example, select `cn`.

   3. In the STATIC ATTRIBUTES frame, add a response attribute pair. For example, add the following pair:

      * PROPERTY NAME: `FrequentFlyerStatus`

      * PROPERTY VALUE: `gold`

   4. Click Save Changes.

2. In the AM admin UI, select the `web-agent` you created earlier.

   The agent must use the AM policy set and realm where the response attributes are configured.

   If the response attributes are not present in the policy decision from AM, the agent does not create the corresponding HTTP header or cookie.

3. In the Application tab, set Response Attribute Fetch Mode to `HTTP-HEADER` or `HTTP-COOKIE` to select whether to map response attribute names to HTTP header names or HTTP cookie names.

   Learn more in [Response Attribute Fetch Mode](../properties-reference/com.sun.identity.agents.config.response.attribute.fetch.mode.html).

4. In the Response Attribute Map field, map the subject response attributes you selected in AM:

   * Key: `cn`

   * Value: `CUSTOM-name`

     The name of the AM response attribute `cn` is mapped to the HTTP header or cookie called `CUSTOM-name`. The value is taken from the user profile.

     Learn more in [Response Attribute Fetch Mode](../properties-reference/com.sun.identity.agents.config.response.attribute.fetch.mode.html).

5. In the Response Attribute Map field, map the static response attributes you added in AM:

   * Key: `FrequentFlyerStatus`

   * Value: `CUSTOM-flyer-status`

     The name of the AM response attribute `FrequentFlyerStatus` is mapped to the HTTP header or cookie called `CUSTOM-flyer-status`. The value is `gold`.

     Learn more in [Response Attribute Map](../properties-reference/com.sun.identity.agents.config.response.attribute.mapping.html)

---

---
title: POST data preservation
description: Configure PingAM Web Agent POST data preservation to save and replay form data after authentication, with CSRF attack mitigation guidance.
component: web-agents
version: 2026
page_id: web-agents:user-guide:pdp
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/pdp.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  security_considerations_for_post_data_preservation: Security considerations for POST data preservation
  pdp-csrf: Defend against CSRF attacks when using POST data preservation
  csrf_attack_when_post_data_preservation_is_disabled: CSRF attack when POST data preservation is disabled
  csrf_attack_when_post_data_preservation_is_enabled: CSRF attack when POST data preservation is enabled
---

# POST data preservation

Use POST data preservation in environments where clients submit form data, and have short-lived sessions.

When POST data preservation is enabled, and an unauthenticated client posts data to a protected resource, the agent stores the POST data temporarily, and redirects the client to the login screen. The data can be any POST content, such as HTML form data or a file upload. After successful authentication, the agent recovers the stored POST data, and automatically submits it to the protected resource.

The following image shows a simplified data flow, when an unauthenticated client POSTs data to a protected web application:

![POST data preservation](_images/pdp-flow.svg)

Web Agent guarantees the integrity of the data, and the authenticity of the client as follows:

1. An unauthenticated client requests a POST to a protected resource.

2. The agent stores the POST data temporarily in the directory defined by [POST Data Storage Directory](../properties-reference/org.forgerock.agents.config.postdata.preserve.dir.html), and saves data about the request in a standard pre-authentication cookie.

3. The agent sets a pre-authentication cookie in the browser, and redirects to the `/authorize` endpoint in AM.

4. The client authenticates with AM.

5. AM sends an authentication response to the registered redirect URI.

6. The agent retrieves the original application URL from the pre-authentication cookie, and replays the request with its body content to the server. The authentication response includes an OIDC token, which the agent sets as a secure cookie in the browser.

7. The agent sends a self-submitting form to the client browser, that includes the form data the user attempted to post in step 1. The self-submitting form POSTs to the protected resource.

For information about configuration properties, refer to [POST data preservation](../properties-reference/preface.html#post_data_preservation).

## Security considerations for POST data preservation

POST data is stored temporarily in the agent file system before a user is authenticated. Therefore, any unauthenticated user can POST a file that is then stored by the agent. Consider the following when you configure POST data preservation:

* Payloads from unauthenticated users are stored in the agent files system. If your threat evaluation does not accept this risk, do not use POST data preservation; set [Enable POST Data Preservation](../properties-reference/com.sun.identity.agents.config.postdata.preserve.enable.html) to `false`.

* By default, POST data is stored in the installation directory, `/path/to/web_agents/agent_type/instances/agent_n/pdp-cache`. To store POST data in a dedicated directory, set [POST Data Storage Directory](../properties-reference/org.forgerock.agents.config.postdata.preserve.dir.html). Make sure that the new directory has the correct read/write permissions for the ID that the server uses.

* Set the directory permissions to minimize the following risks:

  * Permissive access to POST data.

  * Leakage of personally identifiable information (PII).

* POST data is stored for the time defined by [POST Data Entries Cache Period](../properties-reference/com.sun.identity.agents.config.postcache.entry.lifetime.html) and then deleted. To identify threats in POST data before it is deleted, make sure Intrusion Detection Systems inspect the data within the specified time.

## Defend against CSRF attacks when using POST data preservation

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Cross-site request forgery attacks (CSRF or XSRF) can be a cause of serious vulnerabilities in web applications. It is the responsibility of the protected application to implement countermeasures against such attacks, because Web Agent cannot provide generic protection against CSRF. Ping Identity recommends following the latest guidance from the [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html).When POST data preservation is enabled, captured POST data that is replayed appears to come from the same origin as the protected application, not from the site that originated the request. Therefore, CSRF defenses that rely solely on checking the origin of requests, such as SameSite cookies or Origin headers, are not reliable.To defend against CSRF attacks when POST data preservation is enabled, the agent uses a secure cookie and a nonce. The nonce must correspond to the authentication response from AM. This defense during authentication is specified in [Cross-Site Request Forgery](https://www.rfc-editor.org/rfc/rfc6749#section-10.12).Ping Identity strongly recommends using token-based mitigations against CSRF, and relying on other measures only as a defense in depth, in accordance with OWASP guidance. |

### CSRF attack when POST data preservation is disabled

The following image shows a simplified data flow during a CSRF attack on an authenticated client when POST data preservation is disabled. In this limited scenario, the agent SameSite setting is enough to defend the web application:

![Flow of data showing how in a limited scenario](_images/csrf-no-pdp-flow.svg)

### CSRF attack when POST data preservation is enabled

The following image shows a simplified data flow during a CSRF attack on an authenticated client when POST data preservation is enabled. In this scenario, the SameSite setting **is not** enough to defend the web application:

![Flow of data showing how the SameSite setting does not protect a client from a CSRF attack when POST data preservation is enabled.](_images/csrf-pdp-flow.svg)

---

---
title: SSO-only mode
description: "Configure PingAM Web Agent in SSO-only mode to manage user authentication without policy enforcement, using PingAM's authentication service to verify identity."
component: web-agents
version: 2026
page_id: web-agents:user-guide:sso-only-mode
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/sso-only-mode.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# SSO-only mode

Web Agent intercepts all inbound client requests to access a protected resource and processes the request based on the [Enable SSO Only Mode](../properties-reference/com.sun.identity.agents.config.sso.only.html) property.

The configuration setting determines the mode of operation that should be carried out on the intercepted inbound request, as follows:

* When `true`, the agent manages user authentication only. The filter invokes the AM Authentication Service to verify the identity of the user. If the identity is verified, the user is issued a session token through AM's session service.

* When `false`, which is the default, the agent also manages user authorization, by using the policy engine in AM.

---

---
title: User guide
description: User guide for PingAM Web Agent, covering configuration, policy enforcement, SSO, caching, logout, and integration with PingAM and PingOne Advanced Identity Cloud.
component: web-agents
version: 2026
page_id: web-agents:user-guide:preface
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/preface.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
---

# User guide

This guide describes how to use Web Agent.
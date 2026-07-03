---
title: About Web Agent
description: "Overview of PingAM Web Agent: components, configuration locations, request processing flow, realms, and session management."
component: web-agents
version: 2026
page_id: web-agents:user-guide:about
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/about.html
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
title: Continuous security
description: Configure PingAM Web Agent to pass request context to PingAM in an environment map, enabling policy conditions based on client IP, DNS name, cookies, and headers.
component: web-agents
version: 2026
page_id: web-agents:user-guide:continuous-security
canonical_url: https://docs.pingidentity.com/web-agents/2026/user-guide/continuous-security.html
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
---
title: About Java Agent
description: "Overview of PingAM Java Agent architecture: agent components, configuration modes, session handling, and the request processing flow."
component: java-agents
version: 2026
page_id: java-agents:user-guide:about
canonical_url: https://docs.pingidentity.com/java-agents/2026/user-guide/about.html
section_ids:
  about-components: Agent components
  configuration: Agent configuration
  about-bootstrap-properties: AgentBootstrap.properties
  agentconfiguration_properties: AgentConfiguration.properties
  agentPassword-properties: AgentPassword.properties
  agentkey-properties: AgentKey.properties
  agent_logback_xml: agent-logback.xml
  changing-configuration-properties: Change the agent configuration
  realms: Realms
  agent_profile_realm: Agent profile realm
  policy_evaluation_realm: Policy evaluation realm
  user_realm: User realm
  sessions: Sessions
  request-process-flow: Request flow
---

# About Java Agent

Java Agent is a PingAM or Advanced Identity Cloud add-on component that operates as a Policy Enforcement Point (PEP) or policy agent for web applications deployed on a Java container.

Java Agents intercept inbound requests to web applications. Depending on the *filter mode* configuration, Java Agents interact with AM to:

* Ensure that clients provide appropriate authentication.

* Enforce AM resource-based policies.

This chapter covers how Java Agents work and how their features can protect web applications.

## Agent components

Java Agent includes the following main components:

* Agent Filter

  Intercepts inbound client requests to a resource and processes them based on the filter mode of operation.

* Agent Application

  Deployed as `agentapp.war`, it is required for authentication and the cross-domain single sign-on (CDSSO) flow.

The following components are not part of Java Agent, but they play an important part in the agent operation:

* AM SDKs

  A set of APIs required to interact with AM.

* Agent Profile

  A set of configuration properties that define the agent behavior. The agent profile can be stored in AM's configuration store or as a text file local to the agent installation.

The following image shows the Java Agent components when the agent profile is stored in the AM configuration store:

![Java Agent components](_images/jee-policy-agent.svg)

## Agent configuration

Java Agent uses the configuration files described in this section.

The files must be in a location defined by a property added to `JAVA_OPTS`. For example, in Tomcat, the agent can take the file location from `bin/setenv.sh`, as follows:

```xml
JAVA_OPTS="$JAVA_OPTS -Dopenam.agents.bootstrap.dir=/path/to/agents/agent/agent_instance/config"
```

### AgentBootstrap.properties

This file defines bootstrap parameters. The following information is required in the file:

* Private AM URL:

  Used for communication with AM, for example, to retrieve policy information or user information. The URL is assembled from the following properties, and is required, even if the agent never contacts AM:

  * [AM Authentication Service Protocol](../properties-reference/org.forgerock.agents.am.protocol.html)

  * [AM Authentication Service Host Name](../properties-reference/org.forgerock.agents.am.hostname.html)

  * [AM Authentication Service Port](../properties-reference/org.forgerock.agents.am.port.html)

  * [AM Authentication Service Path](../properties-reference/org.forgerock.agents.am.path.html)

* [Public AM URL](../properties-reference/org.forgerock.agents.public.am.url.html):

  This URL must be provided by the user if the AM firewall rules distinguish between a public and a private URL. The agent uses this property to redirect the user's browser to public-facing URLs for login. If it is not provided, the AM private URL is used.

* Agent Profile:

  * [Agent Profile Name](../properties-reference/org.forgerock.agents.profile.name.html)

  * [Agent Profile Realm](../properties-reference/org.forgerock.agents.agent.profile.realm.html)

* [Location of Agent Configuration Repository](../properties-reference/org.forgerock.agents.config.location.html):

  Defines the agent configuration mode:

  * Local configuration mode

    The agent reads its configuration from `AgentConfiguration.properties`. When the agent is in this mode, it ignores changes made to the agent profile in AM.

    Depending on the configuration in the `AgentConfiguration.properties` file, the agent might never need to contact AM. For example, if [Autonomous mode](../properties-reference/org.forgerock.agents.fallback.mode.enabled.html) is `true`, the agent runs independently of an AM instance.

  * Remote configuration mode (default)

    The agent ignores the configuration in `AgentConfiguration.properties`, retains the retrieved bootstrap properties, and downloads the configuration from AM.

    When the first user request is made, the agent contacts AM to retrieve the agent configuration. If AM is unavailable, the request returns an `HTTP 503 Service Unavailable`.

### AgentConfiguration.properties

This file defines agent configuration settings, and overrides any properties set in the bootstrap file.

If the value of [Location of Agent Configuration Repository](../properties-reference/org.forgerock.agents.config.location.html) is `LOCAL`, the agent reads the `AgentConfiguration.properties` file after `AgentBootstrap.properties`. If the value of [Location of Agent Configuration Repository](../properties-reference/org.forgerock.agents.config.location.html) is `REMOTE`, the agent ignores this file.

In Java Agent 5.7 and earlier versions, this file was named `OpenSSOAgentConfiguration.properties`.

### AgentPassword.properties

This file defines an encrypted password for the agent profile. For more information, refer to [Encrypted Agent Password](../properties-reference/org.forgerock.agents.encrypted.password.html).

### AgentKey.properties

This file defines the following keys:

* The encryption key for the agent profile password. For more information, refer to [Encryption Key/Salt](../properties-reference/org.forgerock.agents.encryption.key.html).

* The signing key for pre-authentication cookies and POST data preservation cookies. For more information, refer to [Pre-Authn and Post Data Preservation Cookie Signing Value](../properties-reference/org.forgerock.agents.cookie.signing.value.html).

### agent-logback.xml

This file configures logging of Java Agent and third-party dependencies, using the Logback implementation of the Simple Logging Facade for Java (SLF4J) API. For more information, refer to [Manage logs](../maintenance-guide/logging.html).

### Change the agent configuration

Change the agent configuration in the following ways:

* Change the agent bootstrap configuration

  Manually edit `AgentBootstrap.properties`, and then restart the container running the agent.

* Change the agent configuration in LOCAL mode

  Manually edit the `AgentConfiguration.properties` file, and set a value for [Configuration Reload Interval](../properties-reference/org.forgerock.agents.config.reload.seconds.html).

  The interval defines the number of seconds after which the agent reads the local property file, and reloads it if has changed since it was last read.

  The value of [Location of Agent Configuration Repository](../properties-reference/org.forgerock.agents.config.location.html) must be `LOCAL`.

* Change the agent configuration in REMOTE mode

  The agent is notified by the WebSocket mechanism when its configuration is changed in AM. The agent then re-reads its configuration from AM within a few seconds.

  The value of [Location of Agent Configuration Repository](../properties-reference/org.forgerock.agents.config.location.html) must be `REMOTE`.

* Change the agent configuration on the AM admin UI

  Go to Realms > *Realm Name* > Applications > Agents > Java > *Agent Name*.

  The value of [Location of Agent Configuration Repository](../properties-reference/org.forgerock.agents.config.location.html) must be `REMOTE`.

## Realms

### Agent profile realm

The agent profile stores a set of configuration properties that define the behavior of the agent.

During agent installation, the installer prompts for the profile realm, and populates the property [Agent Profile Realm](../properties-reference/org.forgerock.agents.agent.profile.realm.html) in the bootstrap properties file. By default, the profile realm is set to the top-level realm.

The agent profile realm can be different to the user and policy evaluation realms. Groups of agents can use the same agent profile realm, which can be separate from the user and policy evaluation realms.

For information about creating agent profiles in the top-level realm or other realms, refer to [Create agent profiles](../installation-guide/pre-installation.html#create-agent-profiles).

### Policy evaluation realm

The policy evaluation realm is the realm the agent uses to request policy decisions from AM. In most circumstances, the policy evaluation realm is the same as the user realm.

The policy evaluation realm is configured by [Policy Evaluation Realm Map](../properties-reference/org.forgerock.agents.policy.evaluation.realm.map.html), and defaults to the top-level realm. The policy set to use is configured by [Policy Set Map](../properties-reference/org.forgerock.agents.policy.set.map.html) To ensure that policies are always evaluated in the user realm, set [Enable Policy Evaluation in User Authentication Realm](../properties-reference/org.forgerock.agents.user.realm.overrides.policy.evaluation.realm.enabled.html) to `true`.

In AM, only the top-level realm has a default policy set, called iPlanetAMWebAgentService. If you use a policy evaluation realm that is in a subrealm of the top-level realm, you must also define a policy set and policies in the equivalent realm in AM.

### User realm

The user realm is the realm in which a user is authenticated. In most circumstances, the user evaluation realm is the same as the policy realm.

By default, users authenticate to AM in the top-level realm, however, the agent can authenticate users in different realms depending on the request domain, path, or resource.

When a user logs out, the agent maintains the user realm. The agent obtains the realm info from the JWT, if one is available, or by calling `sessioninfo`. When the user logs out, the stored realm is passed to the logout endpoint automatically.

The first time an authenticated user requests a resource from the agent, the agent establishes the user realm from the session. It permanently associates the realm with the session in the session cache. When the session ends, the agent automatically passes the realm to the logout endpoint.

For more information about changing the user realm, refer to [Login redirect](login-redirect.html).

## Sessions

On startup, Java Agent uses the following properties to obtain a session from AM:

* [Agent Profile Name](../properties-reference/org.forgerock.agents.profile.name.html)

* [Encrypted Agent Password](../properties-reference/org.forgerock.agents.encrypted.password.html)

* [Agent Profile Realm](../properties-reference/org.forgerock.agents.agent.profile.realm.html)

The agent session lifetime is defined by the AM version and configuration, and is essentially indefinite.

For the security of your deployment, set the agent session lifetime as described in [Manage Java Agent sessions](../security-guide/access.html#agent_sessions).

If you clear agent sessions in the AM admin UI, you can accidentally kill an active agent session. If this happens, the agent detects that its session has expired and automatically obtains a new one.

## Request flow

The following simplified data flow occurs when an unauthenticated client requests a resource protected by a Java Agent and AM. The flow assumes that requests must meet the requirements of an AM policy. For more information, see [Single sign-on](https://docs.pingidentity.com/pingam/8.1/authentication-guide/about-sso.html) in AM's *Authentication and SSO guide*.

![Flow of a request through an agent.](_images/jee-agent-process-flow.svg)

* FQDN check

  When FQDN checking is enabled, the agent can redirect requests to different domains, depending on the hostname of the request. For more information, refer to [FQDN checks](fqdn-checking.html).

* Not-enforced rules check

  The agent evaluates whether the requested resource or the client IP address matches a not-enforced rule.

  If the requested resource or the client IP address matches a not-enforced rule. The agent allows access to the resource, and the client receives a response from `www.example.com`. The flow ends.

  For more information, refer to [Not-enforced rules](not-enforced-rules.html).

- Authentication

  1: The agent creates a pre-authentication cookie to protect against reply attacks. The agent uses this cookie to track the authentication request to AM. Depending on the configuration, the agent may either issue a cookie to track all concurrent authentication requests, or may issue one cookie for each request. For added security, the pre-authentication cookie can be optionally be signed.

  2: The agent sets the AM login URL, which includes the `goto` parameter for the OAuth 2.0 authorize endpoint, and

  3: The agent redirects the client to log in to AM.

  4-7: The client authenticates to AM:

  * AM's Authentication Service verifies the client credentials. AM creates an SSO token, and OIDC JWT with session information.

  * AM sends the client a self-submitting form with the OIDC JWT.

  8: The client posts the self-submitting form to the agent endpoint, and the Java Agent consumes it.

  9: The agent sets the cookie domain to the FQDN of the resource.

  10: The client attempts to access the protected resource again, and the agent intercepts the request.

  11: The agent contacts AM to validate the session contained in the OIDC JWT.

  12: AM validates the session.

- Authorization

  1: The agent contacts AM's Policy Service, requesting a decision about whether the client is authorized to access the resource.

  2: AM's Policy Service returns `ALLOW`.

  3: The agent writes the policy decision to the audit log.

  4: The agent enforces the policy decision. Because the Policy Service returned `ALLOW`, the agent performs a pass-through operation to return the resource to the client.

  5: The client accesses the resource.

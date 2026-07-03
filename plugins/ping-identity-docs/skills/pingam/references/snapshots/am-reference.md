---
title: Glossary
description: A glossary of key authentication, authorization, and identity management terms used in PingAM documentation
component: pingam
version: 8.1
page_id: pingam:am-reference:glossary
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-reference/glossary.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CIAM", "Training"]
page_aliases: ["reference:glossary.adoc"]
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

* Agent authenticator

  Entity with read-only access to multiple agent profiles defined in the same realm; allows an agent to read web service profiles.

* Application

  In general terms, a service exposing protected resources.

  In the context of AM policies, the application is a template that constrains the policies that govern access to protected resources. An application can have zero or more policies.

* Application type

  Application types act as templates for creating policy applications.

  Application types define a preset list of actions and functional logic, such as policy lookup and resource comparator logic.

  Application types also define the internal normalization, indexing logic, and comparator logic for applications.

* Attribute-based access control (ABAC)

  Access control that is based on attributes of a user, such as how old a user is or whether the user is a paying customer.

- Authenticated session

  The interval that starts after the user has authenticated and ends when the user logs out or their session is terminated. For browser-based clients, AM manages authenticated sessions across one or more applications by setting a session cookie.

  Learn more in [server-side sessions](#def-server-side-session) and [client-side sessions](#def-client-side-session).

  A [journey session](#def-journey-session) exists before an authenticated session.

- Authentication

  The act of confirming the identity of a principal.

- Authentication level

  Positive integer associated with an authentication node, usually used to require success with more stringent authentication measures when requesting resources requiring special protection.

- Authorization

  The act of determining whether to grant or to deny a principal access to a resource.

- Authorization server

  In OAuth 2.0, issues access tokens to the client after authenticating a resource owner and confirming that the owner authorizes the client to access the protected resource. AM can play this role in the OAuth 2.0 authorization framework.

- Auto-federation

  Arrangement to federate a principal's identity automatically based on a common attribute value shared across the principal's profiles at different providers.

- Bulk federation

  Batch job permanently federating user profiles between a service provider and an identity provider based on a list of matched user identifiers that exist on both providers.

- Circle of trust

  Group of providers, including at least one identity provider, who have agreed to trust each other to participate in a SAML 2.0 provider federation.

- Client

  In OAuth 2.0, requests protected web resources on behalf of the resource owner given the owner's authorization. AM can play this role in the OAuth 2.0 authorization framework.

* Client-side OAuth 2.0 tokens

  After a successful OAuth 2.0 grant flow, AM returns a token to the client. This differs from [server-side OAuth 2.0 tokens](#def-server-side-token), where AM returns a *reference* to token to the client.

- Client-side sessions

  Sessions for which AM returns session state to the client after each request, and requires the state to be passed in with the subsequent request.

  For browser-based clients, AM sets a cookie in the browser that contains the session state. When the browser returns the cookie, AM decodes the session state from the cookie.

  A [journey session](#def-journey-session) and an [authenticated session](#def-auth-session) can be a client-side session.

- Conditions

  Defined as part of policies, these determine the circumstances under which a policy applies.

  Environmental conditions reflect circumstances like the client IP address, time of day, how the subject authenticated, or the authentication level achieved.

  Subject conditions reflect characteristics of the subject like whether the subject authenticated, the identity of the subject, or claims in the subject's JWT.

- Configuration datastore

  LDAP directory service holding AM configuration data.

- Cross-domain single sign-on (CDSSO)

  AM capability allowing single sign-on across different DNS domains.

- Delegation

  Granting users administrative privileges with AM.

- Entitlement

  Decision that defines which resource names can and cannot be accessed for a given identity in the context of a particular application, which actions are allowed and which are denied, and any related advice and attributes.

- Extended metadata

  Federation configuration information specific to AM.

- Extensible Access Control Markup Language (XACML)

  Standard, XML-based access control policy language, including a processing model for making authorization decisions based on policies.

- Federation

  Standardized means for aggregating identities, sharing authentication and authorization data information between trusted providers, and allowing principals to access services across different providers without authenticating repeatedly.

- Fedlet

  Service provider application capable of participating in a circle of trust and allowing federation without installing all of AM on the service provider side; AM lets you create Java Fedlets.

- Hot swappable

  Refers to configuration properties for which changes can take effect without restarting the container where AM runs.

- Identity

  Set of data that uniquely describes a person or a thing such as a device or an application.

- Identity federation

  Linking of a principal's identity across multiple providers.

- Identity provider (IdP)

  Entity that produces assertions about a principal (such as how and when a principal authenticated, or that the principal's profile has a specified attribute value).

- Identity repository

  Another name for an [identity store](#def-identity-store).

* Identity store

  Datastore holding user profiles and group information. Different identity stores can be defined for different realms.

* Java agent

  Java web application installed in a web container that acts as a policy enforcement point, filtering requests to other applications in the container with policies based on application resource URLs.

- Journey session

  The interval that starts when the user begins progressing through an authentication journey and ends when the journey completes or the session has timed out.

  An [authenticated session](#def-auth-session) is created if they authenticate successfully.

  A journey session can be a [server-side session](#def-server-side-session) or a [client-side session](#def-client-side-session).

- Metadata

  Federation configuration information for a provider.

- No session tree

  Tree that doesn't result in an authenticated session when it successfully completes.

- Policy

  Set of rules that define who is granted access to a protected resource when, how, and under what conditions.

- Policy agent

  Java, web, or custom agent that intercepts requests for resources, directs principals to AM for authentication, and enforces policy decisions from AM.

- Policy Administration Point (PAP)

  Entity that manages and stores policy definitions.

- Policy Decision Point (PDP)

  Entity that evaluates access rights and then issues authorization decisions.

- Policy Enforcement Point (PEP)

  Entity that intercepts a request for a resource and then enforces policy decisions from a PDP.

- Policy Information Point (PIP)

  Entity that provides extra information, such as user profile attributes that a PDP needs to make a decision.

* Principal

  Represents an entity that has been authenticated (such as a user, a device, or an application), and thus is distinguished from other entities.

  When a [Subject](#def-subject) successfully authenticates, AM associates the Subject with the Principal.

* Privilege

  In the context of delegated administration, a set of administrative tasks that can be performed by specified identities in a given realm.

* Provider federation

  Agreement among providers to participate in a circle of trust.

* Realm

  AM unit for organizing configuration and identity information.

  Realms can be used for example when different parts of an organization have different applications and identity stores, and when different organizations use the same AM deployment.

  Administrators can delegate realm administration. The administrator assigns administrative privileges to users, allowing them to perform administrative tasks within the realm.

* Resource

  Something a user can access over the network such as a web page.

  Defined as part of policies, these can include wildcards to match multiple actual resources.

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

- Server-side OAuth 2.0 tokens

  After a successful OAuth 2.0 grant flow, AM returns a *reference* to the token to the client, rather than the token itself. This differs from [client-side OAuth 2.0 tokens](#def-client-side-token), where AM returns the entire token to the client.

* Server-side sessions

  Sessions that reside in the Core Token Service (CTS) token store. Server-side sessions could also be cached in memory on one or more AM servers. AM tracks these sessions to handle events like logout and timeout, to permit session constraints, and to notify applications involved in SSO when a session ends.

  A [journey session](#def-journey-session) and an [authenticated session](#def-auth-session) can be a server-side session.

* Service provider (SP)

  Entity that consumes assertions about a principal (and provides a service that the principal is trying to access).

* Session high availability

  Capability that lets any AM server in a clustered deployment access shared, persistent information about users' sessions from the CTS token store. The user does not need to log in again unless the entire deployment goes down.

* Session token

  Unique identifier issued by AM after successful authentication. For [server-side sessions](#def-server-side-session), the session token is used to track a principal's session.

* Single log out (SLO)

  Capability allowing a principal to end a session once, thereby ending her session across multiple applications.

* Single sign-on (SSO)

  Capability allowing a principal to authenticate once and gain access to multiple applications without authenticating again.

* Site

  Group of AM servers configured the same way, accessed through a load balancer layer. The load balancer handles failover to provide service-level availability.

  The load balancer can also be used to protect AM services.

* Standard metadata

  Standard federation configuration information that you can share with other access management software.

- Stateless service

  Stateless services do not store any data locally to the service. When the service requires data to perform any action, it requests it from a datastore. For example, a stateless authentication service stores session state for logged-in users in a database. This way, any server in the deployment can recover the session from the database and service requests for any user.

  All AM services are stateless unless otherwise specified. Learn more in [client-side sessions](#def-client-side-session) and [server-side sessions](#def-server-side-session).

* Subject

  Entity that requests access to a resource

  When an identity successfully authenticates, AM associates the identity with the [Principal](#def-principal) that distinguishes it from other identities. An identity can be associated with multiple principals.

* Web Agent

  Native library installed in a web server that acts as a policy enforcement point with policies based on web page URLs.

---

---
title: Reference
description: Access comprehensive reference information for PingAM, including Amster entity references, audit logging, authentication settings, token types, ports, service configuration, and REST API documentation
component: pingam
version: 8.1
page_id: pingam:am-reference:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-reference/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Administration", "Configuration"]
page_aliases: ["index.adoc", "reference:preface.adoc"]
---

# Reference

The following table summarizes the reference information available in the wider AM documentation.

| Reference information                                                                          | Useful links                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amster                                                                                         | [Amster entity reference](../entity-reference/preface.html)                                                                                                                                           |
| Audit log formats, event components, and fields you can filter by.                             | [Audit logging reference](../monitoring/audit-logging-ref.html)                                                                                                                                       |
| Authentication settings, endpoints, node configuration, supported callbacks.                   | [Authentication reference](../am-authentication/authn-reference.html)                                                                                                                                 |
| Core Token Service token reference information, including LDAP attributes and example formats. | [CTS token types](../cts/cts-token-types.html)                                                                                                                                                        |
| Ports used                                                                                     | [Default ports used by AM](../security/am-ports-used.html)                                                                                                                                            |
| Configuration settings for AM services such as the OAuth2 provider, Email, and CORS.           | [Configure AM services](../setup/services-configuration.html)                                                                                                                                         |
| Deployment configuration, such as advanced server properties.                                  | [Manage deployment configuration](../setup/deployment-configuration-reference.html)                                                                                                                   |
| Public API Javadoc                                                                             | [PingAM Java API Specification](../_attachments/apidocs/index.html)                                                                                                                                   |
| Common REST API                                                                                | * [REST API endpoints](../am-rest/rest-endpoints.html)

* Log in to the AM admin UI and access the API at the following URL:

  ```none
  https://am.example.com:8443/am/ui-admin/#api/explorer
  ``` |

[icon: flag, set=fad, size=3x]

#### [Standards support](am-supported-standards.html)

View the wide range of standards that AM supports.

[icon: browser, set=fad, size=3x]

#### [Service endpoints](endpoints-reference.html)

Learn about the AM web service endpoints.

[icon: edit, set=fad, size=3x]

#### [Glossary](endpoints-reference.html)

The definitions for terminology used within AM documentation.

---

---
title: Service endpoints
description: Reference for PingAM service endpoints including JSP files, REST API endpoints, and well-known URIs with guidance on blocking unused endpoints
component: pingam
version: 8.1
page_id: pingam:am-reference:endpoints-reference
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-reference/endpoints-reference.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Endpoints", "JSP"]
page_aliases: ["reference:endpoints-reference.adoc"]
section_ids:
  jsp-endpoints: JSP files
  web-inf-endpoints: Configure access to endpoints
  json-rest-endpoints: REST API endpoints
  well-known-endpoints: Well-known endpoints
---

# Service endpoints

A service endpoint is an entry point to a web service. This page lists AM service endpoints that are accessible by default.

If you're certain a particular AM service endpoint isn't used in your deployment, you can block access to the endpoint.

Learn more in [Secure network communication](../security/securing-communications.html).

## JSP files

Some AM JSP pages are directly accessible as service endpoints. The following sections describe the files for those JSP pages. Directory paths in this section are relative to AM's deployment path, for example, `/path/to/tomcat/webapps/am/`.

> **Collapse: Top-level JSP files**
>
> You will find these files in the top-level directory of AM's deployment path.
>
> * `Logback.jsp`
>
>   Provides a page to configure debug logging.
>
>   See [Debug logging](../monitoring/debug-logging.html) for details.
>
> * `encode.jsp`
>
>   Provides a page to encode a cleartext password for use in SAML entity configurations.
>
> * `getServerInfo.jsp`
>
>   Supports requests for server information. This page is used internally by AM.
>
> * `isAlive.jsp`
>
>   Displays a "Server is ALIVE" message when AM is ready to serve requests.
>
> * `proxyidpfinder.jsp`
>
>   Supports access to a remote identity provider through the federation broker.
>
> * `services.jsp`
>
>   Only used for ssoadm, which has been removed.
>
> * `showServerConfig.jsp`
>
>   Displays system configuration information, including the deployment URL, OS, Java VM, configuration directory, and more.

> **Collapse: Authentication JSP files**
>
> The JSP files in the `config/auth/default*/` directories were used only for authentication modules.

> **Collapse: OAuth 2.0 JSP files**
>
> The JSP file, `oauth2/registerClient.jsp`, provides a template page to register an OAuth 2.0 client application without using the main console.
>
> The JSP files in the `oauth2c/` directory were used only for authentication modules. They weren't intended to be used directly as external endpoints.

> **Collapse: WS Federation JSP files**
>
> The JSP files in the `wsfederation/jsp/` directory provide endpoints used in WS-Federation deployments.

|   |                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Previous versions of AM provided JSPs for SAML 2.0 standalone mode. These JSPs are now deprecated.You can still invoke the JSPs because they're mapped to URLs for backward compatibility, but any customizations to the JSPs will be lost.Learn more in the [release notes](https://docs.pingidentity.com/pingam/release-notes/removed.html). |

## Configure access to endpoints

When protecting an AM server, consider blocking external access to unused services. You can either configure a reverse proxy (nginx, for example) to prevent access to endpoints, or configure the deployment descriptor file, `WEB-INF/web.xml`, to use a custom version of `AmServletInitializer`.

The Guice dependency injection framework initializes servlets and filters programmatically, but you can still customize filters that don't use Guice, such as `SecureCookieFilter` or `SetHeadersFilter`. Register new filters by adding `<filter>` and `<filter-mapping>` elements to your `web.xml` file. If you're overriding an existing filter, you only need to define the `<filter>` element, as `AmFilterInitializer` handles the corresponding mapping.

Find an example of customizing the `SecureCookieFilter` in [Exclude cookies from the filter](../security/secure-cookie-filter.html#exclude-cookies-from-secure-filter).

The `web.xml` file and AM endpoints may change from release to release. Review the [API documentation](../am-rest/rest-endpoints.html) and release notes to check for changes.

Learn more about securing your deployment by restricting access to endpoints in [Protecting PingAM with PingGateway](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/protect-am.html), [How do I remove admin UI access in PingAM](https://support.pingidentity.com/s/article/How-do-I-remove-admin-UI-access-in-PingAM) and [Best practice for blocking the top level realm in a proxy for PingAM](https://support.pingidentity.com/s/article/Best-practice-for-blocking-the-top-level-realm-in-a-proxy-for-PingAM).

## REST API endpoints

REST API endpoints are discussed in detail as follows:

| What do you want to do?                                                                                                                      | APIs                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Authenticate to AM and log out                                                                                                               | * [Authenticate over REST](../am-authentication/authn-rest.html)

* [Log out of AM over REST](../am-authentication/logout-using-rest.html)                                                                                                                                                                                                             |
| Create and configure authentication trees                                                                                                    | - [Create a tree over REST](../am-authentication/create-auth-trees.html#create-authn-tree-rest)

- [Configure authentication trees](../am-authentication/configure-auth-trees.html)                                                                                                                                                                    |
| Manage a user's registered devices                                                                                                           | [Manage devices for MFA](../am-authentication/authn-mfa-devices.html)                                                                                                                                                                                                                                                                                  |
| Manage policies                                                                                                                              | * [Policies over REST](../am-authorization/rest-api-authz-policies.html)

* [Policy sets over REST](../am-authorization/rest-api-authz-applications.html)

* [Resource types over REST](../am-authorization/rest-api-authz-resource-types.html)

* [Policy set application types over REST](../am-authorization/rest-api-authz-application-types.html) |
| Request authorization decisions                                                                                                              | [Request policy decisions over REST](../am-authorization/rest-api-authz-policy-decisions.html)                                                                                                                                                                                                                                                         |
| Use OAuth 2.0-specific endpoints to request access and refresh tokens, as well as introspect and revoke them                                 | [OAuth 2.0 endpoints](../am-oauth2/oauth2-client-endpoints.html)                                                                                                                                                                                                                                                                                       |
| Perform OAuth 2.0 administrative tasks such as registering, reading, and deleting clients                                                    | [OAuth 2.0 administration REST endpoints](../am-oauth2/oauth2-admin-endpoints.html)                                                                                                                                                                                                                                                                    |
| Use OpenID Connect-specific endpoints to retrieve information about an authenticated user, as well as validate ID tokens and check sessions. | [OpenID Connect 1.0 endpoints](../am-oidc1/oidc-client-endpoints.html)                                                                                                                                                                                                                                                                                 |
| Implement user self-registration and forgotten password reset                                                                                | - [Retrieve forgotten usernames](../user-self-service/uss-forgotten-username.html)

- [Reset forgotten passwords](../user-self-service/uss-forgotten-password.html)

- [Register a user](../user-self-service/uss-registering-users.html)                                                                                                              |
| Manage AM identities and realms                                                                                                              | [Configure identities and realms over REST](../setup/am-realms.html#sec-rest-realm-rest)                                                                                                                                                                                                                                                               |
| Manage AM scripts                                                                                                                            | [Manage scripts (REST)](../am-scripting/manage-scripts-rest.html)                                                                                                                                                                                                                                                                                      |
| Record information to help you troubleshoot AM                                                                                               | [Capture troubleshooting information](../maintenance/record-troubleshooting.html)                                                                                                                                                                                                                                                                      |
| Manage AM sessions                                                                                                                           | [Manage sessions using REST](../am-sessions/managing-sessions-REST.html)                                                                                                                                                                                                                                                                               |
| Manage AM's Security Token Service to bridge identities across web and enterprise identity access management (IAM) systems                   | * [Consume STS instances](../sts/sts-consume-rest.html)

* [Query, validate, and cancel tokens](../sts/sts-query-validate-cancel.html)                                                                                                                                                                                                                 |

## Well-known endpoints

The endpoints described in this section are [Well-known URIs](https://www.rfc-editor.org/info/rfc5785) supported by AM:

* `/.well-known/openid-configuration`

  Exposes OpenID Provider configuration by HTTP GET as specified by OpenID Connect Discovery 1.0. No query string parameters are required.

* `/uma/.well-known/uma2-configuration`

  Exposes User-Managed Access (UMA) configuration by HTTP GET as specified by UMA Profile of OAuth 2.0. No query string parameters are required.

  Find an example in [/uma/.well-known/uma2-configuration](../uma/endpoint-configuration.html).

* `/.well-known/webfinger`

  Lets a client retrieve the provider URL for an end user by HTTP GET as specified by OpenID Connect Discovery 1.0.

  Find an example in [OpenID Connect Discovery](../am-oidc1/oidc-am-provider.html#configure-openid-connect-discovery).

---

---
title: Supported standards
description: PingAM implements OAuth 2.0, OpenID Connect, SAML 2.0, UMA, and other federation and security standards
component: pingam
version: 8.1
page_id: pingam:am-reference:am-supported-standards
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-reference/am-supported-standards.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Standards", "Federation", "SAML 2.0", "OAuth 2.0", "OpenID Connect (OIDC)"]
page_aliases: ["reference:am-supported-standards.adoc"]
---

# Supported standards

AM implements the following RFCs, Internet-Drafts, and standards:

> **Collapse: Open Authentication**
>
> [RFC 4226: HOTP: An HMAC-Based One-Time Password Algorithm](https://www.rfc-editor.org/info/rfc4226), supported by the OATH authentication nodes.
>
> [RFC 6238: TOTP: Time-Based One-Time Password Algorithm](https://www.rfc-editor.org/info/rfc6238), supported by the OATH authentication nodes.
>
> For more information, refer to [Open Authentication](https://en.wikipedia.org/wiki/Initiative_for_Open_Authentication).

> **Collapse: OAuth 2.0**
>
> [RFC 6749: The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/info/rfc6749)
>
> [RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://www.rfc-editor.org/info/rfc6750)
>
> [RFC 7009: OAuth 2.0 Token Revocation](https://www.rfc-editor.org/info/rfc7009)
>
> [RFC 7515: JSON Web Signature (JWS)](https://www.rfc-editor.org/info/rfc7515)
>
> [RFC 7516: JSON Web Encryption (JWE)](https://www.rfc-editor.org/info/rfc7516)
>
> [RFC 7517: JSON Web Key (JWK)](https://www.rfc-editor.org/info/rfc7517)
>
> [RFC 7518: JSON Web Algorithms (JWA)](https://www.rfc-editor.org/info/rfc7518)
>
> [RFC 7519: JSON Web Token (JWT)](https://www.rfc-editor.org/info/rfc7519)
>
> [RFC 7522: Security Assertion Markup Language (SAML) 2.0 Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://www.rfc-editor.org/info/rfc7522)
>
> [RFC 7523: JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://www.rfc-editor.org/info/rfc7523)
>
> [RFC 7591: OAuth 2.0 Dynamic Client Registration Protocol](https://www.rfc-editor.org/info/rfc7591)
>
> [RFC 7636: Proof Key for Code Exchange by OAuth Public Clients](https://www.rfc-editor.org/info/rfc7636)
>
> [RFC 7662: OAuth 2.0 Token Introspection](https://www.rfc-editor.org/info/rfc7662)
>
> [RFC 7800: Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs)](https://www.rfc-editor.org/info/rfc7800)
>
> [RFC 8628: OAuth 2.0 Device Authorization Grant](https://www.rfc-editor.org/info/rfc8628)
>
> [RFC 8705: OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens](https://www.rfc-editor.org/info/rfc8705)
>
> [RFC 7592: OAuth 2.0 Dynamic Client Registration Management Protocol](https://www.rfc-editor.org/info/rfc7592)
>
> [Internet Draft: JWT Response for OAuth Token Introspection](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-jwt-introspection-response-03)
>
> [RFC 8693: OAuth 2.0 Token Exchange](https://www.rfc-editor.org/info/rfc8693) (Access token to access token, access token to ID token, ID token to ID token, and ID token to access token)
>
> [RFC 9101: The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR)](https://www.rfc-editor.org/info/rfc9101)
>
> [RFC 9126: OAuth 2.0 Pushed Authorization Requests](https://www.rfc-editor.org/info/rfc9126)
>
> For more information, see [OAuth 2.0](https://oauth.net/2/)

> **Collapse: OpenID Connect 1.0**
>
> [OpenID Connect Core 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-core-1_0.html).
>
> In section 5.6 of this specification, AM supports *Normal Claims*. AM does not support the optional *Aggregated Claims* and *Distributed Claims* representations.
>
> [OpenID Connect Client Initiated Backchannel Authentication Flow - Core 1.0 draft-02](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html)
>
> AM applies the guidelines suggested by the OpenID [Financial-grade API (FAPI) Working Group](https://openid.net/wg/fapi/) to the implementation of CIBA, which shapes the support of CIBA in AM.
>
> |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | Implementation Decisions Applying to CIBA Support in AM- AM only supports the CIBA "poll" mode, not the "push" or "ping" modes.
>
> - AM requires use of confidential clients for CIBA.
>
> - AM requires use of signed JSON-web tokens (JWT) to pass parameters, using one of the following algorithms:
>
>   * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.
>
>   * `PS256` - RSASSA-PSS using SHA-256.Plain JSON or form parameters for CIBA-related data is not supported. |
>
> [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html)
>
> [OpenID Connect Dynamic Client Registration 1.0](https://openid.net/specs/openid-connect-registration-1_0.html)
>
> [OpenID Connect Session Management 1.0 Draft 10](https://openid.net/specs/openid-connect-session-1_0-10.html)
>
> [OAuth 2.0 Multiple Response Type Encoding Practices](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html)
>
> [OAuth 2.0 Form Post Response Mode](https://openid.net/specs/oauth-v2-form-post-response-mode-1_0.html)
>
> [Financial-grade API: JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)](https://openid.net/specs/openid-financial-api-jarm-wd-01.html)
>
> [OpenID Connect Back-Channel Logout 1.0 Draft 06](https://openid.net/specs/openid-connect-backchannel-1_0.html).
>
> AM currently only supports backchannel logout when acting as the provider.
>
> For more information, see:
>
> * [OpenID Connect 1.0](http://openid.net/connect/)
>
> * [OpenID Connect Basic Client Implementer's Guide 1.0](https://openid.net/specs/openid-connect-basic-1_0.html)
>
> * [OpenID Connect Implicit Client Implementer's Guide 1.0](https://openid.net/specs/openid-connect-implicit-1_0.html)

> **Collapse: User-Managed Access (UMA) 2.0**
>
> [User-Managed Access (UMA) 2.0 Grant for OAuth 2.0 Authorization](https://docs.kantarainitiative.org/uma/wg/oauth-uma-grant-2.0-08.html)
>
> [Federated Authorization for User-Managed Access (UMA) 2.0](https://docs.kantarainitiative.org/uma/wg/oauth-uma-federated-authz-2.0-08.html)

> **Collapse: Security Assertion Markup Language (SAML) and Federation-related standards**
>
> AM supports SAML 2.0, although WS-Federation functionality still creates assertions in SAML v1.x format.
>
> SAML Specifications are available from the [OASIS standards page](https://www.oasis-open.org/standards/).
>
> [Web Services Federation Language (WS-Federation)](https://en.wikipedia.org/wiki/WS-Federation)
>
> [Web Services Description Language (WSDL)](https://www.w3.org/TR/wsdl/)
>
> [eXtensible Access Control Markup Language (XACML)](https://wiki.oasis-open.org/xacml)
>
> For more information, see [Security Assertion Markup Language (SAML)](http://saml.xml.org/)

> **Collapse: Encryption and signatures**
>
> Assertion encryption:
>
> [aes128-cbc](http://www.w3.org/2001/04/xmlenc#aes128-cbc)\
> [aes192-cbc](http://www.w3.org/2001/04/xmlenc#aes192-cbc)\
> [aes256-cbc](http://www.w3.org/2001/04/xmlenc#aes256-cbc)\
> [tripledes-cbc](http://www.w3.org/2001/04/xmlenc#tripledes-cbc)
>
> Assertion signatures:
>
> [rsa-sha1](http://www.w3.org/2000/09/xmldsig#rsa-sha1)\
> [rsa-sha256](http://www.w3.org/2001/04/xmldsig-more#rsa-sha256)\
> [rsa-sha384](http://www.w3.org/2001/04/xmldsig-more#rsa-sha384)\
> [rsa-sha512](http://www.w3.org/2001/04/xmldsig-more#rsa-sha512)
>
> Query string signatures:
>
> [rsa-sha1](http://www.w3.org/2000/09/xmldsig#rsa-sha1)\
> [rsa-sha256](http://www.w3.org/2001/04/xmldsig-more#rsa-sha256)\
> [rsa-sha384](http://www.w3.org/2001/04/xmldsig-more#rsa-sha384)\
> [rsa-sha512](http://www.w3.org/2001/04/xmldsig-more#rsa-sha512)\
> [ecdsa-sha1](http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha1)\
> [ecdsa-sha256](http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256)\
> [ecdsa-sha384](http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha384)\
> [ecdsa-sha512](http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512)
>
> [RFC 2898: PKCS #5: Password-Based Cryptography Specification Version 2.0](https://www.rfc-editor.org/info/rfc2898)
>
> [RFC 3394: Advanced Encryption Standard (AES) Key Wrap Algorithm](https://www.rfc-editor.org/info/rfc3394)
>
> [RFC 7518: JSON Web Algorithms (JWA)](https://www.rfc-editor.org/info/rfc7518)
>
> [Federal Information Processing Standard (FIPS) "Security Requirements for Cryptographic Modules"](https://www.nist.gov/publications/security-requirements-cryptographic-modules-includes-change-notices-1232002)

> **Collapse: Other standards**
>
> [REST](https://en.wikipedia.org/wiki/REST)
>
> [Simple Object Access Protocol (SOAP)](http://www.w3.org/TR/soap/)
>
> [Recommendation E.146](https://www.itu.int/rec/T-REC-E.164/en), concerning Mobile Subscriber ISDN Numbers (MSISDN), supported for authentication.
>
> [RFC 2616: Hypertext Transfer Protocol — HTTP/1.1](https://www.rfc-editor.org/info/rfc2616).
>
> [RFC 2617: HTTP Authentication: Basic and Digest Access Authentication](https://www.rfc-editor.org/info/rfc2617), supported for authentication.
>
> [RFC 2865: Remote Authentication Dial In User Service (RADIUS)](https://www.rfc-editor.org/info/rfc2865), supported as an AM service.
>
> [RFC 4510: Lightweight Directory Access Protocol (LDAP)](https://www.rfc-editor.org/info/rfc4510), for authentication and when accessing datastores.
>
> [RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](https://www.rfc-editor.org/info/rfc5280), supported for certificate-based authentication.
>
> [RFC 5646: Tags for Identifying Languages](https://www.rfc-editor.org/info/rfc5646).
>
> [RFC 5785: Defining Well-Known Uniform Resource Identifiers (URIs)](https://www.rfc-editor.org/info/rfc5785).
>
> [RFC 6265: HTTP State Management Mechanism](https://www.rfc-editor.org/info/rfc6265) regarding HTTP Cookies and `Set-Cookie` header fields.
>
> [RFC 7239: Forwarded HTTP Extension](https://www.rfc-editor.org/info/rfc7239).
>
> [Internet-Draft: Password Policy for LDAP Directories](https://datatracker.ietf.org/doc/html/draft-behera-ldap-password-policy-09) (draft 09).
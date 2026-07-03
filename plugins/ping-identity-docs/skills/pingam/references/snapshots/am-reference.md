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

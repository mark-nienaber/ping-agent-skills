---
title: Ping Identity Glossary
description: Glossary for the Ping Identity documentation.
component: glossary
page_id: glossary::index
canonical_url: https://docs.pingidentity.com/glossary/index.html
keywords: ["Ping Identity", "Glossary"]
section_ids:
  a_e: A - E
  f_j: F - J
  k_o: K - O
  p_t: P - T
  u_z: U - Z
---

# Ping Identity Glossary

This glossary contains the definitions for common terms found in the Ping Identity documentation.

## A - E

* access control

  Control to grant or to deny access to a resource.

* access control instruction (ACI)

  An instruction or rule that can be used to grant or deny access to users to perform operations on a server.

* access control rule (ACR)

  An instruction or rule that can be used to grant or deny access to users to perform operations on a server.

* access token

  A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.

* account link

  A persistent name identifier that enables federation of separately established accounts among disparate domains (refer also to account linking and pseudonym).

* account linking

  A form of identity mapping among separate user accounts managed under different domains. The mapping typically involves a name identifier, which can be a pseudonym, to link the user to each account. The identifier is persisted at the SP site to enable seamless SSO/SLO. Additional attributes can be sent with the identifier.

* account lockout

  The act of making an account temporarily or permanently inactive after successive authentication failures.

* account mapping

  A form of identity mapping by which one or more user attributes are passed in an SSO transaction. The attributes are used at the destination site as a means identifying the user and looking up local account information.

* actions

  Defined as part of policies, actions indicate what authorized identities can do to resources.

* Active Directory (AD)

  A directory service for Windows domain networks, included in most Windows Server operation systems.

* adapter

  Plug-in software that allows Ping products to interact with web applications and authentication systems.

* adapter contract

  A list of attributes "hard-wired" to an adapter and conveyed generally through cookies between the adapter and application.

* Advanced Package Tool (APT)

  A software user interface that works with core libraries to install and remove software on several Linux distributions.

* advice

  In the context of a policy decision denying access, a hint to the policy enforcement point about remedial action to take that could result in a decision allowing access.

* agent administrator

  User having privileges only to read and write agent profile configuration information, typically created to delegate agent profile creation to the user installing a web or Java agent.

* agent authenticator

  Entity with read-only access to multiple agent profiles defined in the same realm allows an agent to read web service profiles.

* Amazon Web Services (AWS)

  An Amazon subsidiary providing cloud computing platforms.

* anomaly report

  A report that identifies potential anomalous assignments.

* API Access Management

  In PingOne Authorize, API Access Management addresses the needs of identity and access management (IAM) teams by simplifying common API access control use cases and eliminating the guesswork of OAuth and OpenID Connect (OIDC).

* application

  In general terms, a service exposing protected resources. In the context of PingOne Advanced Identity Cloud policies, the application is a template that constrains the policies that govern access to protected resources. An application can have zero or more policies.

* application programming interface (API)

  A specification of interactions available for building software to access an application or service.

* application type

  Application types act as templates for creating policy applications. Application types also define the internal normalization, indexing logic, and comparator logic for applications.

* artifact

  A reference to a SAML protocol message. The federation partner that receives the artifact dereferences it, identifying the sender, and requests the complete message in a separate SOAP transaction.

* artifact resolution service (ARS)

  The SOAP endpoint that processes artifacts returned from a federation partner to retrieve the referenced XML message. Can be used to dereference authentication requests, assertion responses, and SLO messages.

* as-is predictions

  A process where confidence scores are assigned to the entitlements that users have.

* assertion

  A SAML XML document that contains identifying information about a particular subject; for example, a person, company, application, or system. A SAML assertion can contain authentication, authorization, and attribute information about the subject.

* assertion consumer service (ACS)

  A service provider URL that accepts SAML messages or artifacts to establish a session based on an assertion.

* attribute contract

  A list of attributes, agreed to by the partners in an identity federation, representing information about a user (SAML subject). The attributes are sent from the IdP to the SP during SSO or STS processing.

* attribute mapping

  Matching corresponding attributes between an IdP and an SP to identify federated users or add supplemental user information.

* attribute source

  Specific database or directory location containing data needed by an IdP to fulfill a connection partner's attribute contract or by an SP to look up additional attributes to fulfill an adapter contract.

* attribute-based access control (ABAC)

  Access control based on attributes of a user, such as how old a user is or whether the user is a paying customer.

* attributes

  Distinct characteristics that describe a subject. If the subject is a website user, attributes can include a name, group affiliation, email address, and attributes alike.

* audience

  Part of a SAML assertion indicating the intended SP.

* authentication

  The act of confirming the identity of a principal.

* authentication context

  An element in a SAML assertion indicating the method or process used by an IdP to authenticate the subject of the assertion; can be used for authorization decisions or auditing compliance.

* authentication level

  Positive integers associated with an authentication node used to require success with more stringent authentication measures when requesting resources requiring special protection.

* authentication request

  An OAuth 2.0 authorization request using extension parameters and scopes defined in the OpenID Connect specifications that a relying party (RP, an OAuth client) sends to an OpenID Provider (an OAuth authorization server) for the purpose of authenticating the end user.

* authentication request

  A SAML XML document that an SP sends to an IdP to request that the IdP to authenticate the identity of an end user and to return a response for the request.

* authentication session

  The interval while the user or entity is authenticating to Identity Cloud.

* authentications per second (APS)

  A metric used to measure the total number of authentication workflows processed per second based on a standard benchmark configuration. The total APS can vary depending on the types of authentication methods being used, such as username and password, MFA, or social login, and the triggering mechanisms for these methods.

* authorization

  The act of determining whether to grant or deny a user access to a resource.

* authorization request

  A request based on the OAuth 2.0 Authorization Framework that an OAuth client sends to an authorization server for the purpose of obtaining an access token (for the purpose of ultimately accessing protected resources on a resource server).

* authorization server

  In OAuth 2.0, the authorization server issues access tokens to the client after authenticating a resource owner and confirming that the owner authorizes the client to access the protected resource. PingOne Advanced Identity Cloud can play this role in the OAuth 2.0 authorization framework.

* auto-certify

  An action that an entitlement owner can do to approve a justification. Auto-certify indicates that anyone with the justification is automatically approved for the entitlement.

* auto-federation

  Arrangement to federate a principal's identity automatically based on a common attribute value shared across the principal's profiles at different providers.

* auto-request

  An action that an entitlement owner can do to approve a justification. Auto-request indicates that anyone who matches these justification attributes but might not already have access should automatically get provisioned for this entitlement.

- backchannel

  A direct, cross-domain communication path using a protocol that doesn't rely on a browser as an intermediary.

- benchmark

  A benchmark is a baseline measurement of how a system performs under specific conditions. It is used to compare performance over time and ensure system stability under expected workloads. Performance results are always reported with reference to specific conditions and product configurations used.

- binding

  A mapping of SAML request and response messages to specific transport protocols (redirect, POST, or artifact).

- bottleneck

  A bottleneck occurs when a specific component or resource in the system becomes overloaded and hinders the overall performance, slowing down processing speed or throughput. It represents a point of limitation that reduces the efficiency or scalability of the system. Identifying and addressing bottlenecks is critical for optimizing performance.

* certificate

  A digital file used for identity verification and other security purposes. The certificate, which is often issued by a CA, contains a public key, which can be used to verify the originator's identity.

* certificate authority (CA)

  An entity that issues digital certificates.

* certificate revocation list (CRL)

  A list of revoked signing certificates, maintained by the issuing authority at a public URL.

* certificate signing request (CSR)

  A message sent to a certificate authority in order to apply for a digital identity certificate.

* channel

  A dedicated outbound provisioning configuration specific to a particular service partner, data source, and target service.

* circle of trust

  Group of providers, including at least one identity provider, who have agreed to trust each other to participate in a SAML 2.0 provider federation

* classless inter-domain routing (CIDR)

  A method for allocating IP addresses and for IP routing.

* client

  In OAuth 2.0, the client requests protected web resources on behalf of the resource owner, given the owner's authorization. PingOne Advanced Identity Cloud can play this role in the OAuth 2.0 authorization framework.

* client-initiated backchannel authentication (CIBA)

  An extension to OpenID Connect defining a new OAuth grant type where user consent can be requested and granted through an out-of-band authentication flow. CIBA uses direct relying party to OpenID provider communication without redirects through the user's browser.

* client-side OAuth 2.0 tokens

  After a successful OAuth 2.0 grant flow, PingOne Advanced Identity Cloud returns a token to the client. This differs from server-side OAuth 2.0 tokens, where Advanced Identity Cloud returns a reference to the token to the client.

* client-side sessions

  Sessions for which PingOne Advanced Identity Cloud returns session state to the client after each request and requires the state to be passed in with the subsequent request. For browser-based clients, Advanced Identity Cloud sets a cookie in the browser that contains the session state. When the browser returns the cookie, Advanced Identity Cloud decodes the session state from the cookie.

* closed and open simulations

  Closed simulation: A performance test where the number of concurrent users is fixed, meaning new users only start after previous ones complete their tasks. Open simulation: A performance test where users arrive at a set rate, mimicking real-world traffic where new requests come in continuously.

* Common Event Format (CEF)

  A logging and auditing file format that supports multiple device types.

* concurrency (CC)

  Concurrency is the number of requests being processed at the exact same time. It is not equivalent to the number of users. For example, if 100,000 users log in at 9 AM and 1000 of them send requests at exactly the same time, the concurrency level is 1000.

* conditions

  Defined as part of policies, these determine the circumstances under which a policy applies. Environmental conditions reflect circumstances, such as the client's IP address, time of day, how the subject is authenticated, or the authentication level achieved. Subject conditions reflect characteristics of the subject, such as whether the subject is authenticated, the identity of the subject, or claims in the subject's JSON Web Token (JWT).

* confidence score

  A score on a scale from 0 - 100% that indicates the strength of correlation between an assigned entitlement and a user's data profile.

* configuration datastore

  LDAP directory service holding PingOne Advanced Identity Cloud configuration data.

* connection partner

  Entities, such as companies, that are part of an identity federation.

* credential

  Information used to identify a subject for access purposes (for example, username and password). A credential can also be a certificate.

* cross-domain single sign-on (CDSSO)

  PingOne Advanced Identity Cloud capability allowing SSO across different DNS domains.

* cross-origin resource sharing (CORS)

  A mechanism to allow restricted resources, such as images and scripts, on a web page to be requested from a domain outside of the domain from which the first resource was served.

- data audit

  A pre-analytics process that audits the seven data files to ensure data validity with the client.

- Data Encryption Standard (DES)

  A symmetric-key method of encryption.

- data ingestion

  A pre-analytics process that pushes the seven .csv files into the Cassandra database. This allows the entire training process to be performed from the database.

- data sparsity

  A reference to data that has null values. Identity governance requires dense, high-quality data with very few null values in the user attributes to get accurate analysis scores.

- data validation

  A pre-analytics process that tests the data to ensure that the content is correct and complete prior to the training process.

- database management system

  A system for storing and maintaining user account information and attributes.

- datastore

  A database or directory location containing user account records and associated user attributes.

- defederation

  Optional user-initiated delinking of an identity federation that uses a persistent name identifier or pseudonym for account linking.

- delegation

  Granting users administrative privileges with Identity Cloud.

- digital signature

  A process for verifying the identity of the originator of an electronic document and whether the document has been intercepted or altered. The process involves message signing, signature validation, and signing policy coordination between partners.

- distinguished name (DN)

  A name uniquely identifying an object within the hierarchy of a directory tree.

- driving factor

  An association rule that is a key factor in a high entitlement confidence score. Any rule that exceeds a confidence threshold level (for example, 75%) is considered a driving factor.

- Dynamic Authorization

  In PingOne Authorize, Dynamic Authorization allows application owners and stakeholders to leverage real-time data in fine-grained policies that go beyond identity and roles.

* endpoint

  One end in a communication channel, typically a URI.

* entitlement

  An entitlement is a specialized type of assignment. A user or device with an entitlement gets access rights to specified resources.

* entity ID

  The XML element in a SAML assertion that uniquely identifies an identity provider.

* extended metadata

  Federation configuration information specific to PingOne Advanced Identity Cloud.

* Extensible Access Control Markup Language (XACML)

  Standard, XML-based access control policy language, including a processing model for making authorization decisions based on policies.

* Extensible Markup Language (XML)

  A structured, hierarchical text format, based on SGML, for the flexible and organized exchange of data.

## F - J

* Fast IDentity Online (FIDO)

  A set of open technical specifications developed by the FIDO Alliance for strong authentication.

* federation

  Standardized means for aggregating identities, sharing authentication and authorization data information between trusted providers, and allowing principals to access services across different providers without authenticating repeatedly.

* fully-qualified domain name (FQDN)

  A domain name that specifies its exact location in the DNS tree hierarchy.

- grant type

  The intermediate credentials that represent a resource owner authorization. Grant types are exchanged by the client with the OAuth authorization server in order to obtain an access token.

* hardware security module (HSM)

  A dedicated cryptographic processor designed to manage and protect digital keys. HSMs act as trust anchors that protect the cryptographic key lifecycle by securely managing, processing, and storing cryptographic keys inside a hardened, tamper-resistant device.

* HTTP cookie

  Information sent from a server to a web browser to identify a registered website user. After the cookie is placed in the browser, it is sent back to the server to identify the user every time the user accesses the site.

* HTTP header

  A section of an HTTP request or response that conveys additional information relevant to the client or server in the transaction.

* HTTP request

  A client transaction sent over HTTP to the server specifying a request method, such as GET, POST, and DELETE, to execute against a resource or resources on the server.

- ID token

  A JSON Web Token (JWT) containing an assertion of a user's identity and profile information signed by an OAuth authorization server using JSON Web Signature (JWS) and sent to an OAuth client. The ID token can be encrypted using JSON Web Encryption (JWE). The client receives the ID token after a successful user authentication. The client can extract user information from the token for its purposes.

- identity

  Set of data that uniquely describes a person or a thing, such as a device or an application.

- identity as a service (IDaaS)

  Cloud-based authentication solutions for identity and access management (IAM).

- identity federation

  A trust agreement between or among organizations, implemented using accepted standards, to provide user-authentication tokens and other user or system attributes securely across domains, primarily to enable cross-domain SSO.

- identity provider (IdP)

  A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.

- identity repository

  Datastore holding user profiles and group information.

- IdP-initiated SLO

  An identity federation transaction in which the SLO operation is initiated on the IdP. For example, the user is signed on to the IdP and signs off, triggering an SLO operation on the IdP, which sends the SLO information to the SP.

- IdP-initiated SSO

  An identity federation transaction in which the SSO operation is initiated on the IdP. For example, the user is signed on to the IdP and signs off, triggering an SSO operation on the IdP. The IdP sends the SSO information to the SP.

- inbound

  A direction of message flow coming into a service. The type of message depends service's identity access management role.

- insight report

  A report that provides metrics on the rules and predictions generated in the analytics run.

- Integrated Windows authentication (IWA)

  Internet Information Services (IIS) authentication protocol for authenticated connections between IIS and other Microsoft services.

- Internet Information Services (IIS)

  Extensible web server software designed by Microsoft for use with the Windows N family.

- Internet Protocol (IP)

  The method by which data is sent across the internet from the source host to the destination host.

* Java agent

  Java web application installed in a web container that acts as a policy enforcement point, filtering requests to other applications in the container with policies based on application resource URLs

* Java database connectivity (JDBC)

  A Java API that allows Java programs to interact with databases.

* Java Development Kit (JDK)

  A development environment for building applications and components using Java.

* Java KeyStore (JKS)

  A repository of security certificates and corresponding private keys.

* Java Management Extensions (JMX)

  Java technology that provides tools for managing and monitoring applications, devices, system objects, and service-oriented networks.

* Java Runtime Environment (JRE)

  A software layer that provides the class libraries and resources needed for a Java program to run.

* Java Virtual Machine (JVM)

  A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.

* JavaScript Object Notation (JSON)

  An open, lightweight data-interchange format that uses human-readable text to store and transmit data.

* journey per second (JPS)

  JPS is specific to PingOne Advanced Identity Cloud and measures the number of completed authentication workflows per second. A journey consists of multiple transactions, such as login or password reset flows.

* JSON Web Algorithms (JWA)

  Registers cryptographic algorithms to be used with JSON Web Signature (JWS), JSON Web Encryption (JWE), and JSON Web Key (JWK).

* JSON Web Encryption (JWE)

  A signed and encrypted instance of a JSON Web Token (JWT) based on IETF standard syntax and used for the exchange of encrypted content.

* JSON Web Signature (JWS)

  A signed instance of a JSON Web Token (JWT) based on IETF standard syntax and used for the exchange of signed content.

* JSON Web Token (JWT)

  An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519).

## K - O

* Kerberos

  A network authentication protocol to provide strong authentication for client/server applications using symmetric key cryptography and a trusted authentication service (Key Distribution Center). The KDC authenticates the client and issues tickets allowing access to the server. Kerberos is the default authentication technology used by Microsoft.

* Kerberos ticket

  Issued to an authenticated client to allow access to a server on the network.

* Key Distribution Center (KDC)

  The Kerberos Key Distribution Center (KDC) authenticates the client and issues tickets allowing access to a server on the network.

* key pair

  The private key and public key represented by a certificate.

* key size

  The length in bits for a key used by a cryptographic algorithm..

* Kubernetes

  An open-source system for automating deployment and management of containerized applications.

- latency

  Latency is the time it takes for a transaction to complete after it arrives at the ingress (browser or load generator). This is also known as backend latency. Network latency is the time it takes for a request to reach the ingress. Complete latency is network plus backend latency, but Ping does not control network latency from the client to the ingress.

- LDAP Data Interchange Format (LDIF)

  An IETF standard file format for representing LDAP directory content and modifications to directory content. Typically used to import and export LDAP-based directory information.

- Lightweight Directory Access Protocol (LDAP)

  An open, cross platform protocol used for interacting with directory services.

* magic link

  A passwordless authentication method that involves the authentication service sending a single-use sign on link to the user by email or SMS.

* mean response time (MRT)

  The average response time of multiple transactions over a set period. It helps gauge system efficiency and user experience.

* message authentication code (MAC)

  A generated code that authenticates a message's sender and content.

* metadata

  A summary description of referenced data.

* multi-factor authentication (MFA)

  An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.

- network access server (NAS)

  A server accessible using a point-to-point protocol connection that acts as a gateway between an external network and an internal network. Typically used by Radius clients.

* OAuth

  A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.

* OAuth authorization server (OAuth AS)

  The authorizing service in an OAuth framework that issues and manages access tokens for clients to access protected resources.

* OAuth client

  The application in an OAuth framework that requests access to resources. If the request is approved by the authorization server, the client is issued an access token for the resources.

* one-time passcode (OTP)

  A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.

* Online Certificate Status Protocol (OCSP)

  The protocol used by CAs to check the revocation status of an X.509 certificate.

* opaque

  Not readable. If a user's subject identifier is opaque, an SSO partner cannot directly identify the user with reference to the source. An persistent identifier, or pseudonym, can be used for account linking.

* OpenID Connect (OIDC)

  An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.

* OpenID Provider (OP)

  In OAuth terms, an authorization server (AS). The OP/AS issues access tokens to protected resources for approved clients (relying parties). The clients use the access token to access the protected resources hosted by the OAuth resource server.

* orchestration

  An orchestration platform visually maps user experiences as no code, drag-and-drop visual flows, which help determine how many screens might be needed, the order in which they should appear, and the components required for each experience.

* outbound

  The direction of transaction flow from a service or server.

## P - T

* password credential validator (PCV)

  Configures a centralized location for user credential validation. The validator instances can then be referenced by PingFederate.

* percentiles (PTL)

  Percentiles, such as P95 or P99, indicate the response time threshold for 95% or 99% of requests. For example, a P95 response time of 500 ms means that 95% of transactions were completed within 500 milliseconds. We can report P90, P95, and P99.

* policy

  Set of rules that define who is granted access to a protected resource when, how, and under what conditions.

* Policy Administration Point (PAP)

  Entity that manages and stores policy definitions.

* policy agent

  Java, web, or custom agent that intercepts requests for resources directs principals to PingOne Advanced Identity Cloud for authentication and enforces policy decisions from Advanced Identity Cloud.

* Policy Decision Point (PDP)

  Entity that evaluates access rights and then issues authorization decisions.

* Policy Enforcement Point (PEP)

  Entity that intercepts a request for a resource and then enforces policy decisions from a Policy Decision Point (PDP).

* Policy Information Point (PIP)

  Entity that provides extra information, such as user profile attributes that a Policy Decision Point (PDP) needs in order to make a decision.

* portal

  A web-based application, accessed using a web browser, that often aggregates content from multiple providers, serves as a central point of entry, or both.

* POST

  An HTTP method used to request that the service or server accept the entity enclosed in the request as an addition to the resource identified in the URI.

* primary domain controller (PDC)

  On Microsoft Windows networks, the initial domain controller that maintains the master copy of the directory database and validates users.

* Principal

  Represents an entity that has been authenticated (such as a user, a device, or an application), and thus is distinguished from other entities. When a subject successfully authenticates, PingOne Advanced Identity Cloud associates the subject with the principal.

* private key

  In public key cryptography, a private key is the secret part of an asymmetric key pair that is typically used to digitally sign or decrypt data. The private key is kept secret by its owner, similar to a password.

* privilege

  In the context of delegated administration, a set of administrative tasks that can be performed by specified identities in a given realm.

* protected resource

  Information, typically accessed through a web URL, that is protected by an access management system.

* protocol

  The rules, syntax, semantics, and synchronization of transactions between entities.

* provider federation

  Agreement among providers to participate in a circle of trust.

* pseudonym

  A persistent name identifier assigned to a user and shared among entities, usually with the user's permission, to enable SSO and SLO. Pseudonyms are often used with the SAML account linking protocol to enable SSO while preventing the discovery of the user's identity or activities.

* public key

  In public key cryptography, a public key is the part of an asymmetric key pair that the owner shares with others to allow them to decrypt digital signatures or encrypted data.

* public key infrastructure (PKI)

  Enables users of an unsecured public network to securely and privately exchange data through the use of key pairs and certificates. The PKI provides for a digital certificate that can identify an individual or an organization and directory services that can store and, when necessary, revoke the certificates.

- ramp down

  Ramp down is the process of gradually decreasing the load or number of users after a peak load is reached in a performance test. This allows for the observation of how the system recovers after the load is reduced, helping to understand recovery times and the stability of the system under diminishing traffic.

- ramp rate

  1000 requests per second is the recommended rate for ramping up customer volume for stable autoscaling. It characterizes the system's capacity to accept increasing load and is most valuable during performance testing, where this can be controlled.

- ramp up

  Ramp up refers to the process of gradually increasing the load or number of users in a performance test. This technique helps identify how the system behaves as the demand increases, providing insight into its capacity to handle escalating traffic and ensuring that the system does not crash or degrade unexpectedly as load intensifies.

- realm

  PingOne Advanced Identity Cloud unit for organizing configuration and identity information. Administrators can delegate realm administration. The administrator assigns administrative privileges to users, allowing them to perform administrative tasks within the realm.

- recommendation

  A process run after the as-is predictions that assigns confidence scores to all entitlements and recommends entitlements that users do not currently have. If the confidence score meets a threshold set by the conf\_thresh property in the configuration file, the entitlement will be recommended to the user in the UI console.

- refresh token

  A long-lived token used by OAuth clients to obtain a new access token without having to obtain fresh authorization from the resource owner.

- relying party (RP)

  An OAuth 2.0 client that requires end-user's authenticity and claims (attributes) from an OpenID provider.

- Remote Authentication Dial-In User Service (RADIUS)

  A client/server networking protocol providing centralized user management.

- Representational state transfer (REST)

  A software architecture style for exposing resources using the technologies and protocols of the World Wide Web. REST describes how distributed data objects or resources can be defined and addressed.

- resource

  An external system, database, directory server, or other source of identity data to be managed and audited by an identity management system.

- resource owner

  In OAuth 2.0, a resource owner is an entity that can authorize access to protected web resources, such as an end user.

- resource server

  In OAuth 2.0, a server that hosts protected resources and can accept and respond to resource requests from clients presenting a valid access token.

- response attributes

  Defined as part of policies, Identity Cloud returns additional information as "attributes" with the response to a policy decision.

- response time (RT)

  Response time is the time taken for a single transaction to be processed, as observed by the client.

- REST API

  An API that conforms to the design principles of the representational state transfer (REST) architectural style.

- role-based access control (RBAC)

  Also known as non-discretionary access control, this authorization strategy bases user access on assigned roles.

* SAML authority

  A security domain that issues SAML assertions.

* SAML profiles

  Rules that describe how to embed SAML assertions into and extract them out of other protocols in order to enable SSO or SLO. Profiles describe SAML request and response flows that fulfill specific use cases.

* SAML redirect

  A SAML binding that conveys a request or response by sending the user's browser to another location. For instance, an authentication request can be sent from an SP through a browser to an IdP.

* scope

  In OAuth, a parameter on an access request and resulting, issued access token that specifies a limitation or limitations on access to the protected resource or resources.

* Secure Shell (SSH)

  Protocol for secure operation of network services over an unsecured network.

* Secure Sockets Layer (SSL)

  A protocol for authenticated and encrypted links between networked machines, typically over HTTPS. SSL was deprecated in 1999 in favor of Transport Layer Security (TLS).

* Security Assertion Markup Language (SAML)

  A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.

* security domain

  An application or group of applications that trust a common security token used for authentication, authorization, or session management. The token is issued to a user after the user has authenticated to the security domain.

* security token

  A collection of information used to establish acceptable identity for security purposes. Tokens can be in binary or XML format. A SAML assertion is one kind of security token.

* Security Token Service (STS)

  An entity responsible for responding to WS-Trust requests for validation and issuance of security tokens used for SSO authentication to web services.

* server-side OAuth 2.0 tokens

  An architectural security pattern where sensitive access and refresh tokens are kept entirely on a backend server, rather than being sent to or stored in a client application (such as a web browser or mobile app).

* server-side sessions

  Sessions that reside in the Core Token Service's token store. Server-side sessions might also be cached in memory. Identity Cloud tracks these sessions in order to handle events like logout and timeout, permit session constraints, and notify applications involved in SSO when a session ends.

* service ceiling

  The maximum sustainable level of performance and scalability a cloud service or tenant can achieve under normal operating conditions before encountering diminishing returns, performance degradation, or system constraints. This applies only to PingOne Advanced Identity Cloud. For PingOne Multi-tenant (MT), it is the rate limit before service begins to degrade.

* service provider (SP)

  In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.

* service-oriented architecture

  A loosely coupled application architecture in which all functions or services are accessible using standard protocols. Interfaces are platform and programming-language independent.

* session

  The interval that starts after the user has authenticated and ends when the user signs off or when their session is terminated. For browser-based clients, PingOne Advanced Identity Cloud manages user sessions across one or more applications by setting a session cookie.

* session persistence

  A mechanism for identifying a user or browser for subsequent requests to a server, needed because the HTTP protocol is stateless. This information is used to look up state information for the user. (For example, items in a shopping cart.) A client session is persisted by directing the client to the same backend server or host for the duration of the session.

* session token

  Unique identifier issued by PingOne Advanced Identity Cloud after successful authentication. The session token is used to track a principal's session for server-side sessions.

* Simple Object Access Protocol (SOAP)

  A program and platform-independent messaging protocol for the exchange of structured (XML) information, generally over HTTP. Most often used to invoke web services and process responses.

* simulated think times (TT)

  The delay between user actions in a load test. Real users do not send back-to-back requests instantly; they pause to read, type, or navigate. When high concurrency (in the thousands) is used, think times are essential.

* single logout (SLO)

  The process of signing a user out of multiple sites where the user has started a SSO session.

* single logout return service

  The SAML implementation endpoint URL that returns logout requests.

* single logout service

  The SAML implementation endpoint URL that receives logout requests for processing

* single sign-on (SSO)

  The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.

* single sign-on service

  A service that implements SSO. In SAML, this is an endpoint that receives and processes authentication requests.

* Software Development Kit (SDK)

  A set of tools that allows a developer to build a custom application that integrates with or connects to a platform or service.

* source ID

  A 20-byte sequence used to determine an IdP's identity.

* SP-initiated SLO

  In SAML, an identity-federation transaction in which the initial action for single logout (SLO) occurs at a the service provider (SP) site.

* SP-initiated SSO

  In SAML, an identity federation transaction in which the initial action for SSO occurs at the SP site.

* standard metadata

  Standard federation configuration information that you can share with other access management software.

* stateless service

  Stateless services do not store any data locally to the service. When the service requires data to perform any action, it requests it from a data store. For example, a stateless authentication service stores session state for signed-on users in a database. This way, any server in the deployment can recover the session from the database and service requests for any user. All PingOne Advanced Identity Cloud services are stateless unless otherwise specified.

* stemming

  A process that occurs after training that removes similar association rules that exist in a parent-child relationship. If the child meets three criteria, the system will remove it. The criteria are: 1) the child must match the parent; 2) the child (for example, \[San Jose, Finance]) is a superset of the parent rule (for example, \[Finance]); 3) the child and parent's confidence scores are within a +/- range of each other. The range is set in the configuration file.

* subject ({p1aic})

  Entity that requests access to a resource. When an identity successfully authenticates, Advanced Identity Cloud associates the identity with the principal that distinguishes it from other identities. An identity can be associated with multiple principals.

* subject (SAML)

  A person, computer system, or application. In the SAML context, assertions make statements about subjects.

* System for Cross-domain Identity Management (SCIM)

  An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.

- target URL

  In SAML, the destination on an SP to SSO events.

- throughput

  The total number of successful transactions processed per second, per minute, or over a fixed interval of time.

- Time-based One-Time Password (TOTP)

  A temporary passcode generated by an algorithm that uses the current time of day as one of its authentication factors. Typically, an app or hardware token generates a 6-digit passcode that is valid for less than 1 minute.

- token authorization

  A mechanism for evaluating attribute criteria available during a transaction to determine whether a user is authorized to access resources. A token in this instance can mean any type of security token, such as SSO, session cookie, or OAuth token.

- token exchange

  The process by which a security token is exchanged for another security token.

- token translators

  An aggregate term for both token processors and token generators.

- training

  A multi-step process that generates the association rules with confidence scores for each entitlement. First, Identity Governance models the frequent itemsets that appear in the user attributes for each user. Next, Identity Governance merges the user attributes with the entitlements that were assigned to the user. It then applies association rules to model the sets of user attributes that result in entitlement access and calculates confidence scores based on their frequency of appearances in the dataset.

- transactions per second (TPS)

  TPS measures the number of transactions processed per second. A transaction is a combination of requests that results in a workflow.

- transient name identifier

  A temporary ID used to preserve user anonymity while facilitating account linking.

## U - Z

* Uniform Resource Identifier (URI)

  Identifies a web resource with a string of characters conforming to a specified format.

* Uniform Resource Locator (URL)

  Identifies a resource according to its internet location.

* Universal 2nd Factor (U2F)

  Open standard for two-factor authentication using USB devices.

- virtual server ID

  An optional unique identifier by which an identity federation deployment can be known to a specific connection partner.

* web agent

  Native library installed in a web server that acts as a policy enforcement point with policies based on web page URLs.

* web service client (WSC)

  An entity that requests a web service interaction. In the context of a security token service (STS), the web service client would request that a security token be issued for the interaction.

* web service provider (WSP)

  In the context of a security token service (STS), an entity that requests validation of the security token sent with a client's request for service.

* web services

  A program and platform-independent collection of open protocols and standards available through the internet and used for exchanging data between applications or devices.

* Web Services Enhancement (WSE)

  Supplemental software for the .NET framework provided by Microsoft. (Now obsolete.)

* Web Services Security (WS-Security)

  A standard mechanism for securing web service interactions, often by binding a security token to the web service request.

* webhook

  An HTTP-based callback function that allows lightweight, event-driven communication between two APIs.

* workflow

  A workflow is a structured process that defines how a system handles multiple user interactions, such as authentication and authorization, risk assessment, MFA, and verification in, for example, PingOne DaVinci flows and PingOne Advanced Identity Cloud journeys.

* WS-Federation

  Part of the WS-Security framework and an extension of WS-Trust, it defines mechanisms allowing different security realms to broker information on identities, identity attributes, and authentication.

* WS-SX

  The OASIS committee working on WS-Trust.

* WS-Trust

  A standard protocol by which an application can request that a security token service (STS) issue, validate, or exchange security tokens.

- X.509 Attribute Sharing Profile (XASP)

  Defines a specialized extension of the general attribute query profile and enables organizations with an investment in PKI (Public Key Infrastructure) to issue and receive attribute queries based on user-certificate authentication.

* Zero Trust

  A security framework requiring all users, whether in or outside the organization's network, to be authenticated, authorized, and continuously validated for security configuration and posture before being granted or keeping access to applications and data.

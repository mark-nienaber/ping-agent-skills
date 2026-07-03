---
title: Application Integration Guide
description: This guide will walk the developer through the steps to enable standards-based Single Sign-On (SSO) to an application by integrating the application with the Ping platform.
component: developer-resources
page_id: developer-resources:application_integration_guide:index
canonical_url: https://docs.pingidentity.com/developer-resources/application_integration_guide/index.html
revdate: May 3, 2021
page_aliases: ["dev_app_int_overview.adoc"]
---

# Application Integration Guide

This guide will walk the developer through the steps to enable standards-based Single Sign-On (SSO) to an application by integrating the application with the Ping platform.

Using the concept of "Integrate, Federate and Operate" we can describe the steps an application owner must complete to provide and manage federated SSO in their application:

* Integrate involves making the application federation-aware so that it can accept a federated security token and use the information in that token to authorize a user and create an application session.

* Federate consists of creating federated connections with partners (primarily exchanging metadata).

* Operate describes the management of these connections, adding new customers, managing connections at scale.

This guide will focus on the integrate step.

---

---
title: Integrating APIs and Web Services
description: APIs and Web Services are the heart of applications and system development. They enable us to re-use tried and trusted code across multiple applications and application formats and providing access for partners into internal systems.
component: developer-resources
page_id: developer-resources:application_integration_guide:integrating-apis-web-services
canonical_url: https://docs.pingidentity.com/developer-resources/application_integration_guide/integrating-apis-web-services.html
revdate: September 30, 2020
section_ids:
  rest-apis: Rest APIs
  soap-web-services: SOAP Web Services
---

# Integrating APIs and Web Services

APIs and Web Services are the heart of applications and system development. They enable us to re-use tried and trusted code across multiple applications and application formats and providing access for partners into internal systems.

APIs and web services are now a common method of accessing and exposing an application's functionality and therefore a critical interface to secure.

## Rest APIs

REST-based services use HTTP verbs and JSON to communicate actions. As an example, an API may represent a "product". The following REST API calls may be performed:

* GET <https://api.company.com/product> - get all products

* GET <https://api.company.com/product/{product_id}> - get a specific product

* POST <https://api.company.com/product> - create a new product

Because they use the HTTP protocol, authentication is usually performed via HTTP headers using the authorization header. The most common protocol used to authorize access to REST APIs is the OAuth 2.0 protocol.

![REST API overview](_images/vbn1601508114610.png)

## SOAP Web Services

SOAP-based services are XML based and come with a standard security mechanism (WS-Security protocol). This allows for a security element to be presented as part of a SOAP web services call. There are multiple profiles that define these standards (i.e. the username profile which uses a username and password security token or the x509 profile that uses a certificate as a security token) as an authentication token.

The WS-Trust standard introduces the concept of a Security Token Service (STS) that the web services client and the web services provider can lverage to broker the authentication. In the WS-Trust model, a security token (i.e. a SAML assertion) is issued by the STS for the web service client. This token is passed to the web services provider during the service call. The provider will validate this token against the STS and if valid, allow access to the web services call.

![API SOAP overview](_images/qjy1601508115746.png)

---

---
title: Integrating Mobile Applications
description: Mobile apps are an increasingly common format for application developers. A mobile app is generally a simple, concise rendering of an application with all the functionality packed into a small easy-to-use application available on a users phone or tablet.
component: developer-resources
page_id: developer-resources:application_integration_guide:integrating-mobile-applications
canonical_url: https://docs.pingidentity.com/developer-resources/application_integration_guide/integrating-mobile-applications.html
revdate: September 30, 2020
section_ids:
  anatomy-of-a-mobile-application: Anatomy of a Mobile Application
  authentication-and-single-sign-on: Authentication and Single Sign-on
  user-profile: User Profile
  authorization-and-access-control: Authorization and Access Control
  session-management: Session Management
---

# Integrating Mobile Applications

Mobile apps are an increasingly common format for application developers. A mobile app is generally a simple, concise rendering of an application with all the functionality packed into a small easy-to-use application available on a users phone or tablet.

This section will identify a typical mobile application architecture and walk through integrating a mobile app with the federation infrastructure.

## Anatomy of a Mobile Application

The mobile app architecture generally differs from a traditional web app architecture in that the mobile app is more distributed. Where a web app is more monolithic in design with complexity suiting a larger screen format with a user present, a web app is generally a more distributed model with a simple client that performs actions against an API on behalf of a user - whether the user may or may not be present.

A mobile application requires a new model of managing authentication and security due to the app architecture and fundamental differences between it and a traditional web app:

* Traditional web app is monolithic, components can talk to all other components. A mobile app consists of a client communicating to APIs.

* Web application user is generally always present. Mobile app user may be present or may allow the app to function in the background.

* Web application allows for a more complex UX due to screen size and device. Mobile app generally simplified UX targeted to a touch device.

![Web and mobile architecture](_images/jhw1601508108400.png)

Device capabilities and restrictions also factor into an app design, specifically around security:

* A mobile device is smaller, therefore easier to lose or be stolen so sensitive data (including stored passwords) needs to be secured on the device or not stored in the first place.

* The prevalence of BYOD sees enterprise applications alongside personal applications, leading to less secure entry mechanisms to the device (ie no unlock PIN on the device).

* Ability to work in a disconnected mode (i.e. airplane mode) and attention to user experience results in cached data and credentials.

* Applications are sandboxed on devices making it difficult to interact with other applications and share credentials and sessions.

* Mobile frameworks generally have limited functionality exposed through SDKs (i.e. lack of SAML framework for mobile developers)

Although a different architecture, the same fundamental challenges remain: to eliminate passwords and reduce the authentication complexity from the app developer.

As the mobile app architecture generally involves both the app client and a resource or API that the app is communicating with, mobile app security involves securing both sides. Authentication to the app client (for user identification, personalisation, access to stored data etc) and securing of the API calls to the backend services.

![Web and mobile authentication](_images/zfi1601508109139.png)

Like web application SSO, eliminating passwords and replacing with a standards-based security token the application developer can offload the authentication complexity from the application to the authentication provider. The results are a flexible token model that the application can use to be assured of the identity of the user authenticating and can use to authorize access to backend APIs (without storing or transferring passwords).

![Mobile federated authentication](_images/mac1601508109906.png)

Authentication to mobile applications is also greatly affected by user experience requirements. Better application user experience may be to authenticate a user natively in the application or via a web view in the application, however would limit the authentication flexibility provided when the user is redirected to the mobile browser for authentication (additional authentication functionality such as certificate authentication and a reusable authentication provider session to facilitate SSO across applications).

The prevailing standards for securing mobile applications are OpenID Connect and OAuth 2.0. These complementary protocols allow and application to authenticate a user, retrieve profile information about that user and identify that user to APIs that it calls on the users behalf.

In the OpenID Connect / OAuth 2.0 flow, a mobile app (client) will redirect the user to the Authorization Server for authentication the result of this will be two tokens returned to the client app, an id\_token containing information about the user's authentication event and an access\_token which the client can use as authorization to protected APIs.

The client will then validate those tokens and, if valid, consider the user authenticated. If additional profile information is required, the client can call the UserInfo endpoint on the AS to retrieve additional information about the authenticated user.

![Mobile OIDC flow](_images/omg1601508110665.png)

## Authentication and Single Sign-on

To leverage OpenID Connect for authentication to a mobile application, the app will need to implement a few simple items:

* An action to redirect the user through the authentication process

* A callback URI that receives the authentication tokens

* A process to validate the received tokens

* A process to retrieve the user profile information (optional)NOTE: Due to challenges with keeping a mobile application's client\_secret a secret (i.e. app distribution through the app store, re-issuance of an application if the secret were to be compromised) a mobile application should use the Proof Key for Code Exchange (PKCE) extension with an OpenID Connect basic profile flow.

There are a number of OAuth 2.0 and OpenID Connect libraries and frameworks available via open source which can simplify the implementation even further.

OpenID Connect and OAuth 2.0 can provide secure single sign-on to your mobile applications and the APIs that those applications rely on. By removing passwords from the equation, apps are more secure. By reducing the authentication complexity, developers can focus on building the application rather than the authentication model.

User experience requirements may dictate that the user remain in the application and not redirected to a web flow. In this case, the OAuth 2.0 Resource Owner Password Credentials flows can be used to exchange the user's username / password for OAuth access tokens. As the flow requires a username and password for authentication, this limits the opportunity to handle federated partners.

## User Profile

OpenID Connect publishes an endpoint on the authorization server called the UserInfo endpoint. An application can make a REST call to this endpoint authenticating with the OAuth 2.0 access token assigned to the user. This call will return the user's profile information.

## Authorization and Access Control

Generally authorization for native mobile apps is enforced at the back-end API. After a user authenticates, the application will call a back-end API with the OAuth 2.0 access token. If the token has expired, is not valid or the authorizations provided in the access token are not sufficient for the request, then the API call will fail. The application should handle these failures gracefully.

The application itself may also enforce access control based on the attributes returned in the user profile. For example and enterprise application may only be available for user's in the finance department. If an enterprise user from marketing launches the mobile app, they may be denied access because of their user profile attributes.

## Session Management

A mobile application doesn't have a session as we expect from a web application. Typically the application session is managed by the lifetime of the OAuth 2.0 access token. While the token is valid the user can make API requests and interact with the application. When the access token expires the API calls will fail and the user will need to retrieve a new token to make the API calls.

OAuth 2.0 includes a concept of refresh tokens that can be exchanged for a new access token without requiring the end user to re-authenticate. This can be useful for "offline access" scenarios where the application may want to make a call while the user is not present in the application (i.e. check an order status while the application is running in the background). If a user loses their device, then these refresh tokens should be invalidated so that the application is not available to unauthorized users.

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | A refresh token is not available in every OAuth 2.0 grant type (i.e. Implicit) |

---

---
title: Integrating Web Applications
description: Our first scenario involves analyzing a web application to determine the changes required to make the application behave in a federated model. We will first identify what a typical web application looks like and how it will look after it has been integrated. Then we will use the information we gained in the previous section and walk through the process needed to integrate a web application.
component: developer-resources
page_id: developer-resources:application_integration_guide:integrating-web-applications
canonical_url: https://docs.pingidentity.com/developer-resources/application_integration_guide/integrating-web-applications.html
revdate: September 30, 2020
section_ids:
  authentication-and-single-sign-on: Authentication and Single Sign-On
  user-profile: User Profile
  authorization-and-access-control: Authorization and Access Control
  session-management: Session Management
---

# Integrating Web Applications

Our first scenario involves analyzing a web application to determine the changes required to make the application behave in a federated model. We will first identify what a typical web application looks like and how it will look after it has been integrated. Then we will use the information we gained in the previous section and walk through the process needed to integrate a web application.

A user via their web browser access the application, when they visit a protected page the application wil prompt them for authentication. In a non-federated model this is typically an application login form where the user enters their username and password. The application will then validate these credentials against the user authentication store (an internal data store or maybe a networked directory). If the credentials are valid and the authenticated user is authorized to access the protected content, the user is provided an authenticated session and is allowed to continue.

![Authentication schematic](_images/xsy1601508102686.png)

The goal of application integration for a web application is to move the authentication flow to a federated browser SSO model. As we know with the browser SSO model, the authentication event is offloaded to the identity provider and replaced with a mechanism to validate the authentication token returned via the authentication process. When a user accesses protected content, the application will redirect the users browser to the federated sign-in process. The user authenticates at the identity provider, a security token is issued and provided to the service provider who creates a session in the application.

As we learned in the previous section, there are four items we will evaluate:

* Authentication Event(s)

* User Profile

* Authorization Event(s)

* Session Management

## Authentication and Single Sign-On

The sign-on process may contain more than one location where a visitor can authenticate; the "front door", at an approval stage, if there are any APIs exposed by the application etc. It is important to identify the events in the application that require authentication and what authentication requirements each event has (ie an approval process may require a step-up to a stronger form of authentication such as a second factor).

Focusing on the "front-door" authentication, a general web application sign-on process will go through a simple workflow:

![Traditional web authentication flow](_images/blz1601508104249.png)

To change this workflow to support a federated authentication model, when an unauthenticated user appears the application will redirect the users browser to the SSO process. This will result in the user being challenged for authentication at the identity provider and (after a successful authentication) a token returned to the application sign-on process.

The sign-in process is now expecting three user states:

1. A known user already has an application session (if the user is authorized, the requested page will be rendered)

2. An unknown user is arriving with a federated security token (where the application will validate that token and if valid, create an application session - the user will then be in state #1)

3. An unknown user is arriving without a token (the application will redirect the user to the federated sign-in process - the user will re-appear to the application as state #2)

![Federated web authentication flow](_images/ixp1601508104988.png)

The results of the authentication request are a token containing proof of authentication and the additional attributes required by the application. The application can use these attributes to create the application session and personalize the application for the user.

## User Profile

More than likely, an application requires more information about the user during authentication (i.e. a list of groups to use for authorization decisions or the user's preferred language to personalize the application) these additional attributes can be provided by the authentication provider during the authentication event or through an out-of-band process (i.e. federated provisioning (SCIM) or via an API call like the OpenID Connect UserInfo API).

An application may have an application data store that contains application-specific information about the incoming user. For some applications the only information the application needs from the authentication provider is the username. It can then map that user to their application profile to associate the user with their application profile and authorizations.

## Authorization and Access Control

Once we have an authenticated user (and their user profile), the next event is the authorization and access control stage. The application can use the attributes defined in the user profile (whether that information was received during the authentication or was provided in an alternate method) to make authorization decisions and determine theÂ appropriate level of access to the user.

## Session Management

The authentication process is generally a one-time event. So when the application receives the authentication token and signs that user in, the application will generally create an application session. Once that session expires it will send the user through the sign-in process again to reauthenticate. This process may be aligned with the authentication provider to provide a seamless session extension - if the application session is shorter than the authentication provider session, then the user will automatically be logged back into the application when the session expires. Products such as PingAccess provide session management out of the box.

Terminating the session can be achieved via single log out or by just killing the application session and redirecting the user / instructing them to close their browser. Single log-out is supported across federation protocols however can be trickly to implement due to differing authentication methods provided by authentication providers. It is best to provide options to the federation partner on how to handle the sign-out event. Generally asking the partner to supply a log-out URL during configuration would be sufficient, then the application can log the user out of the application, then redirect to the URL specified by the partner.

---

---
title: Planning
description: At a high level, there are four items that we will focus on in this guide for the integration stage:
component: developer-resources
page_id: developer-resources:application_integration_guide:planning
canonical_url: https://docs.pingidentity.com/developer-resources/application_integration_guide/planning.html
revdate: September 30, 2020
section_ids:
  application-considerations: Application Considerations
  selecting-an-integration-method: Selecting an Integration Method
---

# Planning

At a high level, there are four items that we will focus on in this guide for the integration stage:

* Authentication - How a user is authenticated and their identity validated

* User Profile - How the user's identity attributes are provided

* Authorization & Access Control - How an application can enforce authorization decisions based on the security token

* Session Management - How to start, end, revoke and refresh a users session

There are a number of additional considerations that should also be taken into account (for example federated user provisioning) however, this guide will focus on the SSO activity.

## Application Considerations

Knowing that to provide SSO to my customers, employees and partners I need to integrate my application into the federation infrastructure; the first question that is asked is "How do I integrate my application?". There are a number of mechanisms that can be used for this "last-mile" integrate, so to plan for application integration a number of components should be considered:

* Application Format

  The format of the application. Whether it is a web application, a mobile application or an API or web service.

* Application Platform

  The application platform can help determine the simplest integration method. The platform includes the language and framework the application is written in (i.e. Java / Spring or .NET 4.5) as well as the web application server the application is hosted on (i.e. Apache or IIS).

* Application Deployment Model

  Whether the application is cloud-hosted or deployed inside the firewall can also help determine the simplest integration method. For example PingOne provides a simple REST interface to enable SSO into a cloud-hosted application whereas PingFederate is a a software component but enables more options for complex integrations.

* API Requirements

  If the application needs to talk to specific API's it may be simpler to define the authentication mechanism around those services (i.e. if the application requires user authentication and accesses OAuth 2.0 protected REST web services, then OpenID Connect protocol is a good choice).

* Availability of Source Code

  There may be applications where the source code is not available (i.e. COTS application) or that the source code is not supported. Perhaps a mechanism that doesn't require code changes is the most appropriate.

## Selecting an Integration Method

With the information gathered in the previous stage, we can narrow down our integration options to determine if we need to make code changes to support the integration. The next sections will detail the specifics for integrating the different application formats, however the following general steps should be considered for all application formats before opening up the code in the application:

* Leverage SSO support provided by infrastructure or framework - The goal is to leverage an open standard to provide maximum security and interoperability between partners, vendors and customers. Once the application can speak an open standard, then managing connections can be made via configuration rather than code. For example, if a web application can accept a SAML assertion to sign a user in, then using PingOne or PingFederate multiple partners (i.e. enterprises via SAML, social networks via OpenID Connect etc) can be connected and presented to the application through that SAML connection.

* Leverage an access gateway (i.e. PingAccess) to handle the authentication - PingAccess can be used to protect web applications and APIs by handling the protocol work and presenting the user attributes to the application or API via HTTP headers or cookies. If the application or API can be protected behind an access gateway like PingAccess the work of integrating an application can be greatly simplified and the benefits of administration of authentication and authorization policies can be easily implemented.

* Leverage the federation engine (i.e. PingFederate) to handle token translation - PingFederate is highly skilled at exchanging tokens in a standard and interoperable manner. Scenarios such as protocol transition (i.e. providing SAML SSO to an application that is configured to use the WS-Federation protocol) can easily be achieved. Rather than re-writing the authentication logic, the PingFederate protocol engine can perform all the work. The same is true for applications that have API requirements. Although a cleaner solution maybe be to use OpenID Connect and OAuth 2.0 for a web application that calls OAuth protected API's, a simpler and quicker solution may be to retain a SAML authentication model and provide an OAuth access token as an attribute of the assertion or exchange the assertion for an OAuth access token.

* Finally, integration via code. Either implementing open standards support in the application directly or using an integration kit to simplify the integration of standards into the application.

---

---
title: Selecting an Integration Method for APIs and Web Services
description: As we learned with web and mobile applications, federating API and web services security can greatly increase the flexibility of the APIs and services. By federating, you are replacing username/passwords with tokens allowing an external authentication system to handle the authentication complexity. This in turn allows APIs and services to use that token to authorise access to resources rather than manage the authentication process themselves.
component: developer-resources
page_id: developer-resources:application_integration_guide:select-integration-api-web
canonical_url: https://docs.pingidentity.com/developer-resources/application_integration_guide/select-integration-api-web.html
revdate: September 30, 2020
section_ids:
  rest-apis: REST APIs
  soap-services: SOAP Services
---

# Selecting an Integration Method for APIs and Web Services

As we learned with web and mobile applications, federating API and web services security can greatly increase the flexibility of the APIs and services. By federating, you are replacing username/passwords with tokens allowing an external authentication system to handle the authentication complexity. This in turn allows APIs and services to use that token to authorise access to resources rather than manage the authentication process themselves.

## REST APIs

REST-based web services and APIs can leverage OAuth 2.0 for API protection. In the OAuth 2.0 terminology, the API will act as the Resource Server (RS). As a request is made to the API, an OAuth access\_token will be presented as a bearer token in the "authorization" HTTP header. The API will validate this token and use the attributes provided in the token to authorize access to the API.

![API OAUTH flow](_images/wkv1601508117322.png)

## SOAP Services

SOAP services protected by WS-Security / WS-Trust standards leverage a Security Token Service (STS) to broker the federation transaction. The STS can exchange WS-Security tokens for federated security tokens (i.e. a SAML assertion) to provide cross-domain, federated access to your web services.NOTE: A SOAP web service call is essentiall a HTTP call, therefore a SOAP service can still take advantage of OAuth 2.0 to protect the call. The security will be processed and if the call is authorised, the SOAP message can be processed by the web service provider.

![API WST overview](_images/our1601508118571.png)

---

---
title: Selecting an Integration Method for Mobile Apps
description: Mobile application integration is fairly straightforward with the OAuth 2.0 and OpenID Connect 1.0 protocols. Achieving single sign-on across applications has proven to be the challenging piece.
component: developer-resources
page_id: developer-resources:application_integration_guide:select-integration-mobile
canonical_url: https://docs.pingidentity.com/developer-resources/application_integration_guide/select-integration-mobile.html
revdate: September 30, 2020
---

# Selecting an Integration Method for Mobile Apps

Mobile application integration is fairly straightforward with the OAuth 2.0 and OpenID Connect 1.0 protocols. Achieving single sign-on across applications has proven to be the challenging piece.

For more information about leveraging the mobile OS to facilitate single sign-on, refer to the Native Application SSO (NAPPS) Developers Guide.

---

---
title: Selecting an Integration Method for Web Apps
description: The following question can help narrow down the integration options available for web applications. You can learn more about the integration methods in the Explore section of this website.
component: developer-resources
page_id: developer-resources:application_integration_guide:select-integration-web-apps
canonical_url: https://docs.pingidentity.com/developer-resources/application_integration_guide/select-integration-web-apps.html
revdate: September 30, 2020
---

# Selecting an Integration Method for Web Apps

The following question can help narrow down the integration options available for web applications. You can learn more about the integration methods in the Explore section of this website.

This flowchart assumes that:

* the application will be integrated directly with the federation infrastructure instead of using an access gateway like PingAccess

* the source code for the web application is available (if not, PingAccess may be able to support this scenario)

| Integration Option                                       | Scenario                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Integrate directly with application / platform           | Application supports a federated security protocol such as SAML or WS-Federation (for example Microsoft SharePoint or Microsoft .NET) PingFederate and PingOne can be used to manage federation connection to partners.                                                                                                                                                            |
| PingFederate Web Server Integration Kits                 | If the application server is IIS or Apache.                                                                                                                                                                                                                                                                                                                                        |
| PingFederate Language Integration Kits (Java, .NET, PHP) | Application is either Java, .NET or PHP. Especially if there is no direct communication between PingFederate and the application.                                                                                                                                                                                                                                                  |
| PingFederate Agentless Integration Kit                   | Any code-based language that can make HTTP calls. *Note: This kit requires direct connectivity between the application and PingFederate.*                                                                                                                                                                                                                                          |
| PingOne Application Provider Services                    | Application is cloud-based or there are requirements that no software or libraries are to be used.                                                                                                                                                                                                                                                                                 |
| Native protocol support                                  | Application requires authentication and API authorization. OpenID Connect can be used to authenticate a user to an application client as well as provide an OAuth 2.0 access token use to secure API requests. *Note: PingFederate can perform token translation allowing one token to be exchanged for another (i.e. a SAML assertion to be exchanged for an OAuth access token)* |

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In all cases, the Agentless Integration Kit and PingOne APS can be used to integrate an application with the Ping infrastructure quickly and simply. |
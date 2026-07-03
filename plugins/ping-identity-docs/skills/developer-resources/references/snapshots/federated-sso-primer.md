---
title: A Single, Sign-on Process
description: Prior to diving into SSO, lets re-visit the general process a user follows to login to a traditional application:
component: developer-resources
page_id: developer-resources:federated_sso_primer:single-sign-on-process
canonical_url: https://docs.pingidentity.com/developer-resources/federated_sso_primer/single-sign-on-process.html
revdate: September 30, 2020
section_ids:
  authentication: Authentication
  user-profile: User Profile
  authorization-and-access-control: Authorization and Access Control
  session-management: Session Management
---

# A Single, Sign-on Process

Prior to diving into SSO, lets re-visit the general process a user follows to login to a traditional application:

## Authentication

The authentication step is used to determine the identity of the user accessing the application or service. By challenging them with a action (i.e. entering a username and password) that only that person will be able to successfully complete, the application can be reasonably comfortable that the user accessing the system is who they say they are.

In the application world, the most common form of authentication request is the login screen asking for a username and password. These credentials will be validated against a data store and, if valid, the user will be successfully authenticated.

The result of the authentication process is that we now know who is attempting to access our application or service.

## User Profile

Prior to the authorization process the application generally wants to know more information about the user logging in to use in authorization decisions (and in some cases, also for personalization of the application).

The attributes required for authorization and application functionality can be handled in different ways:

* Application stores the attributes in its local store

* Application can store the attributes in a remote store

* Attributes can be provided along with the authentication request

After the application has received the information that it needs about the user (i.e. groups / roles) we can continue to the next step.

## Authorization and Access Control

Access control rules can be defined by both the organization and the application. As a user accesses an application (or part of an application), the application will check to see if they are authorized to access that page or to perform the action. If the user requesting access meets the requirements of the access rules, they will be authorized access to the page or action. An example of authorization includes validating whether a user exists in a particular group before allowing them access.

## Session Management

Once a user has been identified, their attributes retrieved and they are authorized to access the application, the final step the application makes is to create a session inside the application. From there the user can interact with the application without being prompted for authentication again (until the session expires or they log off).

After these steps are complete, the application knows who the user is, has allowed them access and has provided them a session so they may use the application without being prompted for authentication at every request.

---

---
title: Achieving Single Sign-on
description: For SSO to be achieved, this process needs to be repeated for each application accessed by the user. Various mechanisms can be used to reduce or eliminate the burden of logging in to each application, such as:
component: developer-resources
page_id: developer-resources:federated_sso_primer:achieving-sso
canonical_url: https://docs.pingidentity.com/developer-resources/federated_sso_primer/achieving-sso.html
revdate: September 30, 2020
---

# Achieving Single Sign-on

For SSO to be achieved, this process needs to be repeated for each application accessed by the user. Various mechanisms can be used to reduce or eliminate the burden of logging in to each application, such as:

* Using a centralised authentication store for all applications (i.e. leveraging LDAP and Active Directory for authentication) - the user will have the same username and password for each application however will be expected to log in to each application.

* Using a domain trust to establish SSO - this could involve using a protocol like Kerberos to achieve single-sign on when the user is on the corporate network.

* Leveraging a Web Access Management (WAM) solution where all applications are protected by an access gateway, the user logs in once to the WAM gateway and gains access to all applications they are entitled to.

* Leveraging a shared cookie or token across multiple applications.

* Vaulting passwords and replaying them as a user access an application.

We see that to achieve the end goal of SSO between applications, we must replace the password with a trusted token (i.e. a kerberos ticket or a cookie) or system (i.e. a WAM).

---

---
title: Browser SSO Flow
component: developer-resources
page_id: developer-resources:federated_sso_primer:browser-sso-flow
canonical_url: https://docs.pingidentity.com/developer-resources/federated_sso_primer/browser-sso-flow.html
revdate: September 30, 2020
---

# Browser SSO Flow

![Browser SSO](_images/jxj1601508127380.png)

---

---
title: Extending Single Sign-on to the Cloud
description: "A new challenge arrives when the requirement for cross-domain authentication is introduced \"browser SSO\" where the user authenticating is no longer in the same domain as the application. A few examples of where this occurs are:"
component: developer-resources
page_id: developer-resources:federated_sso_primer:extend-sso-cloud
canonical_url: https://docs.pingidentity.com/developer-resources/federated_sso_primer/extend-sso-cloud.html
revdate: September 30, 2020
---

# Extending Single Sign-on to the Cloud

A new challenge arrives when the requirement for cross-domain authentication is introduced "browser SSO" where the user authenticating is no longer in the same domain as the application. A few examples of where this occurs are:

* User wants to access an enterprise application from their home PC or the coffee shop

* Enterprise user accesses a SaaS application and wants to sign on with their enterprise credentials

* Consumer-facing site wants to single sign-on the user to another web asset (either another web application or a 3rd party website)

SSO protocols such as Kerberos rely on the user being located inside a trusted environment and being able to contact authoritative authentication servers (i.e. an Active Directory Domain Controller) so how to support single sign-on across multiple applications located in different security domains. Vaulting passwords is clearly not a secure cross-domain solution as there is still a password stored in the third-party application, meaning when the authentication provider disables a user or changes their password, this is not reflected in the third party application.

Federated sign-on provides a portable trust between an authentication provider and a service provider. When a user from an organization requests authentication to a service provider they will be redirected to their home organization for authentication and, if successful, will be redirected back to the application with a token confirming the authentication.

As the user accesses additional applications, the process is repeated. By retaining a session at the authentication provider an organization can achieve SSO across multiple domains and applications.

For web applications, federated single sign-on uses the web browser to allow the user to interact with both the application and the authentication provider to negotiate authentication. As this "browser SSO" process uses the web browser, all communication is between the end-user and the federation partner (ie between the user and the authentication provider or the user and the application provider) this means that there is no communication direct between the authentication provider and the application provider, no firewall rules, no VPN and reduced risk to an enterprise.

---

---
title: Federated SSO Primer
description: The goal of single sign-on is simple. Remove the need for users to remember a number of passwords to login to their applications.
component: developer-resources
page_id: developer-resources:federated_sso_primer:index
canonical_url: https://docs.pingidentity.com/developer-resources/federated_sso_primer/index.html
revdate: May 3, 2021
page_aliases: ["dev_fed_sso_overview.adoc"]
---

# Federated SSO Primer

The goal of single sign-on is simple. Remove the need for users to remember a number of passwords to login to their applications.

For an application developer, [SSO](https://www.pingidentity.com/en/platform/single-sign-on.html) can enable:

* A web application wanting to log users in across multiple web assets without re-prompting them to login

* A user being able to log in to all their applications (on-prem and SaaS) by only typing their password once (or maybe not at all)

* Removing passwords from applications; reducing risk and aligning SaaS applications with organizational IAM policies

This guide will walk you through the concepts and considerations of authentication, Single Sign-On (SSO) through to federated SSO. Learn what "Federation" means and why open standard federation protocols enable cross-domain identity propagation.

In the following sections, we will provide a background into the protocols, roles and terminology involved in open standard federation protocols and how you as a developer can leverage these protocols to secure and enable identity in your application.

---

---
title: Protocols and Standards
description: "Open standard protocols define how the two parties (application provider and authentication provider) build a trust and communicate to authenticate the identity. Standards are critical as they allow inter-operability between different organizations and vendors - enabling connections to be made to many partners and applications easily and securely. Federation becomes a simple task when the only question that needs to be asked is \"Do you speak SAML?\"."
component: developer-resources
page_id: developer-resources:federated_sso_primer:protocols-standards
canonical_url: https://docs.pingidentity.com/developer-resources/federated_sso_primer/protocols-standards.html
revdate: September 30, 2020
section_ids:
  security-assertion-markup-language-saml: Security Assertion Markup Language (SAML)
  ws-federation: WS-Federation
  openid-connect: OpenID Connect
---

# Protocols and Standards

Open standard protocols define how the two parties (application provider and authentication provider) build a trust and communicate to authenticate the identity. Standards are critical as they allow inter-operability between different organizations and vendors - enabling connections to be made to many partners and applications easily and securely. Federation becomes a simple task when the only question that needs to be asked is "Do you speak SAML?".

There are three open standard federation protocols used widely today:

## Security Assertion Markup Language (SAML)

SAML is the most common protocol use to provide SSO to SaaS applications today. There are three versions SAML 1.0, 1.1 and 2.0 with version 2.0 being the most common implementation of SAML available.

## WS-Federation

WS-Federation is the passive or browser SSO protocol that is part of the WS-\* family of protocols. This protocol is widely used in Microsoft and IBM environments.

## OpenID Connect

A relatively new protocol (ratified in February 2014), Connect is designed as an extension to the popular OAuth 2.0 protocol used in web service security. OpenID Connect adds an authentication and identity layer on top of the core OAuth 2.0 protocol allowing an application to authenticate a user and receive a token it can use for API calls via the same process. OpenID Connect is optimal for internal SSO, web application SSO and mobile SSO.

---

---
title: Roles and Components
description: There are two main roles in a browser SSO transaction, the Identity Provider (IDP) who is responsible for authenticating the identity and generating a security token and the Service Provider (SP) who consumes that security token (receives and validates it) and translates the asserted identity into an application session.
component: developer-resources
page_id: developer-resources:federated_sso_primer:roles-components
canonical_url: https://docs.pingidentity.com/developer-resources/federated_sso_primer/roles-components.html
revdate: September 30, 2020
---

# Roles and Components

There are two main roles in a browser SSO transaction, the Identity Provider (IDP) who is responsible for authenticating the identity and generating a security token and the Service Provider (SP) who consumes that security token (receives and validates it) and translates the asserted identity into an application session.

![Federated web](_images/xvl1601508126178.png)

Along with the Identity Provider and Service Provider roles, there are a number of components that complete the overall federation scenario:

| Component                        | Description                                                                                                                                                                                                                                                                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Security Token                   | The security token or assertion is used to convey the identity of the authenticated user from the IDP over to the SP in a standard manner. The assertion contains security attributes, a digital signature and identity attributes. A SAML assertion and an OpenID Connect ID token are examples of federated security tokens. |
| Identity Store                   | The Identity Store is where the user authentication data is stored. Federation allows for this ID store to be moved from the Service Provider to the Identity Provider reducing the password proliferation challenge. A single identity store can be used to store passwords leading to increased security.                    |
| Authentication Integration Point | The interface that the authentication provider uses to authenticate the user. This may be a HTML form, an X509 certificate, Windows Authentication or other custom authentication process such as multi-factor.                                                                                                                |
| Application Integration Point    | On the Service Provider side, once a security token has been issued, received and validated at the SP an application session can be generated based on the asserted identity. The process to integrate an application into the federated process occurs at this application integration point.                                 |
| Federated Trust                  | For a Service Provider to trust an assertion generated by an Identity Provider a federated trust must be established. Generally this is achieved by swapping a metadata file which contains information about the connection and a digital signature certificate.                                                              |
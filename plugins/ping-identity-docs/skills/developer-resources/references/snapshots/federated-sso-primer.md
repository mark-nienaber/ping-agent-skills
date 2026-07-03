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

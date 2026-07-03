---
title: Agentless Integration Kit
description: The Agentless Integration Kit allows PingFederate to integrate with identity provider (IdP) and service provider (SP) applications for single sign-on (SSO).
component: agentless
page_id: agentless::pf_agentless_ik
canonical_url: https://docs.pingidentity.com/integrations/agentless/pf_agentless_ik.html
revdate: March 7, 2025
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Agentless Integration Kit

The Agentless Integration Kit allows PingFederate to integrate with identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* and service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* applications for single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*.

This integration uses a RESTful approach that doesn't require you to integrate agent software into your application. Instead, your application exchanges user-session attributes with PingFederate through direct HTTP calls to the adapter endpoints.

The Reference ID IdP Adapter can also redirect OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* authorization consent requests to an external application, as described in [External consent approval](custom_application_setup/pf_agentless_ik_external_consent_approval.html).

## Components

* Reference ID IdP Adapter

  Allows PingFederate to integrate with IdP applications for SSO.

* Reference ID SP Adapter

  Allows PingFederate to integrate with SP applications for SSO.

* Agentless IdP Java sample application

  An example IdP application that you can use to test the IdP adapter.

* Agentless SP Java sample application

  An example SP application that you can use to test the SP adapter.

|   |                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The sample applications included in the integration `.zip` archive are built with Java. You can find sample applications built with other languages, such as .NET Core, PHP, and Python, and get the latest version of the Java sample applications in the [Ping Identity GitHub repository](https://github.com/pingidentity?q=agentless). |

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, you can find more information in the following sections of the PingFederate documentation:

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

* [Managing SP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html)

* [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

## System requirements

* PingFederate 11.3 or later

* Your application must be web-based and able to do the following:

  * Make REST API calls to PingFederate

  * Store a reference ID, resume path, and other values

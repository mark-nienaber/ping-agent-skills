---
title: .NET Integration Kit
description: The .NET Integration Kit allows PingFederate to communicate user attributes with .NET-based web applications.
component: net
page_id: net::pf_net_ik
canonical_url: https://docs.pingidentity.com/integrations/net/pf_net_ik.html
revdate: June 20, 2024
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# .NET Integration Kit

The .NET Integration Kit allows PingFederate to communicate user attributes with .NET-based web applications.

When PingFederate is serving an identity provider (IdP) role, it can receive user attributes from a .NET IdP application. When PingFederate is serving a service provider (SP) role, it can send user attributes to a .NET SP application.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For new integrations, we encourage you to consider the [Agentless Integration Kit](../agentless/pf_agentless_ik.html), which can integrate with a variety of platforms using a modern RESTful approach. |

## Components

* OpenToken Adapter

  * An adapter that allows PingFederate to send or receive user attributes in the OpenToken format. See [OpenToken Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_opentoken_adapt.html) in the PingFederate documentation.

* OpenToken Agent

  * An agent that runs within your .NET application that allows it to send or receive user attributes in the OpenToken format.

* Sample application

  * The Integration Kit distribution also contains sample IdP and SP applications. The applications may be installed quickly for testing OpenToken processing and to provide a working demonstration of end-to-end single sign-on (SSO) and single logout (SLO). Source code and supporting files are included in the distribution and may be modified or used as a reference for application developers.

## Intended audience

This document is intended for PingFederate administrators and web-application developers.

Before you start, you should be familiar with the following parts of the PingFederate documentation:

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

* [Managing SP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html)

* [OpenToken Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_opentoken_adapt.html)

## System requirements

* PingFederate 9.0 or later.

* Microsoft .NET Framework 4.0 for the agent application.

---
title: Edge Security
description: Use the Edge Security module to integrate web applications, APIs, microservices, Internet of Things devices, and cloud-based services with the Ping Advanced Identity Software.
component: platform
version: 8
page_id: platform:platform-guide:edge-security
canonical_url: https://docs.pingidentity.com/platform/8/platform-guide/edge-security.html
section_ids:
  es-dependencies: Dependencies
  identity-gateway-module: Edge Security (PingGateway) module
  mcp-gateway-module: PingGateway Agent Gateway module
  open-finance-module: Open Finance module
---

# Edge Security

Use the Edge Security module to integrate web applications, APIs, microservices, Internet of Things devices, and cloud-based services with the Ping Advanced Identity Software.

Edge Security modules:

![](../_images/IdentityGateway.svg)

#### [Edge Security (PingGateway)](edge-security.html#identity-gateway-module)

![](../_images/fr-icon-Intelligent_Authentication_2020-120919_11COLOR.vecta.svg)

#### [PingGateway Agent Gateway](edge-security.html#mcp-gateway-module)

![](../_images/digital-identity.svg)

#### [Open Finance](edge-security.html#open-finance-module)

## Dependencies

The [Edge Security module](#identity-gateway-module) doesn't depend on any other modules.

The [PingGateway Agent Gateway module](#mcp-gateway-module) doesn't depend on any other modules.

The [Open Finance module](#open-finance-module) depends on these modules:

* [Edge Security (PingGateway) module](#identity-gateway-module)

* [Intelligent Access modules](access-management.html#authentication-module)

* [Federation module](access-management.html#federation-module)

* [Identity Lifecycle and Relationship module](identity-management.html#identity-lifecycle-module)

## Edge Security (PingGateway) module

PingGateway helps you integrate web applications, APIs, and microservices with Advanced Identity Software, without modifying the application or the container where it runs. Based on reverse proxy architecture, it enforces security and access control in conjunction with the PingAM modules.

PingGateway software provides the following capabilities:

* Protection for IoT services, microservices, and APIs

* Policy enforcement

* Adaptable throttling, monitoring, and auditing

* Secure token transformation

* Support for identity standards such as OAuth 2.0, OpenID Connect, SAML 2.0, and UMA 2.0

* Password capture and replay

* Rapid prototyping

Required modules: none.

| Feature                                  | Description                                                                                                                                              | Documentation                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Studio                                   | User interface for rapid development and prototyping.                                                                                                    | [Studio guide](https://docs.pingidentity.com/pinggateway/2025.11/studio-guide)                                                                                                                                                                                                                                                                                                                       |
| Single sign-on                           | Single sign-on in a single domain and across domains.                                                                                                    | [Single sign-on](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/sso-cdsso.html#sso) and [Cross-domain single sign-on](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/sso-cdsso.html#cdsso)                                                                                                                                                                         |
| Password replay                          | Secure replay of credentials to legacy applications or APIs.                                                                                             | [Password replay from AM](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/sso-cdsso.html#credentials-am), [Password replay from a database](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/sso-cdsso.html#credentials-database), and [Password replay from a file](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/sso-cdsso.html#credentials-file) |
| Policy enforcement                       | Enforcement of centralized authorization policies for applications requiring PingAM.                                                                     | [Enforce policy decisions from AM](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/policy-enforcement.html#pep) and [Harden authorization with advice from AM](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/policy-enforcement.html#stepup)                                                                                                                       |
| Federation                               | OpenID Connect 1.0.                                                                                                                                      | [OpenID Connect](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/oidc.html)                                                                                                                                                                                                                                                                                                          |
|                                          | OAuth 2.0.                                                                                                                                               | [IG as an OAuth 2.0 client](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/oauth2.html#oauth2-client) and [IG as an OAuth 2.0 resource server](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/oauth2.html#about-oauth2-rs)                                                                                                                                         |
|                                          | SAML 2.0.                                                                                                                                                | [SAML](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/saml.html)                                                                                                                                                                                                                                                                                                                    |
|                                          | SAML resources for mobile applications.                                                                                                                  | [Transform OpenID Connect ID tokens into SAML assertions](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/token-transformation.html#ttf)                                                                                                                                                                                                                                             |
| Finance APIs                             | Support for OAuth 2.0 Mutual TLS and Financial-Grade APIs.                                                                                               | [Validate certificate-bound access tokens](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/oauth2.html#oauth2-rs-introspect-mtls) and [FapiInteractionIdFilter](https://docs.pingidentity.com/pinggateway/2025.11/reference/FapiInteractionIdFilter.html)                                                                                                                            |
| WebSocket protocol                       | Detection of requests to upgrade from HTTPS to the WebSocket protocol, and creation of a secure, dedicated tunnel to send and receive WebSocket traffic. | [WebSocket traffic](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/websocket.html)                                                                                                                                                                                                                                                                                                  |
| Throttling                               | Throttling to limit access to protected applications.                                                                                                    | [Throttling](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/throttling.html)                                                                                                                                                                                                                                                                                                        |
| UMA resource server                      | Protection for resources and services according to the UMA 2.0 standard.                                                                                 | [UMA support](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/uma.html)                                                                                                                                                                                                                                                                                                              |
| DevOps tooling                           | Deployment of basic and customized configurations through Docker.                                                                                        | [Deployment guide](https://docs.pingidentity.com/pinggateway/2025.11/devops-guide)                                                                                                                                                                                                                                                                                                                   |
| Integration with Advanced Identity Cloud | Protection and integration of APIs and applications with PingOne Advanced Identity Cloud for authentication and authorization.                           | [Identity Cloud guide](https://docs.pingidentity.com/pinggateway/2025.11/identity-cloud-guide)                                                                                                                                                                                                                                                                                                       |
| Microgateway                             | PingGateway standalone deployed as a microgateway, securing microservices with OAuth 2.0.                                                                | [PingGateway as a microgateway](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/microgateway-protect-service.html)                                                                                                                                                                                                                                                                   |

## PingGateway Agent Gateway module

The PingGateway Agent Gateway module extends PingGateway capabilities to protect [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) services. MCP offers an open standard to connect artificial intelligence (AI) agents with AI servers. By exposing services over MCP, you make them usable by AI agents.

The challenge, however, is to implement an appropriate, consistent, documented, and adaptable security model across the service assets you expose over MCP. PingGateway helps you meet this challenge as an MCP gateway, protecting MCP servers to:

* Allow only valid MCP requests.

* Audit MCP requests and actors.

* Throttle request rates.

* Enforce coarse-grained OAuth 2.0 security controls.

* Enforce fine-grained access control policies with PingOne Authorize, PingOne Protect, and Advanced Identity Cloud.

* Perform token transformation mapped to your security models.

This module grants the rights to use the MCP specific filters and related features:

* McpAuditFiter

* McpContext

* McpProtectionFilter

* McpValidationFilter and MCP metrics

| Feature            | Description                                                   | Documentation                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MCP support        | Tutorial demonstrating how this module protects MCP services. | [MCP security gateway](https://docs.pingidentity.com/pinggateway/2025.11/mcp/)                                                                                                                                                                                                                                                                                                                                   |
| Complete reference | Full reference documentation for this module's capabilities.  | [McpAuditFilter](https://docs.pingidentity.com/pinggateway/2025.11/reference/McpAuditFilter.html)[McpContext](https://docs.pingidentity.com/pinggateway/2025.11/reference/McpContext.html)[McpProtectionFilter](https://docs.pingidentity.com/pinggateway/2025.11/reference/McpProtectionFilter.html)[McpValidationFilter](https://docs.pingidentity.com/pinggateway/2025.11/reference/McpValidationFilter.html) |

## Open Finance module

PingGateway Open Finance support overlays PingOne Advanced Identity Cloud and platform deployments for Financial-grade API (FAPI) compliance. Use the Open Finance module as a foundation for high security applications in trusted ecosystems.

The PingGateway Open Finance module provides the following capabilities:

* Secure dynamic client registration (DCR)

* Secure authorization server access to well-known metadata, authorization codes, pushed authorization requests (PAR), and access tokens

* Secure resource server access

* Trusted directory support

* API client and client organization tracking

* FAPI auditing

| Feature            | Description                                                       | Documentation                                                                                          |
| ------------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| FAPI support       | Tutorial demonstrating how the Open Finance module supports FAPI. | [FAPI tutorial](https://docs.pingidentity.com/pinggateway/2025.11/fapi/index.html) (evaluator's guide) |
| Complete reference | Full reference documentation for Open Finance capabilities.       | [FAPI reference](https://docs.pingidentity.com/pinggateway/2025.11/reference/Fapi.html)                |

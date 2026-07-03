---
title: About PingGateway and FAPI
description: Configure PingGateway and PingOne Advanced Identity Cloud for FAPI, a secure OAuth 2.0 profile for protecting APIs in high-security and financial environments
component: pinggateway
version: 2026
page_id: pinggateway:fapi:fapi
canonical_url: https://docs.pingidentity.com/pinggateway/2026/fapi/fapi.html
revdate: 2025-09-08T17:46:50Z
section_ids:
  testing_and_certification: Testing and certification
  pingone_advanced_identity_cloud: PingOne Advanced Identity Cloud
  pinggateway: PingGateway
  deployment: Deployment
---

# About PingGateway and FAPI

[FAPI](https://openid.net/wg/fapi/), originally short for Financial-grade API, is a secure OAuth 2.0 profile for protecting APIs in high security environments.

FAPI is a secure, interoperable alternative to screen scraping. You can use the secure profile for applications requiring tighter security than standard OAuth 2.0 and OpenID Connect, such as APIs accessing sensitive data or involving financial transactions.

## Testing and certification

In addition to publishing FAPI specifications, the FAPI Working Group at the OpenID Foundation offers conformance testing and certification for organizations implementing FAPI.

For example, a bank with open banking APIs can validate and certify their FAPI implementation. The OpenID Foundation publishes the certification so the bank's partners know what its implementation supports.

## PingOne Advanced Identity Cloud

PingOne Advanced Identity Cloud provides OAuth 2.0 and OpenID Provider authorization services. It dynamically registers and stores API client profiles.

Once configured as described in this tutorial, the PingOne Advanced Identity Cloud services support FAPI.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This tutorial shows how to configure your PingOne Advanced Identity Cloud tenant through the administrative UIs.As an alternative when evaluating PingGateway and FAPI, consider using the [Secure API Gateway platform configuration](https://github.com/SecureApiGateway/fr-platform-config) with the [PingOne Advanced Identity Cloud configuration management tools](https://github.com/ForgeRock/fr-config-manager) instead.For FAPI, use the `core` overlay from the Secure API Gateway configuration. The `ob` overlay is for OpenBanking deployments.While Ping Identity doesn't officially support the configuration management tools, they can simplify your work. The tools are community-supported. If you encounter an issue, raise it through the project GitHub site. |

Although not shown in this tutorial, you can configure self-hosted AM and IDM in a platform deployment to support FAPI. Adapt the instructions for configuring access and identity management services.

## PingGateway

PingGateway protects the PingOne Advanced Identity Cloud endpoints and your APIs, allowing only trusted API clients to register, get access tokens, and use the APIs.

PingGateway communicates with the trusted directory in a FAPI-based ecosystem to vet API clients. It prevents insecure and untrusted API clients from participating in the ecosystem. Trusted organizations register their keys in the trusted directory and use these to sign keys issued to their API clients.

## Deployment

The following image illustrates how you protect APIs with FAPI:

![FAPI deployment protecting banking APIs](_images/ig-fapi-mapping.png)

* You host your APIs and PingGateway acting as a reverse proxy for protected APIs.

* Ping Identity hosts your PingOne Advanced Identity Cloud tenants for access and identity management services.

* A central actor in the ecosystem hosts the trusted directory.

  For this tutorial, you can use the test trusted directory Docker image provided alongside PingGateway.

* Trust partners host the client applications using your APIs securely.

For this tutorial and to get started with conformance testing, you host the sample application as well.

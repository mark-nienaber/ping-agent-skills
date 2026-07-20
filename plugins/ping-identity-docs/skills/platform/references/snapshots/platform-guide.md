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

---

---
title: HSM support
description: This page covers how you can use a Hardware Security Module (HSM) to protect Ping Advanced Identity Software software private and secret keys.
component: platform
version: 8
page_id: platform:platform-guide:hsm-support
canonical_url: https://docs.pingidentity.com/platform/8/platform-guide/hsm-support.html
page_aliases: ["platform-setup-guide:hsm-support.adoc"]
section_ids:
  on_protecting_secrets: On protecting secrets
  performance: Performance
  how_ping_advanced_identity_software_interacts_with_hsms: How Ping Advanced Identity Software interacts with HSMs
  sun_pkcs11_provider_hints: Sun PKCS11 provider hints
  when_using_keytool: When using keytool
  when_java_cannot_find_keys: When Java cannot find keys
  hsm_features_and_ping_advanced_identity_software: HSM features and Ping Advanced Identity Software
  jwt_encryption_algorithms: JWT encryption algorithms
  jwt_signing_algorithms: JWT signing algorithms
  configure_ping_advanced_identity_software_to_use_an_hsm: Configure Ping Advanced Identity Software to use an HSM
---

# HSM support

This page covers how you can use a Hardware Security Module (HSM) to protect Ping Advanced Identity Software software private and secret keys.

## On protecting secrets

You must protect private keys and secret keys that servers use for cryptographic operations:

* Operating system protections

  In many deployments, operating system protections are sufficient. Operating systems are always sufficient for public keys and keystores that do not require protection.

  Isolate the server account on the operating system where it runs, and allow only that account to access the keys. If you store the keys with version control software, also control access to that.

  This deployment option generally offers a better performance/cost ratio. You must take more care to prevent private and secret keys from being exposed, however.

* HSM

  For stronger protection, you can use an HSM.

  An HSM is a secure device that holds the keys, and protects them from unauthorized access. With an HSM, no one gets direct access to the keys. If an attacker does manage to break into an HSM and theoretically get access to the keys, HSM are designed to make the tampering evident, so you can take action.

  To put a private or secret key on an HSM, you have the HSM generate the key. The key never leaves the HSM. Instead, if you need the result of a cryptographic operation involving the key, you authenticate to the HSM and request the operation. The HSM performs the operation without ever exposing any private or secret keys. It only returns the result.

  An HSM can be certified to comply with international standards, including FIPS-140 and Common Criteria. An HSM that is certified to comply with these standards can be part of your supported Ping Identity software solution.

  Ping Identity software uses the HSM through standard PKCS#11 interfaces, and supports the use of compliant cryptographic algorithms.

  An HSM generally offers higher security, but with a significant cost and impact on performance. Good HSMs and standards compliance come with their own monetary costs.

  In terms of performance, each cryptographic operation incurs at minimum a round trip on a secure connection, compared with an operation in local memory for keys on the system. Even if the deployment may guarantee the same throughput, take the latency into account when deciding to deploy with HSMs.

* Key management services

  Key management services, such as Google Cloud KMS and others, offer similar advantages and tradeoffs as HSMs.

  Latency for online key management services can be very high.

## Performance

*Throughput*, the rate of operations completed, might or might not be impacted by your choice of protecting secrets.

*Latency*, how long individual operations take, will be impacted by your choice of protecting secrets.

Performance Example

For example, suppose you want a system that signs one million JWTs per second. As long as you can distribute the signing key across enough hardware, your system can sign one million JWTs a second. This is true even if each signing operation takes ten seconds. You simply need ten million systems, and the network hardware to use them in parallel. Throughput therefore depends mainly on how much you can spend.

Suppose, however, that each signing operation must take no longer than ten milliseconds. Furthermore, suppose you have an HSM that can perform a signing operation in one millisecond, but that the network round trip from the system to the HSM takes an average of eleven milliseconds. In this case, you cannot fix performance by buying a faster HSM, or by somehow speeding up the software. You must first reduce the network time if you want to meet your latency requirements.

Perhaps the same signing operation with a key stored on the operating system takes two milliseconds. Consider the options based on your cost and security requirements.

Performance also depends on the following:

* The impact of latency is greater when performing symmetric cryptographic operations (AES, HMAC) compared to public key cryptography (RSA, EC).

* For public key cryptography, only operations that use the private key must contact the HSM (signing, decryption).

  Operations using the public key (verifying a signature, encryption) retrieve the public key from the HSM once, and then use it locally.

* Most public key cryptography uses hybrid encryption, where only a small operation must be done on the HSM, and the rest can be done locally.

  For example, when decrypting a large message, typically, the HSM is only used to decrypt a per-message AES key that is then used to decrypt the rest of the message locally.

  Similarly, for signing, the message to sign is first hashed in-memory using a secure hash algorithm, and only the short hash value is sent to the HSM to be signed.

  In contrast, when using symmetric key algorithms directly with an HSM, the entire message must be streamed to and from the HSM.

## How Ping Advanced Identity Software interacts with HSMs

Services built with Java interact with HSMs through Java PKCS#11 providers.

The PKCS#11 standard defines a cryptographic token interface, a platform-independent API for accessing an HSM, for example. Ping Advanced Identity Software supports the use of the Sun PKCS11 provider.

The Sun PKCS11 provider doesn't implement every operation and algorithm supported by every HSM. Learn about the Sun PKCS11 provider's capabilities in the [JDK Providers Documentation](https://docs.oracle.com/en/java/javase/21/security/oracle-providers.html), and the JDK [PKCS#11 Reference Guide](https://docs.oracle.com/en/java/javase/21/security/pkcs11-reference-guide.html).

How you configure the JVM to use your HSM depends on the Java environment and on your HSM. Advanced Identity Software components don't implement or manage this configuration, but they do depend on it. Before configuring Advanced Identity Software to use your HSM, you must therefore configure the JVM's Sun PKCS11 provider to access your HSM. Learn how to configure the Java Sun PKCS11 provider with your HSM in the documentation for your HSM and the JDK [PKCS#11 Reference Guide](https://docs.oracle.com/en/java/javase/21/security/pkcs11-reference-guide.html).

### Sun PKCS11 provider hints

The provider configuration depends on your provider.

Compare the following hints for Advanced Identity Software software with the documentation for your HSM:

* `name = FooHsm`

  The name used to produce the Sun PKCS11 provider instance name for your HSM.

  `FooHsm` is just an example.

* `CKA_TOKEN = false`

  Keys generated using the Java `keytool` command effectively have this set to `true`. They are permanent keys, to be shared across the deployment.

  Set this to `false` to prevent temporary keys for RSA hybrid encryption used by some Advanced Identity Software components from exhausting HSM storage.

* `CKA_PRIVATE = true`

  The key can only be accessed after authenticating to the HSM.

* * `CKA_EXTRACTABLE = false`
  * `CKA_SENSITIVE = true`

  `CKA_EXTRACTABLE = false` means the key cannot be extracted *unless it is encrypted*.

  `CKA_SENSITIVE = true` means do not let the secret key be extracted out of the HSM. Set this to `true` for long-term keys.

  Only change these settings to back up keys to a different HSM, when you cannot use a proprietary solution. For example, you might change these settings if the HSMs are from different vendors.

* `CKA_ENCRYPT = true`

  The key can be used to encrypt data.

* `CKA_DECRYPT = true`

  The key can be used to decrypt data.

* `CKA_SIGN = true`

  The key can be used to sign data.

* `CKA_VERIFY = true`

  The key can be used to verify signatures.

* `CKA_WRAP = true`

  The key can be used to wrap another key.

* `CKA_UNWRAP = true`

  The key can be used to unwrap another key.

### When using keytool

When using the Java `keytool` command to generate or access keys on the HSM, set the following options appropriately:

* `-alias` *alias*

  If key pair generation fails, use a new *alias* for the next try. This prevents the conflicts where the previous attempt to create a key was only a partial failure, leaving part of key pair using the previous alias.

* `-keystore none`

  Required setting.

* `-providername` *providerName*

  Required setting.

  Prefix `SunPKCS11-` to the name in the configuration. If, in the Sun PKCS11 configuration, `name = FooHSM`, then the *providerName* is `SunPKCS11-FooHSM`.

* `-storetype pkcs11`

  Required setting.

If necessary, add the following settings:

* `-providerClass sun.security.pkcs11.SunPKCS11`

  Use this to install the provider dynamically.

* `-providerArg` */path/to/config/file.conf*

  Use this to install the provider dynamically.

  The exact configuration depends on your HSM.

### When Java cannot find keys

When keys generated with one Java PKCS#11 provider are later accessed using the Sun PKCS11 provider, the providers may have different naming conventions.

Java's KeyStore abstraction requires that all private key objects have a corresponding Certificate object. SecretKey objects, such as AES or HMAC keys, are excluded from this requirement.

The Sun PKCS11 KeyStore provider loops through all defined private key entries in the HSM (class = private key), and tries to match them up with a corresponding certificate entry (class = certificate) by comparing the `CKA_ID` of the certificate entry to the `CKA_ID` of the private key entry. There may be multiple certificates using the same private key pair The matching process can take several seconds at startup time if you have many keys.

If keys are not found, it is likely that the private key entry `CKA_ID` does not match the certificate entry `CKA_ID`.

## HSM features and Ping Advanced Identity Software

This part outlines how some Ping Advanced Identity Software features support HSMs.

### JWT encryption algorithms

| JWT Encryption Algorithm           | Java Algorithm Equivalent                    | Supported by Sun PKCS11 Provider? |
| ---------------------------------- | -------------------------------------------- | --------------------------------- |
| RSA1\_5                            | RSA/ECB/PKCS1Padding(1)                      | Yes                               |
| RSA-OAEP                           | RSA/ECB/OAEPWithSHA-1AndMGF1Padding          | No                                |
| RSA-OAEP-256                       | RSA/ECB/OAEPWithSHA-256AndMGF1Padding        | No                                |
| ECDH-ES (+A128KW, and so on)(2)    | ECDH (KeyAgreement vs. Cipher)               | Yes                               |
| dir with A128GCM, A192GCM, A256GCM | AES/GCM/NoPadding                            | Yes                               |
| dir with A128CBC-HS256, and so on  | AES/CBC/PKCS5Padding + HmacSHA256, and so on | No                                |
| A128KW, A192KW, A256KW             | AESWrap                                      | No                                |

(1) PKCS#1 version 1.5 padding has known vulnerabilities and should be avoided.

(2) The Sun PKCS11 implementation of ECDH KeyAgreement requires that the derived key be extractable. This is not a security issue, as the derived key is unique to each message, and therefore no more sensitive than the message it is protecting, due to the use of fresh ephemeral keys for each message (ECIES). To ensure that the derived keys are extractable, add the following to the PKCS11 configuration file:

```none
attributes(*,CKO_PRIVATE_KEY,CKK_EC) = {
  CKA_SIGN = true
  CKA_DERIVE = true
  CKA_TOKEN = true
}

attributes(generate,CKO_SECRET_KEY,CKK_GENERIC_SECRET) = {
  CKA_SENSITIVE = false
  CKA_EXTRACTABLE = true
  CKA_TOKEN = false
}
```

This also ensures that EC keys generated with the `keytool` command are marked as allowing ECDH key derivation. The derived keys are also marked as `CKA_TOKEN = false`, which ensures that the derived keys are only created as session keys, and automatically deleted when the session ends to prevent filling up the HSM with temporary keys.

### JWT signing algorithms

| JWT Signing Algorithm | Java Algorithm Equivalent                     | Supported by Sun PKCS11 Provider? |
| --------------------- | --------------------------------------------- | --------------------------------- |
| HS256, HS384, HS512   | HmacSHA256, HmacSHA384, HmacSHA512            | Yes                               |
| RS256, RS384, RS512   | SHA256WithRSA, SHA384WithRSA, SHA512WithRSA   | Yes                               |
| PS256, PS384, PS512   | RSASSA-PSS or SHA256WithRSAAndMGF1, and so on | No                                |
| ES256, ES384, ES512   | SHA256WithECDSA, and so on                    | Yes                               |
| EdDSA                 | Under development                             | No                                |

## Configure Ping Advanced Identity Software to use an HSM

Once you have configured the Java environment to use your HSM through the Sun PKCS11 Provider, you can configure Ping Advanced Identity Software to use the HSM:

* PingAM: Learn more in [Secrets, certificates, and keys](https://docs.pingidentity.com/pingam/8/security-guide/secrets-certs-keys.html).

* PingDS: Learn more in [PKCS#11 hardware security module](https://docs.pingidentity.com/pingds/8/security-guide/pki-hsm.html).

* PingIDM: Learn more in [Hardware secret stores](https://docs.pingidentity.com/pingidm/8/security-guide/secret-stores-hardware.html).

* PingGateway: Learn more in [Keys and secrets](https://docs.pingidentity.com/pinggateway/2025.11/security-guide/keys.html), and [HsmSecretStore](https://docs.pingidentity.com/pinggateway/2025.11/reference/HsmSecretStore.html).

---

---
title: Overview
description: Ping Advanced Identity Software is the only offering for access management, identity management, user-managed access, directory services, and an identity gateway, designed and built as a single, unified platform.
component: platform
version: 8
page_id: platform:platform-guide:about
canonical_url: https://docs.pingidentity.com/platform/8/platform-guide/about.html
page_aliases: ["_@platform::index.adoc"]
section_ids:
  about_this_documentation: About this documentation
  pingam_modules: PingAM modules
  pingidm_modules: PingIDM modules
  pingds_modules: PingDS modules
  pinggateway_modules: PingGateway modules
  sample_deployments: Sample deployments
  deployment_enhancements: Deployment enhancements
  run_advanced_identity_software_in_containers_on_kubernetes: Run Advanced Identity Software in containers on Kubernetes
  kubernetes_deployment_tools_from_ping_identity: Kubernetes deployment tools from Ping Identity
  partner_offerings: Partner offerings
  forgerock_authenticator_application: ForgeRock Authenticator application
---

# Overview

Ping Advanced Identity Software is the only offering for access management, identity management, user-managed access, directory services, and an identity gateway, designed and built as a single, unified platform.

## About this documentation

This documentation includes general statements of functionality for the latest versions of the following software:

* PingAM, with Web Agents and Java Agents

* PingIDM

* PingDS

* Edge Security (PingGateway)

This documentation describes in general terms the modules that compose Ping Advanced Identity Software, and indicates where to find the documentation corresponding to each module. This documentation is not meant to serve as a statement of functional specifications. Software functionality may evolve in incompatible ways in major and minor releases, and occasionally in maintenance (patch) releases. Release notes cover many incompatible changes. If you see an incompatible change for a stable interface that is not mentioned in the release notes, please report an issue with the product documentation for that release.

## PingAM modules

![](../_images/fr-icon-Intelligent_Authentication_2020-120919_11COLOR.vecta.svg)

#### [Intelligent Access](access-management.html#authentication-module)

![](../_images/fr-icon-Authorization_2020-120919_38COLOR.vecta.svg)

#### [Authorization](access-management.html#authorization-module)

![](../_images/fr-icon-Federation_2020-120919_23COLOR.vecta.svg)

#### [Federation](access-management.html#federation-module)

![](../_images/digital-identity.svg)

#### [Self-Managed Strong Authentication](access-management.html#strong-auth)

![](../_images/fr-icon-Control_Access_2020-120919_30COLOR.vecta.svg)

#### [User-Managed Access](access-management.html#uma-module)

## PingIDM modules

![](../_images/fr-icon-Synchronization_Reconcilliation_2020-120919_15COLOR.vecta.svg)

#### [Identity Synchronization](identity-management.html#identity-sync-module)

![](../_images/fr-icon-Basic_SelfService_2020-120919_35COLOR.vecta.svg)

#### [Self-Service](identity-management.html#self-service-module)

![](../_images/fr-icon-Workflow_Engine_2020-120919_16COLOR.vecta.svg)

#### [Workflow](identity-management.html#workflow-module)

![](../_images/fr-icon-Social_Signon_2020-120919_28COLOR.vecta.svg)

#### [Social Identity](identity-management.html#social-identity-module)

![](../_images/fr-icon-Manage_Identities_2020-120919_25COLOR.vecta.svg)

#### [Identity Lifecycle and Relationship](identity-management.html#identity-lifecycle-module)

## PingDS modules

![](../_images/DirectoryServer.svg)

#### [Directory Server](directory-services.html#directory-services-module)

![](../_images/DirectoryProxyServer.svg)

#### [Directory Proxy Server](directory-services.html#directory-proxy-module)

## PingGateway modules

![](../_images/IdentityGateway.svg)

#### [Edge Security (PingGateway)](edge-security.html#identity-gateway-module)

![](../_images/fr-icon-Intelligent_Authentication_2020-120919_11COLOR.vecta.svg)

#### [PingGateway Agent Gateway](edge-security.html#mcp-gateway-module)

![](../_images/digital-identity.svg)

#### [Open Finance](edge-security.html#open-finance-module)

## Sample deployments

The [sample deployments](../sample-setup/preface.html) show a minimal integration of the above modules to get you started with a self-managed deployment.

Ping Advanced Identity Software offers maximum extensibility and flexibility in self-managed deployments. It includes many features and options the sample setup instructions don't cover. If you don't need maximum extensibility and flexibility, there are simpler alternatives:

* To consume Ping Advanced Identity Software as a service, use Advanced Identity Cloud instead.

* To deploy Ping Advanced Identity Software in Kubernetes, start with the [ForgeOps](https://docs.pingidentity.com/forgeops) reference implementation.

## Deployment enhancements

In addition to the modules listed in the preceding section, you can use the following software to enhance Advanced Identity Software deployments.

### Run Advanced Identity Software in containers on Kubernetes

Ping Advanced Identity Software, (PingAM, PingIDM, PingDS, PingGateway, and the Platform UI) is supported when running in containers on Kubernetes platforms, including Google Kubernetes Engine (GKE), Amazon Elastic Kubernetes Service (Amazon EKS), Microsoft Azure Kubernetes Service (AKS), and IBM RedHat OpenShift. It's recommended that you have a support contract in place with your Kubernetes platform vendor or partner to resolve any infrastructure or Kubernetes platform-related issues. Ping Identity supports Ping Advanced Identity Software while the Kubernetes vendor or partner provides support for their platform.

*You are responsible for building images and running containers of the Ping Identity software components using a [supported operating system](https://support.pingidentity.com/s/article/What-operating-systems-are-PingAM-PingDS-PingIDM-and-PingGateway-supported-on) and all required software dependencies.*

#### Kubernetes deployment tools from Ping Identity

Ping Identity provides a reference toolset in the [forgeops](https://github.com/ForgeRock/forgeops/tree/release/7.5-20240402) and [forgeops-extras](https://github.com/ForgeRock/forgeops-extras) Git repositories for automating the deployment of Advanced Identity Software in Kubernetes. These reference tools are provided for use with Google Kubernetes Engine, Amazon Elastic Kubernetes Service, and Microsoft Azure Kubernetes Service. (Ping Identity supports running Advanced Identity Software on IBM RedHat OpenShift but does not provide the reference tools for IBM RedHat OpenShift.)

Ping Identity also publishes reference Docker images for testing and development, but these images should *not* be used in production. For production deployments, it is recommended that customers build and run containers using a [supported operating system](https://support.pingidentity.com/s/article/What-operating-systems-are-PingAM-PingDS-PingIDM-and-PingGateway-supported-on) and all required software dependencies. Additionally, to help ensure interoperability across container images and the ForgeOps tools, Docker images must be built using the Dockerfile templates as described in the [ForgeOps documentation](https://docs.pingidentity.com/forgeops/2025.1).

#### Partner offerings

Ping Identity's partner, [Midships Limited](https://www.midships.io), offers a Kubernetes deployment accelerator (supported by Midships) for Google Kubernetes Engine (GKE), Amazon Elastic Kubernetes Service (Amazon EKS), Microsoft Azure Kubernetes Service (AKS), and IBM RedHat OpenShift.

### ForgeRock Authenticator application

This app allows end users to perform multi-factor authentication and transactional authorization from a registered Android or iOS device. It is designed for use in both multi-factor and passwordless authentication scenarios. It is associated with a Push Authentication Simple Notification Service module that depends on the module described in [Intelligent Access modules](access-management.html#authentication-module).

See [MFA: push authentication](https://docs.pingidentity.com/pingam/8/authentication-guide/authn-mfa-about-push.html) and [Transactional authorization](https://docs.pingidentity.com/pingam/8/authorization-guide/transactional-authorization.html).

---

---
title: PingAM
description: PingAM modules:
component: platform
version: 8
page_id: platform:platform-guide:access-management
canonical_url: https://docs.pingidentity.com/platform/8/platform-guide/access-management.html
section_ids:
  am-overview: Overview of capabilities
  am-dependencies: Dependencies
  authentication-module: Intelligent Access modules
  authorization-module: Authorization module
  federation-module: Federation module
  strong-auth: Self-Managed Strong Authentication module
  uma-module: User-Managed Access module
---

# PingAM

PingAM modules:

![](../_images/fr-icon-Intelligent_Authentication_2020-120919_11COLOR.vecta.svg)

#### [Intelligent Access](access-management.html#authentication-module)

![](../_images/fr-icon-Authorization_2020-120919_38COLOR.vecta.svg)

#### [Authorization](access-management.html#authorization-module)

![](../_images/fr-icon-Federation_2020-120919_23COLOR.vecta.svg)

#### [Federation](access-management.html#federation-module)

![](../_images/digital-identity.svg)

#### [Self-Managed Strong Authentication](access-management.html#strong-auth)

![](../_images/fr-icon-Control_Access_2020-120919_30COLOR.vecta.svg)

#### [User-Managed Access](access-management.html#uma-module)

## Overview of capabilities

* Intelligent access

* Mobile authentication

* Push authentication

* Adaptive risk authentication

* Authorization policies and enforcement

* Federation

* Single sign-on (SSO)

* User self-services and social sign-on

* High-availability and scalability

* Adaptable monitoring and auditing services

* Developer-friendly, rich standards support

## Dependencies

Several Access Management modules require other modules. For example, the Federation module requires the Intelligent Access module. The following diagram summarizes Access Management module dependencies:

![PingAM module dependencies](../_images/AMDependencies.svg)

## Intelligent Access modules

This module helps you build secure, robust, centrally managed single sign-on services. The user, application, or device signs on once and is granted appropriate access everywhere. Authentication management integrates delegated authentication with many authentication methods supported by default. Authentication journeys store authentication sessions in the client as a cookie, or in the CTS store. If the PingAM server goes down or the user is redirected to another PingAM while authenticating, the new PingAM server can grab the authentication session and continue the flow. All authentication-related events are logged for auditing and reporting purposes.

Required modules: none.

| Feature                                | Description                                                                                                                                                                                                                                                                                                                       | Documentation                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication trees and nodes         | Authentication trees provide fine-grained authentication, social authentication, and multi-factor authentication. Trees are made up of authentication nodes. Authentication nodes allow multiple paths and decision points throughout the authentication flow, enabling PingAM to handle different modes of authenticating users. | [Authentication nodes and trees](https://docs.pingidentity.com/pingam/8/authentication-guide/about-authentication-trees.html)                                                                                                                                                                                                                                                    |
| Session high availability              | Persistent access management sessions, authenticating the user until the session expires.                                                                                                                                                                                                                                         | Session high availability is enabled by default with no setup required.                                                                                                                                                                                                                                                                                                          |
| Multi-factor and strong authentication | Capability to challenge for additional credentials when authentication takes place under centrally-defined risky or suspicious conditions.                                                                                                                                                                                        | [Multi-factor authentication](https://docs.pingidentity.com/pingam/8/authentication-guide/authn-introduction-authn.html#about-mfa)                                                                                                                                                                                                                                               |
| External configuration store           | Configuration storage in PingDS for high-availability.                                                                                                                                                                                                                                                                            | [Prepare configuration stores](https://docs.pingidentity.com/pingam/8/install-guide/prepare-configuration-store.html)                                                                                                                                                                                                                                                            |
| Security token service                 | Bridges identities across web and enterprise identity access management (IAM) systems through a token transformation process, securely providing cross-system access to service resources by authenticated requesting applications.                                                                                               | [STS overview](https://docs.pingidentity.com/pingam/8/sts-guide/chap-sts-introduction.html)                                                                                                                                                                                                                                                                                      |
| Web and Java agents for SSO            | Intercept requests to access protected resources and redirect for appropriate authentication.                                                                                                                                                                                                                                     | [Web policy agents](https://docs.pingidentity.com/web-agents/2025.3) and [Java policy agents](https://docs.pingidentity.com/java-agents/2025.3)                                                                                                                                                                                                                                  |
| User login analytics                   | Measure authentication flows using counters and start/stop timers to monitor performance.                                                                                                                                                                                                                                         | [Timer Start node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-timer-start.html), [Timer Stop node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-timer-stop.html), [Meter node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-meter.html), and [Monitoring metrics](https://docs.pingidentity.com/pingam/8/maintenance/monitoring-metrics.html) |

## Authorization module

This module will help you create powerful, context-based policies with a GUI-based policy editor and with REST APIs to control access to online resources. Resources can be URLs, external services, or devices and things. Authorization management lets you manage policies centrally and enforce them locally through installable agents, or through REST, C, and Java applications. Authorization management is extensible, making it possible to define external subjects, complex conditions, and custom access decisions.

Required module: Intelligent Access.

| Feature                             | Description                                                                                                                                                               | Documentation                                                                                                                                   |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Entitlement policies                | Modern web-based policy editor for building policies, making it possible to add and update policies as needed without touching the underlying applications.               | [Authorization and policy decisions](https://docs.pingidentity.com/pingam/8/authorization-guide/what-is-authz-decision.html)                    |
| Web and Java agents for enforcement | Access enforcement for online resources with the capability to require higher levels of authentication and session upgrade when accessing sensitive resources.            | [Web policy agents](https://docs.pingidentity.com/web-agents/2025.3) and [Java policy agents](https://docs.pingidentity.com/java-agents/2025.3) |
| Transactional authorization         | Requires a user to perform additional actions such as reauthenticating to a module or node, or responding to a push notification, to gain access to a protected resource. | [Transactional authorization](https://docs.pingidentity.com/pingam/8/authorization-guide/transactional-authorization.html)                      |
| OAuth 2.0 dynamic scopes            | A single OAuth 2.0 client configured for a comprehensive list of scopes can serve different scope subsets to resource owners based on policy conditions.                  | [Dynamic OAuth 2.0 authorization](https://docs.pingidentity.com/pingam/8/authorization-guide/oauth2-authorization.html)                         |

## Federation module

This module will help you extend SSO capabilities across organization boundaries based on standards-based interoperability.

Required module: Intelligent Access.

| Feature                                  | Description                                                                                                                                              | Documentation                                                                                                           |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| SAML 2.0 IDP and SP                      | Identity federation with SaaS applications, such as Salesforce.com, Google Apps, WebEx, and many more.                                                   | [Configure IdPs, SPs, and COTs](https://docs.pingidentity.com/pingam/8/saml2-guide/saml2-providers-and-cots.html)       |
| SAML 2.0 SSO and SLO                     | Web Single Sign-On and Single Logout profile support.                                                                                                    | [Implement SSO and SLO](https://docs.pingidentity.com/pingam/8/saml2-guide/saml2-sso-slo.html)                          |
| ADFS                                     | Federation with Active Directory Federation Services.                                                                                                    | [Introduction to SAML v2.0](https://docs.pingidentity.com/pingam/8/saml2-guide/saml2-introduction.html)                 |
| SAML 2.0 Attribute and Advanced Profiles | Support for transmitting only attributes used by targeted applications.                                                                                  | [SAML v2.0](https://docs.pingidentity.com/pingam/8/saml2-guide/preface.html)                                            |
| OpenID Connect                           | OpenID Connect 1.0 compliance for running an OpenID Provider, including advanced profiles, such as Mobile Connect.                                       | [OpenID Connect 1.0](https://docs.pingidentity.com/pingam/8/oidc1-guide/preface.html)                                   |
| OAuth 2.0                                | OAuth 2.0 compliance for running an authorization server.                                                                                                | [OAuth 2.0](https://docs.pingidentity.com/pingam/8/oauth2-guide/preface.html)                                           |
| Social login                             | For acting as an OAuth 2.0 client of social identity providers, such as Facebook, Google, and Microsoft.                                                 | [Social authentication](https://docs.pingidentity.com/pingam/8/authentication-guide/social-registration.html)           |
| OAuth 2.0 dynamic scopes                 | A single OAuth 2.0 client configured for a comprehensive list of scopes can serve different scope subsets to resource owners based on policy conditions. | [Dynamic OAuth 2.0 authorization](https://docs.pingidentity.com/pingam/8/authorization-guide/oauth2-authorization.html) |

## Self-Managed Strong Authentication module

This module gives end users additional authentication capabilities through their own devices. Multi-faceted device management enhances security and simplifies the authentication experience for end users.

Required modules: Intelligent Access

| Feature                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Documentation                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Geolocation                          | Manages risk by assessing whether the authenticating user's device is located within range of configured, trusted locations, or within range of somewhere the user has authenticated from, and saved, previously.PingAM compares collected device location metadata with trusted locations in the authentication configuration or with device locations stored in the user's profile.                                                                                                                                                                                                                                                                                                                                                                 | [Device Geofencing node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-device-geofencing.html) and [Device Profile Location Match node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-device-profile-location-match.html)                                                                                                                                                                                           |
| Device tampering                     | Provides a configurable threshold for assessing the risk of a user's device during authentication based on a risk score. The higher the score returned from the device, the more likely the device is jailbroken, rooted, or is a potential security risk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Device Tampering Verification node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-device-tampering-verification.html)                                                                                                                                                                                                                                                                                                        |
| Device binding and trust             | During the Device Binding process, secure cryptography keys are generated, which are used to perform various functions, such as encryption and decryption of user data. These keys are unique to the device and can't be transferred to another device, ensuring that the user's account can only be accessed from authorized devices. This helps to protect against unauthorized access.One user can have multiple associated devices and multiple users can associate with one device.Devices are bound using authentication journeys. PingAM supports a number of different authentication types for device binding, including biometric,biometric with fallback, application PIN and silent authentication.                                       | [Device Binding node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-device-binding.html), [Device Binding Storage node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-device-binding-storage.html), and [Device Signing Verifier node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-device-signing-verifier.html)                                                                                        |
| Application MFA                      | Open AuTHentication (OATH) OATH-related nodes supports the following MFA methods:- Time-based one-time passwords (TOTP)

- HMAC-based one-time passwords (HOTP)

- Push notificationsThese nodes can integrate with the ForgeRock Authenticator app for Android and iOS and with third-party authenticator apps that support the HOTP and TOTP standards.                                                                                                                                                                                                                                                                                                                                                                                             | [OATH Device Storage node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-oath-device-storage.html), [OATH Registration node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-oath-registration.html), [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-oath-token-verifier.html), and [ForgeRock Authenticator](https://docs.pingidentity.com/sdks/latest/authenticator/index.html) |
| Transaction signing                  | Digital signing helps ensure the authenticity and integrity of customer data in a variety of use cases, including financial transactions, end user agreements, changes in account details, and so on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Device Signing Verifier node](https://docs.pingidentity.com/auth-node-ref/8/auth-node-device-signing-verifier.html)                                                                                                                                                                                                                                                                                                                    |
| WebAuthN passwordless authentication | Passwordless authentication (WebAuthn) is better than traditional password-based authentication because it reduces the risk of password-based attacks like phishing and brute-force attacks. Passwordless authentication also creates a better, more seamless experience for end users. It's compatible across most devices and systems and end users don't have to remember a number of passwords across systems.Passwordless authentication uses other forms of identity verification instead of a standard password login. These methods can include face recognition, fingerprints, software or hardware token devices, and so on. End users authenticate with an authenticator device, such as the fingerprint scanner on their laptop or phone. | [MFA: Web authentication (WebAuthn)](https://docs.pingidentity.com/pingam/8/authentication-guide/authn-mfa-webauthn.html)                                                                                                                                                                                                                                                                                                               |

## User-Managed Access module

This module consists of a consumer-facing implementation of the User-Managed Access (UMA) 2.0 standard. The standard defines an OAuth 2.0-based protocol designed to give individuals a unified control point for authorizing who and what can access their digital data, content, and services. For example, you can use this module to build a solution where end users can delegate access through a share button, and then monitor and change sharing preferences through a central dashboard.

Required modules: Authorization, Intelligent Access.

| Feature                  | Description                                                                                                                                                         | Documentation                                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| UMA standard conformance | Conformance to the UMA 2.0 standard for interoperability with organizational and partner systems, including federated authorization and customer-centric use cases. | [User-Managed Access (UMA) 2.0](https://docs.pingidentity.com/pingam/8/uma-guide/preface.html)               |
| UMA authorization server | Authorization server with dynamic resource set registration, end-user control of resource sharing, responses to access requests, and full audit history.            | [PingAM as UMA authorization server](https://docs.pingidentity.com/pingam/8/uma-guide/uma-introduction.html) |
| UMA protector            | PingGateway protection for resources and services with the UMA 2.0 standard.                                                                                        | [UMA support](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/uma.html)                      |

---

---
title: PingDS
description: PingDS 8 serves as a foundation for LDAPv3 and RESTful directories.
component: platform
version: 8
page_id: platform:platform-guide:directory-services
canonical_url: https://docs.pingidentity.com/platform/8/platform-guide/directory-services.html
section_ids:
  ds-overview: Overview of capabilities
  ds-dependencies: Dependencies
  directory-services-module: Directory Server module
  directory-proxy-module: Directory Proxy Server module
---

# PingDS

PingDS 8 serves as a foundation for LDAPv3 and RESTful directories.

PingDS modules:

![](../_images/DirectoryServer.svg)

#### [Directory Server](directory-services.html#directory-services-module)

![](../_images/DirectoryProxyServer.svg)

#### [Directory Proxy Server](directory-services.html#directory-proxy-module)

## Overview of capabilities

* Large-scale, distributed read and write performance

* Flexible key-value data model for storing users, devices, and things

* Data storage with confidentiality, integrity, and security

* High-availability through data replication and proxy services

* Single logical entry point for use in protecting LDAPv3 directory services

* Load balancing and failover for LDAPv3 directory services

* Maximum interoperability and pass-through delegated authentication

* Adaptable monitoring and auditing services

* Easy installation, configuration, and management

* Developer-friendly, rich standards support

* REST API to access LDAP native capabilities over HTTP

## Dependencies

Neither of the Directory Services modules are dependent upon other modules.

## Directory Server module

The Directory Server module helps you store identities for users, devices, and things in a highly available and secure way. This module provides data replication to help you build highly available directory services. It also offers fine-grained access control, password digests, encryption schemes, and customizable password policies to allow you to build very secure directory services. Data may be accessed using LDAP or REST with the same level of security constraints and access control.

Required modules: none.

| Feature                                    | Description                                                                                                                                         | Documentation                                                                                                                                                         |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LDAPv3                                     | Compliance with the latest LDAP protocol standards.                                                                                                 | [About directories](https://docs.pingidentity.com/pingds/8/getting-started/directory-services.html)                                                                   |
| HDAP                                       | Access LDAP data over HTTP using Directory Access Protocol (HDAP) APIs that transform HTTP operations into LDAP operations.                         | [Learn HDAP](https://docs.pingidentity.com/pingds/8/getting-started/rest.html)                                                                                        |
| High-availability multi-master replication | Data replication for always-on services, enabling failover and disaster recovery.                                                                   | [Replication](https://docs.pingidentity.com/pingds/8/config-guide/replication.html)                                                                                   |
| User/object store                          | Flexible key-value data model for storing users, devices, and things.                                                                               | [Use LDAP](https://docs.pingidentity.com/pingds/8/ldap-guide/index.html#preface)                                                                                      |
| Passwords and data security                | Password digests, encryption schemes, and customizable rules for password policy compliance to help protect data on disk and shared infrastructure. | [Data encryption](https://docs.pingidentity.com/pingds/8/security-guide/data.html), [Passwords](https://docs.pingidentity.com/pingds/8/security-guide/passwords.html) |
| REST APIs and HDAP                         | HTTP-based RESTful access to user data.                                                                                                             | [Use HDAP](https://docs.pingidentity.com/pingds/8/rest-guide/preface.html)                                                                                            |

## Directory Proxy Server module

The ForgeRock Directory Proxy Server module helps you increase the availability of a Directory Service deployment, providing a single point of access to a large-scale distributed data store. The module offers a choice of strategies for request load balancing and failover. Data may be accessed using LDAP or REST with the same level of security constraints and access control.

Required modules: none.

| Feature                             | Description                                                                                                                                              | Documentation                                                                                                                                                                                                              |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single point of access              | Uniform view of underlying LDAPv3 directory services for client applications.                                                                            | [Single point of access](https://docs.pingidentity.com/pingds/8/config-guide/proxy.html#proxy-access-point)                                                                                                                |
| High service availability           | LDAP services with reliable crossover and DN-based routing.                                                                                              | [High availability](https://docs.pingidentity.com/pingds/8/config-guide/proxy.html#proxy-ha)                                                                                                                               |
| Load balancing and failover         | Configurable load balancing across directory servers with redundancy, and capabilities to handle referrals, connection failures, and network partitions. | [Load balancing](https://docs.pingidentity.com/pingds/8/config-guide/proxy.html#proxy-load-balancing)                                                                                                                      |
| Protection for PingDS               | Secure incoming and outgoing connections, and provide coarse-grained access control.                                                                     | [Secure connections](https://docs.pingidentity.com/pingds/8/security-guide/connections.html) and [Proxy global policies](https://docs.pingidentity.com/pingds/8/security-guide/access.html#global-access-control-policies) |
| Scaling out using data distribution | Distribute data across multiple shards.                                                                                                                  | [Data distribution](https://docs.pingidentity.com/pingds/8/config-guide/proxy.html#pattern-data-distribution-example)                                                                                                      |
| LDAPv3                              | Compliance with the latest LDAP protocol standards.                                                                                                      | [Supported standards](https://docs.pingidentity.com/pingds/8/ldap-reference/standards.html)                                                                                                                                |
| REST APIs                           | HTTP-based RESTful access to user data.                                                                                                                  | [Use HDAP](https://docs.pingidentity.com/pingds/8/rest-guide/preface.html)                                                                                                                                                 |

---

---
title: PingIDM
description: PingIDM 8 brings together multiple sources of identity for policy and workflow-based management that puts you in control of the data. Build a solution to consume, transform, and feed data to external sources to help you maintain control over identities of users, devices, and things. Identity governance features in PingIDM let you gain visibility into employee provisioning, and help you proactively take action in managing employee access to external systems.
component: platform
version: 8
page_id: platform:platform-guide:identity-management
canonical_url: https://docs.pingidentity.com/platform/8/platform-guide/identity-management.html
section_ids:
  idm-overview: Overview of capabilities
  idm-dependencies: Dependencies
  identity-sync-module: Identity Synchronization module
  self-service-module: Self-Service module
  workflow-module: Workflow module
  social-identity-module: Social Identity module
  identity-lifecycle-module: Identity Lifecycle and Relationship module
---

# PingIDM

PingIDM 8 brings together multiple sources of identity for policy and workflow-based management that puts you in control of the data. Build a solution to consume, transform, and feed data to external sources to help you maintain control over identities of users, devices, and things. Identity governance features in PingIDM let you gain visibility into employee provisioning, and help you proactively take action in managing employee access to external systems.

PingIDM modules:

![](../_images/fr-icon-Synchronization_Reconcilliation_2020-120919_15COLOR.vecta.svg)

#### [Identity Synchronization](identity-management.html#identity-sync-module)

![](../_images/fr-icon-Basic_SelfService_2020-120919_35COLOR.vecta.svg)

#### [Self-Service](identity-management.html#self-service-module)

![](../_images/fr-icon-Workflow_Engine_2020-120919_16COLOR.vecta.svg)

#### [Workflow](identity-management.html#workflow-module)

![](../_images/fr-icon-Social_Signon_2020-120919_28COLOR.vecta.svg)

#### [Social Identity](identity-management.html#social-identity-module)

![](../_images/fr-icon-Manage_Identities_2020-120919_25COLOR.vecta.svg)

#### [Identity Lifecycle and Relationship](identity-management.html#identity-lifecycle-module)

## Overview of capabilities

* Provisioning

* Synchronization and reconciliation

* Adaptable monitoring and auditing services

* Connections to cloud services with simple social registration

* Flexible developer access

* Password synchronization

* Identity data visualization

* Delegated administration

* User self-service

* Privacy and consent

* Progressive profile completion

* Workflow engine

* OpenICF connector framework to external systems

## Dependencies

Several Identity Management modules require other modules. For example, the Synchronization module requires the Identity Lifecycle and Relationship module. The following diagram summarizes Identity Management module dependencies:

![PingIDM module dependencies](../_images/IDMDependencies.svg)

## Identity Synchronization module

This module can serve as the foundation for provisioning and identity data reconciliation. Synchronization capabilities are available as a service and hrough REST APIs to be used directly by external applications. Activities occurring in the system can be configured to log and audit events for reporting purposes.

Required module: Identity Lifecycle and Relationship.

| Feature                             | Description                                                                                                                       | Documentation                                                                                                                                                                                                                          |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Discovery and synchronization       | Synchronization of identity data across managed data stores.                                                                      | [Synchronization types](https://docs.pingidentity.com/pingidm/8/synchronization-guide/sync-types.html#overview-livesync)                                                                                                               |
| Reconciliation                      | Alignment between accounts across managed data stores.                                                                            | [Synchronization types](https://docs.pingidentity.com/pingidm/8/synchronization-guide/sync-types.html#overview-recon)                                                                                                                  |
| Password synchronization            | Near real-time password synchronization across managed data stores.                                                               | [Password synchronization plugins](https://docs.pingidentity.com/pingidm/8/pwd-plugin-guide)                                                                                                                                           |
| PingDS and Active Directory plugins | Native password synchronization plugins for PingDS and Microsoft Active Directory.                                                | [Synchronize passwords with DS](https://docs.pingidentity.com/pingidm/8/pwd-plugin-guide/chap-sync-dj.html), [Synchronize passwords with Active Directory](https://docs.pingidentity.com/pingidm/8/pwd-plugin-guide/chap-sync-ad.html) |
| Delegated administration            | Grant role-based, limited access to perform fine-grained administrative tasks on managed objects.                                 | [Delegated administration](https://docs.pingidentity.com/pingidm/8/auth-guide/delegated-admin.html)                                                                                                                                    |
| All connectors                      | Extensible interoperability for identity, compliance, and risk management across a variety of specific applications and services. | [Connector reference](https://docs.pingidentity.com/openicf/connector-reference/preface.html)                                                                                                                                          |

## Self-Service module

This module can be used to allow end users to manage their own passwords and profiles securely according to predefined policies.

Required modules:

* Full capabilities: Identity Lifecycle and Relationship.

* Basic capabilities: Intelligent Access. Learn more in [About user self-service](https://docs.pingidentity.com/pingam/8/user-self-service/about-uss.html) regarding self-service capabilities in PingAM.

| Feature                                    | Description                                                                                                        | Documentation                                                                                                                 |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| User self-registration                     | End-user self-service UI that lets users create their own accounts with customizable criteria.                     | [Register a user](https://docs.pingidentity.com/pingam/8/user-self-service/uss-registering-users.html)                        |
| Password reset                             | End-user self-service UI for changing and resetting passwords based on predefined policies and security questions. | [Reset forgotten passwords](https://docs.pingidentity.com/pingam/8/user-self-service/uss-forgotten-password.html)             |
| Knowledge-based authentication             | Verification for user identities based on predefined and end user-created security questions.                      | [Configure knowledge-based security questions](https://docs.pingidentity.com/pingam/8/user-self-service/configuring-kba.html) |
| Forgotten username                         | Mechanisms to allow users to recover their usernames with predefined policies.                                     | [Retrieve forgotten usernames](https://docs.pingidentity.com/pingam/8/user-self-service/uss-forgotten-username.html)          |
| Progressive profile completion             | Short forms used to simplify registration and incrementally collect profile data over time.                        | [Profile Completeness Decision node](https://docs.pingidentity.com/auth-node-ref/8/profile-completeness-decision.html)        |
| Consent and preference management          | Configurable user preferences.                                                                                     | [Consent Collector node](https://docs.pingidentity.com/auth-node-ref/8/consent-collector.html)                                |
| Terms and conditions (or terms of service) | Verifies the user has accepted the active set of terms and conditions.                                             | [Terms and Conditions Decision node](https://docs.pingidentity.com/auth-node-ref/8/terms-and-conditions-decision.html)        |

## Workflow module

This module can be used to visually organize identity synchronization, reconciliation, and provisioning into repeatable processes with logging and auditing for reporting purposes.

Required modules: Self-Service, Identity Lifecycle, and Relationship.

| Feature                      | Description                                                                                                            | Documentation                                                                                                                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BPMN 2.0 support             | Standards-based Business Process Model and Notation 2.0 support.                                                       | [BPMN 2.0 and workflow tools](https://docs.pingidentity.com/pingidm/8/workflow-guide/about-workflow-tools.html)                                                                                    |
| Flowable process engine      | Lightweight workflow and business process management platform.                                                         | [Enable workflows](https://docs.pingidentity.com/pingidm/8/workflow-guide/enable-workflows.html)                                                                                                   |
| Workflow-driven provisioning | Define provisioning workflows for self-service, sunrise and sunset processes, approvals, escalations, and maintenance. | [Create workflows](https://docs.pingidentity.com/pingidm/8//workflow-guide/create-workflow.html), [Invoke workflows](https://docs.pingidentity.com/pingidm/8//workflow-guide/invoke-workflow.html) |

## Social Identity module

With this module, you can allow users to register and authenticate with specified standards-compliant social identity providers. These users can also link multiple social identity providers to the same account, establishing a single consumer identity.

With the attributes collected from each user profile, you can configure the module to authorize access to applications and resources, including lead generation tools.

Required modules: Self-Service, Identity Lifecycle, Intelligent Access, and Relationship.

| Feature        | Description                    | Documentation                                                                                                 |
| -------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Authentication | Social registration and login. | [Social authentication](https://docs.pingidentity.com/pingam/8/authentication-guide/social-registration.html) |

## Identity Lifecycle and Relationship module

This module can help you to provision user identities into PingIDM, and includes the capability to manage roles, relationships between identities, and entitlements.

Required modules: none.

| Feature                                    | Description                                                                                                                                 | Documentation                                                                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Inbound provisioning engine                | Provisioning engine to import data from an external resource into PingIDM.                                                                  | [Synchronization](https://docs.pingidentity.com/pingidm/8/synchronization-guide)                                               |
| Data modeling                              | Ability to map PingIDM objects to tables in a JDBC database or to organizational units in a PingDS repository.                              | [Object mappings](https://docs.pingidentity.com/pingidm/8/objects-guide/explicit-generic-mapping.html)                         |
| Identity lifecycle management              | An extensible object model that enables you to manage the complete lifecycle of identity objects.                                           | [Managed objects](https://docs.pingidentity.com/pingidm/8/objects-guide/managed-objects.html)                                  |
| Identity relationship lifecycle management | Ability to create and track relationship references between objects.                                                                        | [Relationships between objects](https://docs.pingidentity.com/pingidm/8/objects-guide/relationships.html)                      |
| Role lifecycle management                  | Provisioning roles to control how objects are exported to external systems and authorization roles to control authorization within PingIDM. | [Roles](https://docs.pingidentity.com/pingidm/8/objects-guide/roles.html)                                                      |
| Entitlement lifecycle management           | Entitlements to provision attributes or sets of attributes, based on role membership.                                                       | [Use assignments to provision users](https://docs.pingidentity.com/pingidm/8/objects-guide/working-with-role-assignments.html) |
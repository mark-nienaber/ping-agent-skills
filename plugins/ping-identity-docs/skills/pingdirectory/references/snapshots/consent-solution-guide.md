---
title: Authentication methods
description: The Consent Service supports the following HTTP authentication methods and the use of token validators for authorization.
component: pingdirectory
version: 11.1
page_id: pingdirectory:consent_solution_guide:pd_cs_authn_methods
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/consent_solution_guide/pd_cs_authn_methods.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  supported-http-authentication-methods: Supported HTTP authentication methods
  configuring-token-validators: Configuring token validators
---

# Authentication methods

The Consent Service supports the following HTTP authentication methods and the use of token validators for authorization.

## Supported HTTP authentication methods

The Consent Service supports the following HTTP authentication methods that are enabled by default:

* Basic authentication

  With basic authentication, the client provides an encoded username-password pair in the HTTP Authorization request header. When the Consent Service receives a request using basic authentication, it maps the username credential to a distinguished name (DN) using an identity mapper. This DN is designated the `auth DN` and is used to make subsequent authorization decisions. The Consent Service then performs an Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
  \<p>An open, cross platform protocol used for interacting with directory services.\</p>
  \</div>)* bind using the DN and password to determine if the request can be processed.

* Bearer token authentication

  With bearer token authentication, the client provides an access token *(tooltip: \<div class="paragraph">
  \<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
  \</div>)* in the HTTP Authorization request header. The access token is always obtained by the client from an external OAuth 2 authorization server and encapsulates information "claims" about a user identity, the client identity, and the requests that the client is authorized to make.

The Consent servlet looks at the request's Authorization header to determine which authentication type is being used by the client.

## Configuring token validators

The PingDirectory server must be configured to accept access tokens using one or both of the following access token validators:

* PingFederate access token validator

  Supports access tokens issued by a PingFederate authorization server. This validator verifies an access token and discovers its claims by making a request to the PingFederate server's token introspection endpoint.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are using PingFederate 10.0 or earlier, ensure that PingFederate is configured to respond to OAuth and OpenID Connect (OIDC) requests by selecting the checkboxes mentioned in steps 2 and 3 in [Enabling the OAuth AS role](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-100.pdf) in the PingFederate documentation.Starting with PingFederate 10.1, these items are always enabled. |

* JWT access token validator

  Supports signed or encrypted JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
  \<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
  \</div>)* access tokens issued by an arbitrary authorization server. This validator checks an access token by cryptographically verifying the token's signature using a trusted public certificate. The token's claims are encoded in the token itself, so discovering the token's claims does not require an outgoing token introspection request.

The token validator uses its identity mapper to map the subject claim to a DN. This DN is designated the `auth DN` and is used along with the token's claims to make subsequent authorization decisions.

If the PingDirectory server is configured with at least one access token validator, the Consent Service uses this access token validator. If the PingDirectory server is configured with more than one access token validator, the validators are consulted in order until one is able to successfully authenticate the request. If the PingDirectory server is configured with multiple access token validators, but only one should be used by the Consent Service, the access token validator can be configured by setting the `access-token-validator` property of the Consent HTTP Servlet Extension.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Configuring an access token validator for the Consent Service requires the following from the authorization server configuration:- The values that the authorization server sets for `subject` claims must be mappable to a DN in the PingDirectory server.

- The authorization server must be configured to authorize clients and grant scopes appropriately for privileged or unprivileged Consent API access.

- The authorization server must be configured to issue tokens with scopes corresponding to the Consent Service's `unprivileged-scope-name` and `privileged-scope-name` configuration.See the authorization server's documentation for guidance. |

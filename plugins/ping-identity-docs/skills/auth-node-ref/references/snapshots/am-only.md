---
title: Amster Jwt Decision node
description: Configure the Amster JWT Decision node to authenticate Amster connections to PingAM using SSH key pairs stored in an authorized_keys file.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:amster-jwt-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/amster-jwt-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Amster"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# Amster Jwt Decision node

The Amster Jwt Decision node lets AM authenticate Amster connections using SSH keys.

The Amster client signs the JWT using a local private key. AM verifies the signature using the list of public keys in the `authorized_keys` file. Specify the path to the `authorized_keys` file in the node configuration.

If the entry in the authorized keys file contains a `from` parameter, only connections originating from a qualifying host are permitted.

Find more information in [Private key connections](https://docs.pingidentity.com/pingam/8.1/amster/connect-am.html#private-login).

## Example

This node is used only by the `amsterService` authentication tree:

![journey amster service](_images/journey-amster-service.png)

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | Changing or removing this tree could prevent Amster from connecting to AM. |

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

The node reads the `NONCE_STATE_KEY` from the Amster client.

## Dependencies

This node has no dependencies.

## Configuration

| Property        | Usage                                                                                                                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authorized Keys | Location of the `authorized_keys` file used to validate remote Amster connections.This file has the same format as an [OpenSSH `authorized_keys`](https://www.ssh.com/academy/ssh/authorized-keys-openssh) file. |

## Outputs

This node doesn't change the shared state.

## Outcomes

* True

  The journey follows this outcome if the node can validate the incoming private key against the public keys in the `authentication_keys` file. Successful authentication creates an `amAdmin` session in AM.

* False

  The journey follows this outcome if the node can't validate the incoming private key against the public keys in the `authentication_keys` file, either because the incoming key is invalid, or because the `authentication_keys` file is inaccessible.

## Errors

If the node can't read the `authorized_keys` file, it returns the error `AmsterJwtDecisionNode: Could not read authorized keys file filename`.

---

---
title: Create Password node (deprecated)
description: Deprecated. The Create Password node prompted users to create a password during social account provisioning in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:create-password
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/create-password.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Passwords", "Social Authentication", "Social Registration", "Social Identity", "Provisioning"]
page_aliases: ["auth-node-create-password.adoc"]
section_ids:
  example: Example
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# Create Password node (deprecated)

Lets users create a password when provisioning an account.

|   |                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This node and its related services are deprecated.Find information on the current methods for implementing social authentication in [PingGateway](https://docs.pingidentity.com/pinggateway/2026/gateway-guide/preface.html). |

Social identity providers do not provide a user's password. Use this node to provide a password to complete the user's credentials before provisioning an account.

|   |                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The flow must provision an account after prompting the user for a password, for example, by using the [Provision Dynamic Account node](provision-dynamic-account.html). If no account is provisioned, the flow does not save the password.Do not place any nodes that request additional input from the user between this node and the provisioning node; otherwise, the password is lost. |

## Example

The following example lets users who have performed social authentication using Google provide a password and provision an account when they don't have one. They must enter a one-time passcode to verify they are the owner of the Google account.

![The Create Password node in context](_images/trees-node-Google-DynamicAccountCreation-example.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | No         |

## Outcomes

Single outcome path.

## Configuration

| Property          | Usage                                                       |
| ----------------- | ----------------------------------------------------------- |
| minPasswordLength | The minimum number of characters the password must contain. |

---

---
title: Debug node
description: Use the Debug node in PingAM to display shared node state, identity universalId, and transaction ID during authentication tree testing.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:debug
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/debug.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication"]
page_aliases: ["auth-node-debug.adoc"]
section_ids:
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# Debug node

Displays debug information about the current authentication tree.

This node collects information, such as the shared node state, the identity object's `universalId`, and the transaction ID, which are useful for reference in log messages.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | No         |

## Outcomes

Single outcome path.

## Configuration

| Property           | Usage                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------- |
| Enable Debug Popup | If enabled, a popup window displays debug logs as you step through the flow in a browser. |

---

---
title: OAuth 2.0 node (deprecated)
description: Deprecated. The OAuth 2.0 node authenticated PingAM users against OAuth 2.0-compliant social identity providers using the authorization code grant.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:oauth2
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/oauth2.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "OAuth 2.0", "Social Authentication"]
page_aliases: ["auth-node-oauth2.adoc"]
section_ids:
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# OAuth 2.0 node (deprecated)

Lets AM authenticate users of OAuth 2.0-compliant resource servers.

References in this section are to RFC 6749, [The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/info/rfc6749).

|   |                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This node and its related services are deprecated.Find information on the current methods for implementing social authentication in [PingGateway](https://docs.pingidentity.com/pinggateway/2026/gateway-guide/preface.html). |

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | No         |

## Outcomes

* `Account Exists`

* `No account Exists`

Evaluation continues along the `Account Exists` path if an account matching the attributes retrieved from the social identity provider is found in the user data store; otherwise, evaluation continues along the `No account exists` path.

## Configuration

| Property                                 | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client ID *(required)*                   | Specifies the `client_id` parameter as described in [section 2.2 of The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749.html#section-2.2).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Client Secret *(required)*               | Specifies the `client_secret` parameter as described in [section 2.3 of The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749.html#section-2.3).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Authentication Endpoint URL *(required)* | Specifies the URL to the social provider's endpoint handling authentication as described in [section 3.1 of The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749#section-3.1).Example: `https://accounts.google.com/o/oauth2/v2/auth`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Access Token Endpoint URL *(required)*   | Specifies the URL to the endpoint handling access tokens as described in [section 3.2 of The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.2).Example: `https://www.googleapis.com/oauth2/v4/token`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| User Profile Service URL *(required)*    | Specifies the user profile URL that returns profile information.Example: `https://www.googleapis.com/oauth2/v3/userinfo`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| OAuth Scope *(required)*                 | Specifies a list of user profile attributes that the client application requires, according to [The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/info/rfc6749).Ensure you use the correct scope delimiter required by the identity provider, including commas or spaces.The list depends on the permissions that the resource owner, such as the end user, grants to the client application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Scope Delimiter *(required)*             | Specifies the delimiter used to separate scope values.Some authorization servers use non-standard separators for scopes, for example commas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Redirect URL *(required)*                | Specifies the URL the user is redirected to by the social identity provider after authenticating.For authentication trees in AM, set this property to the URL of the UI. For example, `https://am.example.com:8443/am/XUI/`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Social Provider *(required)*             | Specifies the name of the social provider for which this module is being set up.Example: `Google`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Auth ID Key *(required)*                 | Specifies the attribute the social identity provider uses to identify an authenticated individual.Example: `id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Use Basic Auth                           | Specifies that the client uses HTTP Basic authentication when authenticating to the social provider.Default: `true`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Account Provider *(required)*            | Specifies the name of the class that implements the account provider.Default: `org.forgerock.openam.authentication.modules.common.mapping.DefaultAccountProvider`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Account Mapper *(required)*              | Specifies the name of the class that implements the method of locating local accounts based on the attributes returned from the social identity provider.Provided implementations are:`org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper`The Account Mapper classes can take two constructor parameters:1) A comma-separated list of attributes

2) A prefix to apply to their values.For example, to prefix all received property values with `facebook-` before searching, specify:```
org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper|*|facebook-
```                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Attribute Mapper *(required)*            | Specifies the list of fully qualified class names for implementations that map attributes from the OAuth 2.0 authorization server to AM profile attributes.Provided implementations are:`org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper`The Attribute Mapper classes can take two constructor parameters to help differentiate between the providers:1) A comma-separated list of attributes

2) A prefix to apply to their values.For example, to prefix all incoming values with `facebook-`, specify:```
org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper|*|facebook-
```To prefix all incoming values use an asterisk (`*`) as the attribute list. This prefixes all values, including email addresses, postal addresses, and so on.                                                                                                                                                                                                                                                                 |
| Account Mapper Configuration             | Specifies the attribute configuration used to map the account of the user authenticated in the OAuth 2.0 provider to the local data store in AM.Valid values are in the form `provider-attr=local-attr`.Examples:```
email=mail
id=facebook-id
```&#xA;&#xA;When using the org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper class, you can parse JSON objects in mappings using dot notation.&#xA;&#xA;For example, given a JSON payload of:&#xA;&#xA;{&#xA;  "sub" : "12345",&#xA;  "name" : {&#xA;    "first\_name" : "Demo",&#xA;    "last\_name" : "User"&#xA;  }&#xA;}&#xA;&#xA;You can create a mapper, such as name.first\_name=cn.                                                                                                                                                                                                                                                                                                                                                                                               |
| Attribute Mapper Configuration           | Map of OAuth 2.0 provider user account attributes to local user profile attributes, with values in the form `provider-attr=local-attr`.Examples:```
first_name=givenname
last_name=sn
name=cn
email=mail
id=facebook-id
first_name=facebook-fname
last_name=facebook-lname
email=facebook-email
```&#xA;&#xA;When using the org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper class, you can parse JSON objects in mappings using dot notation.&#xA;&#xA;For example, given a JSON payload of:&#xA;&#xA;{&#xA;  "sub" : "12345",&#xA;  "name" : {&#xA;    "first\_name" : "Demo",&#xA;    "last\_name" : "User"&#xA;  }&#xA;}&#xA;&#xA;You can create a mapper, such as name.first\_name=cn.                                                                                                                                                                                                                                                                                                                                              |
| Save attributes in the session           | When enabled, saves the attributes in the Attribute Mapper Configuration field to the AM session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| OAuth 2.0 Mix-Up Mitigation Enabled      | Controls whether the OAuth 2.0 authentication node carries out additional verification steps when it receives the authorization code from the authorization server.Specifies that the client must compare the issuer identifier of the authorization server upon registration with the issuer value returned as the `iss` response parameter. If they do not match, the client must abort the authorization process. The client must also confirm that the authorization server's response is intended for the client by comparing the client's client identifier to the value of the `client_id` response parameter.When this is enabled, set the Token Issuer property so that the validation can succeed. The authorization code response contains an issuer value (`iss`) for the client to validate.&#xA;&#xA;Refer to the authorization server's documentation for the value it uses for the issuer field.Learn more in [section 4 of OAuth 2.0 Mix-Up Mitigation Draft](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-mix-up-mitigation-01#section-4). |
| Token Issuer                             | Corresponds to the expected issuer identifier value in the `iss` field of the ID token.Example: `https://accounts.google.com`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

---

---
title: OpenID Connect node (deprecated)
description: Deprecated. The OpenID Connect node authenticated PingAM users against OpenID Connect providers using the authorization code grant.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:oidc
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/oidc.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "OpenID Connect (OIDC)", "OAuth 2.0", "Social Authentication", "Authorization", "Account"]
page_aliases: ["auth-node-oidc.adoc"]
section_ids:
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# OpenID Connect node (deprecated)

Lets AM authenticate users of OpenID Connect-compliant resource servers.

As OpenID Connect is an additional layer on top of OAuth 2.0, described in RFC 6749, [The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/info/rfc6749). OpenID Connect is described in the [OpenID Connect Core 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-core-1_0.html) specification.

|   |                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This node and its related services are deprecated.Find information on the current methods for implementing social authentication in [PingGateway](https://docs.pingidentity.com/pinggateway/2026/gateway-guide/preface.html). |

The OpenID Connect node implements the [Authorization code grant](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-authz-grant.html).

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | No         |

## Outcomes

* `Account Exists`

* `No account Exists`

Evaluation continues along the `Account Exists` path if an account matching the attributes retrieved from the OpenID Connect identity provider is found in the identity store; otherwise, evaluation continues along the `No account exists` path.

## Configuration

| Property                                    | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Client ID *(required)*                      | Specifies the `client_id` parameter as described in [section 2.2 of The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749.html#section-2.2).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Client Secret *(required)*                  | Specifies the `client_secret` parameter as described in [section 2.3 of The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749.html#section-2.3).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Authentication Endpoint URL *(required)*    | Specifies the URL to the social provider's endpoint handling authentication as described in [section 3.1 of The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/info/rfc6749#section-3.1).Example: `https://accounts.google.com/o/oauth2/v2/auth`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Access Token Endpoint URL *(required)*      | Specifies the URL to the endpoint handling access tokens as described in [section 3.2 of The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.2).Example: `https://www.googleapis.com/oauth2/v4/token`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| User Profile Service URL *(required)*       | Specifies the user profile URL that returns profile information.If not specified, attributes are mapped from the claims returned by the `id_token`, and no call to a user profile endpoint is made.Example: `https://www.googleapis.com/oauth2/v3/userinfo`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| OAuth Scope                                 | Specifies a list of user profile attributes that the client application requires, according to [The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/info/rfc6749).Ensure you use the correct scope delimiter required by the identity provider, including commas or spaces.The list depends on the permissions that the resource owner, such as the end user, grants to the client application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Redirect URL                                | Specifies the URL the user is redirected to by the social identity provider after authenticating.For authentication trees in AM, set this property to the URL of the UI. For example, `https://am.example.com:8443/am/XUI/`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Social Provider *(required)*                | Specifies the name of the OpenID Connect provider for which this node is being set up.Example: `Google`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Auth ID Key                                 | Specifies the attribute the social identity provider uses to identify an authenticated individual.Example: `sub`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Use Basic Auth                              | Specifies that the client uses HTTP Basic authentication when authenticating to the social provider.Default: `true`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Account Provider                            | Specifies the name of the class that implements the account provider.Default: `org.forgerock.openam.authentication.modules.common.mapping.DefaultAccountProvider`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Account Mapper                              | Specifies the name of the class that implements the method of locating local accounts based on the attributes returned from the social identity provider.The provided implementations is `org.forgerock.openam.authentication.modules.oidc.JwtAttributeMapper`.The Account Mapper classes can take two constructor parameters:1) A comma-separated list of attributes

2) A prefix to apply to their values.For example, to prefix all received property values with `openid-` before searching, specify:```
org.forgerock.openam.authentication.modules.oidc.JwtAttributeMapper|*|openid-
```                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Attribute Mapper                            | Specifies the list of fully qualified class names for implementations that map attributes from the authorization server to AM profile attributes.The provided implementations is `org.forgerock.openam.authentication.modules.oidc.JwtAttributeMapper`.The Attribute Mapper classes can take two constructor parameters to help differentiate between the providers:1) A comma-separated list of attributes

2) A prefix to apply to their values.For example, to prefix incoming `iplanet-am-user-alias-list` values with `openid-`, specify:```
org.forgerock.openam.authentication.modules.oidc.JwtAttributeMapper
```                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| iplanet-am-user-alias-list                  | openid-To prefix all incoming values use an asterisk (`*`) as the attribute list. This prefixes all values, including email addresses, postal addresses, and so on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Account Mapper Configuration                | Specifies the attribute configuration used to map the account of the user authenticated in the provider to the local identity store in AM.To add a mapping, specify the name of the provider attribute as the key, and the local attribute to map to as the value.For example, click Add, then specify `sub` in the Key field and `iplanet-am-user-alias-list` in the Value field, and click [icon: plus, set=fa].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Attribute Mapper Configuration              | Specifies how to map provider user attributes to local user profile attributes.To add a mapping, specify the name of the provider attribute as the Key, and the local attribute to map to as the Value.For example, click Add, then specify `id` in the Key field and `facebook-id` in the Value field, and click [icon: plus, set=fa].Examples:```
first_name=givenname
last_name=sn
name=cn
email=mail
id=facebook-id
first_name=facebook-fname
last_name=facebook-lname
email=facebook-email
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Save attributes in the session              | When enabled, saves the attributes in the Attribute Mapper Configuration field to the AM session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| OAuth 2.0 Mix-Up Mitigation Enabled         | Controls whether the authentication node carries out additional verification steps when it receives the authorization code from the authorization server.Specifies that the client must compare the issuer identifier of the authorization server upon registration with the issuer value returned as the `iss` response parameter. If they do not match, the client must abort the authorization process. The client must also confirm that the authorization server's response is intended for the client by comparing the client's client identifier to the value of the `client_id` response parameter.When this is enabled, set the Token Issuer property so that the validation can succeed. The authorization code response contains an issuer value (`iss`) for the client to validate.&#xA;&#xA;Refer to the authorization server's documentation for the value it uses for the issuer field.Learn more in [section 4 of OAuth 2.0 Mix-Up Mitigation Draft](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-mix-up-mitigation-01#section-4). |
| Token Issuer *(required)*                   | Corresponds to the expected issuer identifier value in the `iss` field of the ID token.Example: `https://accounts.google.com`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| OpenID Connect Validation Type *(required)* | Specifies how to validate the ID token received from the OpenID Connect provider.This ignores keys specified in JWT headers, such as `jku` and `jwe`.The following options are available to validate an incoming OpenID Connect ID token:- `Well Known URL` (Default)

  Retrieves the provider's keys based on the information provided in its OpenID Connect configuration URL.

  Specify the provider's configuration URL in the OpenID Connect Validation Value field; for example, `https://accounts.google.com/.well-known/openid-configuration`.

- `Client Secret`

  Validates the ID token signature with a specified client secret key.

  Specify the key to use in the OpenID Connect Validation Value field.

- `JWK URL`

  Retrieve the necessary JSON web key from the URL that you specify.

  Specify the provider's JWK URI in the OpenID Connect Validation Value field; for example, `https://www.googleapis.com/oauth2/v3/certs`.                                                                                                    |
| OpenID Connect Validation Value             | Provide the URL or secret key used to verify an incoming ID token, depending on the value selected in the OpenID Connect Validation Type property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

---

---
title: Password Collector node
description: Use the Password Collector node in PingAM to prompt users to enter their password and write it to transient state for use later in the journey.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:password-collector
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/password-collector.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Password"]
page_aliases: ["auth-node-password-collector.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
  errors: Errors
---

# Password Collector node

The Password Collector node prompts the user to enter their password.

## Example

This simple login journey demonstrates the Password Collector.

![Simple login journey](../_images/simple-login-journey.png)

a The [Username Collector node](username-collector.html) node prompts the user to enter their username.

b The [Password Collector node](password-collector.html) node prompts the user to enter their password.

c The [Data Store Decision node](../data-store-decision.html) locates the user in the backend identity store and determines if the credentials are correct:

* If the credentials are correct, the journey follows the succcess outcome and the user is authenticated.

* If the credentials aren't correct, the node directs the user to the [Retry Limit Decision node](../retry-limit-decision.html).

d The [Retry Limit Decision node](../retry-limit-decision.html) determines how many times the user has attempted these credentials:

* If the number of attempts doesn't exceed the maximum, the user is redirected to the [Username Collector node](username-collector.html) to attempt their credentials again.

* If the number of attempts exceeds the maximum, the journey follows the failure outcome.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | No         |

## Inputs

None. This node doesn't read shared state data.

## Dependencies

This node has no dependencies.

## Configuration

This node has no configurable properties.

## Outputs

The node writes the captured `password` to transient state. This persists only until the authentication flow reaches the next node requiring user interaction.

## Callbacks

The node sends a [PasswordCallback](https://docs.pingidentity.com/pingam/8.1/am-authentication/callbacks-interactive.html#PasswordCallback), which prompts the user to enter their password.

## Outcomes

Single outcome path.

Evaluation continues after capturing the password.

## Errors

This node doesn't log any error or warning messages of its own.

---

---
title: Provision Dynamic Account node
description: Use the Provision Dynamic Account node in PingAM to create a user account after SAML2 or social authentication using attributes from the identity provider.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:provision-dynamic-account
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/provision-dynamic-account.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["auth-node-provision-dynamic-account.adoc"]
section_ids:
  example: Example
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# Provision Dynamic Account node

Provision an account following successful authentication by a SAML2 authentication node or the [Social Provider Handler node](../social-provider-handler.html).

Accounts are provisioned using properties defined in the attribute mapper configuration of a social authentication or SAML2 authentication node earlier in the flow.

If a password has been acquired from the user, for example, by using the [Platform Password node](../platform-password.html), it is used when provisioning the account; otherwise, a 20-character random string is used.

In addition to retrieving the password from the node state, the [Provision Dynamic Account node](provision-dynamic-account.html) gets the `realm` value, and `attributes` and `userNames` from `userInfo` in the shared state. It sets the `username` attribute in the node's shared state.

## Example

In this example, the node lets users who have performed social authentication using Google provide a password and provision an account if they don't have a matching existing profile. They must enter a one-time passcode to verify they are the owner of the Google account.

![Dynamic account provisioning in context](_images/trees-node-Google-DynamicAccountCreation-example.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | No         |

## Outcomes

Single outcome path.

## Configuration

| Property         | Usage                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account Provider | Specifies the name of the class that implements the account provider.Default: `org.forgerock.openam.authentication.modules.common.mapping.DefaultAccountProvider` |

---

---
title: Provision IDM Account node (deprecated)
description: Deprecated. The Provision IDM Account node redirected users to a PingIDM instance to provision an account after social authentication in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:provision-IDM-account
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/provision-IDM-account.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Social Authentication", "Account"]
page_aliases: ["auth-node-provision-IDM-account.adoc"]
section_ids:
  example: Example
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# Provision IDM Account node (deprecated)

Redirects users to an IDM instance to provision an account.

|   |                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This node and its related services are deprecated.Find information on the current methods for implementing social authentication in [PingGateway](https://docs.pingidentity.com/pinggateway/2026/gateway-guide/preface.html). |

Ensure you configured the details of the IDM instance in AM, by navigating to Configure > Global Services > IDM Provisioning.

## Example

In this example, the node lets users who have performed social authentication with Facebook provide a password and provision an account if they don't have a matching existing profile:

![IDM account provisioning in context](_images/trees-node-Facebook-ProvisionIDMAccount-example.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | No         |

## Outcomes

Single outcome path.

## Configuration

| Property         | Usage                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account Provider | Specifies the name of the class that implements the account provider.Default: `org.forgerock.openam.authentication.modules.common.mapping.DefaultAccountProvider` |

---

---
title: Social Facebook node (deprecated)
description: Deprecated. The Social Facebook node authenticated PingAM users with Facebook using OAuth 2.0, preconfigured with Facebook endpoints.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:social-facebook
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/social-facebook.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "OAuth 2.0", "Social Authentication", "Account"]
page_aliases: ["auth-node-social-facebook.adoc"]
section_ids:
  example: Example
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# Social Facebook node (deprecated)

This node duplicates the [OAuth 2.0 node (deprecated)](oauth2.html) but is preconfigured to work with Facebook. You specify only the `Client ID` and `Client Secret`.

|   |                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This node and its related services are deprecated.Find information on the current methods for implementing social authentication in [PingGateway](https://docs.pingidentity.com/pinggateway/2026/gateway-guide/preface.html). |

## Example

The following example shows the node in context:

![Provisioning an account after social authentication](_images/trees-node-Facebook-ProvisionIDMAccount-example.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | No         |

## Outcomes

* `Account exists`

* `No account exists`

Evaluation continues along the `Account Exists` path if an account matching the attributes retrieved from Facebook are found in the user data store; otherwise, evaluation continues along the `No account exists` path.

## Configuration

| Property                            | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client ID                           | Specifies the `client_id` parameter as provided by Facebook.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Client Secret                       | Specifies the `client_secret` parameter as provided by Facebook.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Authentication Endpoint URL         | Specifies the URL to the social provider's endpoint handling authentication as described in [section 3.1 of The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.1).Default: `https://www.facebook.com/dialog/oauth`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Access Token Endpoint URL           | Specifies the URL to the endpoint handling access tokens as described in [section 3.2 of The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.2).Default: `https://graph.facebook.com/v2.12/oauth/access_token`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| User Profile Service URL            | Specifies the user profile URL that returns profile information.Default: `https://graph.facebook.com/v2.6/me?fields=name%2Cemail%2Cfirst_name%2Clast_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| OAuth Scope                         | Specifies a comma-separated list of user profile attributes the client application requires, according to [The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/info/rfc6749). The list depends on the permissions the resource owner, such as the end user, grants to the client application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Redirect URL                        | Specifies the URL the user is redirected to by Facebook after authenticating to continue the flow\.Set this property to the URL of the AM UI. For example, `https://am.example.com:8443/am/XUI/`.&#xA;&#xA;If the tree is not in the Top Level Realm, you can specify the realm in the redirect URL. Use a DNS alias for the realm, or add the realm as a query parameter, for example, https\://am.example.com:8443/am/XUI/?realm=/mySubRealm.&#xA;&#xA;Learn more in Configure DNS aliases to access a realm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Social Provider                     | Specifies the name of the social provider for which this node is being set up.Default: `facebook`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Auth ID Key                         | Specifies the attribute the social identity provider uses to identify an authenticated individual.Default: `id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Use Basic Auth                      | Specifies that the client uses HTTP Basic authentication when authenticating to the social provider.Default: `true`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Account Provider                    | Specifies the name of the class that implements the account provider.Default: `org.forgerock.openam.authentication.modules.common.mapping.DefaultAccountProvider`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Account Mapper                      | Specifies the name of the class that implements the method of locating local accounts based on the attributes returned from Facebook.Default: `org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Attribute Mapper                    | Specifies the list of fully qualified class names for implementations that map attributes from Facebook to AM profile attributes.Default: `org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper\|uid\|facebook-`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Account Mapper Configuration        | Specifies the attribute configuration used to map the account of the user authenticated in the Social Facebook provider to the local data store in AM. Valid values are in the form `provider-attr=local-attr`.Default: `id=uid`.&#xA;&#xA;When using the org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper class, you can parse JSON objects in mappings using dot notation.&#xA;&#xA;For example, given a JSON payload of:&#xA;&#xA;{&#xA;  "sub" : "12345",&#xA;  "name" : {&#xA;    "first\_name" : "Demo",&#xA;    "last\_name" : "User"&#xA;  }&#xA;}&#xA;&#xA;You can create a mapper, such as name.first\_name=cn.                                                                                                                                                                                                                                                                                                                                              |
| Attribute Mapper Configuration      | Map of Facebook user account attributes to local user profile attributes, with values in the form `provider-attr=local-attr`.Default: `name=cn`, `last_name=sn`, `id=uid`, `first_name=givenname`, `email=mail`.&#xA;&#xA;When using the org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper class, you can parse JSON objects in mappings using dot notation.&#xA;&#xA;For example, given a JSON payload of:&#xA;&#xA;{&#xA;  "sub" : "12345",&#xA;  "name" : {&#xA;    "first\_name" : "Demo",&#xA;    "last\_name" : "User"&#xA;  }&#xA;}&#xA;&#xA;You can create a mapper, such as name.first\_name=cn.                                                                                                                                                                                                                                                                                                                                                               |
| Save attributes in the session      | When enabled, saves the attributes in the Attribute Mapper Configuration field to the AM session.Default: `true`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| OAuth 2.0 Mix-Up Mitigation Enabled | Controls whether the authentication node carries out additional verification steps when it receives the authorization code from the authorization server.Specifies that the client must compare the issuer identifier of the authorization server upon registration with the issuer value returned as the `iss` response parameter. If they do not match, the client must abort the authorization process. The client must also confirm that the authorization server's response is intended for the client by comparing the client's client identifier to the value of the `client_id` response parameter.The Token Issuer property must be entered when the OAuth 2.0 Mix-Up Mitigation feature is enabled, so that the validation can succeed. The authorization code response contains an issuer value (`iss`) for the client to validate.Learn more in [section 4 of OAuth 2.0 Mix-Up Mitigation Draft](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-mix-up-mitigation-01#section-4). |
| Token Issuer                        | Corresponds to the expected issuer identifier value in the `iss` field of the ID token.Example: `https://graph.facebook.com`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

---

---
title: Social Google node (deprecated)
description: Deprecated. The Social Google node authenticated PingAM users with Google using OAuth 2.0, preconfigured with Google endpoints.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:social-google
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/social-google.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "OAuth 2.0", "Social Authentication", "Account"]
page_aliases: ["auth-node-social-google.adoc"]
section_ids:
  example: Example
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# Social Google node (deprecated)

This node duplicates the [OAuth 2.0 node (deprecated)](oauth2.html), but is preconfigured to work with Google. You specify only the `Client ID` and `Client Secret`.

|   |                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This node and its related services are deprecated.Find information on the current methods for implementing social authentication in [PingGateway](https://docs.pingidentity.com/pinggateway/2026/gateway-guide/preface.html). |

## Example

The following example shows the node in context:

![Anonymous user mapping after social authentication](_images/trees-node-Google-AnonymousUser-example.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | No         |

## Outcomes

* `Account exists`

* `No account exists`

Evaluation continues along the `Account Exists` path if an account matching the attributes retrieved from Google are found in the user data store; otherwise, evaluation continues along the `No account exists` path.

## Configuration

| Property                            | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client ID *(required)*              | Specifies the `client_id` parameter as provided by Google.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Client Secret *(required)*          | Specifies the `client_secret` parameter as provided by Google.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Authentication Endpoint URL         | Specifies the URL to the social provider's endpoint handling authentication as described in [section 3.1 of The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.1).Default: `https://accounts.google.com/o/oauth2/v2/auth`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Access Token Endpoint URL           | Specifies the URL to the endpoint handling access tokens as described in [section 3.2 of The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.2).Default: `https://www.googleapis.com/oauth2/v4/token`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| User Profile Service URL            | Specifies the user profile URL that returns profile information.Default: `https://www.googleapis.com/oauth2/v3/userinfo`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| OAuth Scope                         | Specifies a space-separated list of user profile attributes the client application requires, according to [The OAuth 2.0 Authorization Framework (RFC 6749)](https://www.rfc-editor.org/info/rfc6749). The list depends on the permissions the resource owner, such as the end user, grants to the client application.Default: `profile email`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Redirect URL                        | Specifies the URL the user is redirected to by Google after authenticating to continue the flow\.Set this property to the URL of the AM UI. For example, `https://am.example.com:8443/am/XUI/`.&#xA;&#xA;If the tree is not in the Top Level Realm, you can specify the realm in the redirect URL. Use a DNS alias for the realm, or add the realm as a query parameter; for example, https\://am.example.com:8443/am/XUI/?realm=/mySubRealm.&#xA;&#xA;Learn more in Configure DNS aliases to access a realm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Social Provider                     | Specifies the name of the social provider for which this node is being set up.Default: `google`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Auth ID Key                         | Specifies the attribute the social identity provider uses to identify an authenticated individual.Default: `sub`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Use Basic Auth                      | Specifies that the client uses HTTP Basic authentication when authenticating to Google.Default: `true`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Account Provider                    | Specifies the name of the class that implements the account provider.Default: `org.forgerock.openam.authentication.modules.common.mapping.DefaultAccountProvider`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Account Mapper                      | Specifies the name of the class that implements the method of locating local accounts based on the attributes returned from Google.Default: `org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Attribute Mapper                    | Specifies the list of fully qualified class names for implementations that map attributes from Google to AM profile attributes.Default: `org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper\|iplanet-am-user-alias-list\|google-`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Account Mapper Configuration        | Specifies the attribute configuration used to map the account of the user authenticated in the Social Google provider to the local data store in AM. Valid values are in the form `provider-attr=local-attr`.Default: `sub=uid`.&#xA;&#xA;When using the org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper class, you can parse JSON objects in mappings using dot notation.&#xA;&#xA;For example, given a JSON payload of:&#xA;&#xA;{&#xA;  "sub" : "12345",&#xA;  "name" : {&#xA;    "first\_name" : "Demo",&#xA;    "last\_name" : "User"&#xA;  }&#xA;}&#xA;&#xA;You can create a mapper, such as name.first\_name=cn.                                                                                                                                                                                                                                                                                                                                               |
| Attribute Mapper Configuration      | Map of Google user account attributes to local user profile attributes, with values in the form `provider-attr=local-attr`.Default: `sub=uid`, `name=cn`, `given_name=givenName`, `family_name=sn`, `email=mail`.&#xA;&#xA;When using the org.forgerock.openam.authentication.modules.common.mapping.JsonAttributeMapper class, you can parse JSON objects in mappings using dot notation.&#xA;&#xA;For example, given a JSON payload of:&#xA;&#xA;{&#xA;  "sub" : "12345",&#xA;  "name" : {&#xA;    "first\_name" : "Demo",&#xA;    "last\_name" : "User"&#xA;  }&#xA;}&#xA;&#xA;You can create a mapper, such as name.first\_name=cn.                                                                                                                                                                                                                                                                                                                                                              |
| Save attributes in the session      | When enabled, saves the attributes in the Attribute Mapper Configuration field to the AM session.Default: `true`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| OAuth 2.0 Mix-Up Mitigation Enabled | Controls whether the authentication node carries out additional verification steps when it receives the authorization code from the authorization server.Specifies that the client must compare the issuer identifier of the authorization server upon registration with the issuer value returned as the `iss` response parameter. If they do not match, the client must abort the authorization process. The client must also confirm that the authorization server's response is intended for the client by comparing the client's client identifier to the value of the `client_id` response parameter.The Token Issuer property must be entered when the OAuth 2.0 Mix-Up Mitigation feature is enabled, so that the validation can succeed. The authorization code response contains an issuer value (`iss`) for the client to validate.Learn more in [section 4 of OAuth 2.0 Mix-Up Mitigation Draft](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-mix-up-mitigation-01#section-4). |
| Token Issuer                        | Corresponds to the expected issuer identifier value in the `iss` field of the ID token.Example: `https://accounts.google.com`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

---

---
title: Social Ignore Profile node (deprecated)
description: Deprecated. The Social Ignore Profile node issued a PingAM SSO token after social authentication without checking for a local user profile.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:social-ignore-profile
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/social-ignore-profile.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Social Authentication", "Single Sign-on (SSO)"]
page_aliases: ["auth-node-social-ignore-profile.adoc"]
section_ids:
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# Social Ignore Profile node (deprecated)

Specifies whether to ignore a local user profile.

If evaluation flows through this node after successful social authentication, AM issues an SSO token regardless of whether a user profile exists in the data store. AM does not check for whether a user profile is present.

|   |                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This node and its related services are deprecated.Find information on the current methods for implementing social authentication in [PingGateway](https://docs.pingidentity.com/pinggateway/2026/gateway-guide/preface.html). |

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | No         |

## Outcomes

Single outcome path.

## Configuration

This node has no configurable properties.

---

---
title: Username Collector node
description: Use the Username Collector node in PingAM to prompt users to enter their username and write it to shared state for use later in the journey.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:am-only:username-collector
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/username-collector.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication"]
page_aliases: ["auth-node-username-collector.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
  errors: Errors
  changelog: Changelog
---

# Username Collector node

The Username Collector node prompts the user for their username.

## Example

This simple login journey demonstrates the Username Collector node.

![Simple login journey](../_images/simple-login-journey.png)

a The [Username Collector node](username-collector.html) node prompts the user to enter their username.

b The [Password Collector node](password-collector.html) node prompts the user to enter their password.

c The [Data Store Decision node](../data-store-decision.html) locates the user in the backend identity store and determines if the credentials are correct:

* If the credentials are correct, the journey follows the succcess outcome and the user is authenticated.

* If the credentials aren't correct, the node directs the user to the [Retry Limit Decision node](../retry-limit-decision.html).

d The [Retry Limit Decision node](../retry-limit-decision.html) determines how many times the user has attempted these credentials:

* If the number of attempts doesn't exceed the maximum, the user is redirected to the [Username Collector node](username-collector.html) to attempt their credentials again.

* If the number of attempts exceeds the maximum, the journey follows the failure outcome.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | No         |

## Inputs

* Version 1.0

  None. This node doesn't read shared state data.

* Version 2.0

  If the Prepopulate Username option is enabled, the node reads the `username` from the shared state, if it's available.

## Dependencies

This node has no dependencies.

## Configuration

| Property             | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Availability      |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Prepopulate Username | Whether the node should prepopulate the `username` if it's available in the shared state.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [v2.0](#v2)       |
| Autocomplete Values  | (Optional) Enter one or more autocomplete values. These values provide autofill suggestions to the user when they're prompted for their username. Make sure you only use standard autocomplete values that are defined in the [HTML specification](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete) to ensure browsers can recognize them and provide relevant suggestions.For example, if you enter `username`, users will see username suggestions based on the autofill data that's been saved in their browser.&#xA;&#xA;If you want users to see relevant passkeys as autofill suggestions when prompted for their username, make sure you:&#xA;&#xA;Include the username and webauthn autocomplete values in this order.&#xA;&#xA;Configure the WebAuthn Authentication node for passkey autofill. Learn more in Configure WebAuthn conditional UI. | All node versions |

## Outputs

The node writes the captured `username` to shared state.

## Callbacks

The node sends a [NameCallback](https://docs.pingidentity.com/pingam/8.1/am-authentication/callbacks-interactive.html#NameCallback) to prompt the user for their username.

## Outcomes

Single outcome path.

Evaluation continues after capturing the username.

## Errors

This node doesn't log any error or warning messages of its own.

## Changelog

| Version | Changes                                                    |
| ------- | ---------------------------------------------------------- |
| []()2.0 | Addition of the Prepopulate Username configuration option. |
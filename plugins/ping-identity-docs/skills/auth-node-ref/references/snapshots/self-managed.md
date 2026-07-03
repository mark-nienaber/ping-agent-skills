---
title: Authenticate Thing node
description: Use the Authenticate Thing node in PingAM to authenticate IoT devices and gateways using Proof of Possession JWT or Client Assertion.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:self-managed:authenticate-thing
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/self-managed/authenticate-thing.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Identity Store"]
page_aliases: ["self-managed/auth-node-authenticate-thing.adoc"]
section_ids:
  examples: Examples
  availability: Availability
  dependencies: Dependencies
  outcomes: Outcomes
  configuration: Configuration
---

# Authenticate Thing node

This node authenticates a *thing*. A thing represents an IoT device, service, or the [IoT Gateway](https://backstage.forgerock.com/docs/iot/7.4/evaluation-guide/about-iot.html#about-fr-things).

## Examples

The following example shows how to authenticate a thing when the identity already exists in the identity store and when its profile contains a confirmation key:

![trees-node-authenticate-thing-example1](_images/trees-node-authenticate-thing-example1.png)

The following example shows how to authenticate a thing when the identity does not exist, or when it needs to refresh its confirmation key:

![trees-node-authenticate-thing-example2](_images/trees-node-authenticate-thing-example2.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Dependencies

Before you configure this node, you must configure the [IoT service](https://docs.pingidentity.com/pingam/8.1/setup/services-configuration.html#global-iot) for the realm.

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Support for this node is provided by the [IoT SDK](https://backstage.forgerock.com/docs/iot/7.4/evaluation-guide/about-iot.html#about-fr-things). |

The node supports two methods of authentication:

1. Proof of Possession JWT

   The node collects a proof-of-possession JWT from the request and does the following:

   * Checks that the claims are valid.

   * Checks that an identity with the same ID as the name of the JWT subject exists.

   * Checks that the identity contains a confirmation key that matches the JWT `kid`.

   * Validates the JWT signature, using the confirmation key stored in the identity.

2. Client Assertion

   The node collects a JWT Bearer token from the request for authentication and validates the request according to the [JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://www.rfc-editor.org/rfc/rfc7523.html#section-3).

## Outcomes

* `Success`

* `Failure`

* `Requires Registration`

If all checks are successful, evaluation continues through the `Success` path, and adds the username and the verified claims to the shared node state.

If the identity does not exist, or AM cannot match the identity with the confirmation key, evaluation continues through the `Requires Registration` outcome.

If any other check fails, evaluation continues through the `Failure` outcome.

## Configuration

| Property                   | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| JWT Authentication Method  | Choose the required JWT authentication method:- Proof of Possession

  Prove that the signer of the JWT is the owner of the key by including a challenge nonce in the JWT. Validation is according to the [JWT Proof of Possession specification](https://tools.ietf.org/html/rfc7800).

- Client Assertion

  Present a JWT Bearer token for authentication and validate the request according to the [JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://www.rfc-editor.org/rfc/rfc7523.html#section-3). |
| Issue Restricted Token     | If this setting is enabled, the node adds a Proof of Possession restriction to the session token issued on successful authentication.Any requests accompanied by the token must be signed with the key that was used to sign the authentication JWT.                                                                                                                                                                                                                                                                                      |
| Additional Audience Values | Any additional audience values that will be permitted when verifying JWTs.These audience values are in addition to the AM base, issuer and token endpoint URIs for the Client Assertion authentication method or the realm path for Proof of Possession.                                                                                                                                                                                                                                                                                  |

---

---
title: Kerberos node
description: Use the Kerberos node in PingAM to enable desktop single sign-on through SPNEGO, allowing users authenticated with a Kerberos KDC to sign on without re-entering credentials.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:self-managed:kerberos
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/self-managed/kerberos.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Kerberos"]
page_aliases: ["auth-node-kerberos.adoc"]
section_ids:
  example: Example
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# Kerberos node

Enables desktop single sign-on such that a user who has already authenticated with a Kerberos Key Distribution Center can authenticate to AM without having to provide the login information again.

To achieve this, the user presents a Kerberos token to AM through the Simple and Protected GSS-API Negotiation Mechanism (SPNEGO) protocol.

End users may need to set up Integrated Windows Authentication in Microsoft Edge to benefit from single sign-on when logged on to a Windows desktop.

## Example

This flow attempts to authenticate the user with Windows Desktop SSO. If unsuccessful, AM requests the username and password for login. Meter nodes are used to track metrics for the various paths through the flow:

![An example that uses the Kerberos node](_images/trees-node-kerberos-example.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Outcomes

* `True`

* `False`

Evaluation continues along the `True` path if Windows Desktop SSO is successful; otherwise, evaluation continues along the `False` path.

## Configuration

| Property                          | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Service Principal                 | Specifies the Kerberos principal for authentication in the format `HTTP/AM-DOMAIN@AD-DOMAIN`, where *AM-DOMAIN* corresponds to the host and domain names of the AM instance, and *AD-DOMAIN* is the domain name of the Kerberos realm (the FQDN of the Active Directory domain). *AD-DOMAIN* can differ from the domain name for AM.In multi-instance AM deployments, configure *AM-DOMAIN* as the FQDN or IP address of the load balancer in front of the AM instances.For example, `HTTP/AM-LB.example.com@KERBEROSREALM.INTERNAL.COM`. |
| Key Tab File Path                 | Specifies the full, absolute path of the keytab file for the specified Service Principal.&#xA;&#xA;You generate the keytab file using the Windows ktpass utility. For example:&#xA;&#xA;C:\\> ktpass -out fileName.keytab -princ HTTP/am.example.com\@AD\_DOMAIN.COM -pass +rdnPass -maxPass 256 -mapuser amKerberos\@frdpcloud.com -crypto AES256-SHA1 -ptype KRB5\_NT\_PRINCIPAL -kvno 0                                                                                                                                                |
| Kerberos Realm                    | Specifies the name of the Kerberos (Active Directory) realm used for authentication.Must be specified in ALL CAPS.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Kerberos Server Name              | Specifies the fully qualified domain name, or IP address of the Kerberos (Active Directory) server.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Trusted Kerberos realms           | Specifies a list of trusted Kerberos realms for user Kerberos tickets. If realms are configured, then Kerberos tickets are only accepted if the realm part of the user principal name of the user's Kerberos ticket matches a realm from the list.Each trusted Kerberos realm must be specified in all caps.                                                                                                                                                                                                                              |
| Return Principal with Domain Name | When enabled, AM returns the fully qualified name of the authenticated user rather than just the username.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Lookup User In Realm              | Validates the user against the configured data stores. If the user from the Kerberos token is not found, evaluation continues along the `False` path.This search uses the `Alias Search Attribute Name` from the core realm attributes.Find more information about this property in [Core authentication attributes > User profile](https://docs.pingidentity.com/pingam/8.1/am-authentication/authn-core-settings.html#authn-core-user-profile).                                                                                         |
| Is Initiator                      | When enabled (`true`), specifies that the node is using *initiator* credentials, which is the default.When disabled (`false`), specifies that the node is using *acceptor* credentials.                                                                                                                                                                                                                                                                                                                                                   |

---

---
title: Register Thing node
description: Use the Register Thing node in PingAM to register IoT devices and gateways by validating a JWT and creating or updating the thing identity with a confirmation key.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:self-managed:register-thing
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/self-managed/register-thing.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication"]
page_aliases: ["self-managed/auth-node-register-thing.adoc"]
section_ids:
  availability: Availability
  dependencies: Dependencies
  outcomes: Outcomes
  configuration: Configuration
---

# Register Thing node

This node registers a *thing*. A thing represents an IoT device, service, or the [IoT Gateway](https://backstage.forgerock.com/docs/iot/7.4/evaluation-guide/about-iot.html#about-fr-things).

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | No         |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Dependencies

Before you configure this node, you must configure the [IoT service](https://docs.pingidentity.com/pingam/8.1/setup/services-configuration.html#global-iot) for the realm.

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Support for this node is provided by the [IoT SDK](https://backstage.forgerock.com/docs/iot/7.4/evaluation-guide/about-iot.html#about-fr-things). |

The node collects a JWT from the request and validates the JWT according to the configured [JWT registration method](#jwt-registration-method).

If the JWT is valid, the node uses the claims in the JWT to create an identity for the thing and register (or rotate) a confirmation key for it. Then, evaluation continues through the `Success` outcome.

If the node cannot validate the JWT, evaluation continues through the `Failure` outcome.

For an example on how to use this node, refer to [Authenticate Thing node](authenticate-thing.html).

## Outcomes

* `Success`

* `Failure`

## Configuration

| Property                    | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| []()JWT Registration Method | Choose the method to validate the JWT:- Proof of Possession & Certificate

  Register using a Proof of Possession JWT that includes an X.509 certificate for providing trust. A challenge nonce is presented in the callback and must be included in the signed JWT.

- Proof of Possession & Software Statement

  Register using a Proof of Possession JWT and a Software Statement for providing trust. A challenge nonce is presented in the callback and must be included in the signed Proof of Possession JWT. The claims in the Software Statement take precedence over the claims in the Proof of Possession JWT.

- Proof of Possession

  Register using a Proof of Possession JWT without using a trusted third party. A challenge nonce is presented in the callback and must be included in the signed JWT.

- Software Statement

  Register using a Software Statement, without doing proof of possession. If you select this registration method, the resultant session token will not include a proof of possession restriction.Default: Proof of Possession & Certificate |
| Verify Certificate Subject  | If the configured JWT registration method is `Proof of Possession & Certificate`, this option verifies that the subject provided in the JWT is the same as the X.509 certificate subject CN or UID.Default: Enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Create Identity             | Whether AM creates an ID for the thing if one doesn't exist.Default: Disabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Rotate Confirmation Key     | Whether multiple confirmation keys can be registered for a thing. Disable this setting to allow only one key per thing.Default: Disabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Default Attribute Values    | The default values for the thing's attributes, where KEY is the name of the attribute in the data store, and VALUE is the default value of the attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Claim to Attribute Mapping  | If Create Identity is enabled, this property lets you map verified claims in the JWT to attributes in the thing identity. KEY is the claim name and VALUE is the name of the attribute in the data store.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Overwrite Attributes        | Whether the node overwrites the value for an existing profile attribute when a claim with a different value is provided in the JWT.Default: Disabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
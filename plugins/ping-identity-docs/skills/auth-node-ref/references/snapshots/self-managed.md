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

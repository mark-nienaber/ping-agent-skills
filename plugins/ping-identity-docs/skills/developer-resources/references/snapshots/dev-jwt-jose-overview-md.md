---
title: Introduction to JSON Web Tokens (JWT)
description: A JSON Web Token (JWT) is an open-standard token for securely sharing information between parties as an encoded JavaScript Object Notation (JSON) object.
component: developer-resources
page_id: developer-resources::dev_jwt_jose_overview
canonical_url: https://docs.pingidentity.com/developer-resources/dev_jwt_jose_overview.html
revdate: June 6, 2023
section_ids:
  jwt-components: JWT Components
  javascript-object-signing-and-encryption-jose: Javascript Object Signing and Encryption (JOSE)
---

# Introduction to JSON Web Tokens (JWT)

A JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
\</div>)* is an open-standard token for securely sharing information between parties as an encoded JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* object.

JWT claims include information about a subject and transfer information about a user. JWTs are trusted because they are signed using either a secret (HMAC) or a public-private key pair *(tooltip: \<div class="paragraph">
\<p>The private key and public key represented by a certificate.\</p>
\</div>)* (RSA or ECDSA). JWTs are defined in [JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519) and [Introduction to JSON Web Tokens](https://jwt.io/introduction).

JWTs are commonly used for authorization, and particularly single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*. For example, after authenticating to a service, information about the user is encoded and shared between other relevant parties in a JWT. Subsequent domains know who the user is and that they have already been authenticated by a trusted party, so the user can access many different services after signing on once.

JWTs are an increasingly common way to secure application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)*s. You can share JWTs using Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
\<p>Identifies a resource according to its internet location.\</p>
\</div>)*s, POST *(tooltip: \<div class="paragraph">
\<p>An HTTP method used to request that the service or server accept the entity enclosed in the request as an addition to the resource identified in the URI.\</p>
\</div>)* parameters, or HTTP headers. JWT claims are embedded as JSON objects, which are used as the payload of a JSON Web Signature (JWS) *(tooltip: \<div class="paragraph">
\<p>A signed instance of a JSON Web Token (JWT) based on IETF standard syntax and used for the exchange of signed content.\</p>
\</div>)* structure or as text for a JSON Web Encryption (JWE) *(tooltip: \<div class="paragraph">
\<p>A signed and encrypted instance of a JSON Web Token (JWT) based on IETF standard syntax and used for the exchange of encrypted content.\</p>
\</div>)* structure.

## JWT Components

A JWT is defined as either a JWS object or a JWE object. When a token is signed it uses JWS, and when encrypted it uses JWE. There are three main parts of a JWS or JWE that include a JWT claim:

* Header

  The type of encoded object in the payload and information about how it is encoded.

See the following example header:

```json
{
  "typ": "JWT",
  "alg": "HS256"
}
```

This header shows a JWT that is integrity protected with the HMAC SHA-256 algorithm. The payload with a JWE including this header will be of a JWT signed and encrypted with the HMAC SHA-256 algorithm.

The type property can be left out if the JWSs and JWEs used by the application are JWT types. This property is intended to prevent confusion when different types are being used.

* Payload

  The JWT object itself, which is a set of claims.

See the following example payload:

```json
{
  "aud": "https://api.pingone.com",
  "iss": "https://auth.pingone.com/abcdefg12345/as",
  "exp": "1300819380"
}
```

This payload has an audience, `aud`, of the PingOne API, an issuer, `iss`, of the PingOne Authorization Server, and has a set expiration date, `exp`. The claim names might vary depending on the application and service being used.

* Signature

  The header and payload encoded using the algorithm specified in the header. In this example, the signature is the encoded header concatenated with the encoded JWT payload encoded with the HMAC SHA-256 algorithm.

```
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```

## Javascript Object Signing and Encryption (JOSE)

A JWT defines the token format and uses supporting specifications to handle signing and encryption. This collection of specifications is known as JOSE and consists of the following components:

* JSON Web Signature (JWS)

  Defines the process to digitally sign a JWT

* JSON Web Encryption (JWE)

  Defines the process to encrypt a JWT

* JSON Web Algortihm (JWA)

  Defines a list of algorithms for digitally signing or encrypting

* JSON Web Key (JWK)

  Defines how a cryptographic key and sets of keys are represented

Encoded JSON objects within JWTs include a set of claims signed using an algorithm so that they cannot be altered after a token is issued. Claims can be signed digitally or protected using message authentication code (MAC) *(tooltip: \<div class="paragraph">
\<p>A generated code that authenticates a message's sender and content.\</p>
\</div>)* with encryption. Encryption without MAC is also an option. When a user signs on using credentials, the OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* specification dictates that they receive an ID token in return, which is always a JWT.

For more information on JOSE, see [Javascript Object Signing and Encryption (JOSE)](https://jose.readthedocs.io/en/latest/).
---
title: Configure STS instances
description: Configure Security Token Service instances to perform token transformations and expose REST endpoints for SAML2 and OIDC token encryption or signing
component: pingam
version: 8.1
page_id: pingam:sts:sts-using-console
canonical_url: https://docs.pingidentity.com/pingam/8.1/sts/sts-using-console.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security Token Service (STS)", "Rest"]
page_aliases: ["sts-guide:sts-using-console.adoc"]
section_ids:
  sts-rest-console: Configure an STS instance in the UI
  sts-rest-rest: Configure an STS instance over REST
---

# Configure STS instances

You configure Security Token Service (STS) *instances* to perform one or more token transformations. Each instance provides configuration details about how SAML 2.0 and/or OIDC output tokens are encrypted or signed. Deployments that support multiple SAML 2.0 and/or OIDC service providers require multiple STS instances.

When you publish an STS instance, you create an STS instance with a given configuration. You can publish instances using the AM admin UI or the REST API.

When you publish an STS instance, AM exposes a REST endpoint for accessing the instance, and the instance is immediately available for use to callers.

## Configure an STS instance in the UI

To configure an STS instance using the AM admin UI, go to Realms > *realm name* > STS, and click Add Rest STS.

Read [STS configuration properties](sts-configure-rest-properties.html) for detailed information about STS configuration properties.

## Configure an STS instance over REST

To publish an STS instance programmatically, use the Publish service. This service is a collection of endpoints you can use to publish instances instead of accessing the AM admin UI.

Learn more in [The Publish service](sts-publish-service.html).

---

---
title: Consume STS instances
description: Call REST APIs on Security Token Service instances to transform tokens between different formats, including username, X.509, OIDC, and SAML2 tokens
component: pingam
version: 8.1
page_id: pingam:sts:sts-consume-rest
canonical_url: https://docs.pingidentity.com/pingam/8.1/sts/sts-consume-rest.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security Token Service (STS)", "Rest", "JSON", "Java"]
page_aliases: ["sts-guide:sts-consume-rest.adoc"]
section_ids:
  sts-consume-rest-endpoint: STS instance endpoint
  sts-consume-json-payload: JSON representation of token transformations
  sts-consume-rest-cli: Command-line example
  sts-consume-rest-programmatic: Java example
---

# Consume STS instances

You consume a Security Token Service (STS) instance by sending REST API calls to the instance's endpoint.

## STS instance endpoint

An STS instance endpoint is composed of the following:

* The AM context

* The string `rest-sts`

* The realm in which the STS instance is configured

* The deployment URL element (a configuration property of the STS instance)

For example, an STS instance configured in the `alpha` realm with the deployment URL element `username-transformer` exposes the endpoint `/rest-sts/alpha/username-transformer`.

## JSON representation of token transformations

Token transformations are represented in JSON as follows:

```json
{
  "input_token_state": {
    "token_type": "INPUT_TOKEN_TYPE"
    …​INPUT_TOKEN_TYPE_PROPERTIES…​
  },
  "output_token_state": {
    "token_type": "OUTPUT_TOKEN_TYPE"
    …​OUTPUT_TOKEN_TYPE_PROPERTIES…​
  }
}
```

The STS supports the following token types and properties:

* Input token types

  * `USERNAME`

    Requires the `username` and `password` properties.

  * `OPENAM`

    Requires the `session_id` property, with an SSO token as its value.

  * `X509`

    No properties are required because input X.509 tokens are presented in HTTP headers or through TLS.

    Find information about X.509 tokens in the Authentication Target Mappings and Client Certificate Header Key properties in the [STS configuration properties](sts-configure-rest-properties.html).

  * `OPENIDCONNECT`

    Requires the `oidc_id_token` property with the OIDC token as its value.

* Output token types

  * `SAML2`

    Requires the `subject_confirmation` property, the value of which determines the `<saml:ConfirmationMethod>` element for the generated SAML 2.0 assertion. Valid values are `BEARER`, `SENDER_VOUCHES`, and `HOLDER_OF_KEY`.

    When generating an assertion with a holder-of-key subject confirmation method, the `proof_token_state` property is required. The value for this property is an object that contains the `base64EncodedCertificate` property.

  * `OPENIDCONNECT`

    Requires the `nonce` and `allow_access` properties.

The following are examples of JSON payloads that define STS token transformations:

* Transform a username token to a SAML 2.0 token with the `BEARER` subject confirmation method:

  ```json
  {
    "input_token_state": {
      "token_type": "USERNAME",
      "username": "bjensen",
      "password": "Ch4ng31t"
    },
    "output_token_state": {
      "token_type": "SAML2",
      "subject_confirmation": "BEARER"
    }
  }
  ```

* Transform an X.509 token to a SAML 2.0 token with the `SENDER_VOUCHES` subject confirmation method:

  ```json
  {
    "input_token_state": {
      "token_type": "X509"
    },
    "output_token_state": {
      "token_type": "SAML2",
      "subject_confirmation": "SENDER_VOUCHES"
    }
  }
  ```

* Transform an OIDC token to a SAML 2.0 token with the `HOLDER_OF_KEY` subject confirmation method:

  ```json
  {
    "input_token_state": {
      "token_type": "OPENIDCONNECT",
      "oidc_id_token": "eyAiYWxQ.euTNnNDExNTkyMjEyIH0.kuNlKwyvZJqaC8EYpDyPJMiEcII"
    },
    "output_token_state": {
      "token_type": "SAML2",
      "subject_confirmation": "HOLDER_OF_KEY",
      "proof_token_state": {
        "base64EncodedCertificate": "MIMbFAAOBjQAwgYkCgYEArSQ…​c/U75GB2AtKhbGS5pimrW0Y0Q=="
       }
    }
  }
  ```

* Transform an AM SSO token to an OIDC token:

  ```json
  {
    "input_token_state": {
      "token_type": "OPENAM",
      "session_id": "AQIC5wM2…​TMQAA*"
    },
    "output_token_state": {
      "token_type": "OPENIDCONNECT",
      "nonce": "471564333",
      "allow_access": true
    }
  }
  ```

Find more examples of JSON payloads you can send to STS instances in the comments in the [Java example](#sts-consume-rest-programmatic) sample code.

## Command-line example

You can use the `curl` command to check that a published STS instance is working as expected.

For example, if you publish a REST instance with a deployment URL element `username-transformer` that supports username to SAML 2.0 bearer assertion token transformation, you can send an HTTP POST request to the `/rest-sts/username-transformer` endpoint, setting the `_action` parameter to `translate` as follows:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--data '{
  "input_token_state": {
    "token_type": "USERNAME",
    "username": "bjensen",
    "password": "Ch4ng31t"
  },
  "output_token_state": {
    "token_type": "SAML2",
    "subject_confirmation": "BEARER"
  }
}' \
https://am.example.com:8443/am/rest-sts/username-transformer?_action=translate
{
  "issued_token":
     "<saml:Assertion
       xmlns:saml=\"urn:oasis:names:tc:SAML:2.0:assertion\"
       Version=\"2.0\"
       ID=\"s2c51ebd0ad10aae44fb76e4b400164497c63b4ce6\"
       IssueInstant=\"2016-03-02T00:14:47Z\">\n
       <saml:Issuer>saml2-issuer</saml:Issuer>
       <saml:Subject>\n
        <saml:NameID
         Format=\"urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress\">bjensen
        </saml:NameID>
        <saml:SubjectConfirmation
         Method=\"urn:oasis:names:tc:SAML:2.0:cm:bearer\">\n
         <saml:SubjectConfirmationData
          NotOnOrAfter=\"2016-03-02T00:24:47Z\" >
         </saml:SubjectConfirmationData>
        </saml:SubjectConfirmation>\n
       </saml:Subject>
       <saml:Conditions
        NotBefore=\"2016-03-02T00:14:47Z\"
        NotOnOrAfter=\"2016-03-02T00:24:47Z\">\n
        <saml:AudienceRestriction>\n
         <saml:Audience>saml2-issuer-entity</saml:Audience>\n
        </saml:AudienceRestriction>\n</saml:Conditions>\n
        <saml:AuthnStatement
         AuthnInstant=\"2016-03-02T00:14:47Z\">
         <saml:AuthnContext>
          <saml:AuthnContextClassRef>
           urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
          </saml:AuthnContextClassRef>
         </saml:AuthnContext>
        </saml:AuthnStatement>
       </saml:Assertion>\n"
}
```

The `iPlanetDirectoryPro` header is required and should contain the SSO token of an administrative user, such as `amAdmin`, who has access to perform the operation.

## Java example

The `RestSTSConsumer.java` sample code provides an example of how to consume a published STS instance programmatically. Tailor this example as required to provide programmatic consumption of your own STS instances.

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn about downloading and building PingAM sample source code in the following *Knowledge Base* article: [How do I access and build the sample code provided for PingAM?](https://support.pingidentity.com/s/article/How-do-I-access-and-build-the-sample-code-provided-for-PingAM).You can find the STS code examples under `/path/to/openam-samples-external/sts-example-code`. |

|   |                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't *compile* the sample code referenced in this section because it uses classes that aren't available publicly. The code provides patterns to developers familiar with the problem domain and is intended only to assist developers who want to programmatically consume STS instances. |

---

---
title: Custom token types
description: Configure custom token validators and providers in PingAM STS instances to support custom token types in token transformations
component: pingam
version: 8.1
page_id: pingam:sts:sts-custom-token-types
canonical_url: https://docs.pingidentity.com/pingam/8.1/sts/sts-custom-token-types.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["sts-guide:sts-custom-token-types.adoc"]
section_ids:
  sts-consume-rest-custom-validator: Develop custom token type validator classes
  sts-consume-rest-custom-provider: Develop custom token type provider classes
  sts-consume-rest-custom-using: Use custom token type validators and providers
---

# Custom token types

AM supports token transformations to and from a variety of token types, including username, SAML 2.0, OIDC, and X.509. In addition to these core token types, STS instances can use custom token types as the input or output token, or both, in a token transformation. When you configure an STS instance to support a token transformation that takes a custom token type, you can also configure a custom validator and provider class for the custom token type. AM uses custom validator classes to validate custom tokens and custom provider classes to produce custom tokens.

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn about downloading and building PingAM sample source code in the following *Knowledge Base* article: [How do I access and build the sample code provided for PingAM?](https://support.pingidentity.com/s/article/How-do-I-access-and-build-the-sample-code-provided-for-PingAM).You can find the STS code examples under `/path/to/openam-samples-external/sts-example-code`. |

Specify custom token validator and provider classes in the AM admin UI by configuring the Custom Token Validators and Custom Token Providers properties under Realms > *realm name* > STS > *STS instance*.

A custom validator class can be used in transformations that produce standard STS output tokens, such as SAML 2.0 tokens or OIDC tokens, and in transformations that produce custom output token types.

A custom provider class can be used in token transformations that take standard STS input tokens, such as username tokens or AM SSO tokens, and in transformations that take custom input token types.

Before an STS instance can use a custom token type validator or provider class, you must bundle the class into the AM `.war` file and restart AM.

AM invokes a single instance of a validator or provider class to run all concurrently dispatched token transformations that use the custom token type. Because there is only a single instance of the class, you must code custom validator and provider classes to be thread-safe.

## Develop custom token type validator classes

To create a custom token type validator class, implement the `org.forgerock.openam.sts.rest.token.validator.RestTokenTransformValidator` class.

Custom token type validator classes implement the `validateToken` method. This method takes a `RestTokenValidatorParameters` object as input. Note that the generic type of `RestTokenValidatorParameters` is `org.forgerock.json.fluent.JsonValue`. As a result of using this type, custom validator classes can access the JSON representation of the input token passed to the STS instance in the `input_token_state` JSON key.

The `validateToken` method returns an `org.forgerock.openam.sts.rest.token.validator.RestTokenTransformValidatorResult` object. At a minimum, this object contains the AM SSO token corresponding to the validated principal. It can also contain additional information specified as a JSON value, allowing a custom validator to pass extra state to a custom provider in a token transformation.

## Develop custom token type provider classes

To create a custom token type provider class, implement the `org.forgerock.openam.sts.rest.token.provider.RestTokenProvider` class.

Custom token type provider classes implement the `createToken` method. This method takes an `org.forgerock.openam.sts.rest.token.provider.CustomRestTokenProviderParameters` object as input. This object gives the custom provider access to the following information:

* The principal returned by the `RestTokenTransformValidator`

* The AM SSO token corresponding to the validated principal

* Any additional state returned in the `RestTokenValidatorResult` object

* The type of input token validated by the `RestTokenTransformValidator` in the token transformation

* The `JsonValue` corresponding to this validated token, as specified by the `input_token_state` object in the transformation request

* The `JsonValue` corresponding to the `token_output_state` object specified in the token transformation request (which can provide additional information pertinent to the creation of the output token)

The `createToken` method returns a string representation of the custom token in a format that can be transmitted across HTTP in JSON. It should be base64-encoded if binary.

## Use custom token type validators and providers

This section provides an example of how to use custom token type validators and providers.

The example assumes that you already configured a token transformation by completing the following tasks:

* Implementing the `RestTokenTransformValidator` interface to create a custom token type validator

* Implementing the `RestTokenProvider` interface to create a custom token type provider

* Bundling the two classes into the AM `.war` file

* Restarting AM

* Publishing an STS instance with a custom token type named `CUSTOM`, specifying the custom validator and provider classes in the instance's configuration

To transform a `CUSTOM` token to an OIDC token, you might specify a JSON payload similar to the following:

```json
{
    "input_token_state":
        {
            "token_type": "CUSTOM",
            "extra_stuff": "very_useful_state"
        },
    "output_token_state":
        {
            "token_type": "OPENIDCONNECT",
            "nonce": "1234",
            "allow_access": true
        }
}
```

With the preceding JSON payload, AM passes a `JsonValue` instance to the `validateToken` method of the custom token type validator class:

```json
{
    "token_type": "CUSTOM",
    "extra_stuff": "very_useful_state"
}
```

To transform a username token to a `CUSTOM` token, you might specify a JSON payload similar to the following:

```json
{
    "input_token_state":
        {
            "token_type": "USERNAME",
            "username": "unt_user17458687",
            "password": "password"
        },
    "output_token_state":
        {
            "token_type": "CUSTOM",
            "extra_stuff_for_custom": "some_useful_information"
        }
}
```

With the preceding JSON payload, AM passes the following information to the `createToken` method of the custom token type provider:

* The principal returned by the `USERNAME` token validator: `unt_user17458687`.

* The AM SSO token corresponding to this authenticated principal.

* Additional state returned by the token validator, if any. Because the `USERNAME` token validator doesn't return any additional state, the additional state for this example would be null.

* The input token type: `CUSTOM`

* A `JsonValue` representation of the following:

  ```json
  {
      "token_type": "USERNAME",
      "username": "unt_user17458687",
      "password": "password"
  }
  ```

* A `JsonValue` representation of the following:

  ```json
  {
      "token_type": "CUSTOM",
      "extra_stuff_for_custom": "some_useful_information"
  }
  ```

To transform a `CUSTOM` token to a `CUSTOM` token, you might specify a JSON payload similar to the following:

```json
{
    "input_token_state":
        {
            "token_type": "CUSTOM",
            "extra_stuff": "very_useful_state"
        },
    "output_token_state":
        {
            "token_type": "CUSTOM",
            "extra_stuff_for_custom": "some_useful_information"
        }
}
```

The input to the custom validator and provider would be similar to the preceding examples, with the possible addition of any additional state that the custom validator returned from the `validateToken` method.

---

---
title: Introduction to STS
description: Use PingAM Security Token Service (STS) to bridge identities across federated environments by transforming tokens between OIDC and SAML2 formats
component: pingam
version: 8.1
page_id: pingam:sts:chap-sts-introduction
canonical_url: https://docs.pingidentity.com/pingam/8.1/sts/chap-sts-introduction.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security Token Service (STS)"]
page_aliases: ["sts-guide:chap-sts-introduction.adoc"]
section_ids:
  supported_features: Supported features
---

# Introduction to STS

The Security Token Service (STS) lets AM bridge identities across existing federated environments to establish cross-domain trust relationships using token transformations. For example, you can federate two different environments by transforming OIDC ID tokens into SAML 2.0 assertions.

To do this, AM provides a [REST STS framework](sts-rest.html) for token transformations. This framework is loosely based on the SOAP [WS-Trust](https://docs.oasis-open.org/ws-sx/ws-trust/v1.4/ws-trust.html) specification.

A WS-Trust model involves communication between the components, a requestor, web service, and the STS:

* The *requestor* is a web client or programmatic agent that wants to use a service offered by the web service.

* The *web service* lets authenticated and authorized clients access resources or applications.

* The *identity provider* stores claims about subjects and works with the STS to issue security tokens.

* The *STS* acts as a trusted third-party web service. It asserts the identity of a requestor across different security domains through the exchange of security tokens and brokers a trust relationship between the requestor and the web service provider. The STS issues tokens based on its configurations, which model the identity of a given identity provider, and issues tokens to a specific relying party.

* A *security token* is an STS data structure representing a set of claims that assert the identity of a subject. A single claim is identity information, such as a subject's name, age, gender, and email address.

Web services and requestors (that is, consumers or clients) are typically deployed across different security domains and topologies. Each domain may require a specific security token type to assert authenticated identities. The STS provides a way to exchange tokens across these different domains without re-authenticating or re-establishing trust relationships while allowing the requestor access to a web service's protected resources.

## Supported features

The STS supports the following features:

* REST endpoints

  REST endpoints are exposed upon instance creation.

* Token transformations

  The STS issues OpenID Connect V1.0 (OIDC) and SAML 2.0 tokens (bearer, holder-of-key, sender vouches).

  * OIDC

    Username token → OIDC\
    OIDC → OIDC\
    X.509 token → OIDC\
    AM Session token → OIDC

  * SAML 2.0

    Username token → SAML 2.0\
    X.509 token → SAML 2.0\
    OIDC token → SAML 2.0\
    AM Session token → SAML 2.0

* Publish service

  You can configure STS instances using the AM admin UI or programmatically. AM provides an STS publish service that lets you publish these instances with a POST request to the endpoints. Because a published instance can have only a single encryption key, you need one published instance per service provider that the web service invoking the STS intends to call.

* Custom SAML assertion plugins

  AM supports customizable SAML assertion statements. You can create custom plug-ins for `Conditions`, `Subject`, `AuthenticationStatements`, `AttributeStatements`, and `AuthorizationDecisionStatements` statements.

* Custom token validators and providers

  The STS provides the ability to customize tokens. For example, you can configure STS to transform a token of type CUSTOM to a SAML 2.0 token.

---

---
title: Query, validate, and cancel tokens
description: Query, validate, and cancel security tokens issued by PingAM Security Token Service instances using REST API calls and the Core Token Service
component: pingam
version: 8.1
page_id: pingam:sts:sts-query-validate-cancel
canonical_url: https://docs.pingidentity.com/pingam/8.1/sts/sts-query-validate-cancel.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security Token Service (STS)", "Rest", "SAML 2.0", "OpenID Connect (OIDC)", "JSON"]
page_aliases: ["sts-guide:sts-query-validate-cancel.adoc"]
section_ids:
  sts-query-validate-cancel-sts-tokengen: Invoke the sts-tokengen endpoint
  sts-query-validate-cancel-sts-tokengen-query: Query tokens
  sts-query-validate-cancel-sts-tokengen-cancel: Cancel tokens
  query-validate-cancel-rest-sts-instance: Validate and cancel tokens by invoking an STS instance
---

# Query, validate, and cancel tokens

The Security Token Service (STS) instance supports *token persistence*, which is the ability to store tokens issued for the STS instance in the Core Token Service (CTS). You enable token persistence for STS instances under Realms > *realm name* > STS > *STS instance* > General Configuration > Persist Issued Tokens in Core Token Store. Tokens are saved in the CTS for the duration of the token lifetime, which is a configuration property for STS-issued SAML 2.0 and OIDC tokens. Tokens with expired durations are periodically removed from the CTS.

With token persistence enabled for an STS instance, AM provides the ability to query, validate, and cancel tokens issued for the instance:

* *Querying tokens* means listing tokens issued for an STS instance or for a user.

* *Validating a token* means verifying that the token is still present in the CTS.

* *Cancelling a token* means removing the token from the CTS.

## Invoke the sts-tokengen endpoint

The `sts-tokengen` endpoint provides administrators with the ability to query and cancel tokens issued using REST API calls.

When using the `sts-tokengen` endpoint, make sure you provide the token ID for an AM administrator, such as `amAdmin`, as the value of a header whose name is the name of the SSO token cookie, by default `iPlanetDirectoryPro`.

### Query tokens

List tokens issued for an STS instance by using the `queryFilter` action in an HTTP GET call to the `sts-tokengen` endpoint with the `/sts-id` argument.

The following example lists all the tokens issued for the `username-transformer` STS instance. The results show that AM has issued two OIDC tokens for `bjensen` for the `username-transformer` STS instance:

```bash
$ curl \
--request GET \
--header "iPlanetDirectoryPro: AQIC5…​" \
https://am.example.com:8443/am/sts-tokengen?_queryFilter=\/sts_id+eq+\'username-transformer\'
{
    "result":[
        {
            "_id":"B663D248CE4C3B63A7422000B03B8F5E0F8E443B",
            "_rev":"",
            "token_id":"B663D248CE4C3B63A7422000B03B8F5E0F8E443B",
            "sts_id":"username-transformer",
            "principal_name":"bjensen",
            "token_type":"OPENIDCONNECT",
            "expiration_time":1459376096
        },
        {
            "_id":"7CB70009970D1AAFF177AC2A08D58405EDC35DF5",
            "_rev":"",
            "token_id":"7CB70009970D1AAFF177AC2A08D58405EDC35DF5",
            "sts_id":"username-transformer",
            "principal_name":"bjensen",
            "token_type":"OPENIDCONNECT",
            "expiration_time":1459376098
        }
    ],
    "resultCount":2,
    "pagedResultsCookie":null,
    "totalPagedResultsPolicy":"NONE",
    "totalPagedResults":-1,
    "remainingPagedResults":-1
}
```

List tokens issued for a particular user with the `queryFilter` action in an HTTP GET call to the `sts-tokengen` endpoint with the `/token-principal` argument.

The following example lists all the tokens issued for `bjensen`. The results show that AM has issued two OIDC tokens:

```bash
$ curl \
--request GET \
--header "iPlanetDirectoryPro: AQIC5…​" \
https://am.example.com:8443/am/sts-tokengen?_queryFilter=\/token_principal+eq+\'bjensen\'
{
    "result":[
        {
            "_id":"B663D248CE4C3B63A7422000B03B8F5E0F8E443B",
            "_rev":"",
            "token_id":"B663D248CE4C3B63A7422000B03B8F5E0F8E443B",
            "sts_id":"username-transformer",
            "principal_name":"bjensen",
            "token_type":"OPENIDCONNECT",
            "expiration_time":1459376096
        },
        {
            "_id":"7CB70009970D1AAFF177AC2A08D58405EDC35DF5",
            "_rev":"",
            "token_id":"7CB70009970D1AAFF177AC2A08D58405EDC35DF5",
            "sts_id":"username-transformer",
            "principal_name":"bjensen",
            "token_type":"OPENIDCONNECT",
            "expiration_time":1459376098
        }
    ],
    "resultCount":2,
    "pagedResultsCookie":null,
    "totalPagedResultsPolicy":"NONE",
    "totalPagedResults":-1,
    "remainingPagedResults":-1
}
```

### Cancel tokens

Cancel tokens by making an HTTP DELETE call to the `sts-tokengen`/*token-id* endpoint:

```bash
$ curl \
--request DELETE \
--header "iPlanetDirectoryPro: AQIC5…​" \
https://am.example.com:8443/am/sts-tokengen/B663D248CE4C3B63A7422000B03B8F5E0F8E443B
{
    "_id":"B663D248CE4C3B63A7422000B03B8F5E0F8E443B",
    "_rev":"B663D248CE4C3B63A7422000B03B8F5E0F8E443B",
    "result":"token with id B663D248CE4C3B63A7422000B03B8F5E0F8E443B successfully removed."
}
```

## Validate and cancel tokens by invoking an STS instance

STS users can validate and cancel tokens by making an HTTP POST call to an STS instance's endpoint.

To validate a token, use the `validate` action. The following example validates an OIDC token previously issued by the `username-transformer` STS instance:

```bash
$ curl \
--request POST \
--header "iPlanetDirectoryPro: AQIC5…​" \
--header "Content-Type: application/json" \
--data '{
    "validated_token_state": {
        "token_type": "OPENIDCONNECT",
        "oidc_id_token": "eyAidHlwIjogIkpXVCIsIC…​"
    }
}' \
https://am.example.com:8443/am/rest-sts/username-transformer?_action=validate
{
    "token_valid":true
}
```

To cancel a token, use the `cancel` action. The following example cancels an OIDC token previously issued by the `username-transformer` STS instance:

```bash
$ curl \
--request POST \
--header "iPlanetDirectoryPro: AQIC5…​" \
--header "Content-Type: application/json" \
--data '{
    "cancelled_token_state": {
        "token_type": "OPENIDCONNECT",
        "oidc_id_token": "eyAidHlwIjogIkpXVCIsIC…​"
    }
}' \
 https://am.example.com:8443/am/rest-sts/username-transformer?_action=cancel
{
    "result":"OPENIDCONNECT token cancelled successfully."
}
```

---

---
title: Reference
description: Configuration settings and reference information for the Security Token Service (STS)
component: pingam
version: 8.1
page_id: pingam:sts:chap-sts-reference
canonical_url: https://docs.pingidentity.com/pingam/8.1/sts/chap-sts-reference.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security Token Service (STS)"]
page_aliases: ["sts-guide:chap-sts-reference.adoc"]
---

# Reference

The reference pages cover configuration settings for the Security Token Service (STS).

---

---
title: Security Token Service (STS)
description: Use the Security Token Service in PingAM to transform, validate, issue, and cancel tokens for token exchange management
component: pingam
version: 8.1
page_id: pingam:sts:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/sts/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security Token Service (STS)"]
page_aliases: ["index.adoc", "sts-guide:preface.adoc"]
---

# Security Token Service (STS)

These topics cover concepts, configuration, and usage procedures for working with the Security Token Service (STS) provided by PingAM.

This information is intended for anyone using the STS in PingAM to manage token exchange.

[icon: book, set=fad, size=3x]

#### [STS overview](chap-sts-introduction.html)

Learn how the STS can transform, validate, issue, and cancel tokens.

[icon: edit, set=fad, size=3x]

#### [Configure the STS](sts-using-console.html)

Add one or more STS instances to your AM deployment.

[icon: exchange-alt, set=fad, size=3x]

#### [Query, validate, and cancel tokens](sts-query-validate-cancel.html)

Manage tokens stored in the CTS token store.

---

---
title: STS configuration properties
description: Configure PingAM Security Token Service instances to persist tokens, support token transformations, validate custom token types, and authenticate input tokens through authentication trees
component: pingam
version: 8.1
page_id: pingam:sts:sts-configure-rest-properties
canonical_url: https://docs.pingidentity.com/pingam/8.1/sts/sts-configure-rest-properties.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security Token Service (STS)", "Rest", "Configuration", "Authentication", "Certificates"]
page_aliases: ["sts-guide:sts-configure-rest-properties.adoc"]
section_ids:
  general_configuration_properties: General configuration properties
  deployment_configuration_properties: Deployment configuration properties
  saml2_token_configuration_properties: SAML2 token configuration properties
  sts-issued-openid-token-props: OpenID Connect token configuration properties
---

# STS configuration properties

* Deployment Url Element

  A string that identifies this STS instance.

  The Deployment Url Element is a component of the STS instance's endpoint. For example, if you set `mySTSInstance` as the Deployment Url Element, the STS endpoint would be `rest-sts/myRealm/mySTSInstance`.

## General configuration properties

The following are general configuration properties for STS instances:

* Persist Issued Tokens in Core Token Store

  Indicate whether to enable token persistence in the Core Token Service (CTS).

  AM saves all STS-issued tokens to CTS when token persistence is enabled. A token's lifetime in CTS has the same length as the Token Lifetime property specified for issued tokens.

  STS token validation and cancellation capabilities require tokens to be present in CTS. Therefore, if your deployment requires token validation and cancellation, you must enable token persistence.

* Supported Token Transforms

  The token transformations supported by this STS instance. Token transformations are listed in the AM admin UI using the notation `input-token-type → output-token-type`.

  For each supported token transformation, AM provides an option to invalidate the interim AM session. When transforming a token, the STS creates an AM session. If desired, you can invalidate the AM session after token transformation is complete.

* Custom Token Validators

  A validator class for a custom token type.

  Use the format `CUSTOM-TOKEN-TYPE|custom-validator-class` to specify each validator class. For example, `CUSTOM|org.mycompany.tokens.myCustomTokenValidator`.

  Learn more in [Custom token types](sts-custom-token-types.html).

* Custom Token Providers

  A provider class for a custom token type.

  Use the format `CUSTOM-TOKEN-TYPE|custom-provider-class` to specify each provider class. For example, `CUSTOM|org.mycompany.tokens.myCustomTokenProvider`.

  Learn more in [Custom token types](sts-custom-token-types.html).

* Custom Token Transforms

  The token transformations that take a custom token type as the input or output token. If you specify a custom token validator or provider, you must also specify a custom token transform.

  The custom transform uses three values separated by the vertical bar character `|` as follows:

  1. The input token type

  2. The output token type

  3. Whether to invalidate the AM session created during token transformation. Use `TRUE` to invalidate the session or `FALSE` to let the session remain valid.

  For example, a value of `CUSTOM|SAML2|TRUE` configures a token transformation that transforms a `CUSTOM` token to a SAML 2.0 assertion and then invalidates the created AM session.

- STS Instance is running as remote instance

  Indicate whether the STS instance is running on the AM host or as a separate, remote Java process.

  This property determines how calls are made to the STS instance during session token validation.

  Default: `true`

  If `true`, the STS does an outbound HTTP call to itself during session validation. If you set this property to `false` (for example, for an AM instance running in a clustered Docker pod), the STS validates sessions and generates tokens locally, with no HTTP call to the `sessions` or `sts-gen` endpoints.

## Deployment configuration properties

The following are deployment configuration properties for STS instances:

* Authentication Target Mappings

  The mappings that define how the STS instance authenticates input tokens.

  Each mapping is a set of arguments separated by the vertical bar character `|` as follows:

  1. (Required) The input token type: `USERNAME`, `OPENAM`, `X509`, `OPENIDCONNECT`, or a custom token type.

  2. (Required) The value `service`.

  3. (Required) The name of an authentication tree, which authenticates the input token.

  4. (Optional) The name of the header in which you place the token when authenticating to AM. Set this parameter for input `X509` and `OPENIDCONNECT` tokens as follows:

     * For `X509` input tokens, the format is `x509_token_auth_target_header_key=Header Name`.

     * For `OPENIDCONNECT` input tokens, the format is `oidc_id_token_auth_target_header_key=Header Name`.

     Make sure you specify the header names configured in the [Certificate Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-collector.html) or [OIDC ID Token Validator node](https://docs.pingidentity.com/auth-node-ref/8.1/oidc-idtoken-validator.html) properties as the *Header Name* argument.

     This argument can also be used with custom token types to specify the name of a header or cookie from which to obtain a token. When using this argument with a custom token type, its format is determined by the custom validator class that validates the custom token type.

  The following are example mappings:

  * `USERNAME|service|ldapService` configures STS to authenticate input `USERNAME` tokens to the `ldapService` authentication tree.

  * `X509|service|certificateAuth|x509_token_auth_target_header_key=ClientCert` configures STS to obtain an X.509 certificate from the `ClientCert` header, use it as the input token, and authenticate it using a tree named `certificateAuth` that includes the certificate authentication nodes.

* Client Certificate Header Key

  The name of the header a TLS offloader should use to transmit client certificates.

  Token transformations that take an X.509 certificate as the input token require the certificate to be presented using mTLS, so the TLS handshake can validate client certificate ownership.

  A common way to obtain the client certificate with mTLS is to use the `jakarta.servlet.request.X509Certificate` attribute in the servlet request.

  However, in deployments with TLS offloading, the offloader must use an HTTP header to transmit the certificate to its destination. This configuration property is the name of the HTTP header whose value contains the certificate.

* Trusted Remote Hosts

  The IP addresses of hosts trusted to transmit client X.509 certificates in deployments with TLS offloading.

  To allow any host to transmit a certificate, specify `any` as the value of this property.

  As with the Client Certificate Header Key property, configure this property for deployments with TLS offloading.

## SAML2 token configuration properties

The following are SAML 2.0 token configuration properties for STS instances:

The properties fall into two categories:

* Properties that determine content in STS-issued SAML 2.0 assertions. Learn more about SAML 2.0 assertions in [Assertions and Protocols for the OASIS Security Assertion Markup Language (SAML) 2.0](https://www.oasis-open.org/committees/download.php/35711/sstc-saml-core-errata-2.0-wd-06-diff.pdf).

* Properties that determine how the issued SAML 2.0 assertion is signed or encrypted.

- The SAML2 Issuer Id

  The IdP entity ID. Populates the `Issuer` element of the SAML 2.0 assertion.

- Service Provider Entity Id

  An audience attribute value. Populates the `AudienceRestriction` sub-element of the `Conditions` element of the SAML 2.0 assertion.

  This value is required when issuing Bearer assertions.

- Service Provider Assertion Consumer Service Url

  A recipient attribute value. Populates the `Recipient` sub-element of the `SubjectConfirmation` element of the SAML 2.0 assertion.

  The scheme, FQDN, and port configured must exactly match those of the service provider as they appear in its metadata.

  This value is required when issuing Bearer assertions.

- NameIdFormat

  The name identifier format for the SAML 2.0 assertion.

- Token Lifetime(Seconds)

  The lifetime, in seconds, for the assertion. The default is 600 seconds.

- Custom Conditions Provider Class Name

  (Optional) The name of a custom class that generates a `Conditions` element in the SAML 2.0 assertion. Use a custom class when the `Conditions` element created by the default provider doesn't meet your needs.

  The class must implement the `org.forgerock.openam.sts.tokengeneration.saml2.statements.ConditionsProvider` interface, and must be bundled in the AM `.war` file.

- Customs Subject Provider Class Name

  (Optional) The name of a custom class that generates a `Subject` element in the SAML 2.0 assertion. Use a custom class when the `Subject` element created by the default provider doesn't meet your needs.

  The class must implement the `org.forgerock.openam.sts.tokengeneration.saml2.statements.SubjectProvider` interface and must be bundled in the AM `.war` file.

- Custom AuthenticationStatements Class Name

  (Optional) The name of a custom class that generates an `AuthnStatement` element in the SAML 2.0 assertion. Use a custom class when the `AuthnStatement` element created by the default provider doesn't meet your needs.

  The class must implement the `org.forgerock.openam.sts.tokengeneration.saml2.statements.AuthenticationStatementsProvider` interface and must be bundled in the AM `.war` file.

- Custom AttributeStatements Class Name

  (Optional) The name of a custom class that generates an `AttributeStatement` element in the SAML 2.0 assertion. Use a custom class when the `AttributeStatement` element created by the default provider doesn't meet your needs.

  The class must implement the `org.forgerock.openam.sts.tokengeneration.saml2.statements.AttributeStatementsProvider` interface and must be bundled in the AM `.war` file.

- Custom Authorization Decision Statements Class Name

  (Optional) The name of a custom class that generates an `AuthzDecisionStatement` element in the SAML 2.0 assertion. Use a custom class when the `AuthzDecisionStatement` element created by the default provider doesn't meet your needs.

  The class must implement the `org.forgerock.openam.sts.tokengeneration.saml2.statements.AuthzDecisionStatementsProvider` interface and must be bundled in the AM `.war` file.

- Custom Attribute Mapper Class Name

  The name of a custom attribute mapper class. An attribute mapper generates `attribute` elements to be included in the SAML 2.0 assertion.

  The class must implement the `org.forgerock.openam.sts.tokengeneration.saml2.statements.AttributeMapper` interface and must be bundled in the AM `.war` file.

- Custom Authentication Context Class Name

  (Optional) The name of a custom class that generates an `AuthnContext` element in the SAML 2.0 assertion. Use a custom class when the `AuthnContext` element created by the default provider doesn't meet your needs.

  The class must implement the `org.forgerock.openam.sts.tokengeneration.saml2.statements.AuthnContextMapper` interface and must be bundled in the AM `.war` file.

  By default, AM generates the `AuthnContext` element based on the input token type as follows:

  * For input AM tokens: `urn:oasis:names:tc:SAML:2.0:ac:classes:PreviousSession`

  * For input username tokens and OIDC ID tokens: `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport`

  * For input X.509 tokens: `urn:oasis:names:tc:SAML:2.0:ac:classes:X509`

- Attribute Mappings

  Configures mappings between SAML 2.0 attribute names (*map keys*) and AM user profile attributes or session properties to generate `Attribute` elements in the SAML 2.0 assertion.

  AM's default attribute mapper generates `Attribute` elements as follows:

  * The map key populates the `Attribute` element's `Name` property.

  * The user profile or session property value populates the `Attribute` element's `AttributeValue` property.

  When specifying map keys in the `Attribute Mappings` property, use the following format: `[NameFormatURI]|SAML_ATTRIBUTE_NAME`.

  Map values enclosed in quotes are included in the attribute without mapping. Add `;binary` to the end of a map value for attributes with binary values.

  The following are examples of attribute mappings:

  * `EmailAddress=mail`

  * `Address=postaladdress`

  * `urn:oasis:names:tc:SAML:2.0:attrname-format:uri|urn:mace:dir:attribute-def:cn=cn`

  * `partnerID="staticPartnerIDValue"`

  * `urn:oasis:names:tc:SAML:2.0:attrname-format:uri|nameID="staticNameIDValue"`

  * `photo=photo;binary`

  * `urn:oasis:names:tc:SAML:2.0:attrname-format:uri|photo=photo;binary`

- Sign Assertion

  Indicate whether to sign the SAML 2.0 assertion.

  When enabling assertion signing, you must also specify the KeystorePath, Keystore Password, Signature Key Alias, and Signature Key Password properties.

- Encrypt Assertion

  Indicate whether to encrypt the entire SAML 2.0 assertion. When enabling assertion encryption:

  * You must also specify the KeystorePath, Keystore Password, and Encryption Key Alias properties.

  * You mustn't specify the Encrypt Attributes or Encrypt NameID options.

  The Encryption Key Alias corresponds to the public key of the service provider that is the intended audience of the assertion. SAML 2.0 assertion encryption works as follows:

  1. AM generates a symmetric key.

  2. AM encrypts the symmetric key with the recipient's public key.

  3. AM includes the encrypted key in the part of the assertion that isn't symmetric key-encrypted.

  4. The service provider (owner of the corresponding private key) uses the private key to decrypt the symmetric key included in the assertion.

  5. The service provider can then use the decrypted symmetric key to decrypt the assertion.

- Encrypt Attributes

  Indicate whether to encrypt the assertion's attributes only. When specifying this option, don't specify the Encrypt Assertion option.

  When encrypting attributes, you must also specify the KeystorePath, Keystore Password, and Encryption Key Alias properties.

- Encrypt NameID

  Indicate whether to encrypt the assertion's NameID only. When specifying this option, don't specify the Encrypt Assertion option.

  When encrypting the NameID, you must also specify the KeystorePath, Keystore Password, and Encryption Key Alias properties.

- Encryption Algorithm

  The encryption algorithm to use when encrypting the entire assertion, the assertion's attributes, or the NameID.

- Encryption Algorithm Strength

  The encryption algorithm strength to use.

- Key Transport Algorithm

  The algorithm used to encrypt the symmetric encryption key when SAML 2.0 token encryption is enabled. Possible values are:

  * `http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p`.

  * `http://www.w3.org/2009/xmlenc11#rsa-oaep`.

    When this algorithm is configured, AM will use the Mask Generation Function Algorithm property (Configure > Global Services > Common Federation Configuration) to encrypt the transport key.

    Find a list of supported mask generation function algorithms in [Algorithms](../setup/services-configuration.html#global-federation-common-algorithms).

  * `http://www.w3.org/2001/04/xmlenc#rsa-1_5`.

- KeystorePath

  The path to the JKS keystore containing the key aliases for encrypting and signing SAML assertions. Use an absolute path or a location in the AM classpath.

  AM provides a JKS keystore with demo keys, `/path/to/am/security/keystores/keystore.jks`. Learn more in [Secrets, certificates, and keys](../security/secrets-certs-keys.html).

- Keystore Password

  The password used to decrypt the keystore.

- Encryption Key Alias

  The key alias in the keystore that holds the service provider's X.509 certificate for this STS instance. This key alias is used to encrypt assertions.

- Signature Key Alias

  The private key alias in the keystore used to sign assertions.

- Signature Key Password

  The password of the private key used to sign the assertion.

## OpenID Connect token configuration properties

The following are OIDC token configuration properties for STS instances:

The properties fall into two categories:

* Properties that determine content in the issued OIDC ID token. Learn more about OIDC ID tokens in the [OpenID Connect Core 1.0 specification](https://openid.net/specs/openid-connect-core-1_0.html#IDToken).

* Properties that determine how the issued token is signed.

An STS instance configured to issue OIDC tokens models the relationship between an OIDC token provider and relying party. In other words, an STS instance issues tokens for a particular OAuth 2.0 client. The tokens contain `aud` and `azp` claims for the OAuth 2.0 client, and signing key state corresponding to a token provider.

In this model, when users call an STS instance to generate an OIDC ID token, the process is analogous to the exchange between an OAuth 2.0 authorization server and resource owner following the initial redirection from an OAuth 2.0 client initiating the implicit flow. The STS instance returns the OIDC ID token that corresponds to the authorization server's authentication of the resource owner.

AM authenticates the token specified as the `input_token_state` for the token transformation

Implicit in this model is the notion that an OIDC ID token has value outside of an OAuth 2.0 flow, and that an OAuth 2.0 client, as a relying party, could be generalized as a SAML 2.0 service provider. The ID token isn't simply an an entity-provided verifiable authorized access to a specific resource, but rather a generic service provider that consumes an OIDC ID token to authenticate and authorize the subject asserted by the token.

Therefore, the configuration of an STS instance that issues OIDC ID tokens contains information that defines the token provider and relying party.

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `nonce` claim in the ID token isn't a configuration property of an STS instance. STS consumers requesting an output OIDC token provide a `nonce` value when making token transformation requests. |

* OpenID Connect Token Provider ID

  The OIDC token provider issuer ID. Populates the `iss` claim of the ID token.

* Token Lifetime(Seconds)

  The ID token's expiration in seconds. Populates the `exp` claim of the ID token.

* Token Signature Algorithm

  An HMAC or RSA algorithm used to sign ID tokens.

* Public Key Reference Type

  Indicate how public keys should be referenced in issued ID tokens signed with RSA. OIDC ID tokens are issued as JSON web tokens (JWTs). Tokens can reference RSA public keys as JSON web keys (JWKs), or not at all.

  Used with RSA signing.

* KeyStore Location

  The path to the JKS keystore containing the key alias for signing the ID token. Use an absolute path or a location in the AM classpath.

  Used with RSA signing.

  AM provides a JKS keystore with demo keys, `/path/to/am/security/keystores/keystore.jks`. Learn more about keystores in [Secrets, certificates, and keys](../security/secrets-certs-keys.html).

* KeyStore Password

  The password used to decrypt the keystore.

  Used with RSA signing.

* KeyStore Signing Key Alias

  The private key alias in the keystore used to sign the ID token.

  Used with RSA signing.

* Signature Key Password

  The password of the private key alias used to sign the ID token.

  Used with RSA signing.

* Client secret

  The secret shared between the client and the ID token generator used to sign the ID token.

  Used with HMAC signing.

* Issued Tokens Audience

  The intended audience for the ID token. Populates the `aud` claim of the ID token.

* Authorized Party

  The party to which the ID token is being issued. Populates the `azp` claim of the ID token.

* Claim Map

  The additional claim entries to be inserted into the ID token.

  The entries use the format `claim-name=user-profile-attribute`. When issuing the ID token, AM populates the claim value with the value of the attribute in the authenticated user's profile.

  For example, suppose the `Claim map` property had an entry with the value `email=mail`. A generated OIDC ID token for user Sam Carter would contain the claim `"email":"scarter@example.com"` if the `mail` attribute in Sam Carter's user profile had the value `scarter@example.com`.

* Custom Claim Mapper Class

  The name of a custom claim mapper class. A claim mapper generates additional claims to be included in the OIDC ID token.

  The class must implement the `org.forgerock.openam.sts.tokengeneration.oidc.OpenIdConntectTokenClaimMapper` interface and must be bundled in the AM `.war` file.

* Custom Authn Context Mapper Class

  The name of a custom class that generates an `acr` claim in the OIDC ID token. An `acr` claim indicates which authentication context class was satisfied by the authentication of the principal asserted in the OIDC ID token. The `acr` claim is optional and isn't included in the generated ID token by default.

  The class must implement the `org.forgerock.openam.sts.rest.token.provider.oidc.OpenIdConnectTokenAuthnContextMapper` interface and must be bundled in the AM `.war` file.

* Custom Authn Methods References Mapper Class

  The name of a custom class that generates an `amr` claim in the OIDC ID token. An `amr` claim indicates which authentication methods were used to authenticate the principal asserted in the OIDC ID token. The `amr` claim is optional and isn't included in the generated ID token by default.

  The class must implement the `org.forgerock.openam.sts.rest.token.provider.oidc.OpenIdConnectTokenAuthMethodReferencesMapper` interface and must be bundled in the AM `.war` file.

---

---
title: STS instances
description: Configure PingAM Security Token Service instances to issue OIDC or SAML 2.0 tokens with customizable conditions, subjects, and authentication statements
component: pingam
version: 8.1
page_id: pingam:sts:sts-rest
canonical_url: https://docs.pingidentity.com/pingam/8.1/sts/sts-rest.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security Token Service (STS)", "Rest", "SAML 2.0"]
page_aliases: ["sts-guide:sts-rest.adoc"]
section_ids:
  sts_process_flow: STS process flow
  sts-validate: Validate input tokens
  sts-validate-username: Validate username tokens
  sts-validate-x509: Validate X.509 certificate tokens
  sts-validate-oidc: Validate OIDC tokens
---

# STS instances

AM's Security Token Service (STS) issues OpenID Connect v1.0 (OIDC) or SAML 2.0 tokens for a single service provider. An STS instance has the following mandatory configuration:

* **Issuer**. The issuer corresponds to the IdP `EntityID`.

* **SP EntityID**. The SP `EntityID` is used in the `AudienceRestriction` element of the `Conditions` statement of the issued assertion.

* **SP assertion consumer service URL**. The SP assertion consumer service URL is used as the `Recipient` attribute of the `subjectConfirmation` element in the `Subject` statement, which is required for bearer assertions according to the [Web SSO profile](https://docs.oasis-open.org/security/saml/v2.0/saml-profiles-2.0-os.pdf).

To support signing and encryption, each STS instance has a configuration state that specifies the location of the signing and encryption keys:

* If you use *assertion signature*, you must specify the keystore path and password and the alias and password of the `PrivateKey` used to sign the assertion.

* If you use *assertion encryption*, you must specify the keystore path and password. You must also must specify the alias of the SP's X509 certificate that includes the `PublicKey` used to encrypt the *symmetric key* that encrypts the generated assertion.

  The keystore location can be an absolute path on the local filesystem or a path relative to the AM classpath. You can choose to encrypt only the `NameID` and `AttributeStatement` attributes or the entire assertion.

Any statement that constitutes a SAML 2.0 assertion can be customized.

For each STS instance, you can provide custom plug-ins for `Conditions`, `Subject`, `AuthenticationStatements`, `AttributeStatements`, and `AuthorizationDecisionStatements`. If you specify custom plug-ins in the configuration state of the published STS instance, the custom classes are consulted to provide the specific statements. Learn more in [`org.forgerock.openam.sts.tokengeneration.saml2.statements`](../_attachments/apidocs/org/forgerock/openam/sts/tokengeneration/saml2/statements/package-summary.html).

Each STS instance must specify the authentication context (`AuthnContext`) that will be included in the `AuthenticationStatements` of the generated assertion. The `AuthnContext` lets the generated SAML 2.0 assertion specify how the assertion's subject was authenticated. For a token transformation, the `AuthnContext` is a function of the input token type.

By default, the following `AuthnContext` strings are included in the SAML 2.0 assertion generated as part of the transformation of the following input token types:

| Input token type              | `AuthnContext` string                                               |
| ----------------------------- | ------------------------------------------------------------------- |
| AM                            | `urn:oasis:names:tc:SAML:2.0:ac:classes:PreviousSession`            |
| Username Token and OIDC Token | `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport` |
| X.509 Token                   | `urn:oasis:names:tc:SAML:2.0:ac:classes:X509`                       |

|   |                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To override these default mappings, implement the `org.forgerock.openam.sts.token.provider.AuthnContextMapper` interface and specify the name of the implementation in the configuration of the published STS instance. |

Read the following specifications before you implement the STS:

* [SAML 2.0](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)

* [SAML 2.0 Errata Composite](https://www.oasis-open.org/committees/download.php/35389/sstc-saml-profiles-errata-2.0-wd-06-diff.pdf)

* [Profiles for the OASIS Security Assertion Markup Language (SAML) 2.0](https://docs.oasis-open.org/security/saml/v2.0/saml-profiles-2.0-os.pdf)

* [OpenID Connect Core 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-core-1_0.html)

The STS model illustrates a simple STS topology between a requestor, a web service, and an STS instance. The STS instance is set up with the identity provider, which has a trust relationship with the web service:

![A simple STS model.](_images/sts-generic-model-simple.png)Figure 1. STS model

## STS process flow

1. A requestor makes an access request to a web resource.

2. The web service redirects the requestor to the STS.

3. The requestor sends an HTTP(S) POST request to the STS endpoint. The request includes credentials, token input type, and desired token output type.

   The following example generates a bearer token:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --data '{
       "input_token_state": {
           "token_type": "USERNAME",
           "username": "bjensen",
           "password": "Ch4ng31t"
       },
       "output_token_state": {
           "token_type": "SAML2",
           "subject_confirmation": "BEARER"
       }
   }' \
   https://am.example.com:8443/am/rest-sts/username-transformer?_action=translate
   ```

   The following example generates an OIDC token:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --data '{
       "input_token_state": {
           "token_type": "USERNAME",
           "username": "bjensen",
           "password": "Ch4ng31t"
       },
       "output_token_state": {
           "token_type": "OPENIDCONNECT",
           "nonce":"12345678",
           "allow_access":true
       }
   }' \
   https://am.example.com:8443/am/rest-sts/username-transformer?_action=translate
   ```

4. The STS does the following:

   1. Validates the signature.

   2. Decodes the payload and verifies that the requestor issued the transaction.

   3. Validates the requestor's credentials.

   4. Creates an interim AM session and, optionally, creates a CTS token for the session.

   5. Issues a token to the requestor.

   6. Invalidates the interim AM session, if configured.

5. The requestor is redirected to the web service and presents its token to the web service.

6. The web service does the following:

   1. Validates the signature and decodes the payload.

   2. Verifies that the requestor issued the request.

   3. Extracts and validates the token and processes the request.

7. If a CTS token was created for the session, the web service can call the STS to invalidate the token and the corresponding AM session.

## Validate input tokens

STS token transformations validate input tokens before generating output tokens. The STS uses authentication trees to perform token validation. When deploying STS, you must configure an appropriate authentication tree to validate input tokens.

This section describes authentication configuration requirements for username, X.509, and OIDC tokens. No special authentication configuration is required when using AM session tokens as the input tokens in token transformations.

Because STS instances aren't part of a secure framework like WS-Trust, this section also discusses security considerations when sending tokens across a network to an STS instance.

In addition to configuring AM authentication to support input token validation, you must identify the authentication tree that will validate each input token type. To do so, configure the Authentication Target Mappings property in the STS instance configuration. Learn more in the [STS configuration properties](sts-configure-rest-properties.html).

### Validate username tokens

Username tokens passed to an STS instance contain the username/password combination in cleartext. Tokens can be validated using any tree that supports username/password authentication.

With usernames and passwords in cleartext, be sure to configure your deployment with an appropriate level of security. Deploy STS instances that support input username token transformations over TLS.

### Validate X.509 certificate tokens

STS instances can obtain X.509 certificates used as input tokens in two ways:

* From the header key defined in the STS instance's Client Certificate Header Key property. In this case, STS also confirms the request came from a host specified in the Trusted Remote Hosts property.

* From the `jakarta.servlet.request.X509Certificate` attribute in the ServletRequest. If you don't set a header key in the Client Certificate Header Key property, the STS instance obtains the X.509 certificate from the ServletRequest.

To validate X.509 certificate tokens, an STS instance must reference a tree that includes the [Certificate Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-collector.html) and the [Certificate Validation node](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-validation.html) in the Authentication Target Mappings property.

The Certificate Validation node validates the X.509 certificate input token. The node optionally performs Certificate Revocation List (CRL) or Online Certificate Status Protocol (OCSP) checking, and can check that the specified certificate is in an LDAP datastore.

If certificates are passed to the STS using HTTP headers, you must configure the HTTP Header Name for the Client Certificate and the Trusted Remote Hosts properties in the Certificate Collector node to match the configuration of your STS instance.

### Validate OIDC tokens

To validate OIDC input tokens, an STS instance must reference a tree that includes the [OIDC ID Token Validator node](https://docs.pingidentity.com/auth-node-ref/8.1/oidc-idtoken-validator.html) in the Authentication Target Mappings property.

Configure the OIDC ID Token Validator node as follows:

* ID Token Header Name

  Specify a header. The STS instance's Target Authentication Mapping property must reference the same header.

* Token Issuer

  Specify the issuer name. Set the token issuer's discovery URL, JWK URL, or client secret in the OpenID Connect validation configuration value property.

* Audience name

  If incoming OIDC tokens contains `aud` claims, specify the valid claims in this property.

* Authorized parties

  If incoming OIDC tokens contain `azp` claims, specify valid claims in this property.

* Transformation Script

  Select a `Social Identity Provider Profile Transformation` script to map JWK claims to attributes in the identity store.

---

---
title: The Publish service
description: Publish Security Token Service instances programmatically using the REST endpoint with HTTP POST, GET, and DELETE operations
component: pingam
version: 8.1
page_id: pingam:sts:sts-publish-service
canonical_url: https://docs.pingidentity.com/pingam/8.1/sts/sts-publish-service.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security Token Service (STS)", "Rest", "Customization", "JSON"]
page_aliases: ["sts-guide:sts-publish-service.adoc"]
section_ids:
  sts-publish-rest: Publish STS instances
---

# The Publish service

To publish an STS instance, perform an HTTP POST on the `/sts-publish/rest` endpoint, specifying the `_action=create` parameter in the URL.

For example, you could publish an STS instance named `username-transformer` in the Top Level Realm as follows:

```bash
$ curl \
--request POST \
--header "iPlanetDirectoryPro: AQIC5…​" \
--header "Content-Type: application/json" \
--data '{
    "invocation_context": "invocation_context_client_sdk",
    "instance_state":
    {
        "saml2-config":
        {
            "issuer-name":"saml2-issuer",
            …​
        },
        "deployment-config":
        {
            "deployment-url-element":"username-transformer",
            "deployment-realm":"/",
            …​
        },
        "persist-issued-tokens-in-cts":"false",
        "supported-token-transforms":[{
            "inputTokenType":"USERNAME",
            "outputTokenType":"OPENIDCONNECT",
            "invalidateInterimOpenAMSession":false
        }],
        "oidc-id-token-config":{
            "oidc-issuer":"test",
            …​
        }
    }
}' \
https://am.example.com:8443/am/sts-publish/rest?_action=create
{
  "_id":"username-transformer",
  "_rev":"21939129",
  "result":"success",
  "url_element":"username-transformer"}
}
```

The `instance_state` object in the JSON payload represents the STS instance's configuration.

Find a complete example of an `instance_state` object in the sample code for the `RestSTSInstancePublisher` class in [Publish STS instances](#sts-publish-rest).

Accessing the `sts-publish` endpoint requires administrative privileges. Authenticate as an AM administrative user, such as `amAdmin`, before attempting to publish an STS instance.

In addition to publishing instances, the `sts-publish` endpoint can also return the configuration of an STS instance when you perform an HTTP GET on the endpoint for the instance, such as `/sts-publish/rest/realm/deployment-URL-element`.

Where *deployment-URL-element* is the value of the STS instance's deployment URL element, which is one of the instance's configuration properties, and *realm* is the realm in which the instance has been configured.

For example, you could obtain the configuration of an STS instance configured in the Top Level Realm with the deployment URL element `username-transformer` as follows:

```bash
$ curl \
--request GET \
--header "iPlanetDirectoryPro: AQIC5…​" \
https://am.example.com:8443/am/sts-publish/rest/username-transformer
{
   "_id":"username-transformer",
   "_rev":"-659999943",
   "username-transformer":{
      "saml2-config":{
         "issuer-name":"saml2-issuer",
         …​
      },
      "deployment-config":{
         "deployment-url-element":"username-transformer",
         …​
      },
      "persist-issued-tokens-in-cts":"false",
      "supported-token-transforms":[
         {
            "inputTokenType":"USERNAME",
            "outputTokenType":"OPENIDCONNECT",
            "invalidateInterimOpenAMSession":false
         }
      ],
      "oidc-id-token-config":{
         "oidc-issuer":"test",
         …​
      }
   }
}
```

You can delete STS instances by performing an HTTP DELETE on `/sts-publish/rest/realm/deployment-URL-element`.

## Publish STS instances

The sample code referenced in this section provides an example of how to programmatically publish STS instance. The code isn't intended to be a working example. Instead, it is a starting point that you can modify to satisfy your organization's specific requirements.

Learn about downloading and building PingAM sample source code in the following *Knowledge Base* article: [How do I access and build the sample code provided for PingAM?](https://support.pingidentity.com/s/article/How-do-I-access-and-build-the-sample-code-provided-for-PingAM).

You can find the STS code examples under `/path/to/openam-samples-external/sts-example-code`.

After publishing an STS instance programmatically, you can view the instance's configuration in the AM admin UI. The instance is ready for consumption.

Sample code is available for the following classes:

* RestSTSInstancePublisher

  The `RestSTSInstancePublisher` class exposes an API to publish, delete, and update STS instances by calling methods that perform an HTTP POST operation on the `sts-publish/rest` endpoint.

* RestSTSInstanceConfigFactory

  The `RestSTSInstancePublisher` class calls the `RestSTSInstanceConfigFactory` class to create a `RestSTSInstanceConfig` instance. `RestSTSInstanceConfig` objects encapsulate all the configuration information of an STS instance, and emit JSON values that you can post to the `sts-publish/rest` endpoint to publish an STS instance.

* STSPublishContext

  The sample `STSPublishContext` class specifies the configuration necessary to publish STS instances. The class provides a programmatic method for setting configuration properties. The same configuration properties are available through the AM admin UI under Realms > *realm name* > STS.

* CustomTokenOperationContext

  The sample `CustomTokenOperationContext` class specifies custom validators, token types, and transformations that an STS instance can support.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The sample code referenced in this section isn't compilable because it uses classes that aren't available publicly. The code provides patterns to developers familiar with the problem domain and is intended only to assist developers who want to programmatically publish STS instances.The sample code imports a number of classes, introducing dependencies. Classes imported from the AM API can remain in your code, but other imported classes must be removed and replaced with code that provides similar functionality in your environment. For example, the `RestSTSInstanceConfigFactory` class uses a constant named `CommonConstants.ADMIN_PASSWORD` from the imported `com.forgerock.openam.functionaltest.sts.frmwk.common.CommonConstants` utility class. This utility class isn't publicly available. Therefore, you need to replace this constant with another construct.The critical part of the sample code is the idioms that programmatically set all the state necessary to publish an STS instance. |
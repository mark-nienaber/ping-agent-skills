---
title: API Developer Considerations
description: The API developer builds the API that the application talks to. This developer is concerned with the protection of the API calls made and determining whether a user is authorized to make a specific API call.
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:api-developer-considerations
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/api-developer-considerations.html
revdate: September 30, 2020
---

# API Developer Considerations

The API developer builds the API that the application talks to. This developer is concerned with the protection of the API calls made and determining whether a user is authorized to make a specific API call.

The OAuth 2.0 process an API developer needs to handle is to:

* Validate a token

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In some cases the "API Developer" may be using a service bus or authorization gateway to manage access to APIs and therefore the task of validating the access token would be shifted to this infrastructure. |

---

---
title: Application Developer Considerations
description: The application developer will be responsible for the user-facing elements of the process. They will need to authenticate the user and interface with the back-end APIs.
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:application-developer-considerations
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/application-developer-considerations.html
revdate: September 30, 2020
---

# Application Developer Considerations

The application developer will be responsible for the user-facing elements of the process. They will need to authenticate the user and interface with the back-end APIs.

There are three main actions an application developer needs to handle to implement OAuth 2.0:

* Get an access token

* Use an access token

* Refresh an access token (optional)

---

---
title: Get Tokens
description: The most critical step for the application in the OAuth flow is how the client will receive an access token (and optionally a refresh token). The mechanism used to retrieve this token is called a grant type. Different grant types are more appropriate for different scenarios as we will discover in the following sections.
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:get-tokens
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/get-tokens.html
revdate: September 30, 2020
---

# Get Tokens

The most critical step for the application in the OAuth flow is how the client will receive an access token (and optionally a refresh token). The mechanism used to retrieve this token is called a grant type. Different grant types are more appropriate for different scenarios as we will discover in the following sections.

OAuth 2.0 provides four standard grant types and an extension grant type that can be used to customize the authentication and authorization process depending on the application requirements. These grant types are described in detail below.

---

---
title: "Get Tokens: Authorization Code Grant Type"
description: Authorization grant is a client redirect based flow. In this scenario:
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:authorization-code-grant-types
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/authorization-code-grant-types.html
revdate: October 1, 2020
section_ids:
  sample-client-configuration: Sample Client Configuration
  request-authorization-from-user-and-retrieve-authorization-code: Request authorization from user and retrieve authorization code
  swap-the-authorization-code-for-an-access-token: Swap the authorization code for an access token
---

# Get Tokens: Authorization Code Grant Type

Authorization grant is a client redirect based flow. In this scenario:

1. The user will be redirected to the PingFederate authorization endpoint via the user agent (i.e. web browser). This user agent will be used to authenticate the end user and allow them to grant access to the client.

2. Once the user has been authorized, and intermediate code will be granted by the authorization server and returned to the client application via the user agent.

3. Lastly, the client will swap this code for an OAuth access token.

![Oauth flow](_images/qjo1601508150512.png)

| Capability                                            |      |
| ----------------------------------------------------- | ---- |
| Browser-based end user interaction                    | Yes  |
| Can use external IDP for authentication               | Yes  |
| Requires client authentication                        | No\* |
| Requires client to have knowledge of user credentials | No   |
| Refresh token allowed                                 | Yes  |
| Access token is in context of end user                | Yes  |

|   |                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Although the authorization code grant type does not require a client secret value, there are security implications to exchanging a code for an access token without client authentication. |

## Sample Client Configuration

For the authorization code grant type example below, the following client information will be used:

| Admin Label           | OAuth2 Parameter           | Example Value                                                                                                                 |
| --------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Client ID             | client\_id                 | ac\_client                                                                                                                    |
| Client Authentication | client\_secret             | 2Federate                                                                                                                     |
| Allowed Grant Types   | response\_type grant\_type | * response\_type of "code" (code)

* grant\_type of "authorization\_code" (code)

* grant\_type of "refresh\_token" (refresh) |

## Request authorization from user and retrieve authorization code

To initiate the process, the client application will redirect the user to the authorization endpoint. This redirect will contain the applicable attributes URL encoded and included in the query string component of the URL.

Using the above parameters as an example, the application will redirect the user to the following URL:

```
https://localhost:9031/as/authorization.oauth2?client_id=ac_client&response_type=code&scope=edit&redirect_uri=sample%3A%2F%2Foauth2%2Fcode%2Fcb
```

This will initiate an authentication process using the browser (user agent). Once the user successfully completes the authorization request, they will be redirected with an authorization code to the redirect\_uri value defined in the authorization request (if included) otherwise the user will be returned to the redirect\_uri defined when the client was configured.

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | For mobile scenarios, the redirect\_uri may be a custom URL scheme that will cause the code to be returned to the native application. |

Using the example above, a successful authorization request will result in the resource owner redirected to the following URL with the authorization code included as a code query string parameter:

```
sample://oauth2/code/cb?code=XYZ...123
```

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * If the authorization request also included a state value, this will also be included on this callback.

* An error condition from the authentication / authorization process will be returned to this callback URI with error and error\_description parameters. |

The client will then extract the code value from the response and, optionally, verify that the state value matches the value provided in the authorization request

## Swap the authorization code for an access token

The final step for the client is to swap the authorization code received in the previous step for an access token that can be used to authorize access to resources. By limiting the exposure of the access token to a direct HTTPS connection between the client application and the authorization endpoint, the risk of exposing this access token to an unauthorized party is reduced.

For this to occur, the client makes a HTTP POST request to the token endpoint on the AS. This request will use the following parameters sent in the body of the request:

| Item          | Description                                                                 |
| ------------- | --------------------------------------------------------------------------- |
| grant\_type   | Required to be "authorization\_code"                                        |
| code          | The authorization code received in the previous step                        |
| redirect\_uri | If this was included in the authorization request, it MUST also be included |

This request should also authenticate as the pre-configured client using either HTTP BASIC authentication or by including the client\_id and client\_secret values in the request.

To retrieve the access token in the example, the following request will be made:

```
POST https://localhost:9031/as/token.oauth2 HTTP/1.1

Content-Type: application/x-www-form-urlencoded

Authorization: BasicYWNfY2xpZW50OjJGZWRlcmF0ZQ==

grant_type=authorization_code
  &code=XYZ...123
```

A successful response to this message will result in a 200 OK HTTP response and the access token (and optional refresh token) returned in a JSON structure in the body of the response.

```
HTTP/1.1 200 OK

Content-Type: application/json;charset=UTF-8

{
   "access_token":"zzz...yyy",
   "token_type":"Bearer",
   "expires_in":14400,
   "refresh_token":"123...789"
}
```

The application can now parse the access token and, if present, the refresh token to use for authorization to resources. If a refresh token was returned, it can be used to refresh access token once it expires.

---

---
title: "Get Tokens: Client Credentials Grant Type"
description: The client credentials type works in a similar way to the ROPC grant type and is used to provide an access token to a client based on the credentials or the client, not the resource owner. In this grant type, the client credentials are swapped for an access token (step 1 below).
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:client-credentials-grant-type
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/client-credentials-grant-type.html
revdate: September 30, 2020
section_ids:
  sample-client-configuration: Sample Client Configuration
  getting-the-token: Getting the Token
---

# Get Tokens: Client Credentials Grant Type

The client credentials type works in a similar way to the ROPC grant type and is used to provide an access token to a client based on the credentials or the client, not the resource owner. In this grant type, the client credentials are swapped for an access token (step 1 below).

![Oauth cc flow](_images/qok1601508155833.png)

| Capability                                            |     |
| ----------------------------------------------------- | --- |
| Browser-based end user interaction                    | No  |
| Can use external IDP for authentication               | No  |
| Requires client authentication                        | Yes |
| Requires client to have knowledge of user credentials | No  |
| Refresh token allowed                                 | No  |
| Access token is in context of end user                | No  |

## Sample Client Configuration

For the client credentials example below, the following client information will be used:

| Admin Label           | OAuth2 Parameter | Example Value                        |
| --------------------- | ---------------- | ------------------------------------ |
| Client ID             | client\_id       | cc\_client                           |
| Client Authentication | client\_secret   | 2Federate                            |
| Allowed Grant Types   | grant\_type      | grant\_type of "client\_credentials" |
| Scope Settings        | scope            | edit                                 |

## Getting the Token

The client makes a request (HTTP POST) to the token endpoint with the client credentials presented as HTTP Basic authentication:

```
POST https://localhost:9031/as/token.oauth2 HTTP/1.1

Content-Type: application/x-www-form-urlencoded

Authorization: Basic Y2NfY2xpZW50OjJGZWRlcmF0ZQ==

grant_type=client_credentials
  &scope=edit
```

|   |                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------- |
|   | The client credentials can also be provided using the client\_id and client\_secret parameters in the contents of the POST. |

The client will receive a response to this request. If successful, a 200 OK response will be received and the access token will be returned in a JSON structure. A refresh token will NOT be returned to the client.

```
HTTP/1.1 200 OK

Content-Type: application/json;charset=UTF-8

{
  "access_token":"zzz...yyy",
  "token_type":"Bearer",
  "expires_in":14400,
}
```

---

---
title: "Get Tokens: Extension Grants"
description: The extension grant type provides support for additional grant types extending the OAuth2.0 specifications. An example is the use of the SAML 2.0 Bearer extension grant. In this grant type, a SAML assertion (indicated by step 1 below, however the process used to acquire this SAML assertion is out of scope of this document) can be exchanged for an OAuth 2.0 access token (step 2).
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:extension-grants
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/extension-grants.html
revdate: September 30, 2020
section_ids:
  sample-client-configuration: Sample Client Configuration
  getting-a-token: Getting a Token
---

# Get Tokens: Extension Grants

The extension grant type provides support for additional grant types extending the OAuth2.0 specifications. An example is the use of the SAML 2.0 Bearer extension grant. In this grant type, a SAML assertion (indicated by step 1 below, however the process used to acquire this SAML assertion is out of scope of this document) can be exchanged for an OAuth 2.0 access token (step 2).

![Oauth saml flow](_images/gan1601508160586.png)

| Capability                                            |        |
| ----------------------------------------------------- | ------ |
| Browser-based end user interaction                    | No1    |
| Can use external IDP for authentication               | Yes2   |
| Requires client authentication                        | No     |
| Requires client to have knowledge of user credentials | No     |
| Refresh token allowed                                 | No     |
| Access token is in context of end user                | Maybe3 |

1 Although the grant type does not allow for user interaction, the process to generate the SAML assertion used in this flow can involve user interaction.

2 As long as the PingFederate AS is able to verify the SAML assertion, this assertion can be generated from a foreign STS.

3 Access token will be in the context of the subject of the SAML assertion, which may be an end-user a service or the client itself.

## Sample Client Configuration

For the SAML bearer extension grant type example below, the following client information will be used:

| Admin Label           | OAuth2 Parameter | Example Value                                                  |
| --------------------- | ---------------- | -------------------------------------------------------------- |
| Client ID             | client\_id       | saml\_client                                                   |
| Client Authentication | client\_secret   | 2Federate                                                      |
| Allowed Grant Types   | grant\_type      | grant\_type of "urn:ietf:params:oauth:grant-type:saml2-bearer" |

## Getting a Token

At this stage, the client has a SAML assertion that it needs to exchange for an OAuth 2.0 access token. The process in which the client received the assertion is out of scope (i.e. bootstrap assertion, STS token exchange), however the client would Base64 URL encode the assertion and include it in a HTTP POST to the token endpoint.

For the example below, the following SAML assertion (abbreviated for readability) was received by the client and is are used to request an access token:

```
PHNhbWw6QXNzZXJ0aW9uIElEPSJTdXdCSDdiQjM3cWVmT0tycmlaZkc3Y09H
...
Pjwvc2FtbDpBc3NlcnRpb24-
```

```
POST https://localhost:9031/as/token.oauth2 HTTP/1.1

Content-Type: application/x-www-form-urlencoded

Authorization: Basic c2FtbF9jbGllbnQ6MkZlZGVyYXRl

grant_type= urn:ietf:params:oauth:grant-type:saml2-bearer&assertion=
PHNhbWw6QXNzZXJ0aW9uIElEPSJTdXdCSDdiQjM3cWVmT0tycmlaZkc3Y09H...Pjwvc2FtbDpBc3NlcnRpb24-&scope=edit
```

|   |                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------- |
|   | The client credentials can also be provided using the client\_id and client\_secret parameters in the contents of the POST. |

The client will receive a response to this request. If successful, a 200 OK response will be received and the access token will be returned in a JSON structure. A refresh token will NOT be returned to the client.

```
HTTP/1.1 200 OK

Content-Type: application/json;charset=UTF-8

{
  "access_token":"zzz...yyy",
  "token_type":"Bearer",
  "expires_in":14400
}
```

---

---
title: "Get Tokens: Implicit Grant Type"
description: The implicit grant is similar to an authorization code grant, however the user agent will receive an access token directly from an authorization request (rather than swapping an intermediate authorization code).
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:implicit-grant-type
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/implicit-grant-type.html
revdate: September 30, 2020
section_ids:
  sample-client-configuration: Sample Client Configuration
  getting-the-token: Getting the Token
---

# Get Tokens: Implicit Grant Type

The implicit grant is similar to an authorization code grant, however the user agent will receive an access token directly from an authorization request (rather than swapping an intermediate authorization code).

In this flow,

* the user requests authentication and authorization via the user agent (step 1 below). If authorized, the authorization server will redirect the user to a URL containing the access token in a URL fragment.

* The client can then parse this from the URL (step 2) to use for requests to protected resources.

![Oauth implicit flow](_images/blg1601508153400.png)

This grant type is suitable for clients that are unable to keep a secret (i.e. client-side applications like JavaScript). The client is mapped to the authorization server via the redirect\_uri, as there is no client secret to authenticate the client, the access token will be sent to a specific URL pre-negotiated between the client and the authorization server.

As the access token is provided to the client in the request URI, it is inherently less secure than the authorization code grant type. For this reason, an implicit grant type cannot take advantage of refresh tokens. Only access tokens can be provided via this grant type.

| Capability                                            |     |
| ----------------------------------------------------- | --- |
| Browser-based end user interaction                    | Yes |
| Can use external IDP for authentication               | Yes |
| Requires client authentication                        | No  |
| Requires client to have knowledge of user credentials | No  |
| Refresh token allowed                                 | No  |
| Access token is in context of end user                | Yes |

## Sample Client Configuration

For the implicit grant type example below, the following client information will be used:

| Admin Label         | OAuth2 Parameter | Example Value             |
| ------------------- | ---------------- | ------------------------- |
| Client ID           | client\_id       | im\_client                |
| Allowed Grant Types | response\_type   | response\_type of "token" |
| Redirect URIs       | redirect\_uri    | sample://oauth2/code/cb   |
| Scope Settings      | scope            | edit                      |

## Getting the Token

To initiate the process, the client application will redirect the user to the authorization endpoint. This redirect will contain the applicable attributes URL encoded and included in the query string component of the URL.

Using the above parameters as an example, the application will redirect the user to the following URL:

```
https://localhost:9031/as/authorization.oauth2?client_id=im_client&response_type=token&scope=edit&redirect_uri=sample%3A%2F%2Foauth2%2Fimplicit%2Fcb
```

This will initiate an authentication process using the browser (user agent). Once the user has authenticated and approved the authorization request they will be redirected to the configured URI with the access token included as a fragment of the URL. A refresh token will NOT be returned to the client:

```
sample://oauth2/implicit/cb#access_token=zzz...yyy&token_type=bearer&expires_in=14400
```

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * For mobile scenarios, the redirect\_uri may be a custom URL scheme which will cause the access token to be returned to the native application.

* The implicit response is returned via a URL fragment. The fragment is only visible from client-side code. Therefore if you need to parse the values from server-side code, you must post the values to the server for parsing. |

---

---
title: "Get Tokens: Resource Owner Password Credentials"
description: The ROPC grant type can be used in scenarios where an interactive user agent is not available, where specific design requirements warrant the use of a native application login interface, or for legacy reasons (i.e. retro-fitting a login form for OAuth2). In the ROPC grant type, the client captures the user credentials (step 1 below) and uses those credentials to swap for an access token (step 2).
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:resource-owner-password-credentials
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/resource-owner-password-credentials.html
revdate: September 30, 2020
section_ids:
  sample-client-configuration: Sample Client Configuration
  getting-the-tokens: Getting the Tokens
---

# Get Tokens: Resource Owner Password Credentials

The ROPC grant type can be used in scenarios where an interactive user agent is not available, where specific design requirements warrant the use of a native application login interface, or for legacy reasons (i.e. retro-fitting a login form for OAuth2). In the ROPC grant type, the client captures the user credentials (step 1 below) and uses those credentials to swap for an access token (step 2).

![Oauth ropc flow](_images/amt1601508158196.png)

| Capability                                            |     |
| ----------------------------------------------------- | --- |
| Browser-based end user interaction                    | No  |
| Can use external IDP for authentication               | No  |
| Requires client authentication                        | No  |
| Requires client to have knowledge of user credentials | Yes |
| Refresh token allowed                                 | Yes |
| Access token is in context of end user                | Yes |

## Sample Client Configuration

For the resource owner password credentials grant type example below, the following client information will be used:

| Admin Label           | OAuth2 Parameter           | Example Value                                                                   |
| --------------------- | -------------------------- | ------------------------------------------------------------------------------- |
| Client ID             | client\_id                 | ro\_client                                                                      |
| Client Authentication | client\_secret             | 2Federate                                                                       |
| Allowed Grant Types   | response\_type grant\_type | * grant\_type of "password" (ropc)

* grant\_type of "refresh\_token" (refresh) |

## Getting the Tokens

At this stage, the client displays a login form to the user and collects the credentials (i.e. username/password) and defined scope if required from the resource owner (user) and makes a HTTP POST to the token endpoint.

For the example below, the following credentials were received by the client and are used to request an access token:

|   |                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The credentials passed via the Resource Owner Password Credential flow are processed through a PingFederate Password Credential Validator. These credentials do not have to be a username and password, they could be for example a username / PIN combination or another credential that is validated by a PCV. |

```
POST https://localhost:9031/as/token.oauth2 HTTP/1.1

Content-Type: application/x-www-form-urlencoded

Authorization: Basic cm9fY2xpZW50OjJGZWRlcmF0ZQ==

grant_type=password&username=joe&password=2Federate&scope=edit
```

If successful, the client will receive a 200 OK response to this request and the access token (and optional refresh token) will be returned in a JSON structure:

```
HTTP/1.1 200 OK

Content-Type: application/json;charset=UTF-8

{
  "access_token":"zzz...yyy",
  "token_type":"Bearer",
  "expires_in":14400,
  "refresh_token":"123...789"
}
```

|   |                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | An error condition from the authentication / authorization process will be returned to this callback URI with error and error\_description parameters. |

The application can now parse the access token and, if present, the refresh token to use for authorization to resources. If a refresh token was returned, it can be used to refresh access token once it expires.

---

---
title: OAuth 2.0 Developer Guide
description: This document provides a developer overview of the OAuth 2.0 protocol. It provides an overview of the processes an application developer and an API developer need to consider to implement the OAuth 2.0 protocol.
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:index
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/index.html
revdate: May 3, 2021
page_aliases: ["dev_oauth_2_overview.adoc"]
---

# OAuth 2.0 Developer Guide

This document provides a developer overview of the OAuth 2.0 protocol. It provides an overview of the processes an application developer and an API developer need to consider to implement the OAuth 2.0 protocol.

Explanations and code examples are provided for "quick win" integration efforts. As such they are incomplete and meant to complement existing documentation and specifications.

This document assumes familiarity with OAuth 2.0 protocol and PingFederate. For more information about OAuth 2.0, refer to:

* PingFederate Administrator's Manual

* OAuth 2.0 RFC 6749

The samples described in this document use the OAuth2 Playground sample application available for download from the products page on pingidentity.com.

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This document explains a number of manual processes to request and validate the OAuth tokens. While the interactions are simple, PingFederate is compatible with many 3rd party OAuth client libraries that may simplify development effort. |

![Oauth overview](_images/lid1601508147724.png)

The OAuth 2.0 protocol uses a number of actors to achieve the main tasks of getting an access token and using an access token. In addition, optional steps of refreshing this access token and validating the access token are also described.

The main actors involved are:

|                           |                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| User or Resource Owner    | The actual end user, responsible for authentication and to provide consent to share their resources with the requesting client.                        |
| User Agent                | The user's browser. Used for redirect-based flows where the user must authenticate and optionally provide consent to share their resources.            |
| Client                    | The client application that is requesting an access token on behalf of the end user.                                                                   |
| Authorization Server (AS) | The PingFederate server that authenticates the user and/or client, issues access tokens and tracks the access tokens throughout their lifetime.        |
| Resource Server (RS)      | The target application or API that provides the requested resources. This actor will validate an access token to provide authorization for the action. |

---

---
title: Refresh the Token
description: If a refresh token was requested along with the access token, then the refresh token can be used to request a new access token without having to ask the user to re-authenticate. If the refresh token is still valid, then a new access token and refresh token will be returned to the client.
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:refresh-the-token
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/refresh-the-token.html
revdate: September 30, 2020
section_ids:
  sample-client-configuration: Sample Client Configuration
  refreshing-the-token: Refreshing the Token
---

# Refresh the Token

If a refresh token was requested along with the access token, then the refresh token can be used to request a new access token without having to ask the user to re-authenticate. If the refresh token is still valid, then a new access token and refresh token will be returned to the client.

If the refresh token has been invalidated for any reason, then the client must require the user to re-authenticate to retrieve a new access token. The reasons for refresh tokens becoming invalid are:

* Refresh token has expired;

* Refresh token has been administratively revoked (separation / security reasons);

* User has explicitly revoked the refresh token

To refresh a token, the access token must have been requested with a grant type that supports refresh tokens (authorization code or resource owner password credentials). A request will then be made to the token endpoint with the grant\_type parameter set to "refresh\_token".

|   |                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A new access token can be requested with a scope of equal or lesser value than the original access token request. Refreshing an access token with additional scopes will return an error. If the scope parameter is omitted, then access token will be valid for the original request scope. |

## Sample Client Configuration

For the refresh token example below, the client configuration for the authorization code grant type from above will be used to refresh the token:

| Admin Label           | OAuth2 Parameter           | Example Value                                                                                                                 |
| --------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Scope Settings        | scope                      | edit                                                                                                                          |
| Client ID             | client\_id                 | ac\_client                                                                                                                    |
| Client Authentication | client\_secret             | 2Federate                                                                                                                     |
| Allowed Grant Types   | response\_type grant\_type | * response\_type of "code" (code)

* grant\_type of "authorization\_code" (code)

* grant\_type of "refresh\_token" (refresh) |

## Refreshing the Token

The following request is made by the client:

```
POST https://localhost:9031/as/token.oauth2 HTTP/1.1

Content-Type: application/x-www-form-urlencoded

Authorization: Basic YWNfY2xpZW50OjJGZWRlcmF0ZQ==

grant_type=refresh_token&refresh_token=123...789
```

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A token can only be refreshed with the same or a lesser scope than the original token issued. If the token is being refreshed with the same scope as the original request, the scope parameter can be omitted. If a greater scope is required, the client must re-authenticate the user. |

A successful response to this message will result in a 200 OK HTTP response and the following JSON structure in the body of the response:

```
HTTP/1.1 200 OK

Content-Type: application/json;charset=UTF-8

{
  "access_token":"aaa...ccc",
  "token_type":"Bearer",
  "expires_in":14400,
  "refresh_token":"456...321"
}
```

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Depending on the PingFederate configuration, the client could be configured to roll the refresh token returned from a refresh token request. i.e. a new refresh token is returned and the original refresh token is invalidated. |

---

---
title: Use the Token
description: An access token can then be used as an authorization token to configured web services. To use an access token to access a protected resource, the access token must be passed to the resource server.
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:use-the-token
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/use-the-token.html
revdate: September 30, 2020
section_ids:
  using-a-token: Using a Token
---

# Use the Token

An access token can then be used as an authorization token to configured web services. To use an access token to access a protected resource, the access token must be passed to the resource server.

The client should use a bearer authorization method as defined in RFC 6750 to present the access token to the resource. The most common approach is to use the HTTP Authorization header and include the access token as a Bearer authorization credential, however RFC 6750 also defines mechanisms for presenting an access token via query string and in a post body.

In the diagram below, the client presents the OAuth 2.0 access token to the protected resource (step 1). The resource then validates the access token before returning the requested resource (if authorized).

![Oauth use a token](_images/vqo1601508164584.png)

## Using a Token

For example, to enact a GET request on a REST web service, given an access token AAA…​ZZZ, the client makes the following HTTP request:

```
GET https://api.company.com/user HTTP/1.1
Authorization: Bearer AAA...ZZZ
```

This will provide the access token to the resource server, which can then validate the token, verify the scope or the request, the identity of the resource owner and the client and perform the appropriate action if authorized.

---

---
title: Validate the Token
description: For an API developer to integrate with OAuth 2.0, the resource must accept and validate the OAuth 2.0 access token (step 1 below). Once the token has been received, the resource can then validate the access token against the PingFederate authorization server (step 2). The response from the access token validation will include attributes that the resource can use for authorization decisions.
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:validate-the-token
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/validate-the-token.html
revdate: September 30, 2020
section_ids:
  sample-client-configuration: Sample Client Configuration
  validating-the-token: Validating the Token
---

# Validate the Token

For an API developer to integrate with OAuth 2.0, the resource must accept and validate the OAuth 2.0 access token (step 1 below). Once the token has been received, the resource can then validate the access token against the PingFederate authorization server (step 2). The response from the access token validation will include attributes that the resource can use for authorization decisions.

![Oauth use a token](_images/vqo1601508164584.png)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * This section will demonstrate the manual method of validating an access token through code. This effort could also be handled by an API gateway / service bus architecture or by the API validating a JWT formatted token internally.

* The OAuth 2.0 specifications do not define a standard mechanism for access token validation. The process described in this section is specific to a PingFederate implementation. |

## Sample Client Configuration

For the access token validation example below, the following client information will be used:

| Admin Label           | OAuth2 Parameter | Example Value                                                                                                                    |
| --------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Redirect URIs         | redirect\_uri    | sample://oauth2/code/cb                                                                                                          |
| Scope Settings        | scope            | edit                                                                                                                             |
| Refresh Token         | refresh\_token   | 123…​789                                                                                                                         |
| Client ID             | client\_id       | rs\_client                                                                                                                       |
| Client Authentication | client\_secret   | 2Federate                                                                                                                        |
| Allowed Grant Types   | grant\_type      | Access Token Validation (Client is a Resource Server)- grant\_type of "urn:pingidentity.com:oauth2:grant\_type:validate\_bearer" |

## Validating the Token

The API first needs to receive the access token from the client as it was provided per the "Use a Token" section of this guide.

A request from a client would look similar to the following:

```
GET https://api.company.com/user HTTP/1.1
Authorization: Bearer AAA...ZZZ
```

In order to fulfill the request, the API first extracts the access token from the authorization header, then queries the token endpoint of the PingFederate AS to validate the token:

```
POST https://localhost:9031/as/token.oauth2 HTTP/1.1

Content-Type: application/x-www-form-urlencoded

Authorization: Basic cnNfY2xpZW50OjJGZWRlcmF0ZQ==

grant_type=urn:pingidentity.com:oauth2:grant_type:validate_bearer&token=AAA...ZZZ
```

A successful response to this message will result in a 200 OK HTTP response and a JSON structure in the body of the response similar to the following:

```
HTTP/1.1 200 OK

Content-Type: application/json;charset=UTF-8

{
  "access_token": { "role":"all_access" },
  "token_type":"Bearer",
  "expires_in":14400,
  "scope":"edit",
  "client_id":"ac_client"
}
```

The resource server can then use this information to make an authorization decision and allow or deny the web request.
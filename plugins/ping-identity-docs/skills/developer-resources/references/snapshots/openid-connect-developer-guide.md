---
title: Basic Client Profile
description: "The OpenID Connect 1.0 Basic Client Profile uses the OAuth 2.0 \"Authorization Code\" grant type. You will notice the flow is almost identical to the OAuth 2.0 authorization code flow with the exception of the \"openid\" scope and the tokens returned."
component: developer-resources
page_id: developer-resources:openid_connect_developer_guide:basic-client-profile
canonical_url: https://docs.pingidentity.com/developer-resources/openid_connect_developer_guide/basic-client-profile.html
revdate: October 10, 2020
page_aliases: ["dev_openid_1_client_basic.adoc"]
section_ids:
  step-1-authenticate-the-end-user-and-receive-code: "Step 1: Authenticate the End-User and Receive Code"
  step-2-exchange-the-authorization-code-for-the-tokens: "Step 2: Exchange the Authorization Code for the Tokens"
  step-3-validate-the-id-token: "Step 3: Validate the ID Token"
  step-4-retrieve-the-user-profile: "Step 4: Retrieve the User Profile"
---

# Basic Client Profile

The OpenID Connect 1.0 Basic Client Profile uses the OAuth 2.0 "Authorization Code" grant type. You will notice the flow is almost identical to the OAuth 2.0 authorization code flow with the exception of the "openid" scope and the tokens returned.

This section walks through an example authentication using the OpenID Connect Basic Client Profile. This will step through requesting the authentication of a user, receiving and validating the OpenID Connect id\_token (step 1 through 3 below) and then query the UserInfo endpoint to retrieve profile information about the user (step 4).

![wjz1602362734115](_images/wjz1602362734115.png)

This example assumes PingFederate 7.3 or higher is installed with the OAuth 2.0 Playground developer tool. The following configuration will be used:

|                              |                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------- |
| PingFederate server base URL | https\://sso.pingdeveloper.com                                                  |
| OAuth 2.0 client\_id         | ac\_oic\_client                                                                 |
| OAuth 2.0 client\_secret     | abc123DEFghijklmnop4567rstuvwxyzZYXWUT8910SRQPOnmlijhoauthplaygroundapplication |
| Application callback URI     | https\://sso.pingdeveloper.com/OAuthPlayground/case1A-callback.jsp              |

|   |                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * For native mobile applications, the callback URI may be a non-http URI. This is configured in your application settings and will cause the mobile application to be launched to process the callback.

* Also with mobile applications, the client secret is guaranteed to be secret and therefore can be omitted. The Proof Key for Code Exchange (PKCE) specification is used to mitigate this scenario. |

## Step 1: Authenticate the End-User and Receive Code

The initial user authentication request follows the OAuth2 Authorization Grant Type flow. To initiate the OpenID Connect process, the user will be redirected to the OAuth2 authorization endpoint with the "openid profile" scope value. Additional scope values can be included to return specific profile scopes. The request is made to the authorization endpoint with the following parameters:

|                |                                                                    |
| -------------- | ------------------------------------------------------------------ |
| client\_id     | ac\_oic\_client                                                    |
| response\_type | code                                                               |
| redirect\_uri  | https\://sso.pingdeveloper.com/OAuthPlayground/case1A-callback.jsp |
| scope          | openid profile                                                     |

The client will then form the authorization URL and redirect the user to this URL via their user agent (i.e. browser). This can be performed in different ways depending on the client and the desired user experience. For example, a web application can just issue a HTTP 302 redirect to the browser and redirect the user to the authorization URL. A native mobile application may launch the mobile browser and open the authorization URL. The authorization URL using the values above would be:

```
https://sso.pingdeveloper.com/as/authorization.oauth
	?client_id=ac_oic_client
	&response_type=code
	&redirect_uri=https://sso.pingdeveloper.com/OAuthPlayground/case1A-callback.jsp
	&scope=openid%20profile
```

For mobile application scenarios where it is not guaranteed that the app at the end of the redirect\_uri is the intended application, the Proof Key for Code Exchange (PKCE) specification should be used to mitigate tokens being issued to an incorrect client. The "plain" variant of PKCE involves including a code\_challenge parameter at this stage to link this authorization request with the subsequent token request (step 2 below). Therefore an example of a mobile authorization request (using com.pingidentity.developer.oauthplayground://oidc\_callback as the redirect\_uri) will be:

```
https://sso.pingdeveloper.com/as/authorization.oauth2
	?client_id=ac_oic_client
	&response_type=code
	&redirect_uri=com.pingidentity.developer.oauthplayground://oidc_callback
	&scope=openid%20profile
	&code_challenge=abcd-this-is-a-unique-per-request-value
```

The user will then be sent through the authentication process (i.e. prompted for their username/password at their IDP, authenticated via Kerberos or x509 certificate etc). Once the user authentication (and optional consent approval) is complete, the authorization code will be returned as a query string parameter to the redirect\_uri specified in the authorization request.

```
GET https://sso.pingdeveloper.com/OAuthPlayground/Case1A callback.jsp?code=ABCâ€¦XYZ HTTP/1.1
```

(or for a mobile application, this URL will be handled in according to the mobile OS - for example in iOS in the AppDelegate class using the application:handleOpenUrl:function) NOTE: An error condition from the authentication / authorization process will be returned to this callback URI with "error" and "error\_description" parameters.

## Step 2: Exchange the Authorization Code for the Tokens

Following the Authorization Code grant type defined in the OAuth 2.0 protocol, the application will then swap this authorization code at the token endpoint for the OAuth2 token(s) and the OpenID Connect ID Token as follows:

```
POST https://sso.pingdeveloper.com/as/token.oauth2 HTTP/1.1

Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&
client_id=ac_oic_client&
client_secret=abc123DEFghijklmnop4567rstuvwxyzZYXWUT8910SRQPOnmlijhoauthplaygroundapplication&
code=ABC...XYZ&
redirect_uri=https://sso.pingdeveloper.com/OAuthPlayground/case1A-callback.jsp
```

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | As the redirect\_uri was specified in the original authorization request. It is required to be sent in the token request. |

In the mobile scenario, as we are using PKCE to prove to the Authorization Server that we are the same application that initiated the authorization request, we also need to include the PKCE code\_verifier parameter and use our application's redirect\_uri:

```
POST https://sso.pingdeveloper.com/as/token.oauth2 HTTP/1.1

Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&
client_id=ac_oic_client&
client_secret=abc123DEFghijklmnop4567rstuvwxyzZYXWUT8910SRQPOnmlijhoauthplaygroundapplication&
code=ABC...XYZ&
redirect_uri=com.pingidentity.developer.oauthplayground://oidc_callback&
code_verifier=abcd-this-is-a-unique-per-request-value
```

|   |                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | An OAuth client used for mobile authentication is not likely to have a client\_secret. In this scenario, the client\_secret parameter int he request can be omitted. |

The token endpoint will respond with a JSON structure containing the OAuth2 access token, refresh token (if enabled in the OAuth client configuration) and the OpenID Connect ID token:

```
HTTP/1.1 200 OK

Content-Type: application/json;charset=UTF-8

{
	"token_type":"Bearer",
	"expires_in":7199,
	"refresh_token":"BBB...YYY",
	"id_token":"eyJhbGciOiJSUzI1NiIsImtpZCI6IjRvaXU4In0.eyJzdWIiOiJuZnlmZSIsImF1ZCI6ImFjX29pY19jbGllbnQiLCJqdGkiOi
		JIR1AwdnlxbmgwOVBjQ3MzenBHbUVsIiwiaXNzIjoiaHR0cHM6XC9cL3Nzby5tZXljbG91ZC5uZXQ6OTAzMSIsImlhdCI6MTM5MzczMDM4MCwi
		ZXhwIjoxMzkzNzMwNjgwfQ.EQeAm84Xj2lekxUMSK9H3BvoCl511JV1TWHCyQQ7vTnXcuvZYdBHE9_OpIr9gD5OHjoDrOhwVEjKUqvwwGhzBPN
		EueeY8bUgkTfIBKzUUJETSeaO1U8uH9Td0QYv7q3rRfurLhrpzubFbAIfjPOiv8jxgBjMyGEdPJ7aXtBwP_cr2RxMUzg_iBRA4cD8c4PwEOROr
		0T-xKnwZcocDZs_rYAOHFljLPgO2tX8BBePJfqUUUG46U1K4hSqo7LP3zru4BDE2wNbZyOhb2keeLjetNq2ES33YthNU9dkmHUgbtoD-Ji7kYn
		Maij3ta1OyLSB_HB-NbhQCKvjm4GT9ocm0w",
	"access_token":"AAA...ZZZ"
}
```

The application now has multiple tokens to use for authentication and authorization decisions:

|                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OAuth 2.0 access\_token   | AAA…​ZZZ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| rOAuth 2.0 refresh\_token | BBB…​YYY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| OpenID Connect id\_token  | eyJhbGciOiJSUzI1NiIsImtpZCI6IjRvaXU4In0.eyJzdWIiOiJuZnlmZSIsImF1ZCI6ImFjX29pY19jbG llbnQiLCJqdGkiOiJIR1AwdnlxbmgwOVBjQ3MzenBHbUVsIiwiaXNzIjoiaHR0cHM6XC9cL3Nzby5tZXlj bG91ZC5uZXQ6OTAzMSIsImlhdCI6MTM5MzczMDM4MCwiZXhwIjoxMzkzNzMwNjgwfQ.EQeAm84Xj2lekxU MSK9H3BvoCl511JV1TWHCyQQ7vTnXcuvZYdBHE9\_OpIr9gD5OHjoDrOhwVEjKUqvwwGhzBPNEueeY8bUgk TfIBKzUUJETSeaO1U8uH9Td0QYv7q3rRfurLhrpzubFbAIfjPOiv8jxgBjMyGEdPJ7aXtBwP\_cr2RxMUzg \_iBRA4cD8c4PwEOROr0T-xKnwZcocDZs\_rYAOHFljLPgO2tX8BBePJfqUUUG46U1K4hSqo7LP3zru4BDE2 wNbZyOhb2keeLjetNq2ES33YthNU9dkmHUgbtoD-Ji7kYnMaij3ta1OyLSB\_HB-NbhQCKvjm4GT9ocm0w |

## Step 3: Validate the ID Token

The next step is to parse the id\_token, and validate the contents. Note, that as the id\_token was received via a direct call to the token endpoint, the verification of the digital signature is optional.

Firstly, decode both the header and payload components of the JWT:

| Component | Value                                                                                                                                                                                              | Value Decoded                                                                                                                                        |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Header    | eyJhbGciOiJSUzI1NiIsImtpZCI6IjRvaXU4In0                                                                                                                                                            | \\{ "alg":"RS256", "kid":"4oiu8" }                                                                                                                   |
| Payload   | eyJzdWIiOiJuZnlmZSIsImF1ZCI6ImFjX29pY19 jbGllbnQiLCJqdGkiOiJIR1AwdnlxbmgwOVBjQ3 MzenBHbUVsIiwiaXNzIjoiaHR0cHM6XC9cL3Nzb y5tZXljbG91ZC5uZXQ6OTAzMSIsImlhdCI6MTM5 MzczMDM4MCwiZXhwIjoxMzkzNzMwNjgwfQ | \\{ "sub":"nfyfe", "aud":"ac\_oic\_client", "jti":"HGP0vyqnh09PcCs3zpGmEl", "iss":"https:\\/\\/localhost:9031", "iat":1393730380, "exp":1393730680 } |

Now we follow the guidelines in the OpenID Connect specifications (Core specification section 3.1.3.7) for ID Token Validation (see 4.3 for details on validating the id\_token)

| Step # | Test Summary                                                                                                                                | Result                                           |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| 1      | Decrypt the token (if encrypted)                                                                                                            | Token not encrypted, skip test                   |
| 2      | Verify the issuer claim (iss) matches the OP issuer value                                                                                   | Valid                                            |
| 3      | Verify the audience claim (aud) contains the OAuth2 client\_id                                                                              | Valid                                            |
| 4      | If the token contain multiple audiences, then verify that an Authorized Party claim (azp) is present                                        | Only one audience, skip test                     |
| 5      | If the azp claim is present, verify it matches the OAuth2 client\_id                                                                        | Not present, skip test                           |
| 6,7,8  | Optionally verify the digital signature (required for implicit client profile) (see section 4.4)                                            | TLS security sufficient, skip test               |
| 9      | Verify the current time is prior to the expiry claim (exp) time value                                                                       | Valid                                            |
| 10     | Client specific: Verify the token was issued within an acceptable timeframe (iat)                                                           | Valid                                            |
| 11     | If the nonce claim (nonce) is present, verify that it matches the nonce passed in the authentication request                                | Nonce was not sent in initial request, skip test |
| 12     | Client specific: Verify the Authn Context Reference claim (acr) value is appropriate                                                        | No acr value present, skip test                  |
| 13     | Client specific: If the authentication time claim (auth\_time) present, verify it is within an acceptable range                             | No auth\_time present, skip test                 |
| 14     | If the implicit client profile is used, verify that the access token hash claim (at\_hash) matches the hash of the associated access\_token | Not an implicit profile, skip test               |

The results of the ID token validation are sufficient to trust the id\_token and the user can be considered "authenticated".

## Step 4: Retrieve the User Profile

We now have an authenticated user, the next step is to request the user profile attributes so that we can personalize their application experience and render the appropriate content to the user. This is achieved by requesting the contents of the UserInfo endpoint:

```
GET https://sso.pingdeveloper.com/idp/userinfo.openid HTTP/1.1

Authorization: Bearer AAA...ZZZ
```

The response from the UserInfo endpoint will be a JSON structure with the requested OpenID Connect profile claims:

```
HTTP/1.1 200 OK

Content-Type: application/json;charset=UTF-8

{
	"sub":"nfyfe",
	"family_name":"Fyfe",
	"given_name":"Nathan",
	"nickname":"Nat",
	...[additional claims]...
}
```

Before we can be confident the response to the UserInfo reflects the authenticated user, we must also check that the subject ("sub" claim) returned from the UserInfo endpoint matches the authenticated user we received in the id\_token.

In this case, the "sub" claim in both the UserInfo response and the id\_token match so we can use the values in the UserInfo response for our application needs.

---
title: AM as OIDC provider
description: Configure PingAM as an OIDC provider and PingGateway as a relying party using AuthorizationCodeOAuth2ClientFilter
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:oidc-am
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/oidc-am.html
revdate: 2026-01-12
section_ids:
  oidc-rp-login-sampleapp: Authenticate automatically to the sample application
---

# AM as OIDC provider

This page gives an example of how to set up AM as an OIDC provider and PingGateway as a relying party for browser requests to the home page of the sample application.

The following sequence diagram shows the flow of information for a request to access the home page of the sample application. AM is the single, preregistered OIDC provider and PingGateway is the relying party:

![A request to access the home page of the sample application with AM as an OIDC provider and PingGateway as a relying party.](_images/oidc-am.svg)

Before you begin, prepare AM, PingGateway, and the sample application. Learn more in the [example installation for this guide](preface.html#preface-examples).

1. Set up AM as an OIDC provider:

   1. Select Services > Add a Service and add a Validation Service with the following Valid goto URL Resources:

      * `https://ig.example.com:8443/*`

      * `https://ig.example.com:8443/*?*`

   2. Create an OAuth 2.0 Authorization Server:

      1. Select Services > Add a Service > OAuth2 Provider.

      2. Add a service with the default values.

   3. Create an OAuth 2.0 Client to request OAuth 2.0 access tokens:

      1. Select Applications > OAuth 2.0 > Clients.

      2. Add a client with the following values:

         * Client ID: `oidc_client`

         * Client secret: `password`

         * Redirection URIs: `https://ig.example.com:8443/home/id_token/callback`

         * Scope(s): `openid`, `profile`, and `email`

      3. (Optional) On the Core tab, switch to using a client secret associated with a secret label by setting a Secret Label Identifier and mapping the label to a secret.

         To learn more, read [Create a client profile](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-register-client.html#client-secret-label-identifier) and [Map and rotate secrets](https://docs.pingidentity.com/pingam/8.1/security/secret-mapping.html) in the AM documentation.

      4. On the Advanced tab, select the following values:

         * Grant Types: `Authorization Code`

2. Set up PingGateway:

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Make sure PingGateway connects to the sample application over HTTPS with a route to access static resources.

      Learn more in [Using the sample application](../getting-started/start-sampleapp.html).

   3. Set an environment variable for `oidc_client`, and then restart PingGateway:

      ```console
      $ export OIDC_SECRET_ID='cGFzc3dvcmQ='
      ```

   4. Add the following route to PingGateway:

      * Linux

        `$HOME/.openig/config/routes/07-openid.json`

      * Windows

        `%appdata%\OpenIG\config\routes\07-openid.json`

      ```json
      {
        "name": "07-openid",
        "baseURI": "https://app.example.com:8444",
        "condition": "${find(request.uri.path, '^/home/id_token')}",
        "heap": [
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          },
          {
            "name": "AuthenticatedRegistrationHandler-1",
            "type": "Chain",
            "config": {
              "filters": [
                {
                  "name": "ClientSecretBasicAuthenticationFilter-1",
                  "type": "ClientSecretBasicAuthenticationFilter",
                  "config": {
                    "clientId": "oidc_client",
                    "clientSecretId": "oidc.secret.id",
                    "secretsProvider": "SystemAndEnvSecretStore-1"
                  }
                }
              ],
              "handler": "ForgeRockClientHandler"
            }
          }
        ],
        "handler": {
          "type": "Chain",
          "config": {
            "filters": [
              {
                "name": "AuthorizationCodeOAuth2ClientFilter-1",
                "type": "AuthorizationCodeOAuth2ClientFilter",
                "config": {
                  "clientEndpoint": "/home/id_token",
                  "failureHandler": {
                    "type": "StaticResponseHandler",
                    "config": {
                      "status": 500,
                      "headers": {
                        "Content-Type": [
                          "text/plain"
                        ]
                      },
                      "entity": "Error in OAuth 2.0 setup."
                    }
                  },
                  "registrations": [
                    {
                      "name": "oidc-user-info-client",
                      "type": "ClientRegistration",
                      "config": {
                        "clientId": "oidc_client",
                        "issuer": {
                          "name": "Issuer",
                          "type": "Issuer",
                          "config": {
                            "wellKnownEndpoint": "http://am.example.com:8088/openam/oauth2/.well-known/openid-configuration"
                          }
                        },
                        "scopes": [
                          "openid",
                          "profile",
                          "email"
                        ],
                        "authenticatedRegistrationHandler": "AuthenticatedRegistrationHandler-1"
                      }
                    }
                  ],
                  "requireHttps": false,
                  "cacheExpiration": "disabled"
                }
              }
            ],
            "handler": "ReverseProxyHandler"
          }
        }
      }
      ```

      Source: [07-openid.json](../_attachments/config/routes/07-openid.json)

      Learn how to use Studio to set up the PingGateway route in [OpenID Connect in Structured Editor](../studio-guide/examples-se.html#example-oidc-am).

      Notice the following features about the route:

      * The route matches requests to `/home/id_token`.

      * The `AuthorizationCodeOAuth2ClientFilter` enables PingGateway to act as a relying party. It uses a single client registration defined inline.

      * The filter has a base client endpoint of `/home/id_token`, which creates the following service URIs:

        * Requests to `/home/id_token/login` start the delegated authorization process.

        * Requests to `/home/id_token/callback` are expected as redirects from the OAuth 2.0 Authorization Server (OIDC provider). This is why the redirect URI in the client profile in AM is set to `https://ig.example.com:8443/home/id_token/callback`.

        * Requests to `/home/id_token/logout` remove the authorization state for the end user, and redirect to the specified URL if a `goto` parameter is provided.

          These endpoints are implicitly reserved. Attempts to access them directly can cause undefined errors.

      * For convenience in this test, `"requireHttps"` is false. In production environments, set it to true. So that you see the delegated authorization process when you make a request, `"requireLogin"` has the default value `true`.

      * The context for storing authorization state information is `${contexts.oauth2Info}`. This is where subsequent filters and handlers can find access tokens and ID token claims.

3. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/id_token>.

      The AM login page is displayed.

   2. Sign on to AM as user `demo`, password `Ch4ng31t` and let the application access user information.

      The browser displays the sample application home page.

## Authenticate automatically to the sample application

To authenticate automatically to the sample application, change the last name of the user `demo` to match the password `Ch4ng31t`, and add a StaticRequestFilter like the following to the end of the chain in `07-openid.json`:

```json
{
  "type": "StaticRequestFilter",
  "config": {
    "method": "POST",
    "uri": "https://app.example.com:8444/login",
    "form": {
      "username": [
        "${contexts.oauth2Info.userInfo.sub}"
      ],
      "password": [
        "${contexts.oauth2Info.userInfo.family_name}"
      ]
    }
  }
}
```

The StaticRequestFilter retrieves the username and password from the context, and replaces the original HTTP GET request with an HTTP POST login request containing credentials.

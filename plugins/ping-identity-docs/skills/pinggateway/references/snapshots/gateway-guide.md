---
title: AM as OIDC provider
description: Configure PingAM as an OIDC provider and PingGateway as a relying party using AuthorizationCodeOAuth2ClientFilter
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:oidc-am
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/oidc-am.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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

---

---
title: Authentication with PingAM
description: Configure authentication with PingAM in PingGateway, covering SSO, CDSSO, credential stores, and session eviction
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:sso-cdsso
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/sso-cdsso.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Configuration", "Authentication", "Single sign-on (SSO)", "Cross Domain SSO (CDSSO)", "Nodes &amp; Trees", "Password", "Sessions"]
---

# Authentication with PingAM

* [Single sign-on with PingAM](sso.html)

  * [Using the default PingAM journey](proc-sso.html)

  * [Using a specific PingAM journey](proc-sso-authservice.html)

* [Cross-domain single sign-on for PingAM](cdsso.html)

* [Password replay with AM](credentials-am.html)

* [Password replay from a database](credentials-database.html)

* [Password replay from a file](credentials-file.html)

* [Session cache eviction with PingAM](session-eviction.html)

---

---
title: Authorizing a single transaction with PingAM
description: Configure PingAM and PingGateway for transactional authorization, requiring users to confirm each access attempt with a ConfirmTransaction tree.
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:stepup-sso-trx
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/stepup-sso-trx.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
section_ids:
  update_am_settings: Update AM settings
  update_the_pinggateway_route: Update the PingGateway route
  validation: Validation
---

# Authorizing a single transaction with PingAM

Transactional authorization requires a user to perform additional actions for one-time access to a resource.

Performing the additional action successfully grants access to the protected resource, but only once. Additional attempts to access the resource require the user to perform the configured actions again.

This section builds on the example in [Stepping up the PingAM authentication level](stepup-sso-session.html), adding a simple authorization policy with a `Transaction` environment condition. Each time the user agent tries to access the protected resource, they confirm the transaction again.

## Update AM settings

Before you start, configure AM as described in [Stepping up the PingAM authentication level](stepup-sso-session.html). The PingGateway configuration is not changed.

1. In the AM admin UI, add a tree to confirm the transaction.

   1. Select [icon: user, set=fa]Authentication > Trees > + Create Tree.

   2. Name the new tree `ConfirmTransaction`.

   3. Set up the tree as in the following image:

      ![ConfirmTransaction tree](_images/ConfirmTransaction-tree.png)

      The [Choice Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/auth-node-choice-collector.html) has these settings:

      * Choices: `Yes` and `No`

      * Default Choice: `No`

      * Prompt: `Confirm transaction?`

   4. Click Save.

2. Update the policy to use the new authentication tree.

   1. Select the policy set:

      * For SSO, select Authorization > Policy Sets > PEP-SSO.

      * For CDSSO, select Authorization > Policy Sets > PEP-CDSSO.

   2. In the policy, select Environments and add another environment condition:

      * `All of`

      * Type: `Transaction`

      * Authentication strategy: `Authenticate To Tree`

      * Strategy specifier: `ConfirmTransaction`

   3. Click [icon: check, set=fa]and Save Changes.

   4. Select Resources and update the resources to point to the PingGateway endpoint for SSO or CDSSO.

      For transactional authorization with trees, AM requires authorization *through* PingGateway:

      * `https://ig.example.com:8443/home/pep-sso*`

      * `https://ig.ext.com:8443/home/pep-cdsso*`

   The summary of the policy looks similar to the following image. This example is for CSSSO:

   ![CDSSO policy summary](_images/pep-cdsso-with-transaction.png)

## Update the PingGateway route

1. Edit the route you created:

   * SSO: `04-pep.json`

   * CDSSO: `04-pep-cdsso.json`

2. Find the `PolicyEnforcementFilter-1` filter and add a [resourceUriProvider](../reference/PolicyEnforcementFilter.html#PolicyEnforcementFilter-resourceUriProvider):

   * SSO

   * CDSSO

   ```json
   {
     "name": "PolicyEnforcementFilter-1",
     "type": "PolicyEnforcementFilter",
     "config": {
       "application": "PEP-SSO",
       "ssoTokenSubject": "${contexts.ssoToken.value}",
       "amService": "AmService-1",
       "resourceUriProvider": {
         "type": "RequestResourceUriProvider",
         "config": {
           "useOriginalUri": true,
           "includeQueryParams": false
         }
       }
     }
   }
   ```

   ```json
   {
     "name": "PolicyEnforcementFilter-1",
     "type": "PolicyEnforcementFilter",
     "config": {
       "application": "PEP-CDSSO",
       "ssoTokenSubject": "${contexts.cdsso.token}",
       "amService": "AmService-1",
       "resourceUriProvider": {
         "type": "RequestResourceUriProvider",
         "config": {
           "useOriginalUri": true,
           "includeQueryParams": false
         }
       }
     }
   }
   ```

3. Save the updated route file.

## Validation

1. In your browser's privacy or incognito mode, go to the appropriate URL:

   * For SSO, go to <https://ig.example.com:8443/home/pep-sso>.

   * For CDSSO, go to <https://ig.ext.com:8443/home/pep-cdsso>.

2. Log in to AM as user `demo`, password `Ch4ng31t`.

   AM creates a session with the default authentication level `0`, and PingGateway requests a policy decision.

3. Enter the OTP verification code from the application you registered on your device.

   AM steps up the authentication level and displays a `Confirm transaction?` choice.

4. Confirm the transaction by selecting Yes and logging in.

   ![Confirm transaction](_images/confirm-transaction.png)

   AM returns a policy decision granting one-time access to the sample application. If you reload the sample application page, you must confirm the new transaction.

---

---
title: Caching PingAM access tokens
description: Configure PingGateway to cache and revoke PingAM access tokens using CacheAccessTokenResolver, reducing introspection calls to PingAM.
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:oauth2-rs-cacheatr
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/oauth2-rs-cacheatr.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
---

# Caching PingAM access tokens

This section builds on the example in [Validating PingAM access tokens with introspection](oauth2-rs-introspect.html) to cache and then revoke access tokens.

When the access token **is not** cached, PingGateway calls AM to validate the access token. When the access token **is** cached, PingGateway doesn't validate the access token with AM.

When an access token is revoked on AM, the CacheAccessTokenResolver can delete the token from the cache when both of the following conditions are true:

* The `notification` property of AmService is enabled.

* The delegate AccessTokenResolver provides the token metadata required to update the cache.

When a refresh\_token is revoked on AM, all associated access tokens are automatically and immediately revoked.

Before you start, set up and test the example in [Validating PingAM access tokens with introspection](oauth2-rs-introspect.html).

1. Add the following route to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/rs-introspect-cache.json`

   * Windows

     `%appdata%\OpenIG\config\routes\rs-introspect-cache.json`

   ```json
   {
     "name": "rs-introspect-cache",
     "condition": "${find(request.uri.path, '^/rs-introspect-cache$')}",
     "heap": [
       {
         "name": "SystemAndEnvSecretStore-1",
         "type": "SystemAndEnvSecretStore"
       },
       {
         "name": "AmService-1",
         "type": "AmService",
         "config": {
           "url": "http://am.example.com:8088/openam",
           "realm": "/",
           "agent" : {
             "username" : "ig_agent",
             "passwordSecretId" : "agent.secret.id"
           },
           "secretsProvider": "SystemAndEnvSecretStore-1"
         }
       }
     ],
     "handler": {
       "type": "Chain",
       "config": {
         "filters": [
           {
             "name": "OAuth2ResourceServerFilter-1",
             "type": "OAuth2ResourceServerFilter",
             "config": {
               "scopes": [
                 "mail",
                 "employeenumber"
               ],
               "requireHttps": false,
               "accessTokenResolver": {
                 "name": "CacheAccessTokenResolver-1",
                 "type": "CacheAccessTokenResolver",
                 "config": {
                   "enabled": true,
                   "defaultTimeout ": "1 hour",
                   "maximumTimeToCache": "1 day",
                   "amService":"AmService-1",
                   "delegate": {
                     "name": "TokenIntrospectionAccessTokenResolver-1",
                     "type": "TokenIntrospectionAccessTokenResolver",
                     "config": {
                       "amService": "AmService-1",
                       "providerHandler": {
                         "type": "Chain",
                         "config": {
                           "filters": [
                             {
                               "type": "HttpBasicAuthenticationClientFilter",
                               "config": {
                                 "username": "ig_agent",
                                 "passwordSecretId": "agent.secret.id",
                                 "secretsProvider": "SystemAndEnvSecretStore-1"
                               }
                             }
                           ],
                           "handler": {
                             "type": "Delegate",
                             "capture": "all",
                             "config": {
                               "delegate": "ForgeRockClientHandler"
                             }
                           }
                         }
                       }
                     }
                   }
                 }
               }
             }
           }
         ],
         "handler": {
           "type": "StaticResponseHandler",
           "config": {
             "status": 200,
             "headers": {
               "Content-Type": [ "text/html; charset=UTF-8" ]
             },
             "entity": "<html><body><h2>Decoded access_token: ${contexts.oauth2.accessToken.info}</h2></body></html>"
           }
         }
       }
     }
   }
   ```

   Source: [rs-introspect-cache.json](../_attachments/config/routes/rs-introspect-cache.json)

   Notice the following features of the route compared to `rs-introspect.json`, in [Validating PingAM access tokens with introspection](oauth2-rs-introspect.html):

   * The OAuth2ResourceServerFilter uses a CacheAccessTokenResolver to cache the access token, and then delegate token resolution to the TokenIntrospectionAccessTokenResolver.

   * The `amService` property in CacheAccessTokenResolver enables WebSocket notifications from AM, for events such as token revocation.

   * The TokenIntrospectionAccessTokenResolver uses a ForgeRockClientHandler and a capture decorator to capture PingGateway's interactions with AM.

2. Test token caching:

   1. In a terminal window, use a `curl` command similar to the following to retrieve an access token:

      ```console
      $ mytoken=$(curl -s \
      --user "client-application:password" \
      --data "grant_type=password&username=demo&password=Ch4ng31t&scope=mail%20employeenumber" \
      http://am.example.com:8088/openam/oauth2/access_token | jq -r ".access_token")
      ```

   2. Access the route, using the access token returned in the previous step:

      ```console
      $ curl -v \
      --cacert /path/to/secrets/ig.example.com-certificate.pem \
      --header "Authorization: Bearer ${mytoken}" \
      https://ig.example.com:8443/rs-introspect-cache
      ```

      Output

      ```
      {
       active = true,
       scope = employeenumber mail,
       client_id = client-application,
       user_id = {amDemoUn},
       token_type = Bearer,
       exp = 158...907,
       ...
      }
      ```

   3. In the route log, note that PingGateway calls AM to introspect the access token:

      ```
      POST http://am.example.com:8088/openam/oauth2/realms/root/introspect HTTP/1.1
      ```

   4. Access the route again. In the route log note that this time PingGateway doesn't call AM, because the token is cached.

   5. Disable the cache and repeat the previous steps to cause PingGateway to call AM to validate the access token for each request.

3. Test token revocation:

   1. In a terminal window, use a `curl` command similar to the following to revoke the access token obtained in the previous step:

      ```console
      $ curl --request POST \
      --data "token=${mytoken}" \
      --data "client_id=client-application" \
      --data "client_secret=password" \
      "http://am.example.com:8088/openam/oauth2/realms/root/token/revoke"
      ```

   2. Access the route using the access token and and note that the request isn't authorized because the token is revoked:

      ```console
      $ curl -v \
      --cacert /path/to/secrets/ig.example.com-certificate.pem \
      --header "Authorization: Bearer ${mytoken}" \
      https://ig.example.com:8443/rs-introspect-cache
      ```

      Output

      ```
      ...
      HTTP/1.1 401 Unauthorized
      ```

---

---
title: Client credentials grant with PingAM
description: Configure the OAuth 2.0 client credentials grant, where a service uses its own credentials to obtain access tokens from PingAM
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:oauth2-clientcredentials
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/oauth2-clientcredentials.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
---

# Client credentials grant with PingAM

This example shows how a client service accesses an OAuth 2.0-protected resource by using its OAuth 2.0 client credentials.

![A client service accesses an OAuth 2.0-protected resource](_images/ClientCredentialsOAuth2ClientFilter.svg)

1. Set up the AM as an Authorization Server:

   1. Register a PingGateway agent with the following values, as described in [Register a PingGateway agent in AM](preface.html#register-agent-am):

      * Agent ID: `ig_agent`

      * Password: `password`

      * Token Introspection: `Realm Only`

        |   |                                                                                                                   |
        | - | ----------------------------------------------------------------------------------------------------------------- |
        |   | Use secure passwords in a production environment. Consider using a password manager to generate secure passwords. |

   2. Create an OAuth 2.0 Authorization Server:

      1. Select Services > Add a Service > OAuth2 Provider.

      2. Add a service with the default values.

   3. Create an OAuth 2.0 client to request access tokens, using client credentials for authentication:

      1. Select Applications > OAuth 2.0 > Clients, and add a client with the following values:

         * Client ID : `client-service`

         * Client secret : `password`

         * Scope(s) : `client-scope`

      2. (Optional) On the Core tab, switch to using a client secret associated with a secret label by setting a Secret Label Identifier and mapping the label to a secret.

         To learn more, read [Create a client profile](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-register-client.html#client-secret-label-identifier) and [Map and rotate secrets](https://docs.pingidentity.com/pingam/8.1/security/secret-mapping.html) in the AM documentation.

      3. On the Advanced tab, select the following value:

         * Grant Types : `Client Credentials`

2. Set up PingGateway:

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Set an environment variable for the PingGateway agent password, and then restart PingGateway:

      ```console
      $ export AGENT_SECRET_ID='cGFzc3dvcmQ='
      ```

      The password is retrieved by a SystemAndEnvSecretStore, and must be base64-encoded.

   3. Add the following route to PingGateway:

      * Linux

        `$HOME/.openig/config/routes/oauth2-protected-resource.json`

      * Windows

        `%appdata%\OpenIG\config\routes\oauth2-protected-resource.json`

      ```json
      {
        "name": "oauth2-protected-resource",
        "condition": "${find(request.uri.path, '^/oauth2-protected-resource')}",
        "heap": [
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          },
          {
            "name": "AmService-1",
            "type": "AmService",
            "config": {
              "agent": {
                "username": "ig_agent",
                "passwordSecretId": "agent.secret.id"
              },
              "secretsProvider": "SystemAndEnvSecretStore-1",
              "url": "http://am.example.com:8088/openam/"
            }
          }
        ],
        "handler": {
          "type": "Chain",
          "config": {
            "filters": [
              {
                "name": "OAuth2ResourceServerFilter-1",
                "type": "OAuth2ResourceServerFilter",
                "config": {
                  "scopes": [ "client-scope" ],
                  "requireHttps": false,
                  "accessTokenResolver": {
                    "name": "TokenIntrospectionAccessTokenResolver-1",
                    "type": "TokenIntrospectionAccessTokenResolver",
                    "config": {
                      "amService": "AmService-1",
                      "providerHandler": {
                        "type": "Chain",
                        "config": {
                          "filters": [
                            {
                              "type": "HttpBasicAuthenticationClientFilter",
                              "config": {
                                "username": "ig_agent",
                                "passwordSecretId": "agent.secret.id",
                                "secretsProvider": "SystemAndEnvSecretStore-1"
                              }
                            }
                          ],
                          "handler": "ForgeRockClientHandler"
                        }
                      }
                    }
                  }
                }
              }
            ],
            "handler": {
              "type": "StaticResponseHandler",
              "config": {
                "status": 200,
                "headers": {
                  "Content-Type": [ "text/html; charset=UTF-8" ]
                },
                "entity": "<html><body><h2>Access Granted</h2></body></html>"
              }
            }
          }
        }
      }
      ```

      Source: [oauth2-protected-resource.json](../_attachments/config/routes/oauth2-protected-resource.json)

      Notice the following features of the route:

      * The route matches requests to `/oauth2-protected-resource`.

      * The `OAuth2ResourceServerFilter` expects an OAuth 2.0 access token in the header of the incoming request, with the scope `client-scope`.

      * The filter uses a TokenIntrospectionAccessTokenResolver to resolve the access token. The introspect endpoint is protected with HTTP Basic Authentication, and the `providerHandler` uses an HttpBasicAuthenticationClientFilter to provide the resource server credentials.

      * For convenience in this test, `"requireHttps"` is false. In production environments, set it to true.

      * After the filter successfully validates the access token, it creates a new context from the Authorization Server response, containing information about the access token.

      * The StaticResponseHandler returns a message that access is granted.

   4. Add the following route to PingGateway:

      * Linux

        `$HOME/.openig/config/routes/client-credentials.json`

      * Windows

        `%appdata%\OpenIG\config\routes\client-credentials.json`

      ```json
      {
        "name": "client-credentials",
        "baseURI": "http://ig.example.com:8080",
        "condition" : "${find(request.uri.path, '^/client-credentials')}",
        "heap" : [ {
          "name" : "clientSecretAccessTokenExchangeHandler",
          "type" : "Chain",
          "capture" : "all",
          "config" : {
            "filters" : [ {
              "type" : "ClientSecretBasicAuthenticationFilter",
              "config" : {
                "clientId" : "client-service",
                "clientSecretId" : "client.secret.id",
                "secretsProvider" : {
                  "type" : "Base64EncodedSecretStore",
                  "config" : {
                    "secrets" : {
                      "client.secret.id" : "cGFzc3dvcmQ="
                    }
                  }
                }
              }
            } ],
            "handler" : "ForgeRockClientHandler"
          }
        }, {
          "name" : "oauth2EnabledClientHandler",
          "type" : "Chain",
          "capture" : "all",
          "config" : {
            "filters" : [ {
              "type" : "ClientCredentialsOAuth2ClientFilter",
              "config" : {
                "tokenEndpoint" : "http://am.example.com:8088/openam/oauth2/access_token",
                "endpointHandler": "clientSecretAccessTokenExchangeHandler",
                "scopes" : [ "client-scope" ]
              }
            } ],
            "handler" : "ForgeRockClientHandler"
          }
        } ],
        "handler" : {
          "type" : "ScriptableHandler",
          "config" : {
            "type" : "application/x-groovy",
            "clientHandler" : "oauth2EnabledClientHandler",
            "source" : [ "request.uri.path = '/oauth2-protected-resource'", "return http.send(context, request);" ]
          }
        }
      }
      ```

      Source: [client-credentials.json](../_attachments/config/routes/client-credentials.json)

      Note the following features of the route:

      * The route matches requests to `/client-credentials`.

      * The ScriptableHandler rewrites the request to target the `/oauth2-protected-resource` endpoint and then calls the HTTP client that has been redefined to use the oauth2EnabledClientHandler.

      * The oauth2EnabledClientHandler calls the ClientCredentialsOAuth2ClientFilter to obtain an access token from AM.

      * The ClientCredentialsOAuth2ClientFilter calls the clientSecretAccessTokenExchangeHandler to exchange tokens on the authorization endpoint.

      * The clientSecretAccessTokenExchangeHandler calls a ClientSecretBasicAuthenticationFilter to authenticate the client through the HTTP basic access authentication scheme, and a ForgeRockClientHandler to propagate the request.

      * The route `oauth2-protected-resource.json` uses the AM introspection endpoint to resolve the access token and display its contents.

3. Test the setup:

   1. In your browser's privacy or incognito mode, go to to <https://ig.example.com:8443/client-credentials>.

   2. If you see warnings that the site isn't secure, respond to the warnings to access the site.

      A message shows that access is granted.

---

---
title: Cross-domain single sign-on for PingAM
description: Configure CDSSO between PingGateway and PingAM using CrossDomainSingleSignOnFilter to authenticate users across different domains
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:cdsso
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/cdsso.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
---

# Cross-domain single sign-on for PingAM

This page shows how to set up Cross-Domain Single Sign-On (CDSSO) for requests in a different domain:

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To require users to authenticate in the correct realm for security reasons, configure SSO or CDSSO with a PolicyEnforcementFilter that refers to an AM policy where the realm is enforced. You can find an example in [Requiring authentication to an PingAM realm](pep-sso-realm.html). |

The SSO mechanism depicted in the following diagram can be used when PingGateway and AM are running in the same domain. When PingGateway and AM are running in different domains, AM cookies aren't visible to PingGateway because of the same-origin policy.

CDSSO using the CrossDomainSingleSignOnFilter provides a mechanism to push tokens issued by AM to PingGateway running in a different domain.

The following sequence diagram shows the flow of information between PingGateway, AM, and the sample application during CDSSO. In this example, AM is running on `am.example.com`, and PingGateway is running on `ig.ext.com`.

![Flow of information for CDSSO.](_images/cdsso.svg)

**1\.** The browser sends an unauthenticated request to access the sample app.

**2-3.** PingGateway intercepts the request, and redirects the browser to AM for authentication.

**4\.** AM authenticates the user and creates a CDSSO token.

**5\.** AM responds to a successful authentication with an HTML autosubmit form containing the issued token.

**6\.** The browser loads the HTML and autosubmit form parameters to the PingGateway callback URL for the redirect endpoint.

**7\.** When `verificationSecretId` in CrossDomainSingleSignOnFilter is configured, PingGateway uses it to verify signature of AM session tokens.

When `verificationSecretId` isn't configured, PingGateway discovers and uses the AM JWK set to verify the signature of AM session tokens.

If that fails, the CrossDomainSingleSignOnFilter fails to load.

**8\.** PingGateway checks the nonce found inside the CDSSO token to confirm that the callback comes from an authentication initiated by PingGateway.

**9\.** PingGateway constructs a cookie, and fulfills it with a cookie name, path, and domain, using the CrossDomainSingleSignOnFilter property `authCookie`. The domain must match that set in the AM PingGateway agent.

**10-11.** PingGateway redirects the request back to the original URI, with the cookie, and the browser follows the redirect back to PingGateway.

**12\.** PingGateway validates the SSO token inside the CDSSO token

**13-15.** PingGateway adds the AM session info to the request, and stores the SSO token and CDSSO token in the contexts for use by downstream filters and handlers.

**16-18.** PingGateway forwards the request to the sample application, and the sample application returns the requested resource to the browser.

Before you begin, prepare AM, PingGateway, and the sample application. Learn more in the [example installation for this guide](preface.html#preface-examples).

1. Set up AM:

   1. Register a PingGateway agent with the following values, as described in [Register a PingGateway agent in AM](preface.html#register-agent-am):

      * Agent ID: `ig_agent_cdsso`

      * Password: `password`

      * Redirect URL for CDSSO: `https://ig.ext.com:8443/home/cdsso/redirect`

        |   |                                                                                                                   |
        | - | ----------------------------------------------------------------------------------------------------------------- |
        |   | Use secure passwords in a production environment. Consider using a password manager to generate secure passwords. |

   2. Select Services > Add a Service, and add a Validation Service with the following Valid goto URL Resources:

      * `https://ig.ext.com:8443/*`

      * `https://ig.ext.com:8443/*?*`

   3. Select Configure > Global Services > Platform, and add `example.com` as an AM cookie domain.

      By default, AM sets host-based cookies. After authentication with AM, requests can be redirected to AM instead of to the resource.

2. Set up PingGateway:

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Make sure PingGateway connects to the sample application over HTTPS with a route to access static resources.

      Learn more in [Using the sample application](../getting-started/start-sampleapp.html).

   3. Add the following `session` configuration to `admin.json`.

      This ensures the browser passes the session cookie in the form-POST to the redirect endpoint (step 6 of [Information flow during CDSSO](#figure-cdsso-auth)):

      ```
      {
        "connectors": […​],
        "session": {
          "type": "InMemorySessionManager",
          "config": {
            "cookie": {
              "sameSite": "none",
              "secure": true
            }
          }
        },
        "heap": […​]
      }
      ```

      This step is required for the following reasons:

      * When `sameSite` is `strict` or `lax`, the browser doesn't send the session cookie, which contains the nonce used in validation. If PingGateway doesn't find the nonce, it assumes that the authentication failed.

      * When `secure` is `false`, the browser is likely to reject the session cookie.

        Learn more in [AdminHttpApplication (`admin.json`)](../reference/AdminHttpApplication.html).

   4. Set an environment variable for the PingGateway agent password, and then restart PingGateway:

      ```console
      $ export AGENT_SECRET_ID='cGFzc3dvcmQ='
      ```

      The password is retrieved by a SystemAndEnvSecretStore, and must be base64-encoded.

   5. Add the following route to PingGateway:

      * Linux

        `$HOME/.openig/config/routes/cdsso.json`

      * Windows

        `%appdata%\OpenIG\config\routes\cdsso.json`

      ```json
      {
        "name": "cdsso",
        "baseURI": "https://app.example.com:8444",
        "condition": "${find(request.uri.path, '^/home/cdsso')}",
        "heap": [
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          },
          {
            "name": "AmService-1",
            "type": "AmService",
            "config": {
              "url": "http://am.example.com:8088/openam",
              "realm": "/",
              "agent": {
                "username": "ig_agent_cdsso",
                "passwordSecretId": "agent.secret.id"
              },
              "secretsProvider": "SystemAndEnvSecretStore-1",
              "sessionCache": {
                "enabled": false
              }
            }
          }
        ],
        "handler": {
          "type": "Chain",
          "config": {
            "filters": [
              {
                "name": "CrossDomainSingleSignOnFilter-1",
                "type": "CrossDomainSingleSignOnFilter",
                "config": {
                  "redirectEndpoint": "/home/cdsso/redirect",
                  "authCookie": {
                    "path": "/home",
                    "name": "ig-token-cookie"
                  },
                  "amService": "AmService-1"
                }
              }
            ],
            "handler": "ReverseProxyHandler"
          }
        }
      }
      ```

      Source: [cdsso.json](../_attachments/config/routes/cdsso.json)

      Notice the following features of the route:

      * The route matches requests to `/home/cdsso`.

      * The agent password for AmService is provided by a SystemAndEnvSecretStore in the heap.

      * Because the CrossDomainSingleSignOnFilter's `verificationSecretId` isn't configured, PingGateway discovers and uses the AM JWK set to verify the signature of AM session tokens. If that fails, the CrossDomainSingleSignOnFilter fails to load.

3. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.ext.com:8443/home/cdsso>.

      The CrossDomainSingleSignOnFilter redirects the request to AM for authentication.

   2. Sign on to AM as user `demo`, password `Ch4ng31t`.

      When you have authenticated, AM calls `/home/cdsso/redirect`, and includes the CDSSO token. The CrossDomainSingleSignOnFilter passes the request to sample app, which returns the home page.

---

---
title: CSRF protection with PingGateway
description: Configure CSRF protection with PingGateway to detect and reject forged POST, PUT, and DELETE requests using token validation
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:csrf
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/csrf.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Configuration", "Cross Site Request Forgery (CSRF)"]
---

# CSRF protection with PingGateway

In a Cross Site Request Forgery (CSRF) attack, a user unknowingly executes a malicious request on a website where they're authenticated. A CSRF attack usually includes a link or script in a web page. When a user accesses the link or script, the page executes an HTTP request on the site where the user is authenticated.

CSRF attacks interact with HTTP requests as follows:

* CSRF attacks can execute POST, PUT, and DELETE requests on the targeted server. For example, a CSRF attack can transfer funds out of a bank account or change a user's password.

* Because of same-origin policy, CSRF attacks **cannot** access any response from the targeted server.

When PingGateway processes POST, PUT, and DELETE requests, it checks a custom HTTP header in the request. If a CSRF token isn't present in the header or not valid, PingGateway rejects the request and returns a valid CSRF token in the response.

Rogue websites that attempt CSRF attacks operate in a different website domain to the targeted website. Because of same-origin policy, rogue websites can't access a response from the targeted website, and can't, therefore, access the response or CSRF token.

The following example shows the data flow when an authenticated user sends a POST request to an application protected against CSRF:

![Data flow when an authenticated user sends a POST request to an application protected against CSRF.](_images/csrf-legit.svg)

The following example shows the data flow when an authenticated user sends a POST request from a rogue site to an application protected against CSRF:

![Data flow when an authenticated user sends a POST request from a rogue site to an application protected against CSRF.](_images/csrf-ilegit.svg)

1. Set up SSO, so that AM authenticates users to the sample app through PingGateway:

   1. Set up AM and PingGateway as described in [Using the default PingAM journey](proc-sso.html).

   2. Remove the condition in `sso.json`, so that the route matches all requests:

      ```none
      "condition": "${find(request.uri.path, '^/home/sso')}"
      ```

2. Test the setup without CSRF protection:

   1. Go to <https://ig.example.com:8443/bank/index> and accept the server certificate.

   2. sign on to the sample application Bank through AM, as user `demo`, password `Ch4ng31t`.

   3. Send a bank transfer of $10 to Bob, and note that the transfer is successful.

   4. Go to <http://localhost:8081/bank/attack-autosubmit> to simulate a CSRF attack.

      |   |                                                                                                                                                                                                                   |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In deployments that use a different protocol, hostname, or port for PingGateway, append the `igUrl` parameter, as follows:```none
      http://localhost:8081/bank/attack-autosubmit?igUrl=protocol://hostname:port
      ``` |

      When you access this page, a hidden HTML form is automatically submitted to transfer $1000 to the rogue user, using the PingGateway session cookie to authenticate to the bank.

      In the bank transaction history, note that $1000 is debited.

3. Test the setup with CSRF protection:

   1. In PingGateway, replace `sso.json` with the following route:

      ```json
      {
        "name": "Csrf",
        "baseURI": "https://app.example.com:8444",
        "heap": [
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          },
          {
            "name": "AmService-1",
            "type": "AmService",
            "config": {
              "agent": {
                "username": "ig_agent",
                "passwordSecretId": "agent.secret.id"
              },
              "secretsProvider": "SystemAndEnvSecretStore-1",
              "url": "http://am.example.com:8088/openam/"
            }
          },
          {
            "name": "FailureHandler-1",
            "type": "StaticResponseHandler",
            "config": {
              "status": 403,
              "headers": {
                "Content-Type": [ "text/plain; charset=UTF-8" ]
              },
              "entity": "Request forbidden"
            }
          }
        ],
        "handler": {
          "type": "Chain",
          "config": {
            "filters": [
              {
                "name": "SingleSignOnFilter-1",
                "type": "SingleSignOnFilter",
                "config": {
                  "amService": "AmService-1"
                }
              },
              {
                "name": "CsrfFilter-1",
                "type": "CsrfFilter",
                "config": {
                  "cookieName": "iPlanetDirectoryPro",
                  "failureHandler": "FailureHandler-1"
                }
              }
            ],
            "handler": "ReverseProxyHandler"
          }
        }
      }
      ```

      Source: [csrf.json](../_attachments/config/routes/csrf.json)

      Notice the following features of the route compared to `sso.json`:

      * The CsrfFilter checks the AM session cookie for the `X-CSRF-Token` header. If a CSRF token isn't present in the header or not valid, the filter rejects the request and provides a valid CSRF token in the header.

   2. Go to <https://ig.example.com:8443/bank/index> and send a bank transfer of $10 to Alice.

      Because there is no CSRF token, PingGateway responds with an HTTP 403 and provides the token.

   3. Send the transfer again, and note that because the CSRF token is provided the transfer is successful.

   4. Go to <http://localhost:8081/bank/attack-autosubmit> to automatically send a rogue transfer.

      |   |                                                                                                                                                                                                                   |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In deployments that use a different protocol, hostname, or port for PingGateway, append the `igUrl` parameter, as follows:```none
      http://localhost:8081/bank/attack-autosubmit?igUrl=protocol://hostname:port
      ``` |

      Because there is no CSRF token, PingGateway rejects the request and provides the CSRF token. However, because the rogue site is in a different domain to `ig.example.com` it can't access the CSRF token.

---

---
title: Decisions in different domains with PingAM
description: Configure PingGateway policy enforcement for cross-domain SSO decisions with PingAM when PingGateway and PingAM are in different domains
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:pep-cdsso
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/pep-cdsso.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
---

# Decisions in different domains with PingAM

The following procedure gives an example of how to create a policy in AM and configure an agent that can request policy decisions, when PingGateway and AM are in different domains.

Before you start, set up and test the example in [Cross-domain single sign-on for PingAM](cdsso.html).

1. Set up AM:

   1. In the AM admin UI, select Applications > Agents > Identity Gateway, and change the redirect URL for `ig_agent_cdsso`:

      * Redirect URL for CDSSO : `https://ig.ext.com:8443/home/pep-cdsso/redirect`

   2. Select [icon: key, set=fa]Authorization > Policy Sets > New Policy Set, and add a policy set with the following values:

      * Id : `PEP-CDSSO`

      * Resource Types : `URL`

        * In the new policy set, add a policy with the following values:

      * Name : `CDSSO`

      * Resource Type : `URL`

      * Resource pattern : `*://*:*/*`

      * Resource value : `https://app.example.com:8444/home/pep-cdsso*`

        This policy protects the home page of the sample application.

      * On the Actions tab, add an action to allow HTTP `GET`.

      * On the Subjects tab, remove any default subject conditions, add a subject condition for all `Authenticated Users`.

2. Add the following route to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/04-pep-cdsso.json`

   * Windows

     `%appdata%\OpenIG\config\routes\04-pep-cdsso.json`

   ```json
   {
     "name": "pep-cdsso",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/home/pep-cdsso')}",
     "heap": [
       {
         "name": "SystemAndEnvSecretStore-1",
         "type": "SystemAndEnvSecretStore"
       },
       {
         "name": "AmService-1",
         "type": "AmService",
         "config": {
           "agent": {
             "username": "ig_agent_cdsso",
             "passwordSecretId": "agent.secret.id"
           },
           "secretsProvider": "SystemAndEnvSecretStore-1",
           "url": "http://am.example.com:8088/openam/"
         }
       }
     ],
     "handler": {
       "type": "Chain",
       "config": {
         "filters": [
           {
             "name": "CrossDomainSingleSignOnFilter-1",
             "type": "CrossDomainSingleSignOnFilter",
             "config": {
               "redirectEndpoint": "/home/pep-cdsso/redirect",
               "authCookie": {
                 "path": "/home",
                 "name": "ig-token-cookie"
               },
               "amService": "AmService-1"
             }
           },
           {
             "name": "PolicyEnforcementFilter-1",
             "type": "PolicyEnforcementFilter",
             "config": {
               "application": "PEP-CDSSO",
               "ssoTokenSubject": "${contexts.cdsso.token}",
               "amService": "AmService-1"
             }
           }
         ],
         "handler": "ReverseProxyHandler"
       }
     }
   }
   ```

   Source: [04-pep-cdsso.json](../_attachments/config/routes/04-pep-cdsso.json)

   |   |                                                                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When `verificationSecretId` isn't configured, PingGateway discovers and uses the AM JWK set to verify the signature of AM session tokens. If the JWK set isn't available, PingGateway doesn't verify the tokens. |

3. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.ext.com:8443/home/pep-cdsso>.

   2. If you see warnings that the site isn't secure, respond to the warnings to access the site.

      PingGateway redirects you to AM for authentication.

   3. Sign on to AM as user `demo`, password `Ch4ng31t`.

      When you have authenticated, AM redirects you back to the request URL, and PingGateway requests a policy decision. AM returns a policy decision that grants access to the sample application.

---

---
title: Decisions in the same domain with PingAM
description: Configure PingAM policy sets and a PingGateway route to enforce policy decisions when PingGateway and PingAM share the same domain
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:pep-sso
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/pep-sso.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
---

# Decisions in the same domain with PingAM

The following procedure gives an example of how to create a policy in AM and configure an agent that can request policy decisions, when PingGateway and AM are in the same domain.

Before you start, set up and test the example in [Using the default PingAM journey](proc-sso.html).

1. Set up AM:

   1. Select [icon: key, set=fa]Authorization > Policy Sets > New Policy Set, and add a policy set with the following values:

      * Id : `PEP-SSO`

      * Resource Types : `URL`

   2. In the policy set, add a policy with the following values:

      * Name : `PEP-SSO`

      * Resource Type : `URL`

      * Resource pattern : `*://*:*/*`

      * Resource value : `https://app.example.com:8444/home/pep-sso*`

        This policy protects the home page of the sample application.

   3. On the Actions tab, add an action to allow HTTP `GET`.

   4. On the Subjects tab, remove any default subject conditions, add a subject condition for all `Authenticated Users`.

2. Add the following route to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/04-pep.json`

   * Windows

     `%appdata%\OpenIG\config\routes\04-pep.json`

   ```json
   {
     "name": "pep-sso",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/home/pep-sso')}",
     "heap": [
       {
         "name": "SystemAndEnvSecretStore-1",
         "type": "SystemAndEnvSecretStore"
       },
       {
         "name": "AmService-1",
         "type": "AmService",
         "config": {
           "agent": {
             "username": "ig_agent",
             "passwordSecretId": "agent.secret.id"
           },
           "secretsProvider": "SystemAndEnvSecretStore-1",
           "url": "http://am.example.com:8088/openam/"
         }
       }
     ],
     "handler": {
       "type": "Chain",
       "config": {
         "filters": [
           {
             "name": "SingleSignOnFilter-1",
             "type": "SingleSignOnFilter",
             "config": {
               "amService": "AmService-1"
             }
           },
           {
             "name": "PolicyEnforcementFilter-1",
             "type": "PolicyEnforcementFilter",
             "config": {
               "application": "PEP-SSO",
               "ssoTokenSubject": "${contexts.ssoToken.value}",
               "amService": "AmService-1"
             }
           }
         ],
         "handler": "ReverseProxyHandler"
       }
     }
   }
   ```

   Source: [04-pep-sso.json](../_attachments/config/routes/04-pep-sso.json)

   Learn how to use Studio to set up the PingGateway route in [Policy enforcement in Structured Editor](../studio-guide/examples-se.html#example-pep-sso-se) or [Protecting a web app with Freeform Designer](../studio-guide/examples-ff.html#example-pep-sso-ff).

   Find an example route that uses `claimsSubject` instead of `ssoTokenSubject` to identify the subject in [Example policy enforcement using claimsSubject](../reference/PolicyEnforcementFilter.html#PEF-example).

3. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/pep-sso> and accept the server certificate.

      Because you haven't previously authenticated to AM, the request does not contain a cookie with an SSO token. The SingleSignOnFilter redirects you to AM for authentication.

   2. Sign on to AM as user `demo`, password `Ch4ng31t`.

      When you have authenticated, AM redirects you back to the request URL, and PingGateway requests a policy decision using the AM session cookie.

      AM returns a policy decision that grants access to the sample application.

---

---
title: Decisions with a claimsSubject and PingAM
description: Configure PingGateway to enforce a PingAM policy decision using claimsSubject to identify the subject
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:pep-claims-subject
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/pep-claims-subject.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
---

# Decisions with a claimsSubject and PingAM

This example extends [Decisions in the same domain with PingAM](pep-sso.html) to enforce a policy decision from AM using the `claimsSubject` instead of `ssoTokenSubject` to identify the subject.

Before you start, set up and test the example in [Decisions in the same domain with PingAM](pep-sso.html).

1. Set up AM:

   1. Select the policy `PEP-SSO` and add a new resource:

      * Resource Type: `URL`

      * Resource pattern: `*://*:*/*`

      * Resource value: `https://app.example.com:8444/home/pep-claims`

   2. In the same policy, add the following subject condition:

      * `Any of`

      * Type : `OpenID Connect/JwtClaim`

      * claimName : `iss`

      * claimValue : `am.example.com`

2. Add the following route to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/04-pep-claims.json`

   * Windows

     `%appdata%\OpenIG\config\routes\04-pep-claims.json`

   ```json
   {
     "name": "pep-claims",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/home/pep-claims')}",
     "heap": [
       {
         "name": "SystemAndEnvSecretStore-1",
         "type": "SystemAndEnvSecretStore"
       },
       {
         "name": "AmService-1",
         "type": "AmService",
         "config": {
           "url": "http://am.example.com:8088/openam",
           "agent": {
             "username": "ig_agent",
             "passwordSecretId": "agent.secret.id"
           },
           "secretsProvider": "SystemAndEnvSecretStore-1"
         }
       }
     ],
     "handler": {
       "type": "Chain",
       "config": {
         "filters": [
           {
             "name": "SingleSignOnFilter-1",
             "type": "SingleSignOnFilter",
             "config": {
               "amService": "AmService-1"
             }
           },
           {
             "name": "PolicyEnforcementFilter-1",
             "type": "PolicyEnforcementFilter",
             "config": {
               "application": "PEP-SSO",
               "claimsSubject": {
                 "sub": "${contexts.ssoToken.info.uid}",
                 "iss": "am.example.com"
               },
               "amService": "AmService-1"
             }
           }
         ],
         "handler": "ReverseProxyHandler"
       }
     }
   }
   ```

   Source: [04-pep-claims.json](../_attachments/config/routes/04-pep-claims.json)

3. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/pep-claims> and accept the server certificate.

   2. Log in to AM as user `demo`, password `Ch4ng31t`.

      AM returns a policy decision that grants access to the sample application.

---

---
title: Discovery and dynamic registration with PingAM
description: Configure PingGateway for OIDC discovery and dynamic client registration with PingAM, using signed JWTs to authenticate with an identity provider
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:oidc-dynamic
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/oidc-dynamic.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
---

# Discovery and dynamic registration with PingAM

OIDC defines mechanisms for discovering and dynamically registering with an identity provider that isn't known in advance, as specified in the following publications: [OpenID Connect Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html), [OpenID Connect Dynamic Client Registration](https://openid.net/specs/openid-connect-registration-1_0.html), and [OAuth 2.0 Dynamic Client Registration Protocol](https://www.rfc-editor.org/rfc/rfc7591).

In dynamic registration, issuer and client registrations are generated dynamically. They are held in memory and can be reused, but don't persist when PingGateway is restarted.

This section builds on the example in [AM as OIDC provider](oidc-am.html) to give an example of discovering and dynamically registering with an identity provider that isn't known in advance. In this example, the client sends a signed JWT to the Authorization Server.

To facilitate the example, a WebFinger service is embedded in the sample application. In a normal deployment, the WebFinger server is likely to be a service on the issuer's domain.

1. Set up a key

   1. Locate a directory for secrets and go to it:

      ```console
      $ cd /path/to/secrets
      ```

   2. Create a key:

      ```console
      $ keytool -genkey \
        -alias myprivatekeyalias \
        -keyalg RSA \
        -keysize 2048 \
        -keystore keystore.p12 \
        -storepass keystore \
        -storetype PKCS12 \
        -keypass keystore \
        -validity 360 \
        -dname "CN=ig.example.com, OU=example, O=com, L=fr, ST=fr, C=fr"
      ```

2. Set up AM:

   1. Set up AM as described in [AM as OIDC provider](oidc-am.html).

   2. Select the user `demo`, and change the last name to `Ch4ng31t`. For this example, the last name must be the same as the password.

   3. Configure the OAuth 2.0 Authorization Server for dynamic registration:

      1. Select Services > OAuth2 Provider.

      2. On the Advanced tab, add the following scopes to Client Registration Scope Allowlist: `openid`, `profile`, `email`.

      3. On the Client Dynamic Registration tab, select these settings:

         * Allow Open Dynamic Client Registration: Enabled

         * Generate Registration Access Tokens: Disabled

   4. Configure the authentication method for the OAuth 2.0 Client:

      1. Select Applications > OAuth 2.0 > Clients.

      2. Select `oidc_client`, and on the Advanced tab, select Token Endpoint Authentication Method: `private_key_jwt`.

3. Set up PingGateway:

   1. Make sure PingGateway connects to the sample application over HTTPS with a route to access static resources.

      Learn more in [Using the sample application](../getting-started/start-sampleapp.html).

   2. In the PingGateway configuration, set an environment variable for the keystore password, and then restart PingGateway:

      ```console
      $ export KEYSTORE_SECRET_ID='a2V5c3RvcmU='
      ```

      The password is retrieved by a SystemAndEnvSecretStore, and must be base64-encoded.

   3. Add the following route to PingGateway to serve the sample application .css and other static resources:

      * Linux

        `$HOME/.openig/config/routes/00-static-resources.json`

      * Windows

        `%appdata%\OpenIG\config\routes\00-static-resources.json`

      ```json
      {
        "name" : "00-static-resources",
        "baseURI" : "https://app.example.com:8444",
        "condition": "${find(request.uri.path,'^/css') or matchesWithRegex(request.uri.path, '^/.*\\\\.ico$') or matchesWithRegex(request.uri.path, '^/.*\\\\.gif$')}",
        "handler": "ReverseProxyHandler"
      }
      ```

      Source: [00-static-resources.json](../_attachments/config/routes/00-static-resources.json)

   4. Add the following script to PingGateway:

      * Linux

        `$HOME/.openig/scripts/groovy/discovery.groovy`

      * Windows

        `%appdata%\OpenIG\scripts\groovy\discovery.groovy`

      ```java
      /*
       * OIDC discovery with the sample application
       */
      response = new Response(Status.OK)
      response.getHeaders().put(ContentTypeHeader.NAME, "text/html");
      response.entity = """
      <!doctype html>
      <html>
        <head>
          <title>OpenID Connect Discovery</title>
          <meta charset='UTF-8'>
        </head>
        <body>
          <form id='form' action='/discovery/login?'>
            Enter your user ID or email address:
              <input type='text' id='discovery' name='discovery'
                placeholder='demo or demo@example.com' />
              <input type='hidden' name='goto'
                value='${contexts.idpSelectionLogin.originalUri}' />
          </form>
          <script>
            // Make sure sampleAppUrl is correct for your sample app.
            window.onload = function() {
            document.getElementById('form').onsubmit = function() {
            // Fix the URL if not using the default settings.
            var sampleAppUrl = 'http://app.example.com:8081/';
            var discovery = document.getElementById('discovery');
            discovery.value = sampleAppUrl + discovery.value.split('@', 1)[0];
            };
          };
          </script>
        </body>
      </html>""" as String
      return response
      ```

      Source: [discovery.groovy](../_attachments/scripts/groovy/discovery.groovy)

      The script transforms the input into a `discovery` value for PingGateway. This is not a requirement for deployment, only a convenience for the purposes of this example. Alternatives are described in the discovery protocol specification.

   5. Add the following route to PingGateway, replacing `/path/to/secrets/keystore.p12` with your path:

      * Linux

        `$HOME/.openig/config/routes/07-discovery.json`

      * Windows

        `%appdata%\OpenIG\config\routes\07-discovery.json`

      ```json
      {
        "heap": [
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          },
          {
            "name": "SecretsProvider-1",
            "type": "SecretsProvider",
            "config": {
              "stores": [
                {
                  "type": "KeyStoreSecretStore",
                  "config": {
                    "file": "/path/to/secrets/keystore.p12",
                    "mappings": [
                      {
                        "aliases": [ "myprivatekeyalias" ],
                        "secretId": "private.key.jwt.signing.key"
                      }
                    ],
                    "storePasswordSecretId": "keystore.secret.id",
                    "storeType": "PKCS12",
                    "secretsProvider": "SystemAndEnvSecretStore-1"
                  }
                }
              ]
            }
          },
          {
            "name": "DiscoveryPage",
            "type": "ScriptableHandler",
            "config": {
              "type": "application/x-groovy",
              "file": "discovery.groovy"
            }
          }
        ],
        "name": "07-discovery",
        "baseURI": "https://app.example.com:8444",
        "condition": "${find(request.uri.path, '^/discovery')}",
        "handler": {
          "type": "Chain",
          "config": {
            "filters": [
              {
                "name": "DynamicallyRegisteredClient",
                "type": "AuthorizationCodeOAuth2ClientFilter",
                "config": {
                  "clientEndpoint": "/discovery",
                  "requireHttps": false,
                  "requireLogin": true,
                  "failureHandler": {
                    "type": "StaticResponseHandler",
                    "config": {
                      "comment": "Trivial failure handler for debugging only",
                      "status": 500,
                      "headers": {
                        "Content-Type": [ "text/plain; charset=UTF-8" ]
                      },
                      "entity": "${contexts.oauth2Failure.error}: ${contexts.oauth2Failure.description}"
                    }
                  },
                  "loginHandler": "DiscoveryPage",
                  "discoverySecretId": "private.key.jwt.signing.key",
                  "tokenEndpointAuthMethod": "private_key_jwt",
                  "secretsProvider": "SecretsProvider-1",
                  "metadata": {
                    "client_name": "My Dynamically Registered Client",
                    "redirect_uris": [ "http://ig.example.com:8080/discovery/callback" ],
                    "scopes": [ "openid", "profile", "email" ]
                  }
                }
              },
              {
                "type": "StaticRequestFilter",
                "config": {
                  "method": "POST",
                  "uri": "https://app.example.com:8444/login",
                  "form": {
                    "username": [
                      "${contexts.oauth2Info.userInfo.name}"
                    ],
                    "password": [
                      "${contexts.oauth2Info.userInfo.family_name}"
                    ]
                  }
                }
              }
            ],
            "handler": "ReverseProxyHandler"
          }
        }
      }
      ```

      Source: [07-discovery.json](../_attachments/config/routes/07-discovery.json)

      Consider the differences with `07-openid.json`:

      * The route matches requests to `/discovery`.

      * The AuthorizationCodeOAuth2ClientFilter uses `DiscoveryPage` as the login handler, and specifies metadata to prepare the dynamic registration request.

      * `DiscoveryPage` uses a ScriptableHandler and script to provide the `discovery` parameter and `goto` parameter.

        If there is a match, then it can use the issuer's registration endpoint and avoid an additional request to look up the user's issuer using the [WebFinger](https://www.rfc-editor.org/rfc/rfc7033) protocol.

        If there is no match, PingGateway uses the `discovery` value as the `resource` for a WebFinger request using the OIDC discovery protocol.

      * PingGateway uses the `discovery` parameter to find an identity provider. PingGateway extracts the domain host and port from the value, and attempts to find a match in the `supportedDomains` lists for issuers configured for the route.

      * When `discoverySecretId` is set, the `tokenEndpointAuthMethod` is always `private_key_jwt`. Clients send a signed JWT to the Authorization Server.

        Redirects PingGateway to the end user's browser, using the `goto` parameter, after the process is complete and PingGateway has injected the OIDC user information into the context.

4. Test the setup:

   1. Log out of AM, and clear any cookies.

   2. Go to <http://ig.example.com:8080/discovery>.

   3. Enter the following email address: `demo@example.com`. The AM login page is displayed.

   4. Log in as user `demo`, password `Ch4ng31t`, and then allow the application to access user information. The sample application returns the user's page.

---

---
title: Encrypted PingAM tokens with KeyStoreSecretStore
description: Configure PingGateway to validate encrypted stateless PingAM access tokens using a KeyStoreSecretStore and StatelessAccessTokenResolver
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:oauth2-rs-stateless-encrypted
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/oauth2-rs-stateless-encrypted.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
section_ids:
  set_up_encryption_keys: Set up encryption keys
  proc-stateless-setup-keystore: Validate tokens
---

# Encrypted PingAM tokens with KeyStoreSecretStore

This page shows how to validate encrypted access tokens with the StatelessAccessTokenResolver using a [JwkSetSecretStore](../reference/JwkSetSecretStore.html).

## Set up encryption keys

1. Locate the following directories for keys, keystores, and certificates, and in a terminal create variables for them:

   * Directory where the keystore is created: `keystore_directory`

   * AM keystore directory: `am_keystore_directory`

   * PingGateway keystore directory: `ig_keystore_directory`

2. Set up keys for AM:

   1. Generate the encryption key:

      ```console
      $ keytool -genseckey \
      -alias encryption-key \
      -dname "CN=ig.example.com, OU=example, O=com, L=fr, ST=fr, C=fr" \
      -keystore "$am_keystore_directory/AM_keystore.p12" \
      -storetype PKCS12 \
      -storepass "password" \
      -keyalg AES \
      -keysize 256
      ```

   2. List the keys in the AM keystore:

      ```console
      $ keytool -list \
      -v \
      -keystore "$am_keystore_directory/AM_keystore.p12" \
      -storepass "password" \
      -storetype PKCS12
      ```

      Output

      ```
      ...
      Your keystore contains 1 entry
      Alias name: encryption-key
      ```

   3. Add a file called `keystore.pass`, with the content `password`:

      ```console
      $ cd $am_keystore_directory
      $ echo -n 'password' > keystore.pass
      ```

      |   |                                                                                                      |
      | - | ---------------------------------------------------------------------------------------------------- |
      |   | Make sure the password file contains only the password, with no trailing spaces or carriage returns. |

      The filename corresponds to the secret ID of the store password and entry password for the KeyStoreSecretStore.

   4. Restart AM.

3. Set up keys for PingGateway:

   1. Import `encryption-key` into the PingGateway keystore, with the alias `decryption-key`:

      ```console
      $ keytool -importkeystore \
      -srcalias encryption-key \
      -srckeystore "$am_keystore_directory/AM_keystore.p12" \
      -srcstoretype PKCS12 \
      -srcstorepass "password" \
      -destkeystore "$ig_keystore_directory/IG_keystore.p12" \
      -deststoretype PKCS12 \
      -destalias decryption-key \
      -deststorepass "password" \
      -destkeypass "password"
      ```

   2. List the keys in the PingGateway keystore:

      ```console
      $ keytool -list \
      -v \
      -keystore "$ig_keystore_directory/IG_keystore.p12" \
      -storepass "password" \
      -storetype PKCS12
      ```

      Output

      ```
      ...
      Your keystore contains 1 entry
      Alias name: decryption-key
      ```

   3. In the PingGateway configuration, set an environment variable for the keystore password:

      ```console
      $ export KEYSTORE_SECRET_ID='cGFzc3dvcmQ='
      ```

   4. Restart PingGateway.

## Validate tokens

1. Set up AM:

   1. Set up AM as described in [Validate tokens](oauth2-rs-stateless-signed-ksss.html#proc-oauth2-rs-stateless-signed-ksss).

   2. Add a mapping for the encryption keystore:

      1. Select [icon: eye-slash, set=fa]Secret Stores > `keystoresecretstore`.

      2. Select the Mappings tab, and add a mapping with the following values:

         * Secret Label : `am.services.oauth2.stateless.token.encryption`

         * Alias : `encryption-key`

   3. Enable token encryption on the OAuth 2.0 Authorization Provider:

      1. Select Services > OAuth2 Provider.

      2. On the Advanced tab, select Encrypt Client-Side Tokens.

2. Set up PingGateway:

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Add the following route to PingGateway, replacing `<ig_keystore_directory>`:

      * Linux

        `$HOME/.openig/config/routes/rs-stateless-encrypted.json`

      * Windows

        `%appdata%\OpenIG\config\routes\rs-stateless-encrypted.json`

      ```json
      {
        "name": "rs-stateless-encrypted",
        "condition": "${find(request.uri.path, '/rs-stateless-encrypted')}",
        "heap": [
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          },
          {
            "name": "KeyStoreSecretStore-1",
            "type": "KeyStoreSecretStore",
            "config": {
              "file": "<ig_keystore_directory>/IG_keystore.p12",
              "storeType": "PKCS12",
              "storePasswordSecretId": "keystore.secret.id",
              "entryPasswordSecretId": "keystore.secret.id",
              "secretsProvider": "SystemAndEnvSecretStore-1",
              "mappings": [
                {
                  "secretId": "stateless.access.token.decryption.key",
                  "aliases": [ "decryption-key" ]
                }
              ]
            }
          }
        ],
        "handler": {
          "type": "Chain",
          "capture": "all",
          "config": {
            "filters": [ {
              "name": "OAuth2ResourceServerFilter-1",
              "type": "OAuth2ResourceServerFilter",
              "config": {
                "scopes": [ "myscope" ],
                "requireHttps": false,
                "accessTokenResolver": {
                  "type": "StatelessAccessTokenResolver",
                  "config": {
                    "secretsProvider": "KeyStoreSecretStore-1",
                    "issuer": "http://am.example.com:8088/openam/oauth2",
                    "decryptionSecretId": "stateless.access.token.decryption.key"
                  }
                }
              }
            } ],
            "handler": {
              "type": "StaticResponseHandler",
              "config": {
                "status": 200,
                "headers": {
                  "Content-Type": [ "text/html; charset=UTF-8" ]
                },
                "entity": "<html><body><h2>Decoded access_token: ${contexts.oauth2.accessToken.info}</h2></body></html>"
              }
            }
          }
        }
      }
      ```

      Source: [rs-stateless-encrypted.json](../_attachments/config/routes/rs-stateless-encrypted.json)

      Notice the following features of the route compared to `rs-stateless-signed.json` from [Validate tokens](oauth2-rs-stateless-signed-ksss.html#proc-oauth2-rs-stateless-signed-ksss).

      * The route matches requests to `/rs-stateless-encrypted`.

      * The OAuth2ResourceServerFilter and KeyStoreSecretStore refer to the configuration for a decryption key instead of a verification key.

3. Test the setup

   1. Get an access token for the demo user, using the scope `myscope`:

      ```console
      $ mytoken=$(curl -s \
      --user "client-application:password" \
      --data "grant_type=password&username=demo&password=Ch4ng31t&scope=myscope" \
      http://am.example.com:8088/openam/oauth2/access_token | jq -r ".access_token")
      ```

   2. Display the token:

      ```console
      $ echo ${mytoken}
      ```

      Note that the token is structured as an encrypted token.

   3. Access the route by providing the token returned in the previous step:

      ```console
      $ curl -v \
      --cacert /path/to/secrets/ig.example.com-certificate.pem \
      --header "Authorization: Bearer ${mytoken}" \
      https://ig.example.com:8443/rs-stateless-encrypted
      ```

      Output

      ```
      ...
      Decoded access_token: {
      sub=demo,
      cts=OAUTH2_STATELESS_GRANT,
      ...
      ```

---

---
title: Enforce AM policy decisions
description: "Use PingGateway to enforce PingAM policy decisions: SSO, cross-domain SSO, claims-based subjects, and cache eviction"
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:pep
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/pep.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2024-07-10T14:05:34Z
---

# Enforce AM policy decisions

The following pages show how to use PingGateway to enforce AM policy decisions:

* [Decisions in the same domain with PingAM](pep-sso.html)

* [Requiring authentication to an PingAM realm](pep-sso-realm.html)

* [Decisions in different domains with PingAM](pep-cdsso.html)

* [Decisions with a claimsSubject and PingAM](pep-claims-subject.html)

* [Notifications and the PingAM policy cache](pep-evict-cache.html)

---

---
title: Example SAML v2.0 Fedlet files
description: Example SAML v2.0 Fedlet configuration files for PingGateway acting as a service provider, with PingAM and PingOne as identity providers
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:federation-example-files
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/federation-example-files.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-20T12:00:00Z
section_ids:
  am_as_idp: AM as IdP
  ping-saml-files: PingOne as IdP
---

# Example SAML v2.0 Fedlet files

PingGateway uses the PingAM Fedlet to act as a SAML v2.0 SP. This page provides example Fedlet configuration files PingGateway can use with specific IdPs.

These examples don't include settings for every possible scenario. Learn more about the Fedlet configuration in the AM documentation [Implement SAML v2.0 SPs by using Fedlets](https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-implementation-fedlet.html).

| File                          | Description                                 |
| ----------------------------- | ------------------------------------------- |
| `FederationConfig.properties` | Fedlet properties                           |
| `fedlet.cot`                  | Circle of trust for PingGateway and the IdP |
| `idp.xml`                     | Standard metadata for the IdP               |
| `idp-extended.xml`            | Metadata extensions for the IdP             |
| `sp.xml`                      | Standard metadata for the PingGateway SP    |
| `sp-extended.xml`             | Metadata extensions for the PingGateway SP  |

## AM as IdP

> **Collapse: FederationConfig.properties**
>
> The following example of `$HOME/.openig/SAML/FederationConfig.properties` defines the fedlet properties:
>
> ```properties
> #
> # DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
> #
> # Copyright (c) 2006 Sun Microsystems Inc. All Rights Reserved
> #
> # The contents of this file are subject to the terms
> # of the Common Development and Distribution License
> # (the License). You may not use this file except in
> # compliance with the License.
> #
> # You can obtain a copy of the License at
> # https://opensso.dev.java.net/public/CDDLv1.0.html or
> # opensso/legal/CDDLv1.0.txt
> # See the License for the specific language governing
> # permission and limitations under the License.
> #
> # When distributing Covered Code, include this CDDL
> # Header Notice in each file and include the License file
> # at opensso/legal/CDDLv1.0.txt.
> # If applicable, add the following below the CDDL Header,
> # with the fields enclosed by brackets [] replaced by
> # your own identifying information:
> # "Portions Copyrighted [year] [name of copyright owner]"
> #
> # $Id: FederationConfig.properties,v 1.21 2010/01/08 22:41:28 exu Exp $
> #
> # Portions Copyright 2016-2024 Ping Identity Corporation.
>
> # If a component wants to use a different datastore provider than the
> # default one defined above, it can define a property like follows:
> # com.sun.identity.plugin.datastore.class.<componentName>=<provider class>
>
> # com.sun.identity.plugin.configuration.class specifies implementation for
> # com.sun.identity.plugin.configuration.ConfigurationInstance interface.
> com.sun.identity.plugin.configuration.class=com.sun.identity.plugin.configuration.impl.FedletConfigurationImpl
>
> # Specifies implementation for
> # com.sun.identity.plugin.datastore.DataStoreProvider interface.
> # This property defines the default datastore provider.
> com.sun.identity.plugin.datastore.class.default=com.sun.identity.plugin.datastore.impl.FedletDataStoreProvider
>
> # Specifies implementation for
> # org.forgerock.openam.federation.plugin.rooturl.RootUrlProvider interface.
> # This property defines the default base url provider.
> com.sun.identity.plugin.root.url.class.default=org.forgerock.openam.federation.plugin.rooturl.impl.FedletRootUrlProvider
>
> # com.sun.identity.plugin.log.class specifies implementation for
> # com.sun.identity.plugin.log.Logger interface.
> com.sun.identity.plugin.log.class=com.sun.identity.plugin.log.impl.FedletLogger
>
> # com.sun.identity.plugin.session.class specifies implementation for
> # com.sun.identity.plugin.session.SessionProvider interface.
> com.sun.identity.plugin.session.class=com.sun.identity.plugin.session.impl.FedletSessionProvider
>
> # com.sun.identity.plugin.monitoring.agent.class specifies implementation for
> # com.sun.identity.plugin.monitoring.FedMonAgent interface.
> com.sun.identity.plugin.monitoring.agent.class=com.sun.identity.plugin.monitoring.impl.FedletAgentProvider
>
> # com.sun.identity.plugin.monitoring.saml2.class specifies implementation for
> # com.sun.identity.plugin.monitoring.FedMonSAML2Svc interface.
> com.sun.identity.plugin.monitoring.saml2.class=com.sun.identity.plugin.monitoring.impl.FedletMonSAML2SvcProvider
>
> # com.sun.identity.saml.xmlsig.keyprovider.class specified the implementation
> # class for com.sun.identity.saml.xmlsig.KeyProvider interface
> com.sun.identity.saml.xmlsig.keyprovider.class=com.sun.identity.saml.xmlsig.JKSKeyProvider
>
> # com.sun.identity.saml.xmlsig.signatureprovider.class specified the
> # implementation class for com.sun.identity.saml.xmlsig.SignatureProvider
> # interface
> com.sun.identity.saml.xmlsig.signatureprovider.class=com.sun.identity.saml.xmlsig.AMSignatureProvider
>
> com.iplanet.am.server.protocol=http
> com.iplanet.am.server.host=am.example.com
> com.iplanet.am.server.port=8080
> com.iplanet.am.services.deploymentDescriptor=/openam
> com.iplanet.am.logstatus=ACTIVE
>
> # Name of the webcontainer.
> # Even though the servlet/JSP are web container independent,
> # Access/Federation Manager uses servlet 2.3 API request.setCharacterEncoding()
> # to decode incoming non English characters. These APIs will not work if
> # Access/Federation Manager is deployed on Sun Java System Web Server 6.1.
> # We use gx_charset mechanism to correctly decode incoming data in
> # Sun Java System Web Server 6.1 and S1AS7.0. Possible values
> # are BEA6.1, BEA 8.1, IBM5.1 or IAS7.0.
> # If the web container is Sun Java System Webserver, the tag is not replaced.
> com.sun.identity.webcontainer=WEB_CONTAINER
>
> # Identify saml xml signature keystore file, keystore password file
> # key password file
> com.sun.identity.saml.xmlsig.keystore=%BASE_DIR%/security/keystores/keystore.jks
> com.sun.identity.saml.xmlsig.storepass=%BASE_DIR%/.storepass
> com.sun.identity.saml.xmlsig.keypass=%BASE_DIR%/.keypass
> com.sun.identity.saml.xmlsig.certalias=test
>
> # Type of keystore used for saml xml signature. Default is JKS.
> #
> # com.sun.identity.saml.xmlsig.storetype=JKS
>
> # Specifies the implementation class for
> # com.sun.identity.saml.xmlsig.PasswordDecoder interface.
> com.sun.identity.saml.xmlsig.passwordDecoder=com.sun.identity.fedlet.FedletEncodeDecode
>
> # The following key is used to specify the maximum content-length
> # for an HttpRequest that will be accepted by the OpenSSO
> # The default value is 16384 which is 16k
> com.iplanet.services.comm.server.pllrequest.maxContentLength=16384
>
> # The following keys are used to configure the Debug service.
> # Possible values for the key 'level' are: off | error | warning | message.
> # The key 'directory' specifies the output directory where the debug files
> # will be created.
> # Trailing spaces are significant.
> # Windows: Use forward slashes "/" separate directories, not backslash "\".
> # Windows: Spaces in the file name are allowed for Windows.
> #
> com.iplanet.services.debug.level=message
> com.iplanet.services.debug.directory=%BASE_DIR%%SERVER_URI%/debug
>
> # The following keys are used to configure the Stats service.
> # Possible values for the key 'level' are: off | file | console
> # Stats state 'file' will write to a file under the specified directory,
> # and 'console' will write into  webserver log files
> # The key 'directory' specifies the output directory where the debug files
> # will be created.
> # Trailing spaces are significant.
> # Windows: Use forward slashes "/" separate directories, not backslash "\".
> # Windows: Spaces in the file name are allowed for Windows.
> # Stats interval should be atleast 5 secs to avoid CPU saturation,
> # the product would assume any thing less than 5 secs is 5 secs.
> com.iplanet.am.stats.interval=60
> com.iplanet.services.stats.state=file
> com.iplanet.services.stats.directory=%BASE_DIR%/var/stats
>
> # The key that will be used to encrypt and decrypt passwords.
> am.encryption.pwd=@AM_ENC_PWD@
>
> # SecureRandom Properties: The key
> # "com.iplanet.security.SecureRandomFactoryImpl"
> # specifies the factory class name for SecureRandomFactory
> # Available impl classes are:
> #   com.iplanet.am.util.JSSSecureRandomFactoryImpl (uses JSS)
> #   com.iplanet.am.util.SecureRandomFactoryImpl (pure Java)
> com.iplanet.security.SecureRandomFactoryImpl=com.iplanet.am.util.SecureRandomFactoryImpl
>
> # SocketFactory properties: The key "com.iplanet.security.SSLSocketFactoryImpl"
> # specifies the factory class name for LDAPSocketFactory
> # Available classes are:
> #    com.iplanet.services.ldap.JSSSocketFactory (uses JSS)
> #    com.sun.identity.shared.ldap.factory.JSSESocketFactory    (pure Java)
> com.iplanet.security.SSLSocketFactoryImpl=com.sun.identity.shared.ldap.factory.JSSESocketFactory
>
> # Encryption: The key "com.iplanet.security.encryptor" specifies
> # the encrypting class implementation.
> # Available classes are:
> #    com.iplanet.services.util.JCEEncryption
> #    com.iplanet.services.util.JSSEncryption
> com.iplanet.security.encryptor=com.iplanet.services.util.JCEEncryption
>
> # Determines if JSS will be added with highest priority to JCE
> # Set this to "true" if other JCE providers should be used for
> # digial signatures and encryptions.
> com.sun.identity.jss.donotInstallAtHighestPriority=true
>
> # Configuration File (serverconfig.xml) Location
> com.iplanet.services.configpath=@BASE_DIR@
> ```
>
> Source: [FederationConfig.properties](../_attachments/SAML/FederationConfig.properties)

> **Collapse: fedlet.cot**
>
> The following example of `$HOME/.openig/SAML/fedlet.cot` defines a circle of trust between AM as the IdP and PingGateway as the SP:
>
> ```properties
> cot-name=Circle of Trust
> sun-fm-cot-status=Active
> sun-fm-trusted-providers=openam, sp
> sun-fm-saml2-readerservice-url=
> sun-fm-saml2-writerservice-url=
> ```
>
> Source: [fedlet.cot](../_attachments/SAML/fedlet.cot)

> **Collapse: idp.xml**
>
> The following example of `$HOME/.openig/SAML/idp.xml` defines a SAML configuration file for the AM IdP, `idp`:
>
> ```xml
> <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
> <EntityDescriptor entityID="openam" xmlns="urn:oasis:names:tc:SAML:2.0:metadata" xmlns:query="urn:oasis:names:tc:SAML:metadata:ext:query" xmlns:mdattr="urn:oasis:names:tc:SAML:metadata:attribute" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:xenc="http://www.w3.org/2001/04/xmlenc#" xmlns:xenc11="http://www.w3.org/2009/xmlenc11#" xmlns:alg="urn:oasis:names:tc:SAML:metadata:algsupport" xmlns:x509qry="urn:oasis:names:tc:SAML:metadata:X509:query" xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
>     <IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
>         <KeyDescriptor use="signing">
>             <ds:KeyInfo>
>                 <ds:X509Data>
>                     <ds:X509Certificate>
> ...
>                     </ds:X509Certificate>
>                 </ds:X509Data>
>             </ds:KeyInfo>
>         </KeyDescriptor>
>         <KeyDescriptor use="encryption">
>             <ds:KeyInfo>
>                 <ds:X509Data>
>                     <ds:X509Certificate>
> ...
>                     </ds:X509Certificate>
>                 </ds:X509Data>
>             </ds:KeyInfo>
>             <EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#rsa-oaep">
>                 <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
>                 <xenc11:MGF Algorithm="http://www.w3.org/2009/xmlenc11#mgf1sha256"/>
>             </EncryptionMethod>
>             <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc">
>                 <xenc:KeySize>128</xenc:KeySize>
>             </EncryptionMethod>
>         </KeyDescriptor>
>         <ArtifactResolutionService index="0" Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="http://am.example.com:8088/openam/ArtifactResolver/metaAlias/idp"/>
>         <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="http://am.example.com:8088/openam/IDPSloRedirect/metaAlias/idp" ResponseLocation="http://am.example.com:8088/openam/IDPSloRedirect/metaAlias/idp"/>
>         <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="http://am.example.com:8088/openam/IDPSloPOST/metaAlias/idp" ResponseLocation="http://am.example.com:8088/openam/IDPSloPOST/metaAlias/idp"/>
>         <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="http://am.example.com:8088/openam/IDPSloSoap/metaAlias/idp"/>
>         <ManageNameIDService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="http://am.example.com:8088/openam/IDPMniRedirect/metaAlias/idp" ResponseLocation="http://am.example.com:8088/openam/IDPMniRedirect/metaAlias/idp"/>
>         <ManageNameIDService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="http://am.example.com:8088/openam/IDPMniPOST/metaAlias/idp" ResponseLocation="http://am.example.com:8088/openam/IDPMniPOST/metaAlias/idp"/>
>         <ManageNameIDService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="http://am.example.com:8088/openam/IDPMniSoap/metaAlias/idp"/>
>         <NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:persistent</NameIDFormat>
>         <NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</NameIDFormat>
>         <NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat>
>         <NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</NameIDFormat>
>         <NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName</NameIDFormat>
>         <NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos</NameIDFormat>
>         <NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName</NameIDFormat>
>         <SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="http://am.example.com:8088/openam/SSORedirect/metaAlias/idp"/>
>         <SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="http://am.example.com:8088/openam/SSOPOST/metaAlias/idp"/>
>         <SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="http://am.example.com:8088/openam/SSOSoap/metaAlias/idp"/>
>         <NameIDMappingService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="http://am.example.com:8088/openam/NIMSoap/metaAlias/idp"/>
>         <AssertionIDRequestService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="http://am.example.com:8088/openam/AIDReqSoap/IDPRole/metaAlias/idp"/>
>         <AssertionIDRequestService Binding="urn:oasis:names:tc:SAML:2.0:bindings:URI" Location="http://am.example.com:8088/openam/AIDReqUri/IDPRole/metaAlias/idp"/>
>     </IDPSSODescriptor>
> </EntityDescriptor>
> ```
>
> Source: [idp.xml](../_attachments/SAML/idp.xml)

> **Collapse: idp-extended.xml**
>
> The following example of `$HOME/.openig/SAML/idp-extended.xml` defines an AM SAML descriptor file for the IdP:
>
> ```xml
> <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
> <!--
>    DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
>
>    Copyright (c) 2002-2010 Sun Microsystems Inc. All Rights Reserved
>
>    The contents of this file are subject to the terms
>    of the Common Development and Distribution License
>    (the License). You may not use this file except in
>    compliance with the License.
>
>    You can obtain a copy of the License at
>    https://opensso.dev.java.net/public/CDDLv1.0.html or
>    opensso/legal/CDDLv1.0.txt
>    See the License for the specific language governing
>    permission and limitations under the License.
>
>    When distributing Covered Code, include this CDDL
>    Header Notice in each file and include the License file
>    at opensso/legal/CDDLv1.0.txt.
>    If applicable, add the following below the CDDL Header,
>    with the fields enclosed by brackets [] replaced by
>    your own identifying information:
>    "Portions Copyrighted [year] [name of copyright owner]"
>
>    Portions Copyrighted 2010-2017 Ping Identity Corporation.
> -->
> <EntityConfig entityID="openam" hosted="0" xmlns="urn:sun:fm:SAML:2.0:entityconfig">
>     <IDPSSOConfig>
>         <Attribute name="description">
>             <Value/>
>         </Attribute>
>         <Attribute name="cotlist">
>             <Value>Circle of Trust</Value>
>         </Attribute>
>     </IDPSSOConfig>
>     <AttributeAuthorityConfig>
>         <Attribute name="cotlist">
>             <Value>Circle of Trust</Value>
>         </Attribute>
>     </AttributeAuthorityConfig>
>     <XACMLPDPConfig>
>         <Attribute name="wantXACMLAuthzDecisionQuerySigned">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="cotlist">
>             <Value>Circle of Trust</Value>
>         </Attribute>
>     </XACMLPDPConfig>
> </EntityConfig>
> ```
>
> Source: [idp-extended.xml](../_attachments/SAML/idp-extended.xml)

> **Collapse: sp.xml**
>
> |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | The SAML library component validates the SP's AssertionConsumerService Location against the incoming IdP SAML Assertion, based on the request information including the port. Always specify the port in the Location value of `AssertionConsumerService` even when using defaults of 443 or 80:```xml
> <AssertionConsumerService isDefault="true"
>                           index="0"
>                           Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
>                           Location="https://sp.example.com:443/fedletapplication" />
> ``` |
>
> The following example of `$HOME/.openig/SAML/sp.xml` defines a SAML configuration file for the PingGateway SP, `sp`.
>
> ```xml
> <!--
>    DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
>
>    Copyright (c) 2002-2010 Sun Microsystems Inc. All Rights Reserved
>
>    The contents of this file are subject to the terms
>    of the Common Development and Distribution License
>    (the License). You may not use this file except in
>    compliance with the License.
>
>    You can obtain a copy of the License at
>    https://opensso.dev.java.net/public/CDDLv1.0.html or
>    opensso/legal/CDDLv1.0.txt
>    See the License for the specific language governing
>    permission and limitations under the License.
>
>    When distributing Covered Code, include this CDDL
>    Header Notice in each file and include the License file
>    at opensso/legal/CDDLv1.0.txt.
>    If applicable, add the following below the CDDL Header,
>    with the fields enclosed by brackets [] replaced by
>    your own identifying information:
>    "Portions Copyrighted [year] [name of copyright owner]"
>
>    Portions Copyrighted 2010-2017 Ping Identity Corporation.
> -->
> <EntityDescriptor entityID="sp" xmlns="urn:oasis:names:tc:SAML:2.0:metadata">
>     <SPSSODescriptor AuthnRequestsSigned="false" WantAssertionsSigned="false" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
>         <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://sp.example.com:8443/saml/fedletSloRedirect" ResponseLocation="https://sp.example.com:8443/saml/fedletSloRedirect"/>
>         <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://sp.example.com:8443/saml/fedletSloPOST" ResponseLocation="https://sp.example.com:8443/saml/fedletSloPOST"/>
>         <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="https://sp.example.com:8443/saml/fedletSloSoap"/>
>         <NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</NameIDFormat>
>         <AssertionConsumerService isDefault="true" index="0" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://sp.example.com:8443/saml/fedletapplication/metaAlias/sp"/>
>         <AssertionConsumerService index="1" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact" Location="https://sp.example.com:8443/saml/fedletapplication/metaAlias/sp"/>
>     </SPSSODescriptor>
>     <RoleDescriptor xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:query="urn:oasis:names:tc:SAML:metadata:ext:query" xsi:type="query:AttributeQueryDescriptorType" protocolSupportEnumeration= "urn:oasis:names:tc:SAML:2.0:protocol">
>     </RoleDescriptor>
>     <XACMLAuthzDecisionQueryDescriptor WantAssertionsSigned="false" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
>     </XACMLAuthzDecisionQueryDescriptor>
> </EntityDescriptor>
> ```
>
> Source: [sp.xml](../_attachments/SAML/sp.xml)

> **Collapse: sp-extended.xml**
>
> The following example of `$HOME/.openig/SAML/sp-extended.xml` defines an AM SAML descriptor file for the SP:
>
> ```xml
> <!--
>    DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
>
>    Copyright (c) 2002-2010 Sun Microsystems Inc. All Rights Reserved
>
>    The contents of this file are subject to the terms
>    of the Common Development and Distribution License
>    (the License). You may not use this file except in
>    compliance with the License.
>
>    You can obtain a copy of the License at
>    https://opensso.dev.java.net/public/CDDLv1.0.html or
>    opensso/legal/CDDLv1.0.txt
>    See the License for the specific language governing
>    permission and limitations under the License.
>
>    When distributing Covered Code, include this CDDL
>    Header Notice in each file and include the License file
>    at opensso/legal/CDDLv1.0.txt.
>    If applicable, add the following below the CDDL Header,
>    with the fields enclosed by brackets [] replaced by
>    your own identifying information:
>    "Portions Copyrighted [year] [name of copyright owner]"
>
>    Portions Copyrighted 2010-2017 Ping Identity Corporation.
> -->
> <EntityConfig xmlns="urn:sun:fm:SAML:2.0:entityconfig" xmlns:fm="urn:sun:fm:SAML:2.0:entityconfig" hosted="1" entityID="sp">
>     <SPSSOConfig metaAlias="/sp">
>         <Attribute name="description">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="signingCertAlias">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="encryptionCertAlias">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="basicAuthOn">
>             <Value>false</Value>
>         </Attribute>
>         <Attribute name="basicAuthUser">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="basicAuthPassword">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="autofedEnabled">
>             <Value>false</Value>
>         </Attribute>
>         <Attribute name="autofedAttribute">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="transientUser">
>             <Value>anonymous</Value>
>         </Attribute>
>         <Attribute name="spAdapter">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="spAdapterEnv">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="fedletAdapter">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="fedletAdapterEnv">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="spAccountMapper">
>             <Value>com.sun.identity.saml2.plugins.DefaultLibrarySPAccountMapper</Value>
>         </Attribute>
>         <Attribute name="spAttributeMapper">
>             <Value>com.sun.identity.saml2.plugins.DefaultSPAttributeMapper</Value>
>         </Attribute>
>         <Attribute name="spAuthncontextMapper">
>             <Value>com.sun.identity.saml2.plugins.DefaultSPAuthnContextMapper</Value>
>         </Attribute>
>         <Attribute name="spAuthncontextClassrefMapping">
>             <Value>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport|0|default</Value>
>         </Attribute>
>         <Attribute name="spAuthncontextComparisonType">
>            <Value>exact</Value>
>         </Attribute>
>         <Attribute name="attributeMap">
>            <Value>*=*</Value>
>         </Attribute>
>         <Attribute name="saml2AuthModuleName">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="localAuthURL">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="intermediateUrl">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="defaultRelayState">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="appLogoutUrl">
>            <Value>https://sp.example.com:8443/saml/logout</Value>
>        </Attribute>
>        <Attribute name="assertionTimeSkew">
>            <Value>300</Value>
>        </Attribute>
>        <Attribute name="wantAttributeEncrypted">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantAssertionEncrypted">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantNameIDEncrypted">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantPOSTResponseSigned">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantArtifactResponseSigned">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantLogoutRequestSigned">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantLogoutResponseSigned">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantMNIRequestSigned">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantMNIResponseSigned">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="cotlist">
>            <Value>Circle of Trust</Value></Attribute>
>        <Attribute name="saeAppSecretList">
>        </Attribute>
>        <Attribute name="saeSPUrl">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="saeSPLogoutUrl">
>        </Attribute>
>        <Attribute name="ECPRequestIDPListFinderImpl">
>            <Value>com.sun.identity.saml2.plugins.ECPIDPFinder</Value>
>        </Attribute>
>        <Attribute name="ECPRequestIDPList">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="enableIDPProxy">
>            <Value>false</Value>
>        </Attribute>
>        <Attribute name="idpProxyList">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="idpProxyCount">
>            <Value>0</Value>
>        </Attribute>
>        <Attribute name="useIntroductionForIDPProxy">
>            <Value>false</Value>
>        </Attribute>
>     </SPSSOConfig>
>     <AttributeQueryConfig metaAlias="/attrQuery">
>         <Attribute name="signingCertAlias">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="encryptionCertAlias">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="wantNameIDEncrypted">
>            <Value></Value>
>         </Attribute>
>         <Attribute name="cotlist">
>            <Value>Circle of Trust</Value>
>         </Attribute>
>     </AttributeQueryConfig>
>     <XACMLAuthzDecisionQueryConfig metaAlias="/pep">
>         <Attribute name="signingCertAlias">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="encryptionCertAlias">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="basicAuthOn">
>             <Value>false</Value>
>         </Attribute>
>         <Attribute name="basicAuthUser">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="basicAuthPassword">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="wantXACMLAuthzDecisionResponseSigned">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="wantAssertionEncrypted">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="cotlist">
>             <Value>Circle of Trust</Value>
>         </Attribute>
>    </XACMLAuthzDecisionQueryConfig>
> </EntityConfig>
> ```
>
> Source: [sp-extended.xml](../_attachments/SAML/sp-extended.xml)

Find additional hints for extended SAML v2.0 SP (`sp-extended.xml`) settings in the AM documentation on [Service Provider Extended XML](https://docs.pingidentity.com/pingam/8.1/am-saml2/create-configure-fedlet.html#unconfigured-fedlet-sp-extended).

## PingOne as IdP

> **Collapse: FederationConfig.properties**
>
> ```none
> # If a component wants to use a different datastore provider than the
> # default one defined above, it can define a property like follows:
> # com.sun.identity.plugin.datastore.class.<componentName>=<provider class>
>
> # com.sun.identity.plugin.configuration.class specifies implementation for
> # com.sun.identity.plugin.configuration.ConfigurationInstance interface.
> com.sun.identity.plugin.configuration.class=com.sun.identity.plugin.configuration.impl.FedletConfigurationImpl
>
> # Specifies implementation for
> # com.sun.identity.plugin.datastore.DataStoreProvider interface.
> # This property defines the default datastore provider.
> com.sun.identity.plugin.datastore.class.default=com.sun.identity.plugin.datastore.impl.FedletDataStoreProvider
>
> # Specifies implementation for
> # org.forgerock.openam.federation.plugin.rooturl.RootUrlProvider interface.
> # This property defines the default base url provider.
> com.sun.identity.plugin.root.url.class.default=org.forgerock.openam.federation.plugin.rooturl.impl.FedletRootUrlProvider
>
> # com.sun.identity.plugin.log.class specifies implementation for
> # com.sun.identity.plugin.log.Logger interface.
> com.sun.identity.plugin.log.class=com.sun.identity.plugin.log.impl.FedletLogger
>
> # com.sun.identity.plugin.session.class specifies implementation for
> # com.sun.identity.plugin.session.SessionProvider interface.
> com.sun.identity.plugin.session.class=com.sun.identity.plugin.session.impl.FedletSessionProvider
>
> # com.sun.identity.plugin.monitoring.agent.class specifies implementation for
> # com.sun.identity.plugin.monitoring.FedMonAgent interface.
> com.sun.identity.plugin.monitoring.agent.class=com.sun.identity.plugin.monitoring.impl.FedletAgentProvider
>
> # com.sun.identity.plugin.monitoring.saml2.class specifies implementation for
> # com.sun.identity.plugin.monitoring.FedMonSAML2Svc interface.
> com.sun.identity.plugin.monitoring.saml2.class=com.sun.identity.plugin.monitoring.impl.FedletMonSAML2SvcProvider
>
> # com.sun.identity.saml.xmlsig.keyprovider.class specified the implementation
> # class for com.sun.identity.saml.xmlsig.KeyProvider interface
> com.sun.identity.saml.xmlsig.keyprovider.class=com.sun.identity.saml.xmlsig.JKSKeyProvider
>
> # com.sun.identity.saml.xmlsig.signatureprovider.class specified the
> # implementation class for com.sun.identity.saml.xmlsig.SignatureProvider
> # interface
> com.sun.identity.saml.xmlsig.signatureprovider.class=com.sun.identity.saml.xmlsig.AMSignatureProvider
>
> com.iplanet.am.server.protocol=http
> com.iplanet.am.server.host=am.example.com
> com.iplanet.am.server.port=8080
> com.iplanet.am.services.deploymentDescriptor=/openam
> com.iplanet.am.logstatus=ACTIVE
>
> # Name of the webcontainer.
> # Even though the servlet/JSP are web container independent,
> # Access/Federation Manager uses servlet 2.3 API request.setCharacterEncoding()
> # to decode incoming non English characters. These APIs will not work if
> # Access/Federation Manager is deployed on Sun Java System Web Server 6.1.
> # We use gx_charset mechanism to correctly decode incoming data in
> # Sun Java System Web Server 6.1 and S1AS7.0. Possible values
> # are BEA6.1, BEA 8.1, IBM5.1 or IAS7.0.
> # If the web container is Sun Java System Webserver, the tag is not replaced.
> com.sun.identity.webcontainer=WEB_CONTAINER
>
> # Identify saml xml signature keystore file, keystore password file
> # key password file
> com.sun.identity.saml.xmlsig.keystore=%BASE_DIR%/security/keystores/keystore.jks
> com.sun.identity.saml.xmlsig.storepass=%BASE_DIR%/.storepass
> com.sun.identity.saml.xmlsig.keypass=%BASE_DIR%/.keypass
> com.sun.identity.saml.xmlsig.certalias=test
>
> # Type of keystore used for saml xml signature. Default is JKS.
> #
> # com.sun.identity.saml.xmlsig.storetype=JKS
>
> # Specifies the implementation class for
> # com.sun.identity.saml.xmlsig.PasswordDecoder interface.
> com.sun.identity.saml.xmlsig.passwordDecoder=com.sun.identity.fedlet.FedletEncodeDecode
>
> # The following key is used to specify the maximum content-length
> # for an HttpRequest that will be accepted by the OpenSSO
> # The default value is 16384 which is 16k
> com.iplanet.services.comm.server.pllrequest.maxContentLength=16384
>
> # The following keys are used to configure the Debug service.
> # Possible values for the key 'level' are: off | error | warning | message.
> # The key 'directory' specifies the output directory where the debug files
> # will be created.
> # Trailing spaces are significant.
> # Windows: Use forward slashes "/" separate directories, not backslash "\".
> # Windows: Spaces in the file name are allowed for Windows.
> #
> com.iplanet.services.debug.level=message
> com.iplanet.services.debug.directory=%BASE_DIR%%SERVER_URI%/debug
>
> # The following keys are used to configure the Stats service.
> # Possible values for the key 'level' are: off | file | console
> # Stats state 'file' will write to a file under the specified directory,
> # and 'console' will write into  webserver log files
> # The key 'directory' specifies the output directory where the debug files
> # will be created.
> # Trailing spaces are significant.
> # Windows: Use forward slashes "/" separate directories, not backslash "\".
> # Windows: Spaces in the file name are allowed for Windows.
> # Stats interval should be atleast 5 secs to avoid CPU saturation,
> # the product would assume any thing less than 5 secs is 5 secs.
> com.iplanet.am.stats.interval=60
> com.iplanet.services.stats.state=file
> com.iplanet.services.stats.directory=%BASE_DIR%/var/stats
>
> # The key that will be used to encrypt and decrypt passwords.
> am.encryption.pwd=@AM_ENC_PWD@
>
> # SecureRandom Properties: The key
> # "com.iplanet.security.SecureRandomFactoryImpl"
> # specifies the factory class name for SecureRandomFactory
> # Available impl classes are:
> #   com.iplanet.am.util.JSSSecureRandomFactoryImpl (uses JSS)
> #   com.iplanet.am.util.SecureRandomFactoryImpl (pure Java)
> com.iplanet.security.SecureRandomFactoryImpl=com.iplanet.am.util.SecureRandomFactoryImpl
>
> # SocketFactory properties: The key "com.iplanet.security.SSLSocketFactoryImpl"
> # specifies the factory class name for LDAPSocketFactory
> # Available classes are:
> #    com.iplanet.services.ldap.JSSSocketFactory (uses JSS)
> #    com.sun.identity.shared.ldap.factory.JSSESocketFactory    (pure Java)
> com.iplanet.security.SSLSocketFactoryImpl=com.sun.identity.shared.ldap.factory.JSSESocketFactory
>
> # Encryption: The key "com.iplanet.security.encryptor" specifies
> # the encrypting class implementation.
> # Available classes are:
> #    com.iplanet.services.util.JCEEncryption
> #    com.iplanet.services.util.JSSEncryption
> com.iplanet.security.encryptor=com.iplanet.services.util.JCEEncryption
>
> # Determines if JSS will be added with highest priority to JCE
> # Set this to "true" if other JCE providers should be used for
> # digial signatures and encryptions.
> com.sun.identity.jss.donotInstallAtHighestPriority=true
>
> # Configuration File (serverconfig.xml) Location
> com.iplanet.services.configpath=@BASE_DIR@
> ```
>
> Source: [ping-FederationConfig.properties](../_attachments/SAML/ping-FederationConfig.properties)

> **Collapse: fedlet.cot**
>
> ```none
> cot-name=Circle of Trust
> sun-fm-cot-status=Active
> sun-fm-trusted-providers=idp-entityID, sp
> sun-fm-saml2-readerservice-url=
> sun-fm-saml2-writerservice-url=
> ```
>
> Source: [ping-fedlet.cot](../_attachments/SAML/ping-fedlet.cot)

> **Collapse: idp-extended.xml**
>
> ```none
> <EntityConfig entityID="idp-entityID" hosted="0" xmlns="urn:sun:fm:SAML:2.0:entityconfig">
>     <IDPSSOConfig>
>         <Attribute name="description">
>             <Value/>
>         </Attribute>
>         <Attribute name="cotlist">
>             <Value>Circle of Trust</Value>
>         </Attribute>
>     </IDPSSOConfig>
>     <AttributeAuthorityConfig>
>         <Attribute name="cotlist">
>             <Value>Circle of Trust</Value>
>         </Attribute>
>     </AttributeAuthorityConfig>
>     <XACMLPDPConfig>
>         <Attribute name="wantXACMLAuthzDecisionQuerySigned">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="cotlist">
>             <Value>Circle of Trust</Value>
>         </Attribute>
>     </XACMLPDPConfig>
> </EntityConfig>
> ```
>
> Source: [ping-idp-extended.xml](../_attachments/SAML/ping-idp-extended.xml)

> **Collapse: sp.xml**
>
> ```none
> <EntityDescriptor entityID="sp" xmlns="urn:oasis:names:tc:SAML:2.0:metadata">
>     <SPSSODescriptor AuthnRequestsSigned="false" WantAssertionsSigned="false" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
>         <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://sp.example.com:8443/home/saml/fedletSloRedirect" ResponseLocation="https://sp.example.com:8443/home/saml/fedletSloRedirect"/>
>         <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://sp.example.com:8443/home/saml/fedletSloPOST" ResponseLocation="https://sp.example.com:8443/home/saml/fedletSloPOST"/>
>         <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="https://sp.example.com:8443/home/saml/fedletSloSoap"/>
>         <NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</NameIDFormat>
>         <AssertionConsumerService isDefault="true" index="0" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://sp.example.com:8443/home/saml/fedletapplication"/>
>         <AssertionConsumerService index="1" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact" Location="https://sp.example.com:8443/home/saml/fedletapplication"/>
>     </SPSSODescriptor>
>     <RoleDescriptor xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:query="urn:oasis:names:tc:SAML:metadata:ext:query" xsi:type="query:AttributeQueryDescriptorType" protocolSupportEnumeration= "urn:oasis:names:tc:SAML:2.0:protocol">
>     </RoleDescriptor>
>     <XACMLAuthzDecisionQueryDescriptor WantAssertionsSigned="false" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
>     </XACMLAuthzDecisionQueryDescriptor>
> </EntityDescriptor>
> ```
>
> Source: [ping-sp.xml](../_attachments/SAML/ping-sp.xml)

> **Collapse: sp-extended.xml**
>
> ```none
> <EntityConfig xmlns="urn:sun:fm:SAML:2.0:entityconfig" xmlns:fm="urn:sun:fm:SAML:2.0:entityconfig" hosted="1" entityID="sp">
>     <SPSSOConfig metaAlias="/sp">
>         <Attribute name="description">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="signingCertAlias">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="encryptionCertAlias">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="basicAuthOn">
>             <Value>false</Value>
>         </Attribute>
>         <Attribute name="basicAuthUser">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="basicAuthPassword">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="autofedEnabled">
>             <Value>false</Value>
>         </Attribute>
>         <Attribute name="autofedAttribute">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="transientUser">
>             <Value>anonymous</Value>
>         </Attribute>
>         <Attribute name="spAdapter">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="spAdapterEnv">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="fedletAdapter">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="fedletAdapterEnv">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="spAccountMapper">
>             <Value>com.sun.identity.saml2.plugins.DefaultLibrarySPAccountMapper</Value>
>         </Attribute>
>         <Attribute name="spAttributeMapper">
>             <Value>com.sun.identity.saml2.plugins.DefaultSPAttributeMapper</Value>
>         </Attribute>
>         <Attribute name="spAuthncontextMapper">
>             <Value>com.sun.identity.saml2.plugins.DefaultSPAuthnContextMapper</Value>
>         </Attribute>
>         <Attribute name="spAuthncontextClassrefMapping">
>           <Value>urn:oasis:names:tc:SAML:2.0:ac:classes:unspecified|0|default</Value>
>         </Attribute>
>         <Attribute name="spAuthncontextComparisonType">
>            <Value>exact</Value>
>         </Attribute>
>         <Attribute name="attributeMap">
>            <Value>*=*</Value>
>         </Attribute>
>         <Attribute name="saml2AuthModuleName">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="localAuthURL">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="intermediateUrl">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="defaultRelayState">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="appLogoutUrl">
>            <Value>https://sp.example.com:8443/home/saml/logout</Value>
>        </Attribute>
>        <Attribute name="assertionTimeSkew">
>            <Value>300</Value>
>        </Attribute>
>        <Attribute name="wantAttributeEncrypted">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantAssertionEncrypted">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantNameIDEncrypted">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantPOSTResponseSigned">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantArtifactResponseSigned">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantLogoutRequestSigned">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantLogoutResponseSigned">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantMNIRequestSigned">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="wantMNIResponseSigned">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="cotlist">
>            <Value>Circle of Trust</Value></Attribute>
>        <Attribute name="saeAppSecretList">
>        </Attribute>
>        <Attribute name="saeSPUrl">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="saeSPLogoutUrl">
>        </Attribute>
>        <Attribute name="ECPRequestIDPListFinderImpl">
>            <Value>com.sun.identity.saml2.plugins.ECPIDPFinder</Value>
>        </Attribute>
>        <Attribute name="ECPRequestIDPList">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="enableIDPProxy">
>            <Value>false</Value>
>        </Attribute>
>        <Attribute name="idpProxyList">
>            <Value></Value>
>        </Attribute>
>        <Attribute name="idpProxyCount">
>            <Value>0</Value>
>        </Attribute>
>        <Attribute name="useIntroductionForIDPProxy">
>            <Value>false</Value>
>        </Attribute>
>     </SPSSOConfig>
>     <AttributeQueryConfig metaAlias="/attrQuery">
>         <Attribute name="signingCertAlias">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="encryptionCertAlias">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="wantNameIDEncrypted">
>            <Value></Value>
>         </Attribute>
>         <Attribute name="cotlist">
>            <Value>Circle of Trust</Value>
>         </Attribute>
>     </AttributeQueryConfig>
>     <XACMLAuthzDecisionQueryConfig metaAlias="/pep">
>         <Attribute name="signingCertAlias">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="encryptionCertAlias">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="basicAuthOn">
>             <Value>false</Value>
>         </Attribute>
>         <Attribute name="basicAuthUser">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="basicAuthPassword">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="wantXACMLAuthzDecisionResponseSigned">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="wantAssertionEncrypted">
>             <Value></Value>
>         </Attribute>
>         <Attribute name="cotlist">
>             <Value>Circle of Trust</Value>
>         </Attribute>
>    </XACMLAuthzDecisionQueryConfig>
> </EntityConfig>
> ```
>
> Source: [ping-sp-extended.xml](../_attachments/SAML/ping-sp-extended.xml)

Find additional hints for extended SAML v2.0 SP (`sp-extended.xml`) settings in the AM documentation on [Service Provider Extended XML](https://docs.pingidentity.com/pingam/8.1/am-saml2/create-configure-fedlet.html#unconfigured-fedlet-sp-extended).

---

---
title: Hardening PingAM authorization
description: Use PingAM policy advice to harden authorization in PingGateway, requiring conditions like secure channels or higher authentication levels
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:stepup
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/stepup.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-15
---

# Hardening PingAM authorization

To protect sensitive resources, AM policies can use additional conditions to harden the authorization. When AM communicates a policy decision to PingGateway, the decision includes advice to indicate extra conditions the user must meet.

Conditions can include requirements to access the resource over a secure channel, access during working hours, or a higher authentication level. Learn more in AM's [Authorization](https://docs.pingidentity.com/pingam/8.1/am-authorization/preface.html) documentation.

The following pages build on the policies to [Enforce AM policy decisions](pep.html):

* [Stepping up the PingAM authentication level](stepup-sso-session.html)

* [Authorizing a single transaction with PingAM](stepup-sso-trx.html)

---

---
title: ID token validation with PingAM
description: Configure PingGateway to validate an ID token using IdTokenValidationFilter with PingAM, including JWK set secret store and route configuration
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:validate-idtoken
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/validate-idtoken.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-07-07T16:48:22Z
---

# ID token validation with PingAM

This page uses an [IdTokenValidationFilter](../reference/IdTokenValidationFilter.html) to validate an ID token.

1. Set up AM:

   1. Set up AM as described in [Validating PingAM access tokens with introspection](oauth2-rs-introspect.html).

   2. Select Applications > OAuth 2.0 > Clients and add the additional scope `openid` to `client-application`.

2. Set up PingGateway:

   1. Add the following route to PingGateway:

      * Linux

        `$HOME/.openig/config/routes/idtokenvalidation.json`

      * Windows

        `%appdata%\OpenIG\config\routes\idtokenvalidation.json`

      ```json
      {
        "name": "idtokenvalidation",
        "condition": "${find(request.uri.path, '^/idtokenvalidation')}",
        "capture": "all",
        "handler": {
          "type": "Chain",
          "config": {
            "filters": [{
              "type": "IdTokenValidationFilter",
              "config": {
                "idToken": "<id_token_value>",
                "audience": "client-application",
                "issuer": "http://am.example.com:8088/openam/oauth2",
                "failureHandler": {
                  "type": "ScriptableHandler",
                  "config": {
                    "type": "application/x-groovy",
                    "source": [
                      "def response = new Response(Status.FORBIDDEN)",
                      "response.headers['Content-Type'] = 'text/html; charset=utf-8'",
                      "def errors = contexts.jwtValidationError.violations.collect{it.description}",
                      "def display = \"<html>Can't validate id_token:<br> ${contexts.jwtValidationError.jwt} \"",
                      "display <<=\"<br><br>For the following errors:<br> ${errors.join(\"<br>\")}</html>\"",
                      "response.entity=display as String",
                      "return response"
                    ]
                  }
                },
                "verificationSecretId": "verify",
                "secretsProvider": {
                  "type": "JwkSetSecretStore",
                  "config": {
                    "jwkUrl": "http://am.example.com:8088/openam/oauth2/connect/jwk_uri"
                  }
                }
              }
            }],
            "handler": {
              "type": "StaticResponseHandler",
              "config": {
                "status": 200,
                "headers": {
                  "Content-Type": [ "text/html; charset=UTF-8" ]
                },
                "entity": "<html><body>Validated id_token:<br> ${contexts.jwtValidation.value}</body></html>"
              }
            }
          }
        }
      }
      ```

      Source: [idtokenvalidation.json](../_attachments/config/routes/idtokenvalidation.json)

      Notice the following features of the route:

      * The route matches requests to `/idtokenvalidation`.

      * A SecretsProvider declares a JwkSetSecretStore to validate secrets for signed JWTs. The JwkSetSecretStore specifies a URL to a JWK set on AM that contains the signing keys.

      * The property `verificationSecretId` is configured with an arbitrary value. If this property isn't configured, the filter doesn't verify the signature of tokens.

      * The JwkSetSecretStore specifies the URL to a JWK set on AM, that contains verification keys identified by a `kid`. PingGateway validates the token signature as follows:

        * If the value of a `kid` in the JWK set matches a `kid` in the signed JWT, the JwkSetSecretStore verifies the signature.

        * If the JWT doesn't have a `kid`, or if the JWK set doesn't contain a key with the same value, the JwkSetSecretStore looks for valid secrets with the same purpose as the value of `verificationSecretId`.

      * If the filter validates the token, the StaticResponseHandler displays the token value from the context `${contexts.jwtValidation.value}`. Otherwise, the ScriptableHandler displays the token value and a list of violations from the context `${contexts.jwtValidationError.violations}`.

3. Test the setup:

   1. In a terminal window, use a `curl` command similar to the following to retrieve an id\_token:

      ```console
      $ curl -s \
      --user "client-application:password" \
      --data "grant_type=password&username=demo&password=Ch4ng31t&scope=openid" \
      http://am.example.com:8088/openam/oauth2/access_token
      ```

      Output

      ```
      {
       "access_token":"...",
       "scope":"openid",
       "id_token":"...",
       "token_type":"Bearer",
       "expires_in":3599
      }
      ```

   2. In the route, replace `<id_token_value>` with the value of the `id_token` returned in the previous step.

   3. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/idtokenvalidation>.

      The validated token is displayed.

   4. In the route, invalidate the token by changing the value of the audience or issuer, and then access the route again.

      The value of the token, and the reasons that the token is invalid, are displayed.

---

---
title: JWT validation with PingAM
description: Configure PingGateway to validate signed and encrypted JWTs using JwtValidationFilter, with examples using PingAM credentials
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:validate-jwt
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/validate-jwt.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Configuration", "JSON"]
---

# JWT validation with PingAM

The following examples show how to use the [JwtValidationFilter](../reference/JwtValidationFilter.html) to validate signed and encrypted JWT.

The JwtValidationFilter can access JWTs in the request, provided in a header, query parameter, form parameter, cookie, or other way. If an upstream filter makes the JWT available in the request's attributes context, the JwtValidationFilter can access the JWT through the context, for example, at `${attributes.jwtToValidate}`.

For convenience, the JWT in this example is provided by the JwtBuilderFilter, and passed to the JwtValidationFilter in a cookie.

The following figure shows the flow of information in the example:

![Validate JWT](_images/jwtvalidation.svg)

Before you begin, set up and test the example in [Pass runtime data in a JWT signed with PEM then encrypted with a symmetric key](data-downstream.html#runtime-sign-then-encrypt).

1. Add a second route to PingGateway, replacing value of the property `secretsDir` with the directory for the PEM files:

   * Linux

     `$HOME/.openig/config/routes/jwt-validate.json`

   * Windows

     `%appdata%\OpenIG\config\routes\jwt-validate.json`

   ```json
   {
     "name": "jwt-validate",
     "condition": "${find(request.uri.path, '^/jwt-validate')}",
     "properties": {
       "secretsDir": "path/to/secrets"
     },
     "capture": "all",
     "heap": [
       {
         "name": "SystemAndEnvSecretStore",
         "type": "SystemAndEnvSecretStore",
         "config": {
           "mappings": [{
             "secretId": "id.decrypted.key.for.signing.jwt",
             "format": "BASE64"
           }]
         }
       },
       {
         "name": "pemPropertyFormat",
         "type": "PemPropertyFormat",
         "config": {
           "decryptionSecretId": "id.decrypted.key.for.signing.jwt",
           "secretsProvider": "SystemAndEnvSecretStore"
         }
       },
       {
         "name": "FileSystemSecretStore-1",
         "type": "FileSystemSecretStore",
         "config": {
           "format": "PLAIN",
           "directory": "&{secretsDir}",
           "mappings": [{
             "secretId": "id.encrypted.key.for.signing.jwt.pem",
             "format": "pemPropertyFormat"
           }, {
             "secretId": "symmetric.key.for.encrypting.jwt",
             "format": {
               "type": "SecretKeyPropertyFormat",
               "config": {
                 "format": "BASE64",
                 "algorithm": "AES"
               }
             }
           }]
         }
       }
     ],
     "handler": {
       "type": "Chain",
       "config": {
         "filters": [{
           "type": "JwtValidationFilter",
           "config": {
             "jwt": "${request.cookies['my-jwt'][0].value}",
             "secretsProvider": "FileSystemSecretStore-1",
             "decryptionSecretId": "symmetric.key.for.encrypting.jwt",
             "customizer": {
               "type": "ScriptableJwtValidatorCustomizer",
               "config": {
                 "type": "application/x-groovy",
                 "source": [
                   "builder.claim('name', JsonValue::asString, isEqualTo('demo'))",
                   "builder.claim('email', JsonValue::asString, isEqualTo('demo@example.com'));"
                 ]
               }
             },
             "failureHandler": {
               "type": "ScriptableHandler",
               "config": {
                 "type": "application/x-groovy",
                 "source": [
                   "def response = new Response(Status.FORBIDDEN)",
                   "response.headers['Content-Type'] = 'text/html; charset=utf-8'",
                   "def errors = contexts.jwtValidationError.violations.collect{it.description}",
                   "def display = \"<html>Can't validate JWT:<br> ${contexts.jwtValidationError.jwt} \"",
                   "display <<=\"<br><br>For the following errors:<br> ${errors.join(\"<br>\")}</html>\"",
                   "response.entity=display as String",
                   "return response"
                 ]
               }
             }
           }
         }],
         "handler": {
           "type": "StaticResponseHandler",
           "config": {
             "status": 200,
             "headers": {
               "Content-Type": [ "text/html; charset=UTF-8" ]
             },
             "entity": [
               "<html>",
               "  <h2>Validated JWT:</h2>",
               "    <p>${contexts.jwtValidation.value}</p>",
               "  <h2>JWT payload:</h2>",
               "    <p>${contexts.jwtValidation.info}</p>",
               "</html>"
             ]
           }
         }
       }
     }
   }
   ```

   Source: [jwt-validate.json](../_attachments/config/routes/jwt-validate.json)

   Notice the following features of the route:

   * The route matches requests to `/jwt-validate`.

   * The JwtValidationFilter takes the value of the JWT from `my-jwt`.

   * The SystemAndEnvSecretStore, PemPropertyFormat, and FileSystemSecretStore objects in the heap are the same as those in the route to create the JWT. The JwtValidationFilter uses the same objects to validate the JWT.

   * The JwtBuilderFilter `customizer` requires that the JWT claims match `name:demo` and `email:demo@example.com`.

   * If the JWT is validated, the StaticResponseHandler displays the validated value. Otherwise, the FailureHandler displays the reason for the failed validation.

2. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/jwtbuilder-sign-then-encrypt> and accept the server certificate to build a JWT.

   2. Sign on to AM as user `demo`, password `Ch4ng31t`. The sample application displays the signed JWT.

   3. Go to <https://ig.example.com:8443/jwt-validate> to validate the JWT. The validated JWT and its payload are displayed.

   4. Test the setup again, but sign on to AM as a different user, or change the email address of the demo user in AM. The JWT isn't validated, and an error is displayed.

---

---
title: mTLS with PingAM and trusted headers
description: Configure PingGateway to validate certificate-bound access tokens using mTLS with trusted HTTP headers when TLS terminates at a proxy
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:oauth2-rs-introspect-mtls-header
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/oauth2-rs-introspect-mtls-header.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
section_ids:
  before_you_start: Before you start
  make_pinggateway_an_rs: Make PingGateway an RS
  try_mtls_with_trusted_headers: Try mTLS with trusted headers
---

# mTLS with PingAM and trusted headers

PingGateway can validate the thumbprint of certificate-bound access tokens by reading the client certificate from a configured, trusted HTTP header.

Use this method when TLS is terminated at a reverse proxy or load balancer before PingGateway. PingGateway cannot authenticate the client through the TLS connection's client certificate because:

* If the connection is over TLS, the connection presents the certificate of the TLS termination point before PingGateway.

* If the connection is not over TLS, the connection presents no client certificate.

If the client is connected directly to PingGateway through a TLS connection, for which PingGateway is the TLS termination point, use the example in [mTLS with PingAM using client certificates](oauth2-rs-introspect-mtls-certificate.html).

Configure the proxy or load balancer to:

* Forward the encoded certificate to PingGateway in the trusted header. Encode the certificate in an HTTP-header compatible format that can convey a full certificate, so that PingGateway can rebuild the certificate.

* Strip the trusted header from incoming requests, and change the default header name to something an attacker can't guess.

Because there is a trust relationship between PingGateway and the TLS termination point, PingGateway doesn't authenticate the contents of the trusted header. PingGateway accepts any value in a header from a trusted TLS termination point.

The following image illustrates the connections and certificates required by the example:

![This image illustrates the connections when PingGateway validates certificate-bound access tokens by reading certificates from HTTP headers.](_images/ig-mtls-header.png)![Validates certificate-bound access tokens by reading certificates from HTTP headers.](_images/mtls-header-flow.svg)

Follow the steps in this example to try mTLS using trusted headers.

## Before you start

1. Set up the keystores, truststores, AM, and PingGateway as described in [mTLS with PingAM using client certificates](oauth2-rs-introspect-mtls-certificate.html).

2. URL-encode the value of `$oauth2_client_keystore_directory/client.cert.pem`.

   PingGateway needs the certificate to validate the confirmation key.

## Make PingGateway an RS

1. Add the following route to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/mtls-header.json`

   * Windows

     `%appdata%\OpenIG\config\routes\mtls-header.json`

   ```json
   {
     "name": "mtls-header",
     "condition": "${find(request.uri.path, '/mtls-header')}",
     "heap": [
       {
         "name": "SystemAndEnvSecretStore-1",
         "type": "SystemAndEnvSecretStore"
       },
       {
         "name": "AmService-1",
         "type": "AmService",
         "config": {
           "agent": {
             "username": "ig_agent",
             "passwordSecretId": "agent.secret.id"
           },
           "secretsProvider": "SystemAndEnvSecretStore-1",
           "url": "http://am.example.com:8088/openam"
         }
       }
     ],
     "handler": {
       "type": "Chain",
       "capture": "all",
       "config": {
         "filters": [
           {
             "name": "CertificateThumbprintFilter-1",
             "type": "CertificateThumbprintFilter",
             "config": {
               "certificate": "${pemCertificate(urlDecode(request.headers['x-ssl-cert'][0]))}",
               "failureHandler": {
                 "type": "ScriptableHandler",
                 "config": {
                   "type": "application/x-groovy",
                   "source": [
                     "def response = new Response(Status.TEAPOT);",
                     "response.entity = 'Failure in CertificateThumbprintFilter'",
                     "return response"
                   ]
                 }
               }
             }
           },
           {
             "name": "OAuth2ResourceServerFilter-1",
             "type": "OAuth2ResourceServerFilter",
             "config": {
               "scopes": [
                 "test"
               ],
               "requireHttps": false,
               "accessTokenResolver": {
                 "type": "ConfirmationKeyVerifierAccessTokenResolver",
                 "config": {
                   "delegate": {
                     "name": "token-resolver-1",
                     "type": "TokenIntrospectionAccessTokenResolver",
                     "config": {
                       "amService": "AmService-1",
                       "providerHandler": {
                         "type": "Chain",
                         "config": {
                           "filters": [
                             {
                               "type": "HttpBasicAuthenticationClientFilter",
                               "config": {
                                 "username": "ig_agent",
                                 "passwordSecretId": "agent.secret.id",
                                 "secretsProvider": "SystemAndEnvSecretStore-1"
                               }
                             }
                           ],
                           "handler": "ForgeRockClientHandler"
                         }
                       }
                     }
                   }
                 }
               }
             }
           }
         ],
         "handler": {
           "name": "StaticResponseHandler-1",
           "type": "StaticResponseHandler",
           "config": {
             "status": 200,
             "headers": {
               "Content-Type": [ "text/plain; charset=UTF-8" ]
             },
             "entity": "mTLS\n Valid token: ${contexts.oauth2.accessToken.token}\n Confirmation keys: ${contexts.oauth2}"
           }
         }
       }
     }
   }
   ```

   Source: [mtls-header.json](../_attachments/config/routes/mtls-header.json)

   Notice the following features of the route compared to `mtls-certificate.json`:

   * The route matches requests to `/mtls-header`.

   * The `CertificateThumbprintFilter` extracts the client certificate from the trusted header.

     In this example, the filter is configured as if NGINX were sending the trusted header. Find additional examples in the [CertificateThumbprintFilter reference](../reference/CertificateThumbprintFilter.html#CertificateThumbprintFilter-examples).

     The filter computes the certificate thumbprint and makes the thumbprint available to the `ConfirmationKeyVerifierAccessTokenResolver`.

## Try mTLS with trusted headers

1. Get a certificate-bound access token from AM as the client application:

   ```console
   $ export ACCESS_TOKEN=$(curl \
   --request POST \
   --cacert $am_keystore_directory/openam-server.cert.pem \
   --cert $oauth2_client_keystore_directory/client.cert.pem \
   --key $oauth2_client_keystore_directory/client.key.pem \
   --header 'cache-control: no-cache' \
   --header 'content-type: application/x-www-form-urlencoded' \
   --data 'client_id=client-application' \
   --data 'grant_type=client_credentials' \
   --data 'scope=test' \
   https://am.example.com:8445/openam/oauth2/access_token | jq -r .access_token)
   ```

   Notice the client gets an access token without using a client secret. It authenticates with its self-signed certificate.

2. Introspect the access token on AM using the PingGateway agent credentials:

   ```console
   $ curl \
   --request POST \
   --user ig_agent:password \
   --header 'content-type: application/x-www-form-urlencoded' \
   --data "token=$ACCESS_TOKEN" \
   http://am.example.com:8088/openam/oauth2/realms/root/introspect | jq
   ```

   Output

   ```
   {
     "active": true,
     "scope": "test",
     "realm": "/",
     "client_id": "client-application",
     "user_id": "client-application",
     "username": "client-application",
     "token_type": "Bearer",
     "exp": 1724249775,
     "sub": "(age!client-application)",
     "iss": "http://am.example.com:8088/openam/oauth2",
     "subname": "client-application",
     "cnf": {
       "x5t#S256": "TTXH27YoFFCgOAQ0189KMBKeqxU1ZfZ_2nYGxrsjHlM"
     },
     "authGrantId": "LMhPEqYaxMbrd2zXMAQjHcc8JYE",
     "auditTrackingId": "962fd5f6-fc2f-43c1-b044-ed1eb33d7aef-403"
   }
   ```

   The `cnf` property indicates the value of the confirmation code:

   * `x5`: X509 certificate

   * `t`: thumbprint

   * `#`: separator

   * `S256`: algorithm used to hash the raw certificate bytes

3. Access the PingGateway route to validate the confirmation key.

   The \<url-encoded-cert> is the URL-encoded value of `$oauth2_client_keystore_directory/client.cert.pem`:

   ```console
   $ curl \
   --request POST \
   --cacert $ig_keystore_directory/ig.example.com-certificate.pem \
   --header "Authorization: Bearer $ACCESS_TOKEN" \
   --header 'x-ssl-cert: <url-encoded-cert>'
   https://ig.example.com:8443/mtls-header
   ```

   Output

   ```
   mTLS
    Valid token: UnUxGRuwXx_ugUCvNKFM3GJo3Cc
    Confirmation keys: { ... }
   ```

   The command displays the validated token and confirmation keys.

---

---
title: mTLS with PingAM using client certificates
description: Configure PingGateway as an OAuth 2.0 resource server that validates mTLS certificate-bound access tokens read from the TLS connection
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:oauth2-rs-introspect-mtls-certificate
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/oauth2-rs-introspect-mtls-certificate.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-15
section_ids:
  prepare_the_keys: Prepare the keys
  prepare_am: Prepare AM
  prepare_pinggateway: Prepare PingGateway
  make_pinggateway_an_rs: Make PingGateway an RS
  try_certificate_based_mtls: Try certificate-based mTLS
---

# mTLS with PingAM using client certificates

PingGateway can validate the thumbprint of certificate-bound access tokens by reading the client certificate from the TLS connection.

For this example, the client must be connected directly to PingGateway through a TLS connection, for which PingGateway is the TLS termination point, as shown in the following image. If TLS is terminated at a reverse proxy or load balancer before PingGateway, use the example in [mTLS with PingAM and trusted headers](oauth2-rs-introspect-mtls-header.html).

![This image illustrates the connections when PingGateway reads certificates from the TLS connection to validate certificate-bound access tokens.](_images/ig-mtls-container.png)![Validate certificate-bound access tokens by reading the client certificate from the TLS connection.](_images/mtls-certificate-flow.svg)

Follow the steps in this example to try mTLS using standard TLS client certificate authentication.

## Prepare the keys

1. To make it easy to identify and refer to secrets used in mTLS examples, create directories and environment variables:

   ```console
   $ export ig_keystore_directory=/path/to/ig/secrets
   $ export am_keystore_directory=/path/to/am/secrets
   $ export oauth2_client_keystore_directory=/path/to/client/secrets
   ```

2. Create keys and certificates for the example:

   1. Create self-signed RSA key pairs for AM and the client:

      ```console
      $ keytool -genkeypair \
      -alias openam-server \
      -keyalg RSA \
      -keysize 2048 \
      -keystore $am_keystore_directory/keystore.p12 \
      -storepass changeit \
      -storetype PKCS12 \
      -keypass changeit \
      -validity 360 \
      -dname CN=am.example.com,O=Example,C=FR
      ```

      ```console
      $ keytool -genkeypair \
      -alias oauth2-client \
      -keyalg RSA \
      -keysize 2048 \
      -keystore $oauth2_client_keystore_directory/keystore.p12 \
      -storepass changeit \
      -storetype PKCS12 \
      -keypass changeit \
      -validity 360 \
      -dname CN=test
      ```

   2. Export the certificates to .pem so that the `curl` client can verify the identity of the AM and PingGateway servers:

      ```console
      $ keytool -export \
      -rfc \
      -alias openam-server \
      -keystore $am_keystore_directory/keystore.p12 \
      -storepass changeit \
      -storetype PKCS12 \
      -file $am_keystore_directory/openam-server.cert.pem
      ```

      Output

      ```
      Certificate stored in file .../openam-server.cert.pem
      ```

   3. Extract the certificate and client private key to .pem so that the `curl` command can identity itself as the client for the HTTPS connection:

      ```console
      $ keytool -export \
      -rfc \
      -alias oauth2-client \
      -keystore $oauth2_client_keystore_directory/keystore.p12 \
      -storepass changeit \
      -storetype PKCS12 \
      -file $oauth2_client_keystore_directory/client.cert.pem
      ```

      Output

      ```
      Certificate stored in file .../client.cert.pem
      ```

      ```console
      $ openssl pkcs12 \
      -in $oauth2_client_keystore_directory/keystore.p12 \
      -nocerts \
      -nodes \
      -passin pass:changeit \
      -out $oauth2_client_keystore_directory/client.key.pem
      ```

      Output

      ```
      ...verified OK
      ```

   4. Create the CACerts truststore so that AM can validate the client identity:

      ```console
      $ keytool -import \
      -noprompt \
      -trustcacerts \
      -file $oauth2_client_keystore_directory/client.cert.pem \
      -keystore $oauth2_client_keystore_directory/cacerts.p12 \
      -storepass changeit \
      -storetype PKCS12 \
      -alias client-cert
      ```

      Output

      ```
      Certificate was added to keystore
      ```

   5. In the *ig\_keystore\_directory*, add a file called `keystore.pass` containing the keystore password:

      ```console
      $ cd $ig_keystore_directory
      $ echo -n 'changeit' > keystore.pass
      ```

## Prepare AM

1. Configure AM for HTTPS connections using information in the AM documentation about [Secure HTTP and LDAP connections](https://docs.pingidentity.com/pingam/8.1/security/secure-connections.html).

   > **Collapse: Learn more**
   >
   > 1. Add a connector configuration for port `8445` to AM's Tomcat `server.xml`, replacing the values for the keystore directories with your path. If the file already contains a connector for the port, edit that connector or replace it:
   >
   >    ```xml
   >    <Connector port="8445" protocol="HTTP/1.1" SSLEnabled="true" scheme="https" secure="true">
   >      <SSLHostConfig protocols="+TLSv1.2,-TLSv1.1,-TLSv1,-SSLv2Hello,-SSLv3"
   >                     certificateVerification="optionalNoCA"
   >                     truststoreFile="oauth2_client_keystore_directory/cacerts.p12"
   >                     truststorePassword="changeit"
   >                     truststoreType="PKCS12">
   >        <Certificate certificateKeystoreFile="am_keystore_directory/keystore.p12"
   >                     certificateKeystorePassword="changeit"
   >                     certificateKeystoreType="PKCS12"/>
   >      </SSLHostConfig>
   >    </Connector>
   >    ```
   >
   > 2. In AM, export an environment variable for the base64-encoded value of the password (`changeit`) for the `cacerts.p12` truststore:
   >
   >    ```console
   >    $ export PASSWORDSECRETID='Y2hhbmdlaXQ='
   >    ```
   >
   > 3. Restart AM, and make sure you can access it on the secure port `https://am.example.com:8445/openam`.

2. Configure AM for mutual TLS using information in the AM documentation about [Mutual TLS](https://docs.pingidentity.com/pingam/8.1/am-oauth2/client-auth-mtls.html).

   > **Collapse: Learn more**
   >
   > 1. In the AM admin UI, select Applications > Agents > Identity Gateway, and register a PingGateway agent that can introspect access tokens:
   >
   >    * Agent ID: `ig_agent`
   >
   >    * Password: `password`
   >
   >    * Token Introspection: `Realm Only`
   >
   >      |   |                                                                                                                   |
   >      | - | ----------------------------------------------------------------------------------------------------------------- |
   >      |   | Use secure passwords in a production environment. Consider using a password manager to generate secure passwords. |
   >
   > 2. Configure an OAuth 2.0 Authorization Server with settings for mTLS:
   >
   >    1. Select Services > Add a Service > OAuth2 Provider, and add a service with the default values.
   >
   >    2. On the Advanced tab, select the following value:
   >
   >       * Support TLS Certificate-Bound Access Tokens: enabled
   >
   > 3. Configure an OAuth 2.0 client to request access tokens:
   >
   >    1. Select Applications > OAuth 2.0 > Clients, and add a client with the following values:
   >
   >       * Client ID: `client-application`
   >
   >       * Client secret: `password`
   >
   >       * Scope(s): `test`
   >
   >    2. (Optional) On the Core tab, switch to using a client secret associated with a secret label by setting a Secret Label Identifier and mapping the label to a secret.
   >
   >       To learn more, read [Create a client profile](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-register-client.html#client-secret-label-identifier) and [Map and rotate secrets](https://docs.pingidentity.com/pingam/8.1/security/secret-mapping.html) in the AM documentation.
   >
   >    3. On the Advanced tab, select the following values:
   >
   >       * Grant Types: `Client Credentials`
   >
   >         The `password` is the only grant type used by the client in the example.
   >
   >       * Token Endpoint Authentication Method: `self_signed_tls_client_auth`
   >
   >    4. On the Signing and Encryption tab, set the following values:
   >
   >       * mTLS Self-Signed Certificate: Enter the content of the X.509 certificate, client.cert.pem.
   >
   >       * mTLS Subject DN: `CN=test`
   >
   >         When this option is set, AM requires the subject DN in the client certificate to have the same value. This ensures that the certificate is from the client and not just a valid certificate trusted by the trust manager.
   >
   >       * Public key selector: `x509`
   >
   >       * Use Certificate-Bound Access Tokens: Enabled

## Prepare PingGateway

1. Configure PingGateway for HTTPS using information from [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   This example uses a self-signed certificate stored in a PEM file.

2. Configure PingGateway for mutual TLS using information from [Configure PingGateway for mTLS (server-side)](../installation-guide/securing-connections.html#server-side-mtls).

   This example uses the following `admin.json` with a SecretsTrustManager:

   * Linux

     `$HOME/.openig/config/admin.json`

   * Windows

     `%appdata%\OpenIG\config\admin.json`

   ```json
   {
     "mode": "DEVELOPMENT",
     "properties": {
       "ig_keystore_directory": "/path/to/ig/secrets",
       "oauth2_client_keystore_directory": "/path/to/client/secrets"
     },
     "connectors": [
       {
         "port": 8080
       },
       {
         "port": 8443,
         "tls": {
           "type": "ServerTlsOptions",
           "config": {
             "alpn": {
               "enabled": true
             },
             "clientAuth": "REQUEST",
             "keyManager": "SecretsKeyManager-1",
             "trustManager": "SecretsTrustManager-1"
           }
         }
       }
     ],
     "heap": [
       {
         "name": "SecretsPasswords",
         "type": "FileSystemSecretStore",
         "config": {
           "directory": "&{ig_keystore_directory}",
           "format": "PLAIN"
         }
       },
       {
         "name": "SecretsKeyManager-1",
         "type": "SecretsKeyManager",
         "config": {
           "signingSecretId": "key.manager.secret.id",
           "secretsProvider": "ServerIdentityStore"
         }
       },
       {
         "name": "SecretsTrustManager-1",
         "type": "SecretsTrustManager",
         "config": {
           "verificationSecretId": "trust.manager.secret.id",
           "secretsProvider": {
             "type": "KeyStoreSecretStore",
             "config": {
               "file": "&{oauth2_client_keystore_directory}/cacerts.p12",
               "storePasswordSecretId": "keystore.pass",
               "secretsProvider": "SecretsPasswords",
               "mappings": [
                 {
                   "secretId": "trust.manager.secret.id",
                   "aliases": ["client-cert"]
                 }
               ]
             }
           }
         }
       },
       {
         "name": "ServerIdentityStore",
         "type": "FileSystemSecretStore",
         "config": {
           "format": "PLAIN",
           "directory": "&{ig_keystore_directory}",
           "suffix": ".pem",
           "mappings": [{
             "secretId": "key.manager.secret.id",
             "format": {
               "type": "PemPropertyFormat"
             }
           }]
         }
       }
     ]
   }
   ```

   Source: [admin-mtls.json](../_attachments/config/admin-mtls.json)

   Notice the `ServerTlsOptions`:

   * The trust manager settings let PingGateway trust the self-signed client certificate.

   * The `"clientAuth": "REQUEST"` setting permits optional HTTPS mutual authentication.

     Clients using mTLS authenticate with their certificates when setting up HTTPS. Other clients can connect over HTTPS without presenting a client certificate.

3. Replace the values of the secret directories with your directories, and then start PingGateway.

## Make PingGateway an RS

1. Configure PingGateway as a resource server for mTLS:

   1. Set an environment variable for the PingGateway agent password, and then restart PingGateway:

      ```console
      $ export AGENT_SECRET_ID='cGFzc3dvcmQ='
      ```

      The password is retrieved by a `SystemAndEnvSecretStore`, and must be base64-encoded.

   2. Add the following route to PingGateway:

      * Linux

        `$HOME/.openig/config/routes/mtls-certificate.json`

      * Windows

        `%appdata%\OpenIG\config\routes\mtls-certificate.json`

      ```json
      {
        "name": "mtls-certificate",
        "condition": "${find(request.uri.path, '/mtls-certificate')}",
        "heap": [
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          },
          {
            "name": "AmService-1",
            "type": "AmService",
            "config": {
              "agent": {
                "username": "ig_agent",
                "passwordSecretId": "agent.secret.id"
              },
              "secretsProvider": "SystemAndEnvSecretStore-1",
              "url": "http://am.example.com:8088/openam/"
            }
          }
        ],
        "handler": {
          "type": "Chain",
          "capture": "all",
          "config": {
            "filters": [
              {
                "name": "OAuth2ResourceServerFilter-1",
                "type": "OAuth2ResourceServerFilter",
                "config": {
                  "scopes": [
                    "test"
                  ],
                  "requireHttps": false,
                  "accessTokenResolver": {
                    "type": "ConfirmationKeyVerifierAccessTokenResolver",
                    "config": {
                      "delegate": {
                        "name": "token-resolver-1",
                        "type": "TokenIntrospectionAccessTokenResolver",
                        "config": {
                          "amService": "AmService-1",
                          "providerHandler": {
                            "type": "Chain",
                            "config": {
                              "filters": [
                                {
                                  "type": "HttpBasicAuthenticationClientFilter",
                                  "config": {
                                    "username": "ig_agent",
                                    "passwordSecretId": "agent.secret.id",
                                    "secretsProvider": "SystemAndEnvSecretStore-1"
                                  }
                                }
                              ],
                              "handler": "ForgeRockClientHandler"
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            ],
            "handler": {
              "name": "StaticResponseHandler-1",
              "type": "StaticResponseHandler",
              "config": {
                "status": 200,
                "headers": {
                  "Content-Type": [ "text/plain; charset=UTF-8" ]
                },
                "entity": "mTLS\n Valid token: ${contexts.oauth2.accessToken.token}\n Confirmation keys: ${contexts.oauth2}"
              }
            }
          }
        }
      }
      ```

      Source: [mtls-certificate.json](../_attachments/config/routes/mtls-certificate.json)

      Notice the following features of the route:

      * The route matches requests to `/mtls-certificate`.

      * The `OAuth2ResourceServerFilter` uses the `ConfirmationKeyVerifierAccessTokenResolver` to validate the certificate thumbprint against the thumbprint from the resolved access token provided by AM.

        The `ConfirmationKeyVerifierAccessTokenResolver` then delegates token resolution to the `TokenIntrospectionAccessTokenResolver`.

      * The `providerHandler` adds an authorization header to the request, containing the username and password of the OAuth 2.0 client with the scope to examine (introspect) access tokens.

      * The `OAuth2ResourceServerFilter` checks the resolved token has the required scopes and injects the token info into the context.

      * The `StaticResponseHandler` returns the content of the access token from the context.

## Try certificate-based mTLS

1. Get a certificate-bound access token from AM as the client application:

   ```console
   $ export ACCESS_TOKEN=$(curl \
   --request POST \
   --cacert $am_keystore_directory/openam-server.cert.pem \
   --cert $oauth2_client_keystore_directory/client.cert.pem \
   --key $oauth2_client_keystore_directory/client.key.pem \
   --header 'cache-control: no-cache' \
   --header 'content-type: application/x-www-form-urlencoded' \
   --data 'client_id=client-application' \
   --data 'grant_type=client_credentials' \
   --data 'scope=test' \
   https://am.example.com:8445/openam/oauth2/access_token | jq -r .access_token)
   ```

   Notice the client gets an access token without using a client secret. It authenticates with its self-signed certificate.

2. Introspect the access token on AM using the PingGateway agent credentials:

   ```console
   $ curl \
   --request POST \
   --user ig_agent:password \
   --header 'content-type: application/x-www-form-urlencoded' \
   --data "token=$ACCESS_TOKEN" \
   http://am.example.com:8088/openam/oauth2/realms/root/introspect | jq
   ```

   Output

   ```
   {
     "active": true,
     "scope": "test",
     "realm": "/",
     "client_id": "client-application",
     "user_id": "client-application",
     "username": "client-application",
     "token_type": "Bearer",
     "exp": 1724250516,
     "sub": "(age!client-application)",
     "iss": "http://am.example.com:8088/openam/oauth2",
     "subname": "client-application",
     "cnf": {
       "x5t#S256": "TTXH27YoFFCgOAQ0189KMBKeqxU1ZfZ_2nYGxrsjHlM"
     },
     "authGrantId": "JqckJ_KhDLDeb4cKRkeBJcXZZUE",
     "auditTrackingId": "962fd5f6-fc2f-43c1-b044-ed1eb33d7aef-429"
   }
   ```

   The `cnf` property indicates the value of the confirmation code:

   * `x5`: X509 certificate

   * `t`: thumbprint

   * `#`: separator

   * `S256`: algorithm used to hash the raw certificate bytes

3. Access the PingGateway route to validate the confirmation key with the ConfirmationKeyVerifierAccessTokenResolver:

   ```console
   $ curl \
   --request POST \
   --cacert $ig_keystore_directory/ig.example.com-certificate.pem \
   --cert $oauth2_client_keystore_directory/client.cert.pem \
   --key $oauth2_client_keystore_directory/client.key.pem \
   --header "Authorization: Bearer ${ACCESS_TOKEN}" \
   https://ig.example.com:8443/mtls-certificate
   ```

   Output

   ```
   mTLS
    Valid token: <ACCESS_TOKEN>
    Confirmation keys: { ... }
   ```

   The command displays the validated token and confirmation keys.

---

---
title: Multiple OIDC providers using PingAM and PingOne Advanced Identity Cloud
description: Configure PingGateway to present an identity provider chooser (Nascar page) for multiple OIDC providers using PingAM and PingOne Advanced Identity Cloud
component: pinggateway
version: 2026
page_id: pinggateway:gateway-guide:oidc-nascar
canonical_url: https://docs.pingidentity.com/pinggateway/2026/gateway-guide/oidc-nascar.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
---

# Multiple OIDC providers using PingAM and PingOne Advanced Identity Cloud

This page shows OIDC with two identity providers.

Client registrations for an AM identity provider and PingOne Advanced Identity Cloud identity provider are declared in the heap. The Nascar page helps the user to choose an identity provider.

1. Set up AM as the first identity provider, as described in [AM as OIDC provider](oidc-am.html).

2. Set up PingOne Advanced Identity Cloud as a second identity provider, as described in [OpenID Connect and PingOne Advanced Identity Cloud](../aic/oidc.html).

3. Make sure PingGateway connects to the sample application over HTTPS with a route to access static resources.

   Learn more in [Using the sample application](../getting-started/start-sampleapp.html).

4. Add the following route to PingGateway, replacing the value for the property `amInstanceUrl`:

   * Linux

     `$HOME/.openig/config/routes/07-openid-nascar.json`

   * Windows

     `%appdata%\OpenIG\config\routes\07-openid-nascar.json`

   ```json
   {
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
       },
       {
         "name": "openam",
         "type": "ClientRegistration",
         "config": {
           "clientId": "oidc_client",
           "issuer": {
             "name": "am_issuer",
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
       },
       {
         "name": "idcloud",
         "type": "ClientRegistration",
         "config": {
           "clientId": "oidc_client",
           "issuer": {
             "name": "idc_issuer",
             "type": "Issuer",
             "config": {
               "wellKnownEndpoint": "&{amInstanceUrl}/oauth2/realms/alpha/.well-known/openid-configuration"
             }
           },
           "scopes": [
             "openid",
             "profile",
             "email"
           ],
           "authenticatedRegistrationHandler": "AuthenticatedRegistrationHandler-1"
         }
       },
       {
         "name": "NascarPage",
         "type": "StaticResponseHandler",
         "config": {
           "status": 200,
           "headers": {
             "Content-Type": [ "text/html; charset=UTF-8" ]
           },
           "entity": [
             "<html>",
             "  <body>",
             "    <p><a href='/home/id_token/login?registration=oidc_client&issuer=am_issuer&goto=${urlEncodeQueryParameterNameOrValue('https://ig.example.com:8443/home/id_token')}'>Access Management login</a></p>",
             "    <p><a href='/home/id_token/login?registration=oidc_client&issuer=idc_issuer&goto=${urlEncodeQueryParameterNameOrValue('https://ig.example.com:8443/home/id_token')}'>Identity Cloud login</a></p>",
             "  </body>",
             "</html>"
           ]
         }
       }
     ],
     "name": "07-openid-nascar",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/home/id_token')}",
     "properties": {
       "amInstanceUrl": "https://myTenant.forgeblocks.com/am"
     },
     "handler": {
       "type": "Chain",
       "config": {
         "filters": [
           {
             "type": "AuthorizationCodeOAuth2ClientFilter",
             "config": {
               "clientEndpoint": "/home/id_token",
               "failureHandler": {
                 "type": "StaticResponseHandler",
                 "config": {
                   "comment": "Trivial failure handler for debugging only",
                   "status": 500,
                   "headers": {
                     "Content-Type": [ "text/plain; charset=UTF-8" ]
                   },
                   "entity": "${contexts.oauth2Failure.error}: ${contexts.oauth2Failure.description}"
                 }
               },
               "loginHandler": "NascarPage",
               "registrations": [ "openam", "idcloud" ],
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

   Source: [07-openid-nascar.json](../_attachments/config/routes/07-openid-nascar.json)

   Consider the differences with `07-openid.json`:

   * The heap objects `openam` and `idcloud` define client registrations.

   * The StaticResponseHandler provides links to the client registrations.

   * The AuthorizationCodeOAuth2ClientFilter uses a `loginHandler` to allow users to choose a client registration and therefore an identity provider.

5. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/id_token>.

      The Nascar page offers the choice of identity provider.

   2. Using the following credentials, select a provider, log in, and allow the application to access user information:

      * AM: user `demo`, password `Ch4ng31t`.

      * PingOne Advanced Identity Cloud: user `demo`, password `Ch4ng3!t`

        The home page of the sample application is displayed.
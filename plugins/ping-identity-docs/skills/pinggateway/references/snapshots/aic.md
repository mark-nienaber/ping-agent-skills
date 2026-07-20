---
title: Move to Advanced Identity Cloud
description: Use PingGateway to route requests when switching from a self-managed PingAM deployment to PingOne Advanced Identity Cloud for OAuth 2.0, OIDC, and SAML V2.0.
component: pinggateway
version: 2026
page_id: pinggateway:aic:switch-to-saas
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/switch-to-saas.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-12-04
section_ids:
  constraints: Constraints for this use case
  tasks: Tasks
  before_you_begin: Before you begin
  task_1_share_keys: "Task 1: Share keys"
  task_2_configure_network_settings: "Task 2: Configure network settings"
  task_3_configure_idp_settings: "Task 3: Configure IdP settings"
  task_4_set_up_pinggateway: "Task 4: Set up PingGateway"
  validation: Validation
---

# Move to Advanced Identity Cloud

PingGateway can help you switch from a self-managed or on-premise AM deployment to PingOne Advanced Identity Cloud.

This page describes how to make the move by using PingGateway in front of the existing deployment to route requests to the appropriate Advanced Identity Cloud realm endpoints.

This example covers OAuth 2.0, OpenID Connect (OIDC), and Security Assertion Markup Language (SAML) V2.0 deployments. Actual steps depend on your deployment and requirements.

|   |                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [Ping Identity Professional Services](https://www.pingidentity.com/en/support/professional-services.html) can assist you with this and other deployment projects. Don't hesitate to contact them for help. |

## Constraints for this use case

This high-level use case applies to self-managed or on-premise AM deployments with:

* AM playing the role of identity provider (IdP) for OAuth 2.0, OpenID Connect (OIDC), or Security Assertion Markup Language (SAML) V2.0.

  Advanced Identity Cloud can play the IdP role in these deployments.

* At most two realms.

  Advanced Identity Cloud supports `alpha` and `bravo` realms.

  The steps and examples in this page focus on switching a single realm deployment. Repeat the instructions as needed for a two-realm deployment.

* A single FQDN as the entry point to AM services.

  Advanced Identity Cloud lets you configure custom domains per realm.

  The deployment can achieve this with either a site configuration or by using a DNS mapping for the Advanced Identity Cloud realm.

* Signing and encryption keys you can export from AM and import into Advanced Identity Cloud.

  Advanced Identity Cloud needs the same keys as the AM deployment so the client applications and service providers (SPs) continue to trust tokens and assertions without changes.

This use case *doesn't* apply to deployments that don't follow these constraints.

This use case also *doesn't* address how to:

* Move data from a self-managed deployment to PingOne Advanced Identity Cloud.

  You must migrate the data separately before switching to Advanced Identity Cloud.

  The data to migrate includes client application and end-user profiles, authentication journeys, and policies.

  End users, client applications, and SPs must find their data in the Advanced Identity Cloud tenant as in the AM deployment.

* Adapt custom code and custom integrations to work with PingOne Advanced Identity Cloud.

* Prevent Advanced Identity Cloud access from direct requests that don't go through PingGateway.

  If needed, you can do this with [PingOne Advanced Identity Cloud Proxy Connect](proxy-connect.html).

## Tasks

The following tasks describe how to use PingGateway to switch from an AM deployment to a deployment with a *single Advanced Identity Cloud tenant*, such as a development tenant.

After you [promote your tenant configuration](https://docs.pingidentity.com/pingoneaic/tenants/self-service-promotions.html) and ESVs, Update the PingGateway configuration, such as its configuration properties, to match the current tenant.

### Before you begin

Make sure:

* The AM deployment fits the [Constraints for this use case](#constraints).

* You can access and configure the PingOne Advanced Identity Cloud tenant as an administrator.

* You can configure DNS settings for the custom domain in Advanced Identity Cloud.

* You can install and configure PingGateway in the existing AM deployment.

### Task 1: Share keys

1. Export the IdP signing and encryption keys from AM.

   Learn more in the AM documentation on [Secrets, certificates, and keys](https://docs.pingidentity.com/pingam/8.1/security/secrets-certs-keys.html).

2. Import each key into Advanced Identity Cloud as an environment secret (ESV).

   Learn more in the Advanced Identity Cloud documentation on [managing ESVs](https://docs.pingidentity.com/pingoneaic/tenants/esvs-manage-ui.html).

3. In the AM admin UI for the target realm, map each ESV to the corresponding realm key alias.

   For example, the OAuth 2.0 signing keys map to the following key aliases, depending on the algorithm:

   * `am.services.oauth2.stateless.signing.ES256`

   * `am.services.oauth2.stateless.signing.ES384`

   * `am.services.oauth2.stateless.signing.ES512`

   * `am.services.oauth2.stateless.signing.HMAC`

   * `am.services.oauth2.stateless.signing.RSA`

   The SAML V2.0 ESVs map to the following key aliases:

   * `am.default.applications.federation.entity.providers.saml2.idp.encryption`

   * `am.default.applications.federation.entity.providers.saml2.idp.signing`

   Find the complete lists of key aliases using the links in the Advanced Identity Cloud documentation on [secret labels](https://docs.pingidentity.com/pingoneaic/am-reference/secret-id-mappings.html) and the AM documentation on [default key aliases](https://docs.pingidentity.com/pingam/8.1/security/change-signing-key.html).

You have successfully shared the relevant keys from the AM deployment with the Advanced Identity Cloud tenant.

### Task 2: Configure network settings

In the Advanced Identity Cloud tenant:

1. Configure a custom domain for the target realm in Advanced Identity Cloud to match the FQDN used by the AM deployment.

   Don't yet change the DNS settings to point to Advanced Identity Cloud, as requests must go through PingGateway first.

   Learn more in the Advanced Identity Cloud documentation on [custom domains](https://docs.pingidentity.com/pingoneaic/realms/custom-domains.html).

2. Configure cross-origin resource sharing (CORS) settings for the target realm in Advanced Identity Cloud as needed.

   Learn more in the Advanced Identity Cloud documentation on [CORS](https://docs.pingidentity.com/pingoneaic/tenants/cors.html).

You have successfully prepared the target realm in Advanced Identity Cloud to use the same FQDN as the AM deployment but haven't yet updated DNS to change the FQDN to direct to Advanced Identity Cloud.

### Task 3: Configure IdP settings

In the Advanced Identity Cloud tenant:

1. Go to the AM admin UI for the target realm.

2. Under Services, configure the `OAuth2Provider` service settings to match the AM deployment for OAuth 2.0 and OIDC.

   When the AM deployment doesn't use DNS aliases for realms, the issuer claim in Advanced Identity Cloud ID tokens can differ from those in the AM deployment. In this case, override the `iss` claim in Advanced Identity Cloud to match the AM deployment. Add `iss` to OpenID Connect > Overrideable Id\_Token Claims and edit the OIDC claims script for the realm to return the expected value.

3. Under Applications > Federation, configure the circle of trust (CoT) and hosted IdP settings using the same entity ID and meta alias to match the AM deployment for SAML V2.0.

   With the same entity ID, the IdP metadata for Advanced Identity Cloud matches the AM deployment and avoids changes for SPs. By using the same names settings for the CoT, you make it easier to compare the two deployments.

   Make sure you duplicate the SAML IdP location settings from the AM deployment in Advanced Identity Cloud. The single sign-on (SSO) and single logout (SLO) endpoints use these to validate the destination attribute in SSO and SLO requests. This ensures SP requests using the original AM IdP remain valid.

You have successfully configured Advanced Identity Cloud to act as the IdP for OAuth 2.0, OIDC, and SAML V2.0.

### Task 4: Set up PingGateway

The examples in this section set up PingGateway for an AM deployment moving to an Advanced Identity Cloud deployment. The two deployments have these characteristics:

* AM deployment base URL

  `https://company.example.com/openam`

* AM realm to move

  `customers`

* Advanced Identity Cloud access management base URL

  `https://openam-company.forgeblocks.com/am`

* Advanced Identity Cloud target realm

  `alpha`

Follow these steps to set up PingGateway:

1. Install PingGateway in the existing AM deployment.

   Learn more in [Installing PingGateway](../installation-guide/preface.html).

2. Add a file for configuration properties to route requests, adapting the following example for your deployment:

   * Linux

     `$HOME/.openig/config/s2sProps.json`

   * Windows

     `%appdata%\OpenIG\config\s2sProps.json`

   > **Collapse: Show source**
   >
   > (Source: [s2sProps.json](../_attachments/config/s2sProps.json))
   >
   > ```json
   > {
   >   "s2s": {
   >     "aicUrl": "https://openam-company.forgeblocks.com",
   >     "aicHost": "openam-company.forgeblocks.com",
   >     "aicHostHeader": "company.example.com",
   >     "mappings": {
   >       "amFromPath": "/openam",
   >       "aicToPath": "/am",
   >       "saml": {
   >         "idp": {
   >           "amSSORedirect": "/openam/SSORedirect/metaAlias/customers/idp",
   >           "aicSSORedirect": "/am/SSORedirect/metaAlias/alpha/idp",
   >           "amSSOPOST": "/openam/SSOPOST/metaAlias/customers/idp",
   >           "aicSSOPOST": "/am/SSOPOST/metaAlias/alpha/idp",
   >           "amSLORedirect": "/openam/IDPSloRedirect/metaAlias/customers/idp",
   >           "aicSLORedirect": "/am/IDPSloRedirect/metaAlias/alpha/idp",
   >           "amSLOPOST": "/openam/IDPSloPOST/metaAlias/customers/idp",
   >           "aicSLOPOST": "/am/IDPSloPOST/metaAlias/alpha/idp"
   >         }
   >       },
   >       "openid": {
   >         "am": "/am/oauth2/realms/root/realms/customers",
   >         "aic": "/am/oauth2/realms/root/realms/alpha"
   >       }
   >     }
   >   }
   > }
   > ```

3. Edit the PingGateway `config.json` file to reference the properties file and use the properties.

   > **Collapse: Show source**
   >
   > (Source: [config-s2s.json](../_attachments/config/config-s2s.json))
   >
   > ```json
   > {
   >   "properties": {
   >     "$location:s2s": "${fileToUrl(openig.configDirectory)}/s2sProps.json"
   >   },
   >   "heap": [
   >     {
   >       "name": "Router",
   >       "type": "Router",
   >       "config": {
   >         "directory": "${openig.configDirectory}/routes"
   >       }
   >     },
   >     {
   >       "name": "RewriteAmPaths",
   >       "type": "UriPathRewriteFilter",
   >       "config": {
   >         "mappings": {
   >           "${s2s.mappings.amFromPath}": "${s2s.mappings.aicToPath}",
   >           "${s2s.mappings.saml.idp.amSSORedirect}": "${s2s.mappings.saml.idp.aicSSORedirect}",
   >           "${s2s.mappings.saml.idp.amSSOPOST}": "${s2s.mappings.saml.idp.aicSSOPOST}",
   >           "${s2s.mappings.saml.idp.amSLORedirect}": "${s2s.mappings.saml.idp.aicSLORedirect}",
   >           "${s2s.mappings.saml.idp.amSLOPOST}": "${s2s.mappings.saml.idp.aicSLOPOST}",
   >           "${s2s.mappings.openid.am}": "${s2s.mappings.openid.aic}"
   >         }
   >       }
   >     },
   >     {
   >       "name": "SetAicHostHeader",
   >       "type": "HeaderFilter",
   >       "config": {
   >         "messageType": "REQUEST",
   >         "replace": {
   >           "host": [
   >             "${s2s.aicHost}"
   >           ]
   >         }
   >       }
   >     },
   >     {
   >       "name": "ResetCookieDomain",
   >       "type": "SetCookieUpdateFilter",
   >       "config": {
   >         "cookies": {
   >           ".*": {
   >             "domain": "${s2s.aicHostHeader}"
   >           }
   >         }
   >       }
   >     }
   >   ],
   >   "handler": "Router"
   > }
   > ```

   This configuration adds filters to:

   * Map AM request paths to the Advanced Identity Cloud endpoints.

   * Rewrite the host header in requests to match the Advanced Identity Cloud tenant domain.

   * Set the cookie domain to match the Advanced Identity Cloud custom domain.

4. Restart PingGateway to load the configuration changes.

5. Add a route to direct filtered requests to Advanced Identity Cloud:

   * Linux

     `$HOME/.openig/config/routes/s2s.json`

   * Windows

     `%appdata%\OpenIG\config\routes\s2s.json`

   > **Collapse: Show route**
   >
   > (Source: [s2s.json](../_attachments/config/routes/s2s.json))
   >
   > ```json
   > {
   >   "name": "S2S",
   >   "baseURI": "${s2s.aicUrl}",
   >   "handler": {
   >     "type": "Chain",
   >     "config": {
   >       "filters": [
   >         "ResetCookieDomain",
   >         "RewriteAmPaths",
   >         "SetAicHostHeader"
   >       ],
   >       "handler": "ReverseProxyHandler"
   >     }
   >   }
   > }
   > ```

   This route applies the filters defined in the configuration and directs requests to the Advanced Identity Cloud endpoints.

You have successfully set up PingGateway to route requests from the AM deployment to the Advanced Identity Cloud target realm.

## Validation

When testing your setup:

* Use test clients and SPs that represent the traffic in the existing AM deployment.

* As a baseline, test the existing AM deployment to define the expected behavior.

* After rolling out PingGateway, test the same clients and SPs to verify they work as expected with Advanced Identity Cloud.

After you validate all client applications and SPs work as expected with PingGateway, consider updating the DNS settings for the custom domain to point to Advanced Identity Cloud directly. After you do this and validate everything still works, you can retire the existing deployment.

You have successfully demonstrated how to switch from a self-managed or on-premise AM deployment to PingOne Advanced Identity Cloud.

---

---
title: OAuth 2.0 and PingOne Advanced Identity Cloud
description: Configure PingGateway as an OAuth 2.0 resource server with PingOne Advanced Identity Cloud as the Authorization Server using token introspection
component: pinggateway
version: 2026
page_id: pinggateway:aic:oauthrs
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/oauthrs.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Single sign-on (SSO)", "Security", "Authenticate", "OAuth 2.0"]
page_aliases: ["identity-cloud-guide:oauthrs.adoc"]
---

# OAuth 2.0 and PingOne Advanced Identity Cloud

This example sets up OAuth 2.0, using the standard introspection endpoint, where PingOne Advanced Identity Cloud is the Authorization Server and PingGateway is the resource server.

Learn about PingGateway as an OAuth 2.0 resource server in [Validating PingAM access tokens with introspection](../gateway-guide/oauth2-rs-introspect.html).

|   |                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure uses the *Resource Owner Password Credentials* grant type. As suggested in [The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749#section-10.7), use other grant types whenever possible. |

Before you start, prepare PingOne Advanced Identity Cloud, PingGateway, and the sample application as described in [Example installation for this guide](preface.html#preface-examples).

1. Set up PingOne Advanced Identity Cloud:

   1. Log in to the Advanced Identity Cloud admin UI as an administrator.

   2. Make sure you are managing the `alpha` realm. If not, click the current realm at the top of the screen, and switch realm.

   3. Go to [icon: group, set=material, size=inline] Identities > Manage > [icon: settings_system_daydream, set=material, size=inline] Alpha realm - Users, and add a user with the following values:

      * Username: `demo`

      * First name: `demo`

      * Last name: `user`

      * Email Address: `demo@example.com`

      * Password: `Ch4ng3!t`

   4. Go to [icon: th, set=fa]Custom Application > [icon: plus, set=fa]Custom Application > OIDC - OpenId Connect > Web and add a web application with the following values:

      * Name: `oauth2-client`

      * Owners: `demo user`

      * Client Secret: `password`

      * (Optional) Use Secret Store for password: Select this to store the password in an ESV secret.

        If you select this option, enter a Secret Label Identifier. This value represents the `identifier` part of the secret label for the client. PingOne Advanced Identity Cloud uses the identifier to generate a secret label in the following format: `am.applications.oauth2.client.identifier.secret`.

        To complete the client profile, add an ESV secret for the password and map the ESV to the secret label. To learn more, read [Secret labels](https://docs.pingidentity.com/pingoneaic/tenants/esvs-signing-encryption.html#secret-labels) in the PingOne Advanced Identity Cloud documentation.

      * Sign On > Grant Types: `Authorization Code`, `Resource owner Password Credentials`

      * Sign On > Scopes: `mail`

        For more information, refer to PingOne Advanced Identity Cloud's [Application management](https://docs.pingidentity.com/pingoneaic/app-management/applications.html).

   5. Register a PingGateway agent with the following values, as described in [Register a PingGateway agent in PingOne Advanced Identity Cloud](preface.html#register-agent-idc):

      * ID: `ig_agent`

      * Password: `password`

2. Set up PingGateway:

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Set an environment variable for the PingGateway agent password, and then restart PingGateway:

      ```console
      $ export AGENT_SECRET_ID='cGFzc3dvcmQ='
      ```

      The password is retrieved by a SystemAndEnvSecretStore, and must be base64-encoded.

   3. Add the following route to PingGateway, replacing the value for the property `amInstanceUrl`:

      * Linux

        `$HOME/.openig/config/routes/oauth2rs-idc.json`

      * Windows

        `%appdata%\OpenIG\config\routes\oauth2rs-idc.json`

      ```json
      {
        "name": "oauth2rs-idc",
        "condition": "${find(request.uri.path, '^/oauth2rs-idc')}",
        "properties": {
          "amInstanceUrl": "https://myTenant.forgeblocks.com/am"
        },
        "heap": [
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          },
          {
            "name": "AmService-1",
            "type": "AmService",
            "config": {
              "url": "&{amInstanceUrl}",
              "realm": "/alpha",
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
                "name": "OAuth2ResourceServerFilter-1",
                "type": "OAuth2ResourceServerFilter",
                "config": {
                  "scopes": [
                    "mail"
                  ],
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
                "entity": "<html><body><h2>Decoded access_token: ${contexts.oauth2.accessToken.info}</h2></body></html>"
              }
            }
          }
        }
      }
      ```

      Source: [oauth2rs-idc.json](../_attachments/config/routes/oauth2rs-idc.json)

      Notice the following features of the route compared to `rs-introspect.json` in [Validating PingAM access tokens with introspection](../gateway-guide/oauth2-rs-introspect.html), where a local PingAM instance is the Authorization Server:

      * The AmService `URL` points to PingAM in PingOne Advanced Identity Cloud.

      * The AmService `realm` points to the realm where you have configured your web application and the PingGateway agent.

3. Test the setup:

   1. In a terminal, export an environment variable for the URL of PingAM in PingOne Advanced Identity Cloud:

      ```console
      $ export amInstanceUrl='myAmInstanceUrl'
      ```

   2. Use a `curl` command similar to the following to retrieve an access token:

      ```console
      $ mytoken=$(curl -s \
      --user "oauth2-client:password" \
      --data 'grant_type=password&username=demo&password=Ch4ng3!t&scope=mail' \
      $amInstanceUrl/oauth2/realms/alpha/access_token | jq -r ".access_token")
      ```

   3. Validate the access token returned in the previous step:

      ```console
      $ curl -v \
      --cacert /path/to/secrets/ig.example.com-certificate.pem \
      --header "Authorization: Bearer ${mytoken}" \
      https://ig.example.com:8443/oauth2rs-idc 
      ```

      Output

      ```none
      {
        active = true,
        scope = mail,
        realm = /alpha,
        client_id = oauth2-client,
        ...
      }
      ```

---

---
title: OpenID Connect and PingOne Advanced Identity Cloud
description: Configure PingOne Advanced Identity Cloud as an OpenID Connect provider with PingGateway as a relying party
component: pinggateway
version: 2026
page_id: pinggateway:aic:oidc
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/oidc.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Single sign-on (SSO)", "Security", "Authenticate", "OAuth 2.0", "OpenID Connect (OIDC)"]
page_aliases: ["identity-cloud-guide:oidc.adoc"]
---

# OpenID Connect and PingOne Advanced Identity Cloud

This example sets up PingOne Advanced Identity Cloud as an OpenID Connect (OIDC) provider with PingGateway as a relying party.

For more information about PingGateway and OIDC, refer to [OpenID Connect and PingAM](../gateway-guide/oidc.html).

Before you start, prepare PingOne Advanced Identity Cloud, PingGateway, and the sample application as described in [Example installation for this guide](preface.html#preface-examples).

1. Set up PingOne Advanced Identity Cloud:

   1. Log in to the Advanced Identity Cloud admin UI as an administrator.

   2. Make sure you are managing the `alpha` realm. If not, click the current realm at the top of the screen, and switch realm.

   3. Go to [icon: group, set=material, size=inline] Identities > Manage > [icon: settings_system_daydream, set=material, size=inline] Alpha realm - Users, and add a user with the following values:

      * Username: `demo`

      * First name: `demo`

      * Last name: `user`

      * Email Address: `demo@example.com`

      * Password: `Ch4ng3!t`

   4. Go to [icon: th, set=fa]Custom Application > [icon: plus, set=fa]Custom Application > OIDC - OpenId Connect > Web and add a web application with the following values:

      * Name: `oidc_client`

      * Owners: `demo user`

      * Client Secret: `password`

      * (Optional) Use Secret Store for password: Select this to store the password in an ESV secret.

        If you select this option, enter a Secret Label Identifier. This value represents the `identifier` part of the secret label for the client. PingOne Advanced Identity Cloud uses the identifier to generate a secret label in the following format: `am.applications.oauth2.client.identifier.secret`.

        To complete the client profile, add an ESV secret for the password and map the ESV to the secret label. To learn more, read [Secret labels](https://docs.pingidentity.com/pingoneaic/tenants/esvs-signing-encryption.html#secret-labels) in the PingOne Advanced Identity Cloud documentation.

      * Sign On > Sign-in URLs: `https://ig.example.com:8443/home/id_token/callback`

      * Sign On > Grant Types: `Authorization Code`

      * Sign On > Scopes: `openid`, `profile`, `email`

      * Show advanced settings > Authentication > Implied Consent: `On`

   For more information, refer to PingOne Advanced Identity Cloud's [Application management](https://docs.pingidentity.com/pingoneaic/app-management/applications.html).

2. Set up PingGateway:

   1. Set an environment variable for the `oidc_client` password, and then restart PingGateway:

      ```console
      $ export OIDC_SECRET_ID='cGFzc3dvcmQ='
      ```

   2. Make sure PingGateway connects to the sample application over HTTPS with a route to access static resources.

      Learn more in [Using the sample application](../getting-started/start-sampleapp.html).

   3. Add the following route to PingGateway, replacing the value for the property `amInstanceUrl`:

      * Linux

        `$HOME/.openig/config/routes/oidc-idc.json`

      * Windows

        `%appdata%\OpenIG\config\routes\oidc-idc.json`

      ```json
      {
        "name": "oidc-idc",
        "baseURI": "https://app.example.com:8444",
        "condition": "${find(request.uri.path, '^/home/id_token')}",
        "properties": {
          "amInstanceUrl": "https://myTenant.forgeblocks.com/am"
        },
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
                      "name": "oauth2-client",
                      "type": "ClientRegistration",
                      "config": {
                        "clientId": "oidc_client",
                        "issuer": {
                          "name": "Issuer",
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

      Source: [oidc-idc.json](../_attachments/config/routes/oidc-idc.json)

      Compared to `07-openid.json` in [AM as OIDC provider](../gateway-guide/oidc-am.html), where PingAM is running locally, the ClientRegistration `wellKnownEndpoint` points to PingOne Advanced Identity Cloud.

3. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/id_token>.

      The PingOne Advanced Identity Cloud login page is displayed.

   2. Log in to PingOne Advanced Identity Cloud as user `demo`, password `Ch4ng3!t`. The home page of the sample application is displayed.

---

---
title: Passing PingOne Advanced Identity Cloud runtime data downstream in a JWT
description: Configure PingOne Advanced Identity Cloud as an identity provider to pass runtime identity data downstream in a JWT signed with a PEM, using PingGateway
component: pinggateway
version: 2026
page_id: pinggateway:aic:runtime
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/runtime.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Single sign-on (SSO)", "Security", "PEM"]
page_aliases: ["identity-cloud-guide:runtime.adoc"]
---

# Passing PingOne Advanced Identity Cloud runtime data downstream in a JWT

This example sets up PingOne Advanced Identity Cloud as an identity provider, to pass identity or other runtime information downstream, in a JWT signed with a PEM.

For more information about using runtime data, refer to [Passing PingAM data along the chain](../gateway-guide/data-downstream.html). To help with development, the sample application includes a `/jwt` endpoint to display the JWT, verify its signature, and decrypt it.

Before you start, prepare PingOne Advanced Identity Cloud, PingGateway, and the sample application as described in [Example installation for this guide](preface.html#preface-examples).

1. Set up secrets:

   1. Locate a directory for secrets and go to it:

      ```console
      $ cd /path/to/secrets
      ```

   2. Create the following secret key and certificate pair as PEM files:

      ```console
      $ openssl req \
      -newkey rsa:2048 \
      -new \
      -nodes \
      -x509 \
      -days 3650 \
      -subj "/CN=ig.example.com/OU=example/O=com/L=fr/ST=fr/C=fr" \
      -keyout ig.example.com-key.pem \
      -out ig.example.com-certificate.pem
      ```

      Two PEM files are created, one for the secret key, and another for the associated certificate.

   3. Map the key and certificate to the same secret ID in PingGateway:

      ```console
      $ cat ig.example.com-key.pem ig.example.com-certificate.pem > key.manager.secret.id.pem
      ```

   4. Generate PEM files to sign and verify the JWT:

      ```console
      $ openssl req \
      -newkey rsa:2048 \
      -new \
      -nodes \
      -x509 \
      -days 3650 \
      -subj "/CN=ig.example.com/OU=example/O=com/L=fr/ST=fr/C=fr" \
      -keyout id.key.for.signing.jwt.pem \
      -out id.key.for.verifying.jwt.pem
      ```

   5. Make sure the following files have been added to your secrets directory:

      * `id.key.for.signing.jwt.pem`

      * `id.key.for.verifying.jwt.pem`

      * `key.manager.secret.id.pem`

      * `ig.example.com-certificate.pem`

      * `ig.example.com-key.pem`

2. Set up PingOne Advanced Identity Cloud:

   1. Log in to the Advanced Identity Cloud admin UI as an administrator.

   2. Go to [icon: group, set=material, size=inline] Identities > Manage > [icon: settings_system_daydream, set=material, size=inline] Alpha realm - Users, and add a user with the following values:

      * Username: `demo`

      * First name: `demo`

      * Last name: `user`

      * Email Address: `demo@example.com`

      * Password: `Ch4ng3!t`

   3. Register a PingGateway agent with the following values, as described in [Register a PingGateway agent in PingOne Advanced Identity Cloud](preface.html#register-agent-idc):

      * ID: `ig_agent_jwt`

      * Password: `password`

      * Redirect URLs: `https://ig.example.com:8443/jwt/redirect`

   4. Add a Validation Service:

      1. In PingOne Advanced Identity Cloud, select [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management. The AM admin UI is displayed.

      2. Select Services, and add a validation service with the following Valid goto URL Resources:

         * `https://ig.example.com:8443/*`

         * `https://ig.example.com:8443/*?*`

3. Set up PingGateway:

   1. Set up TLS by adding the following file to PingGateway, replacing the value for the property `secretsDir`:

      * Linux

        `$HOME/.openig/config/admin.json`

      * Windows

        `%appdata%\OpenIG\config\admin.json`

      ```json
      {
        "mode": "DEVELOPMENT",
        "properties": {
          "secretsDir": "/path/to/secrets"
        },
        "connectors": [
          {
            "port": 8080
          },
          {
            "port": 8443,
            "tls": "ServerTlsOptions-1"
          }
        ],
        "heap": [
          {
            "name": "ServerTlsOptions-1",
            "type": "ServerTlsOptions",
            "config": {
              "keyManager": {
                "type": "SecretsKeyManager",
                "config": {
                  "signingSecretId": "key.manager.secret.id",
                  "secretsProvider": "ServerIdentityStore"
                }
              }
            }
          },
          {
            "name": "ServerIdentityStore",
            "type": "FileSystemSecretStore",
            "config": {
              "format": "PLAIN",
              "directory": "&{secretsDir}",
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

      Source: [admin-https-jwt.json](../_attachments/config/admin-https-jwt.json)

   2. Set an environment variable for the PingGateway agent password, and then restart PingGateway:

      ```console
      $ export AGENT_SECRET_ID='cGFzc3dvcmQ='
      ```

      The password is retrieved by a SystemAndEnvSecretStore, and must be base64-encoded.

   3. Make sure PingGateway connects to the sample application over HTTPS with a route to access static resources.

      Learn more in [Using the sample application](../getting-started/start-sampleapp.html).

   4. Add the following route to PingGateway, replacing the value for the properties `secretsDir` and `amInstanceUrl`:

      * Linux

        `$HOME/.openig/config/routes/jwt-idc.json`

      * Windows

        `%appdata%\OpenIG\config\routes\jwt-idc.json`

      ```json
      {
        "name": "jwt-idc",
        "condition": "${find(request.uri.path, '/jwt')}",
        "baseURI": "https://app.example.com:8444",
        "properties": {
          "secretsDir": "/path/to/secrets",
          "amInstanceUrl": "https://myTenant.forgeblocks.com/am"
        },
        "heap": [
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          },
          {
            "name": "AmService-1",
            "type": "AmService",
            "config": {
              "url": "&{amInstanceUrl}",
              "realm": "/alpha",
              "agent": {
                "username": "ig_agent_jwt",
                "passwordSecretId": "agent.secret.id"
              },
              "secretsProvider": "SystemAndEnvSecretStore-1",
              "sessionCache": {
                "enabled": false
              }
            }
          },
          {
            "name": "pemPropertyFormat",
            "type": "PemPropertyFormat"
          },
          {
            "name": "FileSystemSecretStore-1",
            "type": "FileSystemSecretStore",
            "config": {
              "format": "PLAIN",
              "directory": "&{secretsDir}",
              "suffix": ".pem",
              "mappings": [{
                "secretId": "id.key.for.signing.jwt",
                "format": "pemPropertyFormat"
              }]
            }
          }
        ],
        "session": {
          "type": "InMemorySessionManager",
          "config": {
            "cookie": {
              "sameSite": "none",
              "secure": true
            }
          }
        },
        "handler": {
          "type": "Chain",
          "config": {
            "filters": [
              {
                "name": "CrossDomainSingleSignOnFilter-1",
                "type": "CrossDomainSingleSignOnFilter",
                "config": {
                  "redirectEndpoint": "/jwt/redirect",
                  "authCookie": {
                    "path": "/jwt",
                    "name": "ig-token-cookie"
                  },
                  "amService": "AmService-1"
                }
              },
              {
                "name": "UserProfileFilter",
                "type": "UserProfileFilter",
                "config": {
                  "username": "${contexts.ssoToken.info.uid}",
                  "userProfileService": {
                    "type": "UserProfileService",
                    "config": {
                      "amService": "AmService-1"
                    }
                  }
                }
              },
              {
                "name": "JwtBuilderFilter-1",
                "type": "JwtBuilderFilter",
                "config": {
                  "template": {
                    "name": "${contexts.userProfile.commonName}",
                    "email": "${contexts.userProfile.rawInfo.mail[0]}"
                  },
                  "secretsProvider": "FileSystemSecretStore-1",
                  "signature": {
                    "secretId": "id.key.for.signing.jwt",
                    "algorithm": "RS512"
                  }
                }
              },
              {
                "name": "HeaderFilter-1",
                "type": "HeaderFilter",
                "config": {
                  "messageType": "REQUEST",
                  "add": {
                    "x-openig-user": ["${contexts.jwtBuilder.value}"]
                  }
                }
              }
            ],
            "handler": "ReverseProxyHandler"
          }
        }
      }
      ```

      Source: [jwt-idc.json](../_attachments/config/routes/jwt-idc.json)

4. Test the setup:

   1. Go to <https://ig.example.com:8443/jwt>.

      If you receive warnings that the site is not secure, respond to the warnings to access the site. The PingOne Advanced Identity Cloud login page is displayed.

   2. Log in to PingOne Advanced Identity Cloud as user `demo`, password `Ch4ng3!t`. The sample app displays the signed JWT along with its header and payload.

   3. In `USE PEM FILE`, enter the absolute path to `id.key.for.verifying.jwt.pem` to verify the JWT signature.

---

---
title: Password replay and PingOne Advanced Identity Cloud
description: Configure PingGateway to capture and replay user credentials to legacy web applications using a PingOne Advanced Identity Cloud journey and shared secret key
component: pinggateway
version: 2026
page_id: pinggateway:aic:password-replay
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/password-replay.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-02-16T12:00:00Z
keywords: ["Configuration", "Authentication", "Single sign-on (SSO)", "Cross Domain SSO (CDSSO)", "Nodes &amp; Trees", "Password"]
page_aliases: ["identity-cloud-guide:password-replay.adoc"]
section_ids:
  request_flow: Request flow
  tasks: Tasks
  before_you_begin: Before you begin
  task_1_run_the_sample_application: "Task 1: Run the sample application"
  task_2_install_pinggateway: "Task 2: Install PingGateway"
  task_3_register_pinggateway_with_pingone_advanced_identity_cloud: "Task 3: Register PingGateway with PingOne Advanced Identity Cloud"
  task_4_prepare_a_shared_secret: "Task 4: Prepare a shared secret"
  task_5_prepare_pingone_advanced_identity_cloud: "Task 5: Prepare PingOne Advanced Identity Cloud"
  pwd-replay-config-gateway: "Task 6: Configure PingGateway"
  task_7_create_a_test_user_in_pingone_advanced_identity_cloud: "Task 7: Create a test user in PingOne Advanced Identity Cloud"
  validation: Validation
---

# Password replay and PingOne Advanced Identity Cloud

Password replay brings single sign-on (SSO) to legacy web applications without the need to edit, upgrade, or recode them.

Use PingGateway with an appropriate PingOne Advanced Identity Cloud journey to capture and replay username password credentials. PingGateway and PingOne Advanced Identity Cloud share a secret key to encrypt and decrypt the password and keep it safe.

When running AM in a self-hosted deployment, read [Password replay with AM](../gateway-guide/credentials-am.html).

## Request flow

![Replay a user's password to access a protected application.](_images/password-replay.svg)Figure 1. Password replay sequence diagram

* PingGateway intercepts the browser's HTTP GET request.

* PingGateway redirects the user to the appropriate PingOne Advanced Identity Cloud journey for authentication.

* PingOne Advanced Identity Cloud authenticates the user and stores the encrypted password in a JWT.

* PingOne Advanced Identity Cloud redirects the browser back to the protected application with the JWT.

* PingGateway intercepts the browser's HTTP GET request again:

  * The user is authenticated.

  * PingGateway gets the password from the JWT and decrypts it.

  * PingGateway gets the username from PingOne Advanced Identity Cloud based on the user `_id`.

* PingGateway replaces the request with an HTTP POST to the application, taking the credentials from the context.

* The sample application validates the credentials from the HTTP POST request.

* The sample application responds with the user's profile page.

* PingGateway passes the response from the sample application to the browser.

## Tasks

### Before you begin

* Make sure you can access the PingOne Advanced Identity Cloud tenant as an administrator.

* Choose the realm to use in the PingOne Advanced Identity Cloud tenant.

  The following tasks use the `alpha` realm.

* [Prepare hostnames](../getting-started/prepare-network.html) for PingGateway and the sample application.

  The following tasks use `ig.example.com` for PingGateway and `app.example.com` for the sample application.

### Task 1: Run the sample application

1. [Download the sample application](../getting-started/start-sampleapp.html#start-sampleapp-download).

2. Open a command-line window and [start the sample application](../getting-started/start-sampleapp.html#start-sampleapp-start):

   ```console
   $ java -jar PingGateway-sample-application-2026.6.0.jar
   ```

   The sample application runs in the foreground until you stop it.

### Task 2: Install PingGateway

This task installs PingGateway, but doesn't configure it for password replay yet.

1. [Download and unpack PingGateway](../getting-started/download-product.html).

2. [Configure PingGateway for HTTPS](../installation-guide/securing-connections.html#server-side-tls).

3. [Configure PingGateway to trust the sample application for HTTPS](../getting-started/start-sampleapp.html#sampleapp-trust) and access sample application static resources.

4. Set a top-level `session` property in `config.json` alongside the `heap` and `connections`:

   ```none
   "session": {
           "type": "InMemorySessionManager",
           "config": {
               "cookie": {
                   "sameSite": "none",
                   "secure": true
               }
           }
       }
   ```

   PingOne Advanced Identity Cloud prompts the browser to send a session cookie on successful authentication.

   * When `sameSite` is `strict` or `lax`, the browser doesn't send the session cookie with the nonce used in validation. If PingGateway doesn't find the nonce, it assumes that the authentication failed.

   * When `secure` is `false`, the browser is likely to reject the session cookie.

   Restart PingGateway to read the updated configuration.

5. Add the following route to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/01-static.json`

   * Windows

     `%appdata%\OpenIG\config\routes\01-static.json`

   ```json
   {
     "handler": {
       "type": "Chain",
       "config": {
         "filters": [
           {
             "type": "StaticRequestFilter",
             "config": {
               "method": "POST",
               "uri": "https://app.example.com:8444/login",
               "form": {
                 "username": [
                   "demo"
                 ],
                 "password": [
                   "Ch4ng31t"
                 ]
               }
             }
           }
         ],
         "handler": "ReverseProxyHandler"
       }
     },
     "condition": "${find(request.uri.path, '^/static')}"
   }
   ```

   Source: [01-static.json](../_attachments/config/routes/01-static.json)

   Notice the following features of the route:

   * The route matches requests to `/static`.

   * The StaticRequestFilter replaces the request with an HTTP POST, specifying the resource to post the request to, and a form to include in the request. The form includes credentials for the username `demo`.

   * The ReverseProxyHandler replays the request to the sample application.

6. Verify sample application access through PingGateway by browsing <https://ig.example.com:8443/static>.

   You might have used a self-signed certificate for the PingGateway HTTPS configuration. If your browser doesn't recognize the PingGateway certificate and flags it as a security risk, choose to continue.

   PingGateway displays a basic profile page for the `demo` user.

PingGateway now has the configuration required as a basis on which to build password replay.

### Task 3: Register PingGateway with PingOne Advanced Identity Cloud

If you haven't yet registered PingGateway with PingOne Advanced Identity Cloud, follow these steps:

1. [Configure an `Agent` journey](preface.html#authenticate-agent-idc) PingGateway uses to authenticate with PingOne Advanced Identity Cloud.

2. [Register a profile for PingGateway](preface.html#register-agent-idc).

   | Field         | Value                                         | Description                                                                                                                                  |
   | ------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
   | ID            | `ig_agent`                                    | The PingGateway username when connecting to the `AmService` in PingOne Advanced Identity Cloud.                                              |
   | Password      | `password`                                    | The PingGateway password when connecting to the `AmService` in PingOne Advanced Identity Cloud.In production tenants, use a strong password. |
   | Redirect URLs | `https://ig.example.com:8443/replay/redirect` | The PingGateway endpoint to process the encrypted JWT from PingOne Advanced Identity Cloud.                                                  |

PingOne Advanced Identity Cloud is now ready for PingGateway to connect. You'll share the credentials with PingGateway in [Task 6: Configure PingGateway](#pwd-replay-config-gateway).

### Task 4: Prepare a shared secret

PingGateway and Advanced Identity Cloud share a secret symmetric key to encrypt and decrypt the password.

The Advanced Identity Cloud authentication journey you will configure includes the JWT Password Replay node to capture the password in an encrypted JWT it sends to PingGateway. The JWT Password Replay node relies on a secret label of the form `am.authentication.nodes.jwt.replay.identifier.encryption` to get the shared secret key. This example uses `pinggateway` as the *identifier* and stores is as an ESV secret. PingGateway stores the secret in a PEM file, so the following steps do that first:

1. Create a `secrets` folder next to the PingGateway instance folder to store the shared secret key:

   ```console
   $ mkdir secrets
   ```

2. Generate a base64-encoded shared secret using the filename the JWT Password Replay node requires:

   ```console
   $ echo "-----BEGIN AES SECRET KEY-----" > secrets/am.authentication.nodes.jwt.replay.pinggateway.encryption
   $ head -c32 /dev/urandom | base64 >> secrets/am.authentication.nodes.jwt.replay.pinggateway.encryption
   $ echo "-----END AES SECRET KEY-----" >> secrets/am.authentication.nodes.jwt.replay.pinggateway.encryption
   ```

   The file contains the base64-encoded shared secret in PEM format.

3. Store the shared secret key as an ESV in PingOne Advanced Identity Cloud.

   1. Sign on to the Advanced Identity Cloud admin UI as an administrator and go to [icon: cog, set=fa]Tenant Settings > Global Settings > Environment Secrets & Variables.

   2. Click Secrets > + Add Secret.

   3. In the Add a Secret modal, enter the following settings:

      | Field | Value                                          | Description                                |
      | ----- | ---------------------------------------------- | ------------------------------------------ |
      | Name  | `esv-password-replay-shared-secret`            | The ESV name for the secret.               |
      | Value | Base64-encoded shared secret from the PEM file | The base64-encoded random AES 256-bit key. |

   4. Click Save to create the variable.

   PingOne Advanced Identity Cloud can now access the secret through the ESV secret. PingGateway will use the secret in the local PEM file in [Task 6: Configure PingGateway](#pwd-replay-config-gateway).

You have successfully prepared the shared secret for Advanced Identity Cloud and PingGateway.

### Task 5: Prepare PingOne Advanced Identity Cloud

Update the PingOne Advanced Identity Cloud validation service for PingGateway and add a journey to use the script and a mapping for the secret.

1. Sign on to the Advanced Identity Cloud admin UI as an administrator and go to [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management, select Services, and the following Valid goto URL Resources to the Validation Service:

   * `https://ig.example.com:8443/*`

   * `https://ig.example.com:8443/*?*`

2. Go to Journeys, click + New Journey, and create a journey named `Password replay` whose Identity Object is `managed/alpha_user`.

3. Configure and save the journey with the nodes shown in this screenshot:

   ![Password replay journey](_images/password-replay-journey.png)

   * The Page node presents a page with input fields to prompt for the username and password.

     * The Platform Username node collects and injects the `userName` into the shared node state.

     * The Platform Password node collects and injects the `password` into the shared node state.

   * The Identity Store Decision node uses the username and password to determine whether authentication is successful.

   * The JWT Password Replay node stores the password in a JWT encrypted with the shared secret key. Its Encryption Key Secret Label Identifier is `pinggateway`.

4. In the AM admin UI, go to Secret Stores > ESV > Mappings and add the following mapping to let the JWT Password Replay node access the shared secret:

   * Secret Label

     `am.authentication.nodes.jwt.replay.pinggateway.encryption`

   * Active Alias

     `esv-password-replay-shared-secret`

   Make sure you save the mapping.

5. In your browser's privacy or incognito mode, go to the new journey and make sure you can sign on with the credentials of a known user.

   PingOne Advanced Identity Cloud authenticates you and displays the user profile page.

You have successfully prepared the journey and can now configure PingGateway to replay the password.

### Task 6: Configure PingGateway

The password replay configuration ensures PingGateway can connect to PingOne Advanced Identity Cloud, get the shared secret to decode the JWT with the password, and replay the credentials to the sample application.

1. Set an environment variable locally on the computer running PingGateway to access the base64-encoded agent password:

   ```console
   $ export AGENT_SECRET_ID='cGFzc3dvcmQ='
   ```

   PingGateway retrieves the password with a [SystemAndEnvSecretStore](../reference/SystemAndEnvSecretStore.html), which requires it to be base64-encoded.

   The password must match the agent profile password you set in PingOne Advanced Identity Cloud. PingGateway uses the password to connect to PingOne Advanced Identity Cloud.

2. Add a route to PingGateway to serve the sample application .css and other static resources if you haven't already:

   * Linux

     `$HOME/.openig/config/routes/00-static-resources.json`

   * Windows

     `%appdata%\OpenIG\config\routes\00-static-resources.json`

   > **Collapse: Show route**
   >
   > ```json
   > {
   >   "name" : "00-static-resources",
   >   "baseURI" : "https://app.example.com:8444",
   >   "condition": "${find(request.uri.path,'^/css') or matchesWithRegex(request.uri.path, '^/.*\\\\.ico$') or matchesWithRegex(request.uri.path, '^/.*\\\\.gif$')}",
   >   "handler": "ReverseProxyHandler"
   > }
   > ```

   Source: [00-static-resources.json](../_attachments/config/routes/00-static-resources.json)

   This route correctly sets the content types for the static resources used by the sample application.

3. Add a route for password replay.

   * Linux

     `$HOME/.openig/config/routes/04-replay-aic.json`

   * Windows

     `%appdata%\OpenIG\config\routes\04-replay-aic.json`

   > **Collapse: Show route**
   >
   > ```json
   > {
   >     "name": "04-replay-aic",
   >     "condition": "${find(request.uri.path, '^/replay')}",
   >     "properties": {
   >         "amInstanceUrl": "https://myTenant.forgeblocks.com/am/"
   >     },
   >     "heap": [
   >         {
   >             "name": "SystemAndEnvSecretStore-1",
   >             "type": "SystemAndEnvSecretStore"
   >         },
   >         {
   >             "name": "AmService-1",
   >             "type": "AmService",
   >             "config": {
   >                 "url": "&{amInstanceUrl}",
   >                 "realm": "/alpha",
   >                 "agent": {
   >                     "username": "ig_agent",
   >                     "passwordSecretId": "agent.secret.id"
   >                 },
   >                 "secretsProvider": "SystemAndEnvSecretStore-1"
   >             },
   >             "sessionCache": {
   >                 "enabled": false
   >             }
   >         },
   >         {
   >             "name": "PemPropertyFormat-1",
   >             "type": "PemPropertyFormat"
   >         },
   >         {
   >             "name": "FileSystemSecretStore-1",
   >             "type": "FileSystemSecretStore",
   >             "config": {
   >                 "format": "PLAIN",
   >                 "directory": "&{ig.instance.dir}/../secrets/",
   >                 "mappings": [
   >                     {
   >                         "secretId": "am.authentication.nodes.jwt.replay.pinggateway.encryption",
   >                         "format": "PemPropertyFormat-1"
   >                     }
   >                 ]
   >             }
   >         },
   >         {
   >             "name": "CapturedUserPasswordFilter-1",
   >             "type": "CapturedUserPasswordFilter",
   >             "config": {
   >                 "ssoToken": "${contexts.ssoToken.value}",
   >                 "keySecretId": "am.authentication.nodes.jwt.replay.pinggateway.encryption",
   >                 "secretsProvider": "FileSystemSecretStore-1",
   >                 "amService": "AmService-1"
   >             }
   >         }
   >     ],
   >     "handler": {
   >         "type": "Chain",
   >         "config": {
   >             "filters": [
   >                 {
   >                     "name": "CrossDomainSingleSignOnFilter-1",
   >                     "type": "CrossDomainSingleSignOnFilter",
   >                     "config": {
   >                         "redirectEndpoint": "/replay/redirect",
   >                         "authCookie": {
   >                             "path": "/replay",
   >                             "name": "ig-token-cookie"
   >                         },
   >                         "amService": "AmService-1",
   >                         "authenticationService": "Password replay"
   >                     }
   >                 },
   >                 {
   >                     "name": "UserProfileFilter-1",
   >                     "type": "UserProfileFilter",
   >                     "config": {
   >                         "username": "${contexts.ssoToken.info.uid}",
   >                         "userProfileService": {
   >                             "type": "UserProfileService",
   >                             "config": {
   >                                 "amService": "AmService-1",
   >                                 "profileAttributes": [
   >                                     "username"
   >                                 ]
   >                             }
   >                         }
   >                     }
   >                 },
   >                 {
   >                     "name": "PasswordReplayFilter-1",
   >                     "type": "PasswordReplayFilter",
   >                     "config": {
   >                         "loginPage": "${true}",
   >                         "credentials": "CapturedUserPasswordFilter-1",
   >                         "request": {
   >                             "method": "POST",
   >                             "uri": "https://app.example.com:8444/login",
   >                             "form": {
   >                                 "username": [
   >                                     "${contexts.userProfile.username}"
   >                                 ],
   >                                 "password": [
   >                                     "${contexts.capturedPassword.value}"
   >                                 ]
   >                             }
   >                         }
   >                     },
   >                     "capture": [
   >                         "all"
   >                     ]
   >                 }
   >             ],
   >             "handler": "ReverseProxyHandler"
   >         }
   >     }
   > }
   > ```

   Source: [04-replay-aic.json](../_attachments/config/routes/04-replay-aic.json).

   The route:

   * Matches requests whose path starts with `/replay`.

   * Sets an `amInstanceUrl` property to the access management service in PingOne Advanced Identity Cloud.

     Update the URL to target your tenant.

   * Connects to PingOne Advanced Identity Cloud as `ig_agent` with the `agent.secret.id` password from the local `AGENT_SECRET_ID` environment variable.

   * Loads the `am.authentication.nodes.jwt.replay.pinggateway.encryption` shared secret key from the PEM file.

     Make sure you're using the shared secret key you stored in the PingOne Advanced Identity Cloud ESV. PingOne Advanced Identity Cloud uses the secret key to encrypt the password to replay. PingGateway uses the secret key to decrypt the password to replay.

   * Extracts the captured password from the SSO token context and decrypts it with the shared secret key.

   * Uses a [CrossDomainSingleSignOnFilter](../reference/CrossDomainSingleSignOnFilter.html) to redirect to the PingOne Advanced Identity Cloud `Password replay` journey for authentication, getting the authentication information from the `ig-token-cookie`.

   * Queries the access management service in PingOne Advanced Identity Cloud to retrieve the username for signing on.

     You can retrieve other profile attributes with the [UserProfileFilter](../reference/UserProfileFilter.html), such as the email address or first and last names. The sample application expects the username in this example, so the route gets the username.

   * Signs on to the sample application with the username and password.

   * Returns the result to the browser.

   In production, remove `"capture": ["all"]` from the [PasswordReplayFilter](../reference/PasswordReplayFilter.html) to avoid recording credentials in the logs.

4. Restart PingGateway to read the secrets and load the new route.

   In the PingGateway output, make sure the route loaded successfully with no errors or warnings: `@system - Loaded the route with id '04-replay-aic' registered with the name '04-replay-aic'`.

You have successfully configured PingGateway to replay the password.

### Task 7: Create a test user in PingOne Advanced Identity Cloud

The sample application validates the credentials for password replay. It must recognize the username and password you use.

The sample application has built-in username-password combinations. The username and password credentials shown in the following steps are one of the built-in pairs.

1. In your browser's privacy or incognito mode, go to the default login journey for the realm you're using.

   For example, `https://myTenant.forgeblocks.com/am/XUI/?realm=/alpha#/`.

2. Click the Create an account link and enter the following settings in the Sign Up page:

   | Field                      | Value                                                                                  |
   | -------------------------- | -------------------------------------------------------------------------------------- |
   | Username                   | `wolkig`                                                                               |
   | First name                 | `Wilhelm`                                                                              |
   | Last name                  | `Wolkig`                                                                               |
   | Email Address              | Your email. PingOne Advanced Identity Cloud sends a confirmation mail to this address. |
   | Password                   | `Geh3imnis!`                                                                           |
   | Select a security question | `What's your favorite color?`                                                          |
   | Answer                     | `Red`                                                                                  |

3. Click Next to complete account creation and view the user profile.

4. Sign off.

You have successfully created a test user in PingOne Advanced Identity Cloud with credentials the sample application recognizes.

## Validation

1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/replay/>.

   PingGateway redirects to the PingOne Advanced Identity Cloud journey.

2. Sign on as user `wolkig` with password `Geh3imnis!`.

   PingGateway successfully replays the credentials against the sample application. The sample application displays its user profile page:

   ![Successful password replay](_images/password-replay-success.png)

3. Review the PingGateway output.

   On success, the output displays the credentials and the profile page:

   ```none
   ...INFO  o.f.o.d.c.C.c.PasswordReplayFilter-1 @04-replay-aic -

   [CONTINUED]--- (filtered-request) exchangeId:<id> - transactionId:<id> --->

   [CONTINUED]POST https://app.example.com:8444/login HTTP/1.1
   ...

   [CONTINUED]password=Geh3imnis%21&username=wolkig

   ...INFO  o.f.o.d.c.C.c.PasswordReplayFilter-1 @04-replay-aic -

   [CONTINUED]<--- (response) exchangeId:<id> - transactionId:<id> ---

   [CONTINUED]HTTP/1.1 200 OK
   ...

   [CONTINUED]<!DOCTYPE html>
   ...
   ```

You have successfully demonstrated password replay with PingGateway and PingOne Advanced Identity Cloud.

If password replay fails, consider the outcome of the HTTP POST from PingGateway to the sample application:

* HTTP 401 Unauthorized

  PingGateway isn't replaying the credentials.

  Review the PingGateway output to determine whether the username or password is missing when PingGateway replays the credentials.

  If the password is missing, make sure PingGateway and PingOne Advanced Identity Cloud share the same AES secret key.

* HTTP 403 Forbidden

  PingGateway isn't replaying the right credentials.

  Make sure you're using a username-password combination known to the sample application.

---

---
title: PingGateway and PingOne Advanced Identity Cloud
description: How PingGateway integrates with PingOne Advanced Identity Cloud to enable SSO and API security for business applications and APIs
component: pinggateway
version: 2026
page_id: pinggateway:aic:about
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/about.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Single sign-on (SSO)", "Security", "Authenticate"]
page_aliases: ["identity-cloud-guide:about.adoc"]
---

# PingGateway and PingOne Advanced Identity Cloud

PingOne Advanced Identity Cloud simplifies the consumption of the identity platform. Meanwhile, many organizations have business web applications and APIs deployed across multiple clouds or on-premise.

PingGateway facilitates non-intrusive integration of your web applications and APIs with PingOne Advanced Identity Cloud for SSO and API security. The following image illustrates how PingGateway bridges your business to PingOne Advanced Identity Cloud:

![The gateway bridges business applications and APIs to the cloud.](_images/gateway-aic.png)

Learn more in the [PingOne Advanced Identity Cloud documentation](https://docs.pingidentity.com/pingoneaic/home.html).

---

---
title: PingGateway and PingOne Advanced Identity Cloud
description: Integrate PingGateway with PingOne Advanced Identity Cloud for SSO and API security. Covers example setup, agent authentication, registration, and demo users.
component: pinggateway
version: 2026
page_id: pinggateway:aic:preface
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/preface.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Single sign-on (SSO)", "Security", "URI", "Authenticate", "Agents", "Journeys", "Nodes &amp; Trees"]
page_aliases: ["aic:index.adoc", "identity-cloud-guide:index.adoc", "identity-cloud-guide:preface.adoc"]
section_ids:
  preface-examples: Example installation
  authenticate-agent-idc: About authentication to PingOne Advanced Identity Cloud
  register-agent-idc: Register a PingGateway agent in PingOne Advanced Identity Cloud
  idc-use-the-secret-store-for-the-password: Use an ESV for the password
  optional_settings: Optional settings
  setup-user-idc: Set up a demo user in PingOne Advanced Identity Cloud
  idc-recommendations: Recommendations
---

# PingGateway and PingOne Advanced Identity Cloud

These pages show how to use PingGateway with PingOne Advanced Identity Cloud for single sign-on and API security. They're for PingOne Advanced Identity Cloud evaluators, administrators, and architects.

## Example installation

Unless otherwise stated, the examples with PingOne Advanced Identity Cloud assume the following installation:

* PingGateway listening at `http://ig.example.com:8080`.

  Learn more in [Installing PingGateway](../installation-guide/preface.html).

* The sample application listening at `https://app.example.com:8444` with PingGateway trusting it for HTTPS and ready to serve static resources.

  Learn more in [Using the sample application](../getting-started/start-sampleapp.html).

* A PingOne Advanced Identity Cloud tenant with the default configuration.

  Learn more in the [PingOne Advanced Identity Cloud documentation](https://docs.pingidentity.com/pingoneaic/home.html).

When using PingOne Advanced Identity Cloud, you need to know the value of the following properties:

* The root URL of your PingOne Advanced Identity Cloud tenant. For example, `https://myTenant.forgeblocks.com`.

  The URL of the PingAM component of PingOne Advanced Identity Cloud is the PingOne Advanced Identity Cloud tenant root URL followed by `/am`. For example, `https://myTenant.forgeblocks.com/am`.

* The realm where you work. The examples in this document use `alpha`.

  Prefix each realm in the hierarchy with the `realms` keyword. For example, `/realms/root/realms/alpha`.

If you use a different configuration, substitute in the procedures accordingly.

## About authentication to PingOne Advanced Identity Cloud

PingOne Advanced Identity Cloud provides an authentication journey to validate the agent credentials with an Agent Data Store Decision node.

When you register PingGateway with PingOne Advanced Identity Cloud, PingOne Advanced Identity Cloud uses the journey to authenticate PingGateway.

## Register a PingGateway agent in PingOne Advanced Identity Cloud

This procedure registers an agent profile for PingGateway.

1. Sign on to the Advanced Identity Cloud admin UI as an administrator.

2. Click [icon: verified_user, set=material, size=inline] Gateways & Agents > [icon: plus, set=fa]New Gateway/Agent > Identity Gateway > Next and use the hints in the following table to create the agent profile:

   | Field                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Example                                                                                                    |
   | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
   | ID                            | Set the unique agent profile name PingGateway uses to connect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `ig_agent`                                                                                                 |
   | Password                      | Store the password PingGateway uses to connect in the agent profile.Record the password to use when configuring PingGateway.                                                                                                                                                                                                                                                                                                                                                                                                                                   | A strong password.The examples in the documentation use `password` and its base64-encoding `cGFzc3dvcmQ=`. |
   | Use Secret Store for password | Optionally store the password in a secret and reference the secret by its label.After you create an agent profile with this option enabled, make sure you follow the steps in [Use an ESV for the password](#idc-use-the-secret-store-for-the-password).                                                                                                                                                                                                                                                                                                       | Click to enable                                                                                            |
   | Secret Label Identifier       | This field appears when you select Use Secret Store for password.This value represents the `identifier` part of the secret label for the agent. PingOne Advanced Identity Cloud uses the identifier to generate a secret label in the following format: `am.application.agents.identifier.secret`. Learn more in [Secret labels](https://docs.pingidentity.com/pingoneaic/tenants/esvs-signing-encryption.html#secret-labels).After setting this, make sure you follow the steps in [Use an ESV for the password](#idc-use-the-secret-store-for-the-password). | `ig`                                                                                                       |

   |   |                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------- |
   |   | Use secure passwords in a production environment. Consider using a password manager to generate secure passwords. |

3. Click Save Profile > Done to display the new agent profile.

4. (Optional) Add the list of Redirect URLs used in PingGateway routes and click Save to update the profile.

5. Switch to the AM admin UI, go to Applications > Agents > Identity Gateway > *agent ID*, and update the Login URL Template for CDSSO.

   Advanced Identity Cloud doesn't set a default. Configure this property to ensure Advanced Identity Cloud notifies PingGateway on authentication failure. PingGateway uses the notification to remove stale session data.

   * When using the default Advanced Identity Cloud login pages, add the following template all one line, replacing \<tenantHostname> to match your deployment:

     ```none
     https://<tenantHostname>/am/login?
     <#if service??>&service=${service}</#if>
     &goto=${goto}
     &gotoOnFail=${gotoOnFail}
     <#if acrValues??>&acr_values=${acrValues}</#if>
     <#if realm??>&realm=${realm}</#if>
     <#if module??>&module=${module}</#if>
     <#if locale??>&locale=${locale}</#if>
     ```

   * When using a custom login page outside Advanced Identity Cloud, use a template matching the login page requirements.

     Make sure to include a `${gotoOnFail}` parameter in the template. Update the custom login page to use the new parameter, verify its value is valid to protect against open redirect attacks, and redirect the user-agent when authentication fails.

### Use an ESV for the password

When you select Use Secret Store for password and set a secret label for the agent profile, PingOne Advanced Identity Cloud creates the secret label. You must create an ESV secret for the password and map the ESV to the label:

1. Use the Advanced Identity Cloud admin UI to define an ESV secret, such as `esv-ig-agent`, holding the password for PingGateway to connect.

   The examples in the documentation use `password`.

   Learn how in the PingOne Advanced Identity Cloud documentation on [creating ESV secrets](https://docs.pingidentity.com/pingoneaic/tenants/esvs-manage-ui.html#create_secrets). In production deployments, [restrict access to the password](https://docs.pingidentity.com/pingoneaic/tenants/esvs.html#control-access-to-secrets) from configuration placeholder and script contexts.

2. Use the AM admin UI to map the ESV to the label created when you set the Secret Label Identifier:

   1. Click [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management > Secret Stores > ESV > Mappings > [icon: plus, set=fa]Add mappings.

   2. In the Add Mapping modal, select the label, such as `am.application.agents.ig.secret`, in the Secret Label list.

   3. In the aliases field, enter the ESV secret, such as `esv-ig-agent`, and click Add:

      ![agent password mapping](_images/agent-password-mapping.png)

   4. Click Create to add the mapping.

   Learn more in the Advanced Identity Cloud documentation on [mapping ESV secrets to secret labels](https://docs.pingidentity.com/pingoneaic/tenants/esvs-signing-encryption.html#map-esv-secrets-to-secret-labels).

Note the following points:

* If you update or delete the Secret Label Identifier, AM updates or deletes the corresponding mapping for the previous identifier unless another agent shares the mapping.

* When you rotate a secret, update the corresponding mapping.

### Optional settings

In the AM admin UI, consider the following additional optional settings for the agent profile under Applications > Agents > Identity Gateway > *agent ID*:

1. To apply a different introspection scope, click Token Introspection and select a scope from the list.

2. Click Save to update the profile.

## Set up a demo user in PingOne Advanced Identity Cloud

This procedure sets up a demo user in the alpha realm.

1. Log in to the Advanced Identity Cloud admin UI as an administrator.

2. Go to [icon: group, set=material, size=inline] Identities > Manage > [icon: settings_system_daydream, set=material, size=inline] Alpha realm - Users, and add a user with the following values:

   * Username: `demo`

   * First name: `demo`

   * Last name: `user`

   * Email Address: `demo@example.com`

   * Password: `Ch4ng3!t`

## Recommendations

Use PingGateway with PingOne Advanced Identity Cloud as you would with any other service.

* During updates, individual PingOne Advanced Identity Cloud tenant servers go offline temporarily. PingGateway can receive HTTP 502 Bad Gateway responses for some requests during the update.

  In your [ClientHandler](../reference/ClientHandler.html) and [ReverseProxyHandler](../reference/ReverseProxyHandler.html) configurations, configure PingGateway to retry operations when this occurs:

  ```json
  "retries": {
      "enabled": true,
      "condition": "${response.status.code == 502}"
  }
  ```

* Update PingGateway to use the latest version you can to benefit from fixes and improvements.

---

---
title: PingOne Advanced Identity Cloud cross-domain single sign-on
description: Configure cross-domain single sign-on (CDSSO) using PingOne Advanced Identity Cloud as the authentication server for PingGateway
component: pinggateway
version: 2026
page_id: pinggateway:aic:cdsso
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/cdsso.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-19T12:00:00Z
keywords: ["Single sign-on (SSO)", "Security", "Authenticate", "OAuth 2.0", "OpenID Connect (OIDC)", "Cross Domain SSO (CDSSO)"]
page_aliases: ["identity-cloud-guide:cdsso.adoc"]
---

# PingOne Advanced Identity Cloud cross-domain single sign-on

For organizations relying on AM's session and policy services with SSO, consider Cross-Domain Single Sign-On (CDSSO) as an alternative to SSO through OpenID Connect.

This example sets up PingOne Advanced Identity Cloud as an SSO authentication server for requests processed by PingGateway. Learn about PingGateway and CDSSO in [Cross-domain single sign-on for PingAM](../gateway-guide/cdsso.html).

Before you start, prepare PingOne Advanced Identity Cloud, PingGateway, and the sample application as described in [Example installation for this guide](preface.html#preface-examples).

1. Set up PingOne Advanced Identity Cloud:

   1. Log in to the Advanced Identity Cloud admin UI as an administrator.

   2. Make sure you are managing the `alpha` realm. If not, click the current realm at the top of the screen, and switch realm.

   3. Go to [icon: group, set=material, size=inline] Identities > Manage > [icon: settings_system_daydream, set=material, size=inline] Alpha realm - Users, and add a user with the following values:

      * Username: `demo`

      * First name: `demo`

      * Last name: `user`

      * Email Address: `demo@example.com`

      * Password: `Ch4ng3!t`

   4. Register a PingGateway agent with the following values, as described in [Register a PingGateway agent in PingOne Advanced Identity Cloud](preface.html#register-agent-idc):

      * ID: `ig_agent`

      * Password: `password`

      * Redirect URLs: `https://ig.ext.com:8443/home/cdsso/redirect`

   5. Add a Validation Service:

      1. In PingOne Advanced Identity Cloud, select [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management. The AM admin UI is displayed.

      2. Select Services, and add a validation service with the following Valid goto URL Resources:

         * `https://ig.ext.com:8443/*`

         * `https://ig.ext.com:8443/*?*`

2. Set up PingGateway:

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Make sure PingGateway connects to the sample application over HTTPS with a route to access static resources.

      Learn more in [Using the sample application](../getting-started/start-sampleapp.html).

   3. Add the following `session` configuration to `admin.json`.

      This ensures the browser passes the session cookie in the form-POST to the redirect endpoint (step 6 of [Information flow during CDSSO](../gateway-guide/cdsso.html#figure-cdsso-auth)):

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

   5. Add the following route to PingGateway and correct the value for the property `amInstanceUrl`:

      * Linux

        `$HOME/.openig/config/routes/cdsso-idc.json`

      * Windows

        `%appdata%\OpenIG\config\routes\cdsso-idc.json`

      ```json
      {
        "name": "cdsso-idc",
        "baseURI": "https://app.example.com:8444",
        "condition": "${find(request.uri.path, '^/home/cdsso')}",
        "properties": {
          "amInstanceUrl": "https://myTenant.forgeblocks.com/am"
        },
        "heap": [
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          },
          {
            "name": "AmService-1",
            "type": "AmService",
            "config": {
              "url": "&{amInstanceUrl}",
              "realm": "/alpha",
              "agent": {
                "username": "ig_agent",
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

      Source: [cdsso-idc.json](../_attachments/config/routes/cdsso-idc.json)

      Notice the following features of the route where PingAM is running locally:

      * The AmService `URL` points to PingAM in PingOne Advanced Identity Cloud.

      * The AmService `realm` points to the realm where you configure your PingGateway agent.

   6. Restart PingGateway.

3. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.ext.com:8443/home/cdsso> and accept the server certificate.

      The PingOne Advanced Identity Cloud login page is displayed.

   2. Sign on to PingOne Advanced Identity Cloud as user `demo`, password `Ch4ng3!t`.

      PingAM calls `/home/cdsso/redirect` and includes the CDSSO token. The CrossDomainSingleSignOnFilter passes the request to the sample application.

---

---
title: PingOne Advanced Identity Cloud Proxy Connect
description: Configure PingGateway to use PingOne Advanced Identity Cloud Proxy Connect by decorating API requests with a security header for OAuth 2.0 token introspection
component: pinggateway
version: 2026
page_id: pinggateway:aic:proxy-connect
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/proxy-connect.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Security", "OAuth 2.0"]
page_aliases: ["identity-cloud-guide:proxy-connect.adoc"]
section_ids:
  goals: Goals
  prerequisites: Prerequisites
  tasks: Tasks
  task_1_configure_an_oauth_2_0_profile: "Task 1: Configure an OAuth 2.0 profile"
  proxy-connect-gateway: "Task 2: Configure PingGateway"
  proxy-connect-pre-validation: "Task 3: Pre-validation"
  proxy-connect-security-header: "Task 4: Set a Proxy Connect rule"
  validation: Validation
---

# PingOne Advanced Identity Cloud Proxy Connect

With [Proxy Connect](https://docs.pingidentity.com/pingoneaic/tenants/proxy-connect.html), PingOne Advanced Identity Cloud provides a way to secure traffic to your tenant environments in seamless compliance with the security controls you apply to your company's other network resources.

You use Proxy Connect rules to restrict access to a PingOne Advanced Identity Cloud tenant environment based on an IP address range or a required security header. If the request matches any of the rules, Proxy Connect lets the request through. If not, PingOne Advanced Identity Cloud responds with HTTP 404 Not Found. This affects the PingOne Advanced Identity Cloud UIs, too, as Proxy Connect prevents browser requests that don't follow the rules.

For externally facing applications, Proxy Connect works well with a web application firewall (WAF). A WAF protects against distributed denial-of-service, cross-site scripting, and injection attacks. The WAF isn't application-specific and so doesn't make application-specific decisions.

Requests from PingGateway can go through the WAF, but they don't always need to.

*When PingGateway redirects the browser to an end-user UI page, such as the sign-on page, target the WAF.* There's nothing special to do in PingGateway other than redirect to the WAF instead of the tenant. This includes the following use cases, where you let the WAF add the required security header to the browser and PingGateway requests:

* SSO and CDSSO

* SAML v2.0

* OpenID Connect

* Step-up and transactional authorization where a policy can return advices

*When PingGateway uses PingOne Advanced Identity Cloud APIs directly without redirecting the browser, you can skip the WAF.* This includes headless interactions that involve direct REST requests, not redirects, where you let PingGateway decorate requests with the required security header:

* PingGateway as an OAuth 2.0 resource server

* Using a [SessionInfoFilter](../reference/SessionInfoFilter.html)

* Using a [PolicyEnforcementFilter](../reference/PolicyEnforcementFilter.html) in an SDK-based client application

* Using a [UserProfileFilter](../reference/UserProfileFilter.html)

## Goals

The following example builds on the [OAuth 2.0 and PingOne Advanced Identity Cloud](oauthrs.html) use case.

It shows how to decorate requests to PingOne Advanced Identity Cloud with a security header for Proxy Connect.

## Prerequisites

* Get access as an administrator to a PingOne Advanced Identity Cloud tenant with the Proxy Connect add-on feature.

  Wait to add Proxy Connect rules until you have [added a route to PingGateway](#proxy-connect-gateway) and [verified the route works without restrictions](#proxy-connect-pre-validation).

* Complete the [example installation](preface.html#preface-examples) steps to use PingGateway with PingOne Advanced Identity Cloud.

  You don't need the sample application for this example.

## Tasks

### Task 1: Configure an OAuth 2.0 profile

Configure an OAuth 2.0 client profile for PingGateway as a resource server:

1. Sign on to the Advanced Identity Cloud admin UI as an administrator.

2. Go to Applications > + Custom Application > OIDC - OpenId Connect > Web and add a web application with the following settings:

   * Name

     `oauth2-client`

   * Owners

     `demo user`

   * Client Secret

     `password`

   * Sign On > Grant Types

     Add `Resource Owner Password Credentials`

   * Sign On > Scopes

     Add `mail`

### Task 2: Configure PingGateway

1. [Configure PingGateway for HTTPS](../installation-guide/securing-connections.html#server-side-tls).

2. Set an environment variable for the base64-encoded PingGateway agent password.

   The following command sets the variable to a base64-encoding of the string `password`.

   ```console
   $ export AGENT_SECRET_ID='cGFzc3dvcmQ='
   ```

   A `SystemAndEnvSecretStore` in the route that follows reads the base64-encoded password.

3. Restart PingGateway to reload `admin.json` and access the agent password.

4. Add a route for token introspection that decorates requests with the security header.

   * Linux

     `$HOME/.openig/config/routes/proxy-connect.json`

   * Windows

     `%appdata%\OpenIG\config\routes\proxy-connect.json`

   > **Collapse: Show route**
   >
   > ```json
   > {
   >   "name": "proxy-connect",
   >   "condition": "${find(request.uri.path, '^/proxy-connect')}",
   >   "properties": {
   >     "gatewayUsername": "ig_agent",
   >     "gatewayPasswordSecretId": "agent.secret.id",
   >     "amServiceUrl": "https://myTenant.forgeblocks.com/am"
   >   },
   >   "heap": [
   >     {
   >       "name": "SystemAndEnvSecretStore-1",
   >       "type": "SystemAndEnvSecretStore"
   >     },
   >     {
   >       "name": "SecurityHeaderFilter",
   >       "type": "HeaderFilter",
   >       "config": {
   >         "messageType": "REQUEST",
   >         "add": {
   >           "X-Security-Header": [
   >             "f1drybngmzqj5loposddd5p98z886jp9"
   >           ]
   >         },
   >         "_comment": "The Proxy Connect rule you configure matches this header."
   >       },
   >       "capture": "filtered_request"
   >     },
   >     {
   >       "name": "AmService-1",
   >       "type": "AmService",
   >       "config": {
   >         "url": "&{amServiceUrl}",
   >         "realm": "/alpha",
   >         "agent": {
   >           "username": "&{gatewayUsername}",
   >           "passwordSecretId": "&{gatewayPasswordSecretId}"
   >         },
   >         "secretsProvider": "SystemAndEnvSecretStore-1",
   >         "amHandler": {
   >           "type": "Chain",
   >           "config": {
   >             "filters": [
   >               "SecurityHeaderFilter"
   >             ],
   >             "handler": "ForgeRockClientHandler"
   >           }
   >         },
   >         "notifications": {
   >           "_comment": "Avoid UpgradeRejectedException: WebSocket upgrade failure: 404",
   >           "enabled": false
   >         }
   >       }
   >     }
   >   ],
   >   "handler": {
   >     "type": "Chain",
   >     "config": {
   >       "filters": [
   >         {
   >           "name": "OAuth2ResourceServerFilter-1",
   >           "type": "OAuth2ResourceServerFilter",
   >           "config": {
   >             "scopes": [
   >               "mail"
   >             ],
   >             "requireHttps": false,
   >             "accessTokenResolver": {
   >               "name": "TokenIntrospectionAccessTokenResolver-1",
   >               "type": "TokenIntrospectionAccessTokenResolver",
   >               "config": {
   >                 "amService": "AmService-1",
   >                 "providerHandler": {
   >                   "type": "Chain",
   >                   "config": {
   >                     "filters": [
   >                       "SecurityHeaderFilter",
   >                       {
   >                         "type": "HttpBasicAuthenticationClientFilter",
   >                         "config": {
   >                           "username": "&{gatewayUsername}",
   >                           "passwordSecretId": "&{gatewayPasswordSecretId}",
   >                           "secretsProvider": "SystemAndEnvSecretStore-1"
   >                         }
   >                       }
   >                     ],
   >                     "handler": "ForgeRockClientHandler"
   >                   }
   >                 }
   >               }
   >             }
   >           }
   >         }
   >       ],
   >       "handler": {
   >         "type": "StaticResponseHandler",
   >         "config": {
   >           "status": 200,
   >           "headers": {
   >             "Content-Type": [
   >               "text/html; charset=UTF-8"
   >             ]
   >           },
   >           "entity": "<html><body><h2>Decoded access_token: ${contexts.oauth2.accessToken.info}</h2></body></html>"
   >         }
   >       }
   >     }
   >   }
   > }
   > ```

   Source: [proxy-connect.json](../_attachments/config/routes/proxy-connect.json).

   The Proxy Connect route:

   * Matches requests whose path starts with `proxy-connect`.

   * Defines a [HeaderFilter](../reference/HeaderFilter.html) to add the security header.

     The header name and value must match the Proxy Connect header rule you configure. This route uses `f1drybngmzqj5loposddd5p98z886jp9` to match the header rule set in [Task 4: Set a Proxy Connect rule](#proxy-connect-security-header).

   * Configures an [AmService](../reference/AmService.html) whose requests PingGateway decorates with the security header.

     As the service can't decorate websocket requests for notifications, the configuration disables notifications.

   * Uses a [OAuth2ResourceServerFilter](../reference/OAuth2ResourceServerFilter.html) with a [TokenIntrospectionAccessTokenResolver](../reference/TokenIntrospectionAccessTokenResolver.html) to introspect access tokens.

   * Adds a [StaticResponseHandler](../reference/StaticResponseHandler.html) to display the results of introspection.

5. Update the route's `amServiceUrl` setting to target the PingOne Advanced Identity Cloud tenant and save your work.

   PingGateway loads the route.

### Task 3: Pre-validation

Before you add Proxy Connect rules to restrict access, verify the route works *without* restrictions.

1. Get an access token using the resource owner password credentials flow:

   ```console
   $ export ACCESS_TOKEN=$(curl \
   --request POST 'https://myTenant.forgeblocks.com/am/oauth2/realms/alpha/access_token' \
   --user 'oauth2-client:password' \
   --data 'grant_type=password' \
   --data 'username=demo' \
   --data 'password=Ch4ng3!t' \
   --data 'scope=mail' \
   --silent | jq -r ".access_token")
   ```

   You don't need the security header until you configure a Proxy Connect header rule.

2. Use the route to introspect the access token:

   ```console
   $ curl \
   --request GET 'https://ig.example.com:8443/proxy-connect' \
   --insecure \
   --header "Authorization: Bearer ${ACCESS_TOKEN}"
   ```

   Output

   ```none
   <html><body><h2>Decoded access_token:
   {active=true,
   scope=mail,
   realm=/alpha,
   client_id=oauth2-client,
   user_id=<uuid>,
   username=<uuid>,
   token_type=Bearer,
   exp=<seconds>,
   sub=<uuid>,
   iss=https://myTenant.forgeblocks.com:443/am/oauth2/realms/root/realms/alpha,
   subname=<uuid>,
   auth_level=0,
   authGrantId=<id>,
   auditTrackingId=<uuid>,
   expires_in=<seconds>}</h2></body></html>
   ```

### Task 4: Set a Proxy Connect rule

Learn about this in the [Proxy Connect](https://docs.pingidentity.com/pingoneaic/tenants/proxy-connect-api.html) documentation. Once you understand the steps:

1. Configure a Proxy Connect rule to require the following security header, which is the same one set in the Proxy Connect route configuration:

   ```none
   'X-Security-Header: f1drybngmzqj5loposddd5p98z886jp9'
   ```

   When you first update the header rules, the change is pending (`"requestStatus": "PENDING"`). PingOne Advanced Identity Cloud doesn't check for the security header when the update is still pending.

2. Poll the Proxy Connection configuration in PingOne Advanced Identity Cloud until the request has `"requestStatus": "SUCCESS"`.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Once the request is successful, you can't use the Advanced Identity Cloud admin UI. Your browser doesn't add the security header by default.If you must use the Advanced Identity Cloud admin UI again, either reset the header rules to `{"enabled": false, "headers": []}` or [configure your browser to add the security header](https://docs.pingidentity.com/pingoneaic/tenants/proxy-connect-api.html#prerequisite-actions-for-accessing-a-tenant-when-rulesets-are-configured). |

## Validation

1. Get an access token using the resource owner password credentials flow:

   ```console
   $ export ACCESS_TOKEN=$(curl \
   --request POST 'https://myTenant.forgeblocks.com/am/oauth2/realms/alpha/access_token' \
   --user 'oauth2-client:password' \
   --data 'grant_type=password' \
   --data 'username=demo' \
   --data 'password=Ch4ng3!t' \
   --data 'scope=mail' \
   --header 'X-Security-Header: f1drybngmzqj5loposddd5p98z886jp9' \
   --silent | jq -r ".access_token")
   ```

2. Use the route to introspect the access token:

   ```console
   $ curl \
   --request GET 'https://ig.example.com:8443/proxy-connect' \
   --insecure \
   --header "Authorization: Bearer ${ACCESS_TOKEN}"
   ```

   Output

   ```none
   <html><body><h2>Decoded access_token:
   {active=true,
   scope=mail,
   realm=/alpha,
   client_id=oauth2-client,
   user_id=<uuid>,
   username=<uuid>,
   token_type=Bearer,
   exp=<seconds>,
   sub=<uuid>,
   iss=https://myTenant.forgeblocks.com:443/am/oauth2/realms/root/realms/alpha,
   subname=<uuid>,
   auth_level=0,
   authGrantId=<id>,
   auditTrackingId=<uuid>,
   expires_in=<seconds>}</h2></body></html>
   ```

3. In the PingGateway log, notice the filtered requests have the security header:

   ```none
   [CONTINUED]--- (filtered-request) exchangeId:<uuid> - transactionId:<uuid> --->

   [CONTINUED]POST https://myTenant.forgeblocks.com/am/oauth2/realms/root/realms/alpha/introspect HTTP/1.1
   [CONTINUED]Accept: application/json
   [CONTINUED]Content-Length: 918
   [CONTINUED]Content-Type: application/x-www-form-urlencoded
   [CONTINUED]X-Security-Header: f1drybngmzqj5loposddd5p98z886jp9

   [CONTINUED]token=<token>&token_type_hint=access_token
   ```

   Change `"capture"` to `"_capture"` in the Proxy Connect route to avoid flooding the PingGateway logs.

You've successfully shown how to use PingGateway with Proxy Connect.

---

---
title: Policy enforcement and PingOne Advanced Identity Cloud
description: Configure PingGateway to request and enforce policy decisions from PingOne Advanced Identity Cloud, including step-up authorization for transactions
component: pinggateway
version: 2026
page_id: pinggateway:aic:pep
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/pep.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Single sign-on (SSO)", "Security", "Authorization", "Policy"]
page_aliases: ["identity-cloud-guide:pep.adoc"]
section_ids:
  pep-cdsso: Enforce a simple policy
  stepup-session: Step up authorization for a transaction
---

# Policy enforcement and PingOne Advanced Identity Cloud

The following procedure gives an example of how to request and enforce policy decisions from PingOne Advanced Identity Cloud.

## Enforce a simple policy

Before you start, set up and test the example in [Cross-domain single sign-on](cdsso.html).

1. Set up PingOne Advanced Identity Cloud:

   1. In the Advanced Identity Cloud admin UI, select [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management to open the AM admin UI.

   2. Select [icon: key, set=fa]Authorization > Policy Sets > New Policy Set, and add a policy set with the following values:

      * Id : `PEP-CDSSO`

      * Resource Types : `URL`

   3. In the new policy set, add a policy with the following values:

      * Name : `CDSSO`

      * Resource Type : `URL`

      * Resource pattern : `*://*:*/*`

      * Resource value : `https://app.example.com:8444/home/cdsso`

        This policy protects the home page of the sample application.

   4. On the Actions tab, add an action to allow HTTP `GET`.

   5. On the Subjects tab, remove any default subject conditions, add a subject condition for all `Authenticated Users`.

2. Set up PingGateway:

   1. Replace `cdsso-idc.json` with the following route and correct the value for the property `amInstanceUrl`:

      * Linux

        `$HOME/.openig/config/routes/pep-cdsso-idc.json`

      * Windows

        `%appdata%\OpenIG\config\routes\pep-cdsso-idc.json`

      ```json
      {
        "name": "pep-cdsso-idc",
        "baseURI": "https://app.example.com:8444",
        "condition": "${find(request.uri.path, '^/home/cdsso')}",
        "properties": {
          "amInstanceUrl": "https://myTenant.forgeblocks.com/am"
        },
        "heap": [
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          },
          {
            "name": "AmService-1",
            "type": "AmService",
            "config": {
              "url": "&{amInstanceUrl}",
              "realm": "/alpha",
              "agent": {
                "username": "ig_agent",
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

      Source: [pep-cdsso-idc.json](../_attachments/config/routes/pep-cdsso-idc.json)

      Notice that compared to `cdsso-idc.json` the CrossDomainSingleSignOnFilter is followed by a PolicyEnforcementFilter to enforce the policy `PEP-CDSSO`.

3. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.ext.com:8443/home/cdsso> and accept the server certificate.

      PingGateway redirects you to PingOne Advanced Identity Cloud for authentication.

   2. Sign on to PingOne Advanced Identity Cloud as user `demo`, password `Ch4ng3!t`.

      PingOne Advanced Identity Cloud redirects you back to the request URL, and PingGateway requests a policy decision. PingOne Advanced Identity Cloud returns a policy decision that grants access to the sample application.

## Step up authorization for a transaction

Before you begin, set up and test the example in [Enforce a simple policy](#pep-cdsso).

1. In the Advanced Identity Cloud admin UI, select [icon: code, set=material, size=inline] Scripts > Auth Scripts > New Script > Journey Decision Node > Next, and add a default Journey Decision Node Script called `TxTestPassword`:

   ```javascript
   /*
     - Data made available by nodes that have already executed are available in the sharedState variable.
     - The script should set outcome to either "true" or "false".
    */

   var givenPassword = nodeState.get("password").asString()

   if (givenPassword.equals("7890")) {
     outcome = "true"
   } else {
     outcome = "false"
   }
   ```

   Source: [TxTestPassword.js](../_attachments/scripts/TxTestPassword.js)

2. Configure a journey:

   1. Click [icon: account_tree, set=material, size=inline] Journeys and add a journey with the following configuration:

      * Name: `Tx01_Tree`

      * Identity Object: `Alpha realm users`

        The browser displays the journey canvas.

   2. In Nodes > Basic Authentication, drag a Password Collector node onto the canvas.

   3. In Nodes > Utilities, drag a Scripted decision node onto the canvas.

   4. Configure the scripted decision node as follows:

      * Script: select `TxTestPassword`

      * Outcomes: enter `true` and `false`

   5. Connect the nodes as shown:

      ![Authentication journey](_images/auth.jpg)

      Learn about configuring journeys in the [PingOne Advanced Identity Cloud Docs](https://docs.pingidentity.com/pingoneaic/home.html)

3. Edit the authorization policy:

   1. In the Advanced Identity Cloud admin UI, select [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management to open the AM admin UI.

   2. Select [icon: key, set=fa]Authorization > Policy Sets > PEP-CDSSO and add the following environment condition to the `CDSSO` policy:

      * `All of`

      * Type: `Transaction`

      * Script name: `Authenticate to tree`

      * Strategy Specifier: `Tx01_Tree`

4. Test the setup:

   1. In a browser, go to <https://ig.ext.com:8443/home/cdsso> and accept the server certificate.

      If you haven't previously authenticated to PingOne Advanced Identity Cloud, the CrossDomainSingleSignOnFilter redirects the request to PingOne Advanced Identity Cloud for authentication.

   2. Sign on to PingOne Advanced Identity Cloud as user `demo`, password `Ch4ng3!t`.

   3. Enter the password `7890` required by the script `TxTestPassword`.

      PingOne Advanced Identity Cloud redirects you back to the request URL and PingGateway requests a policy decision. PingOne Advanced Identity Cloud returns a policy decision based on the authentication journey.

---

---
title: Securing the OAuth 2.0 access token endpoint with PingOne Advanced Identity Cloud
description: Configure PingGateway to transform OAuth 2.0 grant-type requests into secure JWT bearer grants and propagate them to PingOne Advanced Identity Cloud
component: pinggateway
version: 2026
page_id: pinggateway:aic:grant-swap
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/grant-swap.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-15
keywords: ["Grant swap", "OAuth 2.0"]
page_aliases: ["identity-cloud-guide:grant-swap.adoc"]
---

# Securing the OAuth 2.0 access token endpoint with PingOne Advanced Identity Cloud

This page uses a [GrantSwapJwtAssertionOAuth2ClientFilter](../reference/GrantSwapJwtAssertionOAuth2ClientFilter.html) to transform requests for OAuth 2.0 access tokens into secure [JWT bearer grant type](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-jwt-bearer-grant.html) requests. It propagates the transformed requests to PingOne Advanced Identity Cloud to obtain an access token.

Use GrantSwapJwtAssertionOAuth2ClientFilter to increase the security of less-secure grant-type requests, such as [Client credentials grant](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-client-cred-grant.html) requests or [Resource owner password credentials grant](https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-ropc-grant.html) requests.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The GrantSwapJwtAssertionOAuth2ClientFilter obtains access tokens from the `/oauth2/access_token` endpoint. To prevent unwanted or malicious access to the endpoint, make sure only a well-defined set of clients can use this filter.Consider the following options to secure access to the GrantSwapJwtAssertionOAuth2ClientFilter:- Deploy PingGateway on a trusted network.

- Use mutual TLS (mTLS) and X.509 certificates for authentication between clients and PingGateway. For more information, refer to [OAuth 2.0 Mutual TLS Client Authentication and Certificate Bound Access Tokens](https://tools.ietf.org/html/draft-ietf-oauth-mtls).

- Configure an [AllowOnlyFilter](../reference/AllowOnlyFilter.html) in front of the GrantSwapJwtAssertionOAuth2ClientFilter to control access within a route.

- Define restrictive [Route](../reference/Route.html) conditions to allow access only for expected grant-type requests. For example, define a route condition that requires a specific client ID, grant-type, or scope.

- Configure a [ScriptableFilter](../reference/ScriptableFilter.html) in front of the GrantSwapJwtAssertionOAuth2ClientFilter to validate requests. |

The following figure shows the flow of information for a grant swap:

![GrantSwapJwtAssertionOAuth2ClientFilter](_images/GrantSwapJwtAssertionOAuth2ClientFilter.svg)

Before you start, prepare PingOne Advanced Identity Cloud, PingGateway, and the sample application as described in [Example installation for this guide](preface.html#preface-examples).

1. Set up PingOne Advanced Identity Cloud:

   1. Log in to the Advanced Identity Cloud admin UI as an administrator.

   2. Create a service account with the following values, as described in [Create a new service account](https://docs.pingidentity.com/pingoneaic/tenants/service-accounts.html#create_a_new_service_account):

      * Name: `myServiceAccount`

      * Scopes: `fr:idm:* All Identity Management APIs`

        The service account ID is displayed and you are prompted to download the private key. The public key is held in PingOne Advanced Identity Cloud.

        For more information, refer to [Service accounts](https://docs.pingidentity.com/pingoneaic/tenants/service-accounts.html).

   3. Make a note of the service account ID and download the private key to your secrets directory.

   4. Rename the key to match the regex format `(\.[a-zA-Z0-9])*`. For example, rename `myServiceAccount_privateKey.jwk` to `privateKey.jwk`.

2. Set up PingGateway:

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Add the following route to PingGateway:

      * Linux

        `$HOME/.openig/config/routes/grant-swap.json`

      * Windows

        `%appdata%\OpenIG\config\routes\grant-swap.json`

      ```json
      {
        "name" : "grant-swap",
        "properties": {
          "idcInstanceUrl": "https://myTenant.forgeblocks.com",
          "issuer": "service-account-id",
          "secretsDir": "path-to-secrets",
          "privateKeyFilename": "privateKey.jwk"
        },
        "condition" : "#{find(request.uri.path, '^/am/oauth2/access_token') && request.entity.form['grant_type'][0] == 'client_credentials'}",
        "baseURI" : "&{idcInstanceUrl}:443/",
        "heap" : [ {
          "name": "JwkPropertyFormat-01",
          "type": "JwkPropertyFormat"
        },
          {
            "name": "FileSystemSecretStore-01",
            "type": "FileSystemSecretStore",
            "config": {
              "format": "JwkPropertyFormat-01",
              "directory": "&{secretsDir}",
              "mappings": [ {
                "secretId": "&{privateKeyFilename}",
                "format": "JwkPropertyFormat-01"
              }
              ]
            }
          }
        ],
        "handler" : {
          "type" : "Chain",
          "capture" : "all",
          "config" : {
            "filters" : [
              {
                "name" : "GrantSwapJwtAssertionOAuth2ClientFilter-01",
                "description": "access /access_token endpoint with jwt-bearer-profile",
                "type" : "GrantSwapJwtAssertionOAuth2ClientFilter",
                "capture" : "all",
                "config" : {
                  "clientId" : "service-account",
                  "assertion" : {
                    "issuer" : "&{issuer}",
                    "audience" : "&{idcInstanceUrl}/am/oauth2/access_token",
                    "subject" : "&{issuer}",
                    "expiryTime": "2 minutes"
                  },
                  "signature": {
                    "secretId": "&{privateKeyFilename}",
                    "includeKeyId": false
                  },
                  "secretsProvider": "FileSystemSecretStore-01",
                  "scopes" : {
                    "type": "RequestFormResourceAccess"
                  }
                }
              }
            ],
            "handler" : "ForgeRockClientHandler"
          }
        }
      }
      ```

      Source: [grant-swap.json](../_attachments/config/routes/grant-swap.json)

   3. In the route, replace the values for the following properties with your values:

      * `idcInstanceUrl`: The root URL of your PingOne Advanced Identity Cloud tenant.

      * `issuer`: The ID of the service account created in PingOne Advanced Identity Cloud

      * `secretsDir`: The directory containing the downloaded private key

      * `privateKeyFilename`: The filename of the downloaded private key

   4. Notice the following features of the route:

      * The condition intercepts only `client_credentials` grant-type requests on the path `/am/oauth2/access_token`. A more secure condition can be set on the client ID.

      * Requests are rebased to the PingOne Advanced Identity Cloud URL.

      * A FileSystemSecretStore loads the private-key JWK used to sign the JWT.

      * The GrantSwapJwtAssertionOAuth2ClientFilter:

        * Requires the core JWT claims `issuer`, `subject`, `audience`, and `expiryTime`.

        * Uses RequestFormResourceAccess to extract scopes from the inbound request for inclusion in the JWT-assertion grant-type request propagated to AM.

        * Signs the JWT with the JWK provided by the service account.

      * The GrantSwapJwtAssertionOAuth2ClientFilter `clientId` refers to the OAuth 2.0 client ID created by AM. The value must be `service-account`.

   5. Add the following route to PingGateway to return a standard OAuth 2.0 error response if the request fails the route condition:

      * Linux

        `$HOME/.openig/config/routes/zz-returns-invalid-request.json`

      * Windows

        `%appdata%\OpenIG\config\routes\zz-returns-invalid-request.json`

      ```json
      {
        "name" : "zz-returns-invalid-request",
        "handler" : {
          "type" : "StaticResponseHandler",
          "capture" : "all",
          "config" : {
            "status": 400,
            "headers": {"Content-Type": ["application/json; charset=UTF-8"]},
            "entity": "{\"error\": \"Invalid_request\", \"error_description\": \"Invalid request\"}"
          }
        }
      }
      ```

      Source: [zz-returns-invalid-request.json](../_attachments/config/routes/zz-returns-invalid-request.json)

3. Test the setup by accessing the route with a `curl` command similar to this:

   ```console
   $ curl  \
       --cacert /path/to/secrets/ig.example.com-certificate.pem \
       --location \
       --request POST 'https://ig.example.com:8443/am/oauth2/access_token' \
       --header 'Content-Type: application/x-www-form-urlencoded' \
       --data-urlencode 'client_id=myServiceAccount' \
       --data-urlencode 'grant_type=client_credentials' \
       --data-urlencode 'scope=fr:idm:*'
   ```

   Output

   ```json
   {"access_token":"eyJ...","scope":"fr:idm:*","token_type":"Bearer","expires_in":899}
   ```

   The command makes a `client_credentials` grant-type request on the path `/am/oauth2/access_token`, supplying the client ID and scopes. PingGateway transforms the request into a JWT-assertion grant-type request and propagates it to PingOne Advanced Identity Cloud.

   Because the service account in PingOne Advanced Identity Cloud supports the requested scope, the GrantSwapJwtAssertionOAuth2ClientFilter returns an access token.

---

---
title: Windows desktop single sign-on for PingOne Advanced Identity Cloud
description: Configure Windows desktop SSO for PingOne Advanced Identity Cloud using PingGateway to validate Kerberos tickets without re-signing on
component: pinggateway
version: 2026
page_id: pinggateway:aic:wdsso
canonical_url: https://docs.pingidentity.com/pinggateway/2026/aic/wdsso.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-19T12:00:00Z
keywords: ["Single sign-on (SSO)", "Security", "Authenticate"]
section_ids:
  wdsso_authentication_flow: WDSSO authentication flow
  configuration_steps: Configuration steps
  learn_more: Learn more
---

# Windows desktop single sign-on for PingOne Advanced Identity Cloud

PingGateway helps you achieve Windows desktop single sign-on (WDSSO) for Advanced Identity Cloud PingGateway runs in the Windows domain and validates Kerberos tickets.

With WDSSO, after the end user signs on to their Windows desktop environment they authenticate to Advanced Identity Cloud without signing on again.

This page describes the flow and the high-level steps to set up WDSSO for Advanced Identity Cloud. It links to other pages in the Advanced Identity Cloud, PingGateway, and authentication node documentation for detailed implementation instructions.

## WDSSO authentication flow

The following sequence diagram illustrates Advanced Identity Cloud authentication with WDSSO. It assumes the end user signed on to their Windows desktop environment and the application they're using redirected them to the Advanced Identity Cloud identity assertion journey to authenticate.

This diagram omits optional steps like adding or updating claims in the JWTs or in the Kerberos request and response.

![Authentication flow when using WDSSO](_images/wdsso.svg)

The explanation of each step follows:

1. The Identity Assertion node in the journey redirects to the PingGateway identity assertion route.

   This route uses an `IdentityAssertionHandler` with a `KerberosIdentityAssertionPlugin` for WDSSO to validate and consume the identity request JWT.

2. The PingGateway identity assertion handler consumes the JWT and the `KerberosIdentityAssertionPlugin` in the route validates the Windows Kerberos ticket.

3. The Windows service responds to the request from PingGateway.

   If the response is HTTP 401 unauthorized, the plugin's unauthorized response handler can redirect the end user to sign on again.

4. The `KerberosIdentityAssertionPlugin` an encrypted identity assertion JWT with claims for the authentication response and returns this to the identity assertion journey.

   On successful authentication, the JWT includes the `principal` claim, which the Identity Assertion node maps to the shared node state `username` attribute by default.

   The journey continues processing the authentication response and finally redirects the end user back to the application.

## Configuration steps

Complete the following high-level configuration steps to set up WDSSO with Advanced Identity Cloud as the IdP:

1. In Advanced Identity Cloud, [create an encryption key ESV](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html#auth-node-identity-assertion-key) for the JWTs exchanged with PingGateway.

   Record the key value for use in the PingGateway configuration.

2. In Advanced Identity Cloud, use the AM admin UI to [configure an Identity Assertion service](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html#auth-node-identity-assertion-service) with PingGateway as the identity assertion server.

3. [Map the shared encryption key to a secret label](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html#auth-node-identity-assertion-secret-store) aligned with the Shared Encryption Secret of the Identity Assertion service you configured.

4. In Advanced Identity Cloud, [create an identity assertion journey with an Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html#configure_the_example_authentication_journey) configured to route requests to the PingGateway identity assertion route.

5. In PingGateway, set up the encryption key you created as an ESV in Advanced Identity Cloud as a [secret](../security-guide/keys.html) for use when encrypting and decrypting JWTs.

6. In PingGateway, configure [an identity assertion route to validate identity request JWTs](../reference/IdentityAssertionHandler.html#IdentityAssertionHandler-examples), interact with the Windows service, and return identity assertion JWTs.

   Use a [KerberosIdentityAssertionPlugin](../reference/KerberosIdentityAssertionPlugin.html) as the identity assertion plugin for the route.

After completing these steps, you have configured WDSSO with Advanced Identity Cloud as the IdP.

## Learn more

Find more information and detailed implementation instructions in the following documentation.

| Resource                                                                                                             | Describes how to configure                                                                                        |
| -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html) reference | Advanced Identity Cloud with an encryption key, an identity assertion service, and an identity assertion journey. |
| [IdentityAssertionHandler](../reference/IdentityAssertionHandler.html)                                               | An identity assertion route to process identity request and assertion JWTs.                                       |
| [KerberosIdentityAssertionPlugin](../reference/KerberosIdentityAssertionPlugin.html)                                 | An identity assertion plugin to interact with a Kerberos ticket service on Windows.                               |
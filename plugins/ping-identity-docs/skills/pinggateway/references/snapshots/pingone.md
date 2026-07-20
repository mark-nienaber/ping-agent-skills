---
title: PingGateway and PingOne
description: Use PingGateway with PingOne for SSO and API security, including environment setup and test user configuration
component: pinggateway
version: 2026
page_id: pinggateway:pingone:preface
canonical_url: https://docs.pingidentity.com/pinggateway/2026/pingone/preface.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Single sign-on (SSO)", "Security", "Authenticate"]
page_aliases: ["index.adoc"]
section_ids:
  before_you_start: Before you start
  ping-create-env: Create a PingOne environment
  ping-add-user: Add a PingOne test user
---

# PingGateway and PingOne

These pages show you how to use PingGateway with PingOne for SSO and API security. The examples target PingOne evaluators, administrators, and architects.

## Before you start

Unless otherwise stated, the examples in these pages assume you have:

* PingGateway [installed](../installation-guide/preface.html).

* The sample application [installed](../getting-started/start-sampleapp.html).

* A PingOne environment as described in [Create a PingOne environment](#ping-create-env).

* A PingOne test user as described in [Add a PingOne test user](#ping-add-user).

## Create a PingOne environment

In the PingOne console, create an environment with the following values:

* Select a solution for your Environment: Build your own solution

* Select solution(s) for your Environment: `PingOne SSO`

* ENVIRONMENT NAME: `My environment`

* DESCRIPTION: OIDC `My environment`

* ENVIRONMENT TYPE: `Sandbox`

Learn more in the PingOne documentation on [Adding an environment](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started_adding_environment.html).

## Add a PingOne test user

1. In the PingOne environment under Directory > Users, add a user.

   To match a user known to the sample application, use the following values:

   * Given Name: `Wilhelm`

   * Family Name: `Wolkig`

   * Username: `wolkig`

   * Email: `wolkig@example.com`

   * Password: Click Generate Password and record the generated password.

   Learn more in the PingOne documentation on [Adding a user](https://docs.pingidentity.com/pingone/directory/p1_adduser.html).

2. Under Settings > Environment Properties > URLs, copy the Self-Service Url for your environment.

3. In your browser's privacy or incognito mode, go to the URL you copied and sign on as the user you created.

4. When prompted, change the password so you won't have to change it again when trying an example.

   To match the credentials to those known to the sample application, set the new password to `Geh3imnis!`.

---

---
title: PingGateway with PingOne as a SAML IdP
description: Configure PingGateway to use PingOne as a SAML 2.0 identity provider with unsigned and unencrypted assertions
component: pinggateway
version: 2026
page_id: pinggateway:pingone:saml-ping-one
canonical_url: https://docs.pingidentity.com/pinggateway/2026/pingone/saml-ping-one.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Configuration", "SAML 2.0", "Federation"]
page_aliases: ["gateway-guide:saml-ping-one.adoc"]
section_ids:
  before_you_start: Before you start
  prepare_pingone: Prepare PingOne
  prepare_pinggateway: Prepare PingGateway
  validation: Validation
---

# PingGateway with PingOne as a SAML IdP

This example shows how to use PingOne as the identity provider with unsigned/unencrypted assertions.

## Before you start

1. Add the following basic PingGateway configuration if you have not already done so:

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Add the following route to PingGateway to serve the sample application .css and other static resources:

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

2. Set up the network:

   Add `sp.example.com` to your `/etc/hosts` file:

   ```none
   127.0.0.1 localhost am.example.com ig.example.com app.example.com sp.example.com
   ```

   Traffic to the application is proxied through PingGateway, using the host name `sp.example.com`.

3. Save the [sp.xml](../gateway-guide/federation-example-files.html#ping-saml-files) file as the SAML service provider configuration file `$HOME/.openig/SAML/sp.xml`.

## Prepare PingOne

1. [Prepare the PingOne environment and test user](preface.html).

   Make sure you match the test user's credentials to those known to the sample application.

2. In the PingOne environment, create a SAML web application with the following values:

   * Application Name: `saml_app`

   * Description: `SAML application`

   * Application Type: `SAML Application`

3. In the application, select the Import Metadata panel, add the SAML configuration file `sp.xml` and save the application.

4. On the Attribute Mappings panel, click [icon: edit, set=material, size=inline] (edit) and add the following mappings:

   | saml\_app | PingOne     |
   | --------- | ----------- |
   | cn        | Given Name  |
   | sn        | Family Name |

5. On the Configuration panel, click [icon: edit, set=material, size=inline] (edit) and set the SLO BINDING's SUBJECT NAMEID FORMAT to `urn:oasis:names:tc:SAML:2.0:nameid-format:transient`.

6. On the Configuration panel, click Download Metadata and save the downloaded file as the identity provider configuration file `$HOME/.openig/SAML/idp.xml`.

7. On the Configuration panel, record the Initiate Single Sign-on URL.

   You need the value to set up PingGateway.

8. At the top-right of the page, click the slider to enable the application.

Learn more from the PingOne documentation [Add a SAML application](https://docs.pingidentity.com/pingone/pingone_tutorials/p1_p1tutorial_add_a_saml_app.html).

## Prepare PingGateway

1. Copy the following [example SAML configuration files](../gateway-guide/federation-example-files.html#ping-saml-files) to `$HOME/.openig/SAML` and edit them to match your configuration:

   | File                          | Required changes                                                                 |
   | ----------------------------- | -------------------------------------------------------------------------------- |
   | `FederationConfig.properties` | None                                                                             |
   | `fedlet.cot`                  | Replace idp-entityID with the value of `EntityDescriptor entityID` in `idp.xml`. |
   | `idp-extended.xml`            | Replace idp-entityID with the value of `EntityDescriptor entityID` in `idp.xml`. |
   | `sp-extended.xml`             | None                                                                             |

2. Make sure the PingGateway configuration at `$HOME/.openig/SAML` contains the following files:

   ```console
   $ ls -l $HOME/.openig/SAML
   ```

   Output

   ```
   FederationConfig.properties
   fedlet.cot
   idp-extended.xml
   idp.xml
   sp-extended.xml
   sp.xml
   ```

3. Add the following route to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/saml-filter.json`

   * Windows

     `%appdata%\OpenIG\config\routes\saml-filter.json`

   ```json
   {
     "name": "saml-filter",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/home')}",
     "handler": {
       "type": "Chain",
       "config": {
         "filters": [
           {
             "name": "SamlFilter",
             "type": "SamlFederationFilter",
             "config": {
               "assertionMapping": {
                 "name": "cn",
                 "surname": "sn"
               },
               "subjectMapping": "sp-subject-name",
               "redirectURI": "/home/saml-filter"
             }
           },
           {
             "name": "SetSamlHeaders",
             "type": "HeaderFilter",
             "config": {
               "messageType": "REQUEST",
               "add": {
                 "x-saml-cn": [ "${toString(session.name)}" ],
                 "x-saml-sn": [ "${toString(session.surname)}" ]
               }
             }
           }
         ],
         "handler": "ReverseProxyHandler"
       }
     }
   }
   ```

   Source: [saml-filter.json](../_attachments/config/routes/saml-filter.json)

4. Restart PingGateway.

## Validation

Test IdP-initiated login:

1. In your browser's privacy or incognito mode, go to the URL given by the web application property Initiate Single Sign-on URL.

   PingOne displays the sign-on page.

2. Sign on to PingOne as the test user.

   PingGateway displays the sample application home page.

Test SP-initiated login:

1. In your browser's privacy or incognito mode, go to <https://sp.example.com:8443/home>.

2. Sign on as the test user.

   The request is redirected to the sample application.

   PingGateway displays the sample application home page.

|   |                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If a request returns an HTTP 414 URI Too Long error, read [URI Too Long error](../maintenance-guide/troubleshooting.html#troubleshoot-HTTP414). |

---

---
title: PingGateway with PingOne as an OIDC provider
description: Configure PingGateway as a relying party using PingOne as an OpenID Connect provider, including application setup, route configuration, and validation
component: pinggateway
version: 2026
page_id: pinggateway:pingone:oidc-ping
canonical_url: https://docs.pingidentity.com/pinggateway/2026/pingone/oidc-ping.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-07-03T16:53:36Z
keywords: ["Single sign-on (SSO)", "Security", "Authenticate", "OAuth 2.0", "OpenID Connect (OIDC)"]
page_aliases: ["identity-cloud-guide:oidc-ping.adoc"]
section_ids:
  prepare_pingone: Prepare PingOne
  prepare_pinggateway: Prepare PingGateway
  validation: Validation
---

# PingGateway with PingOne as an OIDC provider

This example sets up PingOne as an OIDC provider with PingGateway as a relying party.

## Prepare PingOne

After you [prepare the PingOne environment and test user](preface.html), follow these steps to [create a PingOne OIDC web application](https://docs.pingidentity.com/pingone/applications/p1_mfa_creating_a_web_application.html):

1. In the environment, create a web application with the following values:

   * Application Name: `oidc_client`

   * Description: `OIDC client`

   * Application Type: `OIDC Web App`

2. In the application, select the Overview panel and click Protocol OpenID Connect.

3. In the Redirect URIs field, add `https://ig.example.com:8443/home/id_token/callback` and save the application.

4. In the Overview panel, click Resource Access, select the `email` and `profile` scopes in addition to the default `openid` scope, and click Save.

   Learn more from the PingOne documentation on [Editing an application - OIDC](https://docs.pingidentity.com/pingone/applications/p1_edit_application_oidc.html).

5. At the top-right of the page, click the slider to enable the application.

6. Go to the Configuration panel and make a note of the following values in the URLs drop-down list:

   * OIDC Discovery Endpoint

   * Client ID

   * Client Secret

   You need the values to set up PingGateway.

## Prepare PingGateway

1. Add the following basic PingGateway configuration if you have not already done so:

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Add the following route to PingGateway to serve the sample application .css and other static resources:

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

2. Base64-encode the OIDC application's Client Secret and set the value as an environment variable:

   ```console
   $ export OIDC_SECRET_ID='<base64-encoded-client-secret>'
   ```

3. Add the following route to PingGateway, replacing the following property values with those of the OIDC application:

   * OIDC\_Discovery\_Endpoint: The OIDC discovery endpoint for the client application you registered.

   * Client\_ID: The client ID of the application.

     * Linux

       `$HOME/.openig/config/routes/oidc-ping.json`

     * Windows

       `%appdata%\OpenIG\config\routes\oidc-ping.json`

     ```json
     {
       "name": "oidc-ping",
       "condition": "${find(request.uri.path, '^/home/id_token')}",
       "properties": {
         "OIDC_Discovery_Endpoint": "OIDC Discovery endpoint of the web app",
         "Client_ID": "Client ID of the web app"
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
                   "clientId": "&{Client_ID}",
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
                         "text/html; charset=UTF-8"
                       ]
                     },
                     "entity": "<html><body>Error in OAuth 2.0 setup.<br> ${contexts.oauth2Failure.exception.message}</body></html>"
                   }
                 },
                 "registrations": [
                   {
                     "name": "oauth2-client",
                     "type": "ClientRegistration",
                     "config": {
                       "clientId": "${Client_ID}",
                       "issuer": {
                         "name": "PingOne",
                         "type": "Issuer",
                         "config": {
                           "wellKnownEndpoint": "&{OIDC_Discovery_Endpoint}"
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
           "handler": {
             "type": "StaticResponseHandler",
             "name": "HTMLResponse",
             "config": {
               "status": 200,
               "entity": "<!DOCTYPE html><html><head><title>Authentication Success</title></head><body><p>Welcome, ${contexts.oauth2Info.userInfo.preferred_username}!</p><code>${contexts.oauth2Info.userInfo}</code></body></html>",
               "headers": {
                 "Content-Type": [
                   "text/html"
                 ]
               }
             }
           }
         }
       }
     }
     ```

     Source: [oidc-ping.json](../_attachments/config/routes/oidc-ping.json)

4. Restart PingGateway.

## Validation

1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/id_token>.

   PingOne displays the sign-on page.

2. Sign on to PingOne as the test user.

   The route displays a welcome page:

   ```none
   Welcome, wolkig!

   {sub=..., preferred_username=wolkig, given_name=Wilhelm, updated_at=..., family_name=Wolkig, email=wolkig@example.com, ...}
   ```

---

---
title: PingOne Authorize integration with PingGateway
description: Configure PingGateway with PingOne Authorize to protect APIs and web applications using authorization decisions based on group membership
component: pinggateway
version: 2026
page_id: pinggateway:pingone:aam
canonical_url: https://docs.pingidentity.com/pinggateway/2026/pingone/aam.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-03-09T12:00:00Z
keywords: ["Configuration", "Authorization"]
section_ids:
  about_the_example: About the example
  before_you_begin: Before you begin
  configure_pingone: Configure PingOne
  add_a_group_who_can_access_to_the_sample_application: Add a group who can access to the sample application
  add_a_test_user_who_gets_access: Add a test user who gets access
  add_a_test_user_who_doesnt_get_access: Add a test user who doesn't get access
  enable_pingone_authorize: Enable PingOne Authorize
  add_a_pinggateway_oidc_client_profile: Add a PingGateway OIDC client profile
  add_an_api_gateway: Add an API gateway
  add_an_api_service: Add an API service
  make_sure_pinggateway_gets_an_access_token: Make sure PingGateway gets an access token
  configure_pinggateway: Configure PingGateway
  validation: Validation
  access_granted_to_a_group_member: Access granted to a group member
  access_denied_for_a_non_member: Access denied for a non-member
  troubleshooting: Troubleshooting
---

# PingOne Authorize integration with PingGateway

Use [PingOne Authorize](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_overview.html) with PingGateway to protect APIs and web applications. When you add a [PingAuthorizeFilter](../reference/PingAuthorizeFilter.html) to a route, PingGateway requests an authorization decision from PingOne Authorize.

The same PingGateway filter works with [PingAuthorize](https://docs.pingidentity.com/pingauthorize) as well. Adapt the configuration to work with the Sideband API for your PingAuthorize deployment.

## About the example

This example uses PingOne as the IdP and OIDC provider. It uses PingOne Authorize [API access management](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_introduction.html#api-access-mgmt) capabilities to protect a sample application path.

When a user tries to access a sample application resource, PingGateway directs the user to PingOne for authentication. On successful authentication, PingOne issues an ID token for the user and an access token that PingGateway uses when getting an access decision from PingOne Authorize. If PingGateway was protecting an API rather than a sample application page, the access token would act as the bearer token that an OAuth 2.0 API client application provides to access the API. In this example, however, PingGateway gets the access token because it's acting as the client application.

PingOne Authorize either grants access or denies it and then PingGateway enforces the decision from PingOne Authorize.

In this example, the decision to authorize access depends on group membership. Learn more about a similar decision to authorize access that depends on group membership in the [Defining operations for protected actions](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_add_api_service_operations.html) tutorial in the PingOne Authorize documentation.

## Before you begin

If you haven't already done so:

* Install PingGateway.

* Install the sample application.

* Create a PingOne environment.

Learn more in the [PingGateway and PingOne examples](preface.html).

## Configure PingOne

Complete the tasks in this section to prepare the PingOne environment for this example.

On completing these tasks, you will have:

* A group for users who can access the sample application

* A test user who belongs to the group

* A test user who doesn't belong to the group

* PingOne Authorize enabled in the environment

* An OIDC client profile for PingGateway to authenticate users with PingOne

* An API gateway account for PingGateway to authenticate to PingOne Authorize

* An API service that PingOne Authorize uses to make access decisions

* PingOne configured to issue access tokens to PingGateway alongside ID tokens for users

### Add a group who can access to the sample application

In your PingOne environment, go to Directory > Groups and add a group named `Full access`. This group's members get access to the sample application.

Learn more in [Creating a group](https://docs.pingidentity.com/pingone/directory/p1_managing_groups.html#creating-a-group) in the PingOne documentation.

### Add a test user who gets access

If you haven't already done so, add a test user.

1. Go to Directory > Users and add a user:

   * Given Name: `Wilhelm`

   * Family Name: `Wolkig`

   * Username: `wolkig`

   * Email: `wolkig@example.com`

   * Password: Click Generate Password and record the generated password.

   Learn more in the PingOne documentation on [Adding a user](https://docs.pingidentity.com/pingone/directory/p1_adduser.html).

2. In the profile for `wolkig`, add the user to the `Full access` group and save your work.

   In this example, PingOne Authorize will grant access to the sample application based on membership in this group.

### Add a test user who doesn't get access

1. Add a second test user:

   * Given Name: `Demo`

   * Family Name: `User`

   * Username: `demo`

   * Email: `demo@example.com`

   * Password: Click Generate Password and record the generated password.

2. *Don't* add the `demo` user to the `Full access` group.

   The `demo` user won't get access to the sample application.

### Enable PingOne Authorize

[Add PingOne Authorize to the environment](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_getting_started.html).

### Add a PingGateway OIDC client profile

In this example, PingGateway acts as a PingOne OIDC client (RP) where PingOne is the OIDC provider for user identities and authentication.

Follow these steps to [create a PingOne OIDC web application for PingGateway](https://docs.pingidentity.com/pingone/applications/p1_mfa_creating_a_web_application.html):

1. Go to Applications > Applications and click + to add a new application:

   * Application Name: `oidc_client`

   * Application Type: `OIDC Web App`

2. In the application Overview, click Protocol OpenID Connect [icon: cogs, set=fa], add a redirect URI, and save your work:

   * Redirect URIs: `https://ig.example.com:8443/home/sso/callback`.

3. Copy the following values from the application Overview and save them somewhere convenient for later use:

   * General > Client ID

   * General > Client Secret

   * Connection Details > OIDC Discovery Endpoint

   You need the values to set up PingGateway.

4. Enable the application.

### Add an API gateway

PingGateway uses a PingOne API gateway account to authenticate to PingOne Authorize:

1. Go to Authorization > API Gateways and click +.

2. Use `PingGateway` as the Name and save your work.

3. Next to Credentials, click + and copy the API gateway credential somewhere convenient for later use.

   You need the credential value to set up PingGateway.

### Add an API service

PingOne Authorize bases authorization decisions on an API service definition. Follow these steps to add the API service:

1. Go to Authorization > API Services and add a new API service with the following values:

   * Name: `PingGateway`

   * Base URLs: `https://app.example.com:8444` (for the sample application)\
     `https://ig.example.com:8443` (for PingGateway)

2. Define an operation for protected access to the sample application.

   This grants users in the `Full access` group access to the sample application page at `/home/sso`:

   * Method: `GET`

   * Paths: `/home/sso`

   * Rules: The user must be a member of any of these groups: `Full access`

   Learn more in the PingOne Authorize documentation on [Defining operations for protected actions](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_add_api_service_operations.html).

3. Click Deploy to deploy the new API service.

### Make sure PingGateway gets an access token

When you added the PingGateway API service, PingOne Authorize automatically created a corresponding PingOne resource by default. Update the resource so PingOne issues access tokens to PingGateway.

To do so, set the audience claim (`aud`) to the PingGateway URL and add a scope specifically for PingGateway:

1. Go to Applications > Resources and click the `PingGateway` resource.

2. Edit the following settings and save your work:

   * Audience: `https://ig.example.com:8443`

   * Scopes: Click Add Scope, add Scope Name: `gateway`, and click Save.

3. Go to Applications > Applications and click `oidc_client`, the OIDC application for PingGateway.

4. Edit Allowed Scopes, select the gateway scope checkbox, and click Save.

   PingOne is now ready to issue access tokens with the scope `gateway` to PingGateway. PingGateway uses the tokens when requesting PingOne Authorize access decisions.

## Configure PingGateway

1. Prepare the secrets PingGateway needs to act as an OIDC RP and an API gateway when making requests to PingOne.

   Base64-encode the API gateway's credential and the OIDC application's client secret and set both values as environment variables:

   ```console
   $ export GATEWAY_SECRET_ID='<base64-encoded-api-gateway-credential>'
   $ export OIDC_SECRET_ID='<base64-encoded-client-secret>'
   ```

2. Restart PingGateway to read the environment variables.

3. Add the following route to PingGateway, replacing the property values to match those from the environment:

   * Linux

     `$HOME/.openig/config/routes/pingone-aam.json`

   * Windows

     `%appdata%\OpenIG\config\routes\pingone-aam.json`

   ```json
   {
     "name": "pingone-aam",
     "condition": "${find(request.uri.path, '^/home/sso')}",
     "baseURI": "https://app.example.com:8444",
     "properties": {
       "gatewayServiceUrl": "https://http-access-api.pingone.eu/v1/environments/test-environment-id",
       "oidcClientId": "oidc-client-id",
       "oidcWellKnownEndpoint": "https://auth.pingone.eu/test-environment-id/as/.well-known/openid-configuration"
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
                 "clientId": "&{oidcClientId}",
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
             "type": "AuthorizationCodeOAuth2ClientFilter",
             "config": {
               "clientEndpoint": "/home/sso",
               "failureHandler": {
                 "type": "StaticResponseHandler",
                 "config": {
                   "status": 500,
                   "headers": {
                     "Content-Type": [
                       "text/plain"
                     ]
                   },
                   "entity": "Error: ${contexts.oauth2Failure.error}\nDescription: ${contexts.oauth2Failure.description}"
                 }
               },
               "registrations": [
                 {
                   "type": "ClientRegistration",
                   "config": {
                     "clientId": "&{oidcClientId}",
                     "issuer": {
                       "type": "Issuer",
                       "config": {
                         "wellKnownEndpoint": "&{oidcWellKnownEndpoint}"
                       }
                     },
                     "scopes": [
                       "openid",
                       "gateway"
                     ],
                     "authenticatedRegistrationHandler": "AuthenticatedRegistrationHandler-1"
                   }
                 }
               ]
             }
           },
           {
             "type": "PingAuthorizeFilter",
             "config": {
               "gatewayServiceUri": "&{gatewayServiceUrl}",
               "secretsProvider": "SystemAndEnvSecretStore-1",
               "gatewayCredentialSecretId": "gateway.secret.id",
               "accessToken": "${contexts.oauth2Info.accessToken}",
               "_sidebandHandler": {
                 "_comment": "s/_sidebandHandler/sidebandHandler/ to troubleshoot AAM decisions",
                 "type": "ClientHandler",
                 "capture": "all"
               }
             }
           }
         ],
         "handler": "ReverseProxyHandler"
       }
     }
   }
   ```

   Source: [pingone-aam.json](../_attachments/config/routes/pingone-aam.json)

   Notice the following features of the route:

   * The route properties use the settings you collected from the PingOne environment.

   * The heap has:

     * A handler to trust the self-signed sample application certificate for HTTPS blindly.

       |   |                                                                                         |
       | - | --------------------------------------------------------------------------------------- |
       |   | For production applications and APIs, use certificates you don't have to trust blindly. |

     * A `SystemAndEnvSecretStore` to get the base64-encoded secrets from the environment variables.

     * A handler to get an ID token and access token.

   * The `AuthorizationCodeOAuth2ClientFilter` authenticates the end user.

   * The `PingAuthorizeFilter` uses the access token when making the authorization decision request to PingOne Authorize.

   * If PingOne Authorize grants access, the `BlindTrustReverseProxyHandler` gets the resource from the sample application.

## Validation

### Access granted to a group member

1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/sso>.

   PingOne displays the sign-on page.

2. Sign on to PingOne as the `wolkig` test user.

   PingOne Authorize grants access and PingGateway displays the sample application home page:

   ![sample application home page](_images/aam-home-page.png)

### Access denied for a non-member

1. In your browser's privacy or incognito mode, go again to <https://ig.example.com:8443/home/sso>.

   PingOne displays the sign-on page.

2. Sign on to PingOne as the `demo` test user.

   PingOne Authorize denies access to the sample application and the browser displays the result:

   ```json
   {
     "id" : "<uuid>",
     "code" : "ACCESS_FAILED",
     "message" : "The request could not be completed. You do not have access to this resource."
   }
   ```

   |   |                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When PingOne Authorize denies access or the example route fails to get an access token, the browser displays text, which isn't user-friendly.If you are protecting web pages rather than an API, use a [StaticResponseHandler](../reference/StaticResponseHandler.html) to show a more friendly page to the user. |

## Troubleshooting

If you get unexpected errors, try these debugging options:

* In the PingGateway route, update the `PingAuthorizeFilter` to enable the capture decorator.

  Change `"_sidebandHandler"` to `"sidebandHandler"` and save your work to let PingGateway reload the route.

* In the PingOne environment, go to Authorization > Recent Decisions, select the PingGateway decision endpoint, and select a decision to visualize.

  PingOne shows you how PingOne Authorize arrived at the authorization decision.

  On the Request and Response tabs, you find detailed traces of the parameters for each. Learn more in [Recent decisions](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_recent_decisions.html) in the PingOne Authorize documentation.

---

---
title: PingOne Protect integration with PingGateway
description: Integrate PingOne Protect risk evaluations with PingGateway to route requests based on low, medium, or high risk scores
component: pinggateway
version: 2026
page_id: pinggateway:pingone:risk
canonical_url: https://docs.pingidentity.com/pinggateway/2026/pingone/risk.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-07-03T16:53:36Z
keywords: ["Configuration", "Authentication", "Risk"]
page_aliases: ["identity-cloud-guide:risk.adoc"]
section_ids:
  risk_management: Risk management
  example_protect_against_session_degradation: "Example: protect against session degradation"
  before_you_begin: Before you begin
  configure_pinggateway: Configure PingGateway
  validation: Validation
  risk-self-managed: Self-managed AM
---

# PingOne Protect integration with PingGateway

Use PingOne Protect risk evaluations with web applications protected by PingGateway. PingGateway routes requests based on the level of risk PingOne Protect associates with them.

## Risk management

PingOne Protect monitors end-user requests and generates a risk score of low, medium, or high based on the user's activity and device context. You configure and fine-tune risk policies and train risk models prior to using PingGateway with PingOne Protect. Learn more in [Threat Protection using PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_overview.html).

You configure PingGateway routes to react to risk scores from PingOne Protect dynamically. For example, if the risk score is medium, PingGateway can direct the user to complete additional verification. If the risk score is high, PingGateway can deny access to the resource instead.

The following sequence diagram shows the PingGateway configuration objects involved in a risk management flow:

* The [PingOneProtectEvaluationFilter](../reference/PingOneProtectEvaluationFilter.html) calls PingOne Protect.

* It populates the [PingOneProtectEvaluationContext](../reference/PingOneProtectEvaluationContext.html) based on the response.

* The [PingOneProtectThreatLevelRoutingHandler](../reference/PingOneProtectThreatLevelRoutingHandler.html) dispatches the request based on its risk level.

* After prompting the user to complete additional actions following a risk evaluation, the [PingOneProtectFeedbackSuccessFilter](../reference/PingOneProtectFeedbackSuccessFilter.html) or [PingOneProtectFeedbackFailureFilter](../reference/PingOneProtectFeedbackFailureFilter.html) can send feedback to PingOne Protect and override the risk level in the session context.

![Data flow with PingOne Protect for risk evaluation](_images/risk.svg)

1. The initial request enters a Chain configured for risk evaluation with PingOne Protect.

2. The PingOneProtectEvaluationFilter includes data about the request in an API call to PingOne Protect.

3. PingOne Protect provides a risk evaluation response.

4. The PingOneProtectEvaluationFilter populates the PingOneProtectEvaluationContext with the risk level based on the evaluation response and passes control to the PingOneProtectThreatLevelRoutingHandler.

5. -10. The PingOneProtectThreatLevelRoutingHandler dispatches the request based on the risk level. The downstream handler returns a response to the initial request that is appropriate for the risk level. The downstream handlers can prompt additional actions to verify the user's identity.

Although not shown in the sequence diagram, when a `medium` risk level leads to additional authentication steps and the user successfully completes the steps, a PingOneProtectFeedbackSuccessFilter included in the process updates PingOne Protect to indicate the successful outcome.

The sequence diagram also omits device profile data collection. When the PingOneProtectEvaluationFilter includes `"deviceProfile"` settings, PingGateway gathers profile data from the user-agent by sending it a self-submitting form page that uses JavaScript to retrieve the profile information. (If JavaScript is disabled in the browser, PingGateway can't get the device profile data.) PingGateway includes the device profile in PingOne Protect risk evaluation requests.

PingGateway runs at the outer edge of your systems, the place where all inbound traffic first arrives and all outbound traffic leaves, just inside the network infrastructure.

PingGateway is well-placed to capture signals about the traffic and its risk profile.

## Example: protect against session degradation

*Session degradation* arises when a valid user session gets used in unexpected ways, increasing the risk the session has been hijacked or otherwise compromised. Session degradation is why we can't let users stay signed in forever unless we can authenticate them again.

Together, PingGateway and PingOne Protect help you automate fine-grained risk evaluation, avoiding the distraction of additional authentication steps unless they're required for a risky request. Users stay signed in with their current session, which they experience as a **keep me signed in** feature. You nevertheless protect their assets from hijacking without needing constantly to verify their identity.

This example demonstrates risk management where the principal already has a valid session. The example doesn't demonstrate how to configure PingOne Protect.

When PingOne Protect returns a risk evaluation, PingGateway responds based on the risk level. This example demonstrates the following responses:

* High risk

  Deny access to the requested resource.

  Although not shown in this brief example, you could route the request to a honeypot.

* Medium risk

  Prompt the user to reauthenticate to verify their identity.

  The user can perform step up or transactional authentication at this point.

* Low risk

  Let the request pass through unchanged.

### Before you begin

* Configure PingOne Protect. Learn more in the [PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_overview.html) documentation.

* Implement [CDSSO with PingOne Advanced Identity Cloud](../aic/cdsso.html) or [CDSSO for self-managed AM](../gateway-guide/cdsso.html). This example opts for CDSSO with PingOne Advanced Identity Cloud. When using self-managed AM, also read [Self-managed AM](#risk-self-managed).

* For additional protection with medium-risk requests, implement [Step up authorization for a transaction](../aic/pep.html#stepup-session).

* Verify you can successfully authenticate with CDSSO to the sample application.

### Configure PingGateway

What follows extends the CDSSO route to protect against session degradation:

1. Sign on to the PingOne environment with PingOne Protect as an administrator and add an application for PingGateway.

   Use the following hints regarding non-default configuration settings:

   | Setting                     | Value                                 |
   | --------------------------- | ------------------------------------- |
   | Application Name            | PingGateway                           |
   | Application Type            | Worker                                |
   | Application profile > Roles | Environment Admin Identity Data Admin |

2. In the PingOne environment, find and record the values of the following settings:

   | Property                  | Description                                                                                                    |
   | ------------------------- | -------------------------------------------------------------------------------------------------------------- |
   | Environment UUID          | This is `<env-uuid>` in other property examples.                                                               |
   | PingGateway client ID     | PingGateway credentials to access PingOne as the application you registered.                                   |
   | PingGateway client secret |                                                                                                                |
   | Policy set UUID           | The PingOne Protect policy for risk evaluation requests.                                                       |
   | Service endpoint          | For risk evaluation and feedback service requests.Example: `https://api.pingone.eu/v1/environments/<env-uuid>` |
   | Token endpoint            | For PingGateway to get an access token.Example: `https://auth.pingone.eu/<env-uuid>/as/token`                  |

3. In the PingGateway [AdminHttpApplication (`admin.json`)](../reference/AdminHttpApplication.html) file, make sure the maximum total headers size is large enough to accommodate request headers for the device profile cookies.

   After PingGateway collects device profile data, it stores the data in cookies on the user-agent. The user-agent returns these to PingGateway in the `Cookie` request header. Set the `maxTotalHeadersSize` for the PingGateway server ports large enough to avoid HTTP 431 Request Header Fields Too Large errors; for example:

   ```json
   "connectors": [
     {
       "port": 8080,
       "maxTotalHeadersSize": 32768
     },
     {
       "port": 8443,
       "maxTotalHeadersSize": 32768,
       "tls": "TlsConf"
     }
   ],
   ```

   You can skip this step if you don't use `"deviceProfile"` settings in the PingOneProtectEvaluationFilter.

4. Set an environment variable for the PingGateway client secret.

   PingGateway uses a SystemAndEnvSecretStore to retrieve the client secret, so you must base64-encode the value you found in the PingOne application profile:

   ```console
   $ export CLIENT_SECRET_ID='<base-64-encoded-client-secret>'
   ```

5. Restart PingGateway to load the updated `admin.json` settings and the environment variable.

6. Update the CDSSO route to add risk management:

   ```json
   {
     "name": "risk",
     "baseURI": "https://app.example.com:8444/login",
     "condition": "${find(request.uri.path, '^/home/cdsso')}",
     "properties": {
       "amInstanceUrl": "https://myTenant.forgeblocks.com/am",
       "clientId": "my-application-client-id",
       "policySetId": "my-policy-set-id",
       "serviceEndpoint": "https://api.pingone.eu/v1/environments/my-environment-id",
       "tokenEndpoint": "https://auth.pingone.eu/my-environment-id/as/token"
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
       },
       {
         "name": "ClientCredentialsOAuth2ClientFilter-1",
         "type": "ClientCredentialsOAuth2ClientFilter",
         "config": {
           "tokenEndpoint": "&{tokenEndpoint}",
           "scopes": [
             "openid",
             "profile",
             "email",
             "p1"
           ],
           "endpointHandler": {
             "name": "AccessTokenHandler",
             "type": "Chain",
             "config": {
               "filters": [
                 {
                   "type": "ClientSecretBasicAuthenticationFilter",
                   "config": {
                     "clientId": "&{clientId}",
                     "clientSecretId": "client.secret.id",
                     "secretsProvider": "SystemAndEnvSecretStore-1"
                   }
                 }
               ],
               "handler": "ForgeRockClientHandler"
             }
           }
         }
       },
       {
         "name": "RiskEndpointHandler",
         "type": "Chain",
         "config": {
           "filters": [
             "ClientCredentialsOAuth2ClientFilter-1"
           ],
           "handler": "ForgeRockClientHandler"
         }
       },
       {
         "name": "PingOneService-1",
         "type": "PingOneService",
         "config": {
           "serviceEndpoint": "&{serviceEndpoint}",
           "endpointHandler": "RiskEndpointHandler"
         }
       },
       {
         "name": "StepUpHandler",
         "type": "Chain",
         "config": {
           "filters": [
             {
               "name": "PolicyEnforcementFilter-1",
               "type": "PolicyEnforcementFilter",
               "config": {
                 "application": "PEP-CDSSO",
                 "ssoTokenSubject": "${contexts.cdsso.token}",
                 "amService": "AmService-1"
               }
             },
             {
               "name": "SuccessFeedbackFilter",
               "type": "PingOneProtectFeedbackSuccessFilter",
               "config": {
                 "pingOneService": "PingOneService-1",
                 "postEvaluationAssumedRiskLevel": "low"
               }
             }
           ],
           "handler": "ReverseProxyHandler"
         }
       },
       {
         "name": "FailureHandler",
         "type": "Chain",
         "config": {
           "filters": [
             {
               "name": "FailureFeedbackFilter",
               "type": "PingOneProtectFeedbackFailureFilter",
               "config": {
                 "pingOneService": "PingOneService-1"
               }
             }
           ],
           "handler": {
             "type": "StaticResponseHandler",
             "config": {
               "status": 403,
               "headers": {
                 "Content-Type": [
                   "text/plain; charset=UTF-8"
                 ]
               },
               "entity": "HTTP 403 Forbidden"
             }
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
             "name": "PingOneProtectEvaluationFilter-1",
             "type": "PingOneProtectEvaluationFilter",
             "config": {
               "pingOneService": "PingOneService-1",
               "policySet": "&{policySetId}",
               "userId": "${contexts.cdsso.claimsSet.getClaim('subname')}",
               "nonEvaluatedUrls": "${find(request.uri.path, '/home/cdsso/redirect')}",
               "deviceProfile": {
                 "callbackEndpoint": "/home/cdsso/profilecallback"
               }
             }
           }
         ],
         "handler": {
           "name": "PingOneProtectThreatLevelRoutingHandler-1",
           "type": "PingOneProtectThreatLevelRoutingHandler",
           "config": {
             "levels": {
               "low": "ReverseProxyHandler",
               "medium": "StepUpHandler",
               "high": "FailureHandler"
             }
           }
         }
       }
     }
   }
   ```

   Source: [risk.json](../_attachments/config/routes/risk.json)

   Notice the following features of the updated route:

   * The route properties use the settings you collected from the PingOne environment.

     Replace the placeholders in the route properties with the settings you collected.

   * The heap has an evaluation endpoint handler to get an access token for risk evaluation requests.

   * The PingOneProtectEvaluationFilter uses the evaluation endpoint handler to make the risk evaluation request and populate the PingOneProtectEvaluationContext (implicit in the configuration).

   * The PingOneProtectThreatLevelRoutingHandler uses the context to route the request based on the risk level:

     * Low-risk requests pass through unchanged.

     * Medium-risk requests use step up authorization for the request.

     * High-risk requests and requests where the PingOneProtectEvaluationFilter failed to update the context get denied.

### Validation

1. In your browser's privacy or incognito mode, go to <https://ig.ext.com:8443/home/cdsso>.

   PingOne Advanced Identity Cloud displays the login page.

2. Log in to PingOne Advanced Identity Cloud as the test user.

   After authentication, PingGateway gets an access token and uses it to make a risk evaluation request. The PingOneProtectThreatLevelRoutingHandler routes the result:

   * Low-risk requests go directly to the sample app.

   * Medium-risk requests prompt the user for the authorization passcode `7890`.

   * PingGateway denies access to other requests.

You've successfully demonstrated risk management to prevent session degradation. Adapt the route to the specifics of your use case.

## Self-managed AM

When you use transactional authorization with self-managed AM in this example, you must configure PingGateway to use *its* URI rather than the URI of the protected application when confirming the transaction.

You can do this by using a PolicyEnforcementFilter `"resourceUriProvider"` to rebase the protected URI on the PingGateway URI.

1. Add the following [ScriptableResourceUri.groovy](../_attachments/scripts/groovy/ScriptableResourceUri.groovy) script to PingGateway:

   * Linux

     `$HOME/.openig/scripts/groovy/ScriptableResourceUri.groovy`

   * Windows

     `%appdata%\OpenIG\scripts\groovy\ScriptableResourceUri.groovy`

   > **Collapse: ScriptableResourceUri.groovy**
   >
   > ```groovy
   > package scripts.groovy
   >
   > import org.forgerock.http.routing.UriRouterContext
   > import org.forgerock.http.util.Uris
   >
   > /**
   >  * Sample scriptable {@code RequestResourceUriProvider} (for use with a {@code PolicyEnforcementFilter}).
   >  *
   >  * This sample script "rebases" the in-flight request URI on top of the original URI. The term "in-flight" represents
   >  * the request's URI as it's manipulated as it progresses through the route. This is to ensure route components have had
   >  * the opportunity to act on the request prior to policy evaluation - e.g. to manipulate query parameters they may be
   >  * responsible for managing.
   >  *
   >  * <p>Example - indicates in-flight request URI's path, query and fragment retained and rebased on to original URI:
   >  * <ul>
   >  *     <li><b>original request URI</b>:  https://ig.ext.com:8443/home?param1=1&param2</li>
   >  *     <li><b>in-flight request URI</b>: http://app.example.com:8080/home?param2</li>
   >  *     <li><b>result (rebased) URI</b>:  https://ig.ext.com:8443/home?param2</li>
   >  * </ul>
   >  *
   >  * <p>Example config:
   >  * <pre>
   >  * {@code {
   >  *   "name" : "RebasingResourceUriProvider",
   >  *   "type" : "ScriptableResourceUriProvider",
   >  *   "config" : {
   >  *     "file" : "ScriptableResourceUri.groovy",
   >  *     "type": "application/x-groovy"
   >  *   }
   >  * }
   >  * }
   >  * </pre>
   >  *
   >  * <p>Example {@code PolicyEnforcementFilter} usage:
   >  * <pre>
   >  * {@code {
   >  *   "type" : "PolicyEnforcementFilter",
   >  *   "config" : {
   >  *     "amService" : "...",
   >  *     "application" : "...",
   >  *     "resourceUriProvider": "RebasingResourceUriProvider",
   >  *     ...
   >  *   }
   >  * }
   >  * }
   >  * </pre>
   >  */
   > def uriRouterContext = context.asContext(UriRouterContext.class)
   >
   > URI originalUri = uriRouterContext.getOriginalUri();
   > URI requestUri = request.getUri().asURI();
   > URI pathAndParams = new URI(null,
   >                             null,
   >                             requestUri.getPath(),
   >                             requestUri.getQuery(),
   >                             requestUri.getFragment());
   > logger.trace("ScriptableResourceUri rebasing {} with request parameters {}", originalUri, pathAndParams);
   > String rebasedUri = Uris.rebase(pathAndParams, originalUri).toASCIIString();
   > logger.trace("ScriptableResourceUri rebased to URI '{}'", rebasedUri);
   > return rebasedUri;
   > ```

2. Add a reference to the script in the route heap:

   ```json
   {
       "name": "RebasingResourceUriProvider",
       "type": "ScriptableResourceUriProvider",
       "config": {
           "file": "ScriptableResourceUri.groovy",
           "type": "application/x-groovy"
       }
   }
   ```

3. In the PolicyEnforcementFilter for the route, use the reference to the script in the `"resourceUriProvider"` setting:

   ```json
   {
       "name": "PolicyEnforcementFilter-1",
       "type": "PolicyEnforcementFilter",
       "config": {
           "application": "PEP-CDSSO",
           "ssoTokenSubject": "${contexts.cdsso.token}",
           "amService": "AmService-1",
           "resourceUriProvider": "RebasingResourceUriProvider"
       }
   }
   ```

4. Make sure the route's `"amInstanceUrl"` reflects your self-managed AM.

5. Save your changes to the route.

   After PingGateway reloads the route, you can validate the scenario with your self-managed AM deployment.
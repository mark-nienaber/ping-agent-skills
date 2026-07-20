---
title: About PingGateway and FAPI
description: Configure PingGateway and PingOne Advanced Identity Cloud for FAPI, a secure OAuth 2.0 profile for protecting APIs in high-security and financial environments
component: pinggateway
version: 2026
page_id: pinggateway:fapi:fapi
canonical_url: https://docs.pingidentity.com/pinggateway/2026/fapi/fapi.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-23T12:00:00Z
section_ids:
  testing_and_certification: Testing and certification
  pingone_advanced_identity_cloud: PingOne Advanced Identity Cloud
  pinggateway: PingGateway
  deployment: Deployment
---

# About PingGateway and FAPI

[FAPI](https://openid.net/wg/fapi/), originally short for Financial-grade API, is a secure OAuth 2.0 profile for protecting APIs in high security environments.

FAPI is a secure, interoperable alternative to screen scraping. You can use the secure profile for applications requiring tighter security than standard OAuth 2.0 and OpenID Connect, such as APIs accessing sensitive data or involving financial transactions.

## Testing and certification

In addition to publishing FAPI specifications, the FAPI Working Group at the OpenID Foundation offers conformance testing and certification for organizations implementing FAPI.

For example, a bank with open banking APIs can validate and certify their FAPI implementation. The OpenID Foundation publishes the certification so the bank's partners know what its implementation supports.

## PingOne Advanced Identity Cloud

PingOne Advanced Identity Cloud provides OAuth 2.0 and OpenID Provider authorization services. It dynamically registers and stores API client profiles.

Once configured as described in this tutorial, the PingOne Advanced Identity Cloud services support FAPI.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This tutorial shows how to configure your PingOne Advanced Identity Cloud tenant through the administrative UIs.As an alternative when evaluating PingGateway and FAPI, consider using the [Secure API Gateway platform configuration](https://github.com/SecureApiGateway/fr-platform-config) with the [PingOne Advanced Identity Cloud configuration management tools](https://github.com/ForgeRock/fr-config-manager) instead.For FAPI, use the `core` overlay from the Secure API Gateway configuration. The `ob` overlay is for OpenBanking deployments.While Ping Identity doesn't officially support the configuration management tools, they can simplify your work. The tools are community-supported. If you encounter an issue, raise it through the project GitHub site. |

Although not shown in this tutorial, you can configure self-hosted AM and IDM in a platform deployment to support FAPI. Adapt the instructions for configuring access and identity management services.

## PingGateway

PingGateway protects the PingOne Advanced Identity Cloud endpoints and your APIs, allowing only trusted API clients to register, get access tokens, and use the APIs.

PingGateway communicates with the trusted directory in a FAPI-based ecosystem to vet API clients. It prevents insecure and untrusted API clients from participating in the ecosystem. Trusted organizations register their keys in the trusted directory and use these to sign keys issued to their API clients.

## Deployment

The following image illustrates how you protect APIs with FAPI:

![FAPI deployment protecting banking APIs](_images/ig-fapi-mapping.png)

* You host your APIs and PingGateway acting as a reverse proxy for protected APIs.

* Ping Identity hosts your PingOne Advanced Identity Cloud tenants for access and identity management services.

* A central actor in the ecosystem hosts the trusted directory.

  For this tutorial, you can use the sample trusted directory Docker image provided alongside PingGateway.

* Trust partners host the client applications using your APIs securely.

For this tutorial and to get started with conformance testing, you host the sample application as well.

---

---
title: Configuring access management for FAPI
description: "Configure PingOne Advanced Identity Cloud and PingAM settings for FAPI: trusted certificates, OpenID provider, validation service, and OAuth 2.0 client account"
component: pinggateway
version: 2026
page_id: pinggateway:fapi:aic-am
canonical_url: https://docs.pingidentity.com/pinggateway/2026/fapi/aic-am.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-09-08T17:46:50Z
section_ids:
  before_you_begin: Before you begin
  trusted_certificates: Trusted certificates
  openid_provider: OpenID provider
  validation_service: Validation service
  create-oauth2-client: Create an OAuth 2.0 client account
---

# Configuring access management for FAPI

FAPI requires specific settings for the OpenID Provider and related services.

This page explains how to configure those settings for a PingOne Advanced Identity Cloud tenant through the Advanced Identity Cloud admin UI and AM admin UI.

|   |                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------- |
|   | If you're configuring a self-managed PingAM deployment, FAPI functionality requires AM version 8.0.2 or later. |

## Before you begin

1. Sign on to the Advanced Identity Cloud admin UI as an administrator.

2. Switch to the realm you use for FAPI.

   This tutorial uses the `alpha` realm. Adapt the realm name to your deployment.

## Trusted certificates

FAPI permits [mutual TLS](https://www.rfc-editor.org/rfc/rfc8705.html) as one of the OAuth 2.0 client authentication methods. For mutual TLS to work, PingOne Advanced Identity Cloud must trust the certificate authority (CA) who signed the client's certificate. This involves storing the trusted certificates as a secret and mapping the secret to a specific label:

1. Get the CA certificates in PEM format for all the clients using mutual TLS.

2. Concatenate the CA certificates into a single PEM format file.

3. [Create an ESV secret](https://docs.pingidentity.com/pingoneaic/tenants/esvs-manage-ui.html#create_secrets) named `esv-am-oauth2-ca-certs` whose value is the base64-encoded content of the trusted CA certificate PEM file.

4. In the Advanced Identity Cloud admin UI, click [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management to open the AM admin UI.

5. Go to Secret Stores > ESV > Mappings and click + Add Mapping.

6. Add the following settings and click Create:

   * Secret Label

     `am.services.oauth2.tls.client.cert.authentication`

   * aliases

     `esv-am-oauth2-ca-certs`

You have successfully trusted the CA certificates for mutual TLS.

## OpenID provider

1. In the Advanced Identity Cloud admin UI, click [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management to open the AM admin UI.

2. Go to Services > OAuth2 Provider.

3. For each of the categories, update the following settings and click Save Changes before changing categories.

   Adapt `https://gateway.example.com:8443` in these settings for your deployment and accept the defaults for all settings not listed:

   | Category                    | Setting                                                      | Use                                                                                                                                                         |
   | --------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Core                        | Access Token Lifetime (seconds)                              | `360000`                                                                                                                                                    |
   | Advanced                    | Additional Audience Values                                   | `https://gateway.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token``https://gateway.example.com:8443/am/oauth2/realms/root/realms/alpha/par` |
   |                             | Client Registration Scope Allowlist                          | Keep only `openid`.                                                                                                                                         |
   |                             | Default Client Scopes                                        | Remove the default settings and leave this empty.                                                                                                           |
   |                             | OAuth2 Token Signing Algorithm                               | `PS256`                                                                                                                                                     |
   |                             | Trusted TLS Client Certificate Header                        | `ssl-client-cert`                                                                                                                                           |
   |                             | Require exp claim in Request Object                          | Enable this setting.                                                                                                                                        |
   |                             | Require nbf claim in Request Object                          | Enable this setting.                                                                                                                                        |
   |                             | Max nbf and exp difference                                   | `60`                                                                                                                                                        |
   | Client Dynamic Registration | Require Software Statement for Dynamic Client Registration   | Enable this setting.                                                                                                                                        |
   |                             | Required Software Statement Attested Attributes              | Remove the default settings and leave this empty.                                                                                                           |
   | OpenID Connect              | ID Token Signing Algorithms supported                        | Keep only `PS256`.                                                                                                                                          |
   |                             | Supported Claims                                             | `acr`                                                                                                                                                       |
   | Advanced OpenID Connect     | Enable "claims\_parameter\_supported"                        | Enable this setting.                                                                                                                                        |
   |                             | Request Parameter Signing Algorithms Supported               | Keep only `PS256`.                                                                                                                                          |
   |                             | Supported Token Endpoint JWS Signing Algorithms              | Keep only `PS256`.                                                                                                                                          |
   |                             | UserInfo Signing Algorithms Supported                        | Set to `ES256` and `PS256`.                                                                                                                                 |
   |                             | Token Introspection Response Signing Algorithms Supported    | Keep only `PS256`.                                                                                                                                          |
   |                             | Authorization Response Signing Algorithms Supported          | Keep only `PS256`.                                                                                                                                          |
   | Consent                     | Allow Clients to Skip Consent                                | Disable this setting.                                                                                                                                       |
   |                             | Remote Consent Service Request Signing Algorithms Supported  | Keep only `PS256`.                                                                                                                                          |
   |                             | Remote Consent Service Response Signing Algorithms Supported | Keep only `PS256`.                                                                                                                                          |

You have successfully configured the OpenID provider services to support FAPI.

## Validation service

1. In the Advanced Identity Cloud admin UI, click [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management to open the AM admin UI.

2. Go to Services > Validation Service, add the following Valid goto URL Resources setting, and click Save Changes:

   `https://gateway.example.com:8443/am/*`\
   `https://gateway.example.com:8443/am/*?*`

You have successfully configured the validation service to support FAPI.

## Create an OAuth 2.0 client account

PingGateway uses this account to get access tokens to read API client information.

1. In the Advanced Identity Cloud admin UI, go to [icon: apps, set=material, size=inline] Applications > [icon: plus, set=fa]Custom Application.

2. Select OIDC - OpenID Connect and click Next.

3. Select Service and click Next.

4. Use the hints in the following table to create the OAuth 2.0 client account:

   | Field                  | Description                                                                 | Example                                                                           |
   | ---------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
   | Name                   | A unique name for the OAuth 2.0 client account.                             | `gateway-oauth2-client`                                                           |
   | Owners                 | The application owner to contact about this OAuth 2.0 client account.       | `gateway-idm-user`                                                                |
   | Client Secret          | A strong password for PingGateway to connect as a resource server.          | `password` (base64-encoding: `cGFzc3dvcmQ=`)                                      |
   | Sign On > Sign-in URLs | The redirect endpoint.                                                      | `https://httpbin.org/anything`                                                    |
   | Sign On > Grant Types  | The OAuth 2.0 grant types PingGateway uses to connect as a resource server. | `Authorization Code`, `Client Credentials`, `Resource Owner Password Credentials` |
   | Sign On > Scopes       | The OAuth 2.0 grant types PingGateway uses to connect as a resource server. | `dynamic_client_registration`, `trusted_gateway`                                  |

   In production deployments, use a secret store to manage the client secret.

5. Click Save.

You have successfully created the OAuth 2.0 client account for PingGateway.

---

---
title: Configuring CORS for FAPI
description: Configure CORS in PingOne Advanced Identity Cloud to allow cross-domain requests from PingGateway when using FAPI
component: pinggateway
version: 2026
page_id: pinggateway:fapi:cors
canonical_url: https://docs.pingidentity.com/pinggateway/2026/fapi/cors.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-09-08T17:46:50Z
---

# Configuring CORS for FAPI

FAPI clients make their requests through PingGateway. This includes requests to authenticate end users in the process of getting an ID token. The end user authenticates through the PingOne Advanced Identity Cloud end-user UI. End-user authentication involves a cross-domain request from the PingGateway domain to the PingOne Advanced Identity Cloud domain.

[Cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) lets user-agents make cross-domain server requests. Follow these steps to allow cross-domain requests from PingGateway to PingOne Advanced Identity Cloud:

1. Sign on to the Advanced Identity Cloud admin UI as an administrator.

2. [Create a custom CORS configuration](https://docs.pingidentity.com/pingoneaic/tenants/configure-cors.html#create-a-new-cors-configuration) with the following settings.

   |   |                                                  |
   | - | ------------------------------------------------ |
   |   | CORS configurations apply for all tenant realms. |

   | Setting                                        | Use                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Name                                           | `FAPI`                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | Accepted Origins                               | The PingGateway endpoint, such as `https://gateway.example.com:8443`                                                                                                                                                                                                                                                                                                                                                                                           |
   | Accepted Methods                               | `DELETE` `FETCH` `GET` `OPTIONS` `PATCH` `POST` `PUT`                                                                                                                                                                                                                                                                                                                                                                                                          |
   | Accepted Headers                               | The Cookie name for your tenant (`iPlanetDirectoryPro` by default for self-hosted AM) `accept-api-version` `accept-encoding` `accept-language` `accept` `authority` `authorization` `content-type` `cookie` `method` `path` `referer` `scheme` `sec-ch-ua-mobile` `sec-ch-ua-platform` `sec-ch-ua` `sec-fetch-dest` `sec-fetch-mode` `sec-fetch-site` `sec-fetch-user` `upgrade-insecure-requests` `user-agent` `x-forgerock-transactionid` `x-requested-with` |
   | Exposed Headers (under Show advanced settings) | `access-control-allow-origin` `cache-control` `content-api-version` `content-language` `content-length` `content-type` `date` `etag` `expires` `last-modified` `pragma` `set-cookie` `strict-transport-security` `x-content-type-options` `x-forgerock-transactionid` `x-frame-options`                                                                                                                                                                        |

3. Click Save CORS Configuration.

You have successfully configured CORS for FAPI.

---

---
title: Configuring identity management for FAPI
description: "Configure PingOne Advanced Identity Cloud identity management for FAPI: create a service account, update the OAuth 2.0 client, and add managed object types"
component: pinggateway
version: 2026
page_id: pinggateway:fapi:aic-idm
canonical_url: https://docs.pingidentity.com/pinggateway/2026/fapi/aic-idm.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-09-08T17:46:50Z
section_ids:
  create_a_user_account: Create a user account
  update_the_pinggateway_oauth_2_0_client: Update the PingGateway OAuth 2.0 client
  prepare_the_update: Prepare the update
  update_the_managed_object_configuration: Update the managed object configuration
  validation: Validation
---

# Configuring identity management for FAPI

FAPI requires additional managed object types to store API client information.

This page explains how to add the managed object types over REST using a PingOne Advanced Identity Cloud service account. Although it's possible to add managed object types through the Advanced Identity Cloud admin UI, using the REST API is less error-prone.

## Create a user account

Create a PingGateway user account with the Advanced Identity Cloud identity management service. This account has administrative access to the identity management service. It lets PingGateway access FAPI client information to verify digital signatures.

1. In the Advanced Identity Cloud admin UI, go to [icon: open_in_new, set=material, size=inline] Native Consoles > Identity Management > to open the IDM admin console.

2. Go to Manage Users > [icon: plus, set=fa]New Alpha realm - User and create the user account:

   | Field         | Description                                                                                          | Example                                           |
   | ------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
   | Username      | PingGateway uses this account to access API client profiles in the identity management service.      | `gateway-idm-user`                                |
   | First Name    | The account schema requires a first name.                                                            | `PingGateway`                                     |
   | Last Name     | The account schema requires a last name.                                                             | `Service Account`                                 |
   | Email address | The account schema requires an email address.                                                        | Your email address                                |
   | Password      | A strong password.Record the password as `gateway.idm.password` to use when configuring PingGateway. | `Secret12!` (base64-encoding: `U2VjcmV0MTIhCg==`) |

3. Click Save to display the new user account.

4. Click the Authorization Roles > [icon: plus, set=fa]Add Authorization Roles, assign the `openidm-admin` role to the service account, and click Add.

   This role lets PingGateway read API client information.

You have successfully created the identity management user account for PingGateway.

## Update the PingGateway OAuth 2.0 client

PingGateway uses the client account created during [access management configuration](aic-am.html#create-oauth2-client) for calls to identity management service APIs. This requires the client account to have the `fr:idm:*` scope.

1. In the Advanced Identity Cloud admin UI, go to [icon: web_asset, set=material, size=inline] OAuth2 Clients > gateway-oauth2-client > Sign On > General Settings.

2. In Scopes, add `fr:idm:*`.

3. Click Save.

You have successfully updated the OAuth 2.0 client account for PingGateway.

## Prepare the update

PingOne Advanced Identity Cloud holds the managed object type configuration as a single JSON array of all managed object types.

To update the configuration, you'll add your definitions to the array and replace the JSON resource. Don't do this while someone else is changing the managed object type configuration.

1. Get an access token with scope `fr:idm:*` using the Resource Owner Password Credentials grant and the OAuth 2.0 client and identity management user accounts:

   ```console
   $ curl \
   --request POST \
   --user 'gateway-oauth2-client:password' \
   --data 'grant_type=password' \
   --data 'username=gateway-idm-user' \
   --data 'password=Secret12!' \
   --data 'scope=fr:idm:*' \
   'https://myTenant.forgeblocks.com/am/oauth2/realms/root/realms/alpha/access_token'
   ```

2. Use the access token to get the current managed object configuration as a JSON file:

   ```console
   $ curl \
   --request GET \
   --header 'Authorization: Bearer <access-token>' \
   --header 'Content-Type: application/json' \
   --header 'Content-Api-Version: protocol=2.1,resource=1.0' \
   --output managed.json \
   'https://myTenant.forgeblocks.com/openidm/config/managed'
   ```

   The command saves the configuration as `managed.json` in the current folder.

3. In a text editor with support for JSON files, open the `managed.json` file.

4. Copy the following JSON objects to the `"objects"` array, taking care to add commas between objects.

   > **Collapse: apiClient.json**
   >
   > (Source: [apiClient.json](../_attachments/others/apiClient.json))
   >
   > ```json
   > {
   >   "iconClass": "fa fa-database",
   >   "name": "apiClient",
   >   "onRead": {
   >     "globals": {},
   >     "source": "if (object.softwareId == null) {\n  object.softwareId = object.id\n}",
   >     "type": "text/javascript"
   >   },
   >   "schema": {
   >     "$schema": "http://forgerock.org/json-schema#",
   >     "description": "FAPI apiClient",
   >     "icon": "fa-cogs",
   >     "mat-icon": null,
   >     "order": [
   >       "_id",
   >       "softwareId",
   >       "name",
   >       "description",
   >       "deleted",
   >       "logoUri",
   >       "jwksUri",
   >       "ssa",
   >       "apiClientOrg",
   >       "oauth2ClientId"
   >     ],
   >     "properties": {
   >       "_id": {
   >         "deleteQueryConfig": false,
   >         "description": null,
   >         "isVirtual": false,
   >         "searchable": true,
   >         "title": "IDM Internal ID",
   >         "type": "string",
   >         "userEditable": true,
   >         "viewable": true
   >       },
   >       "apiClientOrg": {
   >         "deleteQueryConfig": false,
   >         "description": null,
   >         "isVirtual": false,
   >         "notifySelf": false,
   >         "properties": {
   >           "_ref": {
   >             "type": "string"
   >           },
   >           "_refProperties": {
   >             "properties": {
   >               "_id": {
   >                 "propName": "_id",
   >                 "required": false,
   >                 "type": "string"
   >               }
   >             },
   >             "type": "object"
   >           }
   >         },
   >         "referencedObjectFields": null,
   >         "referencedRelationshipFields": null,
   >         "requiredByParent": false,
   >         "resourceCollection": [
   >           {
   >             "label": "apiClientorg",
   >             "notify": false,
   >             "path": "managed/apiClientOrg",
   >             "query": {
   >               "fields": [
   >                 "id",
   >                 "name"
   >               ],
   >               "queryFilter": "true",
   >               "sortKeys": []
   >             }
   >           }
   >         ],
   >         "returnByDefault": false,
   >         "reversePropertyName": "apiClients",
   >         "reverseRelationship": true,
   >         "searchable": false,
   >         "title": "API Client Organization",
   >         "type": "relationship",
   >         "userEditable": false,
   >         "validate": false,
   >         "viewable": true
   >       },
   >       "deleted": {
   >         "default": false,
   >         "description": "Has the ApiClient record been deleted",
   >         "isVirtual": false,
   >         "searchable": true,
   >         "title": "Deleted",
   >         "type": "boolean",
   >         "userEditable": true,
   >         "viewable": true
   >       },
   >       "description": {
   >         "searchable": true,
   >         "title": "Description",
   >         "type": "string",
   >         "userEditable": true,
   >         "viewable": true
   >       },
   >       "id": {
   >         "deleteQueryConfig": false,
   >         "description": null,
   >         "isVirtual": false,
   >         "searchable": true,
   >         "title": "API Client ID",
   >         "type": "string",
   >         "userEditable": true,
   >         "viewable": true
   >       },
   >       "jwks": {
   >         "searchable": false,
   >         "title": "JWK Set",
   >         "type": "object",
   >         "userEditable": false,
   >         "viewable": true
   >       },
   >       "jwksUri": {
   >         "searchable": true,
   >         "title": "JWKS URI",
   >         "type": "string",
   >         "userEditable": true,
   >         "viewable": true
   >       },
   >       "logoUri": {
   >         "searchable": true,
   >         "title": "Logo URI",
   >         "type": "string",
   >         "userEditable": true,
   >         "viewable": true
   >       },
   >       "name": {
   >         "searchable": true,
   >         "title": "API Client Name",
   >         "type": "string",
   >         "userEditable": true,
   >         "viewable": true
   >       },
   >       "oauth2ClientId": {
   >         "deleteQueryConfig": false,
   >         "description": "OAuth2 Client ID",
   >         "isVirtual": false,
   >         "searchable": true,
   >         "title": "OAuth2 Client ID",
   >         "type": "string",
   >         "userEditable": true,
   >         "viewable": true
   >       },
   >       "roles": {
   >         "items": {
   >           "type": "string"
   >         },
   >         "searchable": false,
   >         "title": "Roles",
   >         "type": "array",
   >         "userEditable": true,
   >         "viewable": true
   >       },
   >       "softwareId": {
   >         "deleteQueryConfig": false,
   >         "description": null,
   >         "isVirtual": false,
   >         "searchable": true,
   >         "title": "Software ID",
   >         "type": "string",
   >         "userEditable": true,
   >         "viewable": true
   >       },
   >       "ssa": {
   >         "description": null,
   >         "isVirtual": false,
   >         "minLength": null,
   >         "searchable": true,
   >         "title": "Software Statement Assertion",
   >         "type": "string",
   >         "userEditable": true,
   >         "viewable": true
   >       }
   >     },
   >     "required": [
   >       "name",
   >       "oauth2ClientId",
   >       "ssa",
   >       "deleted"
   >     ],
   >     "title": "apiClient",
   >     "type": "object"
   >   },
   >   "type": "Managed Object"
   > }
   > ```

   > **Collapse: apiClientOrg.json**
   >
   > (Source: [apiClientOrg.json](../_attachments/others/apiClientOrg.json))
   >
   > ```json
   > {
   >   "iconClass": "fa fa-database",
   >   "name": "apiClientOrg",
   >   "schema": {
   >     "$schema": "http://forgerock.org/json-schema#",
   >     "description": "apiClientOrg Details",
   >     "icon": "fa-bank",
   >     "mat-icon": "",
   >     "order": [
   >       "name",
   >       "id",
   >       "created",
   >       "_id",
   >       "apiClients"
   >     ],
   >     "properties": {
   >       "_id": {
   >         "description": null,
   >         "isVirtual": false,
   >         "minLength": null,
   >         "searchable": false,
   >         "title": "Internal IDM Identifier",
   >         "type": "string",
   >         "userEditable": false,
   >         "viewable": true
   >       },
   >       "apiClients": {
   >         "deleteQueryConfig": false,
   >         "description": null,
   >         "isVirtual": false,
   >         "items": {
   >           "notifySelf": false,
   >           "properties": {
   >             "_ref": {
   >               "type": "string"
   >             },
   >             "_refProperties": {
   >               "properties": {
   >                 "_id": {
   >                   "propName": "_id",
   >                   "required": false,
   >                   "type": "string"
   >                 }
   >               },
   >               "type": "object"
   >             }
   >           },
   >           "resourceCollection": [
   >             {
   >               "label": "apiClient",
   >               "notify": false,
   >               "path": "managed/apiClient",
   >               "query": {
   >                 "fields": [],
   >                 "queryFilter": "true",
   >                 "sortKeys": []
   >               }
   >             }
   >           ],
   >           "reversePropertyName": "apiClientOrg",
   >           "reverseRelationship": true,
   >           "type": "relationship",
   >           "validate": false
   >         },
   >         "minLength": null,
   >         "policies": [],
   >         "referencedObjectFields": null,
   >         "referencedRelationshipFields": null,
   >         "requiredByParent": false,
   >         "returnByDefault": false,
   >         "searchable": false,
   >         "title": "API Clients",
   >         "type": "array",
   >         "userEditable": false,
   >         "viewable": true
   >       },
   >       "created": {
   >         "searchable": true,
   >         "title": "Timestamp",
   >         "type": "string",
   >         "userEditable": true,
   >         "viewable": true
   >       },
   >       "id": {
   >         "deleteQueryConfig": false,
   >         "description": "API Client Organization ID",
   >         "isVirtual": false,
   >         "policies": [
   >           {
   >             "params": {},
   >             "policyId": "unique"
   >           }
   >         ],
   >         "searchable": true,
   >         "title": "API Client Organization ID",
   >         "type": "string",
   >         "userEditable": true,
   >         "viewable": true
   >       },
   >       "name": {
   >         "deleteQueryConfig": false,
   >         "description": "API Client Organization Name",
   >         "isVirtual": false,
   >         "searchable": true,
   >         "title": "API Client Organization Name",
   >         "type": "string",
   >         "userEditable": true,
   >         "viewable": true
   >       }
   >     },
   >     "required": [],
   >     "title": "apiClientOrg",
   >     "type": "object"
   >   },
   >   "type": "Managed Object"
   > }
   > ```

5. Verify the objects are top-level objects in the array and check the JSON is syntactically correct.

6. Save your changes to the `managed.json` file.

## Update the managed object configuration

To update the configuration, replace the JSON resource with the JSON from the `managed.json` file.

1. If the access token has expired, use the PingOne Advanced Identity Cloud service account to get a new access token with scope `fr:idm:*`.

2. Use the access token to update the managed object configuration with the JSON file you prepared:

   ```console
   $ curl \
   --request PUT \
   --header 'Authorization: Bearer <access-token>' \
   --header 'Content-Type: application/json' \
   --header 'Content-Api-Version: protocol=2.1,resource=1.0' \
   --data @managed.json \
   'https://myTenant.forgeblocks.com/openidm/config/managed'
   ```

   PingOne Advanced Identity Cloud returns the JSON resource for the updated managed object configuration.

## Validation

Review your updates through the Advanced Identity Cloud admin UI.

1. Sign on to the Advanced Identity Cloud admin UI as an administrator.

2. Go to [icon: open_in_new, set=material, size=inline] Native Consoles > Identity Management > [icon: wrench, set=fa]Configure > Managed Objects.

3. Find your new managed object types in the list:

   ![apiClient and apiClientOrg managed object types](_images/new-managed-object-types.png)

You have successfully added the managed object types to store API client and API client organization objects.

---

---
title: Configuring PingGateway for FAPI
description: Configure PingGateway as a reverse proxy and resource server to enforce FAPI compliance, protecting authorization server endpoints and resource APIs
component: pinggateway
version: 2026
page_id: pinggateway:fapi:gateway
canonical_url: https://docs.pingidentity.com/pinggateway/2026/fapi/gateway.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-23T12:00:00Z
section_ids:
  advanced_identity_cloud_configuration: Advanced Identity Cloud configuration
  before_you_begin: Before you begin
  oauth_2_0_client_accounts: OAuth 2.0 client accounts
  pinggateway_configuration: PingGateway configuration
  base_configuration: Base configuration
  routes_to_protect_the_authorization_server: Routes to protect the authorization server
  resource_server_routes: Resource server routes
  default_route: Default route
---

# Configuring PingGateway for FAPI

To support FAPI, PingGateway plays the role of reverse proxy for the Advanced Identity Cloud authorization server and the role of resource server for protected applications.

PingGateway uses the accounts and routes described here to connect to and protect Advanced Identity Cloud, lets FAPI clients register dynamically, and protects resources for sensitive applications.

## Advanced Identity Cloud configuration

### Before you begin

1. Sign on to the Advanced Identity Cloud admin UI as an administrator.

2. Switch to the realm you use for FAPI.

   This tutorial uses the `alpha` realm. Adapt the realm name to your deployment.

### OAuth 2.0 client accounts

Create as many OAuth 2.0 client accounts as needed for the resource server roles PingGateway plays.

In this tutorial, PingGateway acts as a resource server only as an example, so use the account you created when [configuring access management](aic-am.html#create-oauth2-client).

## PingGateway configuration

The PingGateway routes for FAPI depend on definitions in `config.json`.

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you plan to deploy FAPI components on Kubernetes using Helm, follow the instructions in [Deploy FAPI with Kubernetes and Helm](kubernetes.html) instead.This feature requires PingGateway 2026.6 or later. |

Adapt these settings as necessary for your deployment. In particular, this tutorial uses a sample trusted directory service. In production deployments, use your FAPI ecosystem's official trusted directory service, such as the [Open Banking Directory](https://www.openbanking.org.uk/directory/), for example.

### Base configuration

1. Prepare keys for PingGateway server-side TLS.

   For server-side TLS, HTTPS clients must trust the PingGateway certificate. You can use a CA or generate your own keys as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   The following example generates a TLS key pair in a keystore named `secrets/keystore.p12` and exports the PingGateway self-signed certificate as `secrets/gateway.pem`:

   ```bash
   touch secrets/keystore.pin
   chmod 600 secrets/keystore.pin
   echo -n password > secrets/keystore.pin

   keytool -keystore secrets/keystore.p12 -storetype PKCS12 \
           -genkeypair -alias ssl-key-pair -dname "CN=Gateway TLS keys" \
           -keyalg RSA -keysize 2048 -validity 3650 -ext "san=dns:gateway.example.com" \
           -storepass:file secrets/keystore.pin \
           -keypass:file secrets/keystore.pin

   keytool -keystore secrets/keystore.p12 -storetype PKCS12 \
           -exportcert -alias ssl-key-pair -rfc -file secrets/gateway.pem -storepass:file secrets/keystore.pin
   ```

   Adjust the hostname in `-ext "san=dns:gateway.example.com"` to match your deployment.

2. Add an `admin.json` file such as the following to use the TLS keys, adapting the port numbers and secrets to match the deployment:

   > **Collapse: FAPI**
   >
   > (Source: [admin-fapi.json](../_attachments/config/admin-fapi.json))
   >
   > ```json
   > {
   >   "mode": "DEVELOPMENT",
   >   "heap": [
   >     {
   >       "name": "TlsConf",
   >       "type": "ServerTlsOptions",
   >       "config": {
   >         "clientAuth": "REQUEST",
   >         "keyManager": {
   >           "type": "SecretsKeyManager",
   >           "config": {
   >             "signingSecretId": "key.manager.secret.id",
   >             "secretsProvider": "KeyStoreSecretStore"
   >           }
   >         },
   >         "trustManager": {
   >           "type": "SecretsTrustManager",
   >           "config": {
   >             "verificationSecretId": "trust.manager.secret.id",
   >             "secretsProvider": "KeyStoreSecretStore"
   >           }
   >         }
   >       }
   >     },
   >     {
   >       "name": "KeyStoreSecretStore",
   >       "type": "KeyStoreSecretStore",
   >       "config": {
   >         "file": "&{ig.instance.dir}/../secrets/keystore.p12",
   >         "storePasswordSecretId": "keystore.pin",
   >         "secretsProvider": {
   >           "type": "FileSystemSecretStore",
   >           "config": {
   >             "directory": "&{ig.instance.dir}/../secrets/",
   >             "format": "PLAIN"
   >           }
   >         },
   >         "mappings": [
   >           {
   >             "secretId": "key.manager.secret.id",
   >             "aliases": [
   >               "ssl-key-pair"
   >             ]
   >           },
   >           {
   >             "secretId": "trust.manager.secret.id",
   >             "aliases": [
   >               "ca"
   >             ]
   >           }
   >         ]
   >       }
   >     }
   >   ],
   >   "connectors": [
   >     {
   >       "port": 8080,
   >       "vertx": {
   >         "maxInitialLineLength": 8192,
   >         "maxTotalHeadersSize": 24576
   >       }
   >     },
   >     {
   >       "port": 8443,
   >       "tls": "TlsConf",
   >       "vertx": {
   >         "maxInitialLineLength": 8192,
   >         "maxTotalHeadersSize": 24576
   >       }
   >     }
   >   ],
   >   "adminConnector": {
   >     "port": 9443,
   >     "host": "localhost",
   >     "tls": "TlsConf"
   >   }
   > }
   > ```

3. Add a `config.json` file with these settings, adapting the Advanced Identity Cloud tenant hostname and other properties to your deployment:

   > **Collapse: FAPI**
   >
   > (Source: [config-fapi.json](../_attachments/config/config-fapi.json))
   >
   > ```json
   > {
   >   "properties": {
   >     "asHostname": "myTenant.forgeblocks.com",
   >     "gatewayOAuth2ClientId": "gateway-oauth2-client",
   >     "gatewayIdmUsername": "gateway-idm-user",
   >     "realm": "alpha",
   >     "tenantHostname": "myTenant.forgeblocks.com",
   >     "trustedDirectoryJwksUrl": "http://trustdir.example.com:9080/api/directory/jwks"
   >   },
   >   "handler": "_router",
   >   "heap": [
   >     {
   >       "name": "_router",
   >       "type": "Router",
   >       "config": {
   >         "directory": "${openig.configDirectory}/routes",
   >         "defaultHandler": {
   >           "type": "DispatchHandler",
   >           "config": {
   >             "bindings": [
   >               {
   >                 "condition": "${request.method == 'GET' and request.uri.path == '/'}",
   >                 "handler": {
   >                   "type": "WelcomeHandler"
   >                 }
   >               },
   >               {
   >                 "condition": "${request.uri.path == '/'}",
   >                 "handler": {
   >                   "type": "StaticResponseHandler",
   >                   "config": {
   >                     "status": 405,
   >                     "reason": "Method Not Allowed"
   >                   }
   >                 }
   >               },
   >               {
   >                 "handler": {
   >                   "type": "StaticResponseHandler",
   >                   "config": {
   >                     "status": 404,
   >                     "reason": "Not Found"
   >                   }
   >                 }
   >               }
   >             ]
   >           }
   >         }
   >       }
   >     },
   >     {
   >       "name": "capture",
   >       "type": "CaptureDecorator",
   >       "config": {
   >         "captureEntity": true
   >       }
   >     },
   >     {
   >       "name": "PlatformReverseProxyHandler",
   >       "comment": "Add a transaction ID header for calls to platform services",
   >       "type": "Chain",
   >       "config": {
   >         "filters": [
   >           "TransactionIdOutboundFilter"
   >         ],
   >         "handler": "ReverseProxyHandler"
   >       }
   >     },
   >     {
   >       "name": "SystemAndEnvSecretStore",
   >       "type": "SystemAndEnvSecretStore"
   >     },
   >     {
   >       "name": "IdmClientHandler",
   >       "type": "Chain",
   >       "config": {
   >         "filters": [
   >           {
   >             "type": "ResourceOwnerOAuth2ClientFilter",
   >             "config": {
   >               "tokenEndpoint": "https://&{tenantHostname}/am/oauth2/realms/root/realms/&{realm}/access_token",
   >               "username": "&{gatewayIdmUsername}",
   >               "passwordSecretId": "gateway.idm.password",
   >               "secretsProvider": "SystemAndEnvSecretStore",
   >               "scopes": [
   >                 "fr:idm:*"
   >               ],
   >               "endpointHandler": {
   >                 "type": "Chain",
   >                 "config": {
   >                   "handler": "ForgeRockClientHandler",
   >                   "filters": [
   >                     {
   >                       "type": "ClientSecretBasicAuthenticationFilter",
   >                       "config": {
   >                         "clientId": "&{gatewayOAuth2ClientId}",
   >                         "clientSecretId": "gateway.oauth2.client.secret",
   >                         "secretsProvider": "SystemAndEnvSecretStore"
   >                       }
   >                     }
   >                   ]
   >                 }
   >               }
   >             }
   >           }
   >         ],
   >         "handler": "ForgeRockClientHandler"
   >       }
   >     },
   >     {
   >       "name": "JwkSetService",
   >       "type": "CachingJwkSetService",
   >       "config": {
   >         "cacheMaxSize": 500,
   >         "cacheTimeout": "24 hours"
   >       }
   >     },
   >     {
   >       "name": "TrustedDirectoryService",
   >       "type": "TrustedDirectoryService",
   >       "config": {
   >         "trustedDirectories": [
   >           "TestTrustedDirectory"
   >         ]
   >       }
   >     },
   >     {
   >       "name": "TestTrustedDirectory",
   >       "type": "TrustedDirectory",
   >       "config": {
   >         "issuer": "PingGateway Sample Trusted Directory",
   >         "softwareStatementClaims": {
   >           "organisationIdClaimName": "org_id",
   >           "organisationNameClaimName": "org_name",
   >           "softwareIdClaimName": "software_id",
   >           "clientNameClaimName": "software_client_name",
   >           "redirectUrisClaimName": "software_redirect_uris",
   >           "rolesClaimName": "software_roles",
   >           "_comment": "If your clients publish JWKs, use jwksUriClaimName instead of jwksClaimName.",
   >           "jwksClaimName": "software_jwks"
   >         },
   >         "secretsProvider": {
   >           "type": "SecretsProvider",
   >           "config": {
   >             "stores": [
   >               {
   >                 "type": "JwkSetSecretStore",
   >                 "config": {
   >                   "jwkUrl": "&{trustedDirectoryJwksUrl}"
   >                 }
   >               }
   >             ]
   >           }
   >         }
   >       }
   >     },
   >     {
   >       "name": "IdmService",
   >       "type": "IdmService",
   >       "config": {
   >         "baseEndpoint": "https://&{tenantHostname}/openidm",
   >         "endpointHandler": "IdmClientHandler"
   >       }
   >     },
   >     {
   >       "name": "IdmApiClientService",
   >       "type": "IdmApiClientService",
   >       "config": {
   >         "idmService": "IdmService",
   >         "jwkSetService": "JwkSetService"
   >       }
   >     },
   >     {
   >       "name": "IdmApiClientOrganisationService",
   >       "type": "IdmApiClientOrganisationService",
   >       "config": {
   >         "idmService": "IdmService"
   >       }
   >     },
   >     {
   >       "name": "AsJwkSecretsProvider",
   >       "type": "SecretsProvider",
   >       "config": {
   >         "stores": [
   >           {
   >             "type": "JwkSetSecretStore",
   >             "config": {
   >               "jwkUrl": "https://&{tenantHostname}/am/oauth2/realms/root/realms/&{realm}/connect/jwk_uri"
   >             }
   >           }
   >         ]
   >       }
   >     }
   >   ],
   >   "session": {
   >     "type": "JwtSessionManager"
   >   }
   > }
   > ```

   This file includes the settings for the trusted directory and access to Advanced Identity Cloud identity management services. If your clients publish JWKs, use `jwksUriClaimName` instead of `jwksClaimName` in the trusted directory configuration. This example uses `jwksClaimName` and static JWKs for the test client profiles, where the clients aren't publicly accessible.

   Whenever you change this file, restart PingGateway to reload the configuration.

4. Export secrets the PingGateway configuration takes from the environment.

   ```bash
   export GATEWAY_OAUTH2_CLIENT_SECRET='cGFzc3dvcmQ='  # Base64-encoding of `password`
   export GATEWAY_IDM_PASSWORD='U2VjcmV0MTIh'          # Base64-encoding of `Secret12!`
   ```

   These secrets correspond to the following properties in `config.json`:

   * `gateway.oauth2.client.secret` for the OAuth 2.0 client account `gatewayOAuth2ClientId`.

   * `gateway.idm.password` for the identity management user account `gatewayIdmUsername`.

   In production deployments, use a secure secret store.

5. Restart PingGateway to load the new configuration.

You have successfully configured the base settings for PingGateway to support FAPI.

### Routes to protect the authorization server

PingGateway protects access to these Advanced Identity Cloud authorization server endpoints to enforce FAPI compliance:

* The dynamic client registration endpoint (`/oauth2/register`)

* The access token endpoint (`/oauth2/access_token`)

* The Pushed Authorization Request (PAR) endpoint (`/oauth2/par`)

* The authorization endpoint (`/oauth2/authorize`)

* The well-known configuration endpoint (`/.well-known/openid-configuration`)

Each of these corresponds to a PingGateway route for access to the authorization server. Make sure API clients and conformance tests go through these routes, not directly to Advanced Identity Cloud.

To the `routes` folder of the PingGateway configuration:

1. Add a route to ensure compliant registration requests:

   [fapi-20-as-dcr-endpoint.json](../_attachments/config/routes/fapi-20-as-dcr-endpoint.json)

   When using a public trusted directory rather than the sample trusted directory, don't use `allowPingIssuedTestCerts` in the `FapiDcrFilterChain`.

2. Add a route to ensure compliant access token requests:

   [fapi-21-as-token-endpoint.json](../_attachments/config/routes/fapi-21-as-token-endpoint.json)

3. Add a route to ensure compliant PAR requests:

   [fapi-22-as-par-endpoint.json](../_attachments/config/routes/fapi-22-as-par-endpoint.json)

4. Add a route to ensure compliant authorize requests:

   [fapi-23-as-authorize-endpoint.json](../_attachments/config/routes/fapi-23-as-authorize-endpoint.json)

5. Add a route to ensure compliant well-known metadata requests: [fapi-28-as-metadata.json](../_attachments/config/routes/fapi-28-as-metadata.json).

You have successfully configured the routes for PingGateway to protect the Advanced Identity Cloud authorization server.

### Resource server routes

In production systems, as shown in [Deployment](fapi.html#deployment), use a separate PingGateway server with separate routes for each resource server role.

In this tutorial, this PingGateway server also acts as a resource server. You create a resource server route for this role.

1. Add this script to the `scripts/groovy` folder of the PingGateway configuration: [ExampleRsApiResponseHandler.groovy](../_attachments/scripts/ExampleRsApiResponseHandler.groovy).

2. Add this route to the `routes` folder of the PingGateway configuration: [fapi-01-rs-example-protected-api.json](../_attachments/config/routes/fapi-01-rs-example-protected-api.json).

You have successfully configured the resource server route for PingGateway. Create as many routes as needed for the resource server roles PingGateway plays.

### Default route

Add the following default route to the `routes` folder of the PingGateway configuration: [fapi-99-platform-passthrough.json](../_attachments/config/routes/fapi-99-platform-passthrough.json).

This route lets requests like those for end-user sign on pass through unchanged.

---

---
title: Deploy FAPI with Kubernetes and Helm
description: Deploy PingGateway FAPI components on Kubernetes using evaluation Helm charts and Docker images, as an alternative to manual configuration
component: pinggateway
version: 2026
page_id: pinggateway:fapi:kubernetes
canonical_url: https://docs.pingidentity.com/pinggateway/2026/fapi/kubernetes.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-25T00:00:00Z
section_ids:
  prerequisites: Prerequisites
  deploy_the_sample_trusted_directory: Deploy the sample trusted directory
  create_secrets: Create secrets
  install: Install
  configuration_parameters: Configuration parameters
  register: Register
  deploy_the_fapi_pep_as: Deploy the FAPI PEP AS
  create_secrets_2: Create secrets
  install_2: Install
  configuration_parameters_2: Configuration parameters
  deploy_the_fapi_pep_rs: Deploy the FAPI PEP RS
  create_secrets_3: Create secrets
  install_3: Install
  configuration_parameters_3: Configuration parameters
---

# Deploy FAPI with Kubernetes and Helm

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | **This feature requires PingGateway 2026.6 or later.**Ping Identity provides no commercial support for production deployments that use these evaluation-only Docker images and Helm charts.For production, you must build and use your own Docker images and Helm charts. Get the FAPI configuration for Docker images from the evaluation-only images. Download the Helm charts from the Ping Identity Download Center.Learn more about building PingGateway Docker images in [Deploying PingGateway with Docker](../devops-guide/preface.html). |

As an alternative to manual configuration, you can deploy the PingGateway FAPI components on Kubernetes using Helm. Sample Docker images are available at `gcr.io/forgerock-io` for evaluation. Sample Helm charts are included in the product distribution.

When you deploy with Kubernetes and Helm, the Docker images contain static configuration for FAPI. The Helm charts configure PingGateway and the sample trusted directory.

The FAPI deployment uses three Helm charts:

* `ig-fapi-pep-as` — PingGateway acting as a FAPI-compliant reverse proxy for the authorization server

* `ig-fapi-pep-rs` — PingGateway acting as a FAPI-compliant reverse proxy for the resource server

* `sample-trusted-directory` — a sample trusted directory for evaluation and conformance testing

## Prerequisites

* For conformance testing, a Kubernetes cluster accessible over the internet.

* The PingGateway FAPI Helm charts from the [Ping Identity Download Center](https://product-downloads.pingidentity.com/).

  Find additional details in the README files provided with the Helm charts.

* Kubernetes 1.21 or later.

* Helm 3.x.

* An NGINX Ingress Controller with mTLS support (`auth-tls` annotations).

* Access to a container registry that your cluster can pull images from.

  This example pulls the evaluation-only Docker images from `gcr.io`.

## Deploy the sample trusted directory

Use these hints to deploy the sample trusted directory.

### Create secrets

Create the following Kubernetes secrets in your target namespace before installing the chart:

1. Generate a key store for the sample trusted directory and export certificates for trust stores.

   Find an example in [Run the sample trusted directory](trusted-directory.html#fapi-run-sample-td). The example uses `changeit` as the key store password and key password in all cases.

   The key store must contain two key aliases: `jwt-signer` for signing JWTs, and `ca` for signing transport certificates.

2. Create the key store secret:

   ```bash
   kubectl create secret generic sample-trusted-directory-keystore \
     --from-file=sample-trusted-directory-keystore.p12=/path/to/trusted-directory/secrets/trusted-directory-keystore.p12 \
     -n <namespace>
   ```

3. Create the TLS certificate secret:

   ```bash
   kubectl create secret tls sample-trusted-directory-tls-cert \
     --cert=/path/to/tls.crt \
     --key=/path/to/tls.key \
     -n <namespace>
   ```

4. Create the mTLS CA certificates secret:

   ```bash
   kubectl create secret generic sample-trusted-directory-mtls-ca-certs \
     --from-file=ca.crt=/path/to/ca-bundle.crt \
     -n <namespace>
   ```

### Install

```bash
helm install sample-trusted-directory ./openig-helm/sample-trusted-directory \
  --namespace <namespace> \
  --set config.fqdn=trustdir.example.com \
  --set config.ca.keystoreKeyPwd=Y2hhbmdlaXQ= \
  --set config.ca.keystorePwd=Y2hhbmdlaXQ= \
  --set config.signing.keystoreKeyPwd=Y2hhbmdlaXQ= \
  --set config.signing.keystorePwd=Y2hhbmdlaXQ= \
  --set deployment.image.repo=gcr.io/forgerock-io/ig-sample-trusted-directory:2026.6.0 \
  --set ingress.host=trustdir.example.com \
  --set ingress.tls.host=trustdir.example.com
```

Keystore passwords must be Base64-encoded. Use `echo -n 'your-password' | base64` to encode them. This example uses `Y2hhbmdlaXQ=`, the base64-encoded form of `changeit`.

### Configuration parameters

**Sample trusted directory configuration**

| Parameter                       | Description                                             | Default          |
| ------------------------------- | ------------------------------------------------------- | ---------------- |
| `config.fqdn`                   | Fully-qualified domain name used in issued certificates | `replace-me`     |
| `config.issuerName`             | Name used as the JWT issuer                             | `test-publisher` |
| `config.ca.keystoreAlias`       | Alias of the CA key in the keystore                     | `ca`             |
| `config.ca.keystoreKeyPwd`      | Base64-encoded password for the CA private key          | `replace-me`     |
| `config.ca.keystorePwd`         | Base64-encoded password for the keystore                | `replace-me`     |
| `config.signing.keystoreAlias`  | Alias of the JWT signing key in the keystore            | `jwt-signer`     |
| `config.signing.keystoreKeyPwd` | Base64-encoded password for the signing private key     | `replace-me`     |
| `config.signing.keystorePwd`    | Base64-encoded password for the keystore                | `replace-me`     |
| `config.cert.keySize`           | RSA key size in bits for generated certificates         | `4096`           |
| `config.cert.validityDays`      | Validity period in days for generated certificates      | `365`            |
| `deployment.image.repo`         | Container image repository (required)                   | —                |
| `persistence.enabled`           | Enable a PersistentVolumeClaim to survive pod restarts  | `true`           |
| `persistence.size`              | PVC storage size                                        | `100Mi`          |

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When `persistence.enabled` is `false`, the JWKS file is stored on the container's ephemeral filesystem and is lost on every pod restart. All previously registered software statements become invalid. |

### Register

With the sample trusted directory running, register it with the AS and register API clients with it:

* [Register the sample trusted directory](trusted-directory.html#fapi-register-td)

* [Register the API clients](trusted-directory.html#api-clients)

## Deploy the FAPI PEP AS

The FAPI PEP AS acts as a FAPI-compliant reverse proxy for the authorization server. It enforces dynamic client registration (DCR), token, PAR, and authorize endpoints.

Use these hints to deploy the FAPI PEP AS.

### Create secrets

Create the following Kubernetes secrets before installing the chart:

1. Create a PEM trust store secret to trust the sample trusted directory:

   ```bash
   kubectl create secret generic ig-truststore-pem \
     --from-file=ig-truststore.pem=/path/to/trusted-directory/secrets/trusted-directory-ca.pem \
     -n <namespace>
   ```

   If the AS and platform services certificates aren't signed by a well-known CA, include their CA certificates in this trust store.

2. Create the TLS certificate secrets:

   ```bash
   # Standard TLS ingress
   kubectl create secret tls fapi-pep-as-tls-cert \
     --cert=/path/to/tls.crt \
     --key=/path/to/tls.key \
     -n <namespace>

   # mTLS ingress
   kubectl create secret tls fapi-pep-as-mtls-tls-cert \
     --cert=/path/to/mtls.crt \
     --key=/path/to/mtls.key \
     -n <namespace>
   ```

3. Create the mTLS CA bundle secret:

   ```bash
   kubectl create secret generic fapi-pep-as-mtls-ca-certs \
     --from-file=ca.crt=/path/to/ca-bundle.crt \
     -n <namespace>
   ```

### Install

```bash
helm install ig-fapi-pep-as ./openig-helm/ig-fapi-pep-as \
  --namespace <namespace> \
  --set authorizationServer.fqdn=myTenant.forgeblocks.com \
  --set authorizationServer.mtlsFqdn=myTenant.forgeblocks.com \
  --set authorizationServer.baseFqdn=myTenant.forgeblocks.com \
  --set identityPlatform.fqdn=myTenant.forgeblocks.com \
  --set testDirectory.fqdn=trustdir.example.com \
  --set deployment.image.repo=gcr.io/forgerock-io/ig-fapi-pep-as:2026.6.0 \
  --set pingGateway.oauth2Client.id=Z2F0ZXdheS1vYXV0aDItY2xpZW50 \
  --set pingGateway.oauth2Client.secret=cGFzc3dvcmQ= \
  --set pingGateway.idm.user=Z2F0ZXdheS1pZG0tdXNlcg== \
  --set pingGateway.idm.password=U2VjcmV0MTIhCg==
```

Secret values must be Base64-encoded. Use `echo -n 'your-value' | base64` to encode them. This example uses the values from [Create an OAuth 2.0 client account](aic-am.html#create-oauth2-client) and [Configuring identity management for FAPI](aic-idm.html):

* OAuth 2.0 client ID: `gateway-oauth2-client` (base64-encoding: `Z2F0ZXdheS1vYXV0aDItY2xpZW50`)

* OAuth 2.0 client secret: `password` (base64-encoding: `cGFzc3dvcmQ=`)

* IDM user: `gateway-idm-user` (base64-encoding: `Z2F0ZXdheS1pZG0tdXNlcg==`)

* IDM user password: `Secret12!` (base64-encoding: `U2VjcmV0MTIhCg==`)

### Configuration parameters

**FAPI PEP AS configuration**

| Parameter                         | Description                                                                             | Default                                  |
| --------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------- |
| `authorizationServer.fqdn`        | Public FQDN of the authorization server                                                 | `as.sandbox.pinggateway.com`             |
| `authorizationServer.mtlsFqdn`    | mTLS FQDN of the authorization server                                                   | `as-mtls.sandbox.pinggateway.com`        |
| `authorizationServer.baseFqdn`    | Base domain for the deployment                                                          | `sandbox.pinggateway.com`                |
| `authorizationServer.realm`       | AM realm used in OAuth2 endpoint paths                                                  | `alpha`                                  |
| `identityPlatform.fqdn`           | FQDN of the identity platform (AM/IDM)                                                  | `iam.sandbox.pinggateway.com`            |
| `identityPlatform.type`           | Platform type: `CDK`, `CDM`, or `FIDC`. When `FIDC`, the AIC ConfigMap is also mounted. | `CDK`                                    |
| `identityPlatform.userObject`     | IDM user object name                                                                    | `user`                                   |
| `testDirectory.fqdn`              | FQDN of the test trusted directory                                                      | `test-directory.sandbox.pinggateway.com` |
| `pingGateway.oauth2Client.id`     | Base64-encoded OAuth2 client ID                                                         | `replace-me`                             |
| `pingGateway.oauth2Client.secret` | Base64-encoded OAuth2 client secret                                                     | `replace-me`                             |
| `pingGateway.idm.user`            | Base64-encoded IDM service account username                                             | `replace-me`                             |
| `pingGateway.idm.password`        | Base64-encoded IDM service account password                                             | `replace-me`                             |
| `deployment.image.repo`           | Container image repository (required)                                                   | —                                        |

## Deploy the FAPI PEP RS

The FAPI PEP RS acts as a FAPI-compliant reverse proxy for the resource server. It validates access tokens and enforces scope-based access control.

Use these hints to deploy a FAPI PEP RS for each resource server.

### Create secrets

Create the following Kubernetes secrets before installing the chart:

1. Create a PEM trust store secret to trust the sample trusted directory:

   ```bash
   kubectl create secret generic ig-truststore-pem \
     --from-file=ig-truststore.pem=/path/to/trusted-directory/secrets/trusted-directory-ca.pem \
     -n <namespace>
   ```

   If the AS and platform services certificates aren't signed by a well-known CA, include their CA certificates in this trust store.

2. Create the TLS certificate secrets:

   ```bash
   # Standard TLS ingress
   kubectl create secret tls fapi-pep-rs-core-tls-cert \
     --cert=/path/to/tls.crt \
     --key=/path/to/tls.key \
     -n <namespace>

   # mTLS ingress
   kubectl create secret tls fapi-pep-rs-core-mtls-tls-cert \
     --cert=/path/to/mtls.crt \
     --key=/path/to/mtls.key \
     -n <namespace>
   ```

3. Create the mTLS CA bundle secret:

   ```bash
   kubectl create secret generic fapi-pep-rs-core-mtls-ca-certs \
     --from-file=ca.crt=/path/to/ca-bundle.crt \
     -n <namespace>
   ```

### Install

```bash
helm install ig-fapi-pep-rs ./openig-helm/ig-fapi-pep-rs \
  --namespace <namespace> \
  --set authorizationServer.fqdn=myTenant.forgeblocks.com \
  --set authorizationServer.baseFqdn=myTenant.forgeblocks.com \
  --set identityPlatform.fqdn=myTenant.forgeblocks.com \
  --set resourceServer.fqdn=rs.example.com \
  --set resourceServer.mtlsFqdn=rs-mtls.example.com \
  --set deployment.image.repo=gcr.io/forgerock-io/ig-fapi-pep-rs:2026.6.0 \
  --set resourceServer.oauth2Client.id=Z2F0ZXdheS1vYXV0aDItY2xpZW50) \
  --set resourceServer.oauth2Client.secret=cGFzc3dvcmQ= \
  --set resourceServer.idm.user=Z2F0ZXdheS1pZG0tdXNlcg== \
  --set resourceServer.idm.password=U2VjcmV0MTIhCg==
```

Secret values must be Base64-encoded. Use `echo -n 'your-value' | base64` to encode them. This example uses the values from [Create an OAuth 2.0 client account](aic-am.html#create-oauth2-client) and [Configuring identity management for FAPI](aic-idm.html):

* OAuth 2.0 client ID: `gateway-oauth2-client` (base64-encoding: `Z2F0ZXdheS1vYXV0aDItY2xpZW50`)

* OAuth 2.0 client secret: `password` (base64-encoding: `cGFzc3dvcmQ=`)

* IDM user: `gateway-idm-user` (base64-encoding: `Z2F0ZXdheS1pZG0tdXNlcg==`)

* IDM user password: `Secret12!` (base64-encoding: `U2VjcmV0MTIhCg==`)

### Configuration parameters

**FAPI PEP RS configuration**

| Parameter                            | Description                                 | Default                           |
| ------------------------------------ | ------------------------------------------- | --------------------------------- |
| `authorizationServer.fqdn`           | FQDN of the authorization server            | `as.sandbox.pinggateway.com`      |
| `authorizationServer.baseFqdn`       | Base domain for the deployment              | `sandbox.pinggateway.com`         |
| `authorizationServer.realm`          | AM realm used in OAuth2 endpoint paths      | `alpha`                           |
| `identityPlatform.fqdn`              | FQDN of the identity platform (AM/IDM)      | `iam.sandbox.pinggateway.com`     |
| `identityPlatform.type`              | Platform type: `CDK`, `CDM`, or `FIDC`      | `CDK`                             |
| `resourceServer.fqdn`                | Public FQDN of the resource server          | `rs.sandbox.pinggateway.com`      |
| `resourceServer.mtlsFqdn`            | mTLS FQDN of the resource server            | `rs-mtls.sandbox.pinggateway.com` |
| `resourceServer.oauth2Client.id`     | Base64-encoded OAuth2 client ID             | `replace-me`                      |
| `resourceServer.oauth2Client.secret` | Base64-encoded OAuth2 client secret         | `replace-me`                      |
| `resourceServer.idm.user`            | Base64-encoded IDM service account username | `replace-me`                      |
| `resourceServer.idm.password`        | Base64-encoded IDM service account password | `replace-me`                      |
| `deployment.image.repo`              | Container image repository (required)       | —                                 |

---

---
title: Implementing FAPI with PingGateway
description: Configure PingGateway and PingOne Advanced Identity Cloud for FAPI applications, and run conformance tests to validate your installation
component: pinggateway
version: 2026
page_id: pinggateway:fapi:index
canonical_url: https://docs.pingidentity.com/pinggateway/2026/fapi/index.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-23T12:00:00Z
keywords: ["FAPI", "Security"]
section_ids:
  what_youll_learn: What you'll learn
  before_you_begin: Before you begin
---

# Implementing FAPI with PingGateway

This tutorial shows you how to use PingGateway with PingOne Advanced Identity Cloud for [FAPI](https://openid.net/wg/fapi/) applications.

It isn't intended to cover all nuances and variations of FAPI or how to integrate FAPI into your business. It focuses instead on getting quickly to a functional FAPI environment with a test application you can use to begin the FAPI conformance testing process.

## What you'll learn

* What FAPI is and how PingGateway and PingOne Advanced Identity Cloud support it

* How to configure a PingOne Advanced Identity Cloud tenant to support FAPI

* How to configure PingGateway to support FAPI

* How to use the sample trusted directory to test dynamic client registration

* How to run a basic FAPI conformance test to validate your installation

## Before you begin

|   |                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Unlike other PingGateway tutorials and examples, this tutorial requires deploying PingGateway on a system accessible by DNS.The FAPI conformance tests use DNS to access PingGateway URLs. |

* Get administrator access to a PingOne Advanced Identity Cloud tenant.

* Get a system for PingGateway the conformance tests can access through DNS.

* [Install](../installation-guide/preface.html) PingGateway.

---

---
title: The FAPI trusted directory
description: "Set up a test trusted directory for FAPI conformance testing: run the Docker image, register it in PingOne Advanced Identity Cloud, and register API clients."
component: pinggateway
version: 2026
page_id: pinggateway:fapi:trusted-directory
canonical_url: https://docs.pingidentity.com/pinggateway/2026/fapi/trusted-directory.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T12:00:00Z
section_ids:
  fapi-run-sample-td: Run the sample trusted directory
  update_the_pinggateway_trust_store: Update the PingGateway trust store
  fapi-register-td: Register the sample trusted directory
  api-clients: Register the API clients
  create_an_organization: Create an organization
  create_the_api_clients: Create the API clients
  register_each_api_client: Register each API client
---

# The FAPI trusted directory

In a FAPI-based ecosystem, a central authority operates a *trusted directory*. Although not required for FAPI conformance testing, the trusted directory is [a critical component of the ecosystem](fapi.html#deployment).

The trusted directory records the keys and other metadata for API clients of trusted organizations. The central authority vets the participants and restricts access to trusted organizations and their API clients. Each trusted organization registers its API clients with the trusted directory before registering them with other organizations.

When an API client registers with another organization, the trusted directory ensures only a trusted API clients can do so:

* Each organization configures their authorization server to use the trusted directory.

  When an API client registers dynamically with the authorization server, it presents a signed *software statement* assertion (SSA) from the trusted directory.

  The authorization server validates the software statement including the signature and issuer.

* The software statement from the trusted directory includes the client's keys and other metadata. It vouches for the API client as a trusted participant in the ecosystem.

  The trusted directory issues software statement assertions only to trusted API clients of trusted organizations.

* The trusted directory can revoke an API client's participation in the ecosystem.

Production deployments in FAPI-based ecosystems require the trusted directory. In each participating organization, the authorization server depends on SSAs from the central trusted directory. PingGateway protects dynamic client registration (DCR) requests to the authorization server, allowing only trusted API clients to register.

Make sure you understand the trusted directory's role in API client registration. This page explains how to use the sample trusted directory for this tutorial.

## Run the sample trusted directory

|   |                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you plan to deploy FAPI components on Kubernetes using Helm, generate a keystore for the sample as described in this section, then follow the instructions in [Deploy FAPI with Kubernetes and Helm](kubernetes.html) instead.This feature requires PingGateway 2026.6 or later. |

The sample trusted directory is a Docker image available as `gcr.io/forgerock-io/ig-sample-trusted-directory:2026.6.0`. You can run it locally or in a test environment accessible to PingGateway.

The sample trusted directory requires the following:

* A fully qualified domain name (FQDN).

  If you're running the sample trusted directory locally, add an alias to your hosts file:

  ```none
  127.0.0.1	trustdir.example.com
  ```

* CA keys for TLS and another key pair for signing.

  Generate your own for testing.

* A configuration file for the sample trusted directory.

  Save a configuration file such as the following example as `trusted-directory/config/config.yml`:

  ```yaml
  server:
    port: 8080

  trustedDirectory:
    issuerName: PingGateway Sample Trusted Directory
    fqdn: trustdir.example.com:8080

    signing:
      keystorePath: /var/trusted-directory/secrets/trusted-directory-keystore.p12
      keystoreType: PKCS12
      keyAlias: jwt-signer

    ca:
      keystorePath: /var/trusted-directory/secrets/trusted-directory-keystore.p12
      keystoreType: PKCS12
      keyAlias: ca
      certSigningAlg: SHA256withRSA

    storageFilePath: /var/trusted-directory/data/trusted-directory-jwks.json

    cert:
      keySize: 4096
      validityDays: 365
  ```

  Notice the issuer name is `PingGateway Sample Trusted Directory`. When the sample trusted directory issues a software statement, it uses this issuer name. You'll need it when you register the trusted directory in PingOne Advanced Identity Cloud.

The following sample script runs the sample trusted directory as a Docker container listening on port 9080. It generates the keys in a `./secrets` folder using the `keytool` command on the first run:

```bash
#!/usr/bin/env bash

DOCKER_IMAGE="gcr.io/forgerock-io/ig-sample-trusted-directory:2026.6.0"
SECRETS_DIR="trusted-directory/secrets"
KEYSTORE_FILE="${SECRETS_DIR}/trusted-directory-keystore.p12"

checkForDocker() {
  OUT=$(docker --version)
  RC=$?
  if [ $RC -ne 0 ]; then
      echo "### 'docker' command not found. The sample trusted directory requires Docker to run."
      exit $RC
  else
    echo "Found ${OUT}"
  fi
}

checkForKeytool() {
  OUT=$(keytool --version)
  RC=$?
  if [ $RC -ne 0 ]; then
      echo "### 'keytool' command not found. The sample trusted directory requires keytool to create test keys."
      exit $RC
  else
    echo "Found ${OUT}"
  fi
}

createKeys() {
  echo "### Creating trusted directory keystore ${PWD}/${KEYSTORE_FILE}..."
  echo
  mkdir -p "${SECRETS_DIR}"

  echo "### Generating CA keys..."
  echo
  keytool -keystore "${KEYSTORE_FILE}" -storetype PKCS12 \
          -genkeypair -alias ca -ext bc=ca:true -keyalg RSA -keysize 4096 -validity 365 \
          -dname "CN=PingGateway Sample Trusted Directory Root CA" \
          -storepass changeit -keypass changeit

  echo
  echo "### Generating JWT Signing keys..."
  echo
  keytool -keystore "${KEYSTORE_FILE}" -storetype PKCS12 \
          -genkeypair -alias jwt-signer -keyalg RSA -keysize 4096 -validity 365 \
          -dname "CN=PingGateway Sample Trusted Directory JWT Signer" \
          -storepass changeit -keypass changeit

  echo
  echo "### Listing keystore contents..."
  echo
  keytool -keystore "${KEYSTORE_FILE}" -storetype PKCS12 -list -storepass changeit

  echo
  echo "### Exporting CA certificate..."
  echo
  keytool -exportcert -alias ca -rfc -file "${SECRETS_DIR}/trusted-directory-ca.pem" \
          -keystore "${KEYSTORE_FILE}" -storetype PKCS12 -storepass changeit

  echo
  echo "### Done."
}

initializeDataDir() {
    echo "### Initializing trusted directory data directory..."
    echo
    mkdir -p "${PWD}/trusted-directory/data"
}

runTestTrustedDirectory() {
  echo "### Running sample trusted directory in Docker..."
  echo

  docker pull "${DOCKER_IMAGE}"

  docker run \
  --detach \
  --init \
  --tty \
  --rm \
  --mount type=bind,src="${PWD}/trusted-directory",dst="/var/trusted-directory" \
  --env TD_CONFIG_PATH="/var/trusted-directory/config/config.yml" \
  --env TD_SIGNING_KEYSTORE_PWD=changeit \
  --env TD_SIGNING_KEYSTORE_KEY_PWD=changeit \
  --env TD_CA_KEYSTORE_PWD=changeit \
  --env TD_CA_KEYSTORE_KEY_PWD=changeit \
  --name sample-trusted-directory \
  --publish 9080:8080 \
  "${DOCKER_IMAGE}"
}

checkForDocker

if [ ! -f "${KEYSTORE_FILE}" ]; then
  checkForKeytool
  createKeys
else
  echo "### Sample trusted directory keystore already exists, skipping key creation."
  echo
fi

initializeDataDir

runTestTrustedDirectory
```

You've successfully started the sample trusted directory.

## Update the PingGateway trust store

For mutual TLS, PingGateway must trust the sample trusted directory's CA certificate. The sample trusted directory uses its CA certificate to sign API client TLS certificates.

The following example generates imports the sample trusted directory's CA certificate from a file named `trusted-directory/secrets/trusted-directory-ca.pem` into `secrets/keystore.p12`:

```bash
keytool -keystore secrets/keystore.p12 -storetype PKCS12 \
        -importcert -trustcacerts -alias ca -rfc \
        -file trusted-directory/secrets/trusted-directory-ca.pem -storepass:file secrets/keystore.pin -noprompt
```

## Register the sample trusted directory

In PingOne Advanced Identity Cloud the trusted directory plays the role of a *software publisher*. The authorization server uses a software publisher agent profile with the trusted directory's metadata and keys. It uses the profile to validate and trust software statements (SSAs) the API clients present during registration.

|   |                                                                                                  |
| - | ------------------------------------------------------------------------------------------------ |
|   | In production deployments, use your FAPI ecosystem's official trusted directory service instead. |

1. In the Advanced Identity Cloud admin UI, click [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management to open the AM admin UI.

2. Go to Services > Applications > Software Publisher > [icon: plus, set=fa]Add Software Publisher Agent and configure the account for the trusted directory:

   | Field                                | Value                                                 |
   | ------------------------------------ | ----------------------------------------------------- |
   | Agent ID                             | `Trusted Directory`                                   |
   | Software publisher issuer            | `PingGateway Sample Trusted Directory`                |
   | Software statement signing Algorithm | `PS256`                                               |
   | Public key selector                  | `JWKs_URI`                                            |
   | Json Web Key URI                     | `http://trustdir.example.com:9080/api/directory/jwks` |

3. Click Save Changes.

You have successfully configured the software publisher account for the sample trusted directory.

## Register the API clients

The FAPI conformance tests [use two API clients](https://openid.net/certification/certification-fapi_op_testing/), each with different keys and the same redirect URIs.

### Create an organization

1. Go to the trusted directory Organizations UI page at <http://trustdir.example.com:9080/ui/orgs>, and click + New Organization.

2. Name the new organization `Test organization` and click Create Organization.

You've successfully created a test organization.

### Create the API clients

Create both API clients by following these steps for each client:

1. On the Organizations UI page, click > in the Actions for the `Test organization`.

2. Click + New Software and use the following hints for the settings before clicking Create Software:

   | Field                | Example values                                                                                                                                                                                                                                           |
   | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Name                 | `FAPI test client 1` or `FAPI test client 2`                                                                                                                                                                                                             |
   | Description          | `FAPI test client for conformance tests`                                                                                                                                                                                                                 |
   | Redirect URIs        | `https://www.certification.openid.net/test/a/pinggateway/callback` `https://www.certification.openid.net/test/a/pinggateway/callback?dummy1=lorem&dummy2=ipsum`Change `pinggateway` in the URLs to a path element that's unique to your test deployment. |
   | Roles                | `DATA`                                                                                                                                                                                                                                                   |
   | Terms of Service URI | `https://example.com/terms-of-service`                                                                                                                                                                                                                   |
   | Policy URI           | `https://example.com/policy`                                                                                                                                                                                                                             |

   After you create the API clients, they show up in the UI software list for the test organization:

   ![The UI software list shows the API clients.](_images/fapi-test-api-clients.png)

You've successfully created the test API clients.

### Register each API client

Register *each* API client through PingGateway into PingOne Advanced Identity Cloud.

You provide the SSA and other client metadata as a client-signed JWT in the POST data of the registration request. Make sure you use the SSA and your client-signed JWT before either expires.

1. Get the SSA for the API client.

   1. Go to the trusted directory UI `Test organization` page under <http://trustdir.example.com:9080/ui/orgs>.

   2. Click the > in the Actions for test API client software to open its page.

   3. Click Generate SSA and copy the generated JWT.

2. Prepare the JSON payload for the client registration request.

   Here's an example payload template for the first API client:

   ```json
   {
     "client_name": "FAPI test client 1",
     "issuer": "PingGateway Sample Trusted Directory",
     "grant_types": [
       "authorization_code",
       "client_credentials",
       "refresh_token"
     ],
     "id_token_signed_response_alg": "PS256",
     "iss": "test-client-1",
     "redirect_uris": [
       "https://www.certification.openid.net/test/a/pinggateway/callback",
       "https://www.certification.openid.net/test/a/pinggateway/callback?dummy1=lorem&dummy2=ipsum"
     ],
     "request_object_signing_alg": "PS256",
     "response_types": [
       "code id_token"
     ],
     "scope": "openid",
     "token_endpoint_auth_method": "tls_client_auth",
     "tls_client_auth_subject_dn": "CN=Test organization",
     "token_endpoint_auth_signing_alg": "PS256",
     "exp": <expiration-time>,
     "iat": <issued-at-time>,
     "nbf": <issued-at-time>,
     "software_statement": "<SSA-JWT>"
   }
   ```

   1. Copy the SSA JWT into the template as the `software_statement` value.

   2. Decode the SSA JWT using the Ping Identity [JWT Decoder](https://developer.pingidentity.com/en/tools/jwt-decoder.html) online.

   3. Copy the `exp` and `iat` claim values from the decoded SSA JWT into the template.

      Use the value of `iat` to set the `nbf` (not before) claim.

3. Generate the signed JWT for the client registration request:

   1. Go to <https://www.jwt.io/>, select JWT encoder, and fill the form:

      | Field              | Use                                                                                                                                                                         |
      | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | Header             | `{ "alg": "PS256", "typ": "JWT" }`                                                                                                                                          |
      | Payload            | The completed JSON template from the previous step.                                                                                                                         |
      | Sign JWT           | Find the `sig` key in the JWK set you received when requesting the keys from the trusted directory.Copy and paste the JSON object just for that key, not the whole JWK set. |
      | Private key format | `JWK`                                                                                                                                                                       |

4. Copy the resulting signed JWT to your clipboard.

5. Register the API client in PingOne Advanced Identity Cloud using the SSA JWT from the trusted directory for [dynamic client registration,](https://docs.pingidentity.com/pingoneaic/am-oidc1/oauth2-dynamic-client-registration.html) (DCR).

   The following example registers an API client through PingGateway. Adapt this to match the realm and redirect URIs you use for testing:

   ```console
   $ curl \
   --request POST \
   --url 'https://gateway.example.com:8443/am/oauth2/realms/root/realms/alpha/register' \
   --cacert "$HOME/path/to/secrets/gateway.pem" \
   --header 'Content-Type: application/json' \
   --header "ssl-client-cert: ${SSL_CLIENT_CERT}" \
   --data "<client-signed-jwt>"
   ```

6. Save the JSON response.

   It includes the client ID, client secret, and important metadata required for conformance testing.

You have successfully registered the API client using the sample trusted directory. Repeat the steps for the other API client unless you have already done so.

When you've successfully registered both API clients, you can proceed to the conformance tests.

---

---
title: Validating FAPI with PingGateway
description: Validate your FAPI deployment with PingGateway using the OpenID Foundation conformance test suite and two registered API clients
component: pinggateway
version: 2026
page_id: pinggateway:fapi:test
canonical_url: https://docs.pingidentity.com/pinggateway/2026/fapi/test.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-23T12:00:00Z
section_ids:
  before_you_begin: Before you begin
  review_the_test_documentation: Review the test documentation
  prepare_the_test_plan: Prepare the test plan
  run_the_tests: Run the tests
---

# Validating FAPI with PingGateway

Validate your FAPI deployment using the two API clients you registered and the FAPI conformance test suite.

|   |                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------- |
|   | The FAPI conformance tests use DNS to access PingGateway URLs.Make sure the PingGateway deployment is accessible over the internet. |

## Before you begin

Before you begin, make sure you have:

* [icon: square-o, set=fa][Configured CORS settings in the PingOne Advanced Identity Cloud tenant](cors.html)

* [icon: square-o, set=fa][Configured access management settings in the PingOne Advanced Identity Cloud tenant](aic-am.html)

* [icon: square-o, set=fa][Configured identity management settings in the PingOne Advanced Identity Cloud tenant](aic-idm.html)

* [icon: square-o, set=fa][Configured PingGateway for FAPI](gateway.html)

* [icon: square-o, set=fa][Completed DCR for two API clients using the sample trusted directory](trusted-directory.html)

* [icon: square-o, set=fa]Saved the DCR responses for both API clients

* [icon: square-o, set=fa]Saved the PEM-format certificates and private keys for both API clients

* [icon: square-o, set=fa]Saved the PEM-format CA certificate for the sample trusted directory

## Review the test documentation

The OpenID foundation provides conformance tests accessible online through a Google or GitLab account.

Read the [instructions for the conformance tests](https://openid.net/certification/certification-fapi_op_testing/).

This tutorial focuses on [FAPI 1.0 Part 2 Advanced Final](https://openid.net/specs/openid-financial-api-part-2-1_0-final.html#rfc.section) tests.

## Prepare the test plan

1. Go to [the OpenID certification site](https://www.certification.openid.net/).

2. Sign on with your Google or GitLab account.

3. Create a test plan.

   1. Add the high-level settings:

      | Setting                    | Use                                               |
      | -------------------------- | ------------------------------------------------- |
      | Test Plan                  | `FAPI1-Advanced-Final: Authorization server test` |
      | Client Authentication Type | `private_key_jwt`                                 |
      | Request Object Method      | `by_value`                                        |
      | FAPI Profile               | `plain_fapi`                                      |
      | FAPI Response Mode         | `plain_response`                                  |

   2. Configure the specific settings for your deployment using the hints provided in the test plan page.

      Use the following additional hints to complete the configuration:

      | Setting         | Use                                                                                                                                                                      |
      | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      | alias           | The alias you chose to customize the client `software_redirect_uris`.                                                                                                    |
      | discoveryUrl    | The OpenID Provider well-known endpoint accessed through PingGateway, `https://<gateway-host:port>/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration`. |
      | Client settings | The fields in the DCR responses and the PEM-format certificates and private keys you saved.                                                                              |
      | resourceUrl     | The OpenID Provider well-known endpoint accessed through PingGateway, `https://<gateway-host:port>/rs/fapi/api`.                                                         |

4. Click Create Test Plan to access the tests.

## Run the tests

Run each test in the plan and correct any issues that arise.

You have successfully demonstrated FAPI compliance using PingGateway.
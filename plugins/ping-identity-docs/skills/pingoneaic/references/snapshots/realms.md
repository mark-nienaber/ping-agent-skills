---
title: Alpha and Bravo realms
description: Explore the default Alpha and Bravo realms, delegated administration, and realm-specific features in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:realms:alpha-bravo-realms
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/alpha-bravo-realms.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Administration", "Features", "Getting started", "Realms", "User Interface"]
section_ids:
  end_user_sign_in: End-user sign-in
  delegated_administration: Delegated administration
  assign_internal_roles: Assign internal roles
---

# Alpha and Bravo realms

The Alpha and Bravo realms are the two default realms that are included as part of an PingOne Advanced Identity Cloud tenant. These realms are configurable, unlike the top-level realm that Advanced Identity Cloud configures for tenant administrator identities.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud doesn't support more than two realms in the same tenant. Additionally, [delegated administration](#delegated_administration) and [Identity Governance](../identity-governance/administration/getting-started-what-is-iga.html)\[[1](#_footnotedef_1 "View footnote.")] are only supported in the Alpha realm.For customer identity and access management (CIAM) use cases, you can use either the Alpha or Bravo realm. |

## End-user sign-in

End users access their sign-in page using a URL that specifies the realm they belong to. For example:

* Alpha realm end users: https\://\<tenant-env-fqdn>/am/XUI/?**realm=alpha**\&authIndexType=service\&authIndexValue=Login

* Bravo realm end users: https\://\<tenant-env-fqdn>/am/XUI/?**realm=bravo**\&authIndexType=service\&authIndexValue=Login

Tenant administrators cannot authenticate using these realm-specific login URLs. Learn more in [Sign on to a tenant admin console](../tenants/tenant-administrator-settings.html#sign-on-to-a-tenant-admin-console).

## Delegated administration

In the Alpha realm, you can set up [internal roles](../identities/roles-assignments.html#internal_roles) for delegated administration using a custom set of privilege attributes.You can then assign those internal roles to users so that Alpha realm users can act as delegated administrators and perform actions on the custom set of attributes specified by the role.

The Bravo realm does not support delegated administration.

### Assign internal roles

You can assign the internal roles in two different ways using the Advanced Identity Cloud admin console:

* To add an internal role to a user, go to Identities > Manage > *Realm* - Users. Select a user, then select the Authorization Roles tab, then click + Add Authorization Roles.

* To add a user to an internal role, go to Identities > Manage > Internal Roles. Select a role, then select the Members tab, then click + Add Members.

In the Bravo realm, while you can set up internal roles for delegated administration, you cannot use them. Also, you cannot add a user to an internal role, and even though it appears possible to add an internal role to a user, this will not correctly link the user to the role. If you attempt this, the user will not be listed in the internal role Members tab.

The following table summarizes these differences:

| Action                                                            | Alpha Realm           | Bravo Realm                                                             |
| ----------------------------------------------------------------- | --------------------- | ----------------------------------------------------------------------- |
| Create internal role for the purposes of delegated administration | [icon: check, set=fa] | [icon: check, set=fa]                                                   |
| Add user to internal role                                         | [icon: check, set=fa] | [icon: times, set=fa]                                                   |
| Add internal role to user                                         | [icon: check, set=fa] | [icon: triangle-exclamation, set=fa] appears possible but will not work |

***

[1](#_footnoteref_1). IGA is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Application management (legacy)
description: Manage applications and OAuth 2.0 client profiles for authentication in Advanced Identity Cloud realms
component: pingoneaic
page_id: pingoneaic:realms:applications
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/applications.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Application Management", "Setup &amp; Configuration", "Single Sign-on (SSO)"]
page_aliases: ["pingoneaic::applications.adoc"]
section_ids:
  register_an_application_or_service: Register an application or service
  create_a_client_profile: Create a client profile
  supported_application_types: Supported application types
  native_spa: Native / SPA
  web: Web
  service: Service
  oauth_2_0_and_openid_connect: OAuth 2.0 and OpenID Connect
  oauth_2_0: OAuth 2.0
  openid_connect: OpenID Connect
  whats_in_the_client_profile: What's in the client profile
  scopes: Scopes
  grant_types: Grant types
  claims: Claims
  access_tokens: Access tokens
  keys: Keys
---

# Application management (legacy)

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The topics in this section are for tenants created before January 12, 2023. Learn more in [Application management migration FAQ](../product-information/migration-dependent-features/application-management-migration-faq.html). |

Your applications act as clients to PingOne Advanced Identity Cloud. Ping Identity uses both [OAuth 2.0 and OpenID Connect](#oauth_2_0_and_openid_connect) protocols to protect your applications. When you register a [supported application or service](#supported_application_types), Advanced Identity Cloud sets the OAuth 2.0 grant type based on the type of application you're registering. Advanced Identity Cloud also sets OpenID Connect default options for you. You can customize configuration in the application's client profile.

To get started, first [register your application or service](#register_an_application_or_service) to your tenant. Then, [create a client profile](#create_a_client_profile) for the application or service.

You can view and manage all your applications on the Applications page of the Advanced Identity Cloud admin console.

|   |                                                                                   |
| - | --------------------------------------------------------------------------------- |
|   | The Advanced Identity Cloud admin console supports a maximum of 500 applications. |

## Register an application or service

1. In the Advanced Identity Cloud admin console, go to Applications, and click + Add Application.

2. In the New Consumer App dialog box, choose the application type you want to register:

   * [Native / SPA](#native_spa)

   * [Web](#web)

   * [Service](#service)

3. In the Web Application Credentials dialog box, enter a Client ID to be displayed in the Applications list, and if shown, enter a Client Secret.

4. Click Create Application.

## Create a client profile

1. In the Advanced Identity Cloud admin console, click Applications.

2. In the Applications list, find the application name, then click More ([icon: ellipsis-h, set=fa]), and choose Edit.

3. Review read-only Client Credentials:

   > **Collapse: Client Credentials**
   >
   > |               |                                                                                                                                 |
   > | ------------- | ------------------------------------------------------------------------------------------------------------------------------- |
   > | Discovery URI | AM URL base for OpenID Provider Configuration. Default: <http://openam.example.com:8088/openam/oauth2>                          |
   > | Client ID     | Identifier used to register your client with AM's authorization server, and then used when your client must authenticate to AM. |
   > | Client Secret | Password used to register your client with AM's authorization server, and then used when your client must authenticate to AM.   |

4. Edit General Settings:

   > **Collapse: General Settings**
   >
   > |               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | Name          | Specify a client name to display to the resource owner when the resource owner is asked to authorize client access to protected resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | App Logo URI  | Specify the location of your custom logo image file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | Description   | Specify a client description to display to the resource owner when the resource owner is asked to authorize client access to protected resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   > | Sign-in URLs  | Custom URL for handling sign on. Overrides the default sign-on page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | Sign-out URLs | Custom URL for handling sign off. Example: <https://client.example.com:8443/am/XUI/?realm=/#logout>.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | Grant Types   | Specify the set of OAuth 2.0 grant types, also known as grant flows, allowed for this client:- Authorization Code
   >
   >   (default) Instead of requesting authorization directly from the user, your client application or service directs the user to an authorization server (Advanced Identity Cloud).
   >
   > - Back Channel Request
   >
   >    
   >
   > - Implicit
   >
   >   The client is issued an access token directly. No intermediate credentials (such as an authorization code) are issued. This grant type can potentially pose a security risk. Learn more in [Implicit grant](../am-oauth2/oauth2-implicit-grant.html).
   >
   > - Resource Owner Password Credentials
   >
   >   Username and password can be used directly as an authorization grant to obtain an access token. The credentials should only be used when there is a high degree of trust between the user and the client application or service.
   >
   > - Client Credentials
   >
   >   Used when the client acts on its own behalf or requests access to protected resources based on previously-arranged authorization.
   >
   > - Refresh Token
   >
   >   Credentials used to obtain access tokens.
   >
   > - Device Code
   >
   >   Authorizes a client device, such as a smarthome thermostat, to access its service on an end user's behalf. For example, the end user could log in to the thermostat service using a cell phone to enter a code displayed on the thermostat.
   >
   > - SAML 2.0
   >
   >   Leverages the REST-based services provided by AM's OAuth 2.0 support. Maintains existing SAML 2.0 federation implementation. |
   > | Scopes        | Specify scopes that display to the resource owner when they authorize client access to protected resources.The `openid` scope is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

5. Edit Advanced Settings:

   > **Collapse: Access**
   >
   > |                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   > | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | Add Default Scopes                    | Scopes to be set automatically when tokens are issued. The `openid` scope is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | Add Response types                    | Specify the response types that the client uses. The response type value specifies the flow that determines how the ID token and access token are returned to the client. By default, the following response types are available:- ︎`code`. Specifies that the client application requests an authorization code grant.
   >
   > - `token`. Specifies that the client application requests an implicit grant type and requests a token from the API.
   >
   > - `id_token`. Specifies that the client application requests an ID token.
   >
   > - `code token`. Specifies that the client application requests an access token, access token type, and an authorization code.
   >
   > - `token id_token`. Specifies that the client application requests an access token, access token type, and an ID token.
   >
   > - `code id_token`. Specifies that the client application requests an authorization code and an ID token.
   >
   > - `code token id_token`. Specifies that the client application requests an authorization code, access token, access token type, and an ID token. |
   > | Add Claims                            | Claims can be entered as simple strings, such as `name`, `email`, `profile`, or `sub`. Or, as a pipe-separated string in the format: `scope\|locale\|localized description`. For example, `name\|en\|Full name of user`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   > | Allow wildcard ports in redirect URLs | Specify whether AM allows the use of wildcards (\* characters) in the redirection URI port to match one or more ports.The URL configured in the redirection URI must be either localhost, 127.0.01, or ::1. For example, http\://localhost:\*/, https\://127.0.0.1:80\*/, or https\://\[::1]:\*443/.Enable this setting, for example, for desktop applications that start a web server on a random free port during the OAuth 2.0 flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

   > **Collapse: Authentication**
   >
   > |                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   > | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   > | Token Endpoint Authentication Method               | Authentication method client uses to authenticate to AM. Choose one:- `client_secret_basic`. Clients authenticate using the HTTP Basic authentication scheme after receiving a client\_secret value.
   >
   > - `client_secret_post`. Clients authenticate by including the client credentials in the request body after receiving a client\_secret value.
   >
   > - `private_key_jwt`. Clients sign a JSON web token (JWT) with a registered public key. |
   > | Token Endpoint Authentication Method (Client Type) | * Confidential clients can maintain the confidentiality of their credentials. For example, a web application runs on a server where its credentials are protected.
   >
   > * Public clients run the risk of exposing their passwords to a host or user agent. For example, a JavaScript client running in a browser may be accessible to the public.                                                                                              |
   > | Implied Consent                                    | When enabled, the resource owner will not be asked for consent during authorization flows. The OAuth2 Provider must also be configured to allow clients to skip consent.                                                                                                                                                                                                                                                                   |
   > | OAuth 2.0 Mix-Up Mitigation active                 | Enable this setting only if this OAuth 2.0 client supports the [OAuth 2.0 Mix-Up Mitigation draft](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-mix-up-mitigation-01); otherwise AM will fail to validate access token requests received from this client.                                                                                                                                                                       |
   > | Add Default ACR values                             | Default Authentication Context Class Reference values. Specify strings that will be requested as Voluntary Claims by default in all incoming requests.                                                                                                                                                                                                                                                                                     |
   > | Add Request URIs                                   | Specify request\_uri values that a dynamic client would pre-register.                                                                                                                                                                                                                                                                                                                                                                      |
   > | Client JWT Bearer Public Key                       | A base64-encoded X509 certificate in PEM format used to obtain the client's JWT bearer public key. The client uses the private key to sign client authentication and access token request JWTs, while AM uses the public key for verification.                                                                                                                                                                                             |
   > | Subject Type                                       | Default value is public.* Choose pairwise if you want each client to receive a different subject value. This prevents correlation between clients.
   >
   > * Choose public if you want each client to receive the same subject value.                                                                                                                                                                                                             |
   > | Default Max Age                                    | Enable this option to enforce a default maximum age of ten minutes. If the user session is not currently active, and if more than ten minutes have passed since the user last authenticated, then the user must be authenticated again.                                                                                                                                                                                                    |
   > | Use Certificate-Bound Access Tokens                | Enable this option if you want access tokens issued to this client to be bound to an X.509 certificate. When enabled, access tokens will use the X.509 certificate to authenticate to the `access_token` endpoint.                                                                                                                                                                                                                         |

   > **Collapse: Token Lifetimes**
   >
   > |                                       |                                                                                                                                                                                        |
   > | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | Authorization code lifetime (seconds) | The time an authorization code is valid for. Default value: 120                                                                                                                        |
   > | Access token lifetime (seconds)       | The time an access token is valid for, in seconds If you set the value to 0, the access token will not be valid. A maximum lifetime of 600 seconds is recommended. Default value: 3600 |
   > | Refresh token lifetime (seconds)      | The time a refresh token is valid for. If this field is set to -1, the refresh token will never expire. Default value: 604800                                                          |
   > | JWT token lifetime (seconds)          | The amount of time the JWT is valid for. Default value: 3600                                                                                                                           |

   > **Collapse: Consent Screen**
   >
   > |                         |                                                                                                                                                 |
   > | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
   > | Add Display Name        | Custom user-facing title. In this example, MyClient.                                                                                            |
   > | Add Display Description | User-facing instruction text. In this example, "This application is requesting the following information:"                                      |
   > | Add Privacy Policy URI  | URI containing the client's privacy policy documentation. The URI is displayed as a link in the consent page.![200](_images/consent-screen.png) |

   > **Collapse: Client Management**
   >
   > |              |                                                                                                                                                                 |
   > | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | Access Token | Specify the `registration_access_token` value that you provide when registering the client, and then subsequently, when reading or updating the client profile. |

   > **Collapse: Session Management**
   >
   > |                    |                                                                                                                                                                     |
   > | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | Client Session URI | Specify the relying party (client) URI to which the OpenID Connect Provider sends "session changed" notification. Message is sent using the HTML 5 postMessage API. |

   > **Collapse: Endpoint Response Formats**
   >
   > |                                     |                                                                                                                                                                                                                                                                                 |
   > | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | User info response format           | Specify the output format from the `userinfo` endpoint. The supported output formats are:- (default) User info JSON response format.
   >
   > - User info encrypted JWT response format.
   >
   > - User info signed JWT response format.
   >
   > - ︎ User info signed then encrypted response format. |
   > | Token introspection response format | The format of the token introspection response. The possible values for this property are:- JSON response format
   >
   > - Signed JWT response format
   >
   > - Signed then encrypted JWT response format                                                                                     |

   > **Collapse: Signing and Encryption**
   >
   > |                                |                                                                                                                                                      |
   > | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | Public key selector            | Select the public key for this client, which comes from the JWKs\_URI, manual JWKs, or X.509 field.                                                  |
   > | JSON Web Key URI               | The URI that contains the client public keys in JSON web key format.                                                                                 |
   > | JSON Web Key                   | Raw JSON web key value containing the client public keys.                                                                                            |
   > | ID Token Encryption Public Key | The RSA public key for encrypting ID tokens in X.509 PEM format. For example:+```none
   > -----BEGIN PUBLIC KEY-----
   > ......
   > -----END PUBLIC KEY-----
   > ``` |
   > | Enable ID Token Encryption     | When enabled, encryption uses the algorithm with which the ID token must be encrypted. Default algorithm value is RSA1\_5 (RSAES-PKCS1-V1\_5).       |

6. Click Save.

## Supported application types

When you register an application or service, Advanced Identity Cloud automatically sets the optimal configuration for you. To change the default settings, [edit the client profile](#create_a_client_profile).

### Native / SPA

Native applications are developed for specific platforms or devices. Examples include the applications on mobile phones and applications dedicated to the macOS platform.

Single-page applications (SPAs) are OAuth 2.0 clients that run in a user's web browser. SPAs use PKCE to verify the client because SPAs do not have a way to secure the `client_secret` value. PKCE stands for Proof Key Code Exchange; a security standard explained in the IETF specification [Proof Key for Code Exchange by OAuth Public Clients](https://www.rfc-editor.org/rfc/rfc7636.html).

For a deep dive on how ForgeRock implements PKCE for native and SPA applications, learn more in [Authorization code grant with PKCE](../am-oauth2/oauth2-authz-grant-pkce.html).

### Web

Web applications are OAuth 2.0 clients that run on a web server. End users (resource owners) access web applications using a web browser. The application makes API calls using a server-side programming language. The end user has no access to the OAuth 2.0 client secret or any access tokens issued by the authorization server.

### Service

Machine-to-machine (M2M) applications interact with an API and no user involvement is necessary. The application can ask for an access token without involving a user in the process. A smart meter that tracks your utility usage and wearable devices that gather and communicate health data use services and M2M applications.

## OAuth 2.0 and OpenID Connect

Advanced Identity Cloud uses OAuth 2.0 and OpenID Connect to protect your applications.

### OAuth 2.0

Advanced Identity Cloud provides an authorization service in the OAuth 2.0 authorization flow. OAuth 2.0 lets you set up access to your resources without sharing end-user account information. For a deep dive, learn more in [RFC6749](https://www.rfc-editor.org/rfc/rfc6749.html#section-2.1).

|   |                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You may encounter domain validation prompts when using forgeblocks.com and id.forgerock.io domains as redirect URLs in your Google OAuth 2.0 applications. To resolve this, you must [use a custom domain](custom-domains.html), and then set up [domain verification with Google](custom-domains.html#custom-domain-google). |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You could encounter `No provider found` errors when using forgeblocks.com and id.forgerock.io domains as redirect URLs in your OAuth 2.0 applications. To resolve this, either modify the redirect URL to include a realm identifier, or [use a custom domain](custom-domains.html):- Incorrect: https\://\<tenant-env-fqdn>/am/oauth2/client/form\_post/...

- Correct: https\://\<tenant-env-fqdn>/am/oauth2/\<realm>/client/form\_post/... *or* https\://\<custom-domain-fqdn>/am/oauth2/client/form\_post/...A custom domain acts as a realm DNS alias, so when it is used as a redirect URL, Advanced Identity Cloud implicitly knows which realm to use. |

### OpenID Connect

OpenID Connect (OIDC) provides an identity layer on top of OAuth 2.0. OIDC lets a client make assertions about the user's identity and their means of authentication. For a deep dive, learn more in [OIDC grant flows](../am-oidc1/oidc-implementing-flows.html).

## What's in the client profile

Changing the client profile settings requires a working knowledge of OAuth 2.0, its grant types, and its components. If no one has given you direction on how to configure the client profile, you'll want to read up on some basic concepts.

### Scopes

Scopes limit your client application's access to end users' resources. For a deep dive on how scopes work, learn more in [Scopes](../am-oauth2/oauth2-scopes.html).

### Grant types

Grant types, also known as grant flows, describe how your application or service access gets an access token. Learn more about grant types in [OAuth 2.0 grant flows](../am-oauth2/oauth2-implementing-flows.html).

### Claims

Claims convey information about the end user to your client application or service. For a deep dive on claims, learn more in the [Claims](../am-oidc1/understanding-openid-connect-scopes-and-claims.html).

### Access tokens

Your applications and services use access tokens when making requests on behalf of a user. Tokens provide proof that your application or service is authorized to access the end user's data. For a deep dive on access tokens, learn more in [Advanced Identity Cloud as authorization server](../am-oauth2/am-as-authz-server.html).

### Keys

Keys protect sensitive information that Advanced Identity Cloud needs to both send and receive. You can store keys in [ESV secrets](../tenants/esvs.html#secrets), then use them in OAuth 2.0 authentication flows by mapping the ESVs to [secret labels](../tenants/esvs-signing-encryption.html#secret-labels).

---

---
title: Configure customer-friendly domain names
description: Configure customer-friendly domain names for Advanced Identity Cloud realm access with DNS configuration and verification
component: pingoneaic
page_id: pingoneaic:realms:custom-domains
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/custom-domains.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Customization", "ESV", "Integration", "Realms", "Setup &amp; Configuration"]
section_ids:
  configure-a-custom-domain: Configure a custom domain
  custom-domain-google: Verify a custom domain in Google
  access-oidc-configuration-discovery-endpoint: Access OIDC configuration discovery endpoint
---

# Configure customer-friendly domain names

PingOne Advanced Identity Cloud lets you configure access to your tenant environments using one or more custom domains. Custom domains let you replace the default forgerock.io domain with a customer-friendly URL that reflects your company name or brand:

* Configure the Alpha and Bravo realms to use a custom domain for hosted pages and your customer-facing applications.

* Configure the top-level realm to use a custom domain for the admin console and your administrative applications.

Consider the following points when you customize a domain name:

* You can set a custom domain name only at the realm level.

* You can set multiple custom domain names per realm.

* Don't use your top-level domain name. This is because you must set up a CNAME record for each custom domain, but CNAME records aren't permitted alongside other record types, including any A, NS, TXT, or SOA record types that belong to a top-level domain.

  * Wrong: `mycompany.com`

  * Right: `id.mycompany.com`

  Learn more in section 2.4 of [RFC 1912](https://www.rfc-editor.org/rfc/rfc1912).

## Configure a custom domain

1. Create a CNAME record with your DNS provider that points your custom domain to your Advanced Identity Cloud tenant environment's FQDN. For example:

   | Type  | Name                    | Data                          |
   | ----- | ----------------------- | ----------------------------- |
   | CNAME | customers.mycompany.com | openam-mycompany.forgerock.io |

2. If your custom domain already has CAA records, add additional CAA records to ensure that Advanced Identity Cloud can generate Google-managed SSL certificates. Learn more in [Specify the CAs that can issue your Google-managed certificate](https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#caa). For example:

   | Type | Name                    | Data                    |
   | ---- | ----------------------- | ----------------------- |
   | CAA  | customers.mycompany.com | letsencrypt.org 0 issue |
   | CAA  | customers.mycompany.com | pki.goog 0 issue        |

3. [Create a self-managed certificate](server-certificates.html#self-managed-certificates).

   * This step is required if your custom domain relies on private DNS or you route your HTTP traffic through a WAF service.

   * This step is optional if your custom domain relies on public DNS.

4. Add the custom domain to your realm. Learn more in:

   * [Manage custom domains using the admin console](custom-domains-ui.html) (supports Alpha and Bravo realms only)

   * [Manage custom domains using the API](custom-domains-api.html) (supports Alpha, Bravo, and top-level realms)

5. Configure the cookie domain for the custom domain using the instructions in [Control cookie scope for custom domains](cookie-domains.html).

6. The custom domain should now be successfully configured:

   * If your custom domain relies on public DNS, and you don't have a self-managed SSL certificate, Advanced Identity Cloud adds the custom domain to a Google-managed SSL certificate:

     * If this is the first custom domain you've added to any of the realms in your tenant, Advanced Identity Cloud creates a second Google-managed SSL certificate and adds the custom domain to the Subject Alternative Name (SAN) field of the certificate. It creates a second certificate so that the first Google-managed SSL certificate continues to serve the default tenant FQDN without interruption.

     * If this is the second or subsequent custom domain you're adding to any realm in your tenant, Advanced Identity Cloud adds the custom domain to the SAN field of the second Google-managed SSL certificate.

     |   |                                                                                                     |
     | - | --------------------------------------------------------------------------------------------------- |
     |   | It can take up to 30 minutes to provision or reprovision the second Google-managed SSL certificate. |

   * The custom domain name is added to the realm settings.

   * The FQDN for your custom domain name is mapped to server defaults.

   * The custom domain name is added to the Redirection URIs field of the `end-user-ui` OAuth 2.0 client. Learn more in [Configure OAuth clients](https://docs.pingidentity.com/platform/8/sample-setup/am-setup-1.html#oauth-clients).

7. Confirm that the custom domain is working as expected:

   * To confirm that Advanced Identity Cloud is serving traffic over HTTPS (TLS) for your custom domain name, in a browser, go to your custom domain location. For example, go to `https://id.mycompany.com`.

   * Confirm that URL paths work for both tenant domain and custom domain. You should be able to access the same resources using both domains.

     Example endpoints for the Alpha realm:

     * Access management:

       * `https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate`

       * `https://<custom-domain-fqdn>/am/json/realms/root/realms/alpha/authenticate`

     * Identity management:

       * `https://<tenant-env-fqdn>/openidm/managed/alpha_user/<uuid>`

       * `https://<custom-domain-fqdn>/openidm/managed/alpha_user/<uuid>`

     |   |                                                                                                                   |
     | - | ----------------------------------------------------------------------------------------------------------------- |
     |   | This doesn't apply to the [OIDC configuration discovery endpoint](#access-oidc-configuration-discovery-endpoint). |

   * To test hosted pages or the Advanced Identity Cloud admin console, use an incognito or private browser window:

     * If you added the custom domain to an Alpha or Bravo realm, access an end-user URL. For example:\
       `https://id.mycompany.com/login/?realm=/alpha#/`.

     * If you added the custom domain to the top-level realm, access an administrator URL. For example:\
       `https://id.mycompany.com/login/?realm=/#/`.

   * If your custom domain relies on public DNS, it can take up to 48 hours for domain name changes to propagate. If you try to use the new domain name to access your website, error messages might display until the changes take effect. If error messages still display after 48 hours, make sure your Advanced Identity Cloud domain name settings are correct.

## Verify a custom domain in Google

If you use Google as a social login IdP, you must use your domain to configure the redirect URL fields of your OAuth 2.0 apps. This might create prompts from Google to verify your domain with your domain provider. For information about how to verify your domain, learn more in [Verify your site ownership](https://support.google.com/webmasters/answer/9008080?hl=en) on the Google Search Console.

## Access OIDC configuration discovery endpoint

When you configure a custom domain, the [OIDC configuration discovery](../am-oidc1/rest-api-oidc-discovery-configuration.html#rest-api-oidc-discovery-configuration) endpoint URL changes:

| Domain context | Endpoint URL                                                                                                                                                                                                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Default domain | `https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/<realm>/.well-known/openid-configuration`                                                                                                                                                                                                 |
| Custom domain  | * Incorrect: `https://<custom-domain-fqdn>/am/oauth2/realms/root/realms/<realm>/.well-known/openid-configuration`

* Correct: `https://<custom-domain-fqdn>/.well-known/openid-configuration`	Using the incorrect endpoint URL can result in an OIDC discovery failure due to an issuer mismatch. |

---

---
title: Control cookie scope for custom domains
description: Control cookie scope for Advanced Identity Cloud custom domains across subdomains
component: pingoneaic
page_id: pingoneaic:realms:cookie-domains
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/cookie-domains.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Control cookie scope for custom domains

Advanced Identity Cloud lets you configure the cookie domains of your custom domains so you can control which applications have access to the cookies you create.

By default, when you add a [custom domain](custom-domains.html) to an environment, no cookie domain is set for it. You must explicitly configure its cookie domain to suit your deployment. You can configure it in these ways:

* Set it to use a single subdomain (for example, `sso.mycompany.co.uk`). This ensures cookies can be set or modified only by applications running on that subdomain.

* Set it to use more than one subdomain. This lets you set cookies on one subdomain (for example, `sso.mycompany.co.uk`) but makes them available to an application running on a different subdomain (for example, `banking.mycompany.co.uk`).

* Set it to use a domain (for example, `mycompany.co.uk`). This lets you set cookies at the domain level so they're available to legacy applications yet to be migrated to Advanced Identity Cloud.

Learn how to set cookie domains in:

* [Manage cookie domains using the API](cookie-domains-api.html)

* [Manage cookie domains using the admin console](cookie-domains-ui.html)

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Advanced Identity Cloud always writes cookies to the default [tenant environment FQDN](../tenants/environments.html#tenant-environment-fqdns) of each of your environments. This is not configurable to ensure you retain access to your environments. |

---

---
title: Gateways &amp; agents
description: Integrate Advanced Identity Cloud with PingGateway and policy agents for web resource access security
component: pingoneaic
page_id: pingoneaic:realms:gateways-agents
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/gateways-agents.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Agent", "Authorization", "Integration", "Security", "Realms"]
page_aliases: ["pingoneaic::gateways-agents.adoc"]
section_ids:
  identity-gateway: PingGateway
  policy-agents: Policy agents
---

# Gateways & agents

Integrate PingOne Advanced Identity Cloud with PingGateway and policy agents to secure access to your web resources.

## PingGateway

PingGateway integrates your web applications, APIs, and microservices with Advanced Identity Cloud. PingGateway enforces security and access control without modifying your applications or the containers where they run—whether on premises, in a public cloud, or in a private cloud.

Based on reverse proxy architecture, PingGateway intercepts client requests and server responses. In this process, PingGateway enforces user or service authentication and authorization to HTTP traffic. Advanced Identity Cloud acts as the authentication and authorization provider.

PingGateway can also conduct deep analysis, then throttle and transform requests and responses when necessary.

Learn more in the [PingGateway Guide for Advanced Identity Cloud](https://docs.pingidentity.com/pinggateway/latest/identity-cloud-guide/). In particular, refer to these detailed instructions and examples:

* [API Security With OAuth 2.0 and the Advanced Identity Cloud](https://docs.pingidentity.com/pinggateway/latest/identity-cloud-guide/oauthrs.html)

* [Single Sign-On With OpenID Connect and the Advanced Identity Cloud](https://docs.pingidentity.com/pinggateway/latest/identity-cloud-guide/oidc.html)

* [Cross-Domain Single Sign-On With the Advanced Identity Cloud](https://docs.pingidentity.com/pinggateway/latest/identity-cloud-guide/cdsso.html)

## Policy agents

Policy agents are PingAM add-on components. They operate as policy enforcement points (PEPs) for websites and applications.

Policy agents natively plug into web or applications servers. The agents intercept inbound requests to websites, and interact with AM to:

* Ensure that clients provide appropriate authentication.

* Enforce AM resource-based policies.

Use Web Agents to protect services and web resources hosted on a web or proxy server. Use Java Agents to protect resources hosted on application or portal servers.

Although both agents enforce authentication and authorization to protected resources, they differ in the way they derive policy decisions and enforce them.

For examples of how to transition from on-premises access management to Advanced Identity Cloud without changing the architecture of the agent-based model, learn more in these guides:

* Web Agent Example

  [Web Agent Guide for Advanced Identity Cloud](https://docs.pingidentity.com/web-agents/latest/identity-cloud-guide/)

* Java Agent Example

  [Java Agent Guide for Advanced Identity Cloud](https://docs.pingidentity.com/java-agents/latest/identity-cloud-guide/)

---

---
title: Manage cookie domains using the admin console
description: Configure cookie domains for Advanced Identity Cloud realms using the admin console
component: pingoneaic
page_id: pingoneaic:realms:cookie-domains-ui
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/cookie-domains-ui.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Manage cookie domains using the admin console

You can find background information on cookie domains in [Control cookie scope for custom domains](cookie-domains.html).

Advanced Identity Cloud always writes cookies to your default tenant FQDN to ensure you retain access. Use the Advanced Identity Cloud admin console to view or edit the other domains or subdomains where your tenant environment writes cookies.

1. In the Advanced Identity Cloud admin console, open the TENANT menu (upper right).

2. Click [icon: settings, set=material, size=inline] Tenant Settings.

3. Click Global Settings, then click Cookie.

4. Review the cookie domains configured in the Additional Cookie Domains field:

   * Each cookie domain is displayed in the field as a tag:

     ![cookie domains field](_images/cookie-domains-field.png)

   * To add a cookie domain:

     1. Click inside the Additional Cookie Domains field to give it focus and display a text prompt below the tags.

     2. Enter a cookie domain value (for example, `account.mycompany.co.uk`).

     3. Click an area outside the text prompt (or press `enter`) to create a tag for the new cookie domain value.

   * To delete a cookie domain, click the close icon ([icon: close, set=material, size=inline]) on the right of the cookie domain's tag.

     |   |                                                                                                                                                                        |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Before removing a domain or subdomain from the configuration, you must first update any existing applications that rely on cookies set using that domain or subdomain. |

5. If you made changes in the previous step, click Save to confirm them.

   An asynchronous process updates the environment's cookie domain configuration. This process can take up to 10 minutes to complete.

---

---
title: Manage cookie domains using the API
description: Manage cookie domains for Advanced Identity Cloud realms using the REST API
component: pingoneaic
page_id: pingoneaic:realms:cookie-domains-api
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/cookie-domains-api.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  cookie-domains-api-endpoint: Cookie domains API endpoint
  authenticate-to-the-cookie-domains-api-endpoint: Authenticate to the cookie domains API endpoint
  view-cookie-domains: View cookie domains
  update-cookie-domains: Update cookie domains
---

# Manage cookie domains using the API

You can find background information on cookie domains in PingOne Advanced Identity Cloud in [Control cookie scope for custom domains](cookie-domains.html).

## Cookie domains API endpoint

Advanced Identity Cloud provides the [Cookie Domains API endpoint](https://docs.pingidentity.com/pingoneaic/_attachments/api/#tag/Cookie-Domains) to manage cookie domains.

## Authenticate to the cookie domains API endpoint

To authenticate to the cookie domains API endpoint, use an [access token](../developer-docs/authenticate-to-rest-api-with-access-token.html) created with the following scope:

| Scope                    | Description                                     |
| ------------------------ | ----------------------------------------------- |
| `fr:idc:cookie-domain:*` | Full access to the cookie domains API endpoint. |

## View cookie domains

Advanced Identity Cloud always writes cookies to your default tenant FQDN to ensure you retain access. Make a GET request to the `/environment/cookie-domains` endpoint to view the other domains or subdomains where your tenant environment writes cookies.

To view the cookie domain configuration in any tenant environment:

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) created with the `fr:idc:cookie-domain:*` scope.

2. Get the cookie domain configuration from the `/environment/cookie-domains` endpoint:

   ```shell
   $ curl \
   --request GET 'https://<tenant-env-fqdn>/environment/cookie-domains' \(1)
   --header 'Authorization: Bearer <access-token>' (2)
   ```

   |       |                                                                      |
   | ----- | -------------------------------------------------------------------- |
   | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment. |
   | **2** | Replace \<access-token> with the access token.                       |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "domains": [
   >         "sso.mycompany.co.uk",
   >         "banking.mycompany.co.uk"
   >     ]
   > }
   > ```

## Update cookie domains

Advanced Identity Cloud always writes cookies to your default tenant FQDN to ensure you retain access. Make a PUT request to the `/environment/cookie-domains` endpoint to set or update the other domains or subdomains where your tenant environment writes cookies.

To update the cookie domain configuration in any tenant environment:

1. Review the existing cookie domain configuration. Learn more in [View cookie domains](#view-cookie-domains).

2. Adapt the cookie domain configuration to suit your use case. Learn more in [Control cookie scope for custom domains](cookie-domains.html).

   |   |                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Before removing a domain or subdomain from the configuration, you must first update any existing applications that rely on cookies set using that domain or subdomain. |

3. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) created with the `fr:idc:cookie-domain:*` scope.

4. Replace the existing cookie domain configuration with the cookie domain configuration you adapted in step 2:

   ```shell
   $ curl \
   --request PUT 'https://<tenant-env-fqdn>/environment/cookie-domains' \(1)
   --header 'Authorization: Bearer <access-token>' \(2)
   --header 'Content-Type: application/json' \
   --data '<cookie-domains-configuration>' (3)
   ```

   |       |                                                                                                                                                                                                                                                                                                                                                                                                  |
   | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                                                                                                                                                                                                             |
   | **2** | Replace \<access-token> with the access token.                                                                                                                                                                                                                                                                                                                                                   |
   | **3** | Replace \<cookie-domains-configuration> with a JSON array of cookie domains; for example, the following configuration adds a new subdomain `account.mycompany.co.uk` to the configuration example used in [View cookie domains](#view-cookie-domains).```json
   {
       "domains": [
           "sso.mycompany.co.uk",
           "banking.mycompany.co.uk",
           "account.mycompany.co.uk"
       ]
   }
   ``` |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "domains": [
   >         "sso.mycompany.co.uk",
   >         "banking.mycompany.co.uk",
   >         "account.mycompany.co.uk"
   >     ]
   > }
   > ```

   An asynchronous process updates the environment's cookie domain configuration. This process can take up to 10 minutes to complete.

---

---
title: Manage custom domains using the admin console
description: Add and manage custom domains for Advanced Identity Cloud Alpha and Bravo realms using the admin console
component: pingoneaic
page_id: pingoneaic:realms:custom-domains-ui
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/custom-domains-ui.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Manage custom domains using the admin console

You can find background information on custom domains in [Configure customer-friendly domain names](custom-domains.html).

|   |                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The admin console lets you manage custom domain configuration for only the Alpha and Bravo realms. To configure a custom domain for the top-level realm, follow the instructions in [Manage custom domains using the API](custom-domains-api.html). |

To manage the custom domain configuration for the Alpha or Bravo realms:

1. In the Advanced Identity Cloud admin console, open the Realm menu (upper left).

2. Go to [icon: settings, set=material, size=inline] Realm Settings > Custom Domain.

3. Review the list of custom domains configured for the realm:

   * To add a new custom domain:

     1. Click + Add a Custom Domain.

     2. In the Add a Custom Domain modal, enter your domain or subdomain name. For example, `id.mycompany.com`.

     3. Click Next.

     4. In the Verify Domain Name Ownership modal:

        1. (Optional) Follow the on-screen instructions to set up a CNAME record.

        2. Click Verify, then click Done.

   * To delete a custom domain, click its delete icon ([icon: delete, set=material, size=inline]), and in the Delete Custom Domain? modal, click Delete.

     |   |                                                                                                                                                      |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Before removing a domain or subdomain from the configuration, you must first update any existing applications that rely on that domain or subdomain. |

---

---
title: Manage custom domains using the API
description: Manage custom domains for all Advanced Identity Cloud realms using the REST API
component: pingoneaic
page_id: pingoneaic:realms:custom-domains-api
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/custom-domains-api.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  custom-domains-api-endpoint: Custom domains API endpoint
  authenticate-to-the-custom-domains-api-endpoint: Authenticate to the custom domains API endpoint
  view-custom-domains: View custom domains
  update-custom-domains: Update custom domains
---

# Manage custom domains using the API

You can find background information on custom domains in PingOne Advanced Identity Cloud in [Configure customer-friendly domain names](custom-domains.html).

## Custom domains API endpoint

Advanced Identity Cloud provides the [Custom Domains API endpoint](https://docs.pingidentity.com/pingoneaic/_attachments/api/#tag/Custom-Domains) to manage custom domains:

/environment/custom-domains/\<realm>

The custom domains API endpoint is realm specific, requiring one of the following realm identifiers:

| Realm identifier | Description                                   |
| ---------------- | --------------------------------------------- |
| `root`           | Top-level realm used by tenant administrators |
| `alpha`          | Alpha realm used by customers or employees    |
| `bravo`          | Bravo realm used by customers or employees    |

To view all the custom domains in your tenant environment, make three separate requests to the custom domains API endpoint, one for each realm identifier.

## Authenticate to the custom domains API endpoint

To authenticate to the custom domains API endpoint, use an [access token](../developer-docs/authenticate-to-rest-api-with-access-token.html) created with the following scope:

| Scope                    | Description                                     |
| ------------------------ | ----------------------------------------------- |
| `fr:idc:custom-domain:*` | Full access to the custom domains API endpoint. |

## View custom domains

Make a GET request to the `/environment/custom-domains` endpoint to view the domains or subdomains that you can use to access a realm.

To view the custom domain configuration for a realm:

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) created with the `fr:idc:custom-domain:*` scope.

2. Get the custom domain configuration from the `/environment/custom-domains` endpoint:

   ```shell
   $ curl \
   --request GET 'https://<tenant-env-fqdn>/environment/custom-domains/<realm>' \(1)(2)
   --header 'Authorization: Bearer <access-token>'(3)
   ```

   |       |                                                                                                                                                 |
   | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
   | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                            |
   | **2** | Replace \<realm> with one of the realm identifiers listed in [Custom domains API endpoint](#custom-domains-api-endpoint). For example, `alpha`. |
   | **3** | Replace \<access-token> with the access token.                                                                                                  |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "domains": [
   >         "customers.mycompany.co.uk"
   >     ]
   > }
   > ```

## Update custom domains

Make a PUT request to the `/environment/custom-domains` endpoint to set or update the domains or subdomains that you can use to access a realm.

To update the custom domain configuration for a realm:

1. Review the existing custom domain configuration for the realm. Learn more in [View custom domains](#view-custom-domains).

2. Adapt the custom domain configuration to suit your use case. Learn more in [Configure customer-friendly domain names](custom-domains.html).

   |   |                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Before removing a domain or subdomain from the configuration, you must first update any existing applications that rely on that domain or subdomain. |

3. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) created with the `fr:idc:custom-domain:*` scope.

4. Replace the existing custom domain configuration with the custom domain configuration you adapted in step 2:

   ```shell
   $ curl \
   --request PUT 'https://<tenant-env-fqdn>/environment/custom-domains/<realm>' \(1)(2)
   --header 'Authorization: Bearer <access-token>' \(3)
   --header 'Content-Type: application/json' \
   --data '<custom-domains-configuration>'(4)
   ```

   |       |                                                                                                                                                                                                                                                                                                                                                                     |
   | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                                                                                                                                                                                |
   | **2** | Replace \<realm> with one of the realm identifiers listed in [Custom domains API endpoint](#custom-domains-api-endpoint). For example, `alpha`.                                                                                                                                                                                                                     |
   | **3** | Replace \<access-token> with the access token.                                                                                                                                                                                                                                                                                                                      |
   | **4** | Replace \<custom-domains-configuration> with a JSON array of custom domains. For example, the following configuration adds a new subdomain `customers.mycompany.com` to the configuration example used in [View custom domains](#view-custom-domains).```json
   {
       "domains": [
           "customers.mycompany.co.uk",
           "customers.mycompany.com"
       ]
   }
   ``` |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "domains": [
   >         "customers.mycompany.co.uk",
   >         "customers.mycompany.com"
   >     ]
   > }
   > ```

---

---
title: Manage server certificates using the admin console
description: Manage self-hosted SSL certificates for Advanced Identity Cloud using the admin console
component: pingoneaic
page_id: pingoneaic:realms:server-certificates-ui
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/server-certificates-ui.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/ssl-certificates-self-managed-ui.adoc", "realms:ssl-certificates-self-managed-ui.adoc"]
section_ids:
  manage-csrs-and-certificates: Manage CSRs and certificates
  create-a-certificate-using-the-ui: Create a certificate using the admin console
  create-a-csr-using-the-ui: "Task 1: Create a CSR"
  generate-a-signed-certificate-and-create-a-certificate-chain-3: "Task 2: Generate a signed certificate and create a certificate chain"
  install-the-certificate-using-the-ui: "Task 3: Install the certificate"
---

# Manage server certificates using the admin console

You can find background information on self-managed certificates in PingOne Advanced Identity Cloud in [Self-managed certificates](server-certificates.html#self-managed-certificates).

## Manage CSRs and certificates

You can manage your own CSRs and certificates using *SSL configurations* in the Advanced Identity Cloud admin console. There are broadly two types of SSL configuration:

* **Pending:** The SSL configuration has been used to generate a private key and a CSR, but hasn't been updated with a certificate yet.

* **Complete:** The SSL configuration has been successfully updated with a certificate.

To manage SSL configurations:

1. In the Advanced Identity Cloud admin console, open the TENANT menu (upper right), then go to [icon: settings, set=material, size=inline] Tenant Settings > Global Settings > SSL Configurations.

2. The SSL Configurations page lists any SSL configurations, including any created using the API:

   * Pending SSL configurations display a Pending status and an Add Certificate button.

   * Complete SSL configurations display an Active, Inactive, Expires Soon, or Expired status and a certificate expiration date.

3. To create a new SSL configuration and CSR, follow the instructions in [Task 1: Create a CSR](#create-a-csr-using-the-ui).

4. Review any pending SSL configurations:

   * To continue the set up of a certificate using a pending SSL configuration, follow the instructions in:

     * [Task 2: Generate a signed certificate and create a certificate chain](#generate-a-signed-certificate-and-create-a-certificate-chain-3)

     * [Task 3: Install the certificate](#install-the-certificate-using-the-ui)

   * To delete a pending SSL configuration:

     1. Click its delete icon ([icon: delete, set=material, size=inline]).

     2. In the Delete SSL Configuration? modal, click Delete.

5. Review any complete SSL configurations:

   * To renew a certificate:

     1. Click the SSL configuration's ellipsis icon ([icon: more_horiz, set=material, size=inline]), then click [icon: refresh, set=material, size=inline] Renew or [icon: list_alt, set=material, size=inline] View Details > Renew.

     2. Follow the instructions in [Task 1: Create a CSR](#create-a-csr-using-the-ui).

   * To view information about a certificate:

     1. Click the SSL configuration's ellipsis icon ([icon: more_horiz, set=material, size=inline]), then click [icon: list_alt, set=material, size=inline] View Details.

     2. The Certificate Details modal displays basic information about the certificate:

        * Valid From: The valid-from date of the certificate.

        * Expires: The expiration date of the certificate.

        * Status: The status of the certificate (Active, Inactive, Expires Soon, or Expired).

        * Domains: The domains secured by the certificate.

        * Created: The creation date of the certificate's CSR (only shown for tenant-generated CSRs).

   * To activate or deactivate a certificate:

     * To activate an inactive certificate, click the SSL configuration's ellipsis icon ([icon: more_horiz, set=material, size=inline]), then click [icon: power_settings_new, set=material, size=inline] Activate.

     * To deactivate an active certificate, click the SSL configuration's ellipsis icon ([icon: more_horiz, set=material, size=inline]), then click [icon: power_settings_new, set=material, size=inline] Deactivate.

       |   |                                                                                                             |
       | - | ----------------------------------------------------------------------------------------------------------- |
       |   | It takes a few minutes for a certificate to be activated or deactivated in the environment's load balancer. |

   * To delete a certificate:

     1. Click the SSL configuration's ellipsis icon ([icon: more_horiz, set=material, size=inline]), then click [icon: delete, set=material, size=inline]Delete.

     2. In the Delete SSL Configuration? modal, click Delete.

## Create a certificate using the admin console

You can create certificates using a private key the tenant generates for you and which is retained in the tenant. The benefit of this approach is there is no risk of accidentally leaking your private key as it never leaves the tenant. However, with this approach, you can only install a signed certificate on the same tenant from which you requested the CSR.

|   |                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The admin console supports creating a certificate only using a tenant-generated private key. To create a certificate using your own private key, use the API. Learn more in [Create a certificate using a locally generated private key](server-certificates-api.html#create-a-certificate-using-a-locally-generated-private-key). |

### Task 1: Create a CSR

In this step, you create a certificate signing request (CSR). You'll need this in the next step to create a self-signed certificate or to send to your preferred SSL certificate provider to create a CA-signed certificate.

1. In the Advanced Identity Cloud admin console, open the TENANT menu (upper right), then go to [icon: settings, set=material, size=inline] Tenant Settings > Global Settings > SSL Configurations.

2. Click [icon: add, set=material, size=inline] New SSL Configuration.

3. In the New SSL Configuration modal:

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | For CSR field definitions, learn more in [CSR field reference](ssl-certificate-reference.html). |

   1. Enter a Primary Domain (CN).

   2. (Optional) Add Subject Alternative Domains (SANs):

      1. Click the [icon: add, set=material, size=inline] button located to the right of the Primary Domain (CN) field to add a Subject Alternative Domain (SAN) field.

      2. Enter a SAN in the new field.

      3. Repeat the previous two steps to add as many SANs as you need.

   3. Enter an Organization and a Country.

   4. Select an Encryption Algorithm from RSA (default) or ECDSA.

   5. (Optional) Add additional CSR fields:

      1. Click Show additional settings to display additional CSR fields.

      2. (Optional) Select Extended Validation Certificate if you intend to request an [Extended Validation (EV) certificate](server-certificates.html#dv-and-ev-certificates) from your preferred SSL certificate provider. When Extended Validation Certificate is selected, these additional CSR fields become mandatory:

         * Jurisdiction City

         * Jurisdiction Country

         * Jurisdiction State

         * Serial Number

         * Business Category

      3. Enter as many additional CSR field values as you need, and if you checked Extended Validation Certificate in the previous step, enter the mandatory CSR field values.

   6. Click Generate Certificate Signing Request. The New SSL Configuration modal closes and a success modal opens.

4. In the success modal:

   1. Click the copy button ([icon: copy, set=material, size=inline]) to copy the CSR content in the Certificate Signing Request field to your clipboard.

   2. Transfer the CSR content in the clipboard to somewhere safe until you use it in the next step to create a certificate.

      |   |                                                                   |
      | - | ----------------------------------------------------------------- |
      |   | When you close the modal, the CSR content is not available again. |

   3. Click Done to close the modal.

5. Confirm the new pending SSL configuration is in the list of SSL configurations.

### Task 2: Generate a signed certificate and create a certificate chain

In this step, you create a CA-signed or self-signed certificate, then create a PEM-formatted certificate chain.

1. Create a certificate from the CSR in one of these ways:

   * **CA-signed certificate**:\
     Supply the CSR to your preferred SSL certificate provider so they can generate a CA-signed certificate. Your SSL certificate provider should provide you with a signed certificate and a CA certificate. They may also provide intermediary certificates.

   * **Self-signed certificate**:\
     Use OpenSSL to [create a self-signing CA certificate and a self-signed certificate](server-certificates-utility-tasks.html#create-a-self-signing-ca-certificate-and-a-self-signed-certificate).

2. Combine your signed certificate and CA certificate into a certificate chain and save it in the local file `chain.pem`. If you used an SSL certificate provider, add any intermediary certificates into `chain.pem` too, inserted between your signed certificate and the CA certificate:

   ```none
   $ cat cert.pem [inter.cert.pem ...] ca.cert.pem > chain.pem
   ```

   The following is an example of what the certificate chain might look like:

   ```none
   -----BEGIN CERTIFICATE-----
   content of your signed certificate
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   content of an optional intermediate CA certificate
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   content of a CA certificate
   -----END CERTIFICATE-----
   ```

### Task 3: Install the certificate

In this step, you install the certificate in the tenant environment where you created the CSR request.

1. In the Advanced Identity Cloud admin console, open the TENANT menu (upper right), then go to [icon: settings, set=material, size=inline] Tenant Settings > Global Settings > SSL Configurations.

2. Find the pending SSL configuration that generated your CSR, then click [icon: add, set=material, size=inline] Add Certificate.

3. In the Add Certificate modal:

   1. Enter the certificate chain using one of these options:

      * Click Browse to select a local file that contains the certificate chain.

      * Paste the certificate chain content directly into the text field.

   2. Click Add Certificate.

4. Confirm the SSL configuration is now fully configured and active.

   |   |                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------ |
   |   | It takes a few minutes for the certificate to be installed and activated in the environment's load balancer. |

---

---
title: Manage server certificates using the API
description: Manage SSL certificates using the Advanced Identity Cloud REST API for custom domain security
component: pingoneaic
page_id: pingoneaic:realms:server-certificates-api
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/server-certificates-api.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["realms:ssl-certificates-self-managed.adoc", "realms:ssl-certificates-self-managed-api.adoc"]
section_ids:
  certificate-api-endpoints: Certificate API endpoints
  authenticate-to-certificate-api-endpoints: Authenticate to certificate API endpoints
  server-certificates-api-prerequisites: Prerequisites
  create-a-certificate-using-a-tenant-generated-private-key: Create a certificate using a tenant-generated private key
  create-a-csr-using-the-certificate-api: "Task 1: Create a CSR using the certificate API"
  generate-a-signed-certificate-and-create-a-certificate-chain-1: "Task 2: Generate a signed certificate and create a certificate chain"
  install-the-certificate: "Task 3: Install the certificate"
  create-a-certificate-using-a-locally-generated-private-key: Create a certificate using a locally generated private key
  create-a-csr-using-the-command-line: "Task 1: Create a CSR using the command line"
  generate-a-signed-certificate-and-create-a-certificate-chain-2: "Task 2: Generate a signed certificate and create a certificate chain"
  install-the-certificate-and-private-key: "Task 3: Install the certificate and private key"
  list-certificates: List certificates
  activate-a-certificate: Activate a certificate
  deactivate-a-certificate: Deactivate a certificate
  delete-a-certificate: Delete a certificate
---

# Manage server certificates using the API

You can find background information on self-managed certificates in PingOne Advanced Identity Cloud in [Self-managed certificates](server-certificates.html#self-managed-certificates).

## Certificate API endpoints

To use the certificate API, learn more in the following Advanced Identity Cloud API endpoints:

* [CSRs](https://docs.pingidentity.com/pingoneaic/_attachments/api/#tag/CSRs) API endpoint

* [Certificates](https://docs.pingidentity.com/pingoneaic/_attachments/api/#tag/Certificates) API endpoint

## Authenticate to certificate API endpoints

To authenticate to certificate API endpoints, use an [access token](../developer-docs/authenticate-to-rest-api-with-access-token.html) created with one of the following scopes:

| Scope                     | Description                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `fr:idc:certificate:*`    | Full access to certificate API endpoints. Use this scope to create, activate, deactivate, or delete certificates.          |
| `fr:idc:certificate:read` | Read-only access to certificate API endpoints. Use this scope if you only need to [List certificates](#list-certificates). |

## Prerequisites

You need the [openssl](https://www.openssl.org/) and [jq](https://jqlang.github.io/jq) command-line tools to run some of the commands. You can find installation instructions for your particular package manager in <https://command-not-found.com/openssl> and <https://command-not-found.com/jq>.

## Create a certificate using a tenant-generated private key

You can create certificates using a private key the tenant generates for you and which is retained in the tenant. The benefit of this approach is there is no risk of accidentally leaking your private key as it never leaves the tenant. However, with this approach, you can only install a signed certificate on the same tenant from which you requested the CSR.

### Task 1: Create a CSR using the certificate API

In this step, you create a certificate signing request (CSR). You'll need this in the next step to create a self-signed certificate or to send to your preferred SSL certificate provider to create a CA-signed certificate.

1. Create a JSON payload of CSR information:

   1. Adapt the following example configuration to suit your company:

      ```json
      {
        "commonName": "www.pingidentity.com", (1)
        "organization": "Ping Identity Corporation",  (1)
        "organizationalUnit": "IT", (1)
        "country": "US", (1)
        "streetAddress": "1001 17th Street", (1)
        "city": "Denver", (1)
        "postalCode": "80202", (1)
        "email": "example.user@pingidentity.com", (1)
        "businessCategory": "Private Organization", (2)
        "serialNumber": "3463471", (2)
        "jurisdictionCountry": "US", (2)
        "jurisdictionLocality": "Wilmington", (2)
        "jurisdictionState": "Delaware", (2)
        "subjectAlternativeNames": ["support.pingidentity.com", "labs.pingidentity.com"] (3)
      }
      ```

      |       |                                                                                                                                                                                                                                                                                                                                                            |
      | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | **1** | Configures the [standard CSR fields](ssl-certificate-reference.html#standard-csr-fields). All standard fields are included for demonstration, but this is not strictly necessary. Consult your SSL certificate provider's documentation for the minimum required fields. Remove any fields that are not used rather than include them with an empty value. |
      | **2** | (Optional) Configures the [EV CSR fields](ssl-certificate-reference.html#ev-csr-fields). All EV fields are included for demonstration, but only `businessCategory`, `serialNumber`, and `jurisdictionCountryName` are required.                                                                                                                            |
      | **3** | (Optional) Configures the subject alternative names (SANs). SANs are domains the certificate will secure in addition to the `commonName`. Wildcards values in SAN domains are not permitted.                                                                                                                                                               |

   2. Save your adapted configuration in a local file called `csr-payload.json`.

2. In the tenant environment where you intend to install the certificate:

   1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) created with the `fr:idc:certificate:*` scope.

   2. Create a CSR using the `/environment/csrs` endpoint:

      ```shell
      $ curl \
      --request POST 'https://<tenant-env-fqdn>/environment/csrs' \ (1)
      --header 'Authorization: Bearer <access-token>' \ (2)
      --header 'Content-Type: application/json' \
      --data "$(< csr-payload.json)" \ (3)
      > tee csr-result.json (4)
      ```

      |       |                                                                      |
      | ----- | -------------------------------------------------------------------- |
      | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment. |
      | **2** | Replace \<access-token> with the access token.                       |
      | **3** | The request body is populated with the output of `csr-payload.json`. |
      | **4** | The response is stored in a local file called `csr-result.json`.     |

      > **Collapse: Show response**
      >
      > ```json
      > {
      >   "algorithm": "SHA256-RSA",
      >   "createdDate": "2024-04-24T17:11:42Z",
      >   "id": "4f1caf97-bd2f-4d30-8e68-682fa10d27ff", (1)
      >   "request": "-----BEGIN CERTIFICATE REQUEST-----\nMIIDTTCCAjUCAQAwgbcx ...8<... L3f7aPgXtR6nxPS/oTSl\n-----END CERTIFICATE REQUEST-----\n",
      >   "subject": "CN=www.pingidentity.com,OU=IT,O=Ping Identity Corporation,STREET=1001 17th Street,L=Denver,C=US",
      >   "subjectAlternativeNames": [
      >     "support.pingidentity.com",
      >     "labs.pingidentity.com"
      >   ]
      > }
      > ```
      >
      > |       |                                                                                                                                                                                                   |
      > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      > | **1** | The CSR ID is represented by the `id` key. You need this ID in a later step to update the CSR with the signed certificate. In this example, the CSR ID is `4f1caf97-bd2f-4d30-8e68-682fa10d27ff`. |

   3. Extract the CSR from the `request` key of the JSON object in `csr-result.json`:

      ```shell
      $ jq -r .request csr-result.json > csr.pem
      ```

   4. Review the contents of the CSR in `csr.pem`:

      * For an example of a CSR, learn more in [PEM-formatted certificate examples](ssl-certificate-reference.html#certificate-examples).

      * To check the information in the CSR, learn more in [Check a CSR](server-certificates-utility-tasks.html#server-certificates-check-a-csr).

### Task 2: Generate a signed certificate and create a certificate chain

In this step, you create a CA-signed or self-signed certificate, then create a PEM-formatted certificate chain.

1. Create a certificate from the CSR in one of these ways:

   * **CA-signed certificate**:\
     Supply the CSR to your preferred SSL certificate provider so they can generate a CA-signed certificate. Your SSL certificate provider should provide you with a signed certificate and a CA certificate. They may also provide intermediary certificates.

   * **Self-signed certificate**:\
     Use OpenSSL to [create a self-signing CA certificate and a self-signed certificate](server-certificates-utility-tasks.html#create-a-self-signing-ca-certificate-and-a-self-signed-certificate).

2. Combine your signed certificate and CA certificate into a certificate chain and save it in the local file `chain.pem`. If you used an SSL certificate provider, add any intermediary certificates into `chain.pem` too, inserted between your signed certificate and the CA certificate:

   ```shell
   $ cat cert.pem [inter.cert.pem ...] ca.cert.pem > chain.pem
   ```

   The following is an example of what the certificate chain might look like:

   ```shell
   -----BEGIN CERTIFICATE-----
   content of your signed certificate
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   content of an optional intermediate CA certificate
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   content of a CA certificate
   -----END CERTIFICATE-----
   ```

### Task 3: Install the certificate

In this step, you install the certificate in the tenant environment where you created the CSR request.

1. Create a JSON payload of certificate information:

   1. Add the certificate chain to a JSON object:

      ```shell
      $ jq -Rs '{certificate: .}' ./chain.pem > payload.json
      ```

      Summary of command:

      * Creates a JSON object using the `jq` command. Learn more in [Prerequisites](#server-certificates-api-prerequisites).

      * Adds a `certificate` key to the JSON object set with the contents of `chain.pem` as a single line.

      * Saves the JSON object in a local file called `payload.json`.

   2. The contents of `payload.json` should look something like this:

      ```json
      {
        "certificate": "-----BEGIN CERTIFICATE-----\ncontent of your signed certificate\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\ncontent of an optional intermediate CA certificate\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\ncontent of your CA certificate\n-----END CERTIFICATE-----\n"
      }
      ```

2. In the tenant environment where you created the CSR request in step 2 of task 1 and intend to install the certificate:

   1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) created with the `fr:idc:certificate:*` scope.

   2. Upload the certificate using the `/environment/csrs` endpoint:

      ```shell
      $ curl \
      --request PATCH 'https://<tenant-env-fqdn>/environment/csrs/<csr-id>' \(1) (2)
      --header 'Authorization: Bearer <access-token>' \(3)
      --header 'Content-Type: application/json' \
      --data "$(< payload.json)" (4)
      ```

      |       |                                                                      |
      | ----- | -------------------------------------------------------------------- |
      | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment. |
      | **2** | Replace \<csr-id> with the CSR ID you noted in step 1, 2b.           |
      | **3** | Replace \<access-token> with the access token.                       |
      | **4** | The request body is populated with the output of `payload.json`.     |

      > **Collapse: Show response**
      >
      > ```json
      > {
      >     "algorithm": "SHA256-RSA",
      >     "certificateID": "ccrt-d7bad9b1-65fa-48ce-b56a-bd320a75d477", (1)
      >     "createdDate": "2024-05-03T12:49:29Z",
      >     "id": "11c5419e-c5de-466d-a7e7-d65afbde1217",
      >     "request": "-----BEGIN CERTIFICATE REQUEST-----\nMIIDTTCCAjUCAQAwgbcx ...8<... L3f7aPgXtR6nxPS/oTSl\n-----END CERTIFICATE REQUEST-----\n",
      >     "subject": "CN=www.pingidentity.com,OU=IT,O=Ping Identity Corporation,STREET=1001 17th Street,L=Denver,C=US",
      >     "subjectAlternativeNames": [
      >         "support.pingidentity.com",
      >         "labs.pingidentity.com"
      >     ]
      > }
      > ```
      >
      > |       |                                                                                                                                                                                                                        |
      > | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      > | **1** | The certificate ID is represented by the `certificateID` key. You need this ID to activate, deactivate, or delete the certificate. In this example, the certificate ID is `ccrt-d7bad9b1-65fa-48ce-b56a-bd320a75d477`. |

   3. Get the certificate information using the `/environment/certificates` endpoint:

      ```shell
      $ curl \
      --request GET 'https://<tenant-env-fqdn>/environment/certificates/<certificate-id>' \(1) (2)
      --header 'Authorization: Bearer <access-token>' \(3)
      --header 'Content-Type: application/json'
      ```

      |       |                                                                                   |
      | ----- | --------------------------------------------------------------------------------- |
      | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.              |
      | **2** | Replace \<certificate-id> with the certificate ID you noted in the previous step. |
      | **3** | Replace \<access-token> with the access token.                                    |

      > **Collapse: Show response**
      >
      > ```json
      > {
      >     "active": false, (1)
      >     "expireTime": "2024-06-02T12:58:01Z",
      >     "id": "ccrt-d7bad9b1-65fa-48ce-b56a-bd320a75d477", (2)
      >     "issuer": "CN=Self-signing CA",
      >     "live": false,  (3)
      >     "subject": "CN=www.pingidentity.com,OU=IT,O=Ping Identity Corporation,STREET=1001 17th Street,L=Denver,C=US,1.2.840.113549.1.9.1=#0c1d6578616d706c652e757365724070696e676964656e746974792e636f6d",
      >     "subjectAlternativeNames": [
      >         "support.pingidentity.com",
      >         "labs.pingidentity.com"
      >     ],
      >     "validFromTime": "2024-05-03T12:58:01Z"
      > }
      > ```
      >
      > |       |                                                                                                                                                                                                                                                                                                                                                                                       |
      > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      > | **1** | The `active` key is set to `false` which indicates that the certificate is not active. This is the default value for a new certificate.                                                                                                                                                                                                                                               |
      > | **2** | The certificate ID is represented by the `id` key. This is the same ID as in the `certificateID` key in the CSR response from the previous step.                                                                                                                                                                                                                                      |
      > | **3** | The `live` key returns the value `false`, which indicates the certificate is not installed in the environment's load balancer. In the next step, you will set the `active` key to `true`. This triggers an asynchronous process that installs the certificate in the environment's load balancer. When the asynchronous process is complete, the `live` key returns the value `true`. |

   4. [Activate the certificate](#activate-a-certificate) to install it in the environment's load balancer.

## Create a certificate using a locally generated private key

You can create certificates using a private key you generate locally and retain access to. The benefit of this approach is once you have signed the certificate, you can install it with the private key on as many tenants as you need. However, to use this approach, you must have robust security practices when handling the private key.

### Task 1: Create a CSR using the command line

In this step, you create a certificate signing request (CSR). You'll need this in the next step to create a self-signed certificate or to send to your preferred SSL certificate provider to create a CA-signed certificate.

1. Create an OpenSSL CSR configuration file:

   1. Adapt the following example configuration to suit your company:

      ```ini
      [ req ] (1)
      prompt             = no (2)
      distinguished_name = req_distinguished_name
      req_extensions     = req_ext (5)

      [ req_distinguished_name ]

      # Standard CSR fields (3)
      commonName             = www.pingidentity.com
      organizationName       = Ping Identity Corporation
      organizationalUnitName = IT
      countryName            = US
      streetAddress          = 1001 17th Street
      localityName           = Denver
      stateOrProvinceName    = Colorado
      postalCode             = 80202
      emailAddress           = example.user@pingidentity.com

      # EV CSR fields (4)
      businessCategory                = Private Organization
      serialNumber                    = 3463471
      jurisdictionCountryName         = US
      jurisdictionLocalityName        = Wilmington
      jurisdictionStateOrProvinceName = Delaware

      [ req_ext ] (5)
      subjectAltName = @alt_names

      [alt_names] (5)
      DNS.1 = support.pingidentity.com
      DNS.2 = labs.pingidentity.com
      ```

      |       |                                                                                                                                                                                                                                                                                                                                                            |
      | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | **1** | Configures the `openssl req` command.                                                                                                                                                                                                                                                                                                                      |
      | **2** | Configures the `openssl req` command to use the CSR values supplied in this configuration file instead of prompting for them.                                                                                                                                                                                                                              |
      | **3** | Configures the [standard CSR fields](ssl-certificate-reference.html#standard-csr-fields). All standard fields are included for demonstration, but this is not strictly necessary. Consult your SSL certificate provider's documentation for the minimum required fields. Remove any fields that are not used rather than include them with an empty value. |
      | **4** | (Optional) Configures the [EV CSR fields](ssl-certificate-reference.html#ev-csr-fields). All EV fields are included for demonstration, but only `businessCategory`, `serialNumber`, and `jurisdictionCountryName` are required.                                                                                                                            |
      | **5** | (Optional) Configures the subject alternative names (SANs). SANs are domains the certificate will secure in addition to the `commonName`. Wildcard values in SAN domains are not permitted.                                                                                                                                                                |

   2. Save your adapted configuration in a local file called `openssl-csr.conf`.

2. Create a CSR:

   1. Generate a CSR and private key pair using the configuration in `openssl-csr.conf`:

      ```shell
      $ openssl req \
      -nodes -newkey rsa:2048 \
      -out csr.pem -keyout key.pem \
      -config openssl-csr.conf
      ```

   2. Review the CSR and private key, which are respectively in the local files `csr.pem` and `key.pem`:

      * For examples of a CSR and private key, learn more in [PEM-formatted certificate examples](ssl-certificate-reference.html#certificate-examples).

      * To check the information in the CSR, learn more in [Check a CSR](server-certificates-utility-tasks.html#server-certificates-check-a-csr).

### Task 2: Generate a signed certificate and create a certificate chain

In this step, you create a CA-signed or self-signed certificate, then create a PEM-formatted certificate chain.

1. Create a certificate from the CSR in one of these ways:

   * **CA-signed certificate**:\
     Supply the CSR to your preferred SSL certificate provider so they can generate a CA-signed certificate. Your SSL certificate provider should provide you with a signed certificate and a CA certificate. They may also provide intermediary certificates.

   * **Self-signed certificate**:\
     Use OpenSSL to [create a self-signing CA certificate and a self-signed certificate](server-certificates-utility-tasks.html#create-a-self-signing-ca-certificate-and-a-self-signed-certificate).

2. Combine your signed certificate and CA certificate into a certificate chain and save it in the local file `chain.pem`. If you used an SSL certificate provider, add any intermediary certificates into `chain.pem` too, inserted between your signed certificate and the CA certificate:

   ```shell
   $ cat cert.pem [inter.cert.pem ...] ca.cert.pem > chain.pem
   ```

   The following is an example of what the certificate chain might look like:

   ```shell
   -----BEGIN CERTIFICATE-----
   content of your signed certificate
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   content of an optional intermediate CA certificate
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   content of a CA certificate
   -----END CERTIFICATE-----
   ```

### Task 3: Install the certificate and private key

In this step, you install the certificate and private key in your tenant environments.

1. Create a JSON payload of certificate information:

   1. Add the certificate chain and private key to a JSON object:

      ```shell
      $ (jq -Rs '{certificate: .}' ./chain.pem; jq -Rs '{privateKey: .}' ./key.pem)  | jq -s add  > payload.json
      ```

      Summary of command:

      * Creates a JSON object using the `jq` command. Learn more in [Prerequisites](#server-certificates-api-prerequisites).

      * Adds a `certificate` key to the JSON object set with the contents of `chain.pem` as a single line.

      * Adds a `privateKey` key to the JSON object set with the contents of `key.pem` as a single line.

      * Saves the JSON object in a local file called `payload.json`.

   2. The contents of `payload.json` should look something like this:

      ```json
      {
        "certificate": "-----BEGIN CERTIFICATE-----\ncontent of your signed certificate\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\ncontent of an optional intermediate CA certificate\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\ncontent of your CA certificate\n-----END CERTIFICATE-----\n",
        "privateKey": "-----BEGIN ENCRYPTED PRIVATE KEY-----\ncontent of your private key\n-----END ENCRYPTED PRIVATE KEY-----\n"
      }
      ```

2. In each tenant environment where you want to install the certificate:

   1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) created with the `fr:idc:certificate:*` scope.

   2. Upload the certificate using the `/environment/certificates` endpoint:

      ```shell
      $ curl \
      --request POST 'https://<tenant-env-fqdn>/environment/certificates' \(1)
      --header 'Authorization: Bearer <access-token>' \(2)
      --header 'Content-Type: application/json' \
      --data "$(< payload.json)" (3)
      ```

      |       |                                                                      |
      | ----- | -------------------------------------------------------------------- |
      | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment. |
      | **2** | Replace \<access-token> with the access token.                       |
      | **3** | The request body is populated with the output of `payload.json`.     |

      > **Collapse: Show response**
      >
      > ```json
      > {
      >     "active": false, (1)
      >     "expireTime": "2024-06-01T15:14:54Z",
      >     "id": "ccrt-134425bc-6203-48fe-bbef-b17792faf972", (2)
      >     "issuer": "CN=Self-signing CA",
      >     "live": false, (3)
      >     "subject": "SERIALNUMBER=3463471,CN=www.pingidentity.com,OU=IT,O=Ping Identity Corporation,POSTALCODE=80202,STREET=1001 17th Street,L=Denver,ST=Colorado,C=US,1.3.6.1.4.1.311.60.2.1.2=#130844656c6177617265,1.3.6.1.4.1.311.60.2.1.1=#130a57696c6d696e67746f6e,1.3.6.1.4.1.311.60.2.1.3=#13025553,2.5.4.15=#131450726976617465204f7267616e697a6174696f6e,1.2.840.113549.1.9.1=#0c1d6578616d706c652e757365724070696e676964656e746974792e636f6d",
      >     "subjectAlternativeNames": [
      >         "support.pingidentity.com",
      >         "labs.pingidentity.com"
      >     ],
      >     "validFromTime": "2024-05-02T15:14:54Z"
      > }
      > ```
      >
      > |       |                                                                                                                                                                                                                                                                                                                                                                                       |
      > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      > | **1** | The `active` key is set to `false`, which indicates the certificate is not active. This is the default value for a new certificate.                                                                                                                                                                                                                                                   |
      > | **2** | The certificate ID is represented by the `id` key. You need this ID to activate, deactivate, or delete the certificate. In this example, the certificate ID is `ccrt-134425bc-6203-48fe-bbef-b17792faf972`.                                                                                                                                                                           |
      > | **3** | The `live` key returns the value `false`, which indicates the certificate is not installed in the environment's load balancer. In the next step, you will set the `active` key to `true`. This triggers an asynchronous process that installs the certificate in the environment's load balancer. When the asynchronous process is complete, the `live` key returns the value `true`. |

   3. [Activate the certificate](#activate-a-certificate) to install it in the environment's load balancer.

## List certificates

List certificates to view all certificates in a tenant environment. Certificates can be active (installed in the environment's load balancer) or inactive (not installed in the environment's load balancer). The list includes any certificates the Ping Identity support team added to the environment.

In any tenant environment

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) created with the `fr:idc:certificate:read` scope.

2. Get a list of certificates from the `/environment/certificates` endpoint:

   ```shell
   $ curl \
   --request GET 'https://<tenant-env-fqdn>/environment/certificates' \(1)
   --header 'Authorization: Bearer <access-token>' \(2)
   --header 'Content-Type: application/json'
   ```

   |       |                                                                      |
   | ----- | -------------------------------------------------------------------- |
   | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment. |
   | **2** | Replace \<access-token> with the access token.                       |

   > **Collapse: Show response**
   >
   > ```json
   > [
   >     {
   >         "active": false,
   >         "expireTime": "2024-06-01T15:14:54Z",
   >         "id": "ccrt-4ac300e5-7e0a-4d34-a42c-c41a076458da",
   >         "issuer": "CN=Self-signing CA",
   >         "live": false,
   >         "subject": "SERIALNUMBER=3463471,CN=www.pingidentity.com,OU=IT,O=Ping Identity Corporation,POSTALCODE=80202,STREET=1001 17th Street,L=Denver,ST=Colorado,C=US,1.3.6.1.4.1.311.60.2.1.2=#130844656c6177617265,1.3.6.1.4.1.311.60.2.1.1=#130a57696c6d696e67746f6e,1.3.6.1.4.1.311.60.2.1.3=#13025553,2.5.4.15=#131450726976617465204f7267616e697a6174696f6e,1.2.840.113549.1.9.1=#0c1d6578616d706c652e757365724070696e676964656e746974792e636f6d",
   >         "subjectAlternativeNames": [
   >             "support.pingidentity.com",
   >             "labs.pingidentity.com"
   >         ],
   >         "validFromTime": "2024-05-02T15:14:54Z"
   >     },
   >     {
   >         "active": false,
   >         "expireTime": "2024-06-02T12:58:01Z",
   >         "id": "ccrt-d7bad9b1-65fa-48ce-b56a-bd320a75d477",
   >         "issuer": "CN=Self-signing CA",
   >         "live": false,
   >         "subject": "CN=www.pingidentity.com,OU=IT,O=Ping Identity Corporation,STREET=1001 17th Street,L=Denver,C=US,1.2.840.113549.1.9.1=#0c1d6578616d706c652e757365724070696e676964656e746974792e636f6d",
   >         "subjectAlternativeNames": [
   >             "support.pingidentity.com",
   >             "labs.pingidentity.com"
   >         ],
   >         "validFromTime": "2024-05-03T12:58:01Z"
   >     }
   > ]
   > ```

## Activate a certificate

Activate a certificate to install it in a tenant environment's load balancer. If you activate more than one certificate at once, the environment's load balancer will serve the most appropriate for the requested hostname. This lets you rotate certificates by installing and activating a new certificate before an older certificate expires.

In any tenant environment:

1. [List the certificates in the environment](#list-certificates) and examine the response to find the ID of the certificate (represented as the JSON `id` key) you intend to activate.

2. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) created with the `fr:idc:certificate:*` scope.

3. Update the certificate by patching the JSON `active` key to `true`:

   ```shell
   $ curl \
   --request PATCH 'https://<tenant-env-fqdn>/environment/certificates/<certificate-id>' \(1) (2)
   --header 'Authorization: Bearer <access-token>' \(3)
   --header 'Content-Type: application/json' \
   --data '{"active": true}' (4)
   ```

   |       |                                                                              |
   | ----- | ---------------------------------------------------------------------------- |
   | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.         |
   | **2** | Replace \<certificate-id> with the certificate ID you found in step 1.       |
   | **3** | Replace \<access-token> with the access token.                               |
   | **4** | The request body is set with a new value for the JSON `active` key (`true`). |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "active": true,
   >     "expireTime": "2024-06-01T15:14:54Z",
   >     "id": "ccrt-134425bc-6203-48fe-bbef-b17792faf972",
   >     "issuer": "CN=Self-signing CA",
   >     "live": false,
   >     "subject": "SERIALNUMBER=3463471,CN=www.pingidentity.com,OU=IT,O=Ping Identity Corporation,POSTALCODE=80202,STREET=1001 17th Street,L=Denver,ST=Colorado,C=US,1.3.6.1.4.1.311.60.2.1.2=#130844656c6177617265,1.3.6.1.4.1.311.60.2.1.1=#130a57696c6d696e67746f6e,1.3.6.1.4.1.311.60.2.1.3=#13025553,2.5.4.15=#131450726976617465204f7267616e697a6174696f6e,1.2.840.113549.1.9.1=#0c1d6578616d706c652e757365724070696e676964656e746974792e636f6d",
   >     "subjectAlternativeNames": [
   >         "support.pingidentity.com",
   >         "labs.pingidentity.com"
   >     ],
   >     "validFromTime": "2024-05-02T15:14:54Z"
   > }
   > ```

4. An asynchronous process automatically installs the certificate in the environment's load balancer. To check when the asynchronous process has completed, poll the `/environment/certificates` endpoint using the certificate ID until the `live` key in the response changes from `false` to `true`:

   ```shell
   $ curl \
   --request GET 'https://<tenant-env-fqdn>/environment/certificates/<certificate-id>' \(1) (2)
   --header 'Authorization: Bearer <access-token>' \(3)
   --header 'Content-Type: application/json'
   ```

   |       |                                                                       |
   | ----- | --------------------------------------------------------------------- |
   | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.  |
   | **2** | Replace \<certificate-id> with the ID of the certificate you updated. |
   | **3** | Replace \<access-token> with the access token.                        |

   When the asynchronous process has completed and installed the certificate in the environment's load balancer, the response should look like this:

   > **Collapse: Show response**
   >
   > ```json
   > {
   >     "active": true,
   >     "expireTime": "2024-06-01T15:14:54Z",
   >     "id": "ccrt-134425bc-6203-48fe-bbef-b17792faf972",
   >     "issuer": "CN=Self-signing CA",
   >     "live": true,
   >     "subject": "SERIALNUMBER=3463471,CN=www.pingidentity.com,OU=IT,O=Ping Identity Corporation,POSTALCODE=80202,STREET=1001 17th Street,L=Denver,ST=Colorado,C=US,1.3.6.1.4.1.311.60.2.1.2=#130844656c6177617265,1.3.6.1.4.1.311.60.2.1.1=#130a57696c6d696e67746f6e,1.3.6.1.4.1.311.60.2.1.3=#13025553,2.5.4.15=#131450726976617465204f7267616e697a6174696f6e,1.2.840.113549.1.9.1=#0c1d6578616d706c652e757365724070696e676964656e746974792e636f6d",
   >     "subjectAlternativeNames": [
   >         "support.pingidentity.com",
   >         "labs.pingidentity.com"
   >     ],
   >     "validFromTime": "2024-05-02T15:14:54Z"
   > }
   > ```

## Deactivate a certificate

Deactivate a certificate to uninstall it from a tenant environment's load balancer. If you deactivate all certificates in an environment, the load balancer will fall back to using a [Google-managed certificate](server-certificates.html#google-managed-certificates).

To deactivate a certificate, follow the instructions in [Activate a certificate](#activate-a-certificate) with the following changes:

* In step 3, patch the JSON `active` key to `false`.

* In step 4, poll the `/environment/certificates` endpoint until the `live` key in the response changes from `true` to `false`.

## Delete a certificate

Delete a certificate to permanently remove it from a tenant environment.

In any tenant environment:

1. [List the certificates in the environment](#list-certificates) and examine the response to find the ID of the certificate you intend to delete, represented by the `id` key.

2. If you have not done so already, [deactivate the certificate](#deactivate-a-certificate) to uninstall it from the environment's load balancer.

3. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) created with the `fr:idc:certificate:*` scope.

4. Delete the certificate:

   ```shell
   $ curl \
   --request DELETE 'https://<tenant-env-fqdn>/environment/certificates/<certificate-id>' \(1) (2)
   --header 'Authorization: Bearer <access-token>' \(3)
   --header 'Content-Type: application/json'
   ```

   |       |                                                                        |
   | ----- | ---------------------------------------------------------------------- |
   | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.   |
   | **2** | Replace \<certificate-id> with the certificate ID you found in step 1. |
   | **3** | Replace \<access-token> with the access token.                         |

---

---
title: Password policy
description: Configure password policies in Advanced Identity Cloud including expiration, complexity, and forced changes
component: pingoneaic
page_id: pingoneaic:realms:password-policy
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/password-policy.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Customization", "Security", "Realms", "Setup &amp; Configuration"]
page_aliases: ["pingoneaic::policy-password.adoc", "release-notes:rapid-channel/password-timestamps-rapid.adoc"]
section_ids:
  configure-a-password-policy: Configure a password policy
  force-end-user-password-changes: Force end-user password changes
  strategy-1-target-segments-of-end-users: "Strategy 1: Target segments of end users"
  strategy-2-target-oldest-passwords-first: "Strategy 2: Target oldest passwords first"
  password-timestamps: Password timestamps
---

# Password policy

Configure a password policy in PingOne Advanced Identity Cloud when you want a customized rule for creating valid sign-in passwords. The password policy applies to end users who sign in to your registered apps within a realm.

|   |                                                       |
| - | ----------------------------------------------------- |
|   | You can configure only one password policy per realm. |

By default, Advanced Identity Cloud password policy is set to the minimum security requirements established by the National Institute of Standards and Technology (NIST). Any changes you make to the password policy must conform to requirements contained in their guidelines. Learn more in [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-3/).

## Configure a password policy

1. In the Advanced Identity Cloud admin console, go to Security > Password Policy.

2. Choose the realm the password policy will apply to.

3. Edit password policy details.

   |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Password length       | When enabled, the policy requires a password with the specified minimum number of characters. No maximum.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | Cannot include        | Options to restrict the use of any of the following in the policy:- More than two consecutive characters (Example: aaaaaa)

   - Commonly used passwords (Examples: qwerty or 12345678)

   - Values in certain user attributes:

     * In the Forbidden *Realm* realm - User attributes list, select user attributes to validate passwords against.

     * In the Minimum *n* characters for each attribute field, enter a substring length between 3 - 64 to use when validating passwords against user attribute values. The default is 5 characters. |
   | Must contain          | When enabled, the policy requires the use of a specified 1 - 4 of the following:- Upper case letter

   - Lower case letter

   - Number

   - Space, pipe, or special character: ( ! " # $ % & ' ( ) \* + , - . / : ; < = > ? @ \[ \ ] ^ \_ \` { } \~ ) .                                                                                                                                                                                                                                                                                              |
   | Cannot reuse          | When enabled, the policy restricts the end user from reusing their current password and the specified number of previously set passwords.For example, if you set this value to 3, the end user can't reuse their current password or any of their last three passwords. The end user must create a new password that is different from any of those four passwords.                                                                                                                                                                            |
   | Force password change | When enabled, the policy forcibly expires each end-user password after the specified number of days, months, or years have elapsed from when the password was set. To handle expired passwords in an end-user journey, use the `Expired` outcome in the [Identity Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identity-store-decision.html).	Refer to the considerations in Force end-user password changes before using this policy setting.                                                                |

4. Click Save.

## Force end-user password changes

You can combine a [password policy](#configure-a-password-policy) and the [Identity Store Decision node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/identity-store-decision.html) to expire end-user passwords in a journey; the Force password change policy setting lets you define an expiry time interval, which is measured for each end user from when their password was last set.

If you are introducing such a policy for the first time, you may want to process your end users in batches in order to improve messaging about the changes. The following sections describe two high-level strategies to achieve this.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are considering forcing your end users to change their passwords, review the [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-3/). In particular, NIST no longer recommends scheduled password changes; learn more in [Usability Considerations by Authenticator Type](https://pages.nist.gov/800-63-3/sp800-63b.html#102-usability-considerations-by-authenticator-type).The NIST guidelines are continually refined, so you should keep them in mind when setting password policy. |

### Strategy 1: Target segments of end users

Adapt the end-user login journey to use [dynamic groups](../idm-objects/manage-groups.html#add-users-to-group) or user properties to target a segment of end users to reset their password.

**Advantage**: You can segment users any way you like. For example, you may have a set of end users who could struggle with a password reset. You could add a property to each end user in the set and initially exclude end users with that property from a password reset. Then, at a later time, remove the exclusion when support is available for those end users.

**Disadvantage**: Creating new dynamic groups with large numbers of end users can incur a significant performance cost.

### Strategy 2: Target oldest passwords first

Adapt the end-user login journey to target all end users to reset their password, but initially set a very long expiry time interval to target the oldest passwords first. Then periodically reduce the expiry time interval to eventually target all passwords.

**Advantage**: This strategy segments end users by the date of their last password reset. Additionally, end users with the oldest passwords are targeted first.

## Password timestamps

Password timestamps let you view or query when a user password was last changed and when it is set to expire.

The following timestamp fields and properties are available:

| Field name on the user page | Property name in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)* |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Password Last Changed Time  | `passwordLastChangedTime`                                                                                                                              |
| Password Expiration Time    | `passwordExpirationTime`                                                                                                                               |

Example query on `passwordLastChangedTime`

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=passwordLastChangedTime%20ge%20%222024-01-01T21:22:06.274Z%22&_fields=_id"
{
  "result": [
    {
      "_id": "453a73a9-3f50-4b04-8115-f3915fd1dd89",
      "_rev": "fa876a46-82e6-4a11-a3f4-6b4919815ea4-5851"
    }
  ],
  ...
}
```

---

---
title: Realm settings
description: Configure realm details including deactivation, DNS aliases, client-based sessions, and custom domains in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:realms:realm-settings
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/realm-settings.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Features", "Getting started", "Realms"]
page_aliases: ["pingoneaic::concepts-realms.adoc"]
section_ids:
  manage_realm_settings: Manage realm settings
  override_realm_authentication_attributes: Override realm authentication attributes
  switch_realms: Switch realms
---

# Realm settings

Realms are administrative units that group configurations and identities together so that you can manage different sets of identities and applications within the same PingOne Advanced Identity Cloud tenant.

Each realm is fully self-contained and operates independently of other realms within a tenant; the identities and applications in one realm can't access those in another realm.

A typical example of realm management is when a company divides its identities into two realms: one for employees and one for customers, each having a distinct set of identities and registered applications.

## Manage realm settings

1. In the Advanced Identity Cloud admin console, open the Realm menu (upper left).

2. Go to [icon: settings, set=material, size=inline] Realm Settings > Details.

3. On the Details page:

   * The Status bar indicates whether the realm is Active or Inactive.

   * To take the realm out of service, click Deactivate.\
     When a realm is deactivated, users and devices contained in the realm will not be able to access its applications. Identity and app information is still registered to your identity platform.

   * Name: The realm name is non-configurable.

   * (Optional) DNS Aliases: Alternative display names for the realm's URL.

   * Use Client-based Sessions: Enable this option to allow signing and encryption of the JWT in the global session service.

4. To configure a custom domain name, click Custom Domains. Learn more in [Configure customer-friendly domain names](custom-domains.html).

When you're satisfied with your changes, click Save.

## Override realm authentication attributes

It's useful to override realm authentication attributes when you want to adjust the core authentication properties of a realm. For example, you may want to extend the time limit for responding to an authentication verification email.

Under Native Consoles > Access Management, go to Authentication > Settings.

For detailed property information, learn more in [Core authentication attributes](../am-authentication/realm-auth-config.html).

## Switch realms

Switch realms when you want to access identities or applications registered to a realm other than the current realm.

1. In the Advanced Identity Cloud admin console, open the Realm menu (upper left).

2. Click Switch realm.

3. In the Switch Realm dialog box, click Switch.

---

---
title: Secure tenant connections with TLS certificates
description: Secure Advanced Identity Cloud tenant connections using TLS certificates for inbound and outbound traffic
component: pingoneaic
page_id: pingoneaic:realms:server-certificates
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/server-certificates.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Realms"]
page_aliases: ["realms:ssl-certificates.adoc"]
section_ids:
  inbound-connections: Inbound connections
  ping-domains: Ping Identity domains
  custom-domains: Custom domains
  google-managed-certificates: Google-managed certificates (default)
  self-managed-certificates: Self-managed certificates
  outbound-connections: Outbound connections
  send-ping-a-ca-or-tls-certificate: Send Ping Identity a CA or TLS certificate
---

# Secure tenant connections with TLS certificates

PingOne Advanced Identity Cloud protects all inbound network traffic using TLS encryption. By default, each of your tenant environments is provisioned with Google-managed certificates. If you add one or more custom domains to your tenant environments, you can optionally provide your own self-managed certificates.

Advanced Identity Cloud also lets you add certificates to each tenant environment's truststore to protect outbound connections to your company's other network resources.

What is TLS?

Transport Layer Security (TLS) is a cryptographic protocol used to secure network traffic between a client and a server. It is the more cryptographically secure successor to Secure Sockets Layer (SSL). The terms TLS and SSL are often used interchangeably.

TLS secures network traffic by applying three principles: authenticity (validating that the server is who it claims to be), confidentiality (preventing anyone else from reading the data being exchanged), and integrity (validating that the data sent is the same as the data received).

> **Collapse: Read more about how TLS ensures authenticity, confidentiality, and integrity**
>
> 1. Authenticity: When the client connects to the server, the server sends its certificate and public key. During the TLS handshake, the client validates that the certificate has been signed by a public certificate authority and that the server is in possession of the private key used to create the certificate.
>
> 2. Confidentiality: Data is encrypted and decrypted using a secret key that only the client and server have. The secret key is created and shared during the TLS handshake.
>
> 3. Integrity: The client and server encrypt the data using the same Message Authentication Code (MAC) algorithm and validate that the output hashes match.

## Inbound connections

### Ping Identity domains

Advanced Identity Cloud uses Google-managed certificates to secure inbound traffic to the `forgeblocks.com` and `forgerock.io` domains used by your tenant environments.

### Custom domains

#### Google-managed certificates (default)

If you use a [custom domain](custom-domains.html) to access Advanced Identity Cloud, by default a Google-managed certificate is used to secure inbound traffic to the domain. The domain is added to the certificate's Subject Alternative Name (SAN) field.

#### Self-managed certificates

Advanced Identity Cloud offers you the choice of using a self-managed certificate with your [custom domain](custom-domains.html), in place of the default Google-managed certificate.

You can create self-managed certificates in two main ways, depending on how you want to manage the private key and certificate signing request (CSR):

* Use a tenant-generated private key that is only accessible by the tenant itself. The tenant generates the CSR, and you install the resulting certificate on the same tenant. Learn more in:

  * [Create a certificate using the admin console](server-certificates-ui.html#create-a-certificate-using-the-ui) (UI)

  * [Create a certificate using a tenant-generated private key](server-certificates-api.html#create-a-certificate-using-a-tenant-generated-private-key) (API)

* Use a locally generated private key that you retain access to. You generate the CSR locally and install the resulting certificate on as many tenants as you need. Learn more in:

  * [Create a certificate using a locally generated private key](server-certificates-api.html#create-a-certificate-using-a-locally-generated-private-key) (API)

Learn the best practices for creating and managing certificates in [Server certificate best practices](server-certificates-best-practices.html).

## Outbound connections

Advanced Identity Cloud lets you secure outbound traffic from your tenant environments to your own network. For example, you might want to secure outbound emails from your Advanced Identity Cloud tenant environments to your on-premises SMTP server.

To do this, supply your own CA or TLS certificates to Ping Identity. Ping Identity then adds the certificates into the trust store of your tenant environments. You can supply as many certificates as you need.

### Send Ping Identity a CA or TLS certificate

1. Go to <https://support.pingidentity.com>.

2. Click Create a case.

3. Follow the steps in the case submission wizard by selecting your account and contract and answering questions about your tenant environments.

4. On the Please answer the following questions to help us understand the issue you're facing page, enter the following details, and then click Next:

   | Field                                                | Value                                                                       |
   | ---------------------------------------------------- | --------------------------------------------------------------------------- |
   | What product family is experiencing the issue?       | Select PingOne Advanced Identity Cloud                                      |
   | What specific product is experiencing the issue?     | Select Configuration                                                        |
   | What version of the product are you using?           | Select NA                                                                   |
   | What Hostname(s) or Tenant ID(s) does this apply to? | Enter a comma-separated list of FQDNs for the relevant tenant environments. |

5. On the Tell us about the issue page, enter the following details, and then click Next:

   | Field                                      | Value                                                                                       |
   | ------------------------------------------ | ------------------------------------------------------------------------------------------- |
   | Provide a descriptive title for your issue | Enter `Add CA or TLS certificate to tenant trust stores`                                    |
   | Describe the issue below                   | State the number of certificates you're providing, including any intermediate certificates. |

6. Click Submit.

7. Upload the local file containing your certificate. If your certificate chain includes intermediate certificates, make sure you upload them too.

8. Ping Identity support confirms when the certificate has been imported into the trust stores of your tenant environments.

---

---
title: Server certificate best practices
description: Best practices for managing self-hosted SSL certificates and key security in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:realms:server-certificates-best-practices
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/server-certificates-best-practices.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  certificate-creation-and-key-management: Certificate creation and key management
  ongoing-certificate-lifecycle-management: Ongoing certificate lifecycle management
---

# Server certificate best practices

When you use self-managed certificates, follow these best practices to ensure the security of your tenant environments:

## Certificate creation and key management

* **Prioritize tenant-generated private keys**: Whenever possible, use the feature for generating private keys within the tenant. This significantly reduces the risk of private key leakage as the key never leaves the secure tenant environment, aligning with the principle of secure key storage.

* **Secure locally generated private keys**: If operational requirements necessitate using your own private keys, implement robust security measures. This includes storing private keys in Hardware Security Modules (HSMs) for enhanced protection and ensuring strict access controls with detailed audit trails.

* **Use strong cryptography**: Always select strong encryption algorithms (for example, RSA 2048-bit or higher, or appropriate ECDSA curves) and key sizes when generating CSRs. Regularly review and update your cryptographic standards as new vulnerabilities emerge or best practices evolve.

* **Build complete certificate chains**: Always ensure you construct a complete PEM-formatted certificate chain, including your signed certificate, any intermediate CA certificates (in the correct order), and the root CA certificate. Incorrect chain order can lead to trust validation failures.

## Ongoing certificate lifecycle management

* **Proactive expiration monitoring**: Establish a proactive system for monitoring certificate expiration dates. Leverage the "Expires Soon" status in the admin console and consider implementing external alerts to ensure renewals are initiated well in advance (for example, 30 - 90 days prior to expiration).

* **Generate new key pairs for renewals**: When renewing a certificate, always generate a new private key and CSR. Reusing private keys significantly increases the security risk if the original key is ever compromised.

* **Regular audits**: Conduct periodic audits of your SSL configurations to identify any certificates nearing expiration, those that are no longer in use, or any anomalies that could indicate a security concern.

* **Controlled activation/deactivation**: Follow established change management procedures when activating or deactivating certificates in a production environment to prevent service disruptions.

* **Prompt deletion**: Delete pending CSRs or complete certificates that are no longer needed to maintain a clean and manageable inventory and reduce potential confusion.

* **Principle of least privilege (PoLP)**: Grant only the minimum necessary scopes to service accounts involved in certificate management.

* **Automate where possible**: While manual steps are outlined, explore the automation of certificate lifecycle management tasks for large-scale deployments or environments requiring high agility.

* **Security awareness**: Ensure all personnel involved in certificate management understand the critical importance of certificate security, proper private key handling, and the potential impact of mismanagement.

---

---
title: Server certificate utility tasks
description: Utility tasks for creating and checking SSL certificates and CSRs for Advanced Identity Cloud custom domains
component: pingoneaic
page_id: pingoneaic:realms:server-certificates-utility-tasks
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/server-certificates-utility-tasks.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["realms:ssl-certificates-self-managed-utility-tasks.adoc"]
section_ids:
  create-a-self-signing-ca-certificate-and-a-self-signed-certificate: Create a self-signing CA certificate and a self-signed certificate
  server-certificates-check-a-csr: Check a CSR
  server-certificates-check-a-certificate: Check a certificate
---

# Server certificate utility tasks

## Create a self-signing CA certificate and a self-signed certificate

1. Create a CSR and save it in a local file called `csr.pem`:

   * [Create a CSR using the command line](server-certificates-api.html#create-a-csr-using-the-command-line)

   * [Create a CSR using the certificate API](server-certificates-api.html#create-a-csr-using-the-certificate-api)

   * [Create a CSR using the admin console](server-certificates-ui.html#create-a-csr-using-the-ui)

2. Create a self-signing CA certificate and private key:

   1. Save the following OpenSSL configuration in a local file called `openssl-req-ca.conf`:

      ```ini
      [ req ] (1)
      x509_extensions = x509_req_ext

      [ x509_req_ext ]  (2)
      subjectKeyIdentifier   = hash
      authorityKeyIdentifier = keyid:always,issuer
      basicConstraints       = critical, CA:TRUE
      keyUsage               = critical, digitalSignature, cRLSign, keyCertSign
      ```

      |       |                                                                                             |
      | ----- | ------------------------------------------------------------------------------------------- |
      | **1** | Configures the `openssl req` command.                                                       |
      | **2** | Configures the `openssl req` command when using the `x509` flag to create a CA certificate. |

   2. Generate a self-signing CA certificate and private key:

      ```none
      $ openssl req \
      -x509 -nodes -newkey rsa:2048 -sha256 -days 30 \
      -out ca-cert.pem -keyout ca-key.pem \
      -subj "/CN=Self-signing CA" \
      -config openssl-req-ca.conf
      ```

   3. Review the self-signing CA certificate and private key, which are respectively in the local files `ca-cert.pem` and `ca-key.pem`:

      * For examples of a certificate and private key, learn more in [PEM-formatted certificate examples](ssl-certificate-reference.html#certificate-examples).

      * To check the information in the certificate, learn more in [Check a certificate](#server-certificates-check-a-certificate).

3. Create a self-signed certificate:

   1. Save the following OpenSSL configuration in a local file called `openssl-req-sign.conf`:

      ```ini
      [ req ] (1)
      x509_extensions = x509_req_ext

      [ x509_req_ext ]  (2)
      subjectKeyIdentifier    = hash
      authorityKeyIdentifier  = keyid:always
      keyUsage                = critical, digitalSignature
      extendedKeyUsage        = serverAuth
      ```

      |       |                                                                                |
      | ----- | ------------------------------------------------------------------------------ |
      | **1** | Configures the `openssl req` command.                                          |
      | **2** | Configures the `openssl req` command when using the `x509` flag to sign a CSR. |

   2. Generate a self-signed certificate using the CSR, the self-signing CA certificate and private key, and the configuration in `openssl-req-sign.conf`:

      ```none
      $ openssl req \
      -x509 -nodes -sha256 -days 30 -copy_extensions copy \
      -in csr.pem -out cert.pem -CA ca-cert.pem -CAkey ca-key.pem \
      -config openssl-req-sign.conf
      ```

   3. Review the self-signed certificate, which is in the local file `cert.pem`:

      * For an example of a certificate, learn more in [PEM-formatted certificate examples](ssl-certificate-reference.html#certificate-examples).

      * To check the information in the certificate, learn more in [Check a certificate](#server-certificates-check-a-certificate).

## Check a CSR

To check the information in a CSR, run this command:

```none
$ openssl req -in <csr-filename> -noout -text (1)
```

|       |                                                                                                      |
| ----- | ---------------------------------------------------------------------------------------------------- |
| **1** | Replace \<csr-filename> with the name of the local file containing your CSR; for example, `csr.pem`. |

> **Collapse: Show output**
>
> ```none
> Certificate Request:
>     Data:
>         Version: 1 (0x0)
>         Subject: CN = www.pingidentity.com, O = Ping Identity Corporation, OU = IT, ⏎
>                  C = US, street = 1001 17th Street, L = Denver, ST = Colorado, ⏎
>                  postalCode = 80202, emailAddress = example.user@pingidentity.com, ⏎
>                  businessCategory = Private Organization, serialNumber = 3463471, ⏎
>                  jurisdictionC = US, jurisdictionL = Wilmington, ⏎
>                  jurisdictionST = Delaware (1)
>         Subject Public Key Info:
>             Public Key Algorithm: rsaEncryption
>                 Public-Key: (2048 bit)
>                 Modulus:
>                     00:df:cf:53:47:8b:6a:51:23:0c:b9:8d:65:31:13:
>                     ...8<...
>                     69:71:13:b3:6a:86:d2:a4:7f:25:01:c0:8f:71:96:
>                     16:75
>                 Exponent: 65537 (0x10001)
>         Attributes:
>             Requested Extensions:
>                 X509v3 Subject Alternative Name: (2)
>                     DNS:support.pingidentity.com, DNS:labs.pingidentity.com
>     Signature Algorithm: sha256WithRSAEncryption
>     Signature Value:
>         ab:6d:a7:14:8a:07:6b:69:c8:f7:e9:1f:ca:d3:d4:6d:53:ad:
>         ...8<...
>         84:33:a5:48:61:dd:88:10:41:cc:d8:62:e9:3a:61:85:7d:06:
>         55:04:19:ff
> ```
>
> |       |                                                                                                  |
> | ----- | ------------------------------------------------------------------------------------------------ |
> | **1** | Check the subject contains the fields you entered for the CSR, particularly for EV certificates. |
> | **2** | If you entered SANs for the CSR, check the SAN extension is present.                             |

## Check a certificate

To check the information in a certificate, run this command:

```none
$ openssl x509 -in <certificate-filename> -text -noout (1)
```

|       |                                                                                                                       |
| ----- | --------------------------------------------------------------------------------------------------------------------- |
| **1** | Replace \<certificate-filename> with the name of the local file containing your certificate; for example, `cert.pem`. |

> **Collapse: Show output**
>
> ```none
> Certificate:
>     Data:
>         Version: 3 (0x2)
>         Serial Number: 2 (0x2)
>         Signature Algorithm: sha256WithRSAEncryption
>         Issuer: CN = Self-signing CA
>         Validity
>             Not Before: May  2 12:07:51 2024 GMT
>             Not After : Jun  1 12:07:51 2024 GMT (1)
>         Subject: CN = www.pingidentity.com, C = US, ST = Colorado, L = Denver, ⏎
>                  O = Ping Identity Corporation, OU = IT (2)
>         Subject Public Key Info:
>             Public Key Algorithm: rsaEncryption
>                 Public-Key: (2048 bit)
>                 Modulus:
>                     00:d0:52:11:d0:47:34:32:26:85:ae:c8:db:e1:59:
>                     ...8<...
>                     b8:90:00:12:f8:c4:4c:a2:9c:71:e9:22:c4:89:19:
>                     35:3f
>                 Exponent: 65537 (0x10001)
>         X509v3 extensions:
>             X509v3 Subject Key Identifier:
>                 7B:1D:14:C9:3C:4A:67:37:A2:E5:BE:B5:30:19:BE:EF:E6:08:B3:D6
>             X509v3 Authority Key Identifier:
>                 6E:41:13:8E:26:E4:B0:7E:63:ED:07:0C:4E:2D:CD:FA:66:28:20:21
>             X509v3 Key Usage: critical
>                 Digital Signature
>             X509v3 Extended Key Usage:
>                 TLS Web Server Authentication
>             X509v3 Subject Alternative Name: (3)
>                 DNS:support.pingidentity.com, DNS:labs.pingidentity.com
>     Signature Algorithm: sha256WithRSAEncryption
>     Signature Value:
>         22:60:ab:f8:13:cd:af:36:62:06:c5:fe:d4:eb:4f:7e:17:d1:
>         ...8<...
>         67:c5:8d:dd:ad:68:c6:7a:1d:5c:a5:df:cd:0b:d9:de:83:0f:
>         20:42:83:61
> ```
>
> |       |                                                                                                  |
> | ----- | ------------------------------------------------------------------------------------------------ |
> | **1** | Check the expiry date.                                                                           |
> | **2** | Check the subject contains the fields you entered for the CSR, particularly for EV certificates. |
> | **3** | If you entered SANs for the CSR, check the SAN extension is present.                             |

---

---
title: SSL certificate reference
description: Reference documentation for CSR fields and certificate formats used in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:realms:ssl-certificate-reference
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/ssl-certificate-reference.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Customization", "Security", "Realms", "Setup &amp; Configuration"]
page_aliases: ["realms:ssl-certificates-self-managed-csr-reference.adoc", "realms:ssl-certificates-self-managed-reference.adoc"]
section_ids:
  csr_field_reference: CSR field reference
  standard-csr-fields: Standard CSR fields
  ev-csr-fields: EV CSR fields
  dv-and-ev-certificates: DV and EV certificates
  wildcard-certificates: Wildcard certificates
  certificate-examples: PEM-formatted certificate examples
---

# SSL certificate reference

## CSR field reference

### Standard CSR fields

| CSR field                    | CSR field IDs                                                                        | Additional information                                                       | Examples                                                                                                                                                                                                                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| []()Common Name              | * OpenSSL field

  `commonName` (CN)

* JSON key

  `commonName`                     | Domain name that the SSL certificate is securing                             | •  www\.pingidentity.com •  \*.pingidentity.com\[[1](#_footnotedef_1 "View footnote.")]***[1](#_footnoteref_1). Wildcard certificates are supported within the same tenant environment but not across different tenant environments. Learn more in [Wildcard certificates](server-certificates.html#wildcard-certificates). |
| []()Organization             | - OpenSSL field

  `organizationName` (O)

- JSON key

  `organization`              | Full name of company                                                         | Ping Identity Corporation                                                                                                                                                                                                                                                                                                   |
| Organization Unit            | * OpenSSL field

  `organizationalUnitName` (OU)

* JSON key

  `organizationalUnit` | Company section or department                                                | IT                                                                                                                                                                                                                                                                                                                          |
| []()Country                  | - OpenSSL field

  `countryName` (C)

- JSON key

  `country`                        | Two-letter ISO-3166 country code                                             | US                                                                                                                                                                                                                                                                                                                          |
| State/Province               | * OpenSSL field

  `stateOrProvinceName` (ST)

* JSON key

  `state`                 |                                                                              | Colorado                                                                                                                                                                                                                                                                                                                    |
| Street Address               | - OpenSSL field

  `streetAddress` (street)

- JSON key

  `streetAddress`           |                                                                              | 1001 17th Street                                                                                                                                                                                                                                                                                                            |
| City/Locality                | * OpenSSL field

  `localityName` (L)

* JSON key

  `city`                          |                                                                              | Denver                                                                                                                                                                                                                                                                                                                      |
| Postal Code                  | - OpenSSL field

  `postalCode`

- JSON key

  `postalCode`                          |                                                                              | 80202                                                                                                                                                                                                                                                                                                                       |
| Email Address                | * OpenSSL field

  `emailAddress`

* JSON key

  `email`                             |                                                                              | example.user\@pingidentity.com                                                                                                                                                                                                                                                                                              |
| []()Subject Alternative Name | - OpenSSL field

  `subjectAltName`

- JSON key

  `subjectAlternativeNames`         | (Optional) Additional domain or domains that the SSL certificate is securing | •  support.pingidentity.com •  labs.pingidentity.com •  ...                                                                                                                                                                                                                                                                 |

### EV CSR fields

| CSR field                                            | CSR field IDs                                                                                            | Additional information                                                                                        | Examples             |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------- |
| Business Category                                    | * OpenSSL field

  `businessCategory`

* JSON key

  `businessCategory`                                  | Possible values are: •  Private Organization •  Government Entity •  Business Entity •  Non-commercial Entity | Private Organization |
| Serial Number                                        | - OpenSSL field

  `serialNumber`

- JSON key

  `serialNumber`                                          | Serial number or registration number of incorporated company                                                  | 3463471              |
| Jurisdiction of Incorporation Country Name           | * OpenSSL field

  `jurisdictionCountryName` (jurisdictionC)

* JSON key

  `jurisdictionCountry`        | Two-letter ISO-3166 country code                                                                              | US                   |
| Jurisdiction of Incorporation State or Province Name | - OpenSSL field

  `jurisdictionStateOrProvinceName` (jurisdictionST)

- JSON key

  `jurisdictionState` | (Optional)                                                                                                    | Delaware             |
| Jurisdiction of Incorporation Locality Name          | * OpenSSL field

  `jurisdictionLocalityName` (jurisdictionL)

* JSON key

  `jurisdictionCity`          | (Optional)                                                                                                    | Wilmington           |

## DV and EV certificates

Providing your own Domain Validation (DV) or Extended Validation (EV) SSL certificate can give your end users extra confidence that your applications are secure. Most browser vendors have now removed the visual signals in the browser address bar that distinguished these certificates (green padlock, highlighted company name, highlighted https protocol). However, the additional EV certificate information is still available when you click the padlock in the browser address bar and inspect the certificate:

|                                                                                                                                               |                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard SSL certificate:                                                                                                                     | EV SSL certificate:                                                                                                                                       |
| ![browser ssl padlock info](_images/browser-ssl-padlock-info.png) + ![browser ssl certificate info](_images/browser-ssl-certificate-info.png) | ![browser ssl padlock info ev](_images/browser-ssl-padlock-info-ev.png) + ![browser ssl certificate info ev](_images/browser-ssl-certificate-info-ev.png) |

## Wildcard certificates

Wildcard certificates allow subdomains of the same domain to share a certificate in the following ways:

* Within the same realm

* Across different realms

* Within the same realm *and* across different realms

For example, a certificate for the wildcard domain "\*.example.com" could be shared between an Alpha realm using the subdomain "customers.example.com" and a Bravo realm using the subdomain "employees.example.com".

Similarly, the same certificate could be shared between subdomains "employees-emea.example.com" and "employees-apac.example.com" within the same Alpha or Bravo realm.

## PEM-formatted certificate examples

The contents of a PEM-formatted CSR, private key, and certificate should look something like these examples:

* CSR example

* Private key example

* Certificate example

```text
-----BEGIN CERTIFICATE REQUEST-----
MIIDTTCCAjUCAQAwgbcxCzAJBgNVBAYTAlVTMQ8wDQYDVQQHEwZEZW52ZXIxGTAX
BgNVBAkTEDEwMDEgMTd0aCBTdHJlZXQxIjAgBgNVBAoTGVBpbmcgSWRlbnRpdHkg
Q29ycG9yYXRpb24xCzAJBgNVBAsTAklUMR0wGwYDVQQDExR3d3cucGluZ2lkZW50
aXR5LmNvbTEsMCoGCSqGSIb3DQEJARYdZXhhbXBsZS51c2VyQHBpbmdpZGVudGl0
eS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCtQMavyinYUbzz
uIWq5HtqNE4lkO1kV+JzoIxXY5Ytr/ooyy0m3Xb8SycNGeA+X4eDeBuOX1LUOuSl
sOJYyf4mbHKirgojMJ4oj1ysv4DK2GTJOcAnsqXo5Hd+ahOxD8SLvta8S6qYo2ME
VnujZC0ghVi6+9Q11xavcsCLf3LnBe0oYZ7qUEyyNnx4KjvOpDhy+UH9LHvt7Cur
fOCM0l2guX5+VuRVgkHWOtIi3lIF64a9JSpTFY3Z+ikLlGCXtkCtSdSRMiEITpcR
RBYQkCjivF7xzQ0jipL/CtT7no4LWhy72dS3oyuTNeTtyPu8Mbk4EicnVzQtO5iL
xBK+AMv7AgMBAAGgUDBOBgkqhkiG9w0BCQ4xQTA/MD0GA1UdEQEB/wQzMDGCGHN1
cHBvcnQucGluZ2lkZW50aXR5LmNvbYIVbGFicy5waW5naWRlbnRpdHkuY29tMA0G
CSqGSIb3DQEBCwUAA4IBAQBCxK33xB9UTZRJi9Bi02HA06plcrHVdYONuZOSadP+
PdHYV6BoUMvCznzH6uzYdS+aEKrmVa2r6/4CvafvdcxRqTa0dtMAuVJBltlXjmoX
/+xU4rKXwlX1Y+05ZE7waskv4wnTryfE2eNsloiiZazu2zNsnk5MQouJTrLxSH2u
a3eG9B2Xg8H7tSu8tFuaiwdV+YamjG5qDVU8NRhs1JtQg9OJtCG907WQsN+eUys4
vem0rmJ/vI9djVLe2953N1or/gqC2s/0ZnxdsxfXgp4ChYPoxmIA1BEh8MUREqk/
dSPgWeMMVFQwlmljkE+cvGl9L3f7aPgXtR6nxPS/oTSl
-----END CERTIFICATE REQUEST-----
```

```text
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQIdwl71gz4G1UCAggA
MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECGBfrYt/Ot8sBIIEyB+W3xwf7sbl
XsiQdmnI2ls8ynL0tnULGA404TayGgQIC+bChUdjiw7+n1gaSSfZQAB/nhsOCiuK
Ry9UL6k0ZvjOEyI1l2XEbBswpazh1MKfaqvuCME60O98ntbo+isP/fHzg1JBDYul
/yDFVNj9P7nGRHLdBXU3W9/5hMDzLf5HZSsLi9U4Nfcbs/asbKasHYVm88Qm/I9H
f34YPrwRGYyQCltRKQvNA5z3f8A4GmrXBeED/Incdjf3pxmf+birvzCfK1WYOwgl
J7SfWWKSj55leHvDBmfJcE4TlNDBme+BQ2lUtZ6yvLBzts32EpjqCR2oLwN9h47E
BE8bJjOJ3vEzUWsUxJbi0vkue42fnxFf3n70HemfYO8grQVFP3H2YyBKRC0Dwp2R
xPLldQ6TRFZvTyCxGsAlpo+En9tQHFMaS3RvWp2mWEGqHf0CaSb0aBdt/clbNsPd
HCX5EAghTxZAjWNRTmkihsg6HYXF1uWU6x1h0sZm/xhEEUebdFXFwoYX7tvRFIxp
OJdH+avLp7x33Oyt0jMmaCuZl3uDBnpjzxJT9TwhwSgm/dWBT0b9PPYfB1oPuMwg
pFBi7K9SUxgBSI6ZSISxuf0juFIkIo12ghB6gO6mWoCLC1qSCd0oL3ajP4kWIKBE
a8GIA3EruvF+bQleoHIs7mwOVKkmct59eLJ9UxZzIo6eaAJFJBWBeLGsKB2VyW+p
Fa6lR/mMDH0Jaoh4zMj+K4WVNUXoUoDCe+ERnAqTp0z97bHZDQn0qAdrP79Nh/To
KoD02s0dJl7sOPDso958DE/nP5NmEo46boLFi4NHZDxTxq70zVn1VPfxsXIgfaNA
lbBQu/i+3hjDxoosYMYhIUUYz4X6RzJaC425DFBsW4l8nzEGOhXxlRE8w4G/NgNT
L3JpeKX6tyYYHlNSD2KeSmIb5qC8dqZB640KSH2V6Set1/4sOGMzGtuVa6DYVAic
XtVY8gRy9+os5nsLvI8M9V0j+F/aI3tJ3gjws2eA3cIrbQxCmezsiRG3dt110voc
MDYOdns8jDdi6ViOVQFOQwgo7ekMmnUWuOYavdJXwnyBdT7Prlr1bLFerf4pLfKN
orBgdL1cwyvFjiSi59wbh65zGBvkMbcvvYwo8hh0G3NaST2Q4arLPaZdvpncjVD6
Dr12KFWrsPecg4HtlRVkedlew1De/s+KtIc+dhphL45MF2l9rnOe83tL8qMQI6qE
Q0bYvEOcqkNm0zEWyQCE/m6MpjvvUqS14RBspeIKI4lwvcEJ4jUnPMlmlxJ8EHtn
TfP4xx+KQ7/rjgFUq06qkLu34g3cY+BBzxb1BLSr7kykezU8Dl0qtQFlGUlFQNcC
1AxyB2YV38LfL4wUEF4SvOxQjhmHXQu+L0OApf/wQlKNkbyFR3JfEI+WiW0sQJ3d
PQQnCWorwiWYQXlImY7Zsb30AJOzVB3oX1Pt5NbyK35wUTTWT4kv+giK2SrfJqa0
90PabaDl6/H1h5ushRqmyZibLFIJaoEzR8+82wllHgJwu8NX3N7+Tgx9yCNX4+3r
SNkZ4QZiyo+n2kwvt20lWDCRTLZVXQkaTjqwdr8QZsqOBcmbdLdxv2ctf+umsjAS
Rv8K9FiTy5DNswa1ZE3jYA==
-----END ENCRYPTED PRIVATE KEY-----
```

```text
-----BEGIN CERTIFICATE-----
MIIDvDCCAqSgAwIBAgIBAjANBgkqhkiG9w0BAQsFADAaMRgwFgYDVQQDDA9TZWxm
LXNpZ25pbmcgQ0EwHhcNMjQwNTAyMTIwNzUxWhcNMjQwNjAxMTIwNzUxWjCBgTEd
MBsGA1UEAwwUd3d3LnBpbmdpZGVudGl0eS5jb20xCzAJBgNVBAYTAlVTMREwDwYD
VQQIDAhDb2xvcmFkbzEPMA0GA1UEBwwGRGVudmVyMSIwIAYDVQQKDBlQaW5nIElk
ZW50aXR5IENvcnBvcmF0aW9uMQswCQYDVQQLDAJJVDCCASIwDQYJKoZIhvcNAQEB
BQADggEPADCCAQoCggEBANBSEdBHNDImha7I2+FZnIgH4uEIZWyRl+TmM7tMJO+9
wZjnxGtuQDDVyrj21COuTyrik6PcG3bcn/+tIiNJJhiekPdBfH2JeQvOs/bizuCB
pth64Bpa3XyF/+hbvOUqCiMOac8r/c960thd+mF/1e+gnIptTHRumDY4PgSO9YIy
jF2o9ALzrVTw2RGPiH8LZIeXYWHZEH9UU0ni/ZDjZ6K4VrR/TLzZnDOWjZrDfIVY
RwI4BYCm45V8TFFGn9aBflYSzzW+AVcVZfDUn2EfupOleYTeerojBPqa9JkWYAzv
gJk8/V2vCYxuAi2oAgG9uJAAEvjETKKccekixIkZNT8CAwEAAaOBpDCBoTAdBgNV
HQ4EFgQUex0UyTxKZzei5b61MBm+7+YIs9YwHwYDVR0jBBgwFoAUbkETjibksH5j
7QcMTi3N+mYoICEwDgYDVR0PAQH/BAQDAgeAMBMGA1UdJQQMMAoGCCsGAQUFBwMB
MDoGA1UdEQQzMDGCGHN1cHBvcnQucGluZ2lkZW50aXR5LmNvbYIVbGFicy5waW5n
aWRlbnRpdHkuY29tMA0GCSqGSIb3DQEBCwUAA4IBAQAiYKv4E82vNmIGxf7U609+
F9HJyYJWl47V8VUzZNJPf6t14ChhNVZZ7XqlpmyU5zzhxZwcnkMkzUn1udUOgSvF
Ax8wNqOXz7T0oVXQXdhH3s/y37ls/6E38mGYX6bR2SzC81BxUWuV7NG+s/GaBCmt
YvT15ad7idWnTErliOvV2TpfnJcBeQDcdgXk9jp0YaonU2Alczn9DJu/jmEyWfjz
15Lk6LqzY4tZsOIWBjpDC+wA+K1N+4FQg/GH8C2RCUM6A6ITANsMPp3lU52srYfe
GiVeLsB8F/4hYZQB0zuW54MLqdHIDfoDkwpnxY3drWjGeh1cpd/NC9negw8gQoNh
-----END CERTIFICATE-----
```

---

---
title: Test SAML 2.0 SSO using JSP flows
description: Test SAML SSO using JSP flows between an identity provider and service provider in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:realms:applications-saml2-jsp
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/applications-saml2-jsp.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Application Management", "Troubleshooting"]
page_aliases: ["pingoneaic::applications-saml2-jsp.adoc"]
section_ids:
  set-up-an-sp-and-an-idp: "Task 1: Set up an SP and an IDP"
  create-an-sp-circle-of-trust: "Task 2: Create an SP circle of trust"
  create-an-idp-circle-of-trust: "Task 3: Create an IDP circle of trust"
  test-saml-sso: "Task 4: Test SAML 2.0 SSO"
  more_information: More Information
---

# Test SAML 2.0 SSO using JSP flows

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The topics in this section are for tenants created before January 12, 2023. Learn more in [Application management migration FAQ](../product-information/migration-dependent-features/application-management-migration-faq.html). |

SAML 2.0 helps organizations to share(or *federate*) identities and services without having to manage the identities or credentials themselves.

These instructions describe how to launch an SP-initiated JSP flow to test SAML 2.0 SSO. PingOne Advanced Identity Cloud acts as the authentication service provider (SP) in a circle of trust (CoT). For this test, a self-managed AM instance acts as the identity provider (IDP).

## Task 1: Set up an SP and an IDP

1. Set up the Advanced Identity Cloud AM instance as a service provider:

   1. In the AM native admin console, go to\
      *Realm Name* > Applications > Federation > Entity Providers.

   2. Click + Add Entity Provider > Hosted, and add a hosted entity provider:

      * Entity ID: Enter a unique identifier. Example: Cloud-SP.

      * Service Provider Meta Alias: Provide an SP alias. Example: `cloud-sp`.

   3. Export the SP metadata to an XML file. Example export metadata URL:\
      `https://<tenant-FQDN>/am/saml2/jsp/exportmetadata.jsp?entityid=<SP-Entity-ID>&realm=/alpha`.

2. Set up the self-managed AM instance as an identity provider:

   1. In the AM self-managed admin console, go to\
      Top Level Realm > Applications > Federation > Entity Providers.

   2. Click + Add Entity Provider > Hosted, and add a hosted entity provider:

      * Entity ID: Enter a unique identifier. Example: AM-IDP.

      * Meta Alias: Provide an IDP alias. Example: `am-idp`.

   3. Export the IDP metadata to an XML file. Example export metadata URL:\
      `https://<IDP-host-FQDN>/am/saml2/jsp/exportmetadata.jsp?entityid=<IDP-Entity-ID>`.

3. In the Advanced Identity Cloud AM instance, add a remote entity provider by importing the IDP metadata:

   1. In the AM native admin console, go to\
      *Realm Name* > Authentication > Federation > Entity Providers.

   2. Click + Add Entity Provider > Remote.

   3. Import the IDP metadata.

4. In the self-managed AM instance, add a remote entity provider by importing the SP metadata:

   1. In the AM self-managed admin console, go to:\
      Top Level Realm > Authentication > Federation > Entity Providers.

   2. Click + Add Entity Provider > Remote.

   3. Import the SP metadata.

5. Create a user profile on the SP and IDP:

   1. **SP**: In the AM native admin console, go to Identities and add a user identity.

   2. **IDP**: In the AM self-managed admin console, go to Identities and add a user identity.

## Task 2: Create an SP circle of trust

1. In the Advanced Identity Cloud AM instance, create a circle of trust:

   1. In the AM native admin console, go to\
      *Realm Name* > Applications > Federation > Circles of Trust.

   2. Click + Add Circle of Trust.

   3. On the New Circle of Trust page, provide a name, then click Create.

   4. On the CoT page, provide CoT details.

      > **Collapse: CoT details:**
      >
      > * Description: Enter a unique identifier.
      >
      > * Entity Providers: Choose the entity IDs for the SP and IDP.\
      >   Examples: `Cloud-SP` `AM-IDP`

   5. Click Save Changes.

2. In the Advanced Identity Cloud AM instance, create a federation module:

   1. In the AM native admin console, go to\
      *Realm Name* > Authentication > Modules.

   2. On the Modules page, click Add Module. Enter module details:

      * Name: Must be named `Federation`.

      * Type: Must be type `Federation`.

   3. Click Save Changes.

3. In the Advanced Identity Cloud AM instance, configure the page the browser displays upon successful SSO:

   1. In the AM native admin console, go to\
      *Realm Name* > Applications > Federation > Entity Providers.

   2. In the `Cloud-SP` entity provider page, select the Advanced tab.

   3. In the Relay State URL List field, add the target URL for the SP end-user sign-in page.\
      Example: `https://<tenant-FDQN>/enduser/?realm=alpha#/dashboard`.

   4. Click Save Changes.

## Task 3: Create an IDP circle of trust

1. In the AM self-managed admin console, go to\
   Top Level Realm > Applications > Circles of Trust.

2. Click + Add Circle of Trust.

3. On the New Circle of Trust page, provide a name, then click Create.

4. On the CoT page, provide CoT details.

   > **Collapse: CoT details:**
   >
   > * Description: Enter a unique identifier.
   >
   > * Entity Providers: Choose the entity IDs for the SP and IDP.\
   >   Examples: `Cloud-SP` `AM-IDP`.

5. Click Save Changes.

## Task 4: Test SAML 2.0 SSO

1. In a browser, go the JSP URL to launch an SP-initiated JSP flow. Example:\
   `https://<tenant-FQDN>/am/saml2/jsp/spSSOInit.jsp?realm=/alpha/&metaAlias=/alpha/cloud-sp&idpEntityID=AM-IDP&binding=urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST&NameIDformat=urn:oasis:names:tc:SAML:2.0:nameid-format:persistent&RelayState=https://<tenant-FQDN>/enduser/?realm=alpha#/dashboard`.

2. On the IDP sign-in page, enter the user's credentials:

   Keep this session open. The IDP authenticates the user, then the browser redirects the user back to the SP sign-in page.

3. On the SP sign-in page, enter the user's credentials:

   After this second successful authentication, the user's SP identity is linked to, or federated with, the user's IDP identity.

   The browser redirects to the SP end-user page.

4. Sign the user out of both the SP and IDP.

5. Go to the IDP end-user sign-in page, and enter the user's credentials.

   When the user is successfully authenticated, the browser redirects to the SP end-user page specified in Relay State URL List.

## More Information

For deep dives, learn more in:

* [Introduction to SAML 2.0](../am-saml2/saml2-introduction.html)

* [JSP pages for SSO and SLO](../am-saml2/saml2-standalone-mode.html#using-saml2-sso-slo)

* [Set up IdPs, SPs, and CoTs](../am-saml2/saml2-providers-and-cots.html)
---
title: Access External REST Services
description: "Configure PingIDM's external REST service to call remote HTTP endpoints from scripts or REST, with options for TLS, proxy, and authentication"
component: pingidm
version: 8.1
page_id: pingidm:external-services-guide:external-rest
canonical_url: https://docs.pingidentity.com/pingidm/8.1/external-services-guide/external-rest.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Configuration", "Rest", "REST API", "JSON"]
section_ids:
  configuring-external-rest: Configure the External REST Service
  external.rest.properties: External REST configuration properties
  invocation-parameters: Invocation Parameters
  non-json-responses: Support for Non-JSON Responses
---

# Access External REST Services

The external REST service lets you access remote REST services at the `openidm/external/rest` context path or by specifying the `external/rest` resource in your scripts. Note that this service is not intended as a full connector to synchronize or reconcile identity data, but as a way to make dynamic HTTP calls as part of the IDM logic. For more declarative and encapsulated interaction with remote REST services, and for synchronization or reconciliation operations, use the scripted REST implementation of the [Groovy connector](https://docs.pingidentity.com/openicf/connector-reference/groovy.html).

An external REST call via a script might look something like the following:

```javascript
openidm.action("external/rest", "call", params);
```

The `call` parameter specifies the action name to be used for this invocation, and is the standard method signature for the `openidm.action` method.

An external REST call over REST might look something like the following:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
--data '{
  "url": "http://urlecho.appspot.com/echo?status=200&Content-Type=application%2Fjson&body=%5B%7B%22key%22%3A%22value%22%7D%5D",
  "method": "GET"
}' \
"http://localhost:8080/openidm/external/rest?_action=call"
[
  {
    "key": "value"
  }
]
```

## Configure the External REST Service

You can edit the external REST configuration over REST at the `config/external.rest` endpoint, or in an `external.rest.json` file in your project's `conf` directory.

The following sample external REST configuration *(tooltip: You can edit the external REST configuration over REST at the config/external.rest endpoint, or in a conf/external.rest.json file.)* sets up the external REST service:

* Using REST

* Using the filesystem

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-type: application/json" \
--request PUT \
--data '{
  "socketTimeout" : "10 s",
  "connectionTimeout" : "10 s",
  "reuseConnections" : true,
  "retryRequests" : true,
  "maxConnections" : 64,
  "tlsVersion" : "&{openidm.external.rest.tls.version}",
  "hostnameVerifier" : "&{openidm.external.rest.hostnameVerifier}",
  "proxy" : {
    "proxyUri" : "",
    "userName" : "",
    "password" : ""
  }
}' \
"http://localhost:8080/openidm/config/external.rest"
{
  "_id": "external.rest",
  "socketTimeout": "10 s",
  "connectionTimeout": "10 s",
  "reuseConnections": true,
  "retryRequests": true,
  "maxConnections": 64,
  "tlsVersion": "&{openidm.external.rest.tls.version}",
  "hostnameVerifier": "&{openidm.external.rest.hostnameVerifier}",
  "proxy": {
    "proxyUri": "",
    "userName": "",
    "password": ""
  }
}
```

Copy the config to the `external.rest.json` file in your project's `conf` directory:

```json
{
    "socketTimeout" : "10 s",
    "connectionTimeout" : "10 s",
    "reuseConnections" : true,
    "retryRequests" : true,
    "maxConnections" : 64,
    "tlsVersion" : "&{openidm.external.rest.tls.version}",
    "hostnameVerifier" : "&{openidm.external.rest.hostnameVerifier}",
    "proxy" : {
        "proxyUri" : "",
        "userName" : "",
        "password" : ""
    }
}
```

### External REST configuration properties

* `socketTimeout` (string)

  The TCP socket timeout, in seconds, when waiting for HTTP responses. The default timeout is 10 seconds.

  By default, this property is set in the `resolver/boot.properties` file, and the value in `conf/external.rest.json` references that setting.

  To work properly at startup, you must ensure to escape the space in the `socketTimeout` property, for example:

  ```properties
  openidm.http.client.socketTimeout=10\ s
  ```

* `connectionTimeout` (string)

  The TCP connection timeout for new HTTP connections, in seconds. The default timeout is 10 seconds.

  By default, this property is set in the `resolver/boot.properties` file, and the value in `conf/external.rest.json` references that setting.

  To work properly at startup, you must ensure to escape the space in the `connectionTimeout` property, for example:

  ```properties
  openidm.http.client.connectionTimeout=10\ s
  ```

* `reuseConnections` (boolean, true or false)

  Specifies whether HTTP connections should be kept alive and reused for additional requests. By default, connections will be reused if possible.

* `retryRequests` (boolean, true or false)

  Specifies whether requests should be retried if a failure is detected. By default requests will be retried.

* `maxConnections` (integer)

  The maximum number of connections that should be pooled by the HTTP client. At most `64` connections will be pooled by default.

* `tlsVersion` (string)

  The TLS version that should be used for connections.

  By default, TLS connections made via the external REST service use TLS version 1.2. In some cases, you might need to specify a different TLS version, for example, if you are connecting to a legacy system that supports an old version of TLS that is not accommodated by the backward-compatibility mode of your Java client. If you need to specify that the external REST service uses a different TLS version, uncomment the `openidm.external.rest.tls.version` property towards the end of the `resolver/boot.properties` file and set its value, for example:

  ```properties
  openidm.external.rest.tls.version=TLSv1.3
  ```

  Valid versions for this parameter include TLSv1.1, TLSv1.2, and TLSv1.3.

* `hostnameVerifier` (string)

  Specifies whether the external REST service should check that the hostname to which an SSL client has connected is allowed by the certificate that is presented by the server.

  The property can take the following values:

  * `STRICT`: Hostnames are validated

  * `ALLOW_ALL`: The external REST service doesn't attempt to match the URL hostname to the SSL certificate Common Name, as part of its validation process

  By default, this property is set in the `resolver/boot.properties` file and the value in `conf/external.rest.json` references that setting. For testing purposes, the default setting in `boot.properties` is:

  ```properties
  openidm.external.rest.hostnameVerifier=ALLOW_ALL
  ```

  If you do not set this property (by removing it from the `boot.properties` file or the `conf/external.rest.json` file), the behavior is to validate hostnames (the equivalent of setting `"hostnameVerifier": "STRICT"`). In production environments, you *should* set this property to `STRICT`.

* `proxy`

  Lets you set a proxy server *specific* to the external REST service. If you set a `proxyUri` here, the system-wide proxy settings described in [HTTP Clients](../setup-guide/http-client-config.html) are ignored. To configure a system-wide proxy, leave these `proxy` settings empty and configure the HTTP Client settings instead.

* []()`userAgent`

  Specifies the value of the `User-Agent` header for requests made by the external REST service, relative to the global HTTP client setting [`openidm.http.client.userAgent`](../setup-guide/http-client-config.html#new-user-agent-property).

  If `userAgent` isn't specified, the default `"PingIdentity"` value is used. Request-level headers take precedence over both the IDM configuration and the default value:

  Example request

  ```
  curl \
  --request POST \
  --header "X-OpenIDM-Username: openidm-admin" \
  --header "X-OpenIDM-Password: openidm-admin" \
  --header "Content-Type: application/json" \
  --header "Accept-API-Version: resource=1.0" \
  --data '{
    "url": "http://echo-http-requests.appspot.com/echo?status=200&Content-Type=application%2Fjson&body=%5B%7B%22key%22%3A%22value%22%7D%5D",
    "method": "GET",
    "headers": {
       "User-Agent": "OverriddenValue"
       }
    }' \
    "http://localhost:8080/openidm/external/rest?_action=call"
  ```

  > **Collapse: Show example response**
  >
  > Response
  >
  > ```json
  > {
  >    "request": {
  >       "body": "",
  >       "created": "2026-02-25 21:29:20.253693",
  >       "headers": {
  >          "Content-Type": "; charset=\"utf-8\"",
  >          "Host": "echo-http-requests.appspot.com",
  >          "Traceparent": "00-3daffaa2187dd81345f37b1837661a26-65404f3040d5b362-00",
  >          "User-Agent": "OverriddenValue",
  >          "X-Cloud-Trace-Context": "3daffaa2187dd81345f37b1837661a26/7295918465004974946",
  >          "X-Forgerock-Transactionid": "31fa216a-333e-4e25-9ba0-2c073794121b-387/0"
  >       },
  >       "http_version": "HTTP/1.1",
  >       "method": "GET",
  >       "query_string": "status=200&Content-Type=application%2Fjson&body=%5B%7B%22key%22%3A%22value%22%7D%5D",
  >       "remote_address": "75.164.173.47",
  >       "url": "http://echo-http-requests.appspot.com/echo?status=200&Content-Type=application%2Fjson&body=%5B%7B%22key%22%3A%22value%22%7D%5D"
  >    },
  >    "status": "OK"
  > }
  > ```

## Invocation Parameters

The following parameters are passed in the resource API parameters map. These parameters can override the static configuration (if present) on a per-invocation basis.

* `url`

  The target URL to invoke, in string format.

* `method`

  The HTTP action to invoke, in string format.

  Possible actions include `POST`, `GET`, `PUT`, `DELETE`, and `OPTIONS`.

* `headers` (optional)

  The HTTP headers to set, in a map format from string (header-name) to string (header-value). For example, `Accept-Language: en-US`.

* `contentType` (optional)

  The media type of the data that is sent, for example `"contentType" : "application/json"`. This parameter is applied only if no `Content-Type` header is included in the request. (If a `Content-Type` header is included, that header takes precedence over this `contentType` parameter.) If no `Content-Type` is provided (in the header or with this parameter), the default content type is `application/json; charset=utf-8`.

* `body` (optional)

  The body or resource representation to send (for PUT and POST operations), in string format.

* `base64` (boolean, optional)

  Indicates that the `body` is base64-encoded, and should be decoded prior to transmission.

* `forceWrap` (boolean, optional)

  Indicates that the response must be wrapped in the headers/body JSON message format, even if the response was JSON, and would otherwise have been passed through unchanged.

  If you need to disambiguate between HTTP 20x response codes, you must invoke the external REST service with `forceWrap=true`. For failure cases, the HTTP status code is present within the wrapped response embedded in the exception detail, or through the resource exception itself. For example:

  ```
  curl \
  --header "X-OpenIDM-Username: openidm-admin" \
  --header "X-OpenIDM-Password: openidm-admin" \
  --header "Content-Type: application/json" \
  --header "Accept-API-Version: resource=1.0" \
  --request POST \
  --data '{
    "url": "http://urlecho.appspot.com/echo?status=203&Content-Type=application%2Fjson&body=%5B%7B%22key%22%3A%22value%22%7D%5D",
    "method": "GET",
    "forceWrap": true}' \
  "http://localhost:8080/openidm/external/rest?_action=call"
  {
    "headers": {
      "Access-Control-Allow-Origin": [
        "*"
      ],
      "Cache-Control": [
        "max-age=3600"
      ],
      "Content-Length": [
        "17"
      ],
      "Content-Type": [
        "application/json"
      ],
      "Date": [
        "Fri, 17 Jul 2020 10:55:54 GMT"
      ],
      "Server": [
        "Google Frontend"
      ],
      "X-Cloud-Trace-Context": [
        "11e4441659a85832e47af219d6e657af"
      ]
    },
    "code": 203,
    "body": [
      {
        "key": "value"
      }
    ]
  }
  ```

* `authenticate`

  The authentication type, and the details with which to authenticate.

  IDM supports the following authentication types:

  * `basic` authentication with a username and password, for example:

    ```json
    "authenticate" : {
        "type": "basic",
        "user" : "john",
        "password" : "Passw0rd"
    }
    ```

  * `bearer` authentication, with an OAuth token instead of a username and password, for example:

    ```json
    "authenticate" : {
        "type": "bearer",
        "token" : "ya29.iQDWKpn8AHy09p....."
    }
    ```

  If no `authenticate` parameter is specified, no authentication is used.

## Support for Non-JSON Responses

The external REST service supports any arbitrary payload (currently in stringified format). If the response is anything other than JSON, a JSON message object is returned:

* For text-compatible (non-JSON) content, IDM returns a JSON object similar to the following:

  ```json
  {
      "headers": { "Content-Type": ["..."] },
      "body": "..."
  }
  ```

* Content that is not text-compatible (such as JPEGs) is base64-encoded in the response `body` and returned as follows:

  ```json
  {
      "headers": { "Content-Type": ["..."] },
      "body": "...",
      "base64": true
  }
  ```

|   |                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the response format is JSON, the raw JSON response is returned. If you want to inspect the response headers, set `forceWrap` to `true` in your request. This setting returns a JSON message object with `headers` and `body`, similar to the object returned for text-compatible content. |

---

---
title: Email templates
description: PingIDM preconfigured email templates using Handlebars expressions, with locale support and steps to customize templates using the admin UI or conf/ files
component: pingidm
version: 8.1
page_id: pingidm:external-services-guide:email-templates
canonical_url: https://docs.pingidentity.com/pingidm/8.1/external-services-guide/email-templates.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Email", "Templates", "Handlebars", "JSON", "Locales", "UI"]
section_ids:
  email-templates-example: Example email template
  email-templates-manage: Manage email templates
---

# Email templates

IDM provides preconfigured email templates for common events, such as "Welcome" and "Forgot Password".

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Email templates utilize [Handlebar expressions](https://handlebarsjs.com/guide/) to reference object data dynamically. For example, to reference the `userName` of an object:```html
{{object.userName}}
``` |

## Example email template

The following example displays a default "Welcome" message template:

```json
{
    "enabled" : true,
    "from" : "", (1)
    "subject" : {
        "en" : "Your account has been created",
        "fr" : "Votre compte vient d'être créé !"
    },
    "message" : {
        "en" : "<html><body><p>Welcome to OpenIDM. Your username is '{{object.userName}}'.</p></body></html>",
        "fr" : "<html><body><p>Bienvenue sur OpenIDM. Votre nom d'utilisateur est '{{object.userName}}'.</p></body></html>"
    },
    "defaultLocale" : "en", (2)
    "mimeType" : "text/html"
}
```

|       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1** | Each email template can specify a `from` email address. If this field is left blank, IDM defaults to the address specified in the [email configuration](email.html#configure_outbound_email).                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **2** | Specify locale(s) in the `defaultLocale` property using [ISO 639-1 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes).&#xA;&#xA;preferredLocales specified in the Accept-Language header take precedence over the defaultLocale.&#xA;&#xA;The \_locale parameter takes precedence over the defaultLocale.&#xA;&#xA;Some email providers, such as Google, override the from address you specify in the templates and instead use the address used to authenticate with the SMTP server. The template email address can still be present but in an email header hidden from most users, such as X-Google-Original-From. |

## Manage email templates

Customize and edit email templates using the admin UI or save a `emailTemplate-name.json` file to the `conf/` directory:

1. From the navigation bar, click Configure > Email Settings, and select the Templates tab.

   IDM displays a list of email templates.

   ![Email Settings > Templates](_images/emailSettingsTemplates.png)

2. To customize or edit an email template, click the adjacent edit [icon: pencil-alt, set=fas]button.

3. On the Email Template templateName page, make changes, and click Save.

   ![Email Settings > Templates > Welcome](_images/emailTemplateWelcome.png)

---

---
title: External services
description: Configure outbound email and external REST service access in PingIDM
component: pingidm
version: 8.1
page_id: pingidm:external-services-guide:external-services
canonical_url: https://docs.pingidentity.com/pingidm/8.1/external-services-guide/external-services.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Email", "Rest", "REST API"]
page_aliases: ["index.adoc", "preface.adoc"]
---

# External services

> Configure external email and external REST access.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

[icon: paper-plane, set=fad, size=3x]

#### [Email](email.html)

Configure outbound email from IDM.

[icon: skiing, set=fad, size=3x]

#### [External REST](external-rest.html)

Access external REST services.

---

---
title: Outbound email service
description: Configure PingIDM outbound email using SMTP or MS Graph API, with REST and UI setup, configuration properties, and Azure credential management
component: pingidm
version: 8.1
page_id: pingidm:external-services-guide:email
canonical_url: https://docs.pingidentity.com/pingidm/8.1/external-services-guide/email.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Email", "Rest", "REST API", "JSON", "Scripts"]
section_ids:
  email-service-types: Email service configuration types
  international-email-address: International email addresses
  ms_graph_api_requirements: MS Graph API requirements
  configure_azure_for_ms_graph_api_mail_client: Configure Azure for MS Graph API mail client
  configure_outbound_email: Configure outbound email
  secret-rotation-email: Storing MS Azure credentials as a secret
  external.email.json: Sample email configuration
  external.email.properties: External email configuration properties
  section-mail-limiting2: Email rate limiting
---

# Outbound email service

The outbound email service sends email from IDM using a script or the REST API.

You can edit the email service over REST at the `config/external.email` endpoint, or in the `external.email.json` file in your project's `conf` directory.

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | IDM supports UTF-8 (non-ascii/international) characters in email addresses, such as **zoë@example.com**. When sending emails to these type of addresses, the configured SMTP server must also support UTF-8. |

## Email service configuration types

The outbound email service supports two email service configuration types:

* SMTP - Email service that uses the Simple Mail Transfer Protocol. Can be configured using the UI or API.

* MS Graph API - Email service that uses the [MS Graph API `sendMail`](https://learn.microsoft.com/en-us/graph/api/user-sendmail) endpoint. Can only be configured using the API.

### International email addresses

To use [international email addresses](https://en.wikipedia.org/wiki/International_email), you must:

* Use SMTP as the provider type.

* The SMTP provider must support international email addresses.

* Configure `mail.mime.allowutf8=true`, which is only available using the REST API or the filesystem. For more information, refer to [`smtpProperties` sub-properties](#smtp-sub-prop-table).

## MS Graph API requirements

Use of the MS Graph API email client requires a properly configured Microsoft Azure tenant. The basic steps for configuring an Azure tenant should be used as an outline, as the specific options, menus, and features may have changed.

Microsoft Sandbox

If you need a sandbox for *testing only*, check out the [Microsoft developer sandbox subscription](https://learn.microsoft.com/en-us/office/developer-program/microsoft-365-developer-program-get-started). Although the sandbox accepts `sendMail` requests, the Microsoft Exchange service prevents messages from being delivered. The messages do show up in the sender's "sent" box, which should be sufficient for manual testing purposes.

### Configure Azure for MS Graph API mail client

1. Navigate to [Azure Active Directory | App registrations](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps).

2. Create the IDM client application:

   1. From the menu bar, click + New Registration.

   2. On the Register an application page, enter the application Name, such as `idm-email-client`.

   3. For Supported account types, select the applicable option for your organization.

   4. Click Register.

   5. On the idm-email-client page, in the main Essentials area, record the Application (client) ID.

      |   |                                                                                                                                                                                                                                                                                                     |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | This is the value for `clientId` in the `auth` settings of the email configuration *(tooltip: You can edit the email service over REST at the config/external.email endpoint, or in the external.email.json file in your project's conf directory.)*. Refer to [`oauth2` properties](#oath2-table). |

3. Add a client secret:

   1. On the idm-email-client page, in the main Essentials area, click Add a certificate or secret.

      > **Collapse: Show Me**
      >
      > ![Azure app - add a secret link](_images/azureAppAddSecretLink.png)

   2. On the Certificates & secrets page, select the Client secrets tab, and click + New client secret.

      > **Collapse: Show Me**
      >
      > ![Azure app - add a new client secret](_images/azureNewClientSecret.png)

   3. In the Add a client secret window, enter the details, and click Add.

   4. Copy the Value and Secret ID to a secure place *before* leaving the Certificates & secrets page.

      |   |                                                                                                                                                                                                                                                                                                            |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Use the secret Value for `clientSecret` in the `auth` settings of the email configuration *(tooltip: You can edit the email service over REST at the config/external.email endpoint, or in the external.email.json file in your project's conf directory.)*. Refer to [`oauth2` properties](#oath2-table). |

4. Add API permissions:

   1. From the side menu, click API permissions.

   2. On the API permissions page, click + Add a permission.

   3. In the Request API permissions windows, select the Microsft APIs tab, and click Microsoft Graph.

   4. In the What type of permissions... area, click Application permissions.

   5. In the Select permissions search bar, type `send`.

   6. Expand the Mail node, and select Mail.Send.

   7. Click Add permissions.

      > **Collapse: Show Me**
      >
      > ![Azure app - Request API permissions](_images/azureRequestAPIPermissions.png)

## Configure outbound email

To configure the outbound email service using the admin UI, click Configure > Email Settings.

1. Edit the email configuration *(tooltip: You can edit the email service over REST at the config/external.email endpoint, or in the external.email.json file in your project's conf directory.)* with the mail server details and account.

   |   |                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * For the complete list of configuration options, refer to [External email configuration properties](#external.email.properties).

   * For sample email configurations, refer to [Sample email configuration](#external.email.json). |

2. Submit the configuration over REST or copy the file to your project's `conf/` directory. For example:

   * REST

   * Filesystem

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request PUT \
   --data '{
       "host" : "smtp.gmail.com",
       "port" : 587,
       "debug" : false,
       "auth" : {
           "enable" : true,
           "username" : "admin",
           "password" : "Passw0rd"
       },
       "from" : "admin@example.com",
       "timeout" : 300000,
       "writetimeout" : 300000,
       "connectiontimeout" : 300000,
       "starttls" : {
           "enable" : true
       },
       "ssl" : {
           "enable" : false
       },
       "smtpProperties" : [
           "mail.smtp.ssl.protocols=TLSv1.2",
           "mail.smtps.ssl.protocols=TLSv1.2",
           "mail.mime.allowutf8=true"
       ],
       "threadPoolSize" : 20
   }' \
   "http://localhost:8080/openidm/config/external.email"
   ```

   ```
   cp /path/to/external.email.json /path/to/openidm/conf/
   ```

   |   |                            |
   | - | -------------------------- |
   |   | IDM encrypts the password. |

### Storing MS Azure credentials as a secret

You can enable zero-downtime rotation of your `clientId` and `clientSecret` credentials by storing those values in a file system based secret store.

To configure an existing IDM external email client with an existing MS Azure tenant to use a file system secret store:

1. Add a new secret in the Microsoft Azure portal. For more information, refer to [the Microsoft identity platform documentation](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app#add-a-client-secret).

2. Create the `idm.email.msgraph.credentials` file in your [file system-based secret store](../security-guide/secret-stores.html). The file must contain a JSON object with your secret values, such as:

   ```json
   {
     "clientId": "myClient",
     "clientSecret": "mySecret"
   }
   ```

3. Update the `auth` property in `conf/external.email.json` to read the `clientId` and `clientSecret` from the secret file using a purpose. You must set a `jsonPointer` property that identifies the matching field in the secret file:

   ```json
   {
   ...
     "auth": {
       "enable": true,
       "type": "oauth2",
         "clientId": {
           "$purpose": {
             "name" : "idm.email.msgraph.credentials",
             "jsonPointer" : "clientId"
           }
         },
         "clientSecret" : {
           "$purpose" : {
             "name" : "idm.email.msgraph.credentials",
             "jsonPointer" : "clientSecret"
           }
         },
         "tokenEndpoint" : "https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token",
         "scope" : [
               "https://graph.microsoft.com/.default"
         ],
         "scopeDelimiter" : " ",
         "grantType" : "client_credentials"
       }
   }
   ```

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | If you use a secret that only stores a password, you only need to update the `clientSecret` value in `conf/external.email.json`. |

### Sample email configuration

This sample email configuration *(tooltip: You can edit the email service over REST at the config/external.email endpoint, or in the external.email.json file in your project's conf directory.)* sets up the outbound email service:

* SMTP

* MS Graph API

```json
{
    "host" : "smtp.gmail.com",
    "port" : 587,
    "debug" : false,
    "auth" : {
        "enable" : true,
        "username" : "xxxxxxxx",
        "password" : "xxxxxxxx"
    },
    "timeout" : 300000,
    "writetimeout" : 300000,
    "connectiontimeout" : 300000,
    "starttls" : {
        "enable" : true
    },
    "ssl" : {
        "enable" : false
    },
    "smtpProperties" : [
        "mail.smtp.ssl.protocols=TLSv1.2",
        "mail.smtps.ssl.protocols=TLSv1.2"
    ],
    "threadPoolSize" : 20
}
```

```json
{
    "type" : "msgraph",
    "mailEndpoint" : "https://graph.microsoft.com/v1.0/users/example@myTenant.onmicrosoft.com/sendMail",
    "from" : "example@myTenant.onmicrosoft.com",
    "auth" : {
        "enable" : true,
        "type" : "oauth2",
        "clientId" : "clientId",
        "clientSecret" : "clientSecret",
        "tokenEndpoint" : "https://login.microsoftonline.com/myTenant.onmicrosoft.com/oauth2/v2.0/token",
        "scope" : [
            "https://graph.microsoft.com/.default"
        ]
    },
    "timeout" : 300000,
    "writetimeout" : 300000,
    "connectiontimeout" : 300000,
    "threadPoolSize" : 20
}
```

### External email configuration properties

The `msgraph` type also supports the [External REST configuration properties](external-rest.html#external.rest.properties).

**Properties**

| Property            | Description                                                                                                                                                                                                                                                                                                                                                                                                                            | Required? / Type Support                         |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `type`              | The [email service type](#email-service-types), `smtp` or `msgraph`. When no type is specified, the default value is `smtp`.                                                                                                                                                                                                                                                                                                           | No                                               |
| `mailEndpoint`      | The URI for the MS Graph API `sendMail` endpoint.Typical format:```none
https://graph.microsoft.com/v1.0/users/{user}@{tenant}.onmicrosoft.com/sendMail
```                                                                                                                                                                                                                                                                            | YesOnly for `msgraph` type.                      |
| `host`              | The host name or IP address of the SMTP server. This can be the `localhost`, if the mail server is on the same system as IDM.                                                                                                                                                                                                                                                                                                          | YesOnly for `smtp` type.                         |
| `port`              | SMTP server port number, such as 25, 465, or 587.	Many SMTP servers require the use of a secure port such as 465 or 587. Many ISPs flag email from port 25 as spam.                                                                                                                                                                                                                                                                    | YesOnly for `smtp` type.                         |
| `debug`             | When set to `true`, this option outputs diagnostic messages from the JavaMail library. Debug mode can be useful if you are having difficulty configuring the external email endpoint with your mail server.                                                                                                                                                                                                                            | NoOnly for `smtp` type.                          |
| `from`              | Specifies a default From: address which displays when users receive emails from IDM.&#xA;&#xA;Although from is optional in the email configuration, the email service requires this property to send email. If you do not specify a from address in the email configuration, you must provide one in another way, for example:&#xA;&#xA;From an email template.&#xA;&#xA;As a parameter in the email service request (from or \_from). | No                                               |
| `auth`              | Contains authentication detail sub-properties. Refer to the [authentication sub-properties table](#auth-sub-prop-table) for all options.                                                                                                                                                                                                                                                                                               | YesRequired sub-properties vary based on `type`. |
| `starttls`          | If `"enable" : true`, enables the use of the STARTTLS command (if supported by the server) to switch the connection to a TLS-protected connection before issuing any login commands. If the server does not support STARTTLS, the connection continues without the use of TLS.                                                                                                                                                         | NoOnly for `smtp` type.                          |
| `ssl`               | Set `"enable" : true` to use SSL to connect, and use the SSL port by default.                                                                                                                                                                                                                                                                                                                                                          | NoOnly for `smtp` type.                          |
| `smtpProperties`    | SMTP options. Refer to the [SMTP sub-properties table](#smtp-sub-prop-table) for all options.                                                                                                                                                                                                                                                                                                                                          | NoOnly for `smtp` type.                          |
| `threadPoolSize`    | Emails are sent in separate threads managed by a thread pool. This property sets the number of concurrent emails that can be handled at a specific time. The default thread pool size (if none is specified) is `20`.                                                                                                                                                                                                                  | No                                               |
| `connectiontimeout` | The socket connection timeout, in milliseconds. The default connection timeout (if none is specified) is `300000` milliseconds, or 5 minutes. A setting of 0 disables this timeout.                                                                                                                                                                                                                                                    | No                                               |
| `timeout`           | The socket read timeout, in milliseconds. The default read timeout (if none is specified) is `300000` milliseconds, or 5 minutes. A setting of 0 disables this timeout.                                                                                                                                                                                                                                                                | NoOnly for `smtp` type.                          |
| `writetimeout`      | The socket write timeout, in milliseconds. The default write timeout (if none is specified) is `300000` milliseconds, or 5 minutes. A setting of 0 disables this timeout.                                                                                                                                                                                                                                                              | NoOnly for `smtp` type.                          |

**auth sub-properties**

| Property                                                                                          | Description                                                                                                                                                                                                                                                             | Required? / Type Support |
| ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `enable`                                                                                          | Whether you need login credentials to connect to the server/API.&#xA;&#xA;If "enable" : false,, you can leave the entries for "username" and "password" empty:&#xA;&#xA;"enable" : false,&#xA;"username" : "",&#xA;"password" : ""                                      | Yes                      |
| `username`                                                                                        | Account used to connect to the server/API.                                                                                                                                                                                                                              | No                       |
| `password`                                                                                        | Password used to connect to the server/API.                                                                                                                                                                                                                             | No                       |
| `type`                                                                                            | Authentication type used to connect to the server/API:- `basic`—basic authentication using a username and password. Default value.

- `oauth2`—OAuth2 authentication. Requires additional `oauth2` properties. The `msgraph` configuration type only supports `oauth2`. | Yes                      |
| `oauth2` propertiesThe following properties are only applicable when the `auth/type` is `oauth2`: |                                                                                                                                                                                                                                                                         |                          |
| `clientId`                                                                                        | *clientId* used to request an access token from the token endpoint. Obtained during [Azure application creation](#note-clientId). To store as a secret, refer to [Storing MS Azure credentials as a secret](#secret-rotation-email).                                    | Yes                      |
| `clientSecret`                                                                                    | clientSecret used to request an access token from the token endpoint. Obtained during [Azure application creation](#note-clientSecret). To store as a secret, refer to [Storing MS Azure credentials as a secret](#secret-rotation-email).                              | Yes                      |
| `tokenEndpoint`                                                                                   | OAuth2 token endpoint.Typical format:```none
https://login.microsoftonline.com/{tenant}.onmicrosoft.com/oauth2/v2.0/token
```                                                                                                                                           | Yes                      |
| `scope`                                                                                           | Requested OAuth2 scopes in a JSON array of strings.                                                                                                                                                                                                                     | Yes                      |
| `scopeDelimiter`                                                                                  | Scope delimiter to use. Defaults to space.                                                                                                                                                                                                                              | No                       |
| `grantType`                                                                                       | The only supported grant type is `client_credentials`.                                                                                                                                                                                                                  | No                       |

**smtpProperties sub-properties**

| Property                   | Description                                                                                                                                                                                                                                                                                     | Required? / Type Support |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `mail.smtp.ssl.protocols`  | The enabled SMTP SSL connection protocols. Protocols are specified as a whitespace-separated list. The default protocol is TLSv1.2.                                                                                                                                                             | NoOnly for `smtp` type.  |
| `mail.smtps.ssl.protocols` | The enabled SMTPS SSL connection protocols. Protocols are specified as a whitespace-separated list. The default protocol is TLSv1.2.                                                                                                                                                            | NoOnly for `smtp` type.  |
| `mail.mime.allowutf8`      | Adds support for UTF8 (Non-ASCII) characters in the *local* part of email addresses (everything before the `@` character) if set to `true`.&#xA;&#xA;Do not set this property unless your SMTP provider supports UTF8 characters.&#xA;&#xA;Can only be configured using REST or the filesystem. | NoOnly for `smtp` type.  |

## Email rate limiting

No rate limiting is applied to password reset emails, or any emails sent by the IDM server. This means that an attacker can potentially spam a known user account with an infinite number of emails, filling that user's inbox. In the case of password reset, the spam attack can obscure an actual password reset attempt.

In a production environment, you must configure email rate limiting through the network infrastructure in which IDM runs. Configure the network infrastructure to detect and prevent frequent repeated requests to publicly accessible web pages, such as the password reset page. You can also handle rate limiting within your email server.

---

---
title: Send email
description: Send email in PingIDM through REST API or script using the external/email endpoint, including template support and POST parameters
component: pingidm
version: 8.1
page_id: pingidm:external-services-guide:email-send
canonical_url: https://docs.pingidentity.com/pingidm/8.1/external-services-guide/email-send.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Email", "REST", "REST API", "JSON", "Scripts"]
section_ids:
  send-mail-rest: Send email using REST
  mail_templates: Mail templates
  send-mail-script: Send mail using a script
  mail_templates_2: Mail templates
  externalemail_post_parameters: external/email POST parameters
  section-mail-limiting1: Email rate limiting
---

# Send email

Typically, IDM sends emails from scripts and backend processes. Additionally, you can send test emails using the REST API.

## Send email using REST

In a production environment, you typically send mail from a script. To test your configuration, you can use the REST API by sending an HTTP POST to `/openidm/external/email`. Pass the message parameters as part of the POST payload, URL encoding the content, as necessary.

The following example sends a test email using the REST API:

```
curl \
--header "Content-Type: application/json" \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
--data '{
  "from": "openidm@example.com",
  "to": "your_email@example.com",
  "subject": "Test",
  "body": "Test"
}' \
"http://localhost:8080/openidm/external/email?_action=send"
{
  "status": "OK",
  "message": "Email sent"
}
```

By default, a response is only returned when the SMTP relay has completed. To return a response immediately, without waiting for the SMTP relay to finish, include the parameter `waitForCompletion=false` in the REST call. Use this option only if you do not need to verify that the email was accepted by the SMTP server. For example:

```
curl \
--header "Content-Type: application/json" \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
--data '{
  "from": "openidm@example.com",
  "to": "your_email@example.com",
  "subject": "Test",
  "body": "Test"
}' \
"http://localhost:8080/openidm/external/email?_action=send&waitForCompletion=false"
{
  "status": "OK",
  "message": "Email submitted"
}
```

### Mail templates

You can send an [email template](email-templates.html) using the `sendTemplate` action. For example:

```
curl \
--header "Content-Type: application/json" \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
--data '{
  "templateName": "welcome",
  "to": "your_email@example.com",
  "cc": "alt_email@example.com",
  "bcc": "bigBoss_email@example.com",
  "_locale": "fr"
}' \
"http://localhost:8080/openidm/external/email?_action=sendTemplate"
{
  "status": "OK",
  "message": "Email sent"
}
```

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Email templates utilize [Handlebar expressions](https://handlebarsjs.com/guide/) to reference object data dynamically. For example, to reference the `userName` of an object:```html
{{object.userName}}
``` |

## Send mail using a script

You can send email using the resource API functions, with the `external/email` context. Learn more about these functions in [openidm.action](../scripting-guide/scripting-func-ref.html#function-action). In the following example, `params` is an object that contains the POST parameters:

```javascript
var params =  new Object();
params.from = "openidm@example.com";
params.to = "your_email@example.com";
params.cc = "bjensen@example.com,scarter@example.com";
params.subject = "OpenIDM recon report";
params.type = "text/html";
params.body = "<html><body><p>Recon report follows...</p></body></html>";

openidm.action("external/email", "send", params);
```

### Mail templates

You can send an [email template](email-templates.html) using the `sendTemplate` action. For example:

Example 1

```javascript
var params =  new Object();
params.templateName = "welcome";
params.to = "your_email@example.com";
params.cc = "bjensen@example.com,scarter@example.com";
params.bcc = "bigBoss@example.com";
params._locale = "fr";

openidm.action("external/email", "sendTemplate", params);
```

Example 2

```javascript
var params = new Object();
params.templateName = "myTemplate";
params.to = "hgale815@example.com";
params.object = { "givenName": newObject.givenName, "sn": newObject.sn, "mail": newObject.mail, "country": newObject.country };

openidm.action("external/email", "sendTemplate", params);
```

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Email templates utilize [Handlebar expressions](https://handlebarsjs.com/guide/) to reference object data dynamically. For example, to reference the `userName` of an object:```html
{{object.userName}}
``` |

## `external/email` POST parameters

IDM supports the following POST parameters:

* `from`

  Sender mail address

* `to`

  Comma-separated list of recipient mail addresses

* `cc`

  Optional comma-separated list of copy recipient mail addresses

* `bcc`

  Optional comma-separated list of blind copy recipient mail addresses

* `subject`

  Email subject

* `body`

  Email body text

* `_locale`

  Takes precedence over `defaultLocale` but not `preferredLocales` specified in the `Accept-Language` header. If no preferred locales are set, uses the specified locale ([ISO 639-1 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).

* `type`

  Optional MIME type. One of `"text/plain"`, `"text/html"`, or `"text/xml"`.

## Email rate limiting

No rate limiting is applied to password reset emails, or any emails sent by the IDM server. This means that an attacker can potentially spam a known user account with an infinite number of emails, filling that user's inbox. In the case of password reset, the spam attack can obscure an actual password reset attempt.

In a production environment, you must configure email rate limiting through the network infrastructure in which IDM runs. Configure the network infrastructure to detect and prevent frequent repeated requests to publicly accessible web pages, such as the password reset page. You can also handle rate limiting within your email server.
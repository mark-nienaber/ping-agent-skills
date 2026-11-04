---
title: Access external REST services
description: Configure the Advanced Identity Cloud external REST service to make dynamic HTTP calls to remote REST endpoints from scripts or API requests
component: pingoneaic
page_id: pingoneaic:external-services:external-rest
canonical_url: https://docs.pingidentity.com/pingoneaic/external-services/external-rest.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  configuring-external-rest: Configure the external REST service
  external.rest.properties: External REST configuration properties
  invocation-parameters: Invocation parameters
  non-json-responses: Support for non-JSON responses
---

# Access external REST services

The external REST service lets you access remote REST services at the `openidm/external/rest` context path or by specifying the `external/rest` resource in your scripts. This service is not intended as a full connector to synchronize or reconcile identity data, but as a way to make dynamic HTTP calls as part of the PingOne Advanced Identity Cloud logic. For more declarative and encapsulated interaction with remote REST services, and for synchronization or reconciliation operations, use the scripted REST implementation of the [Groovy connector toolkit](https://docs.pingidentity.com/openicf/connector-reference/groovy.html).

An external REST call via a script may look something like the following:

```javascript
openidm.action("external/rest", "call", params);
```

The `call` parameter specifies the action name to be used for this invocation and is the standard method signature for the [`openidm.action` method](../idm-scripting/scripting-func-engine.html#function-action).

An external REST call over REST may resemble the following:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
--data '{
  "url": "http://urlecho.appspot.com/echo?status=200&Content-Type=application%2Fjson&body=%5B%7B%22key%22%3A%22value%22%7D%5D",
  "method": "GET"
}' \
"https://<tenant-env-fqdn>/openidm/external/rest?_action=call"
[
  {
    "key": "value"
  }
]
```

## Configure the external REST service

You can edit the external REST configuration over REST at the `config/external.rest` endpoint; for example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-type: application/json" \
--request PUT \
--data '{
  "socketTimeout" : "10 s",
  "connectionTimeout" : "10 s",
  "reuseConnections" : true,
  "retryRequests" : true,
  "maxConnections" : 64,
  "tlsVersion" : "TLSv1.2",
  "hostnameVerifier" : "STRICT",
  "proxy" : {
    "proxyUri" : "",
    "userName" : "",
    "password" : ""
  }
}' \
"https://<tenant-env-fqdn>/openidm/config/external.rest"
{
  "_id": "external.rest",
  "socketTimeout": "10 s",
  "connectionTimeout": "10 s",
  "reuseConnections": true,
  "retryRequests": true,
  "maxConnections": 64,
  "tlsVersion" : "TLSv1.2",
  "hostnameVerifier" : "STRICT",
  "proxy": {
    "proxyUri": "",
    "userName": "",
    "password": ""
  }
}
```

### External REST configuration properties

* `socketTimeout` (string)

  The TCP socket timeout, in seconds, when waiting for HTTP responses. The default timeout is 10 seconds.

* `connectionTimeout` (string)

  The TCP connection timeout for new HTTP connections, in seconds. The default timeout is 10 seconds.

* []()`pooledConnectionTtl` (integer)

  Specifies the maximum time to live (TTL), in milliseconds, for pooled HTTP connections. Connections in the pool older than the TTL aren't reused. The default value of `-1` means pooled connections don't expire.

  Set a TTL when a remote service or an intermediary, such as a load balancer, closes long-lived connections. For example, after an idle timeout or when the connection reaches a maximum age. Stale connections left in the pool can cause request failures. Set the TTL lower than the shortest connection lifetime your infrastructure imposes, so the pool retires connections before the remote end can close them.

  |   |                                                                                                                                                                                                                                         |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The value must be a number of milliseconds. Unlike the `socketTimeout` and `connectionTimeout` properties, this property doesn't accept duration values. A value such as `"1 s"` can prevent the external REST service from activating. |

* `reuseConnections` (boolean, true or false)

  Specifies whether HTTP connections should be kept alive and reused for additional requests. By default, connections will be reused if possible.

* `retryRequests` (boolean, true or false)

  Specifies whether requests should be retried if a failure is detected. By default, requests will be retried.

* `maxConnections` (integer)

  The maximum number of connections pooled by the HTTP client. `64` connections are the most pooled by default.

* `tlsVersion` (string)

  The TLS version that should be used for connections.

  In some cases, you may need to specify a different TLS version; for example, if you are connecting to a legacy system that supports an old version of TLS that is not accommodated by the backward-compatibility mode of your Java client.

  Valid versions for this parameter include `TLSv1.1`, `TLSv1.2`, and `TLSv1.3`.

* `hostnameVerifier` (string)

  The external REST service checks that the certificate presented by the server allows the hostname of the SSL client.

  The property can take the following values:

  |             |                                                                                                                                            |
  | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
  | `STRICT`    | Hostnames are validated.                                                                                                                   |
  | `ALLOW_ALL` | The external REST service does not attempt to match the URL hostname to the SSL certificate Common Name as part of its validation process. |

  If you do not set this property, the behavior is to validate hostnames (the equivalent of setting `"hostnameVerifier": "STRICT"`). In production environments, you *should* set this property to `STRICT`.

* []()`userAgent` (string)

  Specifies the value of the `User-Agent` header for requests made by the external REST service. If not set, the `"PingIdentity"` value applies by default.

  Overriding the default `User-Agent` helps you:

  * **Improve logging and auditing**: Allow downstream Security Operations (SecOps) teams to easily identify, attribute, and filter Advanced Identity Cloud traffic in Security Information and Event Management (SIEM) logs. For example, `"MyCompany-AIC/1.0"` gives SecOps a consistent tag to search and filter on.

  * **Avoid bot-detection false positives**: Prevent Web Application Firewalls (WAFs) and third-party APIs from blocking or rate-limiting generic requests as automated bot traffic. For example, `"MyCompany-AIC/1.0 (fraud check)"` identifies a specific integration instead of resembling a generic script default.

  * **Differentiate environments**: Distinguish between sandbox and production integration calls on receiving endpoints by including environment-specific tags. For example, set the value to `"MyCompany-AIC/1.0 (sandbox)"` in your sandbox environment and to `"MyCompany-AIC/1.0"` in your production environment.

  * **Obfuscate underlying systems in use**: The default `"PingIdentity"` value doesn't disclose the HTTP client implementation or version to receiving endpoints. For even greater obfuscation, set a custom value. For example, set the value to `"batch-sync/1.0"`.

    You can set this value in the following ways, listed highest to lowest precedence:

  * Per-request, using the `User-Agent` header in the `headers` parameter:

    Example request

    ```
    curl \
    --header "Authorization: Bearer <access-token>" \
    --request POST \
    --header "Content-Type: application/json" \
    --header "Accept-API-Version: resource=1.0" \
    --data '{
      "url": "http://echo-http-requests.appspot.com/echo?status=200&Content-Type=application%2Fjson&body=%5B%7B%22key%22%3A%22value%22%7D%5D",
      "method": "GET",
      "headers": {
        "User-Agent": "MyCompany-AIC/1.0"
      }
    }' \
      "https://<tenant-env-fqdn>/openidm/external/rest?_action=call"
    ```

    > **Collapse: Show example response**
    >
    > ```json
    > {
    >   "request": {
    >     "body": "",
    >     "created": "2026-02-25 21:29:20.253693",
    >     "headers": {
    >       "Content-Type": "application/json; charset=\"utf-8\"",
    >       "Host": "echo-http-requests.appspot.com",
    >       "Traceparent": "00-3daffaa2187dd81345f37b1837661a26-65404f3040d5b362-00",
    >       "User-Agent": "MyCompany-AIC/1.0",
    >       "X-Cloud-Trace-Context": "3daffaa2187dd81345f37b1837661a26/7295918465004974946",
    >       "X-Forgerock-Transactionid": "31fa216a-333e-4e25-9ba0-2c073794121b-387/0"
    >     },
    >     "http_version": "HTTP/1.1",
    >     "method": "GET",
    >     "query_string": "status=200&Content-Type=application%2Fjson&body=%5B%7B%22key%22%3A%22value%22%7D%5D",
    >     "remote_address": "203.0.113.47",
    >     "url": "http://echo-http-requests.appspot.com/echo?status=200&Content-Type=application%2Fjson&body=%5B%7B%22key%22%3A%22value%22%7D%5D"
    >   },
    >   "status": "OK"
    > }
    > ```

  * Globally, by setting the `userAgent` property in the external REST configuration:

    You can set the `userAgent` property to an Environment Secrets and Variables (ESV) configuration placeholder, for example `"&{esv.user.agent}"`, instead of a static value. This keeps the configuration itself identical across environments while the ESV resolves to the different sandbox and production values described earlier. Learn more in [Configure placeholders to use with ESVs](../tenants/configuration-placeholders.html).

    |   |                                                                                                                                                                                                                                                                          |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | Use only printable ASCII characters, and avoid control characters, which can break header parsing. If your value contains spaces or punctuation, ensure your tooling quotes it correctly in JSON or shell syntax ([RFC 9110](https://www.rfc-editor.org/info/rfc9110/)). |

    Example request

    ```
    curl \
    --header "Authorization: Bearer <access-token>" \
    --header "Accept-API-Version: resource=1.0" \
    --header "Content-Type: application/json" \
    --request PUT \
    --data '{
      "socketTimeout": "10 s",
      "connectionTimeout": "10 s",
      "reuseConnections": true,
      "retryRequests": true,
      "maxConnections": 64,
      "tlsVersion": "TLSv1.2",
      "userAgent": "&{esv.user.agent}",
      "proxy": {
        "proxyUri": "",
        "userName": "",
        "password": ""
      }
    }' \
    "https://<tenant-env-fqdn>/openidm/config/external.rest"
    ```

    > **Collapse: Show example response**
    >
    > ```json
    > {
    >   "_id": "external.rest",
    >   "socketTimeout": "10 s",
    >   "connectionTimeout": "10 s",
    >   "reuseConnections": true,
    >   "retryRequests": true,
    >   "maxConnections": 64,
    >   "tlsVersion": "TLSv1.2",
    >   "userAgent": "&{esv.user.agent}",
    >   "proxy": {
    >     "proxyUri": "",
    >     "userName": "",
    >     "password": ""
    >   }
    > }
    > ```

## Invocation parameters

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

  Indicates the response must be wrapped in the headers/body JSON message format, even if the response was JSON and would otherwise be passed through unchanged.

  If you need to distinguish the HTTP 20x response codes, you must invoke the external REST service with `forceWrap=true`. For failure cases, the HTTP status code is present within the wrapped response embedded in the exception detail or through the resource exception itself. For example:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Content-Type: application/json" \
  --header "Accept-API-Version: resource=1.0" \
  --request POST \
  --data '{
    "url": "http://urlecho.appspot.com/echo?status=203&Content-Type=application%2Fjson&body=%5B%7B%22key%22%3A%22value%22%7D%5D",
    "method": "GET",
    "forceWrap": true}' \
  "https://<tenant-env-fqdn>/openidm/external/rest?_action=call"
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

  Advanced Identity Cloud supports the following authentication types:

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

## Support for non-JSON responses

The external REST service supports any arbitrary payload (currently in stringified format). If the response is anything other than JSON, a JSON message object is returned:

* For text-compatible (non-JSON) content, Advanced Identity Cloud returns a JSON object similar to the following:

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
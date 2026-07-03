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

## Support for non-JSON responses

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

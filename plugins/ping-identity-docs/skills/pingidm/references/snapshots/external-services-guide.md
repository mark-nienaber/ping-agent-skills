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

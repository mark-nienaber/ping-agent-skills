---
title: Assured replication request control
description: Add the assured replication request control to a Directory REST API request to delay the response until replication requirements are satisfied
component: pingdirectory
page_id: pingdirectory:directory:controls/assured-replication-request-control
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/controls/assured-replication-request-control.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Assured replication request control

This control may be included in an add, delete, modify, or modify DN request to indicate that the server should delay the response for that operation until it has satisfied certain replication requirements. The control has an OID of 1.3.6.1.4.1.30221.2.5.28, and it takes a value. The following fields may be present in the `value-json` representation of the value:

* `minimum-local-level`: An optional string field whose value is the name of the minimum assurance level desired for replicas in the same location as the target server. The value may be one of "none", "received-any-server", or "processed-all-servers". If this is not specified, then the server will choose an appropriate minimum local assurance level based on its configuration.

* `maximum-local-level`: An optional string field whose value is the name of the maximum assurance level desired for local replicas. If specified (with a value of "none", "received-any-server", or "processed-all-servers"), it may cause the server to use a lower local assurance level than it may have otherwise chosen based on configuration. If this is not specified, then the server will choose an appropriate maximum local assurance level based on its configuration and the minimum local assurance level.

* `minimum-remote-level`: An optional string field whose value is the name of the minimum assurance level desired for replicas in a different location from the target server. The value may be one of "none", "received-any-remote-location", "received-all-remote-locations", or "processed-all-remote-servers". If this is not specified, then the server will choose an appropriate minimum remote assurance level based on its configuration.

* `maximum-remote-level`: An optional string field whose value is the name of the maximum assurance level desired for remote replicas. If specified (with a value of "none", "received-any-remote-location", "received-all-remote-locations", or "processed-all-remote-servers"), it may cause the server to use a lower remote assurance level than it may have otherwise chosen based on configuration. If this is not specified, then the server will choose an appropriate maximum remote assurance level based on its configuration and the minimum remote assurance level.

* `timeout-millis`: An optional integer field whose value specifies the maximum length of time in milliseconds that the server should wait for assurance to be satisfied. If this is not specified, then the server will choose an appropriate timeout.

* `send-response-immediately`: A Boolean field that indicates whether the server should return the response to the client immediately after applying the change locally, even if it has not yet been replicated. Sending the response immediately is primarily useful if the client will monitor the replication status for the operation.

The following sample shows the JSON encoding for the control:

```json
{ "oid":"1.3.6.1.4.1.30221.2.5.28",
  "control-name":"Assured Replication Request Control",
  "criticality":false,
  "value-json":{ "minimum-local-level":"received-any-server",
                 "minimum-remote-level":"received-any-remote-location",
                 "timeout-millis":1000
    }
}
```

---

---
title: Get All Schemas
description: Retrieve a list of all configured objectClass entities and their schemas using the PingDirectory Directory REST API
component: pingdirectory
page_id: pingdirectory:directory:schemas-apis/get-all-schemas
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/schemas-apis/get-all-schemas.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Get All Schemas

##

```none
GET {{apiPath}}/directory/v1/schemas/
```

The `GET /directory/v1/schemas` endpoint returns a list of all configured objectClass entities on the server. If no `objectClass` entities are configured on the directory server, the request returns an empty list.

The sample gets all configured `schemas` and their associated `objectClass` entities.

### Headers

Authorization      Bearer {{accessToken}}

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/directory/v1/schemas/' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/directory/v1/schemas/")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Authorization", "Bearer {{accessToken}}");
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/directory/v1/schemas/"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
GET /directory/v1/schemas/ HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/directory/v1/schemas/")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/directory/v1/schemas/",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Authorization": "Bearer {{accessToken}}"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{apiPath}}/directory/v1/schemas/',
  'headers': {
    'Authorization': 'Bearer {{accessToken}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{apiPath}}/directory/v1/schemas/"

payload = {}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/directory/v1/schemas/');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Authorization' => 'Bearer {{accessToken}}'
));
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "net/http"

url = URI("{{apiPath}}/directory/v1/schemas/")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/directory/v1/schemas/")!,timeoutInterval: Double.infinity)
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "GET"

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

200 OK

```json
{
  "schemas": [
    {
      "$schema": "http://json-schema.org/draft-07/schema#23",
      "title": "top",
      "required": ["objectClass"],
      "classType": "abstract",
      "type": "object",
      "properties": {
        "objectClass": {
          "type": array,
          "items": {"type": "string"},
          "contains": {"const": "top"},
          "description": "Since 'top' is an abstract objectClass, new objects cannot be created with only 'top' as the objectClass value. A structural objectClass that derives from 'top' must be included"
        }
      },
      "additionalProperties": false,
      "_links": {
        "self": {
          "href": "https://localhost:5034/directory/v1/schemas/top"
        }
      }
    },
    {
      "$schema": "http://json-schema.org/draft-07/schema#23",
      "title": "person",
      ...
    },
    ...
  ],
  "_links": {
    "self: {
      "href": "https://localhost:5034/directory/v1/schemas"
    }
  }
}
```

---

---
title: Get an Entry
description: Retrieve a PingDirectory Server entry by its distinguished name using the Directory REST API GET operation
component: pingdirectory
page_id: pingdirectory:directory:directory-entry-apis/get-an-entry
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/directory-entry-apis/get-an-entry.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Get an Entry

##

```none
GET {{apiPath}}/directory/v1/{{dn}}
```

The following sample shows the `GET /directory/v1/{{dn}}` operation to return the directory entry specified by its distinguished name (`dn`).

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | This endpoint accepts the `expand`, `includeAttributes`, and `excludeAttributes` query parameters. |

### Headers

Authorization      Bearer {{accessToken}}

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/directory/v1/{{dn}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/directory/v1/{{dn}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Authorization", "Bearer {{accessToken}}");
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/directory/v1/{{dn}}"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
GET /directory/v1/{{dn}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/directory/v1/{{dn}}")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/directory/v1/{{dn}}",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Authorization": "Bearer {{accessToken}}"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{apiPath}}/directory/v1/{{dn}}',
  'headers': {
    'Authorization': 'Bearer {{accessToken}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{apiPath}}/directory/v1/{{dn}}"

payload = {}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/directory/v1/{{dn}}');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Authorization' => 'Bearer {{accessToken}}'
));
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "net/http"

url = URI("{{apiPath}}/directory/v1/{{dn}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/directory/v1/{{dn}}")!,timeoutInterval: Double.infinity)
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "GET"

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

200 OK

```json
{
  "_dn": "uid=lindajones,ou=people,dc=example,dc=com",
  "objectClass": [ "top", "ubidPerson" ],
  "uid": ["lindajones"],
  "cn": ["Linda Jones"],
  "sn": ["Jones"],
  "ubidEmailJSON": [
    {
      "type": "work",
      "value": "ljones@example.com"
    },
  ],
  "_links": {
    "schemas": [
      {
        "href": "https://ds.example.com/directory/v1/schemas/ubidPerson"
      }
    ],
    "self": {
      "href": "https://ds.example.com/directory/v1/uid=lindajones,ou=people,dc=example,dc=com"
    }
  }
}
```

---

---
title: Get an Entry (Exclude SN)
description: Retrieve a PingDirectory Server entry using the Directory REST API GET operation while excluding the sn attribute from the response
component: pingdirectory
page_id: pingdirectory:directory:directory-entry-apis/get-an-entry-exclude-sn
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/directory-entry-apis/get-an-entry-exclude-sn.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Get an Entry (Exclude SN)

##

```none
GET {{apiPath}}/directory/v1/{{dn}}?includeAttributes=*&excludeAttributes=sn
```

By default, endpoints that retrieve and list entry data return all user attributes and no operational attributes (unless the server is configured to return specified operational attributes by default). The `GET /directory/v1/{{dn}}` endpoint also supports fine-tuning the response data through the following query parameters:

* `includeAttributes`

  Specifies the attribute or attributes in the entry that should be included in the response.

* `excludeAttributes`

  Specifies the attribute or attributes in the entry that should be excluded in the response.

These query parameters accept a comma-separated list of attributes to either include or exclude from the response entries. They also support the following aliases as values:

* `*`

  Refers to all user attributes of the resource.

* `_operationalAttributes`

  Refers to all operational attributes of the resource.

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the same attribute is provided in both `includeAttributes` and `excludeAttributes`, an error is returned. When the ``**alias is used, the `excludeAttributes` parameter takes precedence. For example, `includeAttributes=`**`&excludeAttributes=sn` returns all user attributes except `sn`, but `excludeAttributes=*&includeAttributes=sn` returns no attributes (except DN). |

The sample shows the `GET /directory/v1/{{dn}}` operation to return the base entry and all user attributes for the entry, but exclude `sn`.

### Headers

Authorization      Bearer {{accessToken}}

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/directory/v1/{{dn}}?includeAttributes=*&excludeAttributes=sn' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/directory/v1/{{dn}}?includeAttributes=*&excludeAttributes=sn")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Authorization", "Bearer {{accessToken}}");
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/directory/v1/{{dn}}?includeAttributes=*&excludeAttributes=sn"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
GET /directory/v1/{{dn}}?includeAttributes=*&excludeAttributes=sn HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/directory/v1/{{dn}}?includeAttributes=*&excludeAttributes=sn")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/directory/v1/{{dn}}?includeAttributes=*&excludeAttributes=sn",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Authorization": "Bearer {{accessToken}}"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{apiPath}}/directory/v1/{{dn}}?includeAttributes=*&excludeAttributes=sn',
  'headers': {
    'Authorization': 'Bearer {{accessToken}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{apiPath}}/directory/v1/{{dn}}?includeAttributes=*&excludeAttributes=sn"

payload = {}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/directory/v1/{{dn}}?includeAttributes=*&excludeAttributes=sn');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Authorization' => 'Bearer {{accessToken}}'
));
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "net/http"

url = URI("{{apiPath}}/directory/v1/{{dn}}?includeAttributes=*&excludeAttributes=sn")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/directory/v1/{{dn}}?includeAttributes=*&excludeAttributes=sn")!,timeoutInterval: Double.infinity)
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "GET"

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

200 OK

```json
{
    "_dn": "uid=lindajones,ou=people,dc=example,dc=com",
    "uid": [
        "lindajones"
    ],
    "cn": [
        "Linda Jones",
        "Linda F. Jones"
    ],
    "objectClass": [
        "top",
        "person",
        "organizationalPerson",
        "inetOrgPerson"
    ],
    "createTimestamp": "2018-05-01T15:04:49.866Z",
    "modifyTimestamp": "2018-05-01T15:04:51.591Z",
    "_links": {
        "schemas": [
            {
                "href": "https://ds.example.com/directory/v1/schemas/inetOrgPerson"
            }
        ],
        "self": {
            "href": "https://ds.example.com/directory/v1/entryUUID=a4fbd3ca-f7a0-42f2-af66-13f2c0dd8cd1,ou=people,dc=example,dc=com"
        }
    }
}
```

---

---
title: Get Current User
description: Retrieve the record of the currently authenticated user from PingDirectory Server using the GET /directory/v1/me alias endpoint
component: pingdirectory
page_id: pingdirectory:directory:directory-entry-apis/get-current-user
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/directory-entry-apis/get-current-user.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Get Current User

##

```none
GET {{apiPath}}/directory/v1/me
```

In addition to retrieving a specified resource by providing the distinguished name, you can get the record of the currently authenticated user by calling the alias `GET /directory/v1/me`.

### Headers

Authorization      Bearer {{accessToken}}

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/directory/v1/me' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/directory/v1/me")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Authorization", "Bearer {{accessToken}}");
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/directory/v1/me"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
GET /directory/v1/me HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/directory/v1/me")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/directory/v1/me",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Authorization": "Bearer {{accessToken}}"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{apiPath}}/directory/v1/me',
  'headers': {
    'Authorization': 'Bearer {{accessToken}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{apiPath}}/directory/v1/me"

payload = {}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/directory/v1/me');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Authorization' => 'Bearer {{accessToken}}'
));
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "net/http"

url = URI("{{apiPath}}/directory/v1/me")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/directory/v1/me")!,timeoutInterval: Double.infinity)
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "GET"

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

200 OK

```json
{
  "_dn": "uid=lindajones,ou=people,dc=example,dc=com",
  "objectClass": [ "top", "ubidPerson" ],
  "uid": ["lindajones"],
  "cn": ["Linda Jones"],
  "sn": ["Jones"],
  "ubidEmailJSON": [
    {
      "type": "work",
      "value": "ljones@example.com"
    },
  ],
  "_links": {
    "schemas": [
      {
        "href": "https://ds.example.com/directory/v1/schemas/ubidPerson"
      }
    ],
    "self": {
      "href": "https://ds.example.com/directory/v1/uid=lindajones,ou=people,dc=example,dc=com"
    }
  }
}
```

---

---
title: Get effective rights request control
description: Add the get effective rights request control to a Directory REST API search request to return access control permissions a user has on matching entries
component: pingdirectory
page_id: pingdirectory:directory:controls/get-effective-rights-request-control
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/controls/get-effective-rights-request-control.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Get effective rights request control

The proprietary get effective rights request control may be included in a search request to indicate that matching entries should include one or more `aclRights` attributes with the access control permissions that a given user may have when interacting with the entry. The control has an OID of 1.3.6.1.4.1.42.2.27.9.5.2, and it takes a value. The following fields may be present in the `value-json` representation of the value:

* `authorization-id`: A mandatory string field whose value is the authorization identity of the user for whom to make the access control determination.

* `attributes`: An optional array field whose values are the names of the attributes for which to calculate effective rights. If this is not provided, or if it is empty, then the default behavior calculates effective rights for all user attributes in the entry.

The following sample shows the JSON encoding for the control:

```json
{
    "oid":"1.3.6.1.4.1.42.2.27.9.5.2",
    "control-name":"Get Effective Rights Request Control",
    "criticality":false,
    "value-json":{
        "authorization-id":"dn:uid=jdoe,ou=People,dc=example,dc=com",
        "attributes":[
            "uid",
            "mail",
            "telephoneNumber",
            "userPassword"
            ]
    }
}
```

---

---
title: Get Metadata
description: Retrieve server and API metadata, including configured schemas, from the PingDirectory Server Directory REST API base endpoint
component: pingdirectory
page_id: pingdirectory:directory:directory-entry-apis/get-metadata
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/directory-entry-apis/get-metadata.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Get Metadata

##

```none
GET {{apiPath}}/directory/v1
```

A `GET` request on the base endpoint, `/directory/v1`, returns metadata about the server and API. It also returns a list of configured schemas allowed on the server. The sample shows the `GET /directory/v1` operation.

When successful, the operation returns a `200 OK` message and the response data.

### Headers

Authorization      Bearer {{accessToken}}

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/directory/v1' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/directory/v1")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Authorization", "Bearer {{accessToken}}");
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/directory/v1"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
GET /directory/v1 HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/directory/v1")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/directory/v1",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Authorization": "Bearer {{accessToken}}"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{apiPath}}/directory/v1',
  'headers': {
    'Authorization': 'Bearer {{accessToken}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{apiPath}}/directory/v1"

payload = {}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/directory/v1');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Authorization' => 'Bearer {{accessToken}}'
));
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "net/http"

url = URI("{{apiPath}}/directory/v1")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/directory/v1")!,timeoutInterval: Double.infinity)
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "GET"

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

200 OK

```json
{
   "vendorName": "Ping Identity Corporation",
   "vendorVersion": "Ping Identity Directory Server 7.2.0.0",
   "startupUUID": "cb1ee26d-683d-43b9-817b-f41ffe68d21c",
   "startTime": "20181108171520Z",
   "publicBaseDNs": [
       "dc=example,dc=com"
   ],
   "_links": {
       "schemas": {
           "href": "https://ds.example.com/directory/v1/schemas"
       },
       "self": {
           "href": "https://ds.example.com/directory/v1/"
       },
       "publicBaseDNs": [
           {
               "href": "https://ds.example.com/directory/v1/dc=example,dc=com"
           }
       ]
   }
}
```

---

---
title: Get Operational Attributes
description: Retrieve the operational attributes configured on the server using the PingDirectory Directory REST API
component: pingdirectory
page_id: pingdirectory:directory:schemas-apis/get-operational-attributes
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/schemas-apis/get-operational-attributes.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Get Operational Attributes

##

```none
GET {{apiPath}}/directory/v1/schemas/_operationalAttributes
```

The `GET /directory/v1/schemas/_operationalAttributes` endpoint returns a list of all operational attributes configured on the server.

### Headers

Authorization      Bearer {{accessToken}}

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/directory/v1/schemas/_operationalAttributes' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/directory/v1/schemas/_operationalAttributes")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Authorization", "Bearer {{accessToken}}");
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/directory/v1/schemas/_operationalAttributes"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
GET /directory/v1/schemas/_operationalAttributes HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/directory/v1/schemas/_operationalAttributes")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/directory/v1/schemas/_operationalAttributes",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Authorization": "Bearer {{accessToken}}"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{apiPath}}/directory/v1/schemas/_operationalAttributes',
  'headers': {
    'Authorization': 'Bearer {{accessToken}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{apiPath}}/directory/v1/schemas/_operationalAttributes"

payload = {}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/directory/v1/schemas/_operationalAttributes');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Authorization' => 'Bearer {{accessToken}}'
));
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "net/http"

url = URI("{{apiPath}}/directory/v1/schemas/_operationalAttributes")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/directory/v1/schemas/_operationalAttributes")!,timeoutInterval: Double.infinity)
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "GET"

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

200 OK

```json
{
    "_operationalAttributes": {
        "aci": {
            "type": "array",
            "items": {
                "type": "string",
                "format": "Sun-defined Access Control Information"
            },
            "description": "Sun-defined access control information attribute type"
        },
        "aclRights": {
            "type": "string",
            "readOnly": true,
            "description": "Sun-defined access control effective rights attribute type"
        },
        "aclRightsInfo": {
            "type": "string",
            "readOnly": true,
            "description": "Sun-defined access control effective rights information attribute type"
        },
        "administratorsAddress": {
            "type": "array",
            "items": {
                "type": "string",
                "format": "IA5 String"
            }
        },
        "altServer": {
            "type": "array",
            "items": {
                "type": "string",
                "format": "IA5 String"
            }
        },
        "attributeTypes": {
            "type": "array",
            "items": {
                "type": "string",
                "format": "Attribute Type Description"
            }
        },
        "baselineConfigurationDigest": {
            "type": "string"
        },
        "blockInheritance": {
            "type": "boolean",
            "readOnly": true
        },
        "changeTime": {
            "type": "string",
            "readOnly": true,
            "description": "the GMT time when the changelog entry was created"
        },
        "changelog-add-entry": {
            "type": "string",
            "format": "Octet String",
            "readOnly": true
        },
        "changelog-deleted-entry": {
            "type": "string",
            "format": "Octet String",
            "readOnly": true
        },


        ...
}
```

---

---
title: Get Password Quality Requirements
description: Retrieve the password quality requirements that apply to a new password for an add, self change, or administrative reset using the PingDirectory Directory REST API
component: pingdirectory
page_id: pingdirectory:directory:extended-operations/get-password-quality-requirements/get-password-quality-requirements
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/extended-operations/get-password-quality-requirements/get-password-quality-requirements.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  request-body: Request body
  response-body: Response body
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Get Password Quality Requirements

##

```none
POST {{apiPath}}/directory/v1/passwordRequirements
```

The `POST /directory/v1/passwordRequirements` request performs the LDAP get password quality requirements extended operation through HTTP.

### Request body

The request may include the following fields:

* `operationType`

  A required parameter that specifies the type of operation in which the new password will be used. The value for this parameter must be one of the following:

  * `add`

    The new password will be used to create a new user.

  * `selfChange`

    The new password will be used for a self password change.

  * `administrativeReset`

    The new password will be used for an administrative password reset.

* `userDN`

  The DN of the target user who will be using the password.

  * This is required if the `operationType` is `administrativeReset`.

  * The must be absent if the `operationType` is `add`.

  * If the request has an authorization header and the new password is for the user associated with that authorization identity, it can be absent for an `operationType` of `selfChange`.

* `passwordPolicyDN`

  An optional parameter that specifies the DN of the password policy to determine the requirements for a new user.

  * This must be absent for an `operationType` of `selfChange` or `administrativeReset`.

  * It can be present for an `operationType` of `add`.

    |   |                                                                      |
    | - | -------------------------------------------------------------------- |
    |   | 	If it is absent, then the server's default password policy is used. |

* `_controls`

  An optional array of JSON-formatted request controls to be used when processing the get password quality requirements request. These controls are narrowed down based on which conversions from JSON to LDAP are currently implemented by the Directory REST API. Documentation for all controls supported by the Directory REST API are listed here.

  * [Operation Purpose Request Control](../../controls/operation-purpose-request-control.html)

  * [Intermediate Client Request Control](../../controls/intermediate-client-request-control.html)

  * [Intermediate Client Response Control](../../controls/intermediate-client-response-control.html)

  * [Proxied Authorization v1 Request Control](../../controls/proxied-authorization-v1-request-control.html)

  * [Proxied Authorization v2 Request Control](../../controls/proxied-authorization-v2-request-control.html)

|   |                                                                                      |
| - | ------------------------------------------------------------------------------------ |
|   | 	The No operation request control is read-only and not supported for this operation. |

### Response body

The response must include a body that is formatted as a JSON object. Upon a successful operation where the LDAP `resultCode value` is `0` and HTTP status code is `200`, the following fields will be included in the JSON object:

* `resultCode`

  A required JSON object that contains the following fields:

  * `value`

    The required integer value for the LDAP result code.

  * `name`

    A name for the LDAP result code. This is optional but recommended.

* `matchedDN`

  An optional string field that holds the matched DN for the operation. You can omit this if no matched DN value is needed or appropriate.

* `diagnosticMessage`

  An optional string field that holds a human-readable message with additional information about the operation. You can omit this if no diagnostic message is needed or appropriate.

* `passwordQualityRequirements`

  A required array of JSON objects that represent the set of password quality requirements that the server will impose. This field will be returned even if the array of JSON objects is empty. Each of these objects should include the following fields:

  * `description`

    A required string field that provides a user-friendly description for the environment.

  * `client-side-validation-type`

    An optional string field that contains the name of the client-side validation type for the requirement.

  * `client-side-validation-properties`

    An optional array of JSON objects with the client-side validation properties for the requirement. Each of these objects should include the following fields:

    * `name`

      A required string field with the name for the client-side validation property.

    * `value`

      A required string field with the value for the client-side validation property.

* `currentPasswordRequired`

  An optional Boolean field that indicates whether the target user is required to provide their current password when choosing a new password. This field is present in a successful response to a request for a self password change, and is absent otherwise.

* `mustChangePassword`

  An optional Boolean field that indicates whether the target user will be required to choose a new password after an administrative reset. This field is present in a successful response to a request for an add or an administrative password reset, and is absent otherwise.

* `secondsUntilExpiration`

  An optional integer field that specifies the length of time that a new password is considered valid for the requested type of operation. This field is absent if the request was not processed successfully or if the new password may be used indefinitely.

* `_controls`

  An optional array of JSON-formatted response controls.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "operationType": "administrativeReset",
    "userDN": "uid=jimbob,ou=people,dc=example,dc=com",
    "_controls": [
        {
            "oid": "1.3.6.1.4.1.30221.2.5.19",
            "criticality": true,
            "value-json": {
                "application-name": "22, A Million",
                "application-version": "22.1000000.0",
                "code-location": "authenticateUser",
                "request-purpose": "It might be over soon"
            }
        },
        {
            "oid": "1.3.6.1.4.1.30221.2.5.2",
            "criticality": true,
            "value-json": {
                "downstream-client-address": "6.6.6",
                "downstream-client-secure": true
            }
        }
    ]
}
```

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/directory/v1/passwordRequirements' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "operationType": "administrativeReset",
    "userDN": "uid=jimbob,ou=people,dc=example,dc=com",
    "_controls": [
        {
            "oid": "1.3.6.1.4.1.30221.2.5.19",
            "criticality": true,
            "value-json": {
                "application-name": "22, A Million",
                "application-version": "22.1000000.0",
                "code-location": "authenticateUser",
                "request-purpose": "It might be over soon"
            }
        },
        {
            "oid": "1.3.6.1.4.1.30221.2.5.2",
            "criticality": true,
            "value-json": {
                "downstream-client-address": "6.6.6",
                "downstream-client-secure": true
            }
        }
    ]
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/directory/v1/passwordRequirements")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""operationType"": ""administrativeReset""," + "\n" +
@"    ""userDN"": ""uid=jimbob,ou=people,dc=example,dc=com""," + "\n" +
@"    ""_controls"": [" + "\n" +
@"        {" + "\n" +
@"            ""oid"": ""1.3.6.1.4.1.30221.2.5.19""," + "\n" +
@"            ""criticality"": true," + "\n" +
@"            ""value-json"": {" + "\n" +
@"                ""application-name"": ""22, A Million""," + "\n" +
@"                ""application-version"": ""22.1000000.0""," + "\n" +
@"                ""code-location"": ""authenticateUser""," + "\n" +
@"                ""request-purpose"": ""It might be over soon""" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        {" + "\n" +
@"            ""oid"": ""1.3.6.1.4.1.30221.2.5.2""," + "\n" +
@"            ""criticality"": true," + "\n" +
@"            ""value-json"": {" + "\n" +
@"                ""downstream-client-address"": ""6.6.6""," + "\n" +
@"                ""downstream-client-secure"": true" + "\n" +
@"            }" + "\n" +
@"        }" + "\n" +
@"    ]" + "\n" +
@"}";
request.AddStringBody(body, DataFormat.Json);
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/directory/v1/passwordRequirements"
  method := "POST"

  payload := strings.NewReader(`{
    "operationType": "administrativeReset",
    "userDN": "uid=jimbob,ou=people,dc=example,dc=com",
    "_controls": [
        {
            "oid": "1.3.6.1.4.1.30221.2.5.19",
            "criticality": true,
            "value-json": {
                "application-name": "22, A Million",
                "application-version": "22.1000000.0",
                "code-location": "authenticateUser",
                "request-purpose": "It might be over soon"
            }
        },
        {
            "oid": "1.3.6.1.4.1.30221.2.5.2",
            "criticality": true,
            "value-json": {
                "downstream-client-address": "6.6.6",
                "downstream-client-secure": true
            }
        }
    ]
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
POST /directory/v1/passwordRequirements HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "operationType": "administrativeReset",
    "userDN": "uid=jimbob,ou=people,dc=example,dc=com",
    "_controls": [
        {
            "oid": "1.3.6.1.4.1.30221.2.5.19",
            "criticality": true,
            "value-json": {
                "application-name": "22, A Million",
                "application-version": "22.1000000.0",
                "code-location": "authenticateUser",
                "request-purpose": "It might be over soon"
            }
        },
        {
            "oid": "1.3.6.1.4.1.30221.2.5.2",
            "criticality": true,
            "value-json": {
                "downstream-client-address": "6.6.6",
                "downstream-client-secure": true
            }
        }
    ]
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"operationType\": \"administrativeReset\",\n    \"userDN\": \"uid=jimbob,ou=people,dc=example,dc=com\",\n    \"_controls\": [\n        {\n            \"oid\": \"1.3.6.1.4.1.30221.2.5.19\",\n            \"criticality\": true,\n            \"value-json\": {\n                \"application-name\": \"22, A Million\",\n                \"application-version\": \"22.1000000.0\",\n                \"code-location\": \"authenticateUser\",\n                \"request-purpose\": \"It might be over soon\"\n            }\n        },\n        {\n            \"oid\": \"1.3.6.1.4.1.30221.2.5.2\",\n            \"criticality\": true,\n            \"value-json\": {\n                \"downstream-client-address\": \"6.6.6\",\n                \"downstream-client-secure\": true\n            }\n        }\n    ]\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/directory/v1/passwordRequirements")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/directory/v1/passwordRequirements",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "operationType": "administrativeReset",
    "userDN": "uid=jimbob,ou=people,dc=example,dc=com",
    "_controls": [
      {
        "oid": "1.3.6.1.4.1.30221.2.5.19",
        "criticality": true,
        "value-json": {
          "application-name": "22, A Million",
          "application-version": "22.1000000.0",
          "code-location": "authenticateUser",
          "request-purpose": "It might be over soon"
        }
      },
      {
        "oid": "1.3.6.1.4.1.30221.2.5.2",
        "criticality": true,
        "value-json": {
          "downstream-client-address": "6.6.6",
          "downstream-client-secure": true
        }
      }
    ]
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{apiPath}}/directory/v1/passwordRequirements',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "operationType": "administrativeReset",
    "userDN": "uid=jimbob,ou=people,dc=example,dc=com",
    "_controls": [
      {
        "oid": "1.3.6.1.4.1.30221.2.5.19",
        "criticality": true,
        "value-json": {
          "application-name": "22, A Million",
          "application-version": "22.1000000.0",
          "code-location": "authenticateUser",
          "request-purpose": "It might be over soon"
        }
      },
      {
        "oid": "1.3.6.1.4.1.30221.2.5.2",
        "criticality": true,
        "value-json": {
          "downstream-client-address": "6.6.6",
          "downstream-client-secure": true
        }
      }
    ]
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests
import json

url = "{{apiPath}}/directory/v1/passwordRequirements"

payload = json.dumps({
  "operationType": "administrativeReset",
  "userDN": "uid=jimbob,ou=people,dc=example,dc=com",
  "_controls": [
    {
      "oid": "1.3.6.1.4.1.30221.2.5.19",
      "criticality": True,
      "value-json": {
        "application-name": "22, A Million",
        "application-version": "22.1000000.0",
        "code-location": "authenticateUser",
        "request-purpose": "It might be over soon"
      }
    },
    {
      "oid": "1.3.6.1.4.1.30221.2.5.2",
      "criticality": True,
      "value-json": {
        "downstream-client-address": "6.6.6",
        "downstream-client-secure": True
      }
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/directory/v1/passwordRequirements');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "operationType": "administrativeReset",\n    "userDN": "uid=jimbob,ou=people,dc=example,dc=com",\n    "_controls": [\n        {\n            "oid": "1.3.6.1.4.1.30221.2.5.19",\n            "criticality": true,\n            "value-json": {\n                "application-name": "22, A Million",\n                "application-version": "22.1000000.0",\n                "code-location": "authenticateUser",\n                "request-purpose": "It might be over soon"\n            }\n        },\n        {\n            "oid": "1.3.6.1.4.1.30221.2.5.2",\n            "criticality": true,\n            "value-json": {\n                "downstream-client-address": "6.6.6",\n                "downstream-client-secure": true\n            }\n        }\n    ]\n}');
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "json"
require "net/http"

url = URI("{{apiPath}}/directory/v1/passwordRequirements")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "operationType": "administrativeReset",
  "userDN": "uid=jimbob,ou=people,dc=example,dc=com",
  "_controls": [
    {
      "oid": "1.3.6.1.4.1.30221.2.5.19",
      "criticality": true,
      "value-json": {
        "application-name": "22, A Million",
        "application-version": "22.1000000.0",
        "code-location": "authenticateUser",
        "request-purpose": "It might be over soon"
      }
    },
    {
      "oid": "1.3.6.1.4.1.30221.2.5.2",
      "criticality": true,
      "value-json": {
        "downstream-client-address": "6.6.6",
        "downstream-client-secure": true
      }
    }
  ]
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"operationType\": \"administrativeReset\",\n    \"userDN\": \"uid=jimbob,ou=people,dc=example,dc=com\",\n    \"_controls\": [\n        {\n            \"oid\": \"1.3.6.1.4.1.30221.2.5.19\",\n            \"criticality\": true,\n            \"value-json\": {\n                \"application-name\": \"22, A Million\",\n                \"application-version\": \"22.1000000.0\",\n                \"code-location\": \"authenticateUser\",\n                \"request-purpose\": \"It might be over soon\"\n            }\n        },\n        {\n            \"oid\": \"1.3.6.1.4.1.30221.2.5.2\",\n            \"criticality\": true,\n            \"value-json\": {\n                \"downstream-client-address\": \"6.6.6\",\n                \"downstream-client-secure\": true\n            }\n        }\n    ]\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/directory/v1/passwordRequirements")!,timeoutInterval: Double.infinity)
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "POST"
request.httpBody = postData

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

200 OK

```json
{
    "resultCode": {
        "value": 0,
        "name": "success"
    },
    "passwordQualityRequirements": [],
    "mustChangePassword": "false",
    "_controls": [
        {
            "oid": "1.3.6.1.4.1.30221.2.5.2",
            "control-name": "Intermediate Client Response Control",
            "criticality": false,
            "value-json": {
                "server-name": "PingDirectory",
                "server-session-id": "conn=-1403",
                "server-response-id": "op=61007"
            }
        }
    ]
}
```

---

---
title: Get Password Quality Requirements
description: The Get Password Quality Requirements extended operation is applicable for user-facing applications that allow users to create accounts or change passwords. This operation enables applications to display a list of the requirements that the new password must satisfy at the initial password request.
component: pingdirectory
page_id: pingdirectory:directory:extended-operations/get-password-quality-requirements/index
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/extended-operations/get-password-quality-requirements/index.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
---

# Get Password Quality Requirements

The Get Password Quality Requirements extended operation is applicable for user-facing applications that allow users to create accounts or change passwords. This operation enables applications to display a list of the requirements that the new password must satisfy at the initial password request.

The Get Password Quality Requirements extended operation is not a standard LDAP operation and has been developed internally for use within PingDirectory products. Its implementation in the Directory REST API is based on the following classes in the UnboundID LDAP SDK:

* [GetPasswordQualityRequirementsExtendedRequest](https://docs.ldap.com/ldap-sdk/docs/javadoc/index.html?com/unboundid/ldap/sdk/unboundidds/extensions/GetPasswordQualityRequirementsExtendedRequest.html)

* [GetPasswordQualityRequirementsExtendedResult](https://docs.ldap.com/ldap-sdk/docs/javadoc/index.html?com/unboundid/ldap/sdk/unboundidds/extensions/GetPasswordQualityRequirementsExtendedResult.html)

* [GetPasswordQualityRequirementsExtendedOperation]()

The API method exists to serves as a translation layer between the client's HTTP request and Directory's internal LDAP operations. For more information on the LDAP Get Password Quality Requirements extended operation, refer to the LDAP [GetPasswordQualityRequirementsExtendedRequest](https://docs.ldap.com/ldap-sdk/docs/javadoc/index.html?com/unboundid/ldap/sdk/unboundidds/extensions/GetPasswordQualityRequirementsExtendedRequest.html) documentation. The LDAP get password quality requirements extended request has an OID of "1.3.6.1.4.1.30221.2.6.43".

---

---
title: Get Schema for the objectclass
description: Retrieve the schema associated with a specified objectClass value using the PingDirectory Directory REST API
component: pingdirectory
page_id: pingdirectory:directory:schemas-apis/get-schema-for-the-objectclass
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/schemas-apis/get-schema-for-the-objectclass.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Get Schema for the objectclass

##

```none
GET {{apiPath}}/directory/v1/schemas/ubidPerson
```

The `GET /directory/v1/schemas/{objectclass}` endpoint returns the `schema` associated with the `objectClass` value of `ubidPerson` specified in the request URL.

### Headers

Authorization      Bearer {{accessToken}}

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/directory/v1/schemas/ubidPerson' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/directory/v1/schemas/ubidPerson")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Authorization", "Bearer {{accessToken}}");
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/directory/v1/schemas/ubidPerson"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
GET /directory/v1/schemas/ubidPerson HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/directory/v1/schemas/ubidPerson")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/directory/v1/schemas/ubidPerson",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Authorization": "Bearer {{accessToken}}"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{apiPath}}/directory/v1/schemas/ubidPerson',
  'headers': {
    'Authorization': 'Bearer {{accessToken}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{apiPath}}/directory/v1/schemas/ubidPerson"

payload = {}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/directory/v1/schemas/ubidPerson');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Authorization' => 'Bearer {{accessToken}}'
));
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "net/http"

url = URI("{{apiPath}}/directory/v1/schemas/ubidPerson")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/directory/v1/schemas/ubidPerson")!,timeoutInterval: Double.infinity)
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "GET"

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

200 OK

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "ubidPerson",
    "classType": "structural",
    "parent": "top",
    "required": [
        "objectClass"
    ],
    "type": "object",
    "properties": {
        "objectClass": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "contains": {
                "const": "ubidPerson"
            },
            "description": "New objects of this type must include the 'ubidPerson' objectClass value. Returned entries will include the complete objectClass hierarchy: [top, ubidPerson]"
        },
        "audio": {
            "type": "array",
            "items": {
                "type": "string",
                "format": "Octet String"
            }
        },
        "authPassword": {
            "type": "array",
            "items": {
                "type": "string",
                "format": "Authentication Password Syntax"
            },
            "description": "password authentication information"
        },
        "businessCategory": {
            "type": "array",
            "items": {
                "type": "string",
                "format": "Directory String"
            }
        },

        ...

    "additionalProperties": false,
    "_links": {
        "self": {
            "href": "https://ds.example.com/directory/v1/schemas/ubidPerson"
        },
        "parent": {
            "href": "https://ds.example.com/directory/v1/schemas/top"
        }
    }
}
```

---

---
title: Getting Started
description: Authenticate requests to the PingDirectory REST API with basic auth or OAuth 2.0 bearer tokens, map OAuth scopes to ACIs, and sync PingDirectoryProxy encryption settings.
component: pingdirectory
page_id: pingdirectory:directory:getting-started/index
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/getting-started/index.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-14
section_ids:
  authentication-types: Authentication types
  access-control: Access control
  create-the-request: Create the request
  request-header: Request header
  request-body: Request body
---

# Getting Started

Requesters can authenticate using any of two authentication types, and the requester may have either a privileged or unprivileged identity that determines the activity scope.

## Authentication types

The Directory REST API supports the following authentication types:

* **Basic authentication**

  Requests are authenticated using a username and password or an encoded API token contained in the `Authorization` header. The user credentials can be collected interactively from the user, or they can represent the client itself.

  Here is a sample of a request using an API token:

  ```none
  GET /directory/v1/uid=lindajones,ou=people,dc=example,dc=com HTTP/1.1
  Authorization: Basic dWlkPXVzZXIuMCxvdT1wZW9wbGUsZGM9ZXhhbXBsZSxkYz1jb206cGFzc3dvcmQ=
  ```

* **Bearer token**

  Requests are authenticated using an access token contained in the `Authorization` header. The access token is obtained through an authorization server, such as PingFederate. Here is a sample:

  ```none
  GET /directory/v1/uid=lindajones,ou=people,dc=example,dc=com HTTP/1.1
  Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtp...
  ```

  When bearer token authentication is used, the access token used must include a scope that the directory service is configured to accept. Additionally, the directory service may be configured to require that the access token include a specific audience claim.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | When using a proxied configuration, PingDirectoryProxy can forward OAuth scopes to PingDirectory for REST API requests that use OAuth bearer tokens. For this to work, both the proxy and the target servers must use identical encryption settings definitions.If their settings differ, you must export the definition from the proxy server and import it into the target servers. For more information, refer to [Exporting encryption settings definitions](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_export_encryption_settings_defs.html) and [Importing encryption settings definitions](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_import_encryption_settings_defs.html). |

  You can define ACIs in PingDirectory that map to specific scopes. When users make requests to Directory REST API endpoints using OAuth 2.0 bearer tokens that include configured scopes, PingDirectory can apply the ACIs associated with those scopes and grant the appropriate permissions.

## Access control

To help isolate access to admin credentials in authentication workflows, you can use OAuth scopes to enforce access control instructions (ACIs) for users authenticating to specific Directory REST API endpoints.

Invoking ACIs using OAuth scopes applies to all REST API endpoints except for the following:

* `GET /directory/v1/`

* `GET /directory/v1/schemas`

* `GET /directory/v1/schemas/{schema}`

Making requests to the Directory REST API with a given user is similar to making an LDAP request with the same user and is subject to the same ACI restrictions. Authenticated users can have full or partial access to the Directory service based on the permissions allowed for that user. In other words, scopes are granted dynamically, and are not explicitly stated in the bearer token. The client sending the bearer token in their request is granted permissions by the access token validator at the time of the request.

To enable this feature, define the ACIs to include the desired OAuth scopes. The following example allows all authenticated users with the OAuth scope `example:scope` to perform the Get Password Quality Requirements extended operation:

```none
(extop="1.3.6.1.4.1.30221.2.6.43")(version 3.0; acl "Extended op permissions for get password quality requirements"; allow (read) oauthscope="example:scope";)
[source]
```

Learn more in [Managing the Directory REST API](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_directory_rest_api.html) and [Using OAuth scopes for ACI rules with the REST API](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_use_oauth_scopes_aci_rest_api.html) in the PingDirectory admin guide.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For security reasons, the PingDirectory REST API never returns the `userPassword` or `authPassword` properties in a response. For example, if you set a user's password using `PUT` with `"userPassword": ["passw0rd"]`, the response does not show the userPassword property or its value. Likewise, if you run a `GET` request with `includeAttribute = userPassword`, the response does not include the `userPassword` property or its value. |

## Create the request

The following information illustrates how to construct a typical API request.

### Request header

The API request header contains the authentication information you must provide to make a call to any Directory REST API resource. The `Authorization` parameter takes the user credentials or the full bearer token as its value, which contains the authorization information needed to access the requested resource.

The following sample shows the API request header (`-H 'Authorization: Bearer`) with a base64url-encoded bearer token as its parameter value.

```none
curl -X "GET" "https://<server>/directory/v1/{{dn}}" \
     -H 'Content-Type: application/json' \
     -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'
[source]
```

The request header also shows an additional parameter or note:

* `Content-Type`

  In the header of a `PATCH`, `PUT`, or `POST` request, this parameter identifies the media type of the request data sent to the server. For most Directory API calls, the Content-Type is `application/json`.

### Request body

The API request body for `POST`, `PATCH`, or `PUT` requests provides the attribute values needed to complete the *create* or *update* operation. For example, to update an LDAP entry, the `PUT` operation requires values for the `attr1` and `attr2` attributes in the request body:

```none
{
  "attr1": "value1",
  "attr2": "value2"
}
```

---

---
title: Hard delete request control
description: Add the hard delete request control to a Directory REST API delete request to override soft delete policies and permanently remove an entry
component: pingdirectory
page_id: pingdirectory:directory:controls/hard-delete-request-control
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/controls/hard-delete-request-control.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Hard delete request control

This control can be included in a [delete request](../directory-entry-apis/delete-an-entry-with-controls.html) to override any soft delete policies and remove the target entry from the server completely. Learn more about soft delete policies in [Soft delete request control](soft-delete-request-control.html).

The following example shows the JSON encoding for the control:

```json
{
    "oid":"1.3.6.1.4.1.30221.2.5.22",
    "control-name":"Hard Delete Request Control",
    "criticality":true,
}
```

---

---
title: Ignore NO-USER-MODIFICATION request control
description: Add the ignore NO-USER-MODIFICATION request control to a Directory REST API add request to set attributes marked NO-USER-MODIFICATION in the schema
component: pingdirectory
page_id: pingdirectory:directory:controls/ignore-no-user-modification-request-control
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/controls/ignore-no-user-modification-request-control.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Ignore NO-USER-MODIFICATION request control

The proprietary ignore NO-USER-MODIFICATION request control may be included in an add request to indicate that the server should allow the client to set all of the provided attributes, even if some of the attribute types are defined with the NO-USER-MODIFICATION constraint in the schema. The control has an OID of 1.3.6.1.4.1.30221.2.5.5, and it does not take a value.

The following sample shows the JSON encoding for the control:

```json
{
    oid":"1.3.6.1.4.1.30221.2.5.5",
    "control-name":"Ignore NO-USER-MODIFICATION Request Control",
    "criticality":false
}
```

---

---
title: Intermediate client request control
description: Add the intermediate client request control to a Directory REST API request to pass downstream client information or an alternate authorization identity
component: pingdirectory
page_id: pingdirectory:directory:controls/intermediate-client-request-control
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/controls/intermediate-client-request-control.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Intermediate client request control

The proprietary intermediate client request control may be included in any type of request, and may serve a few different purposes:

* It may indicate that the request originated from a downstream client, in which case the control may provide additional information about interaction with that client and any other intermediate systems.

* It indicates that the server should provide information about its processing of the operation (along with information from any other upstream servers) that can be used to correlate information about the processing of the operation across multiple systems.

* It can be used to request that the operation be processed with an alternative authorization identity. In this respect, it is similar to the proxied authorization v1 or v2 request control, except the intermediate client control allows multiple authorization requests to be nested.

The intermediate client request control has an OID of 1.3.6.1.4.1.30221.2.5.2, and it takes a value. The following fields may be present in the `value-json` representation of the value:

* `downstream-request`: An optional JSON object field whose value is the representation of information from a downstream client. If present, the fields that may be included in this JSON object are the same fields that may be included in the `value-json` object of the intermediate client request control (optionally including yet another nested `downstream-request` field).

* `downstream-client-address`: An optional string field whose value is the address of the immediate client from which the request was received. For example, the Directory Proxy Server uses this field to pass the address of the end LDAP client to the backend Directory Server used to process the request.

* `downstream-client-secure`: An optional Boolean field whose value indicates whether communication with the immediate downstream client is using a secure channel. For example, the Directory Proxy Server uses this field to indicate to the backend Directory Server whether the communication between the end LDAP client and the Directory Proxy Server is secure.

* `client-identity`: An optional string field whose value contains the authorization identity of a user under whose authority the operation should be processed. For example, the Directory Proxy Server uses this field to indicate that the operation should be processed using the authorization identity of the end LDAP client rather than as the account the Directory Proxy Server uses to authenticate itself to the backend Directory Server.

* `client-name`: An optional string field whose value contains the name of the application that generated this control. For example, the Directory Proxy Server uses this field to indicate that the request has passed through the Directory Proxy Server.

* `client-session-id`: An optional string field whose value contains an identifier that this client is using to reference the current communication session with a downstream client. For example, the Directory Proxy Server uses this field to hold the connection ID that it has assigned to the connection it is using to communicate with the end LDAP client.

* `client-request-id`: An optional string field whose value contains an identifier that this client is using to reference the current request from a downstream client. For example, the Directory Proxy Server uses this field to hold the operation ID it has assigned to the operation being forwarded to the backend Directory Server.

The following sample shows the JSON encoding for the control:

```json
{
    "oid":"1.3.6.1.4.1.30221.2.5.2",
    "control-name":"Intermediate Client Request Control",
    "criticality":false,
    "value-json": {
        "downstream-client-address":"1.2.3.4",
        "downstream-client-secure":true,
        "client-identity":"dn:uid=jdoe,ou=People,dc=example,dc=com",
        "client-name":"PingDirectoryProxy",
        "client-session-id":"conn=1234",
        "client-request-id":"op=56"
    }
}
```

---

---
title: Intermediate client response control
description: Read the intermediate client response control in a Directory REST API response for processing information from the current and upstream servers
component: pingdirectory
page_id: pingdirectory:directory:controls/intermediate-client-response-control
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/controls/intermediate-client-response-control.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Intermediate client response control

This control may be included the response to a request that contains an intermediate client request control, and it may be used to provide information about the processing performed by the current server and any upstream servers. The control has an OID of 1.3.6.1.4.1.30221.2.5.2, and it takes a value. The following fields may be present in the `value-json` representation of the value:

* `upstream-response`: An optional JSON object field whose value provides information about processing performed by a server that is upstream from the one with which the client is communicating. If present, the fields of this JSON object are the same as the fields of the `value-json` object (potentially including another nested `upstream-response` object).

* `upstream-server-address`: An optional string field whose value is the address of an upstream server to which the requested operation was forwarded. For example, if the Directory Proxy Server receives a request that contains an intermediate client request control, it will use this field in the intermediate client response control it returns to provide the address of the backend Directory Server to which the operation was forwarded.

* `upstream-server-secure`: An optional Boolean field used to indicate whether communication with an upstream server occurred over a secure communication channel. For example, if the Directory Proxy Server receives a request that contains an intermediate client request control, it will use this field in the intermediate client response control it returns to indicate whether its communication with the backend Directory Server is secure.

* `server-name`: An optional string field whose value is the name of the application used to process the request. For example, the Directory Server uses this field to indicate that the operation was processed by the Directory Server.

* `server-session-id`: An optional string field whose value is an identifier that the server has assigned to the communication session with the downstream client. For example, the Directory Server uses this field to specify the connection ID it has assigned to the client connection.

* `server-response-id`: An optional string whose value is an identifier that the server has assigned to the request from the downstream client. For example, the Directory Server uses this field to specify the operation ID it has assigned to the client request.

The following represents an example JSON encoding for the control:

```json
{ "oid":"1.3.6.1.4.1.30221.2.5.2",
  "control-name":"Intermediate Client Response Control",
  "criticality":false,
  "value-json":{ "server-name":"PingDirectory",
                 "server-session-id":"conn=1234",
                 "server-request-id":"op=56" } }
```

---

---
title: Join request control
description: Add the join request control to a Directory REST API search request to return related entries alongside each search result entry
component: pingdirectory
page_id: pingdirectory:directory:controls/join-request-control
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/controls/join-request-control.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Join request control

The proprietary join request control can be included in a search request to indicate that each search result entry may include a corresponding join result control with information from one or more other entries that are in some way related to (for example, "joined with") that search result entry. The control has an OID of 1.3.6.1.4.1.30221.2.5.9, and it takes a value. The following fields may be present in the `value-json` representation of the value:

* `join-rule`: A mandatory JSON object field that provides the primary criteria to use when selecting entries to be joined with each search result entry. This is described in detail below.

* `base-dn-type`: A mandatory string field that indicates how the server should determine the base DN to use for joined entries. Only entries matching or below the join base DN (and within the join scope) may be joined with search result entries. This field must have one of the following values:

  * `use-search-base-dn` : Indicates that the server should use the base DN from the associated search request as the join base DN.

  * `use-source-entry-dn`: Indicates that the server should use the DN of the associated search result entry as the join base DN.

  * `use-custom-base-dn`: Indicates that the server should use the specific base DN specified in the base-dn-value field as the join base DN.

* `base-dn-value`: An optional string field whose value is the base DN that should be used for joined entries. This field must be present if the `base-dn-type` value is `use-custom-base-dn`; otherwise, it must be absent.

* `scope`: An optional string field whose value is the scope to use for joined entries. If this is not provided, then the scope from the associated search request will be used. Otherwise, it must have one of the following values (which match the allowed searchScope values in the Directory REST API):

  * `baseObject`: Indicates that only the entry specified as the join base DN may be joined with the search result entry.

  * `singleLevel`: Indicates that only entries immediately below the join base DN (but not the join base entry itself, nor any entries more than one level below it) may be joined with the search result entry.

  * `wholeSubtree`: Indicates that the join base entry or any of its subordinates (to any depth) may be joined with the search result entry.

  * `subordinateSubtree`: Indicates that any entries below the join base entry (to any depth), but not the join base entry itself, may be joined with the search result entry.

* `alias-dereferencing-behavior`: An optional string field whose value is the behavior to use when dereferencing any aliases encountered during join processing. Note that while the LDAP version of the join request control does allow this element to be present, the Ping Identity Directory Server does not support aliases, so it has no purpose and should generally be omitted. However, if a value is provided, then its value must be one of "neverDerefAliases", "derefInSearching", "derefInFindingBaseObj", or "derefAlways".

* `size-limit`: An optional integer field that specifies the maximum number of entries that may be joined with any single search result entry. If this is not specified, the size limit from the search request will be used as the join size limit. Note that the server will impose a maximum join size limit of no more than 1000 entries (and possibly smaller than that, based on resource limits in place for the requester), so the server may use a smaller size limit than the one requested by the client.

* `filter`: An optional string field whose value is the string representation of a search filter that entries will be required to match in order to be joined with a search result entry.

* `attributes`: An optional array field whose values are strings that represent the names of the attributes that should be included in joined entries. If this field is not provided, or if its value is an empty array, then the server behaves as if all user attributes and no operational attributes had been requested.

* `require-match`: A mandatory Boolean field that indicates whether a search result entry will be required to be joined with one or more other entries to be included in the set of search results. If this field has a value of `true`, then a search result entry that is not joined with any other entries will not be returned to the client. If this field has a value of `false`, then search result entries that match the original search request criteria may be returned even if they are not joined with any other entries.

* `nested-join`: An optional JSON object field that may be used to specify nested join criteria, in which each joined entry may itself be joined with other entries. If this is specified, then the fields of this JSON object are the same as those that may be used in the `value-json` element (including another `nested-join` field if desired).

The main criteria used to identify entries that should be joined with each search result entry is specified using the join rule. The supported join rule types are:

* `DN Join`: Indicates that the search result entry includes an attribute whose values are the DNs of the entries to be joined with it. If this type of join is to be used, then the `join-rule` JSON object may include the following fields:

  * `type`: A mandatory string field that indicates the join rule type. For a DN join, the value must be "dn".

  * `source-attribute`: A mandatory string field whose value is the name of the attribute in the source entry whose values are the DNs of the entries to be joined with that entry.

* `Reverse DN Join`: Indicates that the entries to be joined with a search result entry include an attribute in which one of the values is the DN of the search result entry. If this type of join is to be used, then the `join-rule` JSON object may include the following fields:

  * `type`: A mandatory string field that indicates the join rule type. For a reverse DN join, the value must be "reverse-dn".

  * `target-attribute`: A mandatory string field whose value is the name of the attribute in the entries to be joined in which one of the values is the DN of the source entry.

* `Equality Join`: Indicates that the entries to be joined with a search result entry must include an attribute with a value that matches the value of a corresponding attribute in the source entry. If this type of join is to be used, then the `join-rule` JSON object may include the following fields:

  * `type`: A mandatory string field that indicates the join rule type. For an equality join, the value must be "equality".

  * `source-attribute`: A mandatory string field whose value is the name of the attribute in the source entry that must have at least one value that matches a value in the target attribute.

  * `target-attribute`: A mandatory string field whose value is the name of the attribute in the entries to be joined that must match at least one value from the source attribute.

  * `match-all`: A mandatory Boolean field that indicates how to handle multi-valued source attributes. If this field has a value of `true`, then an entry will be joined with the source entry only if the target attribute contains all of the values of the source attribute. If it has a value of `false`, then an entry may be joined with the source entry as long as at least one of the values of the source attribute is present in the target attribute.

* `Contains Join`: Indicates that the entries to be joined with a search result entry must include an attribute with a value that contains (or is equal to) a value from a corresponding attribute in the source entry. That is, at least one value from an attribute in the source entry must be a substring of a value of a specified attribute in the target entry. If this type of join is to be used, then the `join-rule` JSON object may include the following fields:

  * `type`: A mandatory string field that indicates the join rule type. For a contains join, the value must be "contains".

  * `source-attribute`: A mandatory string field whose value is the name of the attribute in the source entry that must have at least one value that matches or is a substring of a value in the target attribute.

  * `target-attribute`: A mandatory string field whose value is the name of the attribute in the entries to be joined that must contain at least one value that matches or contains a substring that matches a value from the source entry.

  * `match-all`: A mandatory Boolean field that indicates how to handle multi-valued source attributes. If this field has a value of `true`, then an entry will be joined with the source entry only if the target attribute contains has values in which all of the source attribute values are present as substrings. If this field is absent, or if it is present with a value of `false`, then an entry may be joined with the source entry as long as at least one of the values of the target attribute contains at least one of the values of the source attribute as a substring.

* `AND Join`: Indicates that the entries to be joined with a search result entry must match multiple sets of nested join rules. If this type of join is to be used, then the `join-rule` JSON object may include the following fields:

  * `type`: A mandatory string field that indicates the join rule type. For an AND join, the value must be "and".

  * `rules`: A mandatory, non-empty array field whose values are JSON objects that represent the nested join rules that will all be required to match a given entry for that entry to be joined with the source entry.

* `OR Join`: Indicates that the entries to be joined with a search result entry must match at least one of a given set of nested join rules. If this type of join is to be used, then the `join-rule` JSON object may include the following fields:

  * `type`: A mandatory string field that indicates the join rule type. For an OR join, the value must be "or".

  * `rules`: A mandatory, non-empty array field whose values are JSON objects that represent the nested join rules of which at least one must match a given entry for that entry to be joined with the source entry.

The following sample shows the JSON encoding for the control:

```json
{
    "oid":"1.3.6.1.4.1.30221.2.5.9",
    "control-name":"Join Request Control",
    "criticality":false,
    "value-json": {
        "join-rule": {
            "type":"dn",
            "attribute":"manager"
        },
        "base-dn-type":"use-custom-base-dn",
        "base-dn-value":"ou=People,dc=example,dc=com",
        "scope":"wholeSubtree",
        "size-limit":10,
        "attributes": [
            "givenName",
            "sn",
            "cn",
            "mail"
        ],
        "require-match":false
    }
}
```

---

---
title: Join result control
description: Read the join result control returned with a search result entry to get the set of entries joined with it
component: pingdirectory
page_id: pingdirectory:directory:controls/join-result-control
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/controls/join-result-control.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Join result control

This control can be included in a search result entry in response to a join request control in order to provide a set of entries that are related to that search result entry. The control has an OID of 1.3.6.1.4.1.30221.2.5.9, and it takes a value. The following fields may be present in the `value-json` representation of the value:

* `result-code`: An integer field whose value is the numeric representation of the LDAP result code for the join processing.

* `matched-dn`: An optional string field that can be used to provide a matched DN for the join processing. If the join base entry does not exist, this may be the closest ancestor to that entry that actually does exist.

* `diagnostic-message`: An optional string field that can be used to provide additional information about the join processing.

* `referral-urls`: An optional array field whose values are strings that represent referral URLs encountered while resolving the join base entry.

* `joined-entries`: An array field whose values are JSON objects that represent entries that were joined with the search result entry. The format of these JSON objects is essentially the same as the format used for search result entries in the Directory REST API, with the string "`_dn`" field used to hold each entry's DN, and a separate string array field for each attribute in the entry. If there are nested join results, then the "`_nested-join-results`" array field may provide a set of JSON objects whose values are the entries joined with that join entry, using the same fields as the joined-entries field (including another "`_nested-join-results`" field, if appropriate).

The following represents an example JSON encoding for the control:

```json
{ "oid":"1.3.6.1.4.1.30221.2.5.9",
  "control-name":"Join Result Control",
  "criticality":false,
  "value-json":{ "result-code":0,
                 "joined-entries":[ { "_dn":"uid=jdoe,ou=People,dc=example,dc=com",
                                      "uid":[ "jdoe" ],
                                      "givenName":[ "John" ],
                                      "sn":[ "Doe" ],
                                      "cn":[ "John Doe" ],
                                      "mail":[ "jdoe@example.com" ] } ] } }
```

---

---
title: List All Entries
description: Retrieve a paginated list of entries under a subtree of an entry with a specified search scope using the PingDirectory Directory REST API
component: pingdirectory
page_id: pingdirectory:directory:subtree-apis/list-all-entries
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/subtree-apis/list-all-entries.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# List All Entries

##

```none
GET {{apiPath}}/directory/v1/{{dn}}/subtree?searchScope=wholeSubtree&limit=100
```

To retrieve a list of entries under a subtree of an entry, use the `{{dn}}/subtree` endpoint. This endpoint requires the `searchScope` parameter. The supported search scopes are:

* `baseObject`

  Returns only the object directly described by the base DN.

* `singleLevel`

  Returns only the entries that are immediate children of the base entry.

* `wholeSubtree`

  Returns the base entry and all of its descendants.

* `subordinateSubtree`

  Returns the descendants of the base entry, but not the base entry itself.

All list requests are paged. The `limit` parameter specifies the page size. However, the page size can be smaller than requested, either because the server has a configured maximum page size or because you have reached the last page and there are not enough entries to fill the page.

The `next` link enables navigation forward from the current page to the next page. The directory service does not support a `previous` link to move backward from the current page.

The `size` value on the returned object shows the actual number of entries returned in the request.

The sample shows the `GET /directory/v1/{{dn}}/subtree+` operation to return the base entry and all of its descendants.

|   |                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `searchScope` parameter value is encoded in the cursor parameter in the next link URL. The search scope does not need to be provided on subsequent requests. This endpoint also accepts the `includeAttributes` and `excludeAttributes` query parameters. For more information about these query parameters, refer to [Get an entry](../directory-entry-apis/get-an-entry.html). |

### Headers

Authorization      Bearer {{accessToken}}

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope=wholeSubtree&limit=100' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope=wholeSubtree&limit=100")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Authorization", "Bearer {{accessToken}}");
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope=wholeSubtree&limit=100"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
GET /directory/v1/{{dn}}/subtree?searchScope=wholeSubtree&limit=100 HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope=wholeSubtree&limit=100")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope=wholeSubtree&limit=100",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Authorization": "Bearer {{accessToken}}"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope=wholeSubtree&limit=100',
  'headers': {
    'Authorization': 'Bearer {{accessToken}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope=wholeSubtree&limit=100"

payload = {}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope=wholeSubtree&limit=100');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Authorization' => 'Bearer {{accessToken}}'
));
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "net/http"

url = URI("{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope=wholeSubtree&limit=100")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope=wholeSubtree&limit=100")!,timeoutInterval: Double.infinity)
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "GET"

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

200 OK

```json
{
  "size": 100,
  "_embedded": {
    "entries": [
      {
        "_dn": "uid=lindajones,ou=people,dc=example,dc=com",
        "objectClass": [ "top", "person", "organizationalPerson", "inetOrgPerson" ],
        "uid": ["lindajones"],
        "cn": ["Linda Jones"],
        "sn": ["Jones"],
        "_links": {
          "schemas": [
            {
              "href": "https://ds.example.com/directory/v1/schemas/inetOrgPerson"
            }
          ],
          "self": {
            "href": "https://ds.example.com/directory/v1/uid=lindajones,ou=people,dc=example,dc=com"
          }
        }
      },

      ... 99 more entries ...

    ]
  },
  "_links": {
    "self": {
      "href": "https://ds.example.com/directory/v1/ou=people,dc=example,dc=com/subtree?searchScope=wholeSubtree&limit=100"
    },
    "next": {
      "href": "https://ds.example.com/directory/v1/ou=people,dc=example,dc=com/subtree?limit=100&cursor=eyJjb29raWUiOiJ1c2VyMTAiLCJmaWx0ZXIiOiIiLCJzY29wZSI6Indob2xlU3VidHJlZSJ9"
    }
  }
}
```

---

---
title: List All Entries (Filter Entries)
description: Filter subtree search results using a SCIM filter parameter with the PingDirectory Directory REST API
component: pingdirectory
page_id: pingdirectory:directory:subtree-apis/list-all-entries-filter-entries
canonical_url: https://developer.pingidentity.com/pingdirectory/directory/subtree-apis/list-all-entries-filter-entries.html
llms_txt: https://developer.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# List All Entries (Filter Entries)

##

```none
GET {{apiPath}}/directory/v1/{{dn}}/subtree?searchScope%3DwholeSubtree%26filter%3DobjectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22
```

The `GET /directory/v1/{{dn}}/subtree` endpoint supports a SCIM filtering parameter to limit the returned result set to those entries meeting the specified criteria. For example, the request below uses the filter `objectClass eq "person" and sn eq "Jones"` to search for all people with the last name of `Jones`.

```none
curl -X "GET" "https://ds.example.com/directory/v1/ou=people,dc=example,dc=com/subtree?searchScope=wholeSubtree&filter=objectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22" \
-H 'Content-type: application/json' \
-H 'Authorization: Bearer accessToken'
```

In the Authorization request header field, the `accessToken` value is your full base64url-encoded JSON web token generated by the authentication service.

Filtering is done before pagination of the response data. The filter parameter is encoded into the `cursor` pagination parameter; it only needs to be provided in the first request.

For more information about filtering, refer to [Conventions](../conventions.html).

### Headers

Authorization      Bearer {{accessToken}}

##

### Example Request

* cURL

* C#

* Go

* HTTP

* Java

* jQuery

* NodeJS

* Python

* PHP

* Ruby

* Swift

```shell
curl --location --globoff '{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope%3DwholeSubtree%26filter%3DobjectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22=' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope%3DwholeSubtree%26filter%3DobjectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22=")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Authorization", "Bearer {{accessToken}}");
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);
```

```golang
package main

import (
  "fmt"
  "net/http"
  "io"
)

func main() {

  url := "{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope%3DwholeSubtree%26filter%3DobjectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22="
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer {{accessToken}}")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

```http
GET /directory/v1/{{dn}}/subtree?searchScope%3DwholeSubtree%26filter%3DobjectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22= HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope%3DwholeSubtree%26filter%3DobjectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22=")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope%3DwholeSubtree%26filter%3DobjectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22=",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Authorization": "Bearer {{accessToken}}"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope%3DwholeSubtree%26filter%3DobjectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22=',
  'headers': {
    'Authorization': 'Bearer {{accessToken}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope%3DwholeSubtree%26filter%3DobjectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22="

payload = {}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope%3DwholeSubtree%26filter%3DobjectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22=');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Authorization' => 'Bearer {{accessToken}}'
));
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```

```ruby
require "uri"
require "net/http"

url = URI("{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope%3DwholeSubtree%26filter%3DobjectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22=")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/directory/v1/{{dn}}/subtree?searchScope%3DwholeSubtree%26filter%3DobjectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22=")!,timeoutInterval: Double.infinity)
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "GET"

let task = URLSession.shared.dataTask(with: request) { data, response, error in
  guard let data = data else {
    print(String(describing: error))
    return
  }
  print(String(data: data, encoding: .utf8)!)
}

task.resume()
```

### Example Response

200 OK

```json
{
    "_links": {
        "self": {
            "href": "https://ds.example.com/directory/v1/ou=people,dc=example,dc=com/subtree?searchScope=wholeSubtree&ldapFilter=objectClass%20eq%20%22person%22%20and%20sn%20eq%20%22Jones%22"
        }
    },
    "size": 1,
    "_embedded": {
        "entries": [
            {
                "_dn": "uid=lindajones,ou=people,dc=example,dc=com",
                "objectClass": [
                    "top",
                    "person",
                    "organizationalPerson",
                    "inetOrgPerson"
                ],
                "uid": [
                    "lindajones"
                ],
                "cn": [
                    "Linda Jones"
                ],
                "sn": [
                    "Jones"
                ],
                "_links": {
                    "schemas": [
                        {
                            "href": "https://ds.example.com/directory/v1/schemas/inetOrgPerson"
                        }
                    ],
                    "self": {
                        "href": "https://ds.example.com/directory/v1/uid=lindajones,ou=people,dc=example,dc=com"
                    }
                }
            }
        ]
    }
}
```